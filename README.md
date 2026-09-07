# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-07 04:59 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1236**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | XIAOMI | okx | +350.45% |
| 2 | SOFTBANK | okx | +235.03% |
| 3 | ONE | bitget | +190.09% |
| 4 | ZHIPU | okx | +189.62% |
| 5 | SOXL | okx | +177.17% |
| 6 | SAMSUNGEM | bitget | +148.70% |
| 7 | ZHIPU | bitget | +135.34% |
| 8 | HANMI | bitget | +123.95% |
| 9 | LGELECTRONICS | bitget | +113.22% |
| 10 | AAOI | okx | +111.55% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ORCA | bitget | -352.92% |
| 2 | CXMT | bitget | -332.88% |
| 3 | CXMT | okx | -281.34% |
| 4 | ACE | bitget | -277.58% |
| 5 | AKE | bitget | -263.68% |
| 6 | T | bitget | -254.37% |
| 7 | LA | okx | -152.91% |
| 8 | RAY | okx | -143.56% |
| 9 | LA | bitget | -129.65% |
| 10 | CFG | bitget | -125.05% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | XIAOMI | +311.03% | okx | +350.45% | bitget | +39.42% |
| 2 | ONE | +184.62% | bitget | +190.09% | okx | +5.47% |
| 3 | SOXL | +150.67% | okx | +177.17% | bitget | +26.50% |
| 4 | AAOI | +110.67% | okx | +111.55% | bitget | +0.88% |
| 5 | RAY | +102.50% | bitget | -41.06% | okx | -143.56% |
| 6 | INTC | +85.21% | okx | +88.61% | bitget | +3.39% |
| 7 | DRAM | +83.95% | okx | +83.95% | bitget | +0.00% |
| 8 | MU | +81.41% | okx | +82.28% | bitget | +0.88% |
| 9 | GPRO | +73.99% | okx | +40.05% | bitget | -33.95% |
| 10 | SMCI | +66.46% | okx | +66.46% | bitget | +0.00% |
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
