# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-23 10:38 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ARQQ | bitget | +547.50% |
| 2 | ALAB | bitget | +94.94% |
| 3 | FWDI | bitget | +90.12% |
| 4 | MINIMAX | bitget | +72.49% |
| 5 | TSLA | okx | +54.00% |
| 6 | UP | okx | +50.06% |
| 7 | EPIC | bitget | +46.43% |
| 8 | MINIMAX | okx | +41.73% |
| 9 | TSM | okx | +37.74% |
| 10 | NDX100 | bitget | +36.68% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BARD | bitget | -1299.22% |
| 2 | DEXE | bitget | -1217.31% |
| 3 | BARD | okx | -1095.00% |
| 4 | TLM | bitget | -972.25% |
| 5 | O | bitget | -795.19% |
| 6 | O | okx | -604.70% |
| 7 | MIRA | bitget | -408.87% |
| 8 | EWH | bitget | -229.73% |
| 9 | ZKC | bitget | -196.11% |
| 10 | SPELL | bitget | -169.18% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BARD | +204.22% | okx | -1095.00% | bitget | -1299.22% |
| 2 | O | +190.49% | okx | -604.70% | bitget | -795.19% |
| 3 | ALAB | +157.42% | bitget | +94.94% | okx | -62.48% |
| 4 | ZIL | +74.08% | okx | -68.49% | bitget | -142.57% |
| 5 | RAY | +61.29% | bitget | +5.47% | okx | -55.82% |
| 6 | BSP | +48.25% | bitget | +0.00% | okx | -48.25% |
| 7 | ZAMA | +38.83% | bitget | -52.34% | okx | -91.18% |
| 8 | BEAT | +32.20% | bitget | +5.47% | okx | -26.72% |
| 9 | AAOI | +31.84% | okx | +31.84% | bitget | +0.00% |
| 10 | MUBARAK | +31.43% | okx | +5.47% | bitget | -25.95% |
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
