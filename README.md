# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-01 06:15 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1291**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOXL | bitget | +428.80% |
| 2 | MVLL | bitget | +301.67% |
| 3 | SNXX | bitget | +275.50% |
| 4 | INTW | bitget | +231.15% |
| 5 | KORU | bitget | +227.65% |
| 6 | SNXX | okx | +213.35% |
| 7 | SKUU | bitget | +211.66% |
| 8 | ARM | bitget | +181.77% |
| 9 | RAM | bitget | +178.59% |
| 10 | CSOPSS2LHKD | bitget | +174.98% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HANMI | bitget | -663.57% |
| 2 | HANMI | okx | -640.74% |
| 3 | ARK | bitget | -477.20% |
| 4 | SOXS | bitget | -455.96% |
| 5 | CT | okx | -417.38% |
| 6 | SKDD | bitget | -150.12% |
| 7 | SQQQ | bitget | -137.64% |
| 8 | USDJPY | bitget | -91.21% |
| 9 | JP225 | bitget | -79.83% |
| 10 | LGELECTRONICS | bitget | -77.31% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SOXS | +461.04% | okx | +5.08% | bitget | -455.96% |
| 2 | SOXL | +428.80% | bitget | +428.80% | okx | +0.00% |
| 3 | MVLL | +305.54% | bitget | +301.67% | okx | -3.87% |
| 4 | INTW | +231.15% | bitget | +231.15% | okx | +0.00% |
| 5 | KORU | +211.41% | bitget | +227.65% | okx | +16.24% |
| 6 | SKUU | +186.75% | bitget | +211.66% | okx | +24.91% |
| 7 | ARM | +181.77% | bitget | +181.77% | okx | +0.00% |
| 8 | SQQQ | +156.99% | okx | +19.35% | bitget | -137.64% |
| 9 | TER | +153.19% | bitget | +153.19% | okx | +0.00% |
| 10 | SKDD | +150.12% | okx | +0.00% | bitget | -150.12% |
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
