# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-06 06:38 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1298**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACN | okx | +213.55% |
| 2 | NAVER | bitget | +209.04% |
| 3 | KIOXIA | bitget | +206.19% |
| 4 | POPMART | bitget | +166.33% |
| 5 | HYUNDAI | okx | +160.74% |
| 6 | SKHYNIX | okx | +144.33% |
| 7 | POET | okx | +142.83% |
| 8 | ZHONGJI | okx | +135.24% |
| 9 | NG | okx | +122.09% |
| 10 | CSOPSKHYNIX2L | okx | +108.42% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -1095.00% |
| 2 | HANMI | okx | -820.33% |
| 3 | LGELECTRONICS | okx | -611.83% |
| 4 | HANMI | bitget | -569.84% |
| 5 | API3 | okx | -507.44% |
| 6 | LGELECTRONICS | bitget | -440.08% |
| 7 | API3 | bitget | -418.95% |
| 8 | UMA | okx | -413.47% |
| 9 | UMA | bitget | -347.12% |
| 10 | BWET | okx | -280.70% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1095.00% | bitget | +0.00% | okx | -1095.00% |
| 2 | BWET | +283.11% | bitget | +2.41% | okx | -280.70% |
| 3 | HANMI | +250.49% | bitget | -569.84% | okx | -820.33% |
| 4 | ONE | +215.98% | okx | +27.53% | bitget | -188.45% |
| 5 | LGELECTRONICS | +171.75% | bitget | -440.08% | okx | -611.83% |
| 6 | NAVER | +164.86% | bitget | +209.04% | okx | +44.18% |
| 7 | OKTA | +144.29% | bitget | +0.00% | okx | -144.29% |
| 8 | POET | +142.83% | okx | +142.83% | bitget | +0.00% |
| 9 | KIOXIA | +138.78% | bitget | +206.19% | okx | +67.40% |
| 10 | SKUU | +131.85% | okx | +46.66% | bitget | -85.19% |
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
