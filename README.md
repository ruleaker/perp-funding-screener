# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-08 02:27 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1164**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KIOXIA | okx | +103.41% |
| 2 | SPIR | bitget | +73.04% |
| 3 | PIEVERSE | bitget | +71.39% |
| 4 | TRIA | okx | +70.79% |
| 5 | PLTR | okx | +64.32% |
| 6 | LIGHT | okx | +62.96% |
| 7 | PRL | bitget | +60.12% |
| 8 | POWER | bitget | +56.83% |
| 9 | FIGHT | bitget | +56.50% |
| 10 | BLEND | okx | +53.09% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MIRA | bitget | -548.70% |
| 2 | LA | bitget | -340.33% |
| 3 | BICO | okx | -295.61% |
| 4 | LA | okx | -257.25% |
| 5 | HOME | bitget | -140.49% |
| 6 | HOME | okx | -139.22% |
| 7 | ERA | bitget | -105.23% |
| 8 | FLY | bitget | -105.01% |
| 9 | SLX | bitget | -95.05% |
| 10 | ZIL | okx | -89.68% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BICO | +306.56% | bitget | +10.95% | okx | -295.61% |
| 2 | FWDI | +113.72% | okx | +33.67% | bitget | -80.04% |
| 3 | FLY | +105.01% | okx | +0.00% | bitget | -105.01% |
| 4 | KIOXIA | +103.41% | okx | +103.41% | bitget | +0.00% |
| 5 | SLX | +100.52% | okx | +5.47% | bitget | -95.05% |
| 6 | LA | +83.08% | okx | -257.25% | bitget | -340.33% |
| 7 | PIEVERSE | +65.92% | bitget | +71.39% | okx | +5.47% |
| 8 | TRIA | +65.32% | okx | +70.79% | bitget | +5.47% |
| 9 | PLTR | +64.32% | okx | +64.32% | bitget | +0.00% |
| 10 | BSP | +61.99% | bitget | +0.00% | okx | -61.99% |
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
