# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-25 18:44 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1436**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZHIPU | okx | +433.35% |
| 2 | ZHIPU | bitget | +377.01% |
| 3 | ZHIPUHKD | bitget | +352.37% |
| 4 | ZHONGJI | bitget | +338.68% |
| 5 | CXMT | okx | +311.86% |
| 6 | MINIMAX | bitget | +263.24% |
| 7 | MINIMAX | okx | +251.76% |
| 8 | CSOPSS2LHKD | bitget | +250.65% |
| 9 | MINIMAXHKD | bitget | +227.65% |
| 10 | INFY | bitget | +179.14% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -620.25% |
| 2 | UVXY | okx | -409.01% |
| 3 | UVXY | bitget | -345.03% |
| 4 | BIGTIME | bitget | -271.23% |
| 5 | BIGTIME | okx | -268.48% |
| 6 | SLX | okx | -234.67% |
| 7 | SKDD | bitget | -221.85% |
| 8 | SSV | okx | -219.33% |
| 9 | SKDD | okx | -180.47% |
| 10 | WAXP | bitget | -178.27% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +625.72% | bitget | +5.47% | okx | -620.25% |
| 2 | ZHONGJI | +199.42% | bitget | +338.68% | okx | +139.26% |
| 3 | CXMT | +157.79% | okx | +311.86% | bitget | +154.07% |
| 4 | BWET | +153.44% | bitget | +0.00% | okx | -153.44% |
| 5 | SKHYNIX | +129.42% | bitget | +169.29% | okx | +39.87% |
| 6 | DOS | +120.95% | bitget | -34.93% | okx | -155.88% |
| 7 | SSV | +118.15% | bitget | -101.18% | okx | -219.33% |
| 8 | INIT | +111.10% | bitget | -18.40% | okx | -129.50% |
| 9 | SSPC | +108.95% | bitget | +108.95% | okx | +0.00% |
| 10 | BARD | +72.89% | bitget | -52.89% | okx | -125.77% |
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
