# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-30 06:08 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1380**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +1095.00% |
| 2 | INTW | okx | +384.12% |
| 3 | SAMSUNGEM | bitget | +357.19% |
| 4 | CEG | okx | +339.28% |
| 5 | BNC | bitget | +330.36% |
| 6 | LGENERGY | bitget | +328.61% |
| 7 | NAVER | bitget | +307.04% |
| 8 | LGELECTRONICS | bitget | +271.45% |
| 9 | QNT | okx | +225.87% |
| 10 | CSOPSS2LHKD | bitget | +220.75% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITREE | okx | -1095.00% |
| 2 | JIO | bitget | -1095.00% |
| 3 | UNITREE | bitget | -459.46% |
| 4 | TRX | okx | -320.61% |
| 5 | BOT | okx | -294.00% |
| 6 | SKDD | okx | -237.75% |
| 7 | DOOD | bitget | -233.02% |
| 8 | DOOD | okx | -230.76% |
| 9 | TRX | bitget | -220.10% |
| 10 | LSK | bitget | -165.89% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1089.53% | okx | +1095.00% | bitget | +5.47% |
| 2 | UNITREE | +635.54% | bitget | -459.46% | okx | -1095.00% |
| 3 | INTW | +384.12% | okx | +384.12% | bitget | +0.00% |
| 4 | CEG | +339.28% | okx | +339.28% | bitget | +0.00% |
| 5 | NAVER | +307.04% | bitget | +307.04% | okx | +0.00% |
| 6 | BOT | +294.00% | bitget | +0.00% | okx | -294.00% |
| 7 | LGELECTRONICS | +271.45% | bitget | +271.45% | okx | +0.00% |
| 8 | QNT | +242.51% | okx | +225.87% | bitget | -16.64% |
| 9 | SKDD | +237.75% | bitget | +0.00% | okx | -237.75% |
| 10 | BWET | +173.23% | bitget | +114.10% | okx | -59.13% |
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
