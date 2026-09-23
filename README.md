# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-23 04:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1273**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SHLD | okx | +245.43% |
| 2 | XIAOMI | okx | +227.00% |
| 3 | XIAOMI | bitget | +206.30% |
| 4 | MSTU | bitget | +190.09% |
| 5 | ZHIPU | okx | +187.69% |
| 6 | BNC | bitget | +179.58% |
| 7 | ZHIPU | bitget | +159.98% |
| 8 | SKHYNIX | okx | +157.81% |
| 9 | ZHONGJI | okx | +152.19% |
| 10 | SKDD | bitget | +143.88% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LGELECTRONICS | bitget | -481.47% |
| 2 | ONE | okx | -433.62% |
| 3 | KERNEL | bitget | -389.93% |
| 4 | ONE | bitget | -350.51% |
| 5 | COTI | bitget | -325.54% |
| 6 | LGELECTRONICS | okx | -239.34% |
| 7 | CELR | bitget | -235.86% |
| 8 | KORU | bitget | -185.38% |
| 9 | CXMT | okx | -156.68% |
| 10 | IOST | okx | -154.90% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LGELECTRONICS | +242.13% | okx | -239.34% | bitget | -481.47% |
| 2 | KORU | +185.38% | okx | +0.00% | bitget | -185.38% |
| 3 | SKDD | +120.85% | bitget | +143.88% | okx | +23.03% |
| 4 | MSTR | +107.85% | bitget | +129.43% | okx | +21.58% |
| 5 | NAVER | +94.33% | okx | +111.41% | bitget | +17.08% |
| 6 | SKUU | +89.02% | okx | +0.00% | bitget | -89.02% |
| 7 | ONE | +83.12% | bitget | -350.51% | okx | -433.62% |
| 8 | UVXY | +73.71% | okx | +73.71% | bitget | +0.00% |
| 9 | HYUNDAI | +66.12% | okx | +130.83% | bitget | +64.71% |
| 10 | SKHYNIX | +64.62% | okx | +157.81% | bitget | +93.18% |
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
