# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-12 18:05 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1312**_
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
| 3 | AGPU | bitget | +312.73% |
| 4 | BWET | okx | +200.64% |
| 5 | RUM | bitget | +160.31% |
| 6 | MP | bitget | +136.88% |
| 7 | US100 | okx | +115.63% |
| 8 | SKUU | okx | +93.93% |
| 9 | SECZ | bitget | +89.46% |
| 10 | KORU | bitget | +84.10% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CTK | bitget | -1555.89% |
| 2 | RSR | bitget | -1374.99% |
| 3 | H100 | okx | -1095.00% |
| 4 | USO | okx | -438.86% |
| 5 | SKDD | okx | -291.73% |
| 6 | BZ | okx | -267.41% |
| 7 | SKL | bitget | -265.10% |
| 8 | BZ | bitget | -245.50% |
| 9 | SKDD | bitget | -234.77% |
| 10 | RSR | okx | -212.19% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RSR | +1162.80% | okx | -212.19% | bitget | -1374.99% |
| 2 | H100 | +1095.00% | bitget | +0.00% | okx | -1095.00% |
| 3 | BWET | +409.13% | okx | +200.64% | bitget | -208.49% |
| 4 | OKTA | +184.58% | bitget | +0.00% | okx | -184.58% |
| 5 | ONE | +108.30% | okx | +5.47% | bitget | -102.82% |
| 6 | AMC | +99.01% | okx | -56.04% | bitget | -155.05% |
| 7 | POET | +76.58% | okx | +76.58% | bitget | +0.00% |
| 8 | SHEIN | +72.08% | bitget | +0.00% | okx | -72.08% |
| 9 | SECZ | +71.38% | bitget | +89.46% | okx | +18.08% |
| 10 | SKDD | +56.96% | bitget | -234.77% | okx | -291.73% |
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
