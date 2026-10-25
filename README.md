# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-25 13:16 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1364**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | PIPPIN | bitget | +183.19% |
| 2 | ZEST | bitget | +49.82% |
| 3 | TRUTH | okx | +41.55% |
| 4 | MINIMAX | okx | +36.68% |
| 5 | DELL | okx | +34.28% |
| 6 | UP | okx | +31.76% |
| 7 | WDC | okx | +27.60% |
| 8 | KORU | okx | +25.86% |
| 9 | XMR | bitget | +24.53% |
| 10 | US100 | okx | +23.57% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BTW | bitget | -1263.85% |
| 2 | H100 | okx | -1095.00% |
| 3 | POLYX | bitget | -740.66% |
| 4 | STEEM | bitget | -718.98% |
| 5 | BIRB | bitget | -613.09% |
| 6 | 1000XEC | bitget | -531.08% |
| 7 | CVC | bitget | -419.28% |
| 8 | MTL | bitget | -416.54% |
| 9 | T | bitget | -415.44% |
| 10 | IOST | okx | -394.03% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1100.47% | bitget | +5.47% | okx | -1095.00% |
| 2 | BTW | +1042.27% | okx | -221.58% | bitget | -1263.85% |
| 3 | IOST | +312.01% | bitget | -82.02% | okx | -394.03% |
| 4 | PIPPIN | +177.72% | bitget | +183.19% | okx | +5.47% |
| 5 | BABY | +88.87% | bitget | -135.56% | okx | -224.43% |
| 6 | AXIS | +77.39% | okx | -34.96% | bitget | -112.35% |
| 7 | MEGA | +49.01% | bitget | +5.47% | okx | -43.54% |
| 8 | CHZ | +46.97% | bitget | +4.93% | okx | -42.05% |
| 9 | LA | +42.97% | bitget | -22.12% | okx | -65.08% |
| 10 | BIO | +40.30% | bitget | +5.47% | okx | -34.82% |
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
