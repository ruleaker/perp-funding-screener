# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-27 17:36 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1051**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MSTR | okx | +76.86% |
| 2 | CAP | bitget | +56.28% |
| 3 | H | okx | +41.75% |
| 4 | BILL | okx | +28.33% |
| 5 | ARIA | bitget | +26.72% |
| 6 | MYX | bitget | +23.43% |
| 7 | BAS | bitget | +20.48% |
| 8 | RIVER | okx | +18.88% |
| 9 | ESPORTS | bitget | +18.18% |
| 10 | URNM | okx | +15.38% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | okx | -749.62% |
| 2 | LAB | bitget | -748.76% |
| 3 | AGLD | bitget | -745.15% |
| 4 | AGLD | okx | -560.98% |
| 5 | BICO | okx | -349.38% |
| 6 | SYN | bitget | -194.80% |
| 7 | RE | bitget | -173.56% |
| 8 | BICO | bitget | -158.12% |
| 9 | RE | okx | -152.43% |
| 10 | PUNDIX | bitget | -149.58% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BICO | +191.27% | bitget | -158.12% | okx | -349.38% |
| 2 | AGLD | +184.17% | okx | -560.98% | bitget | -745.15% |
| 3 | IP | +102.61% | bitget | +5.47% | okx | -97.14% |
| 4 | MSTR | +76.86% | okx | +76.86% | bitget | +0.00% |
| 5 | SNX | +62.77% | bitget | +10.95% | okx | -51.82% |
| 6 | FLOKI | +61.86% | okx | -14.57% | bitget | -76.43% |
| 7 | SUSHI | +51.57% | okx | +10.95% | bitget | -40.62% |
| 8 | CAP | +49.47% | bitget | +56.28% | okx | +6.82% |
| 9 | GLM | +39.31% | okx | -48.94% | bitget | -88.26% |
| 10 | CRO | +39.25% | bitget | +10.95% | okx | -28.30% |
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
