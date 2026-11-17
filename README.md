# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-17 08:13 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1415**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LGENERGY | bitget | +863.85% |
| 2 | NAVER | bitget | +461.54% |
| 3 | LGELECTRONICS | bitget | +416.10% |
| 4 | FWDI | okx | +226.91% |
| 5 | H100 | okx | +218.02% |
| 6 | SAMSUNGEM | bitget | +194.47% |
| 7 | MINIMAXHKD | bitget | +182.43% |
| 8 | HANMI | bitget | +171.48% |
| 9 | HYUNDAI | okx | +120.19% |
| 10 | ZHONGJI | bitget | +118.81% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RARE | bitget | -1804.56% |
| 2 | EWZS | okx | -546.10% |
| 3 | HUMA | okx | -470.59% |
| 4 | SOPH | okx | -430.30% |
| 5 | KAVA | bitget | -396.06% |
| 6 | WUXIBIO | okx | -294.74% |
| 7 | UNITREE | okx | -231.60% |
| 8 | SKR | bitget | -202.47% |
| 9 | INIT | okx | -197.20% |
| 10 | TSEM | bitget | -171.15% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | EWZS | +546.10% | bitget | +0.00% | okx | -546.10% |
| 2 | NAVER | +448.94% | bitget | +461.54% | okx | +12.60% |
| 3 | LGELECTRONICS | +397.81% | bitget | +416.10% | okx | +18.29% |
| 4 | HUMA | +360.98% | bitget | -109.61% | okx | -470.59% |
| 5 | SOPH | +329.67% | bitget | -100.63% | okx | -430.30% |
| 6 | FWDI | +226.91% | okx | +226.91% | bitget | +0.00% |
| 7 | H100 | +212.55% | okx | +218.02% | bitget | +5.47% |
| 8 | UNITREE | +181.89% | bitget | -49.71% | okx | -231.60% |
| 9 | HANMI | +171.48% | bitget | +171.48% | okx | +0.00% |
| 10 | CYPH | +155.01% | bitget | +0.00% | okx | -155.01% |
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
