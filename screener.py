"""Cross-venue perpetual funding rate screener.

Pulls current funding rates from Binance, Bybit, OKX, and Bitget (USDT-margined
perps only), annualizes them, and writes three markdown tables back into README:

  1. Top 10 highest funding (longs paying premium)
  2. Top 10 lowest / most negative funding (shorts paying premium)
  3. Top 10 biggest cross-venue spreads (same symbol, different venue)

Designed to run on a GitHub Actions 8-hour cron aligned with funding settlement
(00:00 / 08:00 / 16:00 UTC). No API keys required.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import ccxt

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
HISTORY_DIR = DATA_DIR / "history"
README = ROOT / "README.md"

VENUES = ["binance", "bybit", "okx", "bitget"]
QUOTE = "USDT"
ANNUALIZE = 3 * 365  # funding settles every 8h → 3 settlements/day × 365


def normalize_symbol(market: dict) -> str | None:
    """Extract base coin for a USDT-margined linear perp; None if not eligible."""
    if not market.get("swap") or not market.get("linear"):
        return None
    if market.get("quote") != QUOTE:
        return None
    if market.get("settle") and market["settle"] != QUOTE:
        return None
    return market.get("base")


def fetch_venue(venue_id: str) -> dict[str, float]:
    """Return {base_coin: annualized_funding_pct} for a venue. Returns empty on failure."""
    out: dict[str, float] = {}
    try:
        ex = getattr(ccxt, venue_id)({"enableRateLimit": True, "timeout": 30_000})
        ex.options["defaultType"] = "swap"
        ex.load_markets()
        rates = ex.fetch_funding_rates()
    except Exception as e:
        msg = str(e).splitlines()[0][:160]
        print(f"  [{venue_id}] unavailable: {msg}", file=sys.stderr)
        return out
    for sym, payload in rates.items():
        market = ex.market(sym) if sym in ex.markets else None
        if market is None:
            continue
        base = normalize_symbol(market)
        if base is None:
            continue
        rate = payload.get("fundingRate")
        if rate is None:
            continue
        try:
            out[base] = float(rate) * ANNUALIZE * 100  # to %/yr
        except (TypeError, ValueError):
            continue
    return out


def collect() -> dict[str, dict[str, float]]:
    """Returns {venue: {base: annualized_pct}}."""
    result: dict[str, dict[str, float]] = {}
    for v in VENUES:
        print(f"Fetching {v}...")
        data = fetch_venue(v)
        print(f"  {v}: {len(data)} symbols")
        result[v] = data
    return result


def flatten(snapshot: dict[str, dict[str, float]]) -> list[tuple[str, str, float]]:
    """Yield (venue, base, rate) tuples."""
    rows: list[tuple[str, str, float]] = []
    for venue, rates in snapshot.items():
        for base, rate in rates.items():
            rows.append((venue, base, rate))
    return rows


def fmt_rate(rate: float) -> str:
    sign = "+" if rate >= 0 else ""
    return f"{sign}{rate:.2f}%"


def table_top_high(rows: list[tuple[str, str, float]], n: int = 10) -> str:
    rows_sorted = sorted(rows, key=lambda r: r[2], reverse=True)[:n]
    lines = [
        "| Rank | Symbol | Venue | Funding (annualized) |",
        "|------|--------|-------|---------------------:|",
    ]
    for i, (v, b, r) in enumerate(rows_sorted, 1):
        lines.append(f"| {i} | {b} | {v} | {fmt_rate(r)} |")
    return "\n".join(lines)


def table_top_low(rows: list[tuple[str, str, float]], n: int = 10) -> str:
    rows_sorted = sorted(rows, key=lambda r: r[2])[:n]
    lines = [
        "| Rank | Symbol | Venue | Funding (annualized) |",
        "|------|--------|-------|---------------------:|",
    ]
    for i, (v, b, r) in enumerate(rows_sorted, 1):
        lines.append(f"| {i} | {b} | {v} | {fmt_rate(r)} |")
    return "\n".join(lines)


def table_top_spreads(
    snapshot: dict[str, dict[str, float]], n: int = 10
) -> str:
    by_symbol: dict[str, dict[str, float]] = {}
    for venue, rates in snapshot.items():
        for base, rate in rates.items():
            by_symbol.setdefault(base, {})[venue] = rate
    spreads: list[tuple[str, float, str, float, str, float]] = []
    for base, venue_rates in by_symbol.items():
        if len(venue_rates) < 2:
            continue
        hi_v, hi_r = max(venue_rates.items(), key=lambda kv: kv[1])
        lo_v, lo_r = min(venue_rates.items(), key=lambda kv: kv[1])
        spread = hi_r - lo_r
        spreads.append((base, spread, hi_v, hi_r, lo_v, lo_r))
    spreads.sort(key=lambda x: x[1], reverse=True)
    spreads = spreads[:n]
    lines = [
        "| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |",
        "|------|--------|-------:|------------|----------:|-----------|---------:|",
    ]
    for i, (b, sp, hv, hr, lv, lr) in enumerate(spreads, 1):
        lines.append(
            f"| {i} | {b} | {fmt_rate(sp)} | {hv} | {fmt_rate(hr)} | {lv} | {fmt_rate(lr)} |"
        )
    return "\n".join(lines)


def save_snapshot(snapshot: dict[str, dict[str, float]]) -> None:
    now = datetime.now(timezone.utc)
    payload = {
        "captured_utc": now.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "venues": snapshot,
    }
    (DATA_DIR / "latest.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    HISTORY_DIR.mkdir(exist_ok=True)
    stamp = now.strftime("%Y-%m-%dT%H%M")
    (HISTORY_DIR / f"{stamp}.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def update_readme(
    top_high: str, top_low: str, top_spreads: str, total_pairs: int
) -> None:
    text = README.read_text(encoding="utf-8")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    venue_str = " · ".join(VENUES)
    stamp_block = (
        f"_Last update: **{now}**  ·  Venues: {venue_str}  ·  "
        f"Pairs scanned: **{total_pairs}**_"
    )
    text = re.sub(
        r"<!-- BEGIN:STAMP -->.*?<!-- END:STAMP -->",
        f"<!-- BEGIN:STAMP -->\n{stamp_block}\n<!-- END:STAMP -->",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"<!-- BEGIN:TOP_HIGH -->.*?<!-- END:TOP_HIGH -->",
        f"<!-- BEGIN:TOP_HIGH -->\n{top_high}\n<!-- END:TOP_HIGH -->",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"<!-- BEGIN:TOP_LOW -->.*?<!-- END:TOP_LOW -->",
        f"<!-- BEGIN:TOP_LOW -->\n{top_low}\n<!-- END:TOP_LOW -->",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"<!-- BEGIN:TOP_SPREADS -->.*?<!-- END:TOP_SPREADS -->",
        f"<!-- BEGIN:TOP_SPREADS -->\n{top_spreads}\n<!-- END:TOP_SPREADS -->",
        text,
        flags=re.DOTALL,
    )
    README.write_text(text, encoding="utf-8")


def main() -> int:
    snapshot = collect()
    rows = flatten(snapshot)
    total = sum(len(v) for v in snapshot.values())
    print(f"\nTotal venue-symbol pairs: {total}")

    th = table_top_high(rows)
    tl = table_top_low(rows)
    ts = table_top_spreads(snapshot)

    save_snapshot(snapshot)
    update_readme(th, tl, ts, total)
    print("README updated, snapshot saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
