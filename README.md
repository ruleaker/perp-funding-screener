# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-07 06:19 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1412**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 哈基米 | bitget | +772.74% |
| 2 | KII | okx | +134.41% |
| 3 | ARIA | bitget | +127.79% |
| 4 | BRETT | bitget | +98.55% |
| 5 | DNA | okx | +89.39% |
| 6 | UP | okx | +82.64% |
| 7 | ETHW | bitget | +76.98% |
| 8 | APR | okx | +71.57% |
| 9 | RLS | okx | +52.14% |
| 10 | SIREN | bitget | +50.70% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -473.57% |
| 2 | LSK | bitget | -283.60% |
| 3 | CHILLGUY | bitget | -273.86% |
| 4 | ERA | bitget | -264.33% |
| 5 | HUMA | okx | -208.11% |
| 6 | 龙虾 | bitget | -157.68% |
| 7 | 1MCHEEMS | bitget | -133.81% |
| 8 | HOT | bitget | -110.16% |
| 9 | HUMA | bitget | -108.51% |
| 10 | AERO | bitget | -98.44% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +479.04% | bitget | +5.47% | okx | -473.57% |
| 2 | HUMA | +99.59% | bitget | -108.51% | okx | -208.11% |
| 3 | BRETT | +93.08% | bitget | +98.55% | okx | +5.47% |
| 4 | IMX | +90.12% | okx | +5.47% | bitget | -84.64% |
| 5 | APR | +65.65% | okx | +71.57% | bitget | +5.91% |
| 6 | ETHW | +62.81% | bitget | +76.98% | okx | +14.17% |
| 7 | XIAOMI | +62.64% | bitget | +0.00% | okx | -62.64% |
| 8 | AERO | +52.06% | okx | -46.38% | bitget | -98.44% |
| 9 | PURR | +49.75% | bitget | +0.00% | okx | -49.75% |
| 10 | ONE | +46.06% | okx | -36.50% | bitget | -82.56% |
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
