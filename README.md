# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-15 19:45 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1251**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GPRO | okx | +156.63% |
| 2 | ONE | okx | +138.86% |
| 3 | JCT | bitget | +84.10% |
| 4 | NES | okx | +77.26% |
| 5 | APR | bitget | +57.27% |
| 6 | NG | okx | +54.47% |
| 7 | KORU | bitget | +52.89% |
| 8 | US100 | okx | +42.08% |
| 9 | PIPPIN | bitget | +41.39% |
| 10 | XPD | okx | +41.02% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ASTR | bitget | -1134.09% |
| 2 | CNPY | okx | -1095.00% |
| 3 | CVC | bitget | -505.45% |
| 4 | STEEM | bitget | -473.48% |
| 5 | HIVE | bitget | -352.59% |
| 6 | USO | okx | -208.77% |
| 7 | KR200 | okx | -205.31% |
| 8 | ACE | bitget | -180.13% |
| 9 | ZIL | okx | -160.55% |
| 10 | LSK | bitget | -157.13% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KR200 | +205.31% | bitget | +0.00% | okx | -205.31% |
| 2 | ZIL | +166.03% | bitget | +5.47% | okx | -160.55% |
| 3 | GPRO | +130.79% | okx | +156.63% | bitget | +25.84% |
| 4 | ONE | +127.91% | okx | +138.86% | bitget | +10.95% |
| 5 | SKDD | +99.80% | okx | -8.72% | bitget | -108.51% |
| 6 | MINIMAX | +75.75% | okx | -47.98% | bitget | -123.73% |
| 7 | OKTA | +70.87% | bitget | +0.00% | okx | -70.87% |
| 8 | UNITREE | +68.42% | bitget | +0.00% | okx | -68.42% |
| 9 | PI | +51.56% | okx | +3.82% | bitget | -47.74% |
| 10 | IOST | +47.39% | bitget | -27.27% | okx | -74.66% |
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
