# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-17 10:16 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1116**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOXS | bitget | +214.73% |
| 2 | ZHIPU | okx | +203.37% |
| 3 | SNXX | okx | +192.44% |
| 4 | TQQQ | okx | +137.59% |
| 5 | SNDK | okx | +135.90% |
| 6 | 龙虾 | bitget | +131.62% |
| 7 | SKHY | okx | +115.25% |
| 8 | ZHIPU | bitget | +113.00% |
| 9 | SOXL | okx | +111.97% |
| 10 | MU | okx | +110.99% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -1528.40% |
| 2 | LRC | okx | -1095.00% |
| 3 | RDDT | bitget | -474.90% |
| 4 | HOME | okx | -443.19% |
| 5 | EWH | bitget | -270.57% |
| 6 | FLOCK | bitget | -267.95% |
| 7 | OGN | bitget | -187.03% |
| 8 | BONK | okx | -183.57% |
| 9 | WEN | okx | -171.16% |
| 10 | FLY | bitget | -168.63% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HOME | +1085.21% | okx | -443.19% | bitget | -1528.40% |
| 2 | RDDT | +474.90% | okx | +0.00% | bitget | -474.90% |
| 3 | SOXS | +263.02% | bitget | +214.73% | okx | -48.29% |
| 4 | BOT | +198.16% | okx | +96.87% | bitget | -101.29% |
| 5 | SNXX | +192.44% | okx | +192.44% | bitget | +0.00% |
| 6 | WEN | +171.16% | bitget | +0.00% | okx | -171.16% |
| 7 | TQQQ | +120.51% | okx | +137.59% | bitget | +17.08% |
| 8 | SKHY | +115.25% | okx | +115.25% | bitget | +0.00% |
| 9 | SNDK | +99.66% | okx | +135.90% | bitget | +36.24% |
| 10 | MVLL | +93.76% | okx | +93.76% | bitget | +0.00% |
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
