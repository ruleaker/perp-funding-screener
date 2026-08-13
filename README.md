# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-13 17:26 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1179**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +439.68% |
| 2 | KIOXIA | okx | +245.33% |
| 3 | KIOXIA | bitget | +163.26% |
| 4 | NG | okx | +162.51% |
| 5 | SAMSUNG | okx | +156.71% |
| 6 | ONE | okx | +139.01% |
| 7 | SKHYNIX | bitget | +137.42% |
| 8 | CSOPSK2LHKD | bitget | +110.70% |
| 9 | NATGAS | bitget | +104.24% |
| 10 | ESPORTS | bitget | +99.43% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | bitget | -684.16% |
| 2 | COTI | bitget | -401.32% |
| 3 | HOME | bitget | -355.00% |
| 4 | HOME | okx | -343.72% |
| 5 | DOS | bitget | -222.94% |
| 6 | DOS | okx | -211.48% |
| 7 | SKUU | okx | -181.01% |
| 8 | AVNT | bitget | -165.24% |
| 9 | ON | okx | -162.68% |
| 10 | SKUU | bitget | -125.71% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +823.16% | okx | +139.01% | bitget | -684.16% |
| 2 | SKHYNIX | +302.25% | okx | +439.68% | bitget | +137.42% |
| 3 | SAMSUNG | +148.71% | okx | +156.71% | bitget | +7.99% |
| 4 | H | +90.25% | okx | +95.72% | bitget | +5.47% |
| 5 | KIOXIA | +82.06% | okx | +245.33% | bitget | +163.26% |
| 6 | GOOGL | +74.01% | bitget | +84.42% | okx | +10.41% |
| 7 | SKUU | +55.30% | bitget | -125.71% | okx | -181.01% |
| 8 | AVNT | +53.50% | okx | -111.74% | bitget | -165.24% |
| 9 | KORU | +50.59% | okx | +0.00% | bitget | -50.59% |
| 10 | XPD | +39.52% | okx | +95.91% | bitget | +56.39% |
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
