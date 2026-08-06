# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-06 03:47 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1164**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 1MCHEEMS | bitget | +377.99% |
| 2 | SNXX | okx | +239.45% |
| 3 | KIOXIA | bitget | +208.71% |
| 4 | SUMIELEC | bitget | +150.78% |
| 5 | KIOXIA | okx | +132.80% |
| 6 | SNDK | okx | +118.31% |
| 7 | HFT | bitget | +115.19% |
| 8 | 龙虾 | bitget | +107.20% |
| 9 | KR200 | okx | +97.28% |
| 10 | ESPORTS | bitget | +94.72% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -740.88% |
| 2 | HOME | okx | -687.77% |
| 3 | CAP | bitget | -276.16% |
| 4 | CAP | okx | -259.25% |
| 5 | MIRA | bitget | -218.01% |
| 6 | SKR | bitget | -186.81% |
| 7 | KORU | bitget | -161.29% |
| 8 | ON | okx | -132.23% |
| 9 | FWDI | okx | -119.66% |
| 10 | LA | okx | -115.70% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SNXX | +239.45% | okx | +239.45% | bitget | +0.00% |
| 2 | BICO | +162.93% | bitget | +82.34% | okx | -80.58% |
| 3 | KORU | +161.29% | okx | +0.00% | bitget | -161.29% |
| 4 | FWDI | +119.66% | bitget | +0.00% | okx | -119.66% |
| 5 | SNDK | +118.31% | okx | +118.31% | bitget | +0.00% |
| 6 | WDC | +86.26% | okx | +86.26% | bitget | +0.00% |
| 7 | KIOXIA | +75.91% | bitget | +208.71% | okx | +132.80% |
| 8 | CGNX | +71.28% | bitget | +71.28% | okx | +0.00% |
| 9 | O | +63.71% | okx | +69.18% | bitget | +5.47% |
| 10 | RAY | +59.42% | bitget | +5.47% | okx | -53.94% |
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
