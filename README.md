# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-20 13:07 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1264**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MINIMAX | bitget | +143.01% |
| 2 | MINIMAXHKD | bitget | +101.29% |
| 3 | MINIMAX | okx | +98.27% |
| 4 | SPCH | okx | +94.02% |
| 5 | FIGHT | bitget | +72.27% |
| 6 | SIREN | bitget | +67.34% |
| 7 | STONK | bitget | +65.48% |
| 8 | O | okx | +54.59% |
| 9 | RAVE | bitget | +53.65% |
| 10 | GRVT | okx | +51.75% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONG | bitget | -1160.37% |
| 2 | CELR | bitget | -950.35% |
| 3 | ONE | okx | -790.54% |
| 4 | G | bitget | -467.78% |
| 5 | ZIL | bitget | -381.28% |
| 6 | IOST | okx | -350.89% |
| 7 | ZIL | okx | -345.19% |
| 8 | IOST | bitget | -330.69% |
| 9 | AKE | okx | -320.13% |
| 10 | AKE | bitget | -279.66% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +603.73% | bitget | -186.81% | okx | -790.54% |
| 2 | EGLD | +144.46% | okx | -130.82% | bitget | -275.28% |
| 3 | SPCH | +94.02% | okx | +94.02% | bitget | +0.00% |
| 4 | MINA | +50.92% | okx | +5.47% | bitget | -45.44% |
| 5 | PI | +49.06% | okx | +5.47% | bitget | -43.58% |
| 6 | GRVT | +46.27% | okx | +51.75% | bitget | +5.47% |
| 7 | CXMT | +45.58% | okx | +45.58% | bitget | +0.00% |
| 8 | MINIMAX | +44.74% | bitget | +143.01% | okx | +98.27% |
| 9 | O | +41.01% | okx | +54.59% | bitget | +13.58% |
| 10 | AKE | +40.46% | bitget | -279.66% | okx | -320.13% |
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
