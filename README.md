# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-27 19:49 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1282**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KII | okx | +121.37% |
| 2 | PIPPIN | bitget | +99.54% |
| 3 | STONK | bitget | +97.56% |
| 4 | XVG | bitget | +91.98% |
| 5 | CNPY | okx | +85.13% |
| 6 | VELODROME | bitget | +76.76% |
| 7 | MMT | bitget | +67.78% |
| 8 | M | bitget | +61.21% |
| 9 | XIAOMI | okx | +60.03% |
| 10 | BIRB | bitget | +60.01% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | okx | -347.36% |
| 2 | MAGIC | okx | -212.04% |
| 3 | COW | bitget | -164.36% |
| 4 | MAGIC | bitget | -134.03% |
| 5 | ONE | bitget | -88.04% |
| 6 | INJ | okx | -78.90% |
| 7 | LSK | bitget | -60.77% |
| 8 | FLOCK | bitget | -58.14% |
| 9 | FLOCK | okx | -49.45% |
| 10 | 2Z | okx | -35.95% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +259.32% | bitget | -88.04% | okx | -347.36% |
| 2 | PIPPIN | +94.06% | bitget | +99.54% | okx | +5.47% |
| 3 | INJ | +89.85% | bitget | +10.95% | okx | -78.90% |
| 4 | MAGIC | +78.01% | bitget | -134.03% | okx | -212.04% |
| 5 | MMT | +62.31% | bitget | +67.78% | okx | +5.47% |
| 6 | XIAOMI | +60.03% | okx | +60.03% | bitget | +0.00% |
| 7 | APR | +50.97% | okx | +56.45% | bitget | +5.47% |
| 8 | GRVT | +48.29% | bitget | +53.76% | okx | +5.47% |
| 9 | AEON | +44.02% | bitget | +49.49% | okx | +5.47% |
| 10 | ACU | +41.50% | bitget | +46.98% | okx | +5.47% |
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
