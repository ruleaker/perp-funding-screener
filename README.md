# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-23 17:54 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KIOXIA | okx | +92.06% |
| 2 | XPD | okx | +85.48% |
| 3 | XPD | bitget | +68.66% |
| 4 | XPT | okx | +55.57% |
| 5 | XPT | bitget | +50.26% |
| 6 | SIREN | bitget | +49.17% |
| 7 | GOOGL | okx | +39.67% |
| 8 | SPCX | bitget | +39.42% |
| 9 | GOOGL | bitget | +37.12% |
| 10 | 1MCHEEMS | bitget | +36.68% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | DEXE | bitget | -683.94% |
| 2 | BARD | bitget | -441.94% |
| 3 | O | bitget | -337.48% |
| 4 | MIRA | bitget | -313.39% |
| 5 | TLM | bitget | -285.79% |
| 6 | O | okx | -221.49% |
| 7 | BARD | okx | -184.28% |
| 8 | ZKC | bitget | -127.68% |
| 9 | HOT | bitget | -124.17% |
| 10 | VANRY | bitget | -110.59% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BARD | +257.66% | okx | -184.28% | bitget | -441.94% |
| 2 | O | +115.99% | okx | -221.49% | bitget | -337.48% |
| 3 | KIOXIA | +92.06% | okx | +92.06% | bitget | +0.00% |
| 4 | RAY | +82.06% | bitget | +5.47% | okx | -76.59% |
| 5 | ALGO | +61.39% | bitget | +10.95% | okx | -50.44% |
| 6 | LA | +52.58% | okx | -6.33% | bitget | -58.91% |
| 7 | GRT | +36.58% | bitget | +10.95% | okx | -25.63% |
| 8 | COIN | +36.35% | bitget | +36.35% | okx | +0.00% |
| 9 | SNDK | +34.63% | bitget | -1.75% | okx | -36.38% |
| 10 | MOVE | +32.79% | bitget | +5.47% | okx | -27.32% |
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
