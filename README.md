# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-25 04:41 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1047**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | bitget | +547.50% |
| 2 | HYUNDAI | bitget | +231.48% |
| 3 | RDW | okx | +224.79% |
| 4 | ZHIPU | bitget | +160.42% |
| 5 | SAMSUNG | bitget | +151.22% |
| 6 | GLW | okx | +116.60% |
| 7 | KIOXIA | bitget | +114.32% |
| 8 | HYUNDAI | okx | +112.51% |
| 9 | VRT | okx | +95.49% |
| 10 | SIREN | bitget | +90.78% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BLEND | okx | -446.82% |
| 2 | LAB | okx | -382.64% |
| 3 | 0G | bitget | -344.71% |
| 4 | ID | bitget | -294.88% |
| 5 | LAB | bitget | -257.11% |
| 6 | 0G | okx | -243.39% |
| 7 | M | bitget | -175.53% |
| 8 | BX | okx | -170.71% |
| 9 | TAIKO | bitget | -157.57% |
| 10 | KORU | okx | -141.89% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +547.50% | bitget | +547.50% | okx | +0.00% |
| 2 | RDW | +224.79% | okx | +224.79% | bitget | +0.00% |
| 3 | BX | +170.71% | bitget | +0.00% | okx | -170.71% |
| 4 | ZHIPU | +160.42% | bitget | +160.42% | okx | +0.00% |
| 5 | KORU | +141.89% | bitget | +0.00% | okx | -141.89% |
| 6 | LAB | +125.54% | bitget | -257.11% | okx | -382.64% |
| 7 | HYUNDAI | +118.98% | bitget | +231.48% | okx | +112.51% |
| 8 | GLW | +116.60% | okx | +116.60% | bitget | +0.00% |
| 9 | UVXY | +114.22% | bitget | +0.00% | okx | -114.22% |
| 10 | SAMSUNG | +104.81% | bitget | +151.22% | okx | +46.41% |
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
