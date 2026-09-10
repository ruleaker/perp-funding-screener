# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-10 19:10 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1250**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +647.50% |
| 2 | KR200 | okx | +625.45% |
| 3 | NATGAS | bitget | +352.15% |
| 4 | NKE | bitget | +123.30% |
| 5 | XPD | okx | +109.17% |
| 6 | GPRO | bitget | +98.66% |
| 7 | GPRO | okx | +97.67% |
| 8 | ONE | okx | +78.30% |
| 9 | KORU | bitget | +75.01% |
| 10 | FIGHT | bitget | +69.31% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | USO | okx | -835.78% |
| 2 | VTHO | bitget | -823.66% |
| 3 | BZ | okx | -393.91% |
| 4 | BZ | bitget | -377.88% |
| 5 | CL | bitget | -342.30% |
| 6 | CL | okx | -338.93% |
| 7 | IOST | okx | -337.14% |
| 8 | RVN | bitget | -204.00% |
| 9 | CNPY | okx | -188.83% |
| 10 | IOST | bitget | -170.49% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KR200 | +625.45% | okx | +625.45% | bitget | +0.00% |
| 2 | IOST | +166.65% | bitget | -170.49% | okx | -337.14% |
| 3 | UNITREE | +128.72% | bitget | +0.00% | okx | -128.72% |
| 4 | SAMSUNG | +84.20% | bitget | +0.00% | okx | -84.20% |
| 5 | SOPH | +81.88% | bitget | -18.07% | okx | -99.95% |
| 6 | RVN | +73.60% | okx | -130.40% | bitget | -204.00% |
| 7 | ONE | +67.35% | okx | +78.30% | bitget | +10.95% |
| 8 | ZIL | +65.11% | bitget | -20.48% | okx | -85.58% |
| 9 | XPD | +61.87% | okx | +109.17% | bitget | +47.30% |
| 10 | RAY | +47.89% | bitget | -10.07% | okx | -57.96% |
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
