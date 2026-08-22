# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-22 16:47 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1197**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 龙虾 | bitget | +78.18% |
| 2 | ONE | okx | +69.58% |
| 3 | BEAT | okx | +65.94% |
| 4 | PROM | bitget | +61.54% |
| 5 | XVG | bitget | +49.82% |
| 6 | TRIA | okx | +39.05% |
| 7 | ZEST | bitget | +38.00% |
| 8 | METIS | okx | +36.55% |
| 9 | SONIC | bitget | +32.41% |
| 10 | FARTCOIN | okx | +32.17% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | COTI | bitget | -413.14% |
| 2 | MOVE | okx | -265.86% |
| 3 | ACE | bitget | -192.17% |
| 4 | MOVE | bitget | -172.13% |
| 5 | BICO | bitget | -156.80% |
| 6 | ONT | bitget | -151.33% |
| 7 | RVN | okx | -141.11% |
| 8 | UNITREE | okx | -121.90% |
| 9 | HOME | bitget | -116.40% |
| 10 | ONG | bitget | -92.09% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | UNITREE | +121.90% | bitget | +0.00% | okx | -121.90% |
| 2 | RVN | +116.48% | bitget | -24.64% | okx | -141.11% |
| 3 | BICO | +94.96% | okx | -61.84% | bitget | -156.80% |
| 4 | MOVE | +93.72% | bitget | -172.13% | okx | -265.86% |
| 5 | ONT | +63.76% | okx | -87.57% | bitget | -151.33% |
| 6 | ONE | +58.63% | okx | +69.58% | bitget | +10.95% |
| 7 | BB | +58.47% | bitget | +5.47% | okx | -53.00% |
| 8 | BEAT | +42.06% | okx | +65.94% | bitget | +23.87% |
| 9 | TRIA | +33.57% | okx | +39.05% | bitget | +5.47% |
| 10 | HOME | +32.31% | okx | -84.09% | bitget | -116.40% |
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
