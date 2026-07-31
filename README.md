# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-31 03:58 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1153**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZHIPU | okx | +1095.00% |
| 2 | KIOXIA | okx | +980.51% |
| 3 | MINIMAX | okx | +476.87% |
| 4 | MAGMA | bitget | +412.49% |
| 5 | SOXS | okx | +142.66% |
| 6 | APR | bitget | +117.93% |
| 7 | ZHIPU | bitget | +111.14% |
| 8 | MINIMAX | bitget | +106.32% |
| 9 | ON | okx | +100.69% |
| 10 | MSTU | bitget | +90.99% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LA | bitget | -1645.02% |
| 2 | LA | okx | -780.77% |
| 3 | ZHIPUHKD | bitget | -547.50% |
| 4 | MIRA | bitget | -507.86% |
| 5 | KR200 | okx | -420.46% |
| 6 | ADVANTEST | bitget | -414.90% |
| 7 | VANRY | bitget | -312.62% |
| 8 | RDDT | bitget | -302.99% |
| 9 | BANK | bitget | -249.11% |
| 10 | EUL | bitget | -231.04% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ZHIPU | +983.86% | okx | +1095.00% | bitget | +111.14% |
| 2 | KIOXIA | +980.51% | okx | +980.51% | bitget | +0.00% |
| 3 | LA | +864.25% | okx | -780.77% | bitget | -1645.02% |
| 4 | MINIMAX | +370.55% | okx | +476.87% | bitget | +106.32% |
| 5 | RDDT | +302.99% | okx | +0.00% | bitget | -302.99% |
| 6 | WEN | +180.61% | bitget | +0.00% | okx | -180.61% |
| 7 | INTW | +124.48% | bitget | -61.87% | okx | -186.35% |
| 8 | SOXL | +119.56% | bitget | -20.91% | okx | -140.48% |
| 9 | APR | +112.46% | bitget | +117.93% | okx | +5.47% |
| 10 | SOXS | +106.09% | okx | +142.66% | bitget | +36.57% |
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
