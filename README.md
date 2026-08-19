# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-19 01:58 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1194**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | okx | +706.86% |
| 2 | BOT | okx | +461.75% |
| 3 | BOT | bitget | +326.31% |
| 4 | CSOPSS2LHKD | bitget | +228.31% |
| 5 | SNXX | bitget | +143.23% |
| 6 | XIAOMI | okx | +122.22% |
| 7 | KORU | bitget | +102.93% |
| 8 | CSOPSK2LHKD | bitget | +102.49% |
| 9 | BX | okx | +85.38% |
| 10 | AAOI | bitget | +83.88% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -600.06% |
| 2 | HOME | okx | -544.39% |
| 3 | BICO | bitget | -372.63% |
| 4 | ACE | bitget | -227.98% |
| 5 | BSP | bitget | -217.25% |
| 6 | RVN | okx | -192.15% |
| 7 | EDEN | okx | -155.51% |
| 8 | RED | bitget | -137.86% |
| 9 | SKHYNIX | bitget | -110.59% |
| 10 | DOS | okx | -80.01% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | FWDI | +706.86% | okx | +706.86% | bitget | +0.00% |
| 2 | BICO | +363.60% | okx | -9.03% | bitget | -372.63% |
| 3 | RVN | +179.01% | bitget | -13.14% | okx | -192.15% |
| 4 | BSP | +164.75% | okx | -52.50% | bitget | -217.25% |
| 5 | BOT | +135.44% | okx | +461.75% | bitget | +326.31% |
| 6 | SNXX | +124.59% | bitget | +143.23% | okx | +18.64% |
| 7 | XIAOMI | +122.22% | okx | +122.22% | bitget | +0.00% |
| 8 | SKHYNIX | +110.59% | okx | +0.00% | bitget | -110.59% |
| 9 | KORU | +102.93% | bitget | +102.93% | okx | +0.00% |
| 10 | BX | +85.38% | okx | +85.38% | bitget | +0.00% |
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
