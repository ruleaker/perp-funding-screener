# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-09 18:15 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1098**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GOOGL | bitget | +87.27% |
| 2 | SAMSUNG | okx | +83.04% |
| 3 | 龙虾 | bitget | +78.51% |
| 4 | SIREN | bitget | +69.20% |
| 5 | LAB | okx | +62.04% |
| 6 | HYUNDAI | okx | +58.87% |
| 7 | SKHYNIX | okx | +58.70% |
| 8 | EVAA | bitget | +54.97% |
| 9 | US | bitget | +46.43% |
| 10 | RKLB | okx | +43.42% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SENT | bitget | -440.63% |
| 2 | SENT | okx | -344.67% |
| 3 | THE | bitget | -261.05% |
| 4 | SKL | bitget | -241.45% |
| 5 | SLX | okx | -240.01% |
| 6 | OGN | bitget | -234.33% |
| 7 | SPELL | bitget | -234.11% |
| 8 | GWEI | bitget | -214.40% |
| 9 | VANRY | bitget | -128.12% |
| 10 | DATA | okx | -121.04% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SLX | +167.74% | bitget | -72.27% | okx | -240.01% |
| 2 | SENT | +95.96% | okx | -344.67% | bitget | -440.63% |
| 3 | SAMSUNG | +83.04% | okx | +83.04% | bitget | +0.00% |
| 4 | GOOGL | +73.48% | bitget | +87.27% | okx | +13.79% |
| 5 | IBM | +73.04% | okx | +0.00% | bitget | -73.04% |
| 6 | DATA | +64.98% | bitget | -56.06% | okx | -121.04% |
| 7 | LAB | +60.62% | okx | +62.04% | bitget | +1.42% |
| 8 | HYUNDAI | +58.87% | okx | +58.87% | bitget | +0.00% |
| 9 | SKHYNIX | +58.70% | okx | +58.70% | bitget | +0.00% |
| 10 | RAY | +47.30% | okx | +10.95% | bitget | -36.35% |
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
