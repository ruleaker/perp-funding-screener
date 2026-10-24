# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-24 18:54 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1364**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +551.31% |
| 2 | MRNA | okx | +108.75% |
| 3 | PIPPIN | bitget | +73.15% |
| 4 | MRNA | bitget | +62.74% |
| 5 | US100 | okx | +38.29% |
| 6 | SOON | okx | +38.27% |
| 7 | CYPH | okx | +33.80% |
| 8 | ARIA | bitget | +32.85% |
| 9 | US500 | okx | +29.61% |
| 10 | MUBARAK | okx | +29.19% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | IN | bitget | -1480.22% |
| 2 | AXIS | bitget | -1256.51% |
| 3 | BIRB | bitget | -914.76% |
| 4 | BTW | bitget | -689.74% |
| 5 | ANIME | okx | -527.41% |
| 6 | ANIME | bitget | -430.44% |
| 7 | ORDER | okx | -407.99% |
| 8 | AXIS | okx | -395.28% |
| 9 | ORDER | bitget | -394.75% |
| 10 | TREE | bitget | -284.04% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | AXIS | +861.23% | okx | -395.28% | bitget | -1256.51% |
| 2 | H100 | +545.83% | okx | +551.31% | bitget | +5.47% |
| 3 | BTW | +510.93% | okx | -178.81% | bitget | -689.74% |
| 4 | ANIME | +96.97% | bitget | -430.44% | okx | -527.41% |
| 5 | IOST | +91.65% | bitget | -33.95% | okx | -125.59% |
| 6 | IRYS | +64.39% | bitget | -1.75% | okx | -66.14% |
| 7 | PIPPIN | +59.30% | bitget | +73.15% | okx | +13.84% |
| 8 | MRNA | +46.01% | okx | +108.75% | bitget | +62.74% |
| 9 | ZBT | +42.78% | bitget | -15.00% | okx | -57.78% |
| 10 | IOTA | +36.51% | bitget | +10.95% | okx | -25.56% |
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
