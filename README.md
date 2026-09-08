# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-08 12:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1238**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BNC | bitget | +1095.00% |
| 2 | NG | okx | +299.91% |
| 3 | ZS | bitget | +217.91% |
| 4 | IONQ | okx | +186.49% |
| 5 | NATGAS | bitget | +167.75% |
| 6 | XPD | okx | +120.93% |
| 7 | IONQ | bitget | +111.91% |
| 8 | ONE | bitget | +111.47% |
| 9 | AVGO | bitget | +99.43% |
| 10 | JCT | bitget | +83.66% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOPH | bitget | -1140.88% |
| 2 | SOPH | okx | -1095.00% |
| 3 | INDA | bitget | -325.98% |
| 4 | BX | okx | -311.56% |
| 5 | ACE | bitget | -215.06% |
| 6 | BZ | bitget | -180.35% |
| 7 | SHLD | okx | -174.35% |
| 8 | BZ | okx | -172.63% |
| 9 | CL | bitget | -151.44% |
| 10 | CL | okx | -140.58% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BX | +311.56% | bitget | +0.00% | okx | -311.56% |
| 2 | GPRO | +75.67% | okx | +75.67% | bitget | +0.00% |
| 3 | IONQ | +74.58% | okx | +186.49% | bitget | +111.91% |
| 4 | ONE | +70.70% | bitget | +111.47% | okx | +40.77% |
| 5 | XPD | +50.52% | okx | +120.93% | bitget | +70.41% |
| 6 | SOPH | +45.88% | okx | -1095.00% | bitget | -1140.88% |
| 7 | VRT | +44.87% | okx | +44.87% | bitget | +0.00% |
| 8 | SHAZ | +41.79% | bitget | +0.00% | okx | -41.79% |
| 9 | GLM | +40.19% | bitget | -15.33% | okx | -55.52% |
| 10 | PIPPIN | +39.18% | okx | +32.72% | bitget | -6.46% |
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
