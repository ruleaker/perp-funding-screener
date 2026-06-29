# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-29 05:09 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1049**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +718.91% |
| 2 | SAMSUNG | okx | +564.59% |
| 3 | SKHYNIX | bitget | +547.50% |
| 4 | SAMSUNG | bitget | +547.50% |
| 5 | HYUNDAI | bitget | +403.40% |
| 6 | HYUNDAI | okx | +325.24% |
| 7 | ISRG | okx | +284.58% |
| 8 | LRCX | okx | +188.64% |
| 9 | POET | okx | +175.71% |
| 10 | KORU | okx | +133.96% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | POWR | bitget | -1106.39% |
| 2 | RE | okx | -657.58% |
| 3 | RE | bitget | -603.35% |
| 4 | IP | okx | -488.72% |
| 5 | MAGIC | bitget | -388.94% |
| 6 | MAGIC | okx | -351.64% |
| 7 | BX | okx | -288.70% |
| 8 | TAIKO | bitget | -283.93% |
| 9 | CELO | bitget | -243.86% |
| 10 | LAB | bitget | -236.19% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BX | +288.70% | bitget | +0.00% | okx | -288.70% |
| 2 | ISRG | +284.58% | okx | +284.58% | bitget | +0.00% |
| 3 | LRCX | +188.64% | okx | +188.64% | bitget | +0.00% |
| 4 | POET | +175.71% | okx | +175.71% | bitget | +0.00% |
| 5 | SKHYNIX | +171.41% | okx | +718.91% | bitget | +547.50% |
| 6 | ACT | +162.48% | bitget | -72.93% | okx | -235.41% |
| 7 | KORU | +133.96% | okx | +133.96% | bitget | +0.00% |
| 8 | ZHIPU | +115.19% | bitget | +115.19% | okx | +0.00% |
| 9 | SOXL | +101.74% | okx | +101.74% | bitget | +0.00% |
| 10 | GLW | +94.98% | okx | +94.98% | bitget | +0.00% |
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
