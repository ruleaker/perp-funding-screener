# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-17 03:45 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1114**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | XIAOMI | bitget | +424.64% |
| 2 | SNXX | okx | +268.00% |
| 3 | ZHIPU | bitget | +263.24% |
| 4 | KIOXIA | okx | +253.78% |
| 5 | TQQQ | okx | +194.30% |
| 6 | MINIMAX | bitget | +192.17% |
| 7 | XPD | okx | +143.25% |
| 8 | XBI | okx | +135.04% |
| 9 | SNDK | okx | +133.16% |
| 10 | RAM | okx | +112.68% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -787.31% |
| 2 | HOME | okx | -710.06% |
| 3 | FLOCK | bitget | -631.60% |
| 4 | SKHYNIX | bitget | -402.74% |
| 5 | BONK | okx | -224.85% |
| 6 | SAMSUNG | okx | -211.04% |
| 7 | DATA | okx | -156.72% |
| 8 | LA | okx | -151.33% |
| 9 | OGN | bitget | -135.89% |
| 10 | KIOXIA | bitget | -134.90% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +410.45% | okx | +7.70% | bitget | -402.74% |
| 2 | KIOXIA | +388.68% | okx | +253.78% | bitget | -134.90% |
| 3 | SNXX | +268.00% | okx | +268.00% | bitget | +0.00% |
| 4 | ZHIPU | +263.24% | bitget | +263.24% | okx | +0.00% |
| 5 | SAMSUNG | +211.04% | bitget | +0.00% | okx | -211.04% |
| 6 | TQQQ | +194.30% | okx | +194.30% | bitget | +0.00% |
| 7 | MINIMAX | +192.17% | bitget | +192.17% | okx | +0.00% |
| 8 | XBI | +135.04% | okx | +135.04% | bitget | +0.00% |
| 9 | SNDK | +133.16% | okx | +133.16% | bitget | +0.00% |
| 10 | LA | +121.33% | bitget | -30.00% | okx | -151.33% |
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
