# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-27 20:49 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1373**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +359.80% |
| 2 | KR200 | okx | +248.83% |
| 3 | USDESTOCK | bitget | +216.37% |
| 4 | AGPU | bitget | +216.15% |
| 5 | BWET | bitget | +158.78% |
| 6 | GPRO | bitget | +148.92% |
| 7 | NDX100 | bitget | +147.50% |
| 8 | KSTR | okx | +136.44% |
| 9 | SHEIN | okx | +124.86% |
| 10 | MSTU | bitget | +102.71% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | DOOD | okx | -483.09% |
| 2 | DOOD | bitget | -473.04% |
| 3 | USDBRL | bitget | -355.22% |
| 4 | IRYS | okx | -152.87% |
| 5 | ANIME | bitget | -132.82% |
| 6 | POLYX | bitget | -127.24% |
| 7 | BIRB | bitget | -111.58% |
| 8 | ANIME | okx | -108.24% |
| 9 | RUM | bitget | -95.92% |
| 10 | REZ | bitget | -89.24% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +354.32% | okx | +359.80% | bitget | +5.47% |
| 2 | KR200 | +248.83% | okx | +248.83% | bitget | +0.00% |
| 3 | BWET | +145.06% | bitget | +158.78% | okx | +13.72% |
| 4 | IRYS | +129.54% | bitget | -23.32% | okx | -152.87% |
| 5 | SHEIN | +124.86% | okx | +124.86% | bitget | +0.00% |
| 6 | GPRO | +124.21% | bitget | +148.92% | okx | +24.71% |
| 7 | RUM | +95.92% | okx | +0.00% | bitget | -95.92% |
| 8 | MSTU | +61.52% | bitget | +102.71% | okx | +41.19% |
| 9 | KSTR | +57.60% | okx | +136.44% | bitget | +78.84% |
| 10 | ZHIPU | +56.09% | bitget | +82.12% | okx | +26.03% |
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
