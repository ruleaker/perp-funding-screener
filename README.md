# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-27 18:20 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1441**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +522.01% |
| 2 | 哈基米 | bitget | +347.12% |
| 3 | UP | okx | +220.16% |
| 4 | CXMT | okx | +147.62% |
| 5 | INFY | bitget | +104.90% |
| 6 | CXMT | bitget | +78.62% |
| 7 | BOT | okx | +76.04% |
| 8 | CSOPSK2LHKD | bitget | +68.22% |
| 9 | CSOPSS2LHKD | bitget | +60.01% |
| 10 | BNC | bitget | +58.58% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BLUR | bitget | -1596.40% |
| 2 | BLUR | okx | -1095.00% |
| 3 | HAEDAL | bitget | -816.32% |
| 4 | CFG | bitget | -451.36% |
| 5 | MMT | bitget | -450.81% |
| 6 | MMT | okx | -440.63% |
| 7 | SKHY | okx | -332.57% |
| 8 | SKDD | bitget | -222.61% |
| 9 | SKDD | okx | -192.54% |
| 10 | BIGTIME | okx | -180.78% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +516.53% | okx | +522.01% | bitget | +5.47% |
| 2 | BLUR | +501.40% | okx | -1095.00% | bitget | -1596.40% |
| 3 | SKHY | +332.57% | bitget | +0.00% | okx | -332.57% |
| 4 | BOT | +148.75% | okx | +76.04% | bitget | -72.71% |
| 5 | BIGTIME | +148.04% | bitget | -32.74% | okx | -180.78% |
| 6 | CXMT | +69.00% | okx | +147.62% | bitget | +78.62% |
| 7 | AMC | +64.31% | bitget | +0.00% | okx | -64.31% |
| 8 | BABY | +57.66% | bitget | -16.32% | okx | -73.98% |
| 9 | BWET | +55.38% | okx | -92.33% | bitget | -147.72% |
| 10 | ALLO | +50.68% | bitget | +5.47% | okx | -45.21% |
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
