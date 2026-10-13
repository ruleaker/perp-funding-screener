# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-13 21:23 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1317**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +1095.00% |
| 2 | NATGAS | bitget | +547.50% |
| 3 | AGPU | bitget | +441.28% |
| 4 | TBT | bitget | +160.97% |
| 5 | BWET | bitget | +149.58% |
| 6 | RUM | bitget | +142.57% |
| 7 | SECZ | bitget | +133.26% |
| 8 | DGAI | okx | +106.41% |
| 9 | TSEM | okx | +103.11% |
| 10 | KIOXIA | okx | +95.32% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -1014.07% |
| 2 | BLUR | okx | -846.22% |
| 3 | BLUR | bitget | -762.01% |
| 4 | ARC | bitget | -394.31% |
| 5 | USDESTOCK | bitget | -294.77% |
| 6 | CTK | bitget | -282.18% |
| 7 | RSR | bitget | -246.05% |
| 8 | BZ | okx | -216.51% |
| 9 | BZ | bitget | -208.93% |
| 10 | OKTA | okx | -203.27% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1014.07% | bitget | +0.00% | okx | -1014.07% |
| 2 | OKTA | +203.27% | bitget | +0.00% | okx | -203.27% |
| 3 | RSR | +176.88% | okx | -69.16% | bitget | -246.05% |
| 4 | QNT | +109.06% | okx | +60.44% | bitget | -48.62% |
| 5 | BWET | +104.22% | bitget | +149.58% | okx | +45.36% |
| 6 | TSEM | +103.11% | okx | +103.11% | bitget | +0.00% |
| 7 | DGAI | +100.93% | okx | +106.41% | bitget | +5.47% |
| 8 | KIOXIA | +95.32% | okx | +95.32% | bitget | +0.00% |
| 9 | BLUR | +84.21% | bitget | -762.01% | okx | -846.22% |
| 10 | CGNX | +78.40% | bitget | +0.00% | okx | -78.40% |
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
