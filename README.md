# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-24 03:52 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TENCENT | bitget | +178.92% |
| 2 | SKHYNIX | bitget | +167.86% |
| 3 | SAMSUNG | bitget | +163.92% |
| 4 | SAMSUNG | okx | +156.71% |
| 5 | XPD | okx | +140.92% |
| 6 | SOXS | bitget | +116.18% |
| 7 | KIOXIA | okx | +110.82% |
| 8 | XPD | bitget | +107.42% |
| 9 | XPT | okx | +77.81% |
| 10 | LYN | bitget | +76.76% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BARD | bitget | -770.55% |
| 2 | BARD | okx | -422.27% |
| 3 | DEXE | bitget | -354.78% |
| 4 | TLM | bitget | -299.81% |
| 5 | KORU | bitget | -276.27% |
| 6 | O | bitget | -273.53% |
| 7 | PROM | bitget | -259.84% |
| 8 | ERA | bitget | -237.40% |
| 9 | ZKC | bitget | -192.72% |
| 10 | VELVET | bitget | -157.24% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BARD | +348.28% | okx | -422.27% | bitget | -770.55% |
| 2 | KORU | +276.27% | okx | +0.00% | bitget | -276.27% |
| 3 | RAM | +147.61% | okx | +0.00% | bitget | -147.61% |
| 4 | O | +135.17% | okx | -138.36% | bitget | -273.53% |
| 5 | SOXS | +116.18% | bitget | +116.18% | okx | +0.00% |
| 6 | SKHYNIX | +98.37% | bitget | +167.86% | okx | +69.49% |
| 7 | KIOXIA | +84.65% | okx | +110.82% | bitget | +26.17% |
| 8 | SNXX | +71.58% | bitget | -61.32% | okx | -132.90% |
| 9 | MUU | +67.23% | okx | +0.00% | bitget | -67.23% |
| 10 | ONE | +59.79% | okx | +5.47% | bitget | -54.31% |
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
