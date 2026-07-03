# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-03 11:06 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1078**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KORU | bitget | +366.17% |
| 2 | KORU | okx | +271.52% |
| 3 | SOXL | okx | +171.17% |
| 4 | COHR | bitget | +139.94% |
| 5 | MUU | bitget | +135.56% |
| 6 | WDC | bitget | +132.82% |
| 7 | MVLL | bitget | +131.95% |
| 8 | RAM | bitget | +128.01% |
| 9 | ASML | okx | +123.93% |
| 10 | AAOI | bitget | +121.22% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 10000NEX | bitget | -1462.48% |
| 2 | ZKP | bitget | -1143.62% |
| 3 | ZKP | okx | -1095.00% |
| 4 | GWEI | bitget | -560.42% |
| 5 | BIRB | bitget | -556.04% |
| 6 | THE | bitget | -475.56% |
| 7 | RPL | bitget | -372.63% |
| 8 | SLX | okx | -296.12% |
| 9 | LAB | okx | -238.92% |
| 10 | LAB | bitget | -232.03% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | PLTR | +215.51% | okx | -0.86% | bitget | -216.37% |
| 2 | SLX | +172.05% | bitget | -124.06% | okx | -296.12% |
| 3 | COHR | +139.94% | bitget | +139.94% | okx | +0.00% |
| 4 | MUU | +135.56% | bitget | +135.56% | okx | +0.00% |
| 5 | WDC | +132.82% | bitget | +132.82% | okx | +0.00% |
| 6 | MVLL | +128.61% | bitget | +131.95% | okx | +3.34% |
| 7 | RAM | +128.01% | bitget | +128.01% | okx | +0.00% |
| 8 | AAOI | +121.22% | bitget | +121.22% | okx | +0.00% |
| 9 | GLW | +107.64% | bitget | +107.64% | okx | +0.00% |
| 10 | NBIS | +102.05% | bitget | +102.05% | okx | +0.00% |
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
