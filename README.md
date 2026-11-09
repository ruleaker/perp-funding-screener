# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-09 18:58 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1412**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +1095.00% |
| 2 | NATGAS | bitget | +547.50% |
| 3 | 哈基米 | bitget | +515.09% |
| 4 | CSOPSK2LHKD | bitget | +402.63% |
| 5 | CSOPSS2LHKD | bitget | +345.91% |
| 6 | CSOPSAMSUNG2L | okx | +231.79% |
| 7 | CSOPSKHYNIX2L | okx | +218.59% |
| 8 | TWDELTA | bitget | +190.53% |
| 9 | SAMSUNG | okx | +183.66% |
| 10 | ZHONGJI | bitget | +164.36% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HUMA | okx | -476.35% |
| 2 | INIT | bitget | -359.71% |
| 3 | INIT | okx | -229.22% |
| 4 | AXIS | bitget | -221.19% |
| 5 | AXIS | okx | -152.98% |
| 6 | BZ | okx | -146.23% |
| 7 | BZ | bitget | -135.89% |
| 8 | HUMA | bitget | -125.05% |
| 9 | LSK | bitget | -118.59% |
| 10 | RSR | bitget | -118.37% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HUMA | +351.31% | bitget | -125.05% | okx | -476.35% |
| 2 | SAMSUNG | +183.66% | okx | +183.66% | bitget | +0.00% |
| 3 | SKHYNIX | +144.11% | okx | +144.11% | bitget | +0.00% |
| 4 | INIT | +130.49% | okx | -229.22% | bitget | -359.71% |
| 5 | SOFTBANK | +123.84% | bitget | +123.84% | okx | +0.00% |
| 6 | AERO | +116.95% | okx | +5.47% | bitget | -111.47% |
| 7 | H100 | +116.33% | bitget | +5.47% | okx | -110.86% |
| 8 | KR200 | +110.12% | okx | +110.12% | bitget | +0.00% |
| 9 | KIOXIA | +95.49% | bitget | +132.17% | okx | +36.68% |
| 10 | UNITREE | +93.66% | bitget | +0.00% | okx | -93.66% |
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
