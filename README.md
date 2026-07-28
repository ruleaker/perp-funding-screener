# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-28 03:44 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1138**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | okx | +838.62% |
| 2 | GIGADEVICE | bitget | +547.50% |
| 3 | KR200 | okx | +515.69% |
| 4 | SAMSUNG | okx | +238.57% |
| 5 | SKHYNIX | okx | +230.86% |
| 6 | SKHYNIX | bitget | +206.52% |
| 7 | MAGMA | bitget | +196.66% |
| 8 | SAMSUNG | bitget | +164.36% |
| 9 | JCT | bitget | +162.72% |
| 10 | APR | bitget | +133.15% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LA | bitget | -897.68% |
| 2 | LA | okx | -800.16% |
| 3 | KORU | bitget | -293.13% |
| 4 | HOT | bitget | -193.81% |
| 5 | SOXS | okx | -191.57% |
| 6 | VANRY | bitget | -191.30% |
| 7 | BLEND | okx | -189.49% |
| 8 | T | bitget | -182.10% |
| 9 | COTI | bitget | -175.20% |
| 10 | RAM | bitget | -163.48% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | FWDI | +962.02% | okx | +838.62% | bitget | -123.41% |
| 2 | KORU | +293.13% | okx | +0.00% | bitget | -293.13% |
| 3 | SOXS | +237.67% | bitget | +46.10% | okx | -191.57% |
| 4 | RAM | +190.41% | okx | +26.92% | bitget | -163.48% |
| 5 | APR | +127.68% | bitget | +133.15% | okx | +5.47% |
| 6 | QNT | +106.53% | okx | +113.32% | bitget | +6.79% |
| 7 | AEHR | +106.04% | bitget | +0.00% | okx | -106.04% |
| 8 | BSP | +100.28% | okx | +100.28% | bitget | +0.00% |
| 9 | LA | +97.52% | okx | -800.16% | bitget | -897.68% |
| 10 | MVLL | +89.35% | okx | +0.00% | bitget | -89.35% |
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
