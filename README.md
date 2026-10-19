# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-19 15:46 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1340**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AGPU | bitget | +505.67% |
| 2 | GPRO | bitget | +226.56% |
| 3 | CXMT | okx | +163.46% |
| 4 | RUM | bitget | +159.10% |
| 5 | GPRO | okx | +141.36% |
| 6 | KSTR | okx | +113.90% |
| 7 | MINIMAX | bitget | +113.33% |
| 8 | CVNA | bitget | +106.22% |
| 9 | MINIMAXHKD | bitget | +102.38% |
| 10 | MINIMAX | okx | +100.33% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KOPN | bitget | -667.62% |
| 2 | BLSH | bitget | -369.78% |
| 3 | SAND | bitget | -260.06% |
| 4 | SDGR | bitget | -259.30% |
| 5 | H100 | okx | -248.91% |
| 6 | BTW | bitget | -240.79% |
| 7 | BWET | bitget | -238.82% |
| 8 | CT | bitget | -221.96% |
| 9 | CT | okx | -209.29% |
| 10 | ETN | bitget | -187.25% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +248.91% | bitget | +0.00% | okx | -248.91% |
| 2 | BWET | +159.91% | okx | -78.91% | bitget | -238.82% |
| 3 | SAND | +112.40% | okx | -147.66% | bitget | -260.06% |
| 4 | KSTR | +107.00% | okx | +113.90% | bitget | +6.90% |
| 5 | BOT | +97.35% | bitget | +97.35% | okx | +0.00% |
| 6 | CYPH | +97.35% | bitget | +97.35% | okx | +0.00% |
| 7 | GPRO | +85.20% | bitget | +226.56% | okx | +141.36% |
| 8 | CXMT | +80.68% | okx | +163.46% | bitget | +82.78% |
| 9 | KO | +79.09% | bitget | +0.00% | okx | -79.09% |
| 10 | UNITREE | +72.63% | bitget | +0.00% | okx | -72.63% |
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
