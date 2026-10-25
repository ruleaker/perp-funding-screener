# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-25 05:01 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1364**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SHEIN | okx | +149.89% |
| 2 | UP | okx | +79.19% |
| 3 | KORU | okx | +75.23% |
| 4 | SNXX | bitget | +72.05% |
| 5 | SNXX | okx | +71.68% |
| 6 | SOON | okx | +62.98% |
| 7 | KR200 | okx | +61.45% |
| 8 | CSOPSK2LHKD | bitget | +59.24% |
| 9 | MINIMAX | okx | +57.74% |
| 10 | PURR | okx | +55.49% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BIRB | bitget | -1106.83% |
| 2 | T | bitget | -923.74% |
| 3 | IRYS | okx | -516.69% |
| 4 | STEEM | bitget | -446.87% |
| 5 | BTW | bitget | -442.05% |
| 6 | IN | bitget | -387.96% |
| 7 | ANIME | bitget | -349.20% |
| 8 | AXIS | bitget | -342.08% |
| 9 | ANIME | okx | -277.32% |
| 10 | IOST | okx | -261.89% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | IRYS | +405.66% | bitget | -111.03% | okx | -516.69% |
| 2 | BTW | +334.46% | okx | -107.59% | bitget | -442.05% |
| 3 | AXIS | +287.71% | okx | -54.36% | bitget | -342.08% |
| 4 | IOST | +158.19% | bitget | -103.70% | okx | -261.89% |
| 5 | PIPPIN | +152.87% | okx | +12.71% | bitget | -140.16% |
| 6 | SHEIN | +149.89% | okx | +149.89% | bitget | +0.00% |
| 7 | ANIME | +71.87% | okx | -277.32% | bitget | -349.20% |
| 8 | LA | +66.81% | bitget | -63.95% | okx | -130.76% |
| 9 | KR200 | +61.45% | okx | +61.45% | bitget | +0.00% |
| 10 | MINIMAX | +57.74% | okx | +57.74% | bitget | +0.00% |
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
