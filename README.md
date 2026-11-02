# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-02 18:38 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1392**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | USDESTOCK | bitget | +286.01% |
| 2 | KSTR | okx | +156.84% |
| 3 | INTW | okx | +143.66% |
| 4 | LITE | bitget | +92.75% |
| 5 | VLO | bitget | +89.24% |
| 6 | PBR | bitget | +88.48% |
| 7 | CYPH | okx | +81.16% |
| 8 | CYPH | bitget | +79.61% |
| 9 | INX | bitget | +79.50% |
| 10 | TQQQ | bitget | +77.42% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOT | bitget | -2190.00% |
| 2 | H100 | okx | -1095.00% |
| 3 | 1000CAT | bitget | -589.88% |
| 4 | SDGR | bitget | -364.42% |
| 5 | CSOPSK2LHKD | bitget | -313.94% |
| 6 | KOPN | bitget | -294.01% |
| 7 | SATL | bitget | -256.01% |
| 8 | MOODENG | bitget | -243.31% |
| 9 | LSK | bitget | -220.75% |
| 10 | BLSH | bitget | -200.71% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1100.47% | bitget | +5.47% | okx | -1095.00% |
| 2 | MOODENG | +248.78% | okx | +5.47% | bitget | -243.31% |
| 3 | AKE | +160.22% | bitget | -37.78% | okx | -197.99% |
| 4 | SKHYNIX | +91.59% | bitget | -69.31% | okx | -160.91% |
| 5 | KSTR | +88.40% | okx | +156.84% | bitget | +68.44% |
| 6 | SAMSUNG | +74.77% | bitget | -28.14% | okx | -102.92% |
| 7 | AMC | +70.63% | okx | +0.00% | bitget | -70.63% |
| 8 | INTW | +66.57% | okx | +143.66% | bitget | +77.09% |
| 9 | DGAI | +62.55% | bitget | -7.01% | okx | -69.56% |
| 10 | ZHONGJI | +62.24% | okx | -63.13% | bitget | -125.38% |
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
