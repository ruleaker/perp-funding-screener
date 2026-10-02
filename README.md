# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-02 20:51 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1298**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +1095.00% |
| 2 | BWET | bitget | +714.05% |
| 3 | SECZ | bitget | +231.48% |
| 4 | JNJ | okx | +147.04% |
| 5 | SECZ | okx | +122.82% |
| 6 | ARX | okx | +103.71% |
| 7 | TWST | bitget | +88.37% |
| 8 | CRML | bitget | +86.72% |
| 9 | COIN | bitget | +84.64% |
| 10 | 哈基米 | bitget | +81.69% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAND | bitget | -488.15% |
| 2 | ENJ | okx | -413.35% |
| 3 | ENJ | bitget | -354.78% |
| 4 | SAND | okx | -274.72% |
| 5 | 2Z | okx | -241.19% |
| 6 | 2Z | bitget | -209.69% |
| 7 | KII | okx | -197.98% |
| 8 | BWET | okx | -193.84% |
| 9 | MANA | okx | -185.62% |
| 10 | USO | okx | -176.63% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1095.00% | okx | +1095.00% | bitget | +0.00% |
| 2 | BWET | +907.89% | bitget | +714.05% | okx | -193.84% |
| 3 | SAND | +213.43% | okx | -274.72% | bitget | -488.15% |
| 4 | SECZ | +108.66% | bitget | +231.48% | okx | +122.82% |
| 5 | ARX | +93.20% | okx | +103.71% | bitget | +10.51% |
| 6 | KORU | +91.39% | okx | -22.82% | bitget | -114.21% |
| 7 | MANA | +89.37% | bitget | -96.25% | okx | -185.62% |
| 8 | ENJ | +58.57% | bitget | -354.78% | okx | -413.35% |
| 9 | SKHY | +57.76% | okx | -51.96% | bitget | -109.72% |
| 10 | FLOCK | +54.29% | bitget | -53.00% | okx | -107.29% |
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
