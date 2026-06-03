# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-03 20:01 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **938**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LUNR | okx | +549.51% |
| 2 | BEAT | bitget | +232.25% |
| 3 | INX | bitget | +171.81% |
| 4 | AAOI | okx | +162.79% |
| 5 | EPIC | bitget | +145.63% |
| 6 | SKHYNIX | bitget | +109.50% |
| 7 | OPN | okx | +107.65% |
| 8 | ADBE | okx | +88.12% |
| 9 | GEV | okx | +85.90% |
| 10 | BEAT | okx | +84.33% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -1239.54% |
| 2 | LAB | okx | -1095.00% |
| 3 | LAB | bitget | -1047.91% |
| 4 | STO | bitget | -686.67% |
| 5 | HOME | okx | -324.06% |
| 6 | EDEN | okx | -289.11% |
| 7 | JST | bitget | -117.17% |
| 8 | LUNC | bitget | -102.38% |
| 9 | PROS | bitget | -98.77% |
| 10 | MMT | bitget | -97.89% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HOME | +915.48% | okx | -324.06% | bitget | -1239.54% |
| 2 | AAOI | +162.79% | okx | +162.79% | bitget | +0.00% |
| 3 | BEAT | +147.92% | bitget | +232.25% | okx | +84.33% |
| 4 | MMT | +103.37% | okx | +5.47% | bitget | -97.89% |
| 5 | OPN | +102.17% | okx | +107.65% | bitget | +5.47% |
| 6 | PROS | +93.39% | okx | -5.37% | bitget | -98.77% |
| 7 | MOODENG | +91.76% | okx | +5.47% | bitget | -86.29% |
| 8 | BLUR | +90.67% | okx | +5.47% | bitget | -85.19% |
| 9 | WAL | +80.26% | okx | +5.47% | bitget | -74.79% |
| 10 | ZBT | +68.66% | bitget | +74.13% | okx | +5.47% |
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
