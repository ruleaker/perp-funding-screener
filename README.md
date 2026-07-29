# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-29 03:47 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1147**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ARQQ | bitget | +547.50% |
| 2 | SKHYNIX | bitget | +415.77% |
| 3 | SKHYNIX | okx | +383.33% |
| 4 | KR200 | okx | +377.51% |
| 5 | SNXX | okx | +321.56% |
| 6 | SAMSUNG | okx | +245.07% |
| 7 | SOXS | bitget | +234.00% |
| 8 | SAMSUNG | bitget | +196.55% |
| 9 | SKDD | bitget | +164.14% |
| 10 | EWY | okx | +110.17% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LA | bitget | -1642.72% |
| 2 | LA | okx | -695.31% |
| 3 | KORU | bitget | -547.50% |
| 4 | SNXX | bitget | -489.57% |
| 5 | ZIL | bitget | -435.15% |
| 6 | HOT | bitget | -370.88% |
| 7 | BOT | okx | -331.97% |
| 8 | ZIL | okx | -325.33% |
| 9 | SKUU | bitget | -307.37% |
| 10 | MUU | bitget | -306.82% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LA | +947.41% | okx | -695.31% | bitget | -1642.72% |
| 2 | SNXX | +811.14% | okx | +321.56% | bitget | -489.57% |
| 3 | KORU | +547.50% | okx | +0.00% | bitget | -547.50% |
| 4 | RAM | +341.32% | okx | +69.21% | bitget | -272.11% |
| 5 | BOT | +331.97% | bitget | +0.00% | okx | -331.97% |
| 6 | MUU | +306.82% | okx | +0.00% | bitget | -306.82% |
| 7 | SOXS | +289.93% | bitget | +234.00% | okx | -55.93% |
| 8 | MVLL | +195.38% | okx | +4.20% | bitget | -191.19% |
| 9 | EWY | +110.17% | okx | +110.17% | bitget | +0.00% |
| 10 | CRDO | +109.83% | okx | +0.00% | bitget | -109.83% |
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
