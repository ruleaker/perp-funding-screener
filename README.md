# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-30 15:02 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1291**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GTLB | okx | +187.59% |
| 2 | PATH | bitget | +142.24% |
| 3 | UVXY | bitget | +108.08% |
| 4 | MP | bitget | +106.65% |
| 5 | SOFI | bitget | +99.54% |
| 6 | BRKB | okx | +94.73% |
| 7 | SOON | bitget | +93.29% |
| 8 | GPRO | bitget | +91.76% |
| 9 | TSLL | bitget | +85.52% |
| 10 | OKLO | bitget | +84.97% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FLOCK | bitget | -292.04% |
| 2 | CT | okx | -239.02% |
| 3 | BWET | bitget | -238.71% |
| 4 | BLSH | bitget | -238.16% |
| 5 | AGPU | bitget | -175.09% |
| 6 | JMKE | bitget | -174.43% |
| 7 | FLOCK | okx | -167.88% |
| 8 | ARK | bitget | -159.32% |
| 9 | MEW | bitget | -154.61% |
| 10 | MEW | okx | -150.45% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | GTLB | +187.59% | okx | +187.59% | bitget | +0.00% |
| 2 | FLOCK | +124.15% | okx | -167.88% | bitget | -292.04% |
| 3 | UVXY | +108.08% | bitget | +108.08% | okx | +0.00% |
| 4 | GPRO | +91.76% | bitget | +91.76% | okx | +0.00% |
| 5 | ALAB | +83.75% | bitget | +0.00% | okx | -83.75% |
| 6 | ADBE | +69.75% | bitget | +69.75% | okx | +0.00% |
| 7 | SOON | +57.59% | bitget | +93.29% | okx | +35.71% |
| 8 | ONE | +51.89% | okx | +5.90% | bitget | -45.99% |
| 9 | TRIA | +51.85% | okx | +57.33% | bitget | +5.47% |
| 10 | RDDT | +45.00% | bitget | +45.00% | okx | +0.00% |
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
