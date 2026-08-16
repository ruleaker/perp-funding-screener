# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-16 08:54 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1185**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +91.32% |
| 2 | POWER | bitget | +75.66% |
| 3 | RLS | okx | +71.72% |
| 4 | 1000CAT | bitget | +67.34% |
| 5 | OKTA | okx | +57.51% |
| 6 | O | okx | +54.29% |
| 7 | TAC | bitget | +45.44% |
| 8 | LUMIA | bitget | +40.84% |
| 9 | SIREN | bitget | +40.84% |
| 10 | TRUTH | okx | +40.81% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | COW | bitget | -1220.93% |
| 2 | ACE | bitget | -1196.18% |
| 3 | WAL | bitget | -860.56% |
| 4 | WAL | okx | -744.21% |
| 5 | BICO | okx | -623.26% |
| 6 | BICO | bitget | -537.97% |
| 7 | STABLE | bitget | -195.35% |
| 8 | XAI | bitget | -187.79% |
| 9 | HOME | bitget | -186.04% |
| 10 | STABLE | okx | -181.65% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | WAL | +116.35% | okx | -744.21% | bitget | -860.56% |
| 2 | RVN | +111.17% | bitget | -21.57% | okx | -132.74% |
| 3 | ONE | +105.23% | okx | +5.47% | bitget | -99.75% |
| 4 | BICO | +85.28% | bitget | -537.97% | okx | -623.26% |
| 5 | O | +48.81% | okx | +54.29% | bitget | +5.47% |
| 6 | AEON | +43.45% | bitget | +5.47% | okx | -37.97% |
| 7 | ARKM | +34.93% | okx | +10.95% | bitget | -23.98% |
| 8 | ALGO | +33.75% | bitget | +3.72% | okx | -30.02% |
| 9 | WOO | +32.35% | bitget | +10.95% | okx | -21.40% |
| 10 | RSR | +32.08% | okx | +10.95% | bitget | -21.13% |
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
