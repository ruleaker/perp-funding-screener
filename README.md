# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-13 10:44 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **982**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SIREN | bitget | +209.25% |
| 2 | USO | okx | +145.32% |
| 3 | ACU | bitget | +99.10% |
| 4 | 龙虾 | bitget | +94.61% |
| 5 | QNT | okx | +93.10% |
| 6 | 1000RATS | bitget | +71.94% |
| 7 | LAB | bitget | +61.87% |
| 8 | AMD | okx | +59.29% |
| 9 | GME | okx | +57.62% |
| 10 | ROK | okx | +54.75% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | STG | bitget | -2299.50% |
| 2 | HOME | okx | -1017.48% |
| 3 | ESPORTS | bitget | -986.81% |
| 4 | H | okx | -837.06% |
| 5 | HOME | bitget | -754.67% |
| 6 | AXL | bitget | -348.54% |
| 7 | ENJ | okx | -158.83% |
| 8 | ENJ | bitget | -157.57% |
| 9 | BEAT | okx | -122.01% |
| 10 | SAHARA | okx | -119.14% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +827.75% | bitget | -9.31% | okx | -837.06% |
| 2 | HOME | +262.81% | bitget | -754.67% | okx | -1017.48% |
| 3 | ACU | +93.62% | bitget | +99.10% | okx | +5.47% |
| 4 | BEAT | +88.72% | bitget | -33.29% | okx | -122.01% |
| 5 | QNT | +82.15% | okx | +93.10% | bitget | +10.95% |
| 6 | SOPH | +82.05% | bitget | +5.47% | okx | -76.57% |
| 7 | CHZ | +62.94% | okx | -18.20% | bitget | -81.14% |
| 8 | AMD | +59.29% | okx | +59.29% | bitget | +0.00% |
| 9 | GME | +57.62% | okx | +57.62% | bitget | +0.00% |
| 10 | TON | +54.31% | bitget | -22.34% | okx | -76.65% |
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
