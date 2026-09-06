# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-06 04:55 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1235**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | okx | +254.54% |
| 2 | ESPORTS | bitget | +183.85% |
| 3 | GPRO | okx | +135.76% |
| 4 | PONS | okx | +120.99% |
| 5 | ONE | bitget | +113.11% |
| 6 | CP | okx | +109.38% |
| 7 | PONS | bitget | +106.00% |
| 8 | HOOD | okx | +71.90% |
| 9 | XMR | bitget | +56.61% |
| 10 | ARIA | bitget | +52.78% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | T | bitget | -474.03% |
| 2 | LA | bitget | -382.48% |
| 3 | LA | okx | -352.99% |
| 4 | ICX | okx | -243.11% |
| 5 | ACE | bitget | -237.29% |
| 6 | CAP | okx | -187.47% |
| 7 | CAP | bitget | -161.51% |
| 8 | CGNX | okx | -101.53% |
| 9 | UNITAS | bitget | -88.15% |
| 10 | COTI | bitget | -83.00% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +141.42% | okx | +254.54% | bitget | +113.11% |
| 2 | GPRO | +135.76% | okx | +135.76% | bitget | +0.00% |
| 3 | CGNX | +101.53% | bitget | +0.00% | okx | -101.53% |
| 4 | HOOD | +71.90% | okx | +71.90% | bitget | +0.00% |
| 5 | CP | +67.44% | okx | +109.38% | bitget | +41.94% |
| 6 | RAY | +54.79% | bitget | +0.55% | okx | -54.24% |
| 7 | BICO | +48.94% | okx | -15.45% | bitget | -64.39% |
| 8 | BMNR | +36.55% | okx | +36.55% | bitget | +0.00% |
| 9 | EDGE | +33.98% | okx | +42.19% | bitget | +8.21% |
| 10 | SAND | +33.41% | bitget | +10.95% | okx | -22.46% |
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
