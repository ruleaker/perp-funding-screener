# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-22 05:12 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1274**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZHIPU | okx | +172.48% |
| 2 | SOXS | bitget | +156.15% |
| 3 | XPT | okx | +141.04% |
| 4 | ZHIPU | bitget | +127.46% |
| 5 | BYD | bitget | +125.82% |
| 6 | SKDD | bitget | +121.00% |
| 7 | MINIMAX | okx | +109.91% |
| 8 | KR200 | bitget | +108.08% |
| 9 | GPRO | okx | +106.87% |
| 10 | TEM | okx | +102.44% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KERNEL | bitget | -1198.48% |
| 2 | ONE | okx | -746.29% |
| 3 | CELR | bitget | -708.68% |
| 4 | NAVER | bitget | -524.83% |
| 5 | LGELECTRONICS | bitget | -522.42% |
| 6 | CXMT | okx | -345.83% |
| 7 | CXMT | bitget | -299.59% |
| 8 | LGELECTRONICS | okx | -292.85% |
| 9 | BNC | bitget | -287.66% |
| 10 | HANMI | bitget | -254.92% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +723.40% | bitget | -22.89% | okx | -746.29% |
| 2 | NAVER | +293.73% | okx | -231.10% | bitget | -524.83% |
| 3 | HANMI | +254.92% | okx | +0.00% | bitget | -254.92% |
| 4 | LGELECTRONICS | +229.57% | okx | -292.85% | bitget | -522.42% |
| 5 | INTW | +218.45% | okx | +0.00% | bitget | -218.45% |
| 6 | SOXL | +176.19% | okx | +0.00% | bitget | -176.19% |
| 7 | AXTI | +160.97% | okx | +0.00% | bitget | -160.97% |
| 8 | MVLL | +160.97% | okx | +0.00% | bitget | -160.97% |
| 9 | DATA | +158.37% | bitget | -9.42% | okx | -167.78% |
| 10 | AAOI | +148.90% | okx | +41.81% | bitget | -107.09% |
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
