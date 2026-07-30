# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-30 10:36 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1151**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | bitget | +547.50% |
| 2 | SKHYNIX | okx | +474.74% |
| 3 | SAMSUNG | okx | +265.46% |
| 4 | KR200 | okx | +255.03% |
| 5 | ZHIPU | okx | +200.71% |
| 6 | ZHIPU | bitget | +188.34% |
| 7 | BSP | okx | +179.60% |
| 8 | GLW | bitget | +165.02% |
| 9 | NDX100 | bitget | +147.28% |
| 10 | BMNR | okx | +146.00% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BANK | bitget | -1726.38% |
| 2 | LA | bitget | -1045.94% |
| 3 | ESP | okx | -901.77% |
| 4 | ESP | bitget | -862.09% |
| 5 | LA | okx | -446.02% |
| 6 | EUL | bitget | -419.28% |
| 7 | BOT | bitget | -283.60% |
| 8 | FWDI | okx | -227.99% |
| 9 | DEXE | bitget | -215.06% |
| 10 | ZIL | okx | -182.90% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | FWDI | +775.49% | bitget | +547.50% | okx | -227.99% |
| 2 | LA | +599.92% | okx | -446.02% | bitget | -1045.94% |
| 3 | SKHYNIX | +399.51% | okx | +474.74% | bitget | +75.23% |
| 4 | BOT | +283.60% | okx | +0.00% | bitget | -283.60% |
| 5 | SAMSUNG | +265.46% | okx | +265.46% | bitget | +0.00% |
| 6 | BSP | +179.60% | okx | +179.60% | bitget | +0.00% |
| 7 | BMNR | +146.00% | okx | +146.00% | bitget | +0.00% |
| 8 | GLW | +134.25% | bitget | +165.02% | okx | +30.77% |
| 9 | SHAZ | +130.63% | bitget | +130.63% | okx | +0.00% |
| 10 | SNXX | +105.77% | okx | +105.77% | bitget | +0.00% |
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
