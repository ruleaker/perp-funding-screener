# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-24 05:07 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1281**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CYPH | okx | +328.62% |
| 2 | SHLD | okx | +232.33% |
| 3 | TMF | okx | +211.60% |
| 4 | XPD | okx | +178.85% |
| 5 | SOFTBANK | bitget | +158.56% |
| 6 | LUNR | okx | +136.43% |
| 7 | XPT | okx | +132.02% |
| 8 | POET | okx | +124.84% |
| 9 | ZHIPU | okx | +112.43% |
| 10 | KUAISHOU | bitget | +110.38% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CVC | bitget | -1145.15% |
| 2 | STEEM | bitget | -747.45% |
| 3 | ONE | bitget | -515.09% |
| 4 | CSOPSS2LHKD | bitget | -217.14% |
| 5 | CSOPSAMSUNG2L | okx | -158.99% |
| 6 | SNXX | bitget | -158.56% |
| 7 | KERNEL | bitget | -140.38% |
| 8 | LSK | bitget | -133.81% |
| 9 | HIVE | bitget | -133.70% |
| 10 | SHAZ | okx | -120.52% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +546.96% | okx | +31.87% | bitget | -515.09% |
| 2 | CYPH | +328.62% | okx | +328.62% | bitget | +0.00% |
| 3 | TMF | +211.60% | okx | +211.60% | bitget | +0.00% |
| 4 | POET | +124.84% | okx | +124.84% | bitget | +0.00% |
| 5 | SHAZ | +120.52% | bitget | +0.00% | okx | -120.52% |
| 6 | XPD | +113.91% | okx | +178.85% | bitget | +64.93% |
| 7 | MVLL | +102.16% | okx | +0.00% | bitget | -102.16% |
| 8 | FWDI | +100.27% | bitget | +0.00% | okx | -100.27% |
| 9 | MSTU | +93.29% | okx | +0.00% | bitget | -93.29% |
| 10 | BOT | +83.27% | okx | +83.27% | bitget | +0.00% |
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
