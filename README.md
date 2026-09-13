# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-13 13:23 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1251**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOXS | bitget | +188.34% |
| 2 | SOXS | okx | +175.42% |
| 3 | CRWD | okx | +143.67% |
| 4 | SKDD | bitget | +90.67% |
| 5 | US500 | okx | +89.94% |
| 6 | ONE | okx | +60.22% |
| 7 | LUMIA | bitget | +51.25% |
| 8 | ARIA | bitget | +46.65% |
| 9 | BAN | bitget | +43.69% |
| 10 | JELLYJELLY | okx | +40.76% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CVC | bitget | -2053.12% |
| 2 | ARK | bitget | -1302.61% |
| 3 | POWR | bitget | -1167.71% |
| 4 | HIVE | bitget | -1099.71% |
| 5 | STEEM | bitget | -977.94% |
| 6 | LSK | bitget | -899.87% |
| 7 | PUNDIX | bitget | -763.87% |
| 8 | POLYX | bitget | -647.80% |
| 9 | MTL | bitget | -614.84% |
| 10 | IOST | okx | -320.77% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | IOST | +226.06% | bitget | -94.72% | okx | -320.77% |
| 2 | CRWD | +143.67% | okx | +143.67% | bitget | +0.00% |
| 3 | UNITREE | +132.92% | bitget | -30.77% | okx | -163.69% |
| 4 | IREN | +111.38% | bitget | -186.92% | okx | -298.29% |
| 5 | ZHONGJI | +109.94% | okx | +0.00% | bitget | -109.94% |
| 6 | SKDD | +89.42% | bitget | +90.67% | okx | +1.25% |
| 7 | MUU | +82.47% | okx | -178.14% | bitget | -260.61% |
| 8 | SKHYNIX | +74.71% | bitget | -22.56% | okx | -97.26% |
| 9 | MINIMAX | +74.02% | okx | +0.00% | bitget | -74.02% |
| 10 | BE | +73.46% | bitget | -66.58% | okx | -140.04% |
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
