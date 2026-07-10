# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-10 18:07 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1102**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAMSUNG | okx | +103.27% |
| 2 | SIREN | bitget | +100.52% |
| 3 | LAB | okx | +90.84% |
| 4 | 1MCHEEMS | bitget | +72.49% |
| 5 | RKLB | okx | +70.05% |
| 6 | TUT | bitget | +68.11% |
| 7 | LAB | bitget | +67.23% |
| 8 | LUNR | okx | +56.21% |
| 9 | SOON | okx | +54.67% |
| 10 | GOOGL | bitget | +53.98% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKL | bitget | -727.96% |
| 2 | RARE | bitget | -592.29% |
| 3 | VANRY | bitget | -241.34% |
| 4 | SKHY | bitget | -194.14% |
| 5 | OGN | bitget | -173.78% |
| 6 | STXSTOCK | bitget | -165.02% |
| 7 | AI | okx | -160.14% |
| 8 | NATGAS | bitget | -146.62% |
| 9 | SPELL | bitget | -129.87% |
| 10 | RVN | okx | -109.30% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHY | +194.14% | okx | +0.00% | bitget | -194.14% |
| 2 | RVN | +112.80% | bitget | +3.50% | okx | -109.30% |
| 3 | SAMSUNG | +103.27% | okx | +103.27% | bitget | +0.00% |
| 4 | BAT | +77.53% | okx | +10.95% | bitget | -66.58% |
| 5 | PARTI | +61.14% | bitget | -7.99% | okx | -69.14% |
| 6 | SOON | +49.20% | okx | +54.67% | bitget | +5.47% |
| 7 | GMX | +48.27% | okx | +8.85% | bitget | -39.42% |
| 8 | PI | +47.24% | bitget | +5.47% | okx | -41.76% |
| 9 | STRC | +45.93% | okx | +45.93% | bitget | +0.00% |
| 10 | ADA | +44.41% | bitget | +9.75% | okx | -34.67% |
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
