# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-08 15:27 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1412**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 哈基米 | bitget | +255.68% |
| 2 | ARIA | bitget | +105.01% |
| 3 | TRUTH | okx | +103.91% |
| 4 | SIREN | bitget | +91.43% |
| 5 | APR | okx | +88.28% |
| 6 | 牛来 | bitget | +42.60% |
| 7 | FIGHT | bitget | +41.72% |
| 8 | USELESS | okx | +40.88% |
| 9 | TLT | okx | +40.58% |
| 10 | MYX | bitget | +34.16% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CYBER | bitget | -732.01% |
| 2 | HOT | bitget | -684.27% |
| 3 | POWER | bitget | -652.07% |
| 4 | BRETT | bitget | -541.15% |
| 5 | LSK | bitget | -348.43% |
| 6 | H100 | okx | -331.66% |
| 7 | CHILLGUY | bitget | -324.12% |
| 8 | HUMA | okx | -264.11% |
| 9 | RSR | bitget | -250.65% |
| 10 | ONE | okx | -248.33% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BRETT | +546.62% | okx | +5.47% | bitget | -541.15% |
| 2 | H100 | +337.13% | bitget | +5.47% | okx | -331.66% |
| 3 | HUMA | +197.21% | bitget | -66.90% | okx | -264.11% |
| 4 | ONE | +183.07% | bitget | -65.26% | okx | -248.33% |
| 5 | RSR | +110.39% | okx | -140.25% | bitget | -250.65% |
| 6 | APR | +82.81% | okx | +88.28% | bitget | +5.47% |
| 7 | AERO | +72.34% | okx | -48.33% | bitget | -120.67% |
| 8 | BTW | +59.44% | bitget | +5.47% | okx | -53.97% |
| 9 | BLUR | +54.53% | bitget | -18.83% | okx | -73.36% |
| 10 | EGLD | +53.83% | bitget | +10.95% | okx | -42.88% |
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
