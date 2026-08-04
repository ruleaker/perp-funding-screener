# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-04 18:10 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1166**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | COTI | bitget | +486.40% |
| 2 | SAMSUNG | okx | +243.68% |
| 3 | SKHYNIX | okx | +121.39% |
| 4 | GOOGL | bitget | +77.64% |
| 5 | ACX | bitget | +68.88% |
| 6 | NG | okx | +56.50% |
| 7 | SIREN | bitget | +54.31% |
| 8 | SKHYNIX | bitget | +44.13% |
| 9 | IDOL | bitget | +42.81% |
| 10 | SAMSUNG | bitget | +34.49% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -521.33% |
| 2 | SP500 | bitget | -178.27% |
| 3 | ACE | bitget | -168.74% |
| 4 | LA | okx | -167.66% |
| 5 | ESP | okx | -164.25% |
| 6 | HOME | okx | -164.05% |
| 7 | ESP | bitget | -149.47% |
| 8 | STORJ | bitget | -143.23% |
| 9 | NDX100 | bitget | -118.59% |
| 10 | LA | bitget | -109.28% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HOME | +357.28% | okx | -164.05% | bitget | -521.33% |
| 2 | SAMSUNG | +209.18% | okx | +243.68% | bitget | +34.49% |
| 3 | KORU | +90.67% | okx | +0.00% | bitget | -90.67% |
| 4 | ROK | +86.83% | okx | +0.00% | bitget | -86.83% |
| 5 | GOOGL | +77.64% | bitget | +77.64% | okx | +0.00% |
| 6 | SKHYNIX | +77.27% | okx | +121.39% | bitget | +44.13% |
| 7 | INTW | +66.20% | bitget | +0.00% | okx | -66.20% |
| 8 | KIOXIA | +62.03% | bitget | +19.93% | okx | -42.11% |
| 9 | ZIL | +60.68% | bitget | -13.03% | okx | -73.71% |
| 10 | SAND | +58.72% | bitget | +2.08% | okx | -56.64% |
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
