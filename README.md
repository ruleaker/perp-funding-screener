# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-21 17:51 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1126**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +240.42% |
| 2 | SAMSUNG | okx | +194.75% |
| 3 | O | bitget | +194.25% |
| 4 | SIREN | bitget | +64.93% |
| 5 | LYN | bitget | +63.62% |
| 6 | GEV | okx | +54.37% |
| 7 | BOT | bitget | +51.14% |
| 8 | EPIC | bitget | +47.63% |
| 9 | SOON | bitget | +44.90% |
| 10 | M | bitget | +42.38% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ERA | bitget | -1163.44% |
| 2 | DEXE | bitget | -1161.80% |
| 3 | ONE | bitget | -1146.57% |
| 4 | ONE | okx | -755.35% |
| 5 | LA | bitget | -562.06% |
| 6 | HOME | okx | -387.56% |
| 7 | HOME | bitget | -317.00% |
| 8 | VANRY | bitget | -283.60% |
| 9 | ON | okx | -220.76% |
| 10 | LA | okx | -164.61% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LA | +397.45% | okx | -164.61% | bitget | -562.06% |
| 2 | ONE | +391.23% | okx | -755.35% | bitget | -1146.57% |
| 3 | SKHYNIX | +240.42% | okx | +240.42% | bitget | +0.00% |
| 4 | SAMSUNG | +194.75% | okx | +194.75% | bitget | +0.00% |
| 5 | O | +161.46% | bitget | +194.25% | okx | +32.79% |
| 6 | SOXS | +149.36% | okx | +0.00% | bitget | -149.36% |
| 7 | HOME | +70.56% | bitget | -317.00% | okx | -387.56% |
| 8 | GEV | +54.37% | okx | +54.37% | bitget | +0.00% |
| 9 | 1INCH | +40.21% | bitget | +10.95% | okx | -29.26% |
| 10 | PROS | +39.84% | bitget | +5.47% | okx | -34.36% |
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
