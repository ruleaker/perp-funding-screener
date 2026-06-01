# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-01 14:30 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **928**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | INX | bitget | +398.80% |
| 2 | AAOI | okx | +357.38% |
| 3 | GLW | okx | +334.86% |
| 4 | ESPORTS | bitget | +214.40% |
| 5 | SHLD | okx | +205.33% |
| 6 | NOK | okx | +204.20% |
| 7 | GEV | okx | +196.20% |
| 8 | DELL | okx | +185.58% |
| 9 | SKYAI | bitget | +164.47% |
| 10 | H | okx | +145.15% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -792.45% |
| 2 | SLX | okx | -319.40% |
| 3 | GUN | bitget | -296.64% |
| 4 | SLX | bitget | -293.90% |
| 5 | HOME | okx | -186.30% |
| 6 | DRIFT | bitget | -148.37% |
| 7 | WAL | bitget | -104.79% |
| 8 | ZORA | okx | -104.17% |
| 9 | MANTRA | bitget | -77.09% |
| 10 | AI | okx | -76.33% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HOME | +606.15% | okx | -186.30% | bitget | -792.45% |
| 2 | AAOI | +317.85% | okx | +357.38% | bitget | +39.53% |
| 3 | COHR | +134.27% | okx | +134.27% | bitget | +0.00% |
| 4 | H | +129.82% | okx | +145.15% | bitget | +15.33% |
| 5 | BB | +128.93% | okx | +134.41% | bitget | +5.47% |
| 6 | NBIS | +99.68% | okx | +99.68% | bitget | +0.00% |
| 7 | CRWV | +96.48% | okx | +96.48% | bitget | +0.00% |
| 8 | RDW | +94.45% | okx | +94.45% | bitget | +0.00% |
| 9 | XPD | +84.27% | okx | +91.71% | bitget | +7.45% |
| 10 | ORCL | +82.04% | okx | +82.04% | bitget | +0.00% |
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
