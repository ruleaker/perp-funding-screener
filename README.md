# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-21 05:12 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1264**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BNC | bitget | +312.51% |
| 2 | SHLD | okx | +296.38% |
| 3 | GPRO | okx | +235.66% |
| 4 | AIN | bitget | +202.57% |
| 5 | RIOT | okx | +157.97% |
| 6 | ON | okx | +140.90% |
| 7 | INTW | bitget | +134.14% |
| 8 | STONK | bitget | +133.15% |
| 9 | HYUNDAI | okx | +131.55% |
| 10 | SKHYNIX | okx | +125.68% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CELR | bitget | -990.76% |
| 2 | LGELECTRONICS | bitget | -620.87% |
| 3 | ONE | okx | -618.76% |
| 4 | SAMSUNGEM | bitget | -389.38% |
| 5 | HANMI | bitget | -370.99% |
| 6 | SKL | bitget | -265.76% |
| 7 | ONG | bitget | -224.04% |
| 8 | G | bitget | -223.38% |
| 9 | LGELECTRONICS | okx | -191.20% |
| 10 | CXMT | okx | -188.16% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +511.78% | bitget | -106.98% | okx | -618.76% |
| 2 | LGELECTRONICS | +429.66% | okx | -191.20% | bitget | -620.87% |
| 3 | HANMI | +370.99% | okx | +0.00% | bitget | -370.99% |
| 4 | GPRO | +235.66% | okx | +235.66% | bitget | +0.00% |
| 5 | EGLD | +139.38% | okx | -18.74% | bitget | -158.12% |
| 6 | BOT | +134.30% | bitget | +78.62% | okx | -55.68% |
| 7 | INTW | +134.14% | bitget | +134.14% | okx | +0.00% |
| 8 | KR200 | +123.13% | bitget | -7.77% | okx | -130.90% |
| 9 | CRO | +108.08% | bitget | +119.03% | okx | +10.95% |
| 10 | TSEM | +86.78% | bitget | +0.00% | okx | -86.78% |
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
