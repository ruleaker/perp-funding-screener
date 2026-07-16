# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-16 03:45 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1110**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +237.17% |
| 2 | SKHYNIX | bitget | +217.25% |
| 3 | KIOXIA | okx | +168.89% |
| 4 | HYUNDAI | okx | +151.45% |
| 5 | HYUNDAI | bitget | +146.73% |
| 6 | SIMO | okx | +123.17% |
| 7 | MINIMAX | bitget | +112.35% |
| 8 | BOT | bitget | +105.23% |
| 9 | BMNR | okx | +100.05% |
| 10 | MVLL | okx | +94.59% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -375.26% |
| 2 | HOME | okx | -356.29% |
| 3 | DATA | okx | -325.55% |
| 4 | DATA | bitget | -274.74% |
| 5 | BONK | okx | -261.69% |
| 6 | 1000BONK | bitget | -228.09% |
| 7 | VANRY | bitget | -181.99% |
| 8 | TLM | bitget | -164.80% |
| 9 | GWEI | bitget | -154.61% |
| 10 | SKL | bitget | -144.32% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KIOXIA | +168.89% | okx | +168.89% | bitget | +0.00% |
| 2 | BOT | +152.10% | bitget | +105.23% | okx | -46.87% |
| 3 | SIMO | +123.17% | okx | +123.17% | bitget | +0.00% |
| 4 | MINIMAX | +112.35% | bitget | +112.35% | okx | +0.00% |
| 5 | BMNR | +100.05% | okx | +100.05% | bitget | +0.00% |
| 6 | MVLL | +94.59% | okx | +94.59% | bitget | +0.00% |
| 7 | VANA | +71.12% | bitget | -41.28% | okx | -112.40% |
| 8 | SNXX | +61.33% | okx | +61.33% | bitget | +0.00% |
| 9 | QNT | +56.10% | okx | +67.05% | bitget | +10.95% |
| 10 | SAMSUNG | +54.26% | bitget | +62.52% | okx | +8.26% |
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
