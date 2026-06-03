# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-03 12:53 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **938**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BB | okx | +419.95% |
| 2 | EWT | okx | +360.89% |
| 3 | ADBE | okx | +343.90% |
| 4 | SHLD | okx | +258.70% |
| 5 | COHR | okx | +257.34% |
| 6 | NOK | okx | +247.32% |
| 7 | GME | okx | +224.43% |
| 8 | HPE | okx | +213.13% |
| 9 | NOW | okx | +189.13% |
| 10 | GLW | okx | +187.07% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -1495.99% |
| 2 | LAB | bitget | -1436.75% |
| 3 | LAB | okx | -1095.00% |
| 4 | HOME | okx | -934.22% |
| 5 | SLX | bitget | -801.87% |
| 6 | SLX | okx | -154.11% |
| 7 | LUNC | bitget | -81.80% |
| 8 | SOXL | bitget | -68.55% |
| 9 | CL | bitget | -42.60% |
| 10 | GUN | bitget | -39.42% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SLX | +647.76% | okx | -154.11% | bitget | -801.87% |
| 2 | HOME | +561.76% | okx | -934.22% | bitget | -1495.99% |
| 3 | BB | +414.47% | okx | +419.95% | bitget | +5.47% |
| 4 | EWT | +360.89% | okx | +360.89% | bitget | +0.00% |
| 5 | LAB | +341.75% | okx | -1095.00% | bitget | -1436.75% |
| 6 | GME | +224.43% | okx | +224.43% | bitget | +0.00% |
| 7 | COHR | +208.39% | okx | +257.34% | bitget | +48.95% |
| 8 | NOW | +189.13% | okx | +189.13% | bitget | +0.00% |
| 9 | AVGO | +183.26% | okx | +183.26% | bitget | +0.00% |
| 10 | AAOI | +181.70% | okx | +181.70% | bitget | +0.00% |
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
