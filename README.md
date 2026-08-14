# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-14 03:05 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1179**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RDDT | bitget | +389.16% |
| 2 | XIAOMI | okx | +297.85% |
| 3 | RLS | okx | +166.48% |
| 4 | POPMART | okx | +159.10% |
| 5 | ONE | okx | +134.87% |
| 6 | XPD | okx | +114.38% |
| 7 | BRKB | okx | +105.25% |
| 8 | LAB | okx | +102.40% |
| 9 | POWER | bitget | +101.51% |
| 10 | SKHYNIX | okx | +84.10% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | bitget | -1275.67% |
| 2 | HOME | bitget | -717.88% |
| 3 | HOME | okx | -664.37% |
| 4 | MMT | okx | -331.19% |
| 5 | MMT | bitget | -302.77% |
| 6 | DOS | bitget | -291.93% |
| 7 | DOS | okx | -287.12% |
| 8 | MOVE | okx | -265.30% |
| 9 | MOVE | bitget | -238.49% |
| 10 | HYUNDAI | okx | -165.13% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +1410.54% | okx | +134.87% | bitget | -1275.67% |
| 2 | RDDT | +389.16% | bitget | +389.16% | okx | +0.00% |
| 3 | XIAOMI | +297.85% | okx | +297.85% | bitget | +0.00% |
| 4 | POPMART | +159.10% | okx | +159.10% | bitget | +0.00% |
| 5 | KORU | +105.67% | okx | +0.00% | bitget | -105.67% |
| 6 | SHAZ | +100.04% | bitget | +0.00% | okx | -100.04% |
| 7 | ZIL | +94.71% | okx | -11.07% | bitget | -105.78% |
| 8 | BICO | +74.34% | bitget | -68.99% | okx | -143.33% |
| 9 | BRKB | +73.60% | okx | +105.25% | bitget | +31.65% |
| 10 | HOME | +53.51% | okx | -664.37% | bitget | -717.88% |
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
