# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-12 12:15 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1251**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | US500 | okx | +79.36% |
| 2 | ORCL | okx | +77.84% |
| 3 | ONE | okx | +76.75% |
| 4 | BNC | bitget | +45.66% |
| 5 | LUMIA | bitget | +40.19% |
| 6 | POWR | bitget | +37.89% |
| 7 | BYD | bitget | +33.95% |
| 8 | O | okx | +31.46% |
| 9 | SIREN | bitget | +31.43% |
| 10 | SONIC | bitget | +31.32% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LSK | bitget | -711.42% |
| 2 | IOST | okx | -523.48% |
| 3 | VTHO | bitget | -380.84% |
| 4 | TREE | bitget | -186.26% |
| 5 | IOST | bitget | -176.30% |
| 6 | RVN | okx | -170.05% |
| 7 | RVN | bitget | -167.97% |
| 8 | UNITAS | bitget | -160.75% |
| 9 | UP | okx | -128.80% |
| 10 | ZIL | bitget | -95.59% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | IOST | +347.19% | bitget | -176.30% | okx | -523.48% |
| 2 | ORCL | +77.84% | okx | +77.84% | bitget | +0.00% |
| 3 | ONE | +65.80% | okx | +76.75% | bitget | +10.95% |
| 4 | ZIL | +48.06% | okx | -47.53% | bitget | -95.59% |
| 5 | SOPH | +46.56% | bitget | -34.60% | okx | -81.17% |
| 6 | RAY | +43.22% | bitget | +5.47% | okx | -37.74% |
| 7 | SHAZ | +41.57% | bitget | +0.00% | okx | -41.57% |
| 8 | BLUR | +32.57% | bitget | -6.68% | okx | -39.25% |
| 9 | MINA | +32.11% | okx | -54.83% | bitget | -86.94% |
| 10 | ZETA | +31.97% | okx | +5.47% | bitget | -26.50% |
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
