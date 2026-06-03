# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-03 05:24 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **935**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BB | okx | +495.15% |
| 2 | MRVL | okx | +325.79% |
| 3 | NOK | okx | +277.92% |
| 4 | INX | bitget | +260.94% |
| 5 | CRWD | okx | +250.49% |
| 6 | AMAT | okx | +229.40% |
| 7 | AAOI | okx | +229.12% |
| 8 | NOW | okx | +222.04% |
| 9 | COHR | okx | +208.71% |
| 10 | DRAM | okx | +174.98% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SLX | bitget | -1869.06% |
| 2 | SLX | okx | -658.75% |
| 3 | DRIFT | bitget | -294.77% |
| 4 | HOME | bitget | -270.46% |
| 5 | LAB | bitget | -237.51% |
| 6 | HOME | okx | -171.05% |
| 7 | IRYS | okx | -114.99% |
| 8 | KOPN | bitget | -109.50% |
| 9 | STABLE | okx | -102.42% |
| 10 | JD | bitget | -100.08% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SLX | +1210.31% | okx | -658.75% | bitget | -1869.06% |
| 2 | BB | +489.67% | okx | +495.15% | bitget | +5.47% |
| 3 | LAB | +238.87% | okx | +1.37% | bitget | -237.51% |
| 4 | NOW | +222.04% | okx | +222.04% | bitget | +0.00% |
| 5 | MRVL | +216.29% | okx | +325.79% | bitget | +109.50% |
| 6 | ASTS | +184.71% | okx | +116.60% | bitget | -68.11% |
| 7 | NBIS | +151.71% | okx | +151.71% | bitget | +0.00% |
| 8 | AMAT | +119.90% | okx | +229.40% | bitget | +109.50% |
| 9 | AAOI | +119.62% | okx | +229.12% | bitget | +109.50% |
| 10 | GME | +118.66% | okx | +118.66% | bitget | +0.00% |
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
