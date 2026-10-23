# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-23 05:07 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1361**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAMSUNGEM | bitget | +379.20% |
| 2 | SKUU | bitget | +370.33% |
| 3 | RAM | bitget | +352.26% |
| 4 | BNC | bitget | +264.11% |
| 5 | LGELECTRONICS | bitget | +251.19% |
| 6 | HANMI | bitget | +235.42% |
| 7 | SHAZ | okx | +225.57% |
| 8 | PIPPIN | bitget | +180.78% |
| 9 | MVLL | bitget | +178.70% |
| 10 | INTW | bitget | +170.82% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BIRB | bitget | -1144.71% |
| 2 | AXIS | bitget | -1125.44% |
| 3 | H100 | okx | -1095.00% |
| 4 | UNITREE | okx | -719.78% |
| 5 | AXIS | okx | -633.84% |
| 6 | ALT | bitget | -569.73% |
| 7 | SKDD | bitget | -396.06% |
| 8 | UNITREE | bitget | -352.81% |
| 9 | BTW | bitget | -305.83% |
| 10 | BTW | okx | -257.24% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1100.47% | bitget | +5.47% | okx | -1095.00% |
| 2 | AXIS | +491.60% | okx | -633.84% | bitget | -1125.44% |
| 3 | SKDD | +427.73% | okx | +31.67% | bitget | -396.06% |
| 4 | UNITREE | +366.98% | bitget | -352.81% | okx | -719.78% |
| 5 | SKUU | +357.14% | bitget | +370.33% | okx | +13.19% |
| 6 | RAM | +314.28% | bitget | +352.26% | okx | +37.98% |
| 7 | LGELECTRONICS | +251.19% | bitget | +251.19% | okx | +0.00% |
| 8 | HANMI | +235.42% | bitget | +235.42% | okx | +0.00% |
| 9 | TMF | +211.71% | bitget | -16.75% | okx | -228.46% |
| 10 | MVLL | +178.70% | bitget | +178.70% | okx | +0.00% |
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
