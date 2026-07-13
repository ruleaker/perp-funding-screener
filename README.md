# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-13 11:36 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1106**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOXS | bitget | +547.50% |
| 2 | DXYZ | bitget | +493.95% |
| 3 | OSS | bitget | +407.56% |
| 4 | SAMSUNG | okx | +397.89% |
| 5 | HYUNDAI | okx | +369.35% |
| 6 | SKHYNIX | okx | +365.75% |
| 7 | SKHYNIX | bitget | +360.91% |
| 8 | CGNX | bitget | +151.99% |
| 9 | KIOXIA | okx | +115.62% |
| 10 | MINIMAX | bitget | +97.45% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOFTBANK | okx | -485.80% |
| 2 | VANRY | bitget | -318.97% |
| 3 | TLM | bitget | -267.95% |
| 4 | NATGAS | bitget | -241.67% |
| 5 | T | bitget | -236.30% |
| 6 | INDA | bitget | -233.56% |
| 7 | 1000XEC | bitget | -211.44% |
| 8 | OGN | bitget | -202.03% |
| 9 | RDDT | bitget | -171.70% |
| 10 | ROK | okx | -136.83% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HYUNDAI | +346.68% | okx | +369.35% | bitget | +22.67% |
| 2 | SAMSUNG | +320.48% | okx | +397.89% | bitget | +77.42% |
| 3 | RDDT | +171.70% | okx | +0.00% | bitget | -171.70% |
| 4 | CGNX | +159.48% | bitget | +151.99% | okx | -7.49% |
| 5 | ROK | +136.83% | bitget | +0.00% | okx | -136.83% |
| 6 | KIOXIA | +113.87% | okx | +115.62% | bitget | +1.75% |
| 7 | MINIMAX | +97.45% | bitget | +97.45% | okx | +0.00% |
| 8 | CRO | +83.04% | bitget | +10.95% | okx | -72.09% |
| 9 | VRT | +75.66% | okx | +0.00% | bitget | -75.66% |
| 10 | BSP | +75.15% | bitget | +0.00% | okx | -75.15% |
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
