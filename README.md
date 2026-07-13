# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-13 04:07 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1102**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +1095.00% |
| 2 | SKHYNIX | bitget | +547.50% |
| 3 | SAMSUNG | bitget | +463.40% |
| 4 | HYUNDAI | bitget | +380.62% |
| 5 | SAMSUNG | okx | +367.44% |
| 6 | KIOXIA | okx | +289.10% |
| 7 | MUU | okx | +277.82% |
| 8 | HYUNDAI | okx | +277.15% |
| 9 | RAM | okx | +170.60% |
| 10 | POPMART | bitget | +166.44% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 1000XEC | bitget | -1119.64% |
| 2 | HOT | bitget | -474.24% |
| 3 | DATA | okx | -388.10% |
| 4 | T | bitget | -334.63% |
| 5 | DATA | bitget | -282.95% |
| 6 | SXT | bitget | -279.23% |
| 7 | NATGAS | bitget | -262.91% |
| 8 | OGN | bitget | -248.89% |
| 9 | NEWT | bitget | -207.83% |
| 10 | SPELL | bitget | -197.98% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +547.50% | okx | +1095.00% | bitget | +547.50% |
| 2 | RAM | +336.27% | okx | +170.60% | bitget | -165.67% |
| 3 | KIOXIA | +289.10% | okx | +289.10% | bitget | +0.00% |
| 4 | MUU | +277.82% | okx | +277.82% | bitget | +0.00% |
| 5 | SKHY | +182.27% | bitget | +0.00% | okx | -182.27% |
| 6 | QNT | +141.71% | bitget | +10.95% | okx | -130.76% |
| 7 | MU | +125.20% | bitget | +0.00% | okx | -125.20% |
| 8 | DATA | +105.15% | bitget | -282.95% | okx | -388.10% |
| 9 | HYUNDAI | +103.47% | bitget | +380.62% | okx | +277.15% |
| 10 | CBRS | +100.38% | bitget | +0.00% | okx | -100.38% |
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
