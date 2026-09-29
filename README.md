# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-29 05:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1282**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BOT | okx | +361.37% |
| 2 | TOKYOEL | bitget | +236.74% |
| 3 | CYPH | okx | +236.35% |
| 4 | XIAOMI | bitget | +210.57% |
| 5 | XIAOMI | okx | +206.42% |
| 6 | XIAOMIHKD | bitget | +192.83% |
| 7 | CSOPSK2LHKD | bitget | +153.52% |
| 8 | KSTR | okx | +153.27% |
| 9 | MEITUAN | bitget | +139.94% |
| 10 | XPD | okx | +132.14% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | okx | -577.83% |
| 2 | HANMI | okx | -513.41% |
| 3 | HANMI | bitget | -471.73% |
| 4 | ONE | bitget | -189.22% |
| 5 | NMR | okx | -154.34% |
| 6 | CYPH | bitget | -141.47% |
| 7 | CNPY | okx | -110.30% |
| 8 | SOXL | bitget | -104.46% |
| 9 | CSOPSAMSUNG2L | okx | -93.78% |
| 10 | NIO | bitget | -84.21% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +388.61% | bitget | -189.22% | okx | -577.83% |
| 2 | CYPH | +377.83% | okx | +236.35% | bitget | -141.47% |
| 3 | BOT | +361.37% | okx | +361.37% | bitget | +0.00% |
| 4 | KSTR | +152.61% | okx | +153.27% | bitget | +0.66% |
| 5 | VRT | +110.48% | okx | +110.48% | bitget | +0.00% |
| 6 | SOXS | +108.04% | bitget | +111.25% | okx | +3.21% |
| 7 | SOXL | +104.46% | okx | +0.00% | bitget | -104.46% |
| 8 | XPD | +83.96% | okx | +132.14% | bitget | +48.18% |
| 9 | NMR | +83.71% | bitget | -70.63% | okx | -154.34% |
| 10 | POPMART | +82.67% | bitget | +82.67% | okx | +0.00% |
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
