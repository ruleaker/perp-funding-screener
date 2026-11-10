# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-10 16:30 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1412**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +1013.88% |
| 2 | NATGAS | bitget | +547.50% |
| 3 | 哈基米 | bitget | +447.53% |
| 4 | QUBT | bitget | +136.22% |
| 5 | H100 | okx | +131.48% |
| 6 | SSPC | bitget | +123.95% |
| 7 | ECHO | bitget | +121.55% |
| 8 | SECZ | bitget | +118.81% |
| 9 | POET | bitget | +103.81% |
| 10 | CGNX | okx | +90.13% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | INIT | okx | -1095.00% |
| 2 | INIT | bitget | -846.33% |
| 3 | SHAZ | bitget | -193.49% |
| 4 | UNITREE | okx | -188.18% |
| 5 | HUMA | okx | -158.00% |
| 6 | CYBER | bitget | -154.29% |
| 7 | CSOPSK2LHKD | bitget | -147.50% |
| 8 | BSP | okx | -143.94% |
| 9 | GILD | bitget | -124.28% |
| 10 | 1000CAT | bitget | -118.92% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | INIT | +248.67% | bitget | -846.33% | okx | -1095.00% |
| 2 | SHAZ | +193.49% | okx | +0.00% | bitget | -193.49% |
| 3 | UNITREE | +188.18% | bitget | +0.00% | okx | -188.18% |
| 4 | SECZ | +139.25% | bitget | +118.81% | okx | -20.45% |
| 5 | H100 | +126.00% | okx | +131.48% | bitget | +5.47% |
| 6 | GILD | +124.28% | okx | +0.00% | bitget | -124.28% |
| 7 | HUMA | +109.38% | bitget | -48.62% | okx | -158.00% |
| 8 | POET | +103.81% | bitget | +103.81% | okx | +0.00% |
| 9 | AERO | +96.91% | okx | +5.47% | bitget | -91.43% |
| 10 | CGNX | +96.37% | okx | +90.13% | bitget | -6.24% |
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
