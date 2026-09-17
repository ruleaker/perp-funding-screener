# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-17 05:04 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1255**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZHONGJI | okx | +232.54% |
| 2 | XIAOMI | okx | +145.23% |
| 3 | ZHONGJI | bitget | +136.00% |
| 4 | BNC | bitget | +127.68% |
| 5 | SKHYNIX | okx | +125.01% |
| 6 | ZHIPU | okx | +122.26% |
| 7 | SHAZ | okx | +113.70% |
| 8 | ZHIPU | bitget | +113.55% |
| 9 | HYUNDAI | okx | +110.57% |
| 10 | XIAOMI | bitget | +110.16% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | okx | -1095.00% |
| 2 | IOST | okx | -671.34% |
| 3 | IOST | bitget | -632.47% |
| 4 | ONE | bitget | -618.24% |
| 5 | CVC | bitget | -464.28% |
| 6 | STEEM | bitget | -259.19% |
| 7 | LSK | bitget | -253.93% |
| 8 | AVA | bitget | -232.14% |
| 9 | CNPY | okx | -184.31% |
| 10 | USO | okx | -180.21% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +476.76% | bitget | -618.24% | okx | -1095.00% |
| 2 | SHAZ | +113.70% | okx | +113.70% | bitget | +0.00% |
| 3 | ZHONGJI | +96.54% | okx | +232.54% | bitget | +136.00% |
| 4 | HYUNDAI | +79.47% | okx | +110.57% | bitget | +31.10% |
| 5 | SKHYNIX | +68.07% | okx | +125.01% | bitget | +56.94% |
| 6 | APP | +55.04% | bitget | +0.00% | okx | -55.04% |
| 7 | VRT | +52.21% | okx | +52.21% | bitget | +0.00% |
| 8 | DOS | +48.67% | bitget | -28.69% | okx | -77.36% |
| 9 | LA | +45.81% | bitget | -82.23% | okx | -128.04% |
| 10 | AVGO | +41.46% | okx | +41.46% | bitget | +0.00% |
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
