# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-14 20:22 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1250**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +594.35% |
| 2 | NATGAS | bitget | +346.68% |
| 3 | US500 | okx | +122.41% |
| 4 | ONE | bitget | +86.40% |
| 5 | XPD | okx | +84.80% |
| 6 | XPT | okx | +76.62% |
| 7 | NOK | okx | +74.79% |
| 8 | AVGO | bitget | +69.75% |
| 9 | KORU | bitget | +69.09% |
| 10 | SOFTBANK | okx | +66.58% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CNPY | okx | -861.81% |
| 2 | STEEM | bitget | -510.71% |
| 3 | CVC | bitget | -420.70% |
| 4 | BZ | bitget | -329.27% |
| 5 | CL | bitget | -323.90% |
| 6 | BZ | okx | -322.45% |
| 7 | ZIL | okx | -309.15% |
| 8 | CL | okx | -306.39% |
| 9 | POWR | bitget | -277.47% |
| 10 | PUNDIX | bitget | -253.49% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ZIL | +310.35% | bitget | +1.20% | okx | -309.15% |
| 2 | IOST | +174.04% | bitget | -54.42% | okx | -228.47% |
| 3 | APP | +98.18% | bitget | +0.00% | okx | -98.18% |
| 4 | OKTA | +82.62% | bitget | +0.00% | okx | -82.62% |
| 5 | ONE | +80.92% | bitget | +86.40% | okx | +5.47% |
| 6 | SKDD | +70.95% | bitget | -87.71% | okx | -158.66% |
| 7 | UNITREE | +70.71% | bitget | +0.00% | okx | -70.71% |
| 8 | CAP | +67.11% | okx | -168.43% | bitget | -235.53% |
| 9 | SOFTBANK | +66.58% | okx | +66.58% | bitget | +0.00% |
| 10 | KR200 | +64.74% | bitget | -8.87% | okx | -73.61% |
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
