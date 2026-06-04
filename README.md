# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-04 11:28 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **941**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AAOI | okx | +134.39% |
| 2 | AVGO | okx | +132.03% |
| 3 | 龙虾 | bitget | +111.25% |
| 4 | SOXS | bitget | +109.50% |
| 5 | LUNR | okx | +109.25% |
| 6 | EWT | okx | +107.40% |
| 7 | SKHYNIX | bitget | +102.82% |
| 8 | GLW | okx | +99.28% |
| 9 | INX | bitget | +86.29% |
| 10 | CRWD | okx | +83.26% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | bitget | -1301.08% |
| 2 | LAB | okx | -1095.00% |
| 3 | HOME | bitget | -552.65% |
| 4 | HOME | okx | -410.47% |
| 5 | DRIFT | bitget | -276.71% |
| 6 | TRX | bitget | -245.83% |
| 7 | TRX | okx | -180.80% |
| 8 | COHR | okx | -172.18% |
| 9 | QCOM | okx | -119.51% |
| 10 | EWT | bitget | -109.50% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | EWT | +216.90% | okx | +107.40% | bitget | -109.50% |
| 2 | LAB | +206.08% | okx | -1095.00% | bitget | -1301.08% |
| 3 | COHR | +172.18% | bitget | +0.00% | okx | -172.18% |
| 4 | HOME | +142.18% | okx | -410.47% | bitget | -552.65% |
| 5 | AAOI | +134.39% | okx | +134.39% | bitget | +0.00% |
| 6 | QCOM | +119.51% | bitget | +0.00% | okx | -119.51% |
| 7 | AVGO | +107.50% | okx | +132.03% | bitget | +24.53% |
| 8 | RSR | +86.53% | bitget | +10.95% | okx | -75.58% |
| 9 | ARM | +84.92% | bitget | +0.00% | okx | -84.92% |
| 10 | DELL | +78.83% | bitget | +0.00% | okx | -78.83% |
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
