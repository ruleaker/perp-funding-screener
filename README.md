# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-17 13:39 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1257**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NKE | bitget | +378.98% |
| 2 | URNM | okx | +277.69% |
| 3 | FLNC | okx | +188.79% |
| 4 | CSOPSS2LHKD | bitget | +188.12% |
| 5 | FLY | bitget | +187.35% |
| 6 | CXMT | okx | +168.41% |
| 7 | SAMSUNG | okx | +160.47% |
| 8 | SKHYNIX | okx | +148.08% |
| 9 | SOFTBANK | bitget | +132.28% |
| 10 | CSOPSAMSUNG2L | okx | +131.71% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AVA | bitget | -1132.56% |
| 2 | ONE | bitget | -1057.66% |
| 3 | JMKE | bitget | -690.07% |
| 4 | ETN | bitget | -657.22% |
| 5 | HPQ | bitget | -601.48% |
| 6 | LSK | bitget | -427.60% |
| 7 | USO | okx | -345.98% |
| 8 | CVC | bitget | -290.50% |
| 9 | IOST | okx | -285.28% |
| 10 | IOST | bitget | -270.36% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +876.67% | okx | -180.99% | bitget | -1057.66% |
| 2 | FLNC | +188.79% | okx | +188.79% | bitget | +0.00% |
| 3 | FLY | +187.35% | bitget | +187.35% | okx | +0.00% |
| 4 | RDDT | +155.38% | okx | +0.00% | bitget | -155.38% |
| 5 | SOFTBANK | +132.28% | bitget | +132.28% | okx | +0.00% |
| 6 | HYUNDAI | +122.84% | okx | +122.84% | bitget | +0.00% |
| 7 | CGNX | +115.98% | bitget | +0.00% | okx | -115.98% |
| 8 | VRT | +100.19% | okx | +100.19% | bitget | +0.00% |
| 9 | APP | +94.02% | bitget | +0.00% | okx | -94.02% |
| 10 | SKHYNIX | +89.94% | okx | +148.08% | bitget | +58.14% |
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
