# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-13 18:51 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1251**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MINIMAX | okx | +254.00% |
| 2 | MINIMAXHKD | bitget | +232.58% |
| 3 | KIOXIA | okx | +217.34% |
| 4 | MINIMAX | bitget | +178.05% |
| 5 | IREN | okx | +156.03% |
| 6 | NBIS | okx | +130.42% |
| 7 | XIAOMI | okx | +101.28% |
| 8 | SOXL | okx | +100.14% |
| 9 | KIOXIA | bitget | +97.13% |
| 10 | MSTR | okx | +95.75% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | POWR | bitget | -717.33% |
| 2 | STEEM | bitget | -481.91% |
| 3 | CVC | bitget | -418.29% |
| 4 | ARK | bitget | -336.27% |
| 5 | GLM | bitget | -267.73% |
| 6 | ZIL | okx | -250.63% |
| 7 | PUNDIX | bitget | -227.43% |
| 8 | IOST | okx | -189.57% |
| 9 | SKHY | bitget | -162.83% |
| 10 | HIVE | bitget | -143.88% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | GLM | +176.64% | okx | -91.09% | bitget | -267.73% |
| 2 | SKHY | +162.83% | okx | +0.00% | bitget | -162.83% |
| 3 | IOST | +157.70% | bitget | -31.86% | okx | -189.57% |
| 4 | IREN | +156.03% | okx | +156.03% | bitget | +0.00% |
| 5 | ZIL | +151.09% | bitget | -99.54% | okx | -250.63% |
| 6 | KIOXIA | +120.22% | okx | +217.34% | bitget | +97.13% |
| 7 | XIAOMI | +101.28% | okx | +101.28% | bitget | +0.00% |
| 8 | SOFTBANK | +95.03% | okx | +95.03% | bitget | +0.00% |
| 9 | MINIMAX | +75.95% | okx | +254.00% | bitget | +178.05% |
| 10 | SAMSUNG | +70.44% | okx | +70.44% | bitget | +0.00% |
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
