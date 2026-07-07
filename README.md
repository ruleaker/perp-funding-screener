# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-07 04:31 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1097**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +741.94% |
| 2 | SKHYNIX | bitget | +547.50% |
| 3 | SAMSUNG | bitget | +545.86% |
| 4 | HYUNDAI | bitget | +461.21% |
| 5 | HYUNDAI | okx | +308.86% |
| 6 | SAMSUNG | okx | +300.75% |
| 7 | KIOXIA | okx | +207.48% |
| 8 | SOFTBANK | okx | +125.16% |
| 9 | SNDK | okx | +101.62% |
| 10 | KORU | okx | +85.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZHIPU | okx | -1095.00% |
| 2 | BLUR | bitget | -971.92% |
| 3 | MINIMAX | okx | -847.34% |
| 4 | LAB | bitget | -808.00% |
| 5 | LAB | okx | -728.60% |
| 6 | MINIMAX | bitget | -547.50% |
| 7 | ZHIPU | bitget | -547.50% |
| 8 | ID | bitget | -374.16% |
| 9 | BLUR | okx | -371.74% |
| 10 | POWER | bitget | -242.00% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BLUR | +600.18% | okx | -371.74% | bitget | -971.92% |
| 2 | ZHIPU | +547.50% | bitget | -547.50% | okx | -1095.00% |
| 3 | MINIMAX | +299.84% | bitget | -547.50% | okx | -847.34% |
| 4 | KORU | +275.37% | okx | +85.50% | bitget | -189.87% |
| 5 | SAMSUNG | +245.11% | bitget | +545.86% | okx | +300.75% |
| 6 | KIOXIA | +207.48% | okx | +207.48% | bitget | +0.00% |
| 7 | SKHYNIX | +194.44% | okx | +741.94% | bitget | +547.50% |
| 8 | SOXL | +168.58% | okx | +58.64% | bitget | -109.94% |
| 9 | HYUNDAI | +152.35% | bitget | +461.21% | okx | +308.86% |
| 10 | MUU | +127.98% | okx | +83.86% | bitget | -44.13% |
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
