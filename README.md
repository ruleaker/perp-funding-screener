# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-20 11:19 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1117**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AMC | bitget | +213.53% |
| 2 | MINIMAX | okx | +212.52% |
| 3 | ZHIPU | okx | +182.94% |
| 4 | MINIMAX | bitget | +167.32% |
| 5 | ZHIPU | bitget | +141.69% |
| 6 | FLY | bitget | +133.26% |
| 7 | SIREN | bitget | +86.94% |
| 8 | BANK | bitget | +84.86% |
| 9 | NOK | okx | +71.96% |
| 10 | MVLL | okx | +68.23% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOXS | bitget | -547.50% |
| 2 | ACE | bitget | -405.81% |
| 3 | ALICE | bitget | -401.54% |
| 4 | TLM | bitget | -237.62% |
| 5 | VANRY | bitget | -127.79% |
| 6 | HOME | okx | -109.08% |
| 7 | RE | bitget | -104.79% |
| 8 | EWH | bitget | -91.21% |
| 9 | HOME | bitget | -88.69% |
| 10 | ZIL | okx | -87.73% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SOXS | +546.15% | okx | -1.35% | bitget | -547.50% |
| 2 | ZIL | +93.20% | bitget | +5.47% | okx | -87.73% |
| 3 | CGNX | +68.31% | bitget | +0.00% | okx | -68.31% |
| 4 | MVLL | +68.23% | okx | +68.23% | bitget | +0.00% |
| 5 | COHR | +67.14% | okx | +67.14% | bitget | +0.00% |
| 6 | PROS | +59.02% | bitget | +5.47% | okx | -53.54% |
| 7 | O | +57.08% | okx | +62.55% | bitget | +5.47% |
| 8 | MET | +51.33% | bitget | +5.47% | okx | -45.86% |
| 9 | NBIS | +50.31% | okx | +50.31% | bitget | +0.00% |
| 10 | NEO | +49.07% | okx | +10.53% | bitget | -38.54% |
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
