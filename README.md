# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-09 06:58 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1412**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +728.61% |
| 2 | NATGAS | bitget | +461.00% |
| 3 | 哈基米 | bitget | +370.99% |
| 4 | NAVER | bitget | +370.66% |
| 5 | LGELECTRONICS | bitget | +337.15% |
| 6 | H100 | okx | +324.32% |
| 7 | KR200 | okx | +305.75% |
| 8 | CSOPSK2LHKD | bitget | +291.16% |
| 9 | CSOPSKHYNIX2L | okx | +228.62% |
| 10 | HANMI | bitget | +214.29% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITREE | okx | -1095.00% |
| 2 | UNITREE | bitget | -679.23% |
| 3 | HOT | bitget | -487.93% |
| 4 | RSR | bitget | -308.57% |
| 5 | HUMA | okx | -304.16% |
| 6 | 1000CAT | bitget | -290.07% |
| 7 | TWASX | bitget | -284.48% |
| 8 | GPRO | okx | -263.20% |
| 9 | ISRG | okx | -260.95% |
| 10 | 1MCHEEMS | bitget | -232.03% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | UNITREE | +415.77% | bitget | -679.23% | okx | -1095.00% |
| 2 | H100 | +318.84% | okx | +324.32% | bitget | +5.47% |
| 3 | SKDD | +279.07% | bitget | +193.60% | okx | -85.48% |
| 4 | NAVER | +273.39% | bitget | +370.66% | okx | +97.27% |
| 5 | GPRO | +263.20% | bitget | +0.00% | okx | -263.20% |
| 6 | ISRG | +260.95% | bitget | +0.00% | okx | -260.95% |
| 7 | HUMA | +240.87% | bitget | -63.29% | okx | -304.16% |
| 8 | LGELECTRONICS | +231.43% | bitget | +337.15% | okx | +105.72% |
| 9 | NVDL | +228.96% | okx | +0.00% | bitget | -228.96% |
| 10 | HANMI | +214.29% | bitget | +214.29% | okx | +0.00% |
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
