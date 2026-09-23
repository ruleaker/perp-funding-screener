# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-23 19:44 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1281**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | okx | +138.64% |
| 2 | XPT | okx | +135.57% |
| 3 | CNPY | okx | +100.39% |
| 4 | XPD | okx | +88.85% |
| 5 | TMF | okx | +79.83% |
| 6 | PIPPIN | bitget | +69.64% |
| 7 | 1000SATS | bitget | +61.98% |
| 8 | XPT | bitget | +61.87% |
| 9 | US | bitget | +60.55% |
| 10 | BABA | bitget | +59.02% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | bitget | -1220.49% |
| 2 | CELR | bitget | -249.11% |
| 3 | TWLO | bitget | -174.54% |
| 4 | KERNEL | bitget | -137.75% |
| 5 | COTI | bitget | -103.48% |
| 6 | CSOPSS2LHKD | bitget | -71.28% |
| 7 | TRUMP | okx | -67.89% |
| 8 | KIOXIA | okx | -67.59% |
| 9 | TRUMP | bitget | -63.29% |
| 10 | OKTA | okx | -48.13% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +1359.13% | okx | +138.64% | bitget | -1220.49% |
| 2 | TWLO | +174.54% | okx | +0.00% | bitget | -174.54% |
| 3 | TMF | +79.83% | okx | +79.83% | bitget | +0.00% |
| 4 | XPT | +73.70% | okx | +135.57% | bitget | +61.87% |
| 5 | PIPPIN | +62.07% | bitget | +69.64% | okx | +7.57% |
| 6 | XPD | +58.74% | okx | +88.85% | bitget | +30.11% |
| 7 | KIOXIA | +49.19% | bitget | -18.40% | okx | -67.59% |
| 8 | OKTA | +48.13% | bitget | +0.00% | okx | -48.13% |
| 9 | BB | +44.89% | okx | +50.37% | bitget | +5.47% |
| 10 | EGLD | +43.44% | okx | +54.39% | bitget | +10.95% |
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
