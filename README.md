# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-18 16:56 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1194**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RAM | okx | +360.45% |
| 2 | RCAT | bitget | +154.72% |
| 3 | 1MCHEEMS | bitget | +116.07% |
| 4 | KIOXIA | okx | +103.25% |
| 5 | XPD | okx | +94.68% |
| 6 | BEAT | okx | +75.20% |
| 7 | OUST | okx | +74.12% |
| 8 | BOT | okx | +72.32% |
| 9 | RAM | bitget | +63.18% |
| 10 | SOXL | bitget | +58.80% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BICO | bitget | -541.26% |
| 2 | RED | bitget | -317.88% |
| 3 | RVN | okx | -302.39% |
| 4 | HOME | okx | -259.60% |
| 5 | HOME | bitget | -259.30% |
| 6 | SAMSUNG | okx | -199.84% |
| 7 | FLY | bitget | -158.23% |
| 8 | SKHYNIX | okx | -153.26% |
| 9 | PROM | bitget | -150.01% |
| 10 | ACE | bitget | -143.01% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BICO | +401.11% | okx | -140.15% | bitget | -541.26% |
| 2 | RAM | +297.27% | okx | +360.45% | bitget | +63.18% |
| 3 | RVN | +228.70% | bitget | -73.69% | okx | -302.39% |
| 4 | SAMSUNG | +178.27% | bitget | -21.57% | okx | -199.84% |
| 5 | FLY | +158.23% | okx | +0.00% | bitget | -158.23% |
| 6 | SKHYNIX | +116.25% | bitget | -37.01% | okx | -153.26% |
| 7 | ROK | +106.03% | bitget | +0.00% | okx | -106.03% |
| 8 | KIOXIA | +103.25% | okx | +103.25% | bitget | +0.00% |
| 9 | DATA | +92.08% | bitget | -17.85% | okx | -109.93% |
| 10 | AEHR | +76.51% | bitget | +0.00% | okx | -76.51% |
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
