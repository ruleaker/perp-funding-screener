# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-18 18:44 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1328**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOXS | okx | +145.10% |
| 2 | SOXS | bitget | +113.55% |
| 3 | UVXY | bitget | +55.52% |
| 4 | UVXY | okx | +54.01% |
| 5 | EPIC | bitget | +44.68% |
| 6 | DGAI | okx | +43.44% |
| 7 | ARC | bitget | +39.86% |
| 8 | ZEST | bitget | +33.07% |
| 9 | ARX | okx | +28.06% |
| 10 | SKDD | okx | +21.80% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAND | bitget | -445.45% |
| 2 | ARIA | bitget | -395.19% |
| 3 | SAND | okx | -170.67% |
| 4 | KORU | bitget | -146.40% |
| 5 | SOXL | okx | -142.10% |
| 6 | KORU | okx | -141.62% |
| 7 | BR | bitget | -139.39% |
| 8 | SOXL | bitget | -116.18% |
| 9 | NXPC | bitget | -115.85% |
| 10 | CSOPSK2LHKD | bitget | -107.53% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SAND | +274.78% | okx | -170.67% | bitget | -445.45% |
| 2 | WDC | +93.56% | bitget | -8.98% | okx | -102.54% |
| 3 | SHAZ | +73.00% | bitget | +0.00% | okx | -73.00% |
| 4 | ZIL | +54.80% | bitget | -24.42% | okx | -79.22% |
| 5 | UMA | +54.56% | bitget | +5.47% | okx | -49.09% |
| 6 | AAOI | +47.63% | bitget | -50.59% | okx | -98.22% |
| 7 | MRNA | +38.54% | okx | -11.61% | bitget | -50.15% |
| 8 | DGAI | +37.96% | okx | +43.44% | bitget | +5.47% |
| 9 | METIS | +37.31% | bitget | +5.47% | okx | -31.84% |
| 10 | BLUR | +37.16% | bitget | -36.79% | okx | -73.95% |
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
