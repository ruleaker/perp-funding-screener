# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-04 10:31 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1078**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RDW | okx | +174.70% |
| 2 | TAG | bitget | +130.09% |
| 3 | IDOL | bitget | +50.70% |
| 4 | MRVL | okx | +49.75% |
| 5 | DEXE | bitget | +43.91% |
| 6 | SIREN | bitget | +42.81% |
| 7 | EPIC | bitget | +42.16% |
| 8 | ZEST | bitget | +39.75% |
| 9 | AAOI | okx | +30.68% |
| 10 | SOXL | okx | +30.53% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 10000NEX | bitget | -847.42% |
| 2 | MIRA | bitget | -840.74% |
| 3 | SLX | okx | -531.25% |
| 4 | STORJ | bitget | -463.40% |
| 5 | LAB | okx | -412.84% |
| 6 | GWEI | bitget | -307.69% |
| 7 | RE | bitget | -137.09% |
| 8 | RE | okx | -133.67% |
| 9 | BIRB | bitget | -94.17% |
| 10 | NEWT | bitget | -89.79% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SLX | +536.07% | bitget | +4.82% | okx | -531.25% |
| 2 | LAB | +420.40% | bitget | +7.56% | okx | -412.84% |
| 3 | RDW | +174.70% | okx | +174.70% | bitget | +0.00% |
| 4 | KSM | +71.60% | okx | -3.18% | bitget | -74.79% |
| 5 | MRVL | +49.75% | okx | +49.75% | bitget | +0.00% |
| 6 | ROBO | +46.99% | bitget | -36.46% | okx | -83.46% |
| 7 | ZKP | +44.07% | bitget | -24.09% | okx | -68.16% |
| 8 | BARD | +38.40% | okx | -30.26% | bitget | -68.66% |
| 9 | MANA | +37.38% | bitget | +10.95% | okx | -26.43% |
| 10 | GLM | +37.32% | bitget | +5.47% | okx | -31.85% |
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
