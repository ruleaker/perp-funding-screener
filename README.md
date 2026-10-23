# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-23 20:00 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1364**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | IRYS | bitget | +1870.04% |
| 2 | IRYS | okx | +1095.00% |
| 3 | AGPU | bitget | +452.34% |
| 4 | BWET | okx | +418.63% |
| 5 | BWET | bitget | +358.83% |
| 6 | NDX100 | bitget | +214.95% |
| 7 | USDESTOCK | bitget | +116.18% |
| 8 | NOKSTOCK | bitget | +102.60% |
| 9 | SIREN | bitget | +80.48% |
| 10 | BAC | bitget | +71.39% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BTW | bitget | -2017.32% |
| 2 | ARK | bitget | -1404.99% |
| 3 | BIRB | bitget | -1175.15% |
| 4 | ALT | bitget | -1153.47% |
| 5 | BTW | okx | -1095.00% |
| 6 | H100 | okx | -476.10% |
| 7 | AXIS | bitget | -465.70% |
| 8 | IOST | okx | -243.11% |
| 9 | AXIS | okx | -237.80% |
| 10 | USO | okx | -154.20% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BTW | +922.32% | okx | -1095.00% | bitget | -2017.32% |
| 2 | IRYS | +775.04% | bitget | +1870.04% | okx | +1095.00% |
| 3 | H100 | +481.57% | bitget | +5.47% | okx | -476.10% |
| 4 | AXIS | +227.91% | okx | -237.80% | bitget | -465.70% |
| 5 | IOST | +205.01% | bitget | -38.11% | okx | -243.11% |
| 6 | AMC | +107.82% | okx | -0.70% | bitget | -108.51% |
| 7 | BWET | +59.80% | okx | +418.63% | bitget | +358.83% |
| 8 | EGLD | +52.59% | bitget | +10.95% | okx | -41.64% |
| 9 | NEO | +47.07% | bitget | +10.51% | okx | -36.55% |
| 10 | APE | +43.66% | bitget | +10.95% | okx | -32.71% |
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
