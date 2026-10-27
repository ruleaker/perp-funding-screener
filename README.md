# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-27 14:45 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1373**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AEHR | bitget | +381.72% |
| 2 | ADI | bitget | +243.09% |
| 3 | BUD | bitget | +215.06% |
| 4 | MSTU | bitget | +210.57% |
| 5 | KR200 | okx | +187.31% |
| 6 | AGPU | bitget | +181.44% |
| 7 | TER | bitget | +172.35% |
| 8 | NOC | bitget | +164.69% |
| 9 | BX | okx | +160.18% |
| 10 | TBT | bitget | +137.31% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | OSS | bitget | -1095.00% |
| 2 | KOPN | bitget | -875.78% |
| 3 | H100 | okx | -835.61% |
| 4 | LWLG | bitget | -699.38% |
| 5 | DOOD | okx | -594.51% |
| 6 | DOOD | bitget | -583.96% |
| 7 | SIMO | bitget | -389.71% |
| 8 | OUST | bitget | -363.43% |
| 9 | GNRC | bitget | -356.86% |
| 10 | TSEM | bitget | -325.54% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +841.08% | bitget | +5.47% | okx | -835.61% |
| 2 | SIMO | +389.71% | okx | +0.00% | bitget | -389.71% |
| 3 | AEHR | +381.72% | bitget | +381.72% | okx | +0.00% |
| 4 | OUST | +363.43% | okx | +0.00% | bitget | -363.43% |
| 5 | CGNX | +234.14% | bitget | +0.00% | okx | -234.14% |
| 6 | KR200 | +187.31% | okx | +187.31% | bitget | +0.00% |
| 7 | FLY | +183.63% | okx | +0.00% | bitget | -183.63% |
| 8 | TER | +172.35% | bitget | +172.35% | okx | +0.00% |
| 9 | BX | +160.18% | okx | +160.18% | bitget | +0.00% |
| 10 | TSEM | +155.82% | okx | -169.72% | bitget | -325.54% |
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
