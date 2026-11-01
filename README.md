# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-01 06:32 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1385**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +283.28% |
| 2 | INTW | okx | +125.81% |
| 3 | GIGADEV | okx | +120.01% |
| 4 | INTW | bitget | +98.99% |
| 5 | SNXX | bitget | +98.22% |
| 6 | FIGHT | bitget | +60.77% |
| 7 | US100 | okx | +60.67% |
| 8 | SNXX | okx | +56.00% |
| 9 | CSOPSS2LHKD | bitget | +54.53% |
| 10 | JELLYJELLY | okx | +49.06% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | POWR | bitget | -1386.93% |
| 2 | POWER | bitget | -447.75% |
| 3 | AKE | okx | -247.36% |
| 4 | LSK | bitget | -228.31% |
| 5 | STEEM | bitget | -214.18% |
| 6 | WET | okx | -132.89% |
| 7 | BX | okx | -130.56% |
| 8 | BLUR | bitget | -118.92% |
| 9 | BLUR | okx | -118.70% |
| 10 | SOPH | bitget | -118.70% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +277.81% | okx | +283.28% | bitget | +5.47% |
| 2 | AKE | +252.83% | bitget | +5.47% | okx | -247.36% |
| 3 | BX | +130.56% | bitget | +0.00% | okx | -130.56% |
| 4 | UNITREE | +85.44% | bitget | +0.00% | okx | -85.44% |
| 5 | WET | +80.22% | bitget | -52.67% | okx | -132.89% |
| 6 | IOST | +54.60% | bitget | -19.49% | okx | -74.09% |
| 7 | PENDLE | +46.54% | okx | +5.47% | bitget | -41.06% |
| 8 | SOPH | +44.51% | okx | -74.19% | bitget | -118.70% |
| 9 | ATOM | +43.96% | bitget | -19.49% | okx | -63.46% |
| 10 | SNXX | +42.22% | bitget | +98.22% | okx | +56.00% |
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
