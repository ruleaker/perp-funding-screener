# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-05-27 04:54 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **903**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +1256.73% |
| 2 | AAOI | okx | +311.89% |
| 3 | NBIS | okx | +269.99% |
| 4 | INFQ | okx | +213.04% |
| 5 | WDC | okx | +205.94% |
| 6 | LITE | okx | +164.44% |
| 7 | BEAT | bitget | +147.83% |
| 8 | LIGHT | bitget | +134.36% |
| 9 | MRVL | okx | +118.80% |
| 10 | ASTS | bitget | +109.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | DRIFT | bitget | -1028.64% |
| 2 | PRL | bitget | -433.29% |
| 3 | GUN | bitget | -387.41% |
| 4 | INX | bitget | -242.87% |
| 5 | ALT | bitget | -161.51% |
| 6 | CHIP | okx | -150.28% |
| 7 | STORJ | bitget | -126.47% |
| 8 | BARD | bitget | -114.97% |
| 9 | RVN | okx | -110.99% |
| 10 | SOXS | bitget | -109.50% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | NBIS | +258.71% | okx | +269.99% | bitget | +11.28% |
| 2 | AAOI | +202.39% | okx | +311.89% | bitget | +109.50% |
| 3 | LITE | +164.44% | okx | +164.44% | bitget | +0.00% |
| 4 | BEAT | +135.15% | bitget | +147.83% | okx | +12.67% |
| 5 | LIGHT | +128.88% | bitget | +134.36% | okx | +5.47% |
| 6 | RVN | +116.46% | bitget | +5.47% | okx | -110.99% |
| 7 | INFQ | +103.54% | okx | +213.04% | bitget | +109.50% |
| 8 | WDC | +96.44% | okx | +205.94% | bitget | +109.50% |
| 9 | MRVL | +94.06% | okx | +118.80% | bitget | +24.75% |
| 10 | BARD | +70.26% | okx | -44.71% | bitget | -114.97% |
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
