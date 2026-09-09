# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-09 19:21 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1247**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +752.15% |
| 2 | NATGAS | bitget | +388.83% |
| 3 | BNC | bitget | +268.38% |
| 4 | CSOPSKHYNIX2L | okx | +166.48% |
| 5 | TEM | bitget | +133.37% |
| 6 | SKHYNIX | okx | +119.69% |
| 7 | NKE | bitget | +116.29% |
| 8 | CSOPSK2LHKD | bitget | +110.59% |
| 9 | IONQ | okx | +103.92% |
| 10 | SHOP | okx | +102.06% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | IOST | bitget | -1769.85% |
| 2 | IOST | okx | -1095.00% |
| 3 | 牛来 | bitget | -540.93% |
| 4 | BZ | bitget | -332.22% |
| 5 | BZ | okx | -321.56% |
| 6 | SKUU | bitget | -318.86% |
| 7 | CL | bitget | -281.96% |
| 8 | CL | okx | -270.57% |
| 9 | SKUU | okx | -262.04% |
| 10 | USO | okx | -198.08% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | IOST | +674.85% | okx | -1095.00% | bitget | -1769.85% |
| 2 | RAY | +119.41% | bitget | -69.75% | okx | -189.16% |
| 3 | ZIL | +106.85% | bitget | +5.47% | okx | -101.37% |
| 4 | SHOP | +102.06% | okx | +102.06% | bitget | +0.00% |
| 5 | SKHYNIX | +89.80% | okx | +119.69% | bitget | +29.89% |
| 6 | VRT | +82.56% | okx | +82.56% | bitget | +0.00% |
| 7 | RDW | +71.54% | okx | +71.54% | bitget | +0.00% |
| 8 | QNT | +66.08% | okx | +77.03% | bitget | +10.95% |
| 9 | GPRO | +63.29% | bitget | +63.29% | okx | +0.00% |
| 10 | UNITREE | +59.37% | bitget | +0.00% | okx | -59.37% |
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
