# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-22 16:30 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1423**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MSTU | bitget | +93.62% |
| 2 | MINIMAX | okx | +87.09% |
| 3 | MSTU | okx | +83.46% |
| 4 | MINIMAX | bitget | +78.51% |
| 5 | MINIMAXHKD | bitget | +61.21% |
| 6 | MSTR | okx | +56.84% |
| 7 | FIGHT | bitget | +54.09% |
| 8 | CRCL | okx | +53.52% |
| 9 | UP | okx | +49.05% |
| 10 | CXMT | okx | +48.08% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ENSO | bitget | -697.30% |
| 2 | BARD | bitget | -385.33% |
| 3 | XVG | bitget | -376.79% |
| 4 | ENSO | okx | -373.27% |
| 5 | BARD | okx | -300.51% |
| 6 | CYBER | bitget | -265.21% |
| 7 | IRYS | okx | -214.79% |
| 8 | AI | okx | -202.02% |
| 9 | RARE | bitget | -193.27% |
| 10 | CP | okx | -158.55% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ENSO | +324.02% | okx | -373.27% | bitget | -697.30% |
| 2 | IRYS | +157.52% | bitget | -57.27% | okx | -214.79% |
| 3 | CP | +146.83% | bitget | -11.72% | okx | -158.55% |
| 4 | COST | +115.88% | bitget | +0.00% | okx | -115.88% |
| 5 | BARD | +84.83% | okx | -300.51% | bitget | -385.33% |
| 6 | GMT | +78.31% | bitget | -0.11% | okx | -78.42% |
| 7 | HUMA | +59.05% | bitget | -16.32% | okx | -75.36% |
| 8 | COMP | +48.10% | okx | -4.67% | bitget | -52.78% |
| 9 | CXMT | +48.08% | okx | +48.08% | bitget | +0.00% |
| 10 | WOO | +46.03% | bitget | +10.95% | okx | -35.08% |
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
