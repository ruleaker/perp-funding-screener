# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-22 20:13 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1361**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +152.87% |
| 2 | SOXL | bitget | +135.78% |
| 3 | BAC | bitget | +130.52% |
| 4 | SECZ | okx | +108.29% |
| 5 | JOBY | bitget | +89.02% |
| 6 | NDX100 | bitget | +84.10% |
| 7 | BNC | bitget | +83.22% |
| 8 | MP | bitget | +78.73% |
| 9 | XPT | okx | +69.81% |
| 10 | SOXL | okx | +67.91% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BTW | okx | -1095.00% |
| 2 | BTW | bitget | -958.78% |
| 3 | ALT | bitget | -831.32% |
| 4 | AXIS | okx | -666.61% |
| 5 | AXIS | bitget | -643.53% |
| 6 | IOST | okx | -332.60% |
| 7 | TWASX | bitget | -166.99% |
| 8 | DGAI | bitget | -163.05% |
| 9 | MEW | okx | -147.60% |
| 10 | CSOPSK2LHKD | bitget | -145.96% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | IOST | +258.90% | bitget | -73.69% | okx | -332.60% |
| 2 | H100 | +147.39% | okx | +152.87% | bitget | +5.47% |
| 3 | BTW | +136.22% | bitget | -958.78% | okx | -1095.00% |
| 4 | SOFTBANK | +119.46% | okx | +0.00% | bitget | -119.46% |
| 5 | DGAI | +112.21% | okx | -50.83% | bitget | -163.05% |
| 6 | AMC | +93.29% | okx | +0.00% | bitget | -93.29% |
| 7 | SECZ | +90.55% | okx | +108.29% | bitget | +17.74% |
| 8 | SAMSUNG | +75.29% | bitget | +0.00% | okx | -75.29% |
| 9 | SOXL | +67.87% | bitget | +135.78% | okx | +67.91% |
| 10 | HYUNDAI | +66.51% | bitget | +0.00% | okx | -66.51% |
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
