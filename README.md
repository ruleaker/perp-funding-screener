# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-09 04:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1239**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SHLD | okx | +338.76% |
| 2 | GPRO | okx | +327.54% |
| 3 | BOT | okx | +288.46% |
| 4 | HANMI | bitget | +266.63% |
| 5 | NG | okx | +263.34% |
| 6 | SAMSUNGEM | bitget | +201.70% |
| 7 | NAVER | bitget | +191.30% |
| 8 | IONQ | okx | +163.35% |
| 9 | XIAOMI | okx | +149.94% |
| 10 | BYD | bitget | +99.32% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MIRA | bitget | -614.19% |
| 2 | CXMT | okx | -319.33% |
| 3 | CXMT | bitget | -233.78% |
| 4 | ACE | bitget | -217.47% |
| 5 | AKE | bitget | -168.74% |
| 6 | KAT | okx | -132.24% |
| 7 | CL | okx | -103.14% |
| 8 | CL | bitget | -99.64% |
| 9 | KAT | bitget | -94.28% |
| 10 | BZ | bitget | -92.75% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | GPRO | +316.70% | okx | +327.54% | bitget | +10.84% |
| 2 | BOT | +288.46% | okx | +288.46% | bitget | +0.00% |
| 3 | IONQ | +163.35% | okx | +163.35% | bitget | +0.00% |
| 4 | XIAOMI | +128.37% | okx | +149.94% | bitget | +21.57% |
| 5 | CXMT | +85.55% | bitget | -233.78% | okx | -319.33% |
| 6 | PIPPIN | +77.64% | bitget | +83.11% | okx | +5.47% |
| 7 | BRKB | +69.60% | okx | +69.60% | bitget | +0.00% |
| 8 | ONE | +67.67% | bitget | +73.15% | okx | +5.47% |
| 9 | ZHIPU | +49.51% | okx | +84.23% | bitget | +34.71% |
| 10 | SHAZ | +39.81% | bitget | +0.00% | okx | -39.81% |
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
