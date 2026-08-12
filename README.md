# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-12 03:03 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1172**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FLY | bitget | +198.63% |
| 2 | SNXX | bitget | +138.19% |
| 3 | KORU | bitget | +134.47% |
| 4 | BRKB | okx | +132.44% |
| 5 | FOXA | bitget | +131.29% |
| 6 | XMR | bitget | +114.43% |
| 7 | DRAM | bitget | +107.53% |
| 8 | ARC | bitget | +99.43% |
| 9 | UNITAS | bitget | +91.21% |
| 10 | NG | okx | +88.26% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KAITO | bitget | -1040.47% |
| 2 | RVN | okx | -694.07% |
| 3 | PROM | bitget | -327.62% |
| 4 | FWDI | okx | -326.30% |
| 5 | DOS | bitget | -288.42% |
| 6 | RVN | bitget | -281.96% |
| 7 | KAITO | okx | -261.77% |
| 8 | DEXE | bitget | -179.47% |
| 9 | HYUNDAI | bitget | -121.33% |
| 10 | EUL | bitget | -113.77% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KAITO | +778.70% | okx | -261.77% | bitget | -1040.47% |
| 2 | RVN | +412.11% | bitget | -281.96% | okx | -694.07% |
| 3 | FWDI | +282.06% | bitget | -44.24% | okx | -326.30% |
| 4 | DOS | +203.26% | okx | -85.16% | bitget | -288.42% |
| 5 | FLY | +198.63% | bitget | +198.63% | okx | +0.00% |
| 6 | KORU | +134.47% | bitget | +134.47% | okx | +0.00% |
| 7 | BRKB | +132.44% | okx | +132.44% | bitget | +0.00% |
| 8 | SNXX | +125.49% | bitget | +138.19% | okx | +12.70% |
| 9 | DRAM | +107.53% | bitget | +107.53% | okx | +0.00% |
| 10 | MUU | +79.39% | bitget | +79.39% | okx | +0.00% |
<!-- END:TOP_SPREADS -->

## How to read this

Funding rate is the periodic payment between long and short holders of a perpetual contract, designed to keep the perp price anchored to spot. Conventions:

- **Positive funding** → longs pay shorts. Usually means perp is trading above spot; market is leveraged long.
- **Negative funding** → shorts pay longs. Usually means perp is trading below spot; market is leveraged short.
- **Annualized** = `8h-rate × 3 × 365`. Useful for comparing across instruments and against alternatives like spot lending yield.

A persistent +100% annualized funding on a major perp is unsustainable — either the spot price catches up, or the long crowd unwinds. The same logic applies to deeply negative funding for shorts.

## Methodology

- Data source: `ccxt` against each venue's public funding endpoint (no API keys required).
- Venues: Binance, Bybit, OKX, Bitget — USDT-margined linear perps only.
- Refresh cadence: every 8 hours via GitHub Actions, aligned with the standard 00:00 / 08:00 / 16:00 UTC funding settlement windows.
- Each run writes the full snapshot to `data/latest.json` and an immutable copy to `data/history/YYYY-MM-DDTHHMM.json` for future analysis.

## Running locally

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python screener.py
```

The script will hit the public endpoints (rate-limited, takes ~30 seconds) and update this README in place.

## Caveats

- Funding-rate sign conventions are standardized via ccxt; if a venue changes its API contract, results may temporarily skew. The script will keep running but the table can mislead until ccxt patches the adapter.
- Snapshots are point-in-time. They don't capture intra-period drift or settlement-time jumps. For statistical work, use the `data/history/` archive rather than reading `latest.json` mid-window.
- This is not a strategy. It's a regime gauge.

## Related

- [awesome-derivatives-data](https://github.com/ruleaker/awesome-derivatives-data) — Curated resources for crypto derivatives data (funding, OI, basis, options).
- [awesome-macro-liquidity](https://github.com/ruleaker/awesome-macro-liquidity) — Macro liquidity drivers behind derivatives flows.
- [net-liquidity-dashboard](https://github.com/ruleaker/net-liquidity-dashboard) — Sister tool tracking US Net Liquidity on a daily cron.

## License

[MIT](LICENSE)
