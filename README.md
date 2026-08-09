# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-09 09:09 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1164**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 龙虾 | bitget | +2190.00% |
| 2 | TUT | bitget | +2053.12% |
| 3 | BICO | bitget | +1519.97% |
| 4 | UNITAS | bitget | +295.87% |
| 5 | US | bitget | +148.59% |
| 6 | SOON | bitget | +136.44% |
| 7 | SKYAI | bitget | +131.29% |
| 8 | RLS | okx | +123.93% |
| 9 | SIREN | bitget | +106.76% |
| 10 | APR | okx | +98.26% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KAITO | bitget | -993.06% |
| 2 | KAITO | okx | -572.12% |
| 3 | IOTX | bitget | -560.75% |
| 4 | DEXE | bitget | -379.97% |
| 5 | BICO | okx | -374.80% |
| 6 | ZBT | okx | -223.95% |
| 7 | ZBT | bitget | -186.26% |
| 8 | COTI | bitget | -174.98% |
| 9 | BANK | bitget | -134.79% |
| 10 | KMNO | bitget | -98.22% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BICO | +1894.77% | bitget | +1519.97% | okx | -374.80% |
| 2 | KAITO | +420.93% | okx | -572.12% | bitget | -993.06% |
| 3 | SOON | +113.83% | bitget | +136.44% | okx | +22.60% |
| 4 | APR | +112.72% | okx | +98.26% | bitget | -14.45% |
| 5 | PIEVERSE | +78.51% | bitget | +83.99% | okx | +5.47% |
| 6 | KGEN | +60.84% | okx | +66.31% | bitget | +5.47% |
| 7 | ZIL | +58.22% | okx | -15.25% | bitget | -73.47% |
| 8 | AEON | +48.40% | bitget | +53.87% | okx | +5.47% |
| 9 | WET | +41.61% | bitget | +47.09% | okx | +5.47% |
| 10 | BILL | +39.56% | okx | +45.04% | bitget | +5.47% |
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
