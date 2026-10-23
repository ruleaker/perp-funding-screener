# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-23 13:40 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1362**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BWET | bitget | +1095.00% |
| 2 | VEEV | bitget | +655.80% |
| 3 | HPQ | bitget | +583.74% |
| 4 | CLSK | bitget | +495.82% |
| 5 | TSTOCK | bitget | +461.21% |
| 6 | BAC | bitget | +459.90% |
| 7 | AXON | bitget | +456.40% |
| 8 | CMCSA | bitget | +429.46% |
| 9 | MUFG | bitget | +417.96% |
| 10 | KTOS | bitget | +417.63% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BIRB | bitget | -2190.00% |
| 2 | H100 | okx | -1060.02% |
| 3 | BTW | bitget | -784.35% |
| 4 | ARK | bitget | -746.57% |
| 5 | AXIS | bitget | -719.96% |
| 6 | VLO | bitget | -630.72% |
| 7 | SIMO | bitget | -600.50% |
| 8 | ALT | bitget | -566.55% |
| 9 | JMKE | bitget | -564.80% |
| 10 | ASX | bitget | -559.98% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1065.50% | bitget | +5.47% | okx | -1060.02% |
| 2 | BWET | +1021.06% | bitget | +1095.00% | okx | +73.94% |
| 3 | SIMO | +600.50% | okx | +0.00% | bitget | -600.50% |
| 4 | BTW | +364.74% | okx | -419.61% | bitget | -784.35% |
| 5 | BOT | +360.47% | bitget | +360.47% | okx | +0.00% |
| 6 | IRYS | +303.64% | bitget | -112.46% | okx | -416.09% |
| 7 | FLY | +285.25% | bitget | +285.25% | okx | +0.00% |
| 8 | AXIS | +258.76% | okx | -461.20% | bitget | -719.96% |
| 9 | ISRG | +254.20% | bitget | +368.58% | okx | +114.38% |
| 10 | OUST | +200.06% | bitget | +200.06% | okx | +0.00% |
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
