# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-11 17:25 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1172**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +197.59% |
| 2 | 龙虾 | bitget | +155.71% |
| 3 | POWER | bitget | +121.22% |
| 4 | NATGAS | bitget | +121.22% |
| 5 | XMR | bitget | +88.59% |
| 6 | XCU | okx | +84.04% |
| 7 | TRUTH | okx | +76.08% |
| 8 | KIOXIA | okx | +72.57% |
| 9 | GOOGL | bitget | +72.27% |
| 10 | COPPER | bitget | +62.41% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KAITO | bitget | -633.68% |
| 2 | RVN | okx | -496.19% |
| 3 | DOS | bitget | -262.69% |
| 4 | RVN | bitget | -250.65% |
| 5 | DEXE | bitget | -212.98% |
| 6 | BZ | bitget | -163.70% |
| 7 | BZ | okx | -159.26% |
| 8 | KAITO | okx | -129.17% |
| 9 | HOME | bitget | -122.31% |
| 10 | HOME | okx | -121.77% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KAITO | +504.51% | okx | -129.17% | bitget | -633.68% |
| 2 | RVN | +245.54% | bitget | -250.65% | okx | -496.19% |
| 3 | DOS | +224.34% | okx | -38.35% | bitget | -262.69% |
| 4 | BSP | +100.52% | bitget | +0.00% | okx | -100.52% |
| 5 | LUNA | +68.06% | bitget | +5.47% | okx | -62.59% |
| 6 | KIOXIA | +55.59% | okx | +72.57% | bitget | +16.97% |
| 7 | GOOGL | +49.18% | bitget | +72.27% | okx | +23.09% |
| 8 | GMX | +48.51% | okx | +10.95% | bitget | -37.56% |
| 9 | APE | +42.06% | bitget | +10.95% | okx | -31.11% |
| 10 | TWLO | +40.34% | bitget | +0.00% | okx | -40.34% |
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
