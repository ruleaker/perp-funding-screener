# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-06 10:28 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **951**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ALLO | bitget | +156.69% |
| 2 | NOK | okx | +121.41% |
| 3 | SNDK | okx | +110.77% |
| 4 | SAHARA | bitget | +109.17% |
| 5 | BEAT | bitget | +106.11% |
| 6 | MTL | bitget | +94.06% |
| 7 | EPIC | bitget | +82.56% |
| 8 | MU | okx | +78.06% |
| 9 | LITE | okx | +72.43% |
| 10 | QQQ | okx | +69.02% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | okx | -383.75% |
| 2 | HOME | bitget | -382.05% |
| 3 | GUN | bitget | -288.86% |
| 4 | STABLE | bitget | -219.77% |
| 5 | STABLE | okx | -217.48% |
| 6 | LA | bitget | -178.59% |
| 7 | PROS | bitget | -139.83% |
| 8 | LA | okx | -137.18% |
| 9 | PROS | okx | -119.92% |
| 10 | WLD | okx | -110.26% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ALLO | +157.89% | bitget | +156.69% | okx | -1.19% |
| 2 | SNDK | +110.77% | okx | +110.77% | bitget | +0.00% |
| 3 | SAHARA | +101.83% | bitget | +109.17% | okx | +7.34% |
| 4 | MU | +78.06% | okx | +78.06% | bitget | +0.00% |
| 5 | LITE | +72.43% | okx | +72.43% | bitget | +0.00% |
| 6 | QQQ | +69.02% | okx | +69.02% | bitget | +0.00% |
| 7 | ASTS | +61.25% | bitget | +0.00% | okx | -61.25% |
| 8 | BEAT | +60.01% | bitget | +106.11% | okx | +46.10% |
| 9 | SEI | +59.39% | okx | -20.33% | bitget | -79.72% |
| 10 | NMR | +49.72% | okx | -34.92% | bitget | -84.64% |
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
