# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-18 12:41 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1328**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +69.08% |
| 2 | NG | okx | +67.34% |
| 3 | ARX | okx | +48.07% |
| 4 | CSOPSK2LHKD | bitget | +47.63% |
| 5 | ORCL | okx | +46.77% |
| 6 | DGAI | okx | +38.80% |
| 7 | EPIC | bitget | +38.65% |
| 8 | KORU | okx | +37.96% |
| 9 | QNT | okx | +32.20% |
| 10 | GWEI | bitget | +27.48% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAND | bitget | -501.40% |
| 2 | ERA | bitget | -221.19% |
| 3 | SAND | okx | -139.03% |
| 4 | BLUR | okx | -104.80% |
| 5 | BR | bitget | -98.88% |
| 6 | ZIL | okx | -73.20% |
| 7 | GMT | bitget | -69.75% |
| 8 | ZIL | bitget | -63.62% |
| 9 | RSR | bitget | -61.87% |
| 10 | 1000SATS | bitget | -61.87% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SAND | +362.37% | okx | -139.03% | bitget | -501.40% |
| 2 | H100 | +69.08% | okx | +69.08% | bitget | +0.00% |
| 3 | BLUR | +64.50% | bitget | -40.30% | okx | -104.80% |
| 4 | GMT | +58.69% | okx | -11.06% | bitget | -69.75% |
| 5 | ORCL | +46.77% | okx | +46.77% | bitget | +0.00% |
| 6 | ARX | +42.60% | okx | +48.07% | bitget | +5.47% |
| 7 | GLM | +39.64% | okx | +5.47% | bitget | -34.16% |
| 8 | KORU | +37.96% | okx | +37.96% | bitget | +0.00% |
| 9 | LDO | +37.63% | bitget | +10.95% | okx | -26.68% |
| 10 | BAT | +36.37% | bitget | -2.41% | okx | -38.78% |
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
