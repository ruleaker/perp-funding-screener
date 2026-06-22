# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-22 14:11 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1033**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GEV | okx | +348.77% |
| 2 | GLW | okx | +325.62% |
| 3 | SKHYNIX | okx | +309.35% |
| 4 | 龙虾 | bitget | +180.68% |
| 5 | SAMSUNG | okx | +155.59% |
| 6 | AXTI | okx | +130.77% |
| 7 | GWEI | bitget | +129.87% |
| 8 | NOK | okx | +122.03% |
| 9 | AMC | bitget | +109.50% |
| 10 | INTC | okx | +108.46% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H | bitget | -511.15% |
| 2 | H | okx | -413.91% |
| 3 | SHLD | okx | -397.06% |
| 4 | ID | bitget | -350.73% |
| 5 | ME | bitget | -306.38% |
| 6 | FIDA | bitget | -240.79% |
| 7 | ME | okx | -237.94% |
| 8 | RE | bitget | -210.57% |
| 9 | RE | okx | -190.02% |
| 10 | LAYER | bitget | -182.43% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | GEV | +348.77% | okx | +348.77% | bitget | +0.00% |
| 2 | GLW | +325.62% | okx | +325.62% | bitget | +0.00% |
| 3 | SKHYNIX | +309.35% | okx | +309.35% | bitget | +0.00% |
| 4 | SAMSUNG | +155.59% | okx | +155.59% | bitget | +0.00% |
| 5 | AXTI | +130.77% | okx | +130.77% | bitget | +0.00% |
| 6 | H | +97.24% | okx | -413.91% | bitget | -511.15% |
| 7 | HOME | +91.54% | bitget | -25.08% | okx | -116.62% |
| 8 | HYUNDAI | +80.04% | okx | +80.04% | bitget | +0.00% |
| 9 | BMNR | +70.40% | okx | +70.40% | bitget | +0.00% |
| 10 | GRAM | +70.08% | bitget | +75.55% | okx | +5.47% |
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
