# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-15 19:56 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1323**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AGPU | bitget | +617.03% |
| 2 | GPRO | bitget | +362.55% |
| 3 | KIOXIA | okx | +271.68% |
| 4 | ZHONGJI | bitget | +242.32% |
| 5 | GPRO | okx | +239.47% |
| 6 | CSOPSKHYNIX2L | okx | +216.64% |
| 7 | CSOPSK2LHKD | bitget | +213.63% |
| 8 | CSOPSS2LHKD | bitget | +206.85% |
| 9 | KR200 | okx | +201.04% |
| 10 | SOFTBANK | bitget | +163.48% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BLUR | bitget | -330.47% |
| 2 | AMC | bitget | -209.47% |
| 3 | BWET | bitget | -195.79% |
| 4 | ANIME | okx | -177.31% |
| 5 | BLUR | okx | -151.02% |
| 6 | USDJPY | bitget | -76.54% |
| 7 | RSR | okx | -66.32% |
| 8 | AMC | okx | -65.59% |
| 9 | SPELL | bitget | -61.76% |
| 10 | MINA | bitget | -60.12% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KIOXIA | +231.71% | okx | +271.68% | bitget | +39.97% |
| 2 | KR200 | +201.04% | okx | +201.04% | bitget | +0.00% |
| 3 | BWET | +195.79% | okx | +0.00% | bitget | -195.79% |
| 4 | BLUR | +179.45% | okx | -151.02% | bitget | -330.47% |
| 5 | AMC | +143.89% | okx | -65.59% | bitget | -209.47% |
| 6 | SAMSUNG | +138.83% | okx | +159.96% | bitget | +21.13% |
| 7 | SOFTBANK | +138.64% | bitget | +163.48% | okx | +24.85% |
| 8 | GPRO | +123.08% | bitget | +362.55% | okx | +239.47% |
| 9 | ANIME | +121.68% | bitget | -55.63% | okx | -177.31% |
| 10 | ZHONGJI | +99.98% | bitget | +242.32% | okx | +142.35% |
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
