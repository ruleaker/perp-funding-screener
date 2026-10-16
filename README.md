# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-16 19:37 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1328**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | USDESTOCK | bitget | +229.62% |
| 2 | CYPH | bitget | +128.01% |
| 3 | GPRO | bitget | +126.25% |
| 4 | AGPU | bitget | +124.28% |
| 5 | SECZ | okx | +122.24% |
| 6 | SOXL | bitget | +110.59% |
| 7 | ELSA | bitget | +74.02% |
| 8 | MSTU | bitget | +62.09% |
| 9 | NDX100 | bitget | +60.88% |
| 10 | SECZ | bitget | +60.66% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CSOPSK2LHKD | bitget | -212.54% |
| 2 | CSOPSS2LHKD | bitget | -197.65% |
| 3 | ZIL | bitget | -176.73% |
| 4 | BLUR | bitget | -152.53% |
| 5 | BLUR | okx | -145.30% |
| 6 | ZIL | okx | -134.47% |
| 7 | USO | okx | -131.39% |
| 8 | SAMSUNG | okx | -117.03% |
| 9 | SKHYNIX | okx | -105.45% |
| 10 | H100 | okx | -100.19% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | GPRO | +126.25% | bitget | +126.25% | okx | +0.00% |
| 2 | H100 | +100.19% | bitget | +0.00% | okx | -100.19% |
| 3 | CYPH | +98.56% | bitget | +128.01% | okx | +29.45% |
| 4 | SAMSUNG | +89.33% | bitget | -27.70% | okx | -117.03% |
| 5 | SOFTBANK | +88.37% | okx | +0.00% | bitget | -88.37% |
| 6 | SKHYNIX | +86.72% | bitget | -18.72% | okx | -105.45% |
| 7 | BAND | +66.19% | bitget | +10.95% | okx | -55.24% |
| 8 | UNITREE | +62.28% | bitget | +0.00% | okx | -62.28% |
| 9 | SECZ | +61.58% | okx | +122.24% | bitget | +60.66% |
| 10 | SOXL | +61.08% | bitget | +110.59% | okx | +49.51% |
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
