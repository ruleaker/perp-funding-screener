# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-05 07:07 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1397**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +789.63% |
| 2 | SAMSUNGEM | bitget | +426.83% |
| 3 | TM | bitget | +403.62% |
| 4 | KR200 | okx | +364.34% |
| 5 | SKHYNIX | okx | +316.37% |
| 6 | LGELECTRONICS | bitget | +223.93% |
| 7 | JPSONY | bitget | +202.03% |
| 8 | SKHYNIX | bitget | +182.76% |
| 9 | KR200 | bitget | +170.27% |
| 10 | MSTU | okx | +160.69% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITREE | okx | -1095.00% |
| 2 | UNITREE | bitget | -1078.90% |
| 3 | APP | okx | -558.55% |
| 4 | LSK | bitget | -427.49% |
| 5 | HUMA | bitget | -265.43% |
| 6 | HUMA | okx | -265.23% |
| 7 | BOT | okx | -254.45% |
| 8 | XIAOMI | okx | -209.30% |
| 9 | BLEND | okx | -199.79% |
| 10 | ERA | bitget | -193.05% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +784.15% | okx | +789.63% | bitget | +5.47% |
| 2 | APP | +496.68% | bitget | -61.87% | okx | -558.55% |
| 3 | BOT | +254.45% | bitget | +0.00% | okx | -254.45% |
| 4 | INTW | +228.13% | okx | +67.17% | bitget | -160.97% |
| 5 | KR200 | +194.07% | okx | +364.34% | bitget | +170.27% |
| 6 | XIAOMI | +178.31% | bitget | -30.99% | okx | -209.30% |
| 7 | MSTU | +160.69% | okx | +160.69% | bitget | +0.00% |
| 8 | LGELECTRONICS | +143.99% | bitget | +223.93% | okx | +79.94% |
| 9 | MVLL | +139.35% | okx | +58.43% | bitget | -80.92% |
| 10 | SKHYNIX | +133.61% | okx | +316.37% | bitget | +182.76% |
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
