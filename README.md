# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-25 11:12 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1049**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GLW | okx | +323.10% |
| 2 | QNTSTOCK | bitget | +136.55% |
| 3 | BMNR | okx | +135.42% |
| 4 | DRAM | bitget | +134.36% |
| 5 | WEN | okx | +125.30% |
| 6 | SIREN | bitget | +119.03% |
| 7 | H | okx | +106.85% |
| 8 | SOXL | okx | +106.42% |
| 9 | ARQQ | bitget | +103.48% |
| 10 | GEV | okx | +102.00% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOXS | bitget | -547.50% |
| 2 | SATSSTOCK | bitget | -547.50% |
| 3 | AXON | bitget | -547.50% |
| 4 | BLEND | okx | -429.43% |
| 5 | LAB | okx | -421.95% |
| 6 | APLD | bitget | -329.38% |
| 7 | NES | okx | -288.99% |
| 8 | SIMO | bitget | -258.53% |
| 9 | M | bitget | -228.31% |
| 10 | PROS | bitget | -194.03% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LAB | +306.98% | bitget | -114.97% | okx | -421.95% |
| 2 | GLW | +269.33% | okx | +323.10% | bitget | +53.76% |
| 3 | UVXY | +173.12% | okx | +0.00% | bitget | -173.12% |
| 4 | SONY | +155.93% | okx | +0.00% | bitget | -155.93% |
| 5 | BMNR | +135.42% | okx | +135.42% | bitget | +0.00% |
| 6 | BX | +115.59% | okx | -11.43% | bitget | -127.02% |
| 7 | GEV | +102.00% | okx | +102.00% | bitget | +0.00% |
| 8 | H | +101.37% | okx | +106.85% | bitget | +5.47% |
| 9 | DRAM | +83.58% | bitget | +134.36% | okx | +50.78% |
| 10 | STRK | +79.15% | okx | -7.14% | bitget | -86.29% |
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
