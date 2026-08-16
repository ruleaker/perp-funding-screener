# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-16 02:03 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1185**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | POWER | bitget | +102.16% |
| 2 | CYS | bitget | +96.47% |
| 3 | ESPORTS | bitget | +87.49% |
| 4 | RAVE | bitget | +84.53% |
| 5 | RLS | okx | +78.18% |
| 6 | ONE | okx | +68.87% |
| 7 | IDOL | bitget | +65.59% |
| 8 | 1000CAT | bitget | +59.02% |
| 9 | BEAT | okx | +58.70% |
| 10 | XIAOMI | okx | +55.03% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | WAL | bitget | -1675.46% |
| 2 | ACE | bitget | -1152.71% |
| 3 | COW | bitget | -1041.13% |
| 4 | BICO | okx | -865.07% |
| 5 | BICO | bitget | -838.77% |
| 6 | WAL | okx | -758.81% |
| 7 | HOME | bitget | -538.30% |
| 8 | HOME | okx | -499.94% |
| 9 | HOLO | bitget | -346.35% |
| 10 | ONE | bitget | -270.79% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | WAL | +916.65% | okx | -758.81% | bitget | -1675.46% |
| 2 | ONE | +339.67% | okx | +68.87% | bitget | -270.79% |
| 3 | RVN | +96.03% | bitget | -77.85% | okx | -173.88% |
| 4 | PIPPIN | +78.73% | okx | +5.47% | bitget | -73.26% |
| 5 | DOS | +71.06% | bitget | -45.00% | okx | -116.07% |
| 6 | ESP | +67.74% | bitget | +5.47% | okx | -62.27% |
| 7 | XIAOMI | +55.03% | okx | +55.03% | bitget | +0.00% |
| 8 | STABLE | +52.46% | bitget | -99.43% | okx | -151.89% |
| 9 | 1INCH | +51.23% | okx | -50.50% | bitget | -101.73% |
| 10 | BEAT | +50.49% | okx | +58.70% | bitget | +8.21% |
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
