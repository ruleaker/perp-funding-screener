# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-27 14:09 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1282**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KII | okx | +203.52% |
| 2 | CNPY | okx | +134.29% |
| 3 | STONK | bitget | +111.36% |
| 4 | 龙虾 | bitget | +108.19% |
| 5 | AEON | bitget | +95.70% |
| 6 | FET | bitget | +90.45% |
| 7 | ROK | okx | +84.91% |
| 8 | SIREN | bitget | +84.86% |
| 9 | BIRB | bitget | +80.92% |
| 10 | MMT | bitget | +77.85% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | okx | -429.62% |
| 2 | LSK | bitget | -362.99% |
| 3 | 2Z | bitget | -136.77% |
| 4 | ZEC | bitget | -114.54% |
| 5 | 2Z | okx | -109.45% |
| 6 | INJ | okx | -92.80% |
| 7 | RARE | bitget | -83.88% |
| 8 | JASMY | bitget | -65.48% |
| 9 | VTHO | bitget | -61.65% |
| 10 | CVC | bitget | -60.99% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +393.70% | bitget | -35.92% | okx | -429.62% |
| 2 | INJ | +103.75% | bitget | +10.95% | okx | -92.80% |
| 3 | ZEC | +96.03% | okx | -18.51% | bitget | -114.54% |
| 4 | PI | +94.89% | bitget | +65.70% | okx | -29.19% |
| 5 | AEON | +90.23% | bitget | +95.70% | okx | +5.47% |
| 6 | FET | +84.97% | bitget | +90.45% | okx | +5.47% |
| 7 | ROK | +84.91% | okx | +84.91% | bitget | +0.00% |
| 8 | MMT | +72.38% | bitget | +77.85% | okx | +5.47% |
| 9 | RIVER | +58.30% | okx | +43.52% | bitget | -14.78% |
| 10 | CXMT | +54.26% | bitget | +0.00% | okx | -54.26% |
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
