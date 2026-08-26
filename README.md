# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-26 09:08 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1197**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | URNM | okx | +153.35% |
| 2 | MINIMAX | okx | +126.62% |
| 3 | SOFTBANK | okx | +120.97% |
| 4 | POPMART | okx | +118.78% |
| 5 | FIGHT | bitget | +104.68% |
| 6 | ZHIPU | okx | +101.65% |
| 7 | MINIMAX | bitget | +99.21% |
| 8 | VRT | okx | +98.37% |
| 9 | QNT | okx | +98.11% |
| 10 | ZHIPU | bitget | +83.00% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | EDEN | okx | -349.19% |
| 2 | ONT | okx | -246.53% |
| 3 | CXMT | okx | -238.89% |
| 4 | CXMT | bitget | -219.11% |
| 5 | ONT | bitget | -209.69% |
| 6 | ACE | bitget | -198.41% |
| 7 | HOME | bitget | -175.75% |
| 8 | HOME | okx | -175.56% |
| 9 | BICO | bitget | -118.26% |
| 10 | SAND | bitget | -116.07% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | VRT | +98.37% | okx | +98.37% | bitget | +0.00% |
| 2 | RVN | +97.99% | bitget | -4.71% | okx | -102.70% |
| 3 | QNT | +87.16% | okx | +98.11% | bitget | +10.95% |
| 4 | POPMART | +80.67% | okx | +118.78% | bitget | +38.11% |
| 5 | SHAZ | +74.43% | bitget | +0.00% | okx | -74.43% |
| 6 | RAM | +72.01% | okx | +72.01% | bitget | +0.00% |
| 7 | CGNX | +62.88% | bitget | +0.00% | okx | -62.88% |
| 8 | HYUNDAI | +62.55% | bitget | +0.00% | okx | -62.55% |
| 9 | UNITREE | +60.58% | bitget | -26.28% | okx | -86.86% |
| 10 | SAND | +55.70% | okx | -60.37% | bitget | -116.07% |
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
