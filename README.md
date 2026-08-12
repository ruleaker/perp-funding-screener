# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-12 09:37 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1178**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | XIAOMI | okx | +491.31% |
| 2 | POPMART | okx | +358.12% |
| 3 | RIOT | okx | +177.79% |
| 4 | KOPN | bitget | +156.15% |
| 5 | 龙虾 | bitget | +125.92% |
| 6 | SIREN | bitget | +102.16% |
| 7 | NG | okx | +82.65% |
| 8 | UNITAS | bitget | +79.39% |
| 9 | ALAB | okx | +72.95% |
| 10 | TRUTH | okx | +71.25% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KAITO | bitget | -1631.77% |
| 2 | PROM | bitget | -1012.55% |
| 3 | STORJ | bitget | -935.68% |
| 4 | RVN | okx | -455.93% |
| 5 | FWDI | okx | -233.59% |
| 6 | RVN | bitget | -198.52% |
| 7 | KAITO | okx | -184.66% |
| 8 | EWH | bitget | -179.25% |
| 9 | EPIC | bitget | -143.01% |
| 10 | BOT | bitget | -143.01% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KAITO | +1447.11% | okx | -184.66% | bitget | -1631.77% |
| 2 | XIAOMI | +491.31% | okx | +491.31% | bitget | +0.00% |
| 3 | POPMART | +311.26% | okx | +358.12% | bitget | +46.87% |
| 4 | RVN | +257.41% | bitget | -198.52% | okx | -455.93% |
| 5 | FWDI | +233.59% | bitget | +0.00% | okx | -233.59% |
| 6 | APR | +147.21% | bitget | +5.47% | okx | -141.74% |
| 7 | BOT | +143.01% | okx | +0.00% | bitget | -143.01% |
| 8 | ALAB | +72.95% | okx | +72.95% | bitget | +0.00% |
| 9 | GEV | +59.78% | okx | +59.78% | bitget | +0.00% |
| 10 | APE | +57.47% | bitget | +10.95% | okx | -46.52% |
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
