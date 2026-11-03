# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-03 21:52 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1393**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AGPU | bitget | +449.72% |
| 2 | USDESTOCK | bitget | +290.50% |
| 3 | KR200 | okx | +203.15% |
| 4 | CSOPSK2LHKD | bitget | +151.33% |
| 5 | KSTR | okx | +145.09% |
| 6 | CXMT | okx | +125.69% |
| 7 | KSTR | bitget | +123.08% |
| 8 | XVG | bitget | +114.32% |
| 9 | CSOPSS2LHKD | bitget | +101.73% |
| 10 | ISRG | bitget | +99.64% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -689.48% |
| 2 | ERA | bitget | -195.68% |
| 3 | POWER | bitget | -173.56% |
| 4 | LSK | bitget | -122.42% |
| 5 | BLUR | okx | -109.85% |
| 6 | 1000CAT | bitget | -106.54% |
| 7 | AKE | bitget | -97.67% |
| 8 | XNDU | bitget | -96.91% |
| 9 | BHP | bitget | -95.59% |
| 10 | BLUR | bitget | -79.94% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +694.96% | bitget | +5.47% | okx | -689.48% |
| 2 | KR200 | +169.97% | okx | +203.15% | bitget | +33.18% |
| 3 | ISRG | +99.64% | bitget | +99.64% | okx | +0.00% |
| 4 | BWET | +98.77% | bitget | +98.77% | okx | +0.00% |
| 5 | CXMT | +86.49% | okx | +125.69% | bitget | +39.20% |
| 6 | SHAZ | +77.63% | okx | +77.63% | bitget | +0.00% |
| 7 | CGNX | +77.53% | okx | +0.00% | bitget | -77.53% |
| 8 | AERO | +71.63% | okx | +4.28% | bitget | -67.34% |
| 9 | AKE | +66.62% | okx | -31.06% | bitget | -97.67% |
| 10 | ROK | +59.65% | okx | +59.65% | bitget | +0.00% |
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
