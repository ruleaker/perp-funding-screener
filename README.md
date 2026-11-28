# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-28 08:13 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1441**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +743.68% |
| 2 | UP | okx | +171.09% |
| 3 | ZHONGJI | bitget | +133.26% |
| 4 | CXMT | okx | +98.90% |
| 5 | MINIMAX | okx | +85.27% |
| 6 | MINIMAX | bitget | +80.59% |
| 7 | MINIMAXHKD | bitget | +80.04% |
| 8 | ZHIPUHKD | bitget | +65.59% |
| 9 | ZHIPU | bitget | +54.53% |
| 10 | CXMT | bitget | +48.29% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TLM | bitget | -964.59% |
| 2 | CFG | bitget | -963.16% |
| 3 | HAEDAL | bitget | -581.99% |
| 4 | WLFI | bitget | -305.40% |
| 5 | BIGTIME | okx | -254.50% |
| 6 | SLX | okx | -252.53% |
| 7 | WLFI | okx | -241.35% |
| 8 | MMT | bitget | -200.28% |
| 9 | MMT | okx | -197.20% |
| 10 | CYBER | bitget | -180.13% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +738.20% | okx | +743.68% | bitget | +5.47% |
| 2 | BIGTIME | +178.95% | bitget | -75.55% | okx | -254.50% |
| 3 | BAND | +130.85% | okx | +10.95% | bitget | -119.90% |
| 4 | ZHONGJI | +93.02% | bitget | +133.26% | okx | +40.24% |
| 5 | SLX | +89.26% | bitget | -163.26% | okx | -252.53% |
| 6 | MOVE | +89.05% | bitget | -33.84% | okx | -122.89% |
| 7 | SKHY | +80.46% | bitget | +0.00% | okx | -80.46% |
| 8 | INIT | +73.91% | bitget | -25.73% | okx | -99.64% |
| 9 | YB | +65.67% | bitget | -29.02% | okx | -94.69% |
| 10 | WLFI | +64.04% | okx | -241.35% | bitget | -305.40% |
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
