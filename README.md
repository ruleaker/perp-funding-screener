# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-26 05:14 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1282**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | STG | bitget | +587.58% |
| 2 | 龙虾 | bitget | +207.61% |
| 3 | CASHCAT | okx | +124.07% |
| 4 | FIGHT | bitget | +110.70% |
| 5 | FOLKS | bitget | +109.39% |
| 6 | PI | bitget | +104.68% |
| 7 | RAVE | okx | +100.83% |
| 8 | STONK | bitget | +85.74% |
| 9 | OKLO | okx | +78.97% |
| 10 | H | okx | +73.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | WAXP | bitget | -1418.02% |
| 2 | ONE | okx | -495.53% |
| 3 | STEEM | bitget | -406.03% |
| 4 | RARE | bitget | -354.45% |
| 5 | CVC | bitget | -188.01% |
| 6 | LSK | bitget | -185.60% |
| 7 | CXMT | okx | -115.70% |
| 8 | FLOCK | okx | -107.97% |
| 9 | FLOCK | bitget | -102.05% |
| 10 | ONE | bitget | -83.55% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +411.98% | bitget | -83.55% | okx | -495.53% |
| 2 | CXMT | +115.70% | bitget | +0.00% | okx | -115.70% |
| 3 | PI | +111.46% | bitget | +104.68% | okx | -6.78% |
| 4 | OKLO | +78.97% | okx | +78.97% | bitget | +0.00% |
| 5 | RAVE | +74.77% | okx | +100.83% | bitget | +26.06% |
| 6 | IRYS | +49.60% | bitget | +55.08% | okx | +5.47% |
| 7 | SOON | +48.92% | bitget | +59.68% | okx | +10.76% |
| 8 | EWZ | +46.61% | bitget | +0.00% | okx | -46.61% |
| 9 | APR | +39.39% | okx | +44.87% | bitget | +5.47% |
| 10 | RIVER | +38.45% | okx | +50.60% | bitget | +12.15% |
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
