# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-17 12:17 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1328**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KIOXIA | okx | +107.20% |
| 2 | NVDL | okx | +96.96% |
| 3 | CNPY | okx | +88.25% |
| 4 | ARIA | bitget | +38.43% |
| 5 | ELSA | bitget | +33.18% |
| 6 | NG | okx | +32.89% |
| 7 | ZEST | bitget | +26.94% |
| 8 | ROK | okx | +25.12% |
| 9 | AAPL | okx | +23.01% |
| 10 | US500 | okx | +20.28% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ERA | bitget | -594.04% |
| 2 | SAND | bitget | -511.80% |
| 3 | RSR | bitget | -429.90% |
| 4 | SAND | okx | -402.08% |
| 5 | BR | bitget | -179.58% |
| 6 | BLUR | okx | -178.53% |
| 7 | DNA | okx | -159.83% |
| 8 | BLUR | bitget | -135.34% |
| 9 | ZIL | okx | -100.18% |
| 10 | KMNO | okx | -100.12% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RSR | +342.74% | okx | -87.15% | bitget | -429.90% |
| 2 | SAND | +109.72% | okx | -402.08% | bitget | -511.80% |
| 3 | KIOXIA | +107.20% | okx | +107.20% | bitget | +0.00% |
| 4 | NVDL | +96.96% | okx | +96.96% | bitget | +0.00% |
| 5 | KMNO | +75.37% | bitget | -24.75% | okx | -100.12% |
| 6 | DGAI | +73.96% | okx | -4.56% | bitget | -78.51% |
| 7 | SOXL | +56.85% | bitget | +0.00% | okx | -56.85% |
| 8 | BLUR | +43.19% | bitget | -135.34% | okx | -178.53% |
| 9 | H100 | +39.42% | bitget | +0.00% | okx | -39.42% |
| 10 | PROS | +36.13% | okx | +5.47% | bitget | -30.66% |
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
