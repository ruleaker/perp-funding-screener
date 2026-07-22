# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-22 03:55 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1126**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GEV | okx | +339.49% |
| 2 | FWDI | bitget | +182.10% |
| 3 | O | bitget | +142.57% |
| 4 | MINIMAX | bitget | +142.02% |
| 5 | SKHYNIX | bitget | +108.41% |
| 6 | BOT | bitget | +87.27% |
| 7 | LUNR | okx | +81.89% |
| 8 | MINIMAX | okx | +79.69% |
| 9 | LYN | bitget | +42.27% |
| 10 | SAMSUNG | bitget | +41.06% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MIRA | bitget | -1602.75% |
| 2 | LA | bitget | -381.39% |
| 3 | DEXE | bitget | -358.17% |
| 4 | VANRY | bitget | -233.45% |
| 5 | ERA | bitget | -160.53% |
| 6 | LA | okx | -149.64% |
| 7 | T | bitget | -124.39% |
| 8 | HOME | okx | -121.48% |
| 9 | QNT | okx | -117.36% |
| 10 | ONE | okx | -101.00% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | GEV | +339.49% | okx | +339.49% | bitget | +0.00% |
| 2 | LA | +231.74% | okx | -149.64% | bitget | -381.39% |
| 3 | O | +134.81% | bitget | +142.57% | okx | +7.76% |
| 4 | QNT | +128.31% | bitget | +10.95% | okx | -117.36% |
| 5 | SKHYNIX | +108.41% | bitget | +108.41% | okx | +0.00% |
| 6 | SOPH | +99.46% | bitget | +5.47% | okx | -93.98% |
| 7 | BOT | +87.27% | bitget | +87.27% | okx | +0.00% |
| 8 | MINIMAX | +62.33% | bitget | +142.02% | okx | +79.69% |
| 9 | RAY | +50.27% | bitget | +5.47% | okx | -44.80% |
| 10 | HOME | +45.49% | bitget | -75.99% | okx | -121.48% |
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
