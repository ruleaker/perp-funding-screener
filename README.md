# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-14 17:25 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1185**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RDDT | bitget | +241.01% |
| 2 | RAM | okx | +140.04% |
| 3 | 1000CAT | bitget | +87.82% |
| 4 | RAVE | bitget | +84.64% |
| 5 | RAVE | okx | +77.74% |
| 6 | ESPORTS | bitget | +77.09% |
| 7 | UNITAS | bitget | +75.77% |
| 8 | LAB | okx | +72.24% |
| 9 | GRIFFAIN | bitget | +69.20% |
| 10 | PROS | bitget | +66.58% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ALICE | bitget | -800.55% |
| 2 | BICO | okx | -690.17% |
| 3 | BICO | bitget | -638.38% |
| 4 | HOME | bitget | -572.58% |
| 5 | HOME | okx | -507.00% |
| 6 | SKUU | bitget | -262.58% |
| 7 | SAMSUNG | okx | -211.46% |
| 8 | RVN | okx | -161.03% |
| 9 | ONE | bitget | -157.46% |
| 10 | KAITO | okx | -141.95% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RDDT | +241.01% | bitget | +241.01% | okx | +0.00% |
| 2 | SKUU | +214.42% | okx | -48.16% | bitget | -262.58% |
| 3 | SAMSUNG | +186.06% | bitget | -25.40% | okx | -211.46% |
| 4 | ONE | +162.94% | okx | +5.47% | bitget | -157.46% |
| 5 | RAM | +140.04% | okx | +140.04% | bitget | +0.00% |
| 6 | AEHR | +111.99% | bitget | +0.00% | okx | -111.99% |
| 7 | RVN | +90.73% | bitget | -70.30% | okx | -161.03% |
| 8 | SKHYNIX | +86.84% | bitget | -30.44% | okx | -117.28% |
| 9 | ZIL | +78.30% | okx | -4.59% | bitget | -82.89% |
| 10 | HOME | +65.57% | okx | -507.00% | bitget | -572.58% |
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
