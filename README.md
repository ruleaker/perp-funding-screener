# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-06 07:06 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1409**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +823.68% |
| 2 | NG | okx | +795.70% |
| 3 | TWDELTA | bitget | +525.93% |
| 4 | NATGAS | bitget | +514.98% |
| 5 | SKHYNIX | okx | +430.60% |
| 6 | NANYA | bitget | +308.68% |
| 7 | WINBOND | bitget | +291.60% |
| 8 | GIGADEV | okx | +288.75% |
| 9 | WALSIN | bitget | +274.52% |
| 10 | SKHYNIX | bitget | +256.45% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITREE | okx | -598.15% |
| 2 | ERA | bitget | -474.68% |
| 3 | HUMA | okx | -430.00% |
| 4 | HUMA | bitget | -235.86% |
| 5 | RUM | okx | -218.57% |
| 6 | AMC | okx | -209.58% |
| 7 | UNITREE | bitget | -204.44% |
| 8 | BRETT | bitget | -185.16% |
| 9 | POET | okx | -168.50% |
| 10 | FLY | okx | -165.94% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +818.20% | okx | +823.68% | bitget | +5.47% |
| 2 | UNITREE | +393.72% | bitget | -204.44% | okx | -598.15% |
| 3 | CYPH | +387.98% | okx | +255.70% | bitget | -132.28% |
| 4 | RUM | +218.57% | bitget | +0.00% | okx | -218.57% |
| 5 | AMC | +209.58% | bitget | +0.00% | okx | -209.58% |
| 6 | GEV | +205.99% | okx | +205.99% | bitget | +0.00% |
| 7 | HUMA | +194.14% | bitget | -235.86% | okx | -430.00% |
| 8 | BRETT | +190.64% | okx | +5.47% | bitget | -185.16% |
| 9 | SKHYNIX | +174.15% | okx | +430.60% | bitget | +256.45% |
| 10 | QNT | +172.77% | bitget | +10.95% | okx | -161.82% |
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
