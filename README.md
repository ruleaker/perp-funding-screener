# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-13 06:56 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1312**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +678.14% |
| 2 | LGELECTRONICS | bitget | +450.92% |
| 3 | SKHYNIX | okx | +326.77% |
| 4 | SKUU | okx | +247.86% |
| 5 | CSOPSAMSUNG2L | okx | +245.03% |
| 6 | LGELECTRONICS | okx | +233.79% |
| 7 | SAMSUNGEM | bitget | +196.55% |
| 8 | BYD | bitget | +194.58% |
| 9 | MSTU | bitget | +192.61% |
| 10 | GPRO | okx | +176.74% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACN | okx | -1095.00% |
| 2 | H100 | okx | -1095.00% |
| 3 | RSR | bitget | -915.31% |
| 4 | CTK | bitget | -632.14% |
| 5 | SKDD | okx | -497.92% |
| 6 | TMF | okx | -295.78% |
| 7 | SKUU | bitget | -292.04% |
| 8 | BZ | okx | -286.21% |
| 9 | BLUR | okx | -216.34% |
| 10 | OGN | bitget | -198.52% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1095.00% | bitget | +0.00% | okx | -1095.00% |
| 2 | RSR | +719.81% | okx | -195.51% | bitget | -915.31% |
| 3 | SKDD | +674.33% | bitget | +176.40% | okx | -497.92% |
| 4 | SKUU | +539.90% | okx | +247.86% | bitget | -292.04% |
| 5 | TMF | +306.95% | bitget | +11.17% | okx | -295.78% |
| 6 | RAM | +256.83% | okx | +136.71% | bitget | -120.12% |
| 7 | BZ | +239.13% | bitget | -47.09% | okx | -286.21% |
| 8 | LGELECTRONICS | +217.13% | bitget | +450.92% | okx | +233.79% |
| 9 | MSTU | +192.61% | bitget | +192.61% | okx | +0.00% |
| 10 | GPRO | +176.74% | okx | +176.74% | bitget | +0.00% |
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
