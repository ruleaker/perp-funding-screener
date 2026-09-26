# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-26 13:16 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1282**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | STG | bitget | +436.69% |
| 2 | STONK | bitget | +191.95% |
| 3 | FIGHT | bitget | +191.30% |
| 4 | PI | bitget | +115.52% |
| 5 | IN | bitget | +90.34% |
| 6 | FOLKS | bitget | +89.35% |
| 7 | SOON | bitget | +86.94% |
| 8 | LAB | okx | +83.78% |
| 9 | CP | bitget | +77.09% |
| 10 | 龙虾 | bitget | +76.32% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RARE | bitget | -729.93% |
| 2 | WAXP | bitget | -656.34% |
| 3 | 2Z | okx | -439.45% |
| 4 | 2Z | bitget | -400.33% |
| 5 | ONE | okx | -399.51% |
| 6 | BR | bitget | -158.67% |
| 7 | STEEM | bitget | -112.46% |
| 8 | KII | okx | -111.65% |
| 9 | ONE | bitget | -84.75% |
| 10 | LSK | bitget | -57.71% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +314.76% | bitget | -84.75% | okx | -399.51% |
| 2 | PI | +133.25% | bitget | +115.52% | okx | -17.73% |
| 3 | LAB | +78.30% | okx | +83.78% | bitget | +5.47% |
| 4 | DOS | +63.84% | bitget | +69.31% | okx | +5.47% |
| 5 | CXMT | +52.27% | bitget | +0.00% | okx | -52.27% |
| 6 | COAI | +49.17% | bitget | +54.64% | okx | +5.47% |
| 7 | APR | +48.53% | okx | +54.01% | bitget | +5.47% |
| 8 | SOON | +44.24% | bitget | +86.94% | okx | +42.70% |
| 9 | MRK | +44.06% | bitget | +0.00% | okx | -44.06% |
| 10 | BAT | +41.26% | okx | +8.52% | bitget | -32.74% |
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
