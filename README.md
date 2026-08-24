# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-24 02:05 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1197**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BRKB | okx | +116.40% |
| 2 | 龙虾 | bitget | +112.68% |
| 3 | MRNA | okx | +93.39% |
| 4 | ONE | bitget | +92.20% |
| 5 | XIAOMI | okx | +87.06% |
| 6 | ESPORTS | bitget | +62.20% |
| 7 | CRCL | okx | +58.70% |
| 8 | FIGHT | bitget | +54.75% |
| 9 | SKDD | bitget | +48.40% |
| 10 | ARX | okx | +46.85% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -395.40% |
| 2 | ACE | bitget | -371.75% |
| 3 | HOME | okx | -370.13% |
| 4 | UNITREE | okx | -369.16% |
| 5 | MOVE | okx | -348.55% |
| 6 | MOVE | bitget | -343.39% |
| 7 | ONG | bitget | -337.92% |
| 8 | STORJ | bitget | -294.12% |
| 9 | ONT | okx | -228.98% |
| 10 | BICO | bitget | -226.77% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | UNITREE | +295.14% | bitget | -74.02% | okx | -369.16% |
| 2 | RVN | +181.64% | bitget | -20.04% | okx | -201.68% |
| 3 | SNXX | +171.69% | okx | +11.06% | bitget | -160.64% |
| 4 | BRKB | +116.40% | okx | +116.40% | bitget | +0.00% |
| 5 | BICO | +108.97% | okx | -117.81% | bitget | -226.77% |
| 6 | CXMT | +99.19% | bitget | -56.83% | okx | -156.02% |
| 7 | SKUU | +96.91% | okx | +0.00% | bitget | -96.91% |
| 8 | MVLL | +95.16% | okx | +0.00% | bitget | -95.16% |
| 9 | MRNA | +93.39% | okx | +93.39% | bitget | +0.00% |
| 10 | ONT | +91.12% | bitget | -137.86% | okx | -228.98% |
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
