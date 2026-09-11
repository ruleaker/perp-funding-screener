# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-11 04:56 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1250**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HANMI | bitget | +547.50% |
| 2 | NAVER | bitget | +451.47% |
| 3 | MINIMAX | okx | +209.63% |
| 4 | SAMSUNGEM | bitget | +187.46% |
| 5 | ZHIPU | okx | +183.78% |
| 6 | BOT | okx | +154.38% |
| 7 | SKHYNIX | okx | +152.61% |
| 8 | LGELECTRONICS | bitget | +138.63% |
| 9 | ZM | okx | +132.59% |
| 10 | ZHIPU | bitget | +124.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | USO | okx | -456.78% |
| 2 | RAY | okx | -432.93% |
| 3 | NEWT | bitget | -387.85% |
| 4 | RVN | okx | -258.45% |
| 5 | RVN | bitget | -258.20% |
| 6 | VTHO | bitget | -231.92% |
| 7 | ANIME | okx | -230.66% |
| 8 | UNITREE | okx | -220.53% |
| 9 | ONG | bitget | -177.72% |
| 10 | ANIME | bitget | -173.89% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RAY | +290.58% | bitget | -142.35% | okx | -432.93% |
| 2 | BOT | +154.38% | okx | +154.38% | bitget | +0.00% |
| 3 | UNITREE | +138.41% | bitget | -82.12% | okx | -220.53% |
| 4 | ZM | +132.59% | okx | +132.59% | bitget | +0.00% |
| 5 | KORU | +121.22% | bitget | +121.22% | okx | +0.00% |
| 6 | MINIMAX | +110.97% | okx | +209.63% | bitget | +98.66% |
| 7 | RAM | +104.98% | okx | +106.29% | bitget | +1.31% |
| 8 | VRT | +98.20% | okx | +98.20% | bitget | +0.00% |
| 9 | BSP | +86.73% | bitget | +0.00% | okx | -86.73% |
| 10 | IOST | +82.18% | bitget | -75.34% | okx | -157.52% |
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
