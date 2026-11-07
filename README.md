# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-07 20:21 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1412**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +1006.79% |
| 2 | DNA | okx | +104.99% |
| 3 | APR | okx | +92.52% |
| 4 | SOXL | okx | +90.76% |
| 5 | US500 | okx | +60.18% |
| 6 | SOXL | bitget | +51.90% |
| 7 | SIREN | bitget | +49.93% |
| 8 | SOON | okx | +46.02% |
| 9 | PIPPIN | okx | +43.82% |
| 10 | TRUTH | okx | +43.80% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CHILLGUY | bitget | -563.92% |
| 2 | 1MCHEEMS | bitget | -291.93% |
| 3 | ONE | okx | -252.85% |
| 4 | ERA | bitget | -210.90% |
| 5 | HUMA | okx | -209.93% |
| 6 | LSK | bitget | -158.12% |
| 7 | HOT | bitget | -139.28% |
| 8 | HUMA | bitget | -123.30% |
| 9 | XIAOMI | okx | -106.40% |
| 10 | POWER | bitget | -106.32% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1001.32% | okx | +1006.79% | bitget | +5.47% |
| 2 | ONE | +171.71% | bitget | -81.14% | okx | -252.85% |
| 3 | XIAOMI | +106.40% | bitget | +0.00% | okx | -106.40% |
| 4 | HUMA | +86.63% | bitget | -123.30% | okx | -209.93% |
| 5 | APR | +82.56% | okx | +92.52% | bitget | +9.96% |
| 6 | BRETT | +68.88% | okx | +5.47% | bitget | -63.40% |
| 7 | YB | +46.15% | bitget | +0.66% | okx | -45.49% |
| 8 | RSR | +46.12% | bitget | +10.95% | okx | -35.17% |
| 9 | EGLD | +45.24% | bitget | +10.95% | okx | -34.29% |
| 10 | ATOM | +44.62% | okx | +2.79% | bitget | -41.83% |
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
