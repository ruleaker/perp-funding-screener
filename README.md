# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-22 07:11 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1423**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +958.45% |
| 2 | DGAI | okx | +50.45% |
| 3 | SOXS | okx | +41.74% |
| 4 | SOXS | bitget | +37.89% |
| 5 | THE | bitget | +27.59% |
| 6 | NATGAS | bitget | +22.23% |
| 7 | GRIFFAIN | bitget | +13.47% |
| 8 | BAND | okx | +10.95% |
| 9 | XTZ | okx | +10.95% |
| 10 | SHIB | okx | +10.95% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ENSO | bitget | -1096.53% |
| 2 | AI | okx | -825.51% |
| 3 | INIT | okx | -667.34% |
| 4 | BARD | bitget | -483.55% |
| 5 | IRYS | okx | -443.75% |
| 6 | ENSO | okx | -412.44% |
| 7 | RARE | bitget | -409.20% |
| 8 | CYBER | bitget | -398.58% |
| 9 | ORCA | bitget | -362.01% |
| 10 | YB | okx | -249.01% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +952.97% | okx | +958.45% | bitget | +5.47% |
| 2 | ENSO | +684.09% | okx | -412.44% | bitget | -1096.53% |
| 3 | INIT | +521.38% | bitget | -145.96% | okx | -667.34% |
| 4 | BARD | +396.24% | okx | -87.31% | bitget | -483.55% |
| 5 | IRYS | +360.86% | bitget | -82.89% | okx | -443.75% |
| 6 | UNITREE | +202.04% | bitget | -8.98% | okx | -211.02% |
| 7 | IOTA | +133.14% | okx | -5.93% | bitget | -139.07% |
| 8 | BAND | +123.95% | okx | +10.95% | bitget | -113.00% |
| 9 | COST | +88.79% | bitget | +0.00% | okx | -88.79% |
| 10 | MSTU | +72.93% | okx | -64.82% | bitget | -137.75% |
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
