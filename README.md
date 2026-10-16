# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-16 04:46 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1323**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TSLL | bitget | +343.06% |
| 2 | SPCH | bitget | +338.46% |
| 3 | CSOPSKHYNIX2L | okx | +280.44% |
| 4 | KR200 | okx | +244.82% |
| 5 | SKHYNIX | okx | +231.13% |
| 6 | H100 | okx | +228.16% |
| 7 | NAVER | bitget | +221.52% |
| 8 | AGPU | bitget | +192.06% |
| 9 | NAVER | okx | +177.57% |
| 10 | TSLA | bitget | +159.10% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SSPC | bitget | -381.28% |
| 2 | BLUR | bitget | -313.39% |
| 3 | BLUR | okx | -307.62% |
| 4 | UNITREE | okx | -269.85% |
| 5 | BOT | okx | -227.86% |
| 6 | HANMI | okx | -175.74% |
| 7 | SIREN | bitget | -166.33% |
| 8 | UNITREE | bitget | -165.02% |
| 9 | SKDD | okx | -156.63% |
| 10 | SDGR | bitget | -150.34% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | TSLL | +343.06% | bitget | +343.06% | okx | +0.00% |
| 2 | SPCH | +338.46% | bitget | +338.46% | okx | +0.00% |
| 3 | H100 | +228.16% | okx | +228.16% | bitget | +0.00% |
| 4 | BOT | +227.86% | bitget | +0.00% | okx | -227.86% |
| 5 | HANMI | +175.74% | bitget | +0.00% | okx | -175.74% |
| 6 | ANTHROPIC | +155.16% | bitget | +155.16% | okx | +0.00% |
| 7 | SKDD | +149.40% | bitget | -7.23% | okx | -156.63% |
| 8 | MVLL | +147.72% | bitget | +147.72% | okx | +0.00% |
| 9 | RAM | +135.78% | bitget | +135.78% | okx | +0.00% |
| 10 | TSLA | +127.58% | bitget | +159.10% | okx | +31.52% |
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
