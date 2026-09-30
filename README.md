# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-30 20:54 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1291**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AGPU | bitget | +385.77% |
| 2 | NKE | bitget | +275.72% |
| 3 | OKLO | bitget | +187.68% |
| 4 | XPD | okx | +134.61% |
| 5 | APLD | bitget | +102.38% |
| 6 | SOFI | bitget | +84.86% |
| 7 | FWDI | bitget | +71.61% |
| 8 | PATH | bitget | +67.56% |
| 9 | PIPPIN | bitget | +67.01% |
| 10 | VRT | okx | +65.94% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CT | okx | -514.59% |
| 2 | BWET | bitget | -452.78% |
| 3 | ARK | bitget | -431.21% |
| 4 | MEW | okx | -161.85% |
| 5 | MEW | bitget | -149.36% |
| 6 | NMR | okx | -115.49% |
| 7 | KOPN | bitget | -98.11% |
| 8 | BLUR | okx | -91.59% |
| 9 | FWDI | okx | -60.44% |
| 10 | NMR | bitget | -59.57% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | OKLO | +153.42% | bitget | +187.68% | okx | +34.27% |
| 2 | FWDI | +132.05% | bitget | +71.61% | okx | -60.44% |
| 3 | APLD | +102.38% | bitget | +102.38% | okx | +0.00% |
| 4 | BLUR | +97.06% | bitget | +5.47% | okx | -91.59% |
| 5 | XPD | +82.59% | okx | +134.61% | bitget | +52.01% |
| 6 | VRT | +65.94% | okx | +65.94% | bitget | +0.00% |
| 7 | USAR | +56.83% | okx | +56.83% | bitget | +0.00% |
| 8 | NMR | +55.92% | bitget | -59.57% | okx | -115.49% |
| 9 | ONE | +55.03% | okx | +11.45% | bitget | -43.58% |
| 10 | KMNO | +50.70% | bitget | +5.47% | okx | -45.22% |
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
