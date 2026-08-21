# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-21 02:06 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1195**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CSOPSK2LHKD | bitget | +204.98% |
| 2 | KORU | bitget | +147.83% |
| 3 | SKUU | bitget | +115.19% |
| 4 | SKDD | okx | +101.46% |
| 5 | QNT | okx | +97.87% |
| 6 | DRAM | bitget | +95.05% |
| 7 | SKHY | bitget | +81.36% |
| 8 | MSTU | bitget | +75.66% |
| 9 | SNXX | bitget | +70.30% |
| 10 | 4 | bitget | +67.89% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONG | bitget | -1407.18% |
| 2 | ONT | bitget | -714.82% |
| 3 | ONT | okx | -450.68% |
| 4 | UNITREE | bitget | -409.75% |
| 5 | BICO | bitget | -296.96% |
| 6 | RVN | okx | -284.79% |
| 7 | CXMT | okx | -227.11% |
| 8 | CXMT | bitget | -223.93% |
| 9 | GAS | okx | -219.95% |
| 10 | BICO | okx | -194.57% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RVN | +286.66% | bitget | +1.86% | okx | -284.79% |
| 2 | ONT | +264.14% | okx | -450.68% | bitget | -714.82% |
| 3 | UNITREE | +248.99% | okx | -160.76% | bitget | -409.75% |
| 4 | SKDD | +208.99% | okx | +101.46% | bitget | -107.53% |
| 5 | KORU | +147.83% | bitget | +147.83% | okx | +0.00% |
| 6 | DATA | +137.88% | bitget | +1.53% | okx | -136.35% |
| 7 | SKUU | +115.19% | bitget | +115.19% | okx | +0.00% |
| 8 | GAS | +108.80% | bitget | -111.14% | okx | -219.95% |
| 9 | BICO | +102.39% | okx | -194.57% | bitget | -296.96% |
| 10 | BX | +100.16% | bitget | +0.00% | okx | -100.16% |
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
