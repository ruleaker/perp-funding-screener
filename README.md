# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-07 09:29 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1163**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KIOXIA | bitget | +231.59% |
| 2 | BSP | okx | +213.77% |
| 3 | SKHYNIX | okx | +168.19% |
| 4 | XCU | okx | +163.78% |
| 5 | NG | okx | +147.49% |
| 6 | KIOXIA | okx | +122.00% |
| 7 | 龙虾 | bitget | +120.56% |
| 8 | KORU | bitget | +89.13% |
| 9 | NATGAS | bitget | +82.23% |
| 10 | SKHYNIX | bitget | +75.45% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | okx | -1095.00% |
| 2 | ERA | bitget | -817.20% |
| 3 | ACE | bitget | -699.16% |
| 4 | KMNO | okx | -461.86% |
| 5 | BICO | okx | -300.43% |
| 6 | HOME | okx | -274.26% |
| 7 | ZHIPU | okx | -255.72% |
| 8 | HOME | bitget | -253.71% |
| 9 | KMNO | bitget | -217.36% |
| 10 | XAI | bitget | -214.07% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | FWDI | +1095.00% | bitget | +0.00% | okx | -1095.00% |
| 2 | BICO | +311.38% | bitget | +10.95% | okx | -300.43% |
| 3 | KMNO | +244.50% | bitget | -217.36% | okx | -461.86% |
| 4 | BSP | +213.77% | okx | +213.77% | bitget | +0.00% |
| 5 | TWLO | +196.72% | bitget | +0.00% | okx | -196.72% |
| 6 | KIOXIA | +109.60% | bitget | +231.59% | okx | +122.00% |
| 7 | SKHYNIX | +92.74% | okx | +168.19% | bitget | +75.45% |
| 8 | KORU | +87.93% | bitget | +89.13% | okx | +1.20% |
| 9 | WEN | +79.31% | bitget | +0.00% | okx | -79.31% |
| 10 | RAM | +60.20% | okx | +60.20% | bitget | +0.00% |
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
