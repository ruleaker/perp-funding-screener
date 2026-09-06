# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-06 12:13 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1235**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GPRO | okx | +329.13% |
| 2 | ONE | bitget | +217.03% |
| 3 | SOFTBANK | okx | +176.57% |
| 4 | XMR | bitget | +160.97% |
| 5 | ESPORTS | bitget | +145.63% |
| 6 | FIGHT | bitget | +134.47% |
| 7 | ONE | okx | +104.39% |
| 8 | CRCL | okx | +97.35% |
| 9 | SOXL | okx | +89.20% |
| 10 | CP | okx | +83.58% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -376.90% |
| 2 | ICX | okx | -297.58% |
| 3 | T | bitget | -238.93% |
| 4 | LA | okx | -169.49% |
| 5 | LA | bitget | -166.22% |
| 6 | COTI | bitget | -112.13% |
| 7 | RAY | okx | -60.76% |
| 8 | BICO | bitget | -48.62% |
| 9 | ZORA | bitget | -48.62% |
| 10 | ZORA | okx | -44.89% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | GPRO | +329.13% | okx | +329.13% | bitget | +0.00% |
| 2 | ONE | +112.64% | bitget | +217.03% | okx | +104.39% |
| 3 | CRCL | +91.65% | okx | +97.35% | bitget | +5.69% |
| 4 | SOXL | +89.20% | okx | +89.20% | bitget | +0.00% |
| 5 | AAOI | +73.05% | okx | +73.05% | bitget | +0.00% |
| 6 | CP | +69.12% | okx | +83.58% | bitget | +14.45% |
| 7 | BSB | +52.24% | okx | +57.72% | bitget | +5.47% |
| 8 | EDGE | +50.73% | okx | +57.08% | bitget | +6.35% |
| 9 | SHELL | +40.74% | okx | +46.22% | bitget | +5.47% |
| 10 | RAY | +39.08% | bitget | -21.68% | okx | -60.76% |
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
