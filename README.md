# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-21 10:36 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1126**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BSP | okx | +644.19% |
| 2 | SITM | bitget | +457.82% |
| 3 | EVEX | bitget | +243.75% |
| 4 | QNTSTOCK | bitget | +131.29% |
| 5 | SAMSUNG | okx | +112.32% |
| 6 | FLY | bitget | +89.79% |
| 7 | SKHYNIX | okx | +76.58% |
| 8 | INX | bitget | +72.38% |
| 9 | GEV | okx | +69.66% |
| 10 | FIGHT | bitget | +69.31% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ERA | bitget | -1359.00% |
| 2 | SOXS | bitget | -547.50% |
| 3 | LA | bitget | -505.45% |
| 4 | FWDI | bitget | -451.14% |
| 5 | LA | okx | -392.81% |
| 6 | ZHIPU | okx | -300.84% |
| 7 | EWH | bitget | -267.18% |
| 8 | HOME | okx | -180.36% |
| 9 | HOME | bitget | -147.06% |
| 10 | INTW | bitget | -132.93% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BSP | +644.19% | okx | +644.19% | bitget | +0.00% |
| 2 | SOXS | +566.14% | okx | +18.64% | bitget | -547.50% |
| 3 | ZHIPU | +241.60% | bitget | -59.24% | okx | -300.84% |
| 4 | LA | +112.64% | okx | -392.81% | bitget | -505.45% |
| 5 | SAMSUNG | +112.32% | okx | +112.32% | bitget | +0.00% |
| 6 | SKHYNIX | +76.58% | okx | +76.58% | bitget | +0.00% |
| 7 | GEV | +69.66% | okx | +69.66% | bitget | +0.00% |
| 8 | PROS | +57.41% | bitget | +5.47% | okx | -51.93% |
| 9 | TWLO | +56.83% | okx | +0.00% | bitget | -56.83% |
| 10 | GOOGL | +48.11% | okx | +56.87% | bitget | +8.76% |
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
