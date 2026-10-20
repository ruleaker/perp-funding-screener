# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-20 20:03 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1344**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KR200 | okx | +105.12% |
| 2 | ARIA | bitget | +97.78% |
| 3 | SIREN | bitget | +83.99% |
| 4 | CSOPSS2LHKD | bitget | +81.36% |
| 5 | SHEIN | okx | +73.29% |
| 6 | CSOPSKHYNIX2L | okx | +69.01% |
| 7 | XPD | okx | +68.42% |
| 8 | CSOPSK2LHKD | bitget | +58.14% |
| 9 | TRUTH | okx | +57.07% |
| 10 | CXMT | okx | +46.15% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BWET | bitget | -937.65% |
| 2 | H100 | okx | -868.09% |
| 3 | BTW | bitget | -245.83% |
| 4 | CT | okx | -162.06% |
| 5 | CT | bitget | -140.60% |
| 6 | SAND | bitget | -118.81% |
| 7 | AMC | bitget | -96.03% |
| 8 | GPRO | okx | -83.30% |
| 9 | BLUR | okx | -81.53% |
| 10 | USO | okx | -81.06% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BWET | +937.65% | okx | +0.00% | bitget | -937.65% |
| 2 | H100 | +873.56% | bitget | +5.47% | okx | -868.09% |
| 3 | KR200 | +105.12% | okx | +105.12% | bitget | +0.00% |
| 4 | AMC | +84.55% | okx | -11.48% | bitget | -96.03% |
| 5 | GPRO | +78.92% | bitget | -4.38% | okx | -83.30% |
| 6 | SHEIN | +73.29% | okx | +73.29% | bitget | +0.00% |
| 7 | UNITREE | +68.17% | bitget | +0.00% | okx | -68.17% |
| 8 | ZIL | +64.89% | bitget | -7.56% | okx | -72.45% |
| 9 | SAND | +53.26% | okx | -65.55% | bitget | -118.81% |
| 10 | RAY | +51.06% | bitget | -16.86% | okx | -67.92% |
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
