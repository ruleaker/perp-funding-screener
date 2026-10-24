# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-24 12:49 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1364**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +1095.00% |
| 2 | FIGHT | bitget | +60.99% |
| 3 | IRYS | okx | +60.45% |
| 4 | ARIA | bitget | +46.32% |
| 5 | ZEST | bitget | +45.77% |
| 6 | US100 | okx | +44.61% |
| 7 | 哈基米 | bitget | +38.11% |
| 8 | US500 | okx | +37.05% |
| 9 | SOXL | okx | +35.67% |
| 10 | SOON | okx | +25.58% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ORDER | bitget | -1656.63% |
| 2 | TREE | bitget | -1123.91% |
| 3 | AXIS | bitget | -1022.07% |
| 4 | BIRB | bitget | -998.20% |
| 5 | ORDER | okx | -942.48% |
| 6 | IN | bitget | -494.72% |
| 7 | AXIS | okx | -451.30% |
| 8 | LA | bitget | -392.56% |
| 9 | BTW | bitget | -375.80% |
| 10 | LA | okx | -371.22% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1089.53% | okx | +1095.00% | bitget | +5.47% |
| 2 | ORDER | +714.15% | okx | -942.48% | bitget | -1656.63% |
| 3 | AXIS | +570.77% | okx | -451.30% | bitget | -1022.07% |
| 4 | BTW | +236.28% | okx | -139.52% | bitget | -375.80% |
| 5 | IOST | +131.31% | bitget | -23.76% | okx | -155.07% |
| 6 | BIGTIME | +100.15% | bitget | +5.47% | okx | -94.68% |
| 7 | TRUST | +95.10% | bitget | +5.47% | okx | -89.62% |
| 8 | IRYS | +59.03% | okx | +60.45% | bitget | +1.42% |
| 9 | WCT | +56.27% | bitget | -40.95% | okx | -97.22% |
| 10 | ARKM | +55.23% | bitget | +10.95% | okx | -44.28% |
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
