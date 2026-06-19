# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-19 12:29 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1021**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAMSUNG | okx | +250.31% |
| 2 | US | bitget | +225.79% |
| 3 | SIREN | bitget | +209.25% |
| 4 | SKHYNIX | okx | +195.09% |
| 5 | ESPORTS | bitget | +190.64% |
| 6 | BTW | bitget | +170.82% |
| 7 | O | okx | +164.27% |
| 8 | GWEI | bitget | +146.73% |
| 9 | HIMS | okx | +93.80% |
| 10 | XPD | okx | +89.95% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RE | bitget | -2033.20% |
| 2 | RE | okx | -1095.00% |
| 3 | TRUST | okx | -657.64% |
| 4 | PRL | bitget | -507.86% |
| 5 | HOME | okx | -263.42% |
| 6 | FIDA | bitget | -230.28% |
| 7 | H | okx | -216.45% |
| 8 | SAHARA | bitget | -176.19% |
| 9 | H | bitget | -166.00% |
| 10 | SAHARA | okx | -137.73% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RE | +938.20% | okx | -1095.00% | bitget | -2033.20% |
| 2 | TRUST | +527.77% | bitget | -129.87% | okx | -657.64% |
| 3 | SAMSUNG | +250.31% | okx | +250.31% | bitget | +0.00% |
| 4 | SKHYNIX | +195.09% | okx | +195.09% | bitget | +0.00% |
| 5 | HOME | +189.51% | bitget | -73.91% | okx | -263.42% |
| 6 | XPD | +89.95% | okx | +89.95% | bitget | +0.00% |
| 7 | BICO | +77.55% | bitget | +10.95% | okx | -66.60% |
| 8 | XPT | +63.07% | okx | +63.07% | bitget | +0.00% |
| 9 | GLM | +60.01% | okx | +5.47% | bitget | -54.53% |
| 10 | ZORA | +58.04% | okx | -0.54% | bitget | -58.58% |
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
