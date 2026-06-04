# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-04 18:33 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **943**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | DRIFT | bitget | +147.28% |
| 2 | SAHARA | bitget | +135.12% |
| 3 | INX | bitget | +110.27% |
| 4 | QNTSTOCK | bitget | +109.50% |
| 5 | SKHYNIX | bitget | +109.50% |
| 6 | GWEI | bitget | +89.46% |
| 7 | BSB | okx | +84.51% |
| 8 | LITE | okx | +81.57% |
| 9 | BMNR | okx | +77.14% |
| 10 | DRAM | okx | +73.04% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -2190.00% |
| 2 | HOME | okx | -531.75% |
| 3 | LAB | bitget | -234.22% |
| 4 | LAB | okx | -199.81% |
| 5 | SEI | bitget | -170.49% |
| 6 | SEI | okx | -75.07% |
| 7 | TRX | bitget | -74.68% |
| 8 | MON | bitget | -68.11% |
| 9 | LUNC | bitget | -58.47% |
| 10 | DASH | bitget | -56.17% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HOME | +1658.25% | okx | -531.75% | bitget | -2190.00% |
| 2 | SAHARA | +103.72% | bitget | +135.12% | okx | +31.41% |
| 3 | SEI | +95.42% | okx | -75.07% | bitget | -170.49% |
| 4 | LITE | +81.57% | okx | +81.57% | bitget | +0.00% |
| 5 | BSB | +79.03% | okx | +84.51% | bitget | +5.47% |
| 6 | DRAM | +73.04% | okx | +73.04% | bitget | +0.00% |
| 7 | MU | +67.81% | okx | +67.81% | bitget | +0.00% |
| 8 | BB | +60.98% | okx | +66.46% | bitget | +5.47% |
| 9 | SNX | +50.14% | bitget | -4.49% | okx | -54.63% |
| 10 | OPN | +48.19% | okx | +53.66% | bitget | +5.47% |
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
