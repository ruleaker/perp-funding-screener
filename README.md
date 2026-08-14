# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-14 09:33 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1179**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RDDT | bitget | +529.54% |
| 2 | BRKB | okx | +132.80% |
| 3 | ONE | okx | +115.50% |
| 4 | KUAISHOU | bitget | +111.91% |
| 5 | RLS | okx | +90.91% |
| 6 | XIAOMI | okx | +84.90% |
| 7 | ZM | okx | +84.48% |
| 8 | XPD | okx | +79.11% |
| 9 | 1000CAT | bitget | +67.12% |
| 10 | LAB | okx | +51.92% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | bitget | -1407.73% |
| 2 | 2Z | okx | -671.83% |
| 3 | 2Z | bitget | -613.31% |
| 4 | HOME | okx | -323.95% |
| 5 | HOME | bitget | -314.16% |
| 6 | COTI | bitget | -262.36% |
| 7 | HYUNDAI | okx | -224.99% |
| 8 | DOS | okx | -221.11% |
| 9 | DOS | bitget | -217.91% |
| 10 | KAITO | bitget | -194.47% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +1523.23% | okx | +115.50% | bitget | -1407.73% |
| 2 | RDDT | +482.68% | bitget | +529.54% | okx | +46.86% |
| 3 | HYUNDAI | +224.99% | bitget | +0.00% | okx | -224.99% |
| 4 | ZIL | +137.30% | okx | -20.82% | bitget | -158.12% |
| 5 | BRKB | +119.33% | okx | +132.80% | bitget | +13.47% |
| 6 | BSP | +110.26% | bitget | +0.00% | okx | -110.26% |
| 7 | CIEN | +89.46% | bitget | +0.00% | okx | -89.46% |
| 8 | XIAOMI | +84.90% | okx | +84.90% | bitget | +0.00% |
| 9 | ZM | +84.48% | okx | +84.48% | bitget | +0.00% |
| 10 | ATOM | +74.13% | okx | +10.95% | bitget | -63.18% |
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
