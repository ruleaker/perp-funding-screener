# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-20 18:56 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1264**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FIGHT | bitget | +303.31% |
| 2 | AIN | bitget | +208.71% |
| 3 | MSTU | bitget | +159.76% |
| 4 | MSTR | okx | +126.61% |
| 5 | KORU | okx | +105.28% |
| 6 | MSTR | bitget | +98.77% |
| 7 | ON | okx | +86.33% |
| 8 | CRCL | okx | +71.48% |
| 9 | GPRO | okx | +70.27% |
| 10 | US500 | okx | +67.22% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CELR | bitget | -928.67% |
| 2 | ONE | okx | -393.00% |
| 3 | ONG | bitget | -345.36% |
| 4 | SKL | bitget | -279.01% |
| 5 | EGLD | bitget | -264.66% |
| 6 | AKE | bitget | -216.04% |
| 7 | AKE | okx | -215.60% |
| 8 | G | bitget | -172.79% |
| 9 | AVA | bitget | -170.60% |
| 10 | IOST | okx | -164.12% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +286.79% | bitget | -106.22% | okx | -393.00% |
| 2 | EGLD | +123.14% | okx | -141.52% | bitget | -264.66% |
| 3 | KORU | +105.28% | okx | +105.28% | bitget | +0.00% |
| 4 | GPRO | +70.27% | okx | +70.27% | bitget | +0.00% |
| 5 | CXMT | +64.55% | okx | +64.55% | bitget | +0.00% |
| 6 | ZHONGJI | +56.27% | okx | +56.27% | bitget | +0.00% |
| 7 | O | +41.19% | okx | +48.97% | bitget | +7.77% |
| 8 | RIVER | +40.56% | bitget | +46.43% | okx | +5.87% |
| 9 | MVLL | +38.05% | okx | +53.71% | bitget | +15.66% |
| 10 | UB | +34.06% | bitget | +5.47% | okx | -28.58% |
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
