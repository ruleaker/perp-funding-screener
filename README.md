# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-22 05:39 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1021**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +706.64% |
| 2 | SAMSUNG | okx | +539.34% |
| 3 | GEV | okx | +479.61% |
| 4 | INFQ | okx | +351.90% |
| 5 | BMNR | okx | +288.45% |
| 6 | RDW | okx | +271.73% |
| 7 | ALAB | okx | +257.68% |
| 8 | GLW | okx | +219.73% |
| 9 | SIREN | bitget | +200.49% |
| 10 | QNT | okx | +171.84% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ID | bitget | -1285.75% |
| 2 | TNSR | bitget | -1050.76% |
| 3 | SHLD | okx | -663.22% |
| 4 | TAIKO | bitget | -596.45% |
| 5 | H | bitget | -439.53% |
| 6 | SYN | bitget | -340.76% |
| 7 | RE | bitget | -217.25% |
| 8 | FIDA | bitget | -214.51% |
| 9 | H | okx | -203.57% |
| 10 | HOME | okx | -197.49% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +597.14% | okx | +706.64% | bitget | +109.50% |
| 2 | SAMSUNG | +429.84% | okx | +539.34% | bitget | +109.50% |
| 3 | INFQ | +351.90% | okx | +351.90% | bitget | +0.00% |
| 4 | BMNR | +288.45% | okx | +288.45% | bitget | +0.00% |
| 5 | RDW | +271.73% | okx | +271.73% | bitget | +0.00% |
| 6 | ALAB | +257.68% | okx | +257.68% | bitget | +0.00% |
| 7 | H | +235.97% | okx | -203.57% | bitget | -439.53% |
| 8 | GLW | +219.73% | okx | +219.73% | bitget | +0.00% |
| 9 | QNT | +168.12% | okx | +171.84% | bitget | +3.72% |
| 10 | HOME | +153.80% | bitget | -43.69% | okx | -197.49% |
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
