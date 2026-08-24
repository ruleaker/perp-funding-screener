# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-24 09:11 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1197**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZHIPU | okx | +248.40% |
| 2 | SSPC | bitget | +226.23% |
| 3 | XIAOMI | okx | +217.07% |
| 4 | ZHIPU | bitget | +183.08% |
| 5 | PURR | okx | +177.06% |
| 6 | ZHONGJI | bitget | +146.07% |
| 7 | MRNA | okx | +136.73% |
| 8 | BOT | bitget | +80.15% |
| 9 | ESPORTS | bitget | +75.66% |
| 10 | RAM | okx | +72.24% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITREE | okx | -299.55% |
| 2 | HOME | okx | -292.25% |
| 3 | CXMT | okx | -288.52% |
| 4 | HOME | bitget | -278.79% |
| 5 | STORJ | bitget | -248.24% |
| 6 | CXMT | bitget | -222.72% |
| 7 | SHAZ | okx | -215.92% |
| 8 | SAND | bitget | -168.19% |
| 9 | BICO | bitget | -165.24% |
| 10 | RVN | okx | -156.68% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | UNITREE | +238.01% | bitget | -61.54% | okx | -299.55% |
| 2 | SHAZ | +215.92% | bitget | +0.00% | okx | -215.92% |
| 3 | XIAOMI | +168.35% | okx | +217.07% | bitget | +48.73% |
| 4 | RVN | +147.59% | bitget | -9.09% | okx | -156.68% |
| 5 | MRNA | +136.73% | okx | +136.73% | bitget | +0.00% |
| 6 | SKHYNIX | +118.26% | bitget | +0.00% | okx | -118.26% |
| 7 | BOT | +80.15% | bitget | +80.15% | okx | +0.00% |
| 8 | SAND | +77.61% | okx | -90.58% | bitget | -168.19% |
| 9 | RAM | +72.24% | okx | +72.24% | bitget | +0.00% |
| 10 | SKDD | +67.14% | bitget | +0.00% | okx | -67.14% |
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
