# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-28 17:02 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1441**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | O | okx | +44.01% |
| 2 | SIREN | bitget | +25.29% |
| 3 | KIOXIA | okx | +17.15% |
| 4 | JCT | okx | +16.30% |
| 5 | LYN | bitget | +15.66% |
| 6 | GRIFFAIN | bitget | +13.47% |
| 7 | INJ | okx | +10.95% |
| 8 | NEO | okx | +10.95% |
| 9 | BAND | okx | +10.95% |
| 10 | COMP | okx | +10.95% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | THE | bitget | -1153.03% |
| 2 | CFG | bitget | -579.47% |
| 3 | BLUR | okx | -254.30% |
| 4 | BLUR | bitget | -228.42% |
| 5 | MMT | bitget | -227.98% |
| 6 | MMT | okx | -227.31% |
| 7 | H100 | okx | -186.80% |
| 8 | CYBER | bitget | -163.70% |
| 9 | CELR | bitget | -134.36% |
| 10 | BIGTIME | okx | -121.32% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +192.27% | bitget | +5.47% | okx | -186.80% |
| 2 | BIGTIME | +86.28% | bitget | -35.04% | okx | -121.32% |
| 3 | WOO | +80.85% | bitget | +10.95% | okx | -69.90% |
| 4 | YB | +80.01% | bitget | -22.01% | okx | -102.02% |
| 5 | SKHY | +77.19% | bitget | +0.00% | okx | -77.19% |
| 6 | MOVE | +76.01% | bitget | -15.33% | okx | -91.34% |
| 7 | NKE | +65.57% | bitget | +0.00% | okx | -65.57% |
| 8 | CVX | +58.24% | okx | +3.60% | bitget | -54.64% |
| 9 | SAHARA | +57.85% | bitget | -52.01% | okx | -109.86% |
| 10 | 1INCH | +52.90% | bitget | +9.96% | okx | -42.94% |
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
