# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-17 18:39 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1328**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +1095.00% |
| 2 | EPIC | bitget | +72.38% |
| 3 | ELSA | bitget | +51.14% |
| 4 | CNPY | okx | +47.99% |
| 5 | AAOI | okx | +45.61% |
| 6 | PIPPIN | bitget | +41.50% |
| 7 | ZBT | okx | +29.67% |
| 8 | APR | okx | +28.55% |
| 9 | ARIA | bitget | +26.17% |
| 10 | NG | okx | +25.83% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAND | bitget | -581.01% |
| 2 | SAND | okx | -226.16% |
| 3 | DNA | okx | -162.92% |
| 4 | BR | bitget | -146.73% |
| 5 | ERA | bitget | -145.96% |
| 6 | BLUR | okx | -126.24% |
| 7 | ZIL | bitget | -107.42% |
| 8 | RSR | bitget | -105.23% |
| 9 | ZIL | okx | -89.85% |
| 10 | BLUR | bitget | -85.08% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1095.00% | okx | +1095.00% | bitget | +0.00% |
| 2 | SAND | +354.85% | okx | -226.16% | bitget | -581.01% |
| 3 | RSR | +106.35% | okx | +1.12% | bitget | -105.23% |
| 4 | NMR | +62.08% | bitget | +5.47% | okx | -56.61% |
| 5 | BAT | +48.49% | bitget | +10.95% | okx | -37.54% |
| 6 | AAOI | +45.61% | okx | +45.61% | bitget | +0.00% |
| 7 | ESP | +44.53% | bitget | +5.47% | okx | -39.06% |
| 8 | GMT | +42.27% | okx | +5.47% | bitget | -36.79% |
| 9 | BLUR | +41.16% | bitget | -85.08% | okx | -126.24% |
| 10 | EGLD | +36.79% | okx | +10.95% | bitget | -25.84% |
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
