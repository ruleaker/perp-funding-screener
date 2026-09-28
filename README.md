# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-28 05:39 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1282**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CXMT | okx | +319.09% |
| 2 | LUNR | okx | +276.70% |
| 3 | UNITREE | okx | +268.56% |
| 4 | ZHONGJI | okx | +259.16% |
| 5 | CXMT | bitget | +244.29% |
| 6 | SOXS | bitget | +209.15% |
| 7 | KIOXIA | okx | +195.78% |
| 8 | SHEINHKD | bitget | +189.65% |
| 9 | SKDD | bitget | +180.46% |
| 10 | XIAOMI | okx | +153.56% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LGELECTRONICS | bitget | -509.61% |
| 2 | SAMSUNG | okx | -504.65% |
| 3 | LGELECTRONICS | okx | -374.32% |
| 4 | INTW | bitget | -273.20% |
| 5 | SAMSUNG | bitget | -270.79% |
| 6 | ONE | okx | -237.06% |
| 7 | SOXL | bitget | -217.47% |
| 8 | MSTU | bitget | -209.04% |
| 9 | CONL | bitget | -205.09% |
| 10 | RAM | bitget | -202.36% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | INTW | +273.20% | okx | +0.00% | bitget | -273.20% |
| 2 | SAMSUNG | +233.86% | bitget | -270.79% | okx | -504.65% |
| 3 | SOXL | +217.47% | okx | +0.00% | bitget | -217.47% |
| 4 | MSTU | +209.04% | okx | +0.00% | bitget | -209.04% |
| 5 | SOXS | +204.40% | bitget | +209.15% | okx | +4.75% |
| 6 | MVLL | +197.21% | okx | +0.00% | bitget | -197.21% |
| 7 | SKDD | +180.46% | bitget | +180.46% | okx | +0.00% |
| 8 | MUU | +175.09% | okx | +0.00% | bitget | -175.09% |
| 9 | ARM | +158.34% | okx | +0.00% | bitget | -158.34% |
| 10 | LYTE | +156.15% | okx | +0.00% | bitget | -156.15% |
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
