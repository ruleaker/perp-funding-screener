# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-08 17:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1098**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +296.26% |
| 2 | SAMSUNG | okx | +171.34% |
| 3 | KIOXIA | okx | +157.87% |
| 4 | EVAA | bitget | +102.38% |
| 5 | ESPORTS | bitget | +94.50% |
| 6 | GOOGL | bitget | +88.59% |
| 7 | GLW | okx | +68.79% |
| 8 | XVG | bitget | +58.14% |
| 9 | 龙虾 | bitget | +58.14% |
| 10 | MRVL | bitget | +54.86% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GWEI | bitget | -512.90% |
| 2 | SPELL | bitget | -368.14% |
| 3 | SLX | okx | -252.97% |
| 4 | NG | okx | -214.20% |
| 5 | EPIC | bitget | -128.33% |
| 6 | ROK | okx | -128.09% |
| 7 | NATGAS | bitget | -121.44% |
| 8 | OPG | okx | -106.70% |
| 9 | ARPA | bitget | -104.68% |
| 10 | RE | okx | -91.67% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +296.26% | okx | +296.26% | bitget | +0.00% |
| 2 | SLX | +171.83% | bitget | -81.14% | okx | -252.97% |
| 3 | SAMSUNG | +171.34% | okx | +171.34% | bitget | +0.00% |
| 4 | KIOXIA | +157.87% | okx | +157.87% | bitget | +0.00% |
| 5 | ROK | +128.09% | bitget | +0.00% | okx | -128.09% |
| 6 | CGNX | +90.05% | bitget | +0.00% | okx | -90.05% |
| 7 | GOOGL | +88.59% | bitget | +88.59% | okx | +0.00% |
| 8 | GLW | +68.79% | okx | +68.79% | bitget | +0.00% |
| 9 | STX | +48.97% | okx | +5.83% | bitget | -43.14% |
| 10 | BB | +46.32% | okx | +0.00% | bitget | -46.32% |
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
