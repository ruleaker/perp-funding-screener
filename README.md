# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-05-29 04:51 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **907**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | IBM | okx | +704.63% |
| 2 | AAOI | okx | +476.59% |
| 3 | ESPORTS | bitget | +312.95% |
| 4 | GLW | okx | +308.65% |
| 5 | INFQ | okx | +238.39% |
| 6 | GEV | okx | +179.18% |
| 7 | GME | okx | +161.34% |
| 8 | NBIS | okx | +138.86% |
| 9 | NOK | okx | +121.63% |
| 10 | COHR | okx | +119.22% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ID | bitget | -861.22% |
| 2 | MMT | bitget | -290.61% |
| 3 | DELL | okx | -197.97% |
| 4 | MMT | okx | -155.97% |
| 5 | ASTS | bitget | -109.50% |
| 6 | FLY | bitget | -109.50% |
| 7 | SOXL | bitget | -109.50% |
| 8 | IRYS | bitget | -89.90% |
| 9 | RDW | bitget | -89.46% |
| 10 | BCH | bitget | -74.24% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | AAOI | +367.09% | okx | +476.59% | bitget | +109.50% |
| 2 | NBIS | +138.86% | okx | +138.86% | bitget | +0.00% |
| 3 | MMT | +134.64% | okx | -155.97% | bitget | -290.61% |
| 4 | INFQ | +128.89% | okx | +238.39% | bitget | +109.50% |
| 5 | SOXL | +120.45% | okx | +10.95% | bitget | -109.50% |
| 6 | COHR | +119.22% | okx | +119.22% | bitget | +0.00% |
| 7 | WDC | +91.57% | okx | +91.57% | bitget | +0.00% |
| 8 | BE | +83.81% | bitget | +109.50% | okx | +25.69% |
| 9 | GME | +82.82% | okx | +161.34% | bitget | +78.51% |
| 10 | ACU | +74.13% | okx | +5.47% | bitget | -68.66% |
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
