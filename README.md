# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-11 05:07 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **974**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SHLD | okx | +386.79% |
| 2 | MTL | bitget | +351.17% |
| 3 | SKHYNIX | okx | +339.27% |
| 4 | BEAT | bitget | +173.89% |
| 5 | BEAT | okx | +148.43% |
| 6 | XPT | okx | +113.08% |
| 7 | SKHYNIX | bitget | +109.50% |
| 8 | GLW | okx | +97.13% |
| 9 | FOLKS | bitget | +95.37% |
| 10 | LITE | okx | +86.65% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ASTR | bitget | -1642.50% |
| 2 | HIVE | bitget | -778.65% |
| 3 | ESPORTS | bitget | -698.50% |
| 4 | ID | bitget | -474.79% |
| 5 | STG | bitget | -273.31% |
| 6 | HOME | okx | -247.14% |
| 7 | H | okx | -183.18% |
| 8 | SAHARA | bitget | -143.77% |
| 9 | LUNC | bitget | -98.33% |
| 10 | HOME | bitget | -93.73% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +229.77% | okx | +339.27% | bitget | +109.50% |
| 2 | H | +184.61% | bitget | +1.42% | okx | -183.18% |
| 3 | HOME | +153.41% | bitget | -93.73% | okx | -247.14% |
| 4 | GLW | +97.13% | okx | +97.13% | bitget | +0.00% |
| 5 | LITE | +86.65% | okx | +86.65% | bitget | +0.00% |
| 6 | SAHARA | +82.75% | okx | -61.03% | bitget | -143.77% |
| 7 | XPD | +78.80% | okx | +78.80% | bitget | +0.00% |
| 8 | XPT | +57.12% | okx | +113.08% | bitget | +55.95% |
| 9 | RDW | +56.48% | okx | +56.48% | bitget | +0.00% |
| 10 | QNT | +54.72% | okx | +65.67% | bitget | +10.95% |
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
