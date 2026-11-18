# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-18 17:24 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1422**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ARTY | bitget | +300.47% |
| 2 | NVDL | okx | +53.88% |
| 3 | PIEVERSE | bitget | +49.49% |
| 4 | DXY | bitget | +49.49% |
| 5 | XPT | okx | +44.35% |
| 6 | VICR | okx | +44.15% |
| 7 | BOT | bitget | +38.87% |
| 8 | SOXL | bitget | +33.73% |
| 9 | MVLL | bitget | +32.74% |
| 10 | SOXL | okx | +32.57% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HUMA | okx | -1095.00% |
| 2 | ZKC | bitget | -844.57% |
| 3 | ZKP | bitget | -772.52% |
| 4 | HUMA | bitget | -415.22% |
| 5 | CSOPSK2LHKD | bitget | -361.79% |
| 6 | ZKP | okx | -353.70% |
| 7 | IRYS | bitget | -270.90% |
| 8 | KAVA | bitget | -231.04% |
| 9 | ZIL | okx | -217.34% |
| 10 | CSOPSS2LHKD | bitget | -200.49% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HUMA | +679.78% | bitget | -415.22% | okx | -1095.00% |
| 2 | ZKP | +418.82% | okx | -353.70% | bitget | -772.52% |
| 3 | IRYS | +167.88% | okx | -103.03% | bitget | -270.90% |
| 4 | SKHYNIX | +152.56% | bitget | -19.27% | okx | -171.83% |
| 5 | SOFTBANK | +141.15% | okx | +0.00% | bitget | -141.15% |
| 6 | KIOXIA | +110.49% | okx | +0.00% | bitget | -110.49% |
| 7 | MINIMAX | +74.56% | okx | -31.54% | bitget | -106.11% |
| 8 | ZIL | +71.71% | bitget | -145.63% | okx | -217.34% |
| 9 | UVXY | +71.43% | bitget | -57.27% | okx | -128.70% |
| 10 | KSTR | +68.36% | bitget | +0.00% | okx | -68.36% |
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
