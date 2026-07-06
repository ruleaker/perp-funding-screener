# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-06 18:24 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1097**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SNDK | bitget | +130.31% |
| 2 | 龙虾 | bitget | +98.22% |
| 3 | RKLB | okx | +85.94% |
| 4 | SIREN | bitget | +78.62% |
| 5 | SPCX | bitget | +78.40% |
| 6 | SNDK | okx | +77.78% |
| 7 | SAMSUNG | okx | +67.16% |
| 8 | KLAC | okx | +65.70% |
| 9 | TAG | bitget | +65.04% |
| 10 | MRVL | bitget | +59.13% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BLUR | bitget | -1619.07% |
| 2 | BLUR | okx | -1095.00% |
| 3 | LAB | okx | -858.02% |
| 4 | SLX | okx | -611.65% |
| 5 | LAB | bitget | -493.74% |
| 6 | HOT | bitget | -296.64% |
| 7 | SLX | bitget | -248.46% |
| 8 | YFI | okx | -240.40% |
| 9 | GWEI | bitget | -149.14% |
| 10 | RPL | bitget | -144.76% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BLUR | +524.07% | okx | -1095.00% | bitget | -1619.07% |
| 2 | LAB | +364.29% | bitget | -493.74% | okx | -858.02% |
| 3 | SLX | +363.19% | bitget | -248.46% | okx | -611.65% |
| 4 | SAMSUNG | +67.16% | okx | +67.16% | bitget | +0.00% |
| 5 | KLAC | +65.70% | okx | +65.70% | bitget | +0.00% |
| 6 | WOO | +54.58% | bitget | +10.95% | okx | -43.63% |
| 7 | QNT | +53.78% | bitget | +10.95% | okx | -42.83% |
| 8 | SNDK | +52.52% | bitget | +130.31% | okx | +77.78% |
| 9 | KIOXIA | +51.89% | okx | +51.89% | bitget | +0.00% |
| 10 | SPCX | +50.64% | bitget | +78.40% | okx | +27.77% |
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
