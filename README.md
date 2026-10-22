# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-22 05:07 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1352**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NATGAS | bitget | +446.10% |
| 2 | SAMSUNGEM | bitget | +312.18% |
| 3 | KR200 | okx | +296.76% |
| 4 | ZHONGJI | okx | +262.48% |
| 5 | LGELECTRONICS | bitget | +254.48% |
| 6 | SKDD | bitget | +234.77% |
| 7 | MINIMAX | okx | +218.80% |
| 8 | CYPH | okx | +212.16% |
| 9 | KR200 | bitget | +208.05% |
| 10 | HYUNDAI | okx | +206.79% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BIRB | bitget | -1500.48% |
| 2 | UNITREE | okx | -838.49% |
| 3 | AXIS | bitget | -735.73% |
| 4 | AXIS | okx | -623.23% |
| 5 | UNITREE | bitget | -465.59% |
| 6 | CT | okx | -402.49% |
| 7 | CT | bitget | -379.20% |
| 8 | MEW | bitget | -364.96% |
| 9 | IOTX | bitget | -278.68% |
| 10 | SKUU | bitget | -235.53% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | UNITREE | +372.89% | bitget | -465.59% | okx | -838.49% |
| 2 | CYPH | +340.49% | okx | +212.16% | bitget | -128.33% |
| 3 | MSTU | +293.27% | okx | +102.74% | bitget | -190.53% |
| 4 | SKDD | +283.36% | bitget | +234.77% | okx | -48.59% |
| 5 | SKUU | +270.41% | okx | +34.87% | bitget | -235.53% |
| 6 | LGELECTRONICS | +229.24% | bitget | +254.48% | okx | +25.24% |
| 7 | MVLL | +212.15% | okx | +11.11% | bitget | -201.04% |
| 8 | RAM | +209.25% | okx | +0.00% | bitget | -209.25% |
| 9 | MEW | +194.16% | okx | -170.81% | bitget | -364.96% |
| 10 | CVNA | +164.35% | bitget | +0.00% | okx | -164.35% |
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
