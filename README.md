# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-01 21:09 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1293**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AGPU | bitget | +425.08% |
| 2 | SECZ | bitget | +311.53% |
| 3 | SKHYNIX | okx | +167.73% |
| 4 | CBRS | bitget | +154.18% |
| 5 | CSOPSK2LHKD | bitget | +141.69% |
| 6 | 龙虾 | bitget | +133.70% |
| 7 | CSOPSKHYNIX2L | okx | +130.89% |
| 8 | CYPH | bitget | +129.43% |
| 9 | KIOXIA | okx | +120.89% |
| 10 | SHAZ | bitget | +115.74% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BWET | bitget | -382.05% |
| 2 | ARK | bitget | -376.57% |
| 3 | KII | okx | -97.23% |
| 4 | JNJ | okx | -91.57% |
| 5 | ACNSTOCK | bitget | -88.69% |
| 6 | EGLD | bitget | -85.74% |
| 7 | KR200 | okx | -79.74% |
| 8 | GPRO | bitget | -78.51% |
| 9 | SKHY | bitget | -66.03% |
| 10 | CT | okx | -62.46% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +149.77% | okx | +167.73% | bitget | +17.96% |
| 2 | CYPH | +121.06% | bitget | +129.43% | okx | +8.37% |
| 3 | KIOXIA | +120.89% | okx | +120.89% | bitget | +0.00% |
| 4 | SHAZ | +115.74% | bitget | +115.74% | okx | +0.00% |
| 5 | SAMSUNG | +95.07% | okx | +96.71% | bitget | +1.64% |
| 6 | SOFTBANK | +86.86% | okx | +86.86% | bitget | +0.00% |
| 7 | KR200 | +79.74% | bitget | +0.00% | okx | -79.74% |
| 8 | GPRO | +78.51% | okx | +0.00% | bitget | -78.51% |
| 9 | VRT | +78.12% | okx | +78.12% | bitget | +0.00% |
| 10 | EGLD | +77.04% | okx | -8.69% | bitget | -85.74% |
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
