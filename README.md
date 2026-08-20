# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-20 01:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1192**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KORU | bitget | +248.02% |
| 2 | SKUU | okx | +192.12% |
| 3 | XPD | okx | +178.92% |
| 4 | CSOPSK2LHKD | bitget | +143.55% |
| 5 | CSOPSS2LHKD | bitget | +141.69% |
| 6 | ZHIPU | okx | +128.43% |
| 7 | MINIMAX | okx | +109.68% |
| 8 | XPD | bitget | +108.84% |
| 9 | LYTE | okx | +107.79% |
| 10 | ESPORTS | bitget | +98.33% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -552.65% |
| 2 | HOME | okx | -541.69% |
| 3 | EWH | bitget | -280.21% |
| 4 | PROM | bitget | -268.93% |
| 5 | ACE | bitget | -244.19% |
| 6 | BICO | bitget | -237.72% |
| 7 | HYUNDAI | bitget | -146.84% |
| 8 | BOT | okx | -100.46% |
| 9 | RVN | okx | -98.76% |
| 10 | DOS | okx | -79.78% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KORU | +237.43% | bitget | +248.02% | okx | +10.59% |
| 2 | BICO | +196.00% | okx | -41.72% | bitget | -237.72% |
| 3 | SKUU | +173.28% | okx | +192.12% | bitget | +18.83% |
| 4 | RVN | +104.24% | bitget | +5.47% | okx | -98.76% |
| 5 | BOT | +100.46% | bitget | +0.00% | okx | -100.46% |
| 6 | LYTE | +87.75% | okx | +107.79% | bitget | +20.04% |
| 7 | HYUNDAI | +82.94% | okx | -63.90% | bitget | -146.84% |
| 8 | EWY | +82.78% | bitget | +82.78% | okx | +0.00% |
| 9 | KIOXIA | +76.13% | okx | +76.13% | bitget | +0.00% |
| 10 | XPD | +70.08% | okx | +178.92% | bitget | +108.84% |
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
