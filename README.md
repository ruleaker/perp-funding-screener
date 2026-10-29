# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-29 21:16 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1380**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SHEIN | okx | +251.70% |
| 2 | TWLO | bitget | +230.17% |
| 3 | BWET | okx | +229.74% |
| 4 | EWZS | bitget | +207.50% |
| 5 | GPRO | bitget | +175.20% |
| 6 | CPNG | bitget | +151.44% |
| 7 | AXON | bitget | +150.67% |
| 8 | NTAP | bitget | +132.93% |
| 9 | RGTI | bitget | +128.99% |
| 10 | JOBY | bitget | +128.12% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | PARTI | bitget | -870.31% |
| 2 | UNITREE | okx | -524.23% |
| 3 | H100 | okx | -488.83% |
| 4 | CSOPSS2LHKD | bitget | -336.82% |
| 5 | PARTI | okx | -308.07% |
| 6 | CSOPSK2LHKD | bitget | -268.06% |
| 7 | LENOVOHKD | bitget | -250.32% |
| 8 | BLUR | bitget | -219.00% |
| 9 | ZHONGJI | bitget | -196.33% |
| 10 | BOT | okx | -195.06% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | PARTI | +562.24% | okx | -308.07% | bitget | -870.31% |
| 2 | UNITREE | +502.66% | bitget | -21.57% | okx | -524.23% |
| 3 | H100 | +494.31% | bitget | +5.47% | okx | -488.83% |
| 4 | SHEIN | +251.70% | okx | +251.70% | bitget | +0.00% |
| 5 | TWLO | +230.17% | bitget | +230.17% | okx | +0.00% |
| 6 | GPRO | +175.20% | bitget | +175.20% | okx | +0.00% |
| 7 | BOT | +166.26% | bitget | -28.80% | okx | -195.06% |
| 8 | BWET | +149.69% | okx | +229.74% | bitget | +80.04% |
| 9 | BLUR | +115.67% | okx | -103.33% | bitget | -219.00% |
| 10 | SHAZ | +101.85% | okx | -14.87% | bitget | -116.73% |
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
