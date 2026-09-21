# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-21 20:29 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1274**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KR200 | okx | +189.31% |
| 2 | NKE | bitget | +124.83% |
| 3 | MINIMAX | bitget | +121.65% |
| 4 | BTW | bitget | +108.08% |
| 5 | MINIMAX | okx | +104.71% |
| 6 | XPT | okx | +92.47% |
| 7 | HANMI | bitget | +82.23% |
| 8 | B2 | bitget | +80.81% |
| 9 | CSOPSKHYNIX2L | okx | +80.66% |
| 10 | ZHIPU | bitget | +74.13% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CELR | bitget | -828.48% |
| 2 | ONE | okx | -285.13% |
| 3 | PROVE | okx | -208.75% |
| 4 | PROVE | bitget | -182.65% |
| 5 | ONG | bitget | -55.19% |
| 6 | PI | bitget | -53.11% |
| 7 | AVA | bitget | -50.59% |
| 8 | IOST | okx | -47.63% |
| 9 | ZIL | bitget | -45.55% |
| 10 | VTHO | bitget | -44.02% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +248.89% | bitget | -36.24% | okx | -285.13% |
| 2 | KR200 | +189.31% | okx | +189.31% | bitget | +0.00% |
| 3 | HANMI | +82.23% | bitget | +82.23% | okx | +0.00% |
| 4 | PI | +58.58% | okx | +5.47% | bitget | -53.11% |
| 5 | ROBO | +56.42% | okx | +61.90% | bitget | +5.47% |
| 6 | XPT | +53.81% | okx | +92.47% | bitget | +38.65% |
| 7 | VRT | +48.16% | okx | +48.16% | bitget | +0.00% |
| 8 | SHELL | +45.33% | bitget | +50.81% | okx | +5.47% |
| 9 | SHEIN | +44.54% | okx | +44.54% | bitget | +0.00% |
| 10 | SAMSUNG | +43.93% | okx | +43.93% | bitget | +0.00% |
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
