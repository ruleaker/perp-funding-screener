# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-08 20:39 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1412**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 哈基米 | bitget | +445.12% |
| 2 | JCT | bitget | +183.63% |
| 3 | KSTR | okx | +112.47% |
| 4 | POWER | bitget | +83.44% |
| 5 | ARIA | bitget | +75.66% |
| 6 | AERO | okx | +75.02% |
| 7 | TLT | okx | +74.89% |
| 8 | XMR | bitget | +68.77% |
| 9 | INX | bitget | +66.79% |
| 10 | ZEC | bitget | +61.87% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -765.22% |
| 2 | CYBER | bitget | -588.34% |
| 3 | BRETT | bitget | -420.37% |
| 4 | RSR | bitget | -373.29% |
| 5 | HUMA | okx | -289.35% |
| 6 | CHILLGUY | bitget | -267.07% |
| 7 | BLEND | okx | -231.42% |
| 8 | 1MCHEEMS | bitget | -200.38% |
| 9 | RSR | okx | -199.19% |
| 10 | HOT | bitget | -182.65% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +770.70% | bitget | +5.47% | okx | -765.22% |
| 2 | BRETT | +425.85% | okx | +5.47% | bitget | -420.37% |
| 3 | AERO | +208.50% | okx | +75.02% | bitget | -133.48% |
| 4 | HUMA | +206.68% | bitget | -82.67% | okx | -289.35% |
| 5 | RSR | +174.09% | okx | -199.19% | bitget | -373.29% |
| 6 | EGLD | +120.87% | bitget | +10.95% | okx | -109.92% |
| 7 | KSTR | +112.47% | okx | +112.47% | bitget | +0.00% |
| 8 | RECALL | +89.90% | okx | +5.47% | bitget | -84.42% |
| 9 | BLUR | +76.63% | bitget | -30.00% | okx | -106.64% |
| 10 | TLT | +74.89% | okx | +74.89% | bitget | +0.00% |
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
