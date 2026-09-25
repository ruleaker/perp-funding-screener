# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-25 20:04 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1282**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | STG | bitget | +716.35% |
| 2 | BLESS | bitget | +244.73% |
| 3 | FIGHT | bitget | +187.79% |
| 4 | RAVE | okx | +164.64% |
| 5 | ARIA | bitget | +146.62% |
| 6 | B2 | bitget | +122.31% |
| 7 | SOON | bitget | +122.20% |
| 8 | QNT | okx | +121.79% |
| 9 | TRUTH | okx | +115.60% |
| 10 | CASHCAT | okx | +114.17% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | okx | -1095.00% |
| 2 | RARE | bitget | -394.31% |
| 3 | KII | okx | -362.32% |
| 4 | STEEM | bitget | -150.67% |
| 5 | LSK | bitget | -139.94% |
| 6 | FLOCK | okx | -78.10% |
| 7 | FLOCK | bitget | -67.12% |
| 8 | ONE | bitget | -62.74% |
| 9 | XAI | bitget | -60.88% |
| 10 | MINA | okx | -44.54% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +1032.26% | bitget | -62.74% | okx | -1095.00% |
| 2 | RAVE | +158.07% | okx | +164.64% | bitget | +6.57% |
| 3 | QNT | +110.84% | okx | +121.79% | bitget | +10.95% |
| 4 | BB | +92.82% | okx | +98.30% | bitget | +5.47% |
| 5 | LAB | +87.56% | okx | +93.04% | bitget | +5.47% |
| 6 | TSLA | +84.44% | bitget | +95.92% | okx | +11.48% |
| 7 | INTC | +82.02% | bitget | +82.23% | okx | +0.21% |
| 8 | SOON | +78.58% | bitget | +122.20% | okx | +43.63% |
| 9 | O | +58.72% | bitget | +92.42% | okx | +33.70% |
| 10 | GOOGL | +54.86% | bitget | +55.63% | okx | +0.77% |
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
