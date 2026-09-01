# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-01 05:23 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1211**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | QNT | okx | +187.66% |
| 2 | TMF | okx | +124.96% |
| 3 | ZM | okx | +119.23% |
| 4 | XIAOMI | okx | +114.08% |
| 5 | XPD | okx | +106.05% |
| 6 | NES | okx | +101.10% |
| 7 | LYN | bitget | +99.75% |
| 8 | HSI | bitget | +88.48% |
| 9 | CXMT | okx | +86.08% |
| 10 | MVLL | okx | +76.83% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TUT | bitget | -395.95% |
| 2 | SKR | bitget | -309.45% |
| 3 | SAND | okx | -305.28% |
| 4 | 0G | okx | -299.94% |
| 5 | SAND | bitget | -292.15% |
| 6 | 0G | bitget | -292.15% |
| 7 | FLOCK | bitget | -290.94% |
| 8 | UNITREE | okx | -272.03% |
| 9 | BSP | okx | -191.79% |
| 10 | MIRA | bitget | -180.57% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BSP | +191.79% | bitget | +0.00% | okx | -191.79% |
| 2 | QNT | +176.71% | okx | +187.66% | bitget | +10.95% |
| 3 | TMF | +124.96% | okx | +124.96% | bitget | +0.00% |
| 4 | UNITREE | +121.46% | bitget | -150.56% | okx | -272.03% |
| 5 | ZM | +119.23% | okx | +119.23% | bitget | +0.00% |
| 6 | XIAOMI | +114.08% | okx | +114.08% | bitget | +0.00% |
| 7 | ZORA | +90.85% | okx | -58.62% | bitget | -149.47% |
| 8 | ANIME | +86.15% | bitget | -55.84% | okx | -141.99% |
| 9 | CXMT | +86.08% | okx | +86.08% | bitget | +0.00% |
| 10 | MVLL | +76.83% | okx | +76.83% | bitget | +0.00% |
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
