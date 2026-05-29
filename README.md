# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-05-29 11:44 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **909**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | IBM | okx | +774.50% |
| 2 | NOK | okx | +569.64% |
| 3 | GLW | okx | +401.67% |
| 4 | USAR | okx | +255.24% |
| 5 | GEV | okx | +249.52% |
| 6 | DELL | okx | +148.87% |
| 7 | ESPORTS | bitget | +137.53% |
| 8 | INX | bitget | +119.03% |
| 9 | AAOI | bitget | +109.50% |
| 10 | NBIS | bitget | +109.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ID | bitget | -2190.00% |
| 2 | IO | bitget | -544.87% |
| 3 | 1MCHEEMS | bitget | -279.01% |
| 4 | BSB | okx | -178.48% |
| 5 | TRX | bitget | -94.83% |
| 6 | AIGENSYN | bitget | -83.99% |
| 7 | LAB | okx | -78.84% |
| 8 | WLD | bitget | -76.65% |
| 9 | SPY | bitget | -72.38% |
| 10 | PRL | bitget | -63.84% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | USAR | +216.59% | okx | +255.24% | bitget | +38.65% |
| 2 | BSB | +176.07% | bitget | -2.41% | okx | -178.48% |
| 3 | LITE | +85.48% | okx | +85.48% | bitget | +0.00% |
| 4 | LAB | +84.32% | bitget | +5.47% | okx | -78.84% |
| 5 | INFQ | +80.85% | okx | +96.51% | bitget | +15.66% |
| 6 | SNDK | +76.28% | okx | +76.28% | bitget | +0.00% |
| 7 | SPY | +71.53% | okx | -0.85% | bitget | -72.38% |
| 8 | GOOGL | +62.96% | bitget | +62.96% | okx | +0.00% |
| 9 | WLD | +61.82% | okx | -14.83% | bitget | -76.65% |
| 10 | QCOM | +58.18% | okx | +58.18% | bitget | +0.00% |
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
