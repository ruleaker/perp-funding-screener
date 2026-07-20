# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-20 04:12 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1118**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MINIMAX | okx | +382.30% |
| 2 | MINIMAX | bitget | +357.96% |
| 3 | ZHIPU | bitget | +340.87% |
| 4 | ZHIPU | okx | +330.41% |
| 5 | SAMSUNG | okx | +250.01% |
| 6 | SKHYNIX | bitget | +224.04% |
| 7 | HYUNDAI | okx | +161.87% |
| 8 | XPD | okx | +147.40% |
| 9 | HYUNDAI | bitget | +134.90% |
| 10 | SKHYNIX | okx | +126.44% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BOT | okx | -394.90% |
| 2 | HOME | bitget | -308.24% |
| 3 | HOME | okx | -282.95% |
| 4 | ACE | bitget | -253.93% |
| 5 | WEN | okx | -222.76% |
| 6 | TLM | bitget | -162.39% |
| 7 | VANRY | bitget | -134.90% |
| 8 | G | bitget | -110.81% |
| 9 | POET | okx | -110.81% |
| 10 | SKL | bitget | -103.04% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BOT | +394.90% | bitget | +0.00% | okx | -394.90% |
| 2 | WEN | +222.76% | bitget | +0.00% | okx | -222.76% |
| 3 | SAMSUNG | +125.07% | okx | +250.01% | bitget | +124.94% |
| 4 | POET | +110.81% | bitget | +0.00% | okx | -110.81% |
| 5 | TQQQ | +104.62% | okx | +104.62% | bitget | +0.00% |
| 6 | SONY | +99.25% | bitget | +0.00% | okx | -99.25% |
| 7 | SKHYNIX | +97.60% | bitget | +224.04% | okx | +126.44% |
| 8 | SOXL | +84.43% | okx | +84.43% | bitget | +0.00% |
| 9 | APLD | +83.57% | bitget | +0.00% | okx | -83.57% |
| 10 | SNOW | +75.08% | bitget | +0.00% | okx | -75.08% |
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
