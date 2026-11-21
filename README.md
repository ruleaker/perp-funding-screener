# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-21 07:30 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1423**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +284.06% |
| 2 | SOXS | okx | +125.74% |
| 3 | SOON | okx | +104.04% |
| 4 | FOLKS | bitget | +91.65% |
| 5 | UVXY | bitget | +87.16% |
| 6 | SOXS | bitget | +78.84% |
| 7 | OPN | okx | +68.64% |
| 8 | SKHYNIX | bitget | +65.59% |
| 9 | WINBOND | bitget | +63.40% |
| 10 | TWDELTA | bitget | +56.94% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ENSO | bitget | -1203.84% |
| 2 | ENSO | okx | -1095.00% |
| 3 | RARE | bitget | -1037.07% |
| 4 | BARD | bitget | -859.36% |
| 5 | CYBER | bitget | -425.95% |
| 6 | IRYS | okx | -255.02% |
| 7 | BARD | okx | -223.58% |
| 8 | KAVA | bitget | -223.16% |
| 9 | KERNEL | bitget | -196.22% |
| 10 | COST | okx | -179.60% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BARD | +635.78% | okx | -223.58% | bitget | -859.36% |
| 2 | H100 | +278.59% | okx | +284.06% | bitget | +5.47% |
| 3 | IRYS | +181.32% | bitget | -73.69% | okx | -255.02% |
| 4 | COST | +179.60% | bitget | +0.00% | okx | -179.60% |
| 5 | MINIMAX | +125.05% | bitget | +5.58% | okx | -119.47% |
| 6 | ENSO | +108.84% | okx | -1095.00% | bitget | -1203.84% |
| 7 | SOON | +98.56% | okx | +104.04% | bitget | +5.47% |
| 8 | UNITREE | +85.68% | bitget | +15.66% | okx | -70.02% |
| 9 | HUMA | +82.19% | bitget | -30.00% | okx | -112.20% |
| 10 | WOO | +71.22% | bitget | +10.95% | okx | -60.27% |
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
