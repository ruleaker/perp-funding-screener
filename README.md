# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-06 12:22 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1085**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ASX | bitget | +258.42% |
| 2 | SKHYNIX | okx | +221.89% |
| 3 | EWJ | bitget | +180.57% |
| 4 | FLEX | bitget | +171.91% |
| 5 | ESPORTS | bitget | +153.85% |
| 6 | SNDK | bitget | +127.68% |
| 7 | EWH | bitget | +119.68% |
| 8 | MRVL | bitget | +116.07% |
| 9 | ORCL | bitget | +113.11% |
| 10 | ASML | bitget | +110.27% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | okx | -1062.64% |
| 2 | SOXS | bitget | -547.50% |
| 3 | BUD | bitget | -547.50% |
| 4 | SLX | okx | -546.46% |
| 5 | LAB | bitget | -484.65% |
| 6 | MINIMAX | okx | -415.42% |
| 7 | MP | bitget | -360.80% |
| 8 | FLNC | bitget | -289.96% |
| 9 | GWEI | bitget | -264.99% |
| 10 | RE | okx | -190.86% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LAB | +577.99% | bitget | -484.65% | okx | -1062.64% |
| 2 | SLX | +410.24% | bitget | -136.22% | okx | -546.46% |
| 3 | MINIMAX | +410.16% | bitget | -5.26% | okx | -415.42% |
| 4 | FLNC | +289.96% | okx | +0.00% | bitget | -289.96% |
| 5 | SKHYNIX | +221.89% | okx | +221.89% | bitget | +0.00% |
| 6 | TWLO | +144.32% | okx | +0.00% | bitget | -144.32% |
| 7 | EWJ | +94.99% | bitget | +180.57% | okx | +85.57% |
| 8 | CRCL | +85.70% | bitget | +101.84% | okx | +16.14% |
| 9 | MRVL | +81.68% | bitget | +116.07% | okx | +34.39% |
| 10 | SNDK | +75.10% | bitget | +127.68% | okx | +52.58% |
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
