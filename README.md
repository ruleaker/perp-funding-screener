# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-05 18:20 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **951**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOXL | okx | +212.29% |
| 2 | APR | bitget | +179.36% |
| 3 | ESPORTS | bitget | +177.06% |
| 4 | MU | okx | +125.06% |
| 5 | BEAT | bitget | +107.53% |
| 6 | XCU | okx | +85.17% |
| 7 | NG | okx | +79.27% |
| 8 | LAB | bitget | +76.76% |
| 9 | DRAM | okx | +63.91% |
| 10 | XAG | okx | +56.09% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BABY | bitget | -426.06% |
| 2 | BABY | okx | -395.20% |
| 3 | HOME | bitget | -334.63% |
| 4 | HOME | okx | -323.47% |
| 5 | LA | bitget | -282.62% |
| 6 | PROS | bitget | -171.26% |
| 7 | PROS | okx | -166.42% |
| 8 | INX | bitget | -158.12% |
| 9 | CL | bitget | -154.29% |
| 10 | LA | okx | -142.50% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SOXL | +212.29% | okx | +212.29% | bitget | +0.00% |
| 2 | APR | +173.89% | bitget | +179.36% | okx | +5.47% |
| 3 | LA | +140.12% | okx | -142.50% | bitget | -282.62% |
| 4 | MU | +112.57% | okx | +125.06% | bitget | +12.48% |
| 5 | BEAT | +99.94% | bitget | +107.53% | okx | +7.59% |
| 6 | STX | +76.41% | okx | -4.84% | bitget | -81.25% |
| 7 | SSV | +72.24% | bitget | +10.95% | okx | -61.29% |
| 8 | PEOPLE | +71.76% | bitget | +10.95% | okx | -60.81% |
| 9 | SEI | +68.16% | okx | -17.03% | bitget | -85.19% |
| 10 | DRAM | +63.91% | okx | +63.91% | bitget | +0.00% |
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
