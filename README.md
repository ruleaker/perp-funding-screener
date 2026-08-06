# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-06 10:58 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1164**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | bitget | +547.50% |
| 2 | WEN | bitget | +205.64% |
| 3 | 1MCHEEMS | bitget | +175.42% |
| 4 | XCU | okx | +162.50% |
| 5 | KIOXIA | okx | +134.45% |
| 6 | COPPER | bitget | +132.06% |
| 7 | INTW | bitget | +117.82% |
| 8 | SOFTBANK | okx | +98.41% |
| 9 | SKHYNIX | okx | +82.39% |
| 10 | JCT | bitget | +81.47% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CAP | bitget | -321.49% |
| 2 | CAP | okx | -299.25% |
| 3 | HOME | okx | -285.75% |
| 4 | HOME | bitget | -241.12% |
| 5 | MIRA | bitget | -236.74% |
| 6 | BANK | bitget | -201.70% |
| 7 | POWR | bitget | -189.44% |
| 8 | CTSI | bitget | -120.89% |
| 9 | OGN | bitget | -109.72% |
| 10 | SITM | bitget | -106.76% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | FWDI | +520.43% | bitget | +547.50% | okx | +27.07% |
| 2 | WEN | +205.64% | bitget | +205.64% | okx | +0.00% |
| 3 | BICO | +139.15% | bitget | +60.12% | okx | -79.04% |
| 4 | INTW | +117.82% | bitget | +117.82% | okx | +0.00% |
| 5 | ZBT | +107.04% | bitget | +5.47% | okx | -101.56% |
| 6 | SKHYNIX | +82.39% | okx | +82.39% | bitget | +0.00% |
| 7 | KIOXIA | +65.80% | okx | +134.45% | bitget | +68.66% |
| 8 | TWLO | +54.64% | bitget | +54.64% | okx | +0.00% |
| 9 | ZIL | +50.88% | bitget | -6.90% | okx | -57.77% |
| 10 | GOOGL | +50.70% | bitget | +50.70% | okx | +0.00% |
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
