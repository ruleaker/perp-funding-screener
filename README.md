# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-19 04:49 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1264**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GPRO | okx | +100.02% |
| 2 | POWER | bitget | +78.51% |
| 3 | STONK | bitget | +68.44% |
| 4 | 哈基米 | bitget | +64.61% |
| 5 | XMR | bitget | +61.43% |
| 6 | G | bitget | +60.77% |
| 7 | GPRO | bitget | +55.84% |
| 8 | US500 | okx | +54.92% |
| 9 | CRO | bitget | +48.95% |
| 10 | SOXS | okx | +47.45% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AVA | bitget | -368.80% |
| 2 | F | bitget | -303.42% |
| 3 | F | okx | -290.44% |
| 4 | IOST | okx | -217.33% |
| 5 | IOST | bitget | -206.96% |
| 6 | LSK | bitget | -195.68% |
| 7 | ONE | bitget | -154.83% |
| 8 | CVC | bitget | -131.73% |
| 9 | ONE | okx | -119.45% |
| 10 | VTHO | bitget | -68.77% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SOPH | +44.52% | bitget | -14.45% | okx | -58.98% |
| 2 | GPRO | +44.18% | okx | +100.02% | bitget | +55.84% |
| 3 | EGLD | +41.46% | bitget | +10.95% | okx | -30.51% |
| 4 | RAVE | +39.36% | okx | +44.83% | bitget | +5.47% |
| 5 | CRO | +38.00% | bitget | +48.95% | okx | +10.95% |
| 6 | ONE | +35.38% | okx | -119.45% | bitget | -154.83% |
| 7 | FLOCK | +30.93% | okx | +36.41% | bitget | +5.47% |
| 8 | MUU | +29.72% | okx | -26.67% | bitget | -56.39% |
| 9 | SNOW | +25.13% | okx | +25.13% | bitget | +0.00% |
| 10 | AEON | +23.98% | bitget | +29.46% | okx | +5.47% |
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
