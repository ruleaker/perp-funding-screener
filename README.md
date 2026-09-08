# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-08 04:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1240**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BNC | bitget | +321.27% |
| 2 | XIAOMI | okx | +313.18% |
| 3 | DISK | bitget | +252.84% |
| 4 | ZHIPU | okx | +224.17% |
| 5 | NG | okx | +197.73% |
| 6 | SKDD | okx | +185.43% |
| 7 | SAMSUNGEM | bitget | +164.47% |
| 8 | IONQ | okx | +149.94% |
| 9 | BRKB | okx | +148.55% |
| 10 | KORU | okx | +135.58% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CP | bitget | -1141.87% |
| 2 | CP | okx | -1095.00% |
| 3 | CFG | bitget | -297.95% |
| 4 | CXMT | bitget | -279.12% |
| 5 | CXMT | okx | -257.25% |
| 6 | SOPH | okx | -247.64% |
| 7 | T | bitget | -228.20% |
| 8 | ONG | bitget | -203.89% |
| 9 | ACE | bitget | -201.04% |
| 10 | ORCA | bitget | -122.86% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | XIAOMI | +248.13% | okx | +313.18% | bitget | +65.04% |
| 2 | SKDD | +228.90% | okx | +185.43% | bitget | -43.47% |
| 3 | SOPH | +155.88% | bitget | -91.76% | okx | -247.64% |
| 4 | IONQ | +149.94% | okx | +149.94% | bitget | +0.00% |
| 5 | BRKB | +148.55% | okx | +148.55% | bitget | +0.00% |
| 6 | ONE | +129.21% | bitget | +134.69% | okx | +5.47% |
| 7 | KORU | +115.76% | okx | +135.58% | bitget | +19.82% |
| 8 | POPMART | +102.46% | okx | +121.40% | bitget | +18.94% |
| 9 | ZHIPU | +99.01% | okx | +224.17% | bitget | +125.16% |
| 10 | SKUU | +84.21% | bitget | +84.21% | okx | +0.00% |
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
