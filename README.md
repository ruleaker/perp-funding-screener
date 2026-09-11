# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-11 19:13 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1250**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +666.58% |
| 2 | NATGAS | bitget | +366.61% |
| 3 | ONE | okx | +164.40% |
| 4 | IONQ | okx | +88.38% |
| 5 | BNC | bitget | +88.26% |
| 6 | XPT | okx | +64.33% |
| 7 | XCU | okx | +49.13% |
| 8 | NKE | bitget | +39.31% |
| 9 | BSB | okx | +36.10% |
| 10 | VRT | okx | +34.88% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | USO | okx | -377.99% |
| 2 | BZ | bitget | -356.53% |
| 3 | BZ | okx | -346.35% |
| 4 | CL | bitget | -318.86% |
| 5 | IOST | okx | -318.17% |
| 6 | CL | okx | -308.94% |
| 7 | BLUR | okx | -207.40% |
| 8 | PIPPIN | bitget | -196.66% |
| 9 | LSK | bitget | -195.13% |
| 10 | VTHO | bitget | -193.49% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | IOST | +228.71% | bitget | -89.46% | okx | -318.17% |
| 2 | PIPPIN | +216.60% | okx | +19.94% | bitget | -196.66% |
| 3 | ONE | +153.45% | okx | +164.40% | bitget | +10.95% |
| 4 | RAY | +116.84% | bitget | +3.50% | okx | -113.34% |
| 5 | MINIMAX | +112.89% | okx | +0.00% | bitget | -112.89% |
| 6 | RVN | +78.74% | okx | -87.04% | bitget | -165.78% |
| 7 | IONQ | +63.96% | okx | +88.38% | bitget | +24.42% |
| 8 | MINA | +63.11% | okx | -2.48% | bitget | -65.59% |
| 9 | STRC | +59.36% | bitget | +0.00% | okx | -59.36% |
| 10 | BLUR | +55.53% | bitget | -151.88% | okx | -207.40% |
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
