# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-15 04:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1323**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +463.06% |
| 2 | SKHYNIX | bitget | +288.86% |
| 3 | KR200 | okx | +273.51% |
| 4 | CSOPSAMSUNG2L | okx | +256.71% |
| 5 | CSOPSKHYNIX2L | okx | +202.77% |
| 6 | CXMT | okx | +186.10% |
| 7 | KR200 | bitget | +182.76% |
| 8 | JP225 | okx | +139.66% |
| 9 | SKUU | okx | +132.26% |
| 10 | RAM | okx | +114.97% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -749.32% |
| 2 | RSR | bitget | -515.42% |
| 3 | WAL | bitget | -462.97% |
| 4 | RSR | okx | -421.04% |
| 5 | WAL | okx | -386.40% |
| 6 | SKDD | okx | -380.22% |
| 7 | CSOPSK2LHKD | bitget | -369.12% |
| 8 | VICR | okx | -351.60% |
| 9 | BSP | okx | -273.57% |
| 10 | BWET | okx | -268.75% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +749.32% | bitget | +0.00% | okx | -749.32% |
| 2 | SKDD | +397.63% | bitget | +17.41% | okx | -380.22% |
| 3 | BSP | +273.57% | bitget | +0.00% | okx | -273.57% |
| 4 | SKUU | +246.69% | okx | +132.26% | bitget | -114.43% |
| 5 | TMF | +190.94% | bitget | +33.51% | okx | -157.43% |
| 6 | XIAOMI | +184.22% | bitget | -55.84% | okx | -240.06% |
| 7 | RAM | +181.33% | okx | +114.97% | bitget | -66.36% |
| 8 | SKHYNIX | +174.20% | okx | +463.06% | bitget | +288.86% |
| 9 | BWET | +169.11% | bitget | -99.64% | okx | -268.75% |
| 10 | JP225 | +139.66% | okx | +139.66% | bitget | +0.00% |
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
