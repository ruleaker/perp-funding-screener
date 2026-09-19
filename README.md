# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-19 12:36 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1264**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | EGLD | bitget | +953.85% |
| 2 | GPRO | okx | +128.11% |
| 3 | DGAI | okx | +80.71% |
| 4 | US500 | okx | +78.76% |
| 5 | ELSA | bitget | +67.01% |
| 6 | FIGHT | bitget | +66.47% |
| 7 | POWER | bitget | +65.04% |
| 8 | SIREN | bitget | +64.71% |
| 9 | SPCH | okx | +62.56% |
| 10 | FLOCK | okx | +53.82% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AVA | bitget | -325.54% |
| 2 | XTZ | okx | -299.15% |
| 3 | ONE | okx | -236.54% |
| 4 | F | bitget | -216.26% |
| 5 | F | okx | -177.06% |
| 6 | ONE | bitget | -139.17% |
| 7 | LSK | bitget | -120.45% |
| 8 | AKE | okx | -105.57% |
| 9 | IOST | okx | -77.51% |
| 10 | ESP | okx | -74.93% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | EGLD | +942.90% | bitget | +953.85% | okx | +10.95% |
| 2 | XTZ | +226.22% | bitget | -72.93% | okx | -299.15% |
| 3 | GPRO | +128.11% | okx | +128.11% | bitget | +0.00% |
| 4 | ONE | +97.36% | bitget | -139.17% | okx | -236.54% |
| 5 | DGAI | +70.63% | okx | +80.71% | bitget | +10.07% |
| 6 | SPCH | +62.56% | okx | +62.56% | bitget | +0.00% |
| 7 | RAVE | +43.57% | okx | +49.05% | bitget | +5.47% |
| 8 | FLOCK | +42.43% | okx | +53.82% | bitget | +11.39% |
| 9 | CRO | +41.94% | bitget | +52.89% | okx | +10.95% |
| 10 | AR | +41.27% | bitget | +6.46% | okx | -34.81% |
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
