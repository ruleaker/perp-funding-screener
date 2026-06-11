# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-11 12:26 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **978**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ARIA | bitget | +161.51% |
| 2 | POWER | bitget | +146.95% |
| 3 | LITE | okx | +132.61% |
| 4 | FOLKS | bitget | +100.52% |
| 5 | GOOGL | bitget | +85.63% |
| 6 | SKYAI | bitget | +80.15% |
| 7 | XPT | okx | +73.49% |
| 8 | CRDO | okx | +73.33% |
| 9 | RLS | okx | +73.25% |
| 10 | BMNR | okx | +64.49% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ID | bitget | -1965.20% |
| 2 | ASTR | bitget | -1556.43% |
| 3 | FIDA | bitget | -1326.37% |
| 4 | STG | bitget | -916.19% |
| 5 | HOME | okx | -515.34% |
| 6 | HOME | bitget | -435.04% |
| 7 | SXT | bitget | -372.08% |
| 8 | ESPORTS | bitget | -263.02% |
| 9 | H | okx | -227.96% |
| 10 | SAHARA | okx | -206.88% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +229.39% | bitget | +1.42% | okx | -227.96% |
| 2 | LITE | +132.61% | okx | +132.61% | bitget | +0.00% |
| 3 | SAHARA | +87.09% | bitget | -119.79% | okx | -206.88% |
| 4 | OP | +81.36% | okx | +10.95% | bitget | -70.41% |
| 5 | HOME | +80.30% | bitget | -435.04% | okx | -515.34% |
| 6 | GOOGL | +74.91% | bitget | +85.63% | okx | +10.72% |
| 7 | CRDO | +73.33% | okx | +73.33% | bitget | +0.00% |
| 8 | LA | +56.02% | bitget | +5.47% | okx | -50.55% |
| 9 | ZEC | +53.49% | bitget | -13.91% | okx | -67.40% |
| 10 | LDO | +53.32% | okx | +7.33% | bitget | -45.99% |
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
