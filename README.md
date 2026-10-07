# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-07 15:39 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1301**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +877.78% |
| 2 | NATGAS | bitget | +537.97% |
| 3 | ETN | bitget | +316.35% |
| 4 | BLSH | bitget | +289.41% |
| 5 | ECHO | bitget | +269.37% |
| 6 | GPRO | bitget | +219.88% |
| 7 | KOPN | bitget | +147.39% |
| 8 | SOFTBANK | okx | +141.69% |
| 9 | MP | bitget | +125.16% |
| 10 | ACNSTOCK | bitget | +109.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SECZ | bitget | -410.84% |
| 2 | USDESTOCK | bitget | -356.97% |
| 3 | NMR | bitget | -329.05% |
| 4 | H100 | okx | -308.28% |
| 5 | BWET | okx | -302.11% |
| 6 | NMR | okx | -278.28% |
| 7 | BR | bitget | -261.05% |
| 8 | BOT | bitget | -200.06% |
| 9 | MINA | bitget | -189.33% |
| 10 | ALAB | bitget | -167.53% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SECZ | +410.84% | okx | +0.00% | bitget | -410.84% |
| 2 | H100 | +308.28% | bitget | +0.00% | okx | -308.28% |
| 3 | BWET | +233.45% | bitget | -68.66% | okx | -302.11% |
| 4 | GPRO | +219.88% | bitget | +219.88% | okx | +0.00% |
| 5 | SOFTBANK | +146.61% | okx | +141.69% | bitget | -4.93% |
| 6 | AMC | +132.60% | okx | +0.00% | bitget | -132.60% |
| 7 | ALAB | +131.32% | okx | -36.21% | bitget | -167.53% |
| 8 | BOT | +120.92% | okx | -79.14% | bitget | -200.06% |
| 9 | MINA | +87.99% | okx | -101.33% | bitget | -189.33% |
| 10 | SAND | +68.32% | okx | -63.51% | bitget | -131.84% |
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
