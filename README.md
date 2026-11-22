# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-22 21:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1423**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UP | okx | +130.90% |
| 2 | BAND | okx | +107.45% |
| 3 | SNXX | okx | +51.62% |
| 4 | SNXX | bitget | +44.57% |
| 5 | GRIFFAIN | bitget | +38.32% |
| 6 | NBIS | okx | +29.89% |
| 7 | NVDL | bitget | +24.97% |
| 8 | SNDK | okx | +23.71% |
| 9 | LAB | okx | +22.46% |
| 10 | THE | bitget | +21.79% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -2190.00% |
| 2 | ENSO | bitget | -553.85% |
| 3 | INIT | okx | -468.78% |
| 4 | H100 | okx | -457.76% |
| 5 | XVG | bitget | -362.55% |
| 6 | BARD | bitget | -303.97% |
| 7 | COST | okx | -278.95% |
| 8 | BARD | okx | -270.62% |
| 9 | IRYS | okx | -270.21% |
| 10 | CYBER | bitget | -262.58% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +463.24% | bitget | +5.47% | okx | -457.76% |
| 2 | ENSO | +334.08% | okx | -219.77% | bitget | -553.85% |
| 3 | INIT | +284.71% | bitget | -184.07% | okx | -468.78% |
| 4 | COST | +278.95% | bitget | +0.00% | okx | -278.95% |
| 5 | IRYS | +206.70% | bitget | -63.51% | okx | -270.21% |
| 6 | BAND | +96.50% | okx | +107.45% | bitget | +10.95% |
| 7 | GMT | +72.91% | bitget | -8.54% | okx | -81.45% |
| 8 | UNITREE | +69.88% | bitget | +0.00% | okx | -69.88% |
| 9 | ADI | +66.11% | bitget | +0.00% | okx | -66.11% |
| 10 | HUMA | +62.72% | bitget | -3.07% | okx | -65.78% |
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
