# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-18 04:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1257**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BNC | bitget | +736.50% |
| 2 | FWDI | okx | +247.75% |
| 3 | SHAZ | okx | +204.51% |
| 4 | CONL | bitget | +198.41% |
| 5 | GGLL | bitget | +181.00% |
| 6 | PURR | bitget | +162.06% |
| 7 | MSTU | bitget | +147.61% |
| 8 | XIAOMI | okx | +136.04% |
| 9 | ZHONGJI | okx | +122.72% |
| 10 | HYUNDAI | okx | +122.16% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AVA | bitget | -672.33% |
| 2 | IOST | okx | -524.66% |
| 3 | IOST | bitget | -521.44% |
| 4 | LSK | bitget | -469.65% |
| 5 | CVC | bitget | -249.99% |
| 6 | ONE | bitget | -177.39% |
| 7 | NAVER | bitget | -164.91% |
| 8 | LGELECTRONICS | bitget | -143.34% |
| 9 | USO | okx | -137.59% |
| 10 | SOPH | okx | -110.08% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | FWDI | +247.75% | okx | +247.75% | bitget | +0.00% |
| 2 | SHAZ | +204.51% | okx | +204.51% | bitget | +0.00% |
| 3 | PURR | +162.06% | bitget | +162.06% | okx | +0.00% |
| 4 | NAVER | +160.85% | okx | -4.06% | bitget | -164.91% |
| 5 | MSTR | +111.88% | bitget | +118.81% | okx | +6.92% |
| 6 | LGELECTRONICS | +110.02% | okx | -33.32% | bitget | -143.34% |
| 7 | SKUU | +105.89% | bitget | +105.89% | okx | +0.00% |
| 8 | ZHONGJI | +103.12% | okx | +122.72% | bitget | +19.60% |
| 9 | BSP | +101.80% | bitget | +0.00% | okx | -101.80% |
| 10 | SKDD | +100.24% | okx | +6.29% | bitget | -93.95% |
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
