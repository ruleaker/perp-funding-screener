# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-15 13:34 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1323**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BLSH | bitget | +883.23% |
| 2 | KOPN | bitget | +533.37% |
| 3 | SDGR | bitget | +324.67% |
| 4 | H100 | okx | +269.71% |
| 5 | FWDI | bitget | +252.84% |
| 6 | ETN | bitget | +250.32% |
| 7 | HPQ | bitget | +241.12% |
| 8 | KR200 | okx | +185.31% |
| 9 | SKHYNIX | okx | +175.44% |
| 10 | INDA | bitget | +168.30% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BLUR | bitget | -1406.64% |
| 2 | AGPU | bitget | -816.65% |
| 3 | TWST | bitget | -766.72% |
| 4 | VICR | okx | -648.05% |
| 5 | BLUR | okx | -588.14% |
| 6 | BWET | bitget | -411.17% |
| 7 | BSP | bitget | -335.18% |
| 8 | BSP | okx | -326.81% |
| 9 | BOT | okx | -323.24% |
| 10 | SPIR | bitget | -295.32% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BLUR | +818.50% | okx | -588.14% | bitget | -1406.64% |
| 2 | H100 | +269.71% | okx | +269.71% | bitget | +0.00% |
| 3 | FLY | +255.79% | okx | +0.00% | bitget | -255.79% |
| 4 | FWDI | +252.84% | bitget | +252.84% | okx | +0.00% |
| 5 | KR200 | +185.31% | okx | +185.31% | bitget | +0.00% |
| 6 | SKHYNIX | +175.44% | okx | +175.44% | bitget | +0.00% |
| 7 | BWET | +164.68% | okx | -246.50% | bitget | -411.17% |
| 8 | ROK | +133.39% | bitget | +0.00% | okx | -133.39% |
| 9 | AMC | +126.36% | okx | +0.00% | bitget | -126.36% |
| 10 | SOFTBANK | +121.87% | bitget | +0.00% | okx | -121.87% |
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
