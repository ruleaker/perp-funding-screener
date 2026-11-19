# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-19 17:30 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1421**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ARQQ | bitget | +76.76% |
| 2 | SHEIN | okx | +74.68% |
| 3 | NVDL | okx | +51.31% |
| 4 | UP | okx | +48.82% |
| 5 | DXY | bitget | +48.40% |
| 6 | TLT | okx | +42.64% |
| 7 | EURUSD | bitget | +34.38% |
| 8 | SIREN | bitget | +33.95% |
| 9 | XPT | okx | +32.10% |
| 10 | KORU | bitget | +30.55% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | YB | okx | -1095.00% |
| 2 | YB | bitget | -1027.11% |
| 3 | CSOPSK2LHKD | bitget | -528.34% |
| 4 | IRYS | bitget | -506.11% |
| 5 | CSOPSS2LHKD | bitget | -503.26% |
| 6 | ZHONGJI | bitget | -406.90% |
| 7 | CSOPSAMSUNG2L | okx | -309.45% |
| 8 | KIOXIA | bitget | -300.03% |
| 9 | ZHONGJI | okx | -284.35% |
| 10 | ZKC | bitget | -277.25% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | IRYS | +244.33% | okx | -261.78% | bitget | -506.11% |
| 2 | BREV | +211.53% | bitget | -43.36% | okx | -254.89% |
| 3 | HUMA | +191.68% | bitget | -40.62% | okx | -232.31% |
| 4 | GTLB | +164.35% | bitget | +0.00% | okx | -164.35% |
| 5 | H100 | +134.13% | bitget | +5.47% | okx | -128.65% |
| 6 | SOFTBANK | +132.17% | okx | +0.00% | bitget | -132.17% |
| 7 | ZHONGJI | +122.55% | okx | -284.35% | bitget | -406.90% |
| 8 | MURATA | +121.98% | okx | +0.00% | bitget | -121.98% |
| 9 | SKHYNIX | +116.57% | bitget | -145.31% | okx | -261.88% |
| 10 | INIT | +111.88% | bitget | -36.35% | okx | -148.24% |
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
