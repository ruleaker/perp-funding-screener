# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-10 06:08 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **2977**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UAI | bybit | +118.65% |
| 2 | KII | okx | +105.90% |
| 3 | STG | bybit | +85.00% |
| 4 | UAI | bitget | +72.71% |
| 5 | REZ | bybit | +67.07% |
| 6 | US500 | okx | +64.28% |
| 7 | 1000BTT | bybit | +63.08% |
| 8 | AGI | bybit | +60.19% |
| 9 | TRUTH | okx | +59.40% |
| 10 | TRUTH | binance | +58.45% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -958.71% |
| 2 | MINA | bybit | -606.42% |
| 3 | RLC | bybit | -384.30% |
| 4 | KAIA | bybit | -357.97% |
| 5 | MINA | binance | -335.19% |
| 6 | MINA | bitget | -259.30% |
| 7 | KAIA | binance | -247.07% |
| 8 | MINA | okx | -246.02% |
| 9 | KAIA | bitget | -242.87% |
| 10 | RLC | binance | -208.91% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +958.71% | bitget | +0.00% | okx | -958.71% |
| 2 | MINA | +360.39% | okx | -246.02% | bybit | -606.42% |
| 3 | RLC | +175.40% | binance | -208.91% | bybit | -384.30% |
| 4 | KAIA | +115.10% | bitget | -242.87% | bybit | -357.97% |
| 5 | XDP | +105.16% | bybit | -29.00% | okx | -134.16% |
| 6 | 1000LUNC | +103.32% | binance | +10.95% | bybit | -92.37% |
| 7 | UAI | +89.19% | bybit | +118.65% | binance | +29.46% |
| 8 | KII | +89.17% | okx | +105.90% | bybit | +16.73% |
| 9 | PIXEL | +85.20% | bitget | +0.77% | binance | -84.44% |
| 10 | STG | +85.00% | bybit | +85.00% | binance | +0.00% |
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
