# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-27 05:29 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1282**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | STONK | bitget | +112.35% |
| 2 | BIRB | bitget | +108.73% |
| 3 | JCT | bitget | +97.02% |
| 4 | AEON | bitget | +95.59% |
| 5 | CNPY | okx | +90.58% |
| 6 | VELODROME | bitget | +90.56% |
| 7 | NES | okx | +89.12% |
| 8 | US | bitget | +87.71% |
| 9 | FET | bitget | +78.40% |
| 10 | CP | bitget | +66.36% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | okx | -469.27% |
| 2 | RARE | bitget | -330.91% |
| 3 | 2Z | okx | -267.76% |
| 4 | 2Z | bitget | -242.76% |
| 5 | ESP | okx | -164.76% |
| 6 | ZEC | bitget | -154.83% |
| 7 | ESP | bitget | -131.73% |
| 8 | COW | bitget | -128.66% |
| 9 | QNT | bitget | -97.02% |
| 10 | INJ | okx | -96.59% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +399.41% | bitget | -69.86% | okx | -469.27% |
| 2 | ZEC | +152.90% | okx | -1.93% | bitget | -154.83% |
| 3 | INJ | +107.54% | bitget | +10.95% | okx | -96.59% |
| 4 | QNT | +97.02% | okx | +0.00% | bitget | -97.02% |
| 5 | AEON | +90.12% | bitget | +95.59% | okx | +5.47% |
| 6 | FET | +72.93% | bitget | +78.40% | okx | +5.47% |
| 7 | CXMT | +61.47% | bitget | +0.00% | okx | -61.47% |
| 8 | XTZ | +60.41% | bitget | +5.47% | okx | -54.94% |
| 9 | PI | +57.00% | bitget | +51.57% | okx | -5.42% |
| 10 | RIVER | +56.32% | okx | +61.79% | bitget | +5.47% |
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
