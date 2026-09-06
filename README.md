# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-06 18:28 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1236**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GPRO | okx | +336.17% |
| 2 | ONE | bitget | +192.39% |
| 3 | SOXL | okx | +175.36% |
| 4 | PONS | okx | +157.23% |
| 5 | XMR | bitget | +119.36% |
| 6 | CP | okx | +115.72% |
| 7 | ESPORTS | bitget | +69.75% |
| 8 | PONS | bitget | +67.67% |
| 9 | IDOL | bitget | +65.48% |
| 10 | USELESS | bitget | +61.21% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -252.29% |
| 2 | UNITAS | bitget | -197.43% |
| 3 | LA | okx | -170.43% |
| 4 | AKE | bitget | -163.92% |
| 5 | LA | bitget | -155.82% |
| 6 | RAY | okx | -130.63% |
| 7 | UP | okx | -124.29% |
| 8 | T | bitget | -101.18% |
| 9 | ORCA | bitget | -79.39% |
| 10 | ONG | bitget | -76.43% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | GPRO | +336.17% | okx | +336.17% | bitget | +0.00% |
| 2 | ONE | +177.88% | bitget | +192.39% | okx | +14.52% |
| 3 | SOXL | +152.47% | okx | +175.36% | bitget | +22.89% |
| 4 | RAY | +93.84% | bitget | -36.79% | okx | -130.63% |
| 5 | PONS | +89.56% | okx | +157.23% | bitget | +67.67% |
| 6 | CP | +73.35% | okx | +115.72% | bitget | +42.38% |
| 7 | KSM | +65.49% | bitget | +10.95% | okx | -54.54% |
| 8 | CXMT | +46.41% | okx | +46.41% | bitget | +0.00% |
| 9 | BSB | +42.22% | okx | +50.98% | bitget | +8.76% |
| 10 | BICO | +38.65% | okx | -10.85% | bitget | -49.49% |
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
