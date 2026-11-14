# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-14 20:50 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1413**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOXS | bitget | +78.73% |
| 2 | SOXS | okx | +67.61% |
| 3 | KII | okx | +59.57% |
| 4 | DNA | okx | +52.35% |
| 5 | SKDD | bitget | +36.79% |
| 6 | SQQQ | okx | +21.40% |
| 7 | SQQQ | bitget | +16.53% |
| 8 | O | okx | +12.94% |
| 9 | BAND | okx | +10.95% |
| 10 | CRV | okx | +10.95% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -535.80% |
| 2 | BARD | okx | -330.67% |
| 3 | BARD | bitget | -298.28% |
| 4 | SOPH | okx | -262.40% |
| 5 | BERA | bitget | -246.27% |
| 6 | KAVA | bitget | -243.09% |
| 7 | POWER | bitget | -228.64% |
| 8 | INTW | okx | -214.38% |
| 9 | SOPH | bitget | -211.44% |
| 10 | MSTU | bitget | -209.47% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +541.28% | bitget | +5.47% | okx | -535.80% |
| 2 | BERA | +120.00% | okx | -126.27% | bitget | -246.27% |
| 3 | INIT | +119.34% | bitget | -62.41% | okx | -181.75% |
| 4 | HUMA | +92.41% | bitget | -17.19% | okx | -109.60% |
| 5 | SNX | +80.36% | bitget | +10.95% | okx | -69.41% |
| 6 | HOME | +66.59% | bitget | +5.47% | okx | -61.12% |
| 7 | EGLD | +63.46% | bitget | +10.95% | okx | -52.51% |
| 8 | MUU | +59.85% | okx | -40.56% | bitget | -100.41% |
| 9 | PROS | +58.00% | okx | +2.59% | bitget | -55.41% |
| 10 | WOO | +57.81% | bitget | +10.95% | okx | -46.86% |
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
