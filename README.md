# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-20 16:59 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1195**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | POWER | bitget | +94.17% |
| 2 | FIGHT | bitget | +87.71% |
| 3 | COHR | bitget | +68.99% |
| 4 | RLS | okx | +66.67% |
| 5 | BMNR | okx | +64.10% |
| 6 | GWEI | bitget | +55.63% |
| 7 | META | bitget | +53.33% |
| 8 | AVGO | bitget | +51.14% |
| 9 | PIPPIN | okx | +47.68% |
| 10 | WET | bitget | +46.98% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITREE | okx | -286.19% |
| 2 | RVN | okx | -266.79% |
| 3 | ONG | bitget | -235.97% |
| 4 | KR200 | okx | -162.91% |
| 5 | ICX | okx | -128.03% |
| 6 | BICO | bitget | -125.71% |
| 7 | HOME | okx | -124.60% |
| 8 | BOT | bitget | -113.22% |
| 9 | HOME | bitget | -112.78% |
| 10 | ACE | bitget | -111.58% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | UNITREE | +274.26% | bitget | -11.94% | okx | -286.19% |
| 2 | RVN | +253.32% | bitget | -13.47% | okx | -266.79% |
| 3 | KR200 | +162.91% | bitget | +0.00% | okx | -162.91% |
| 4 | ICX | +133.50% | bitget | +5.47% | okx | -128.03% |
| 5 | BOT | +97.00% | okx | -16.23% | bitget | -113.22% |
| 6 | BICO | +83.16% | okx | -42.54% | bitget | -125.71% |
| 7 | BMNR | +64.10% | okx | +64.10% | bitget | +0.00% |
| 8 | POPMART | +53.39% | bitget | +0.00% | okx | -53.39% |
| 9 | PIPPIN | +42.21% | okx | +47.68% | bitget | +5.47% |
| 10 | COHR | +41.67% | bitget | +68.99% | okx | +27.31% |
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
