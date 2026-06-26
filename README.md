# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-26 11:21 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1049**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SATSSTOCK | bitget | +547.50% |
| 2 | KIOXIA | okx | +351.27% |
| 3 | SOXS | bitget | +198.52% |
| 4 | GLW | okx | +159.35% |
| 5 | GLW | bitget | +132.28% |
| 6 | EH | bitget | +126.80% |
| 7 | KORU | okx | +113.33% |
| 8 | RDDT | bitget | +87.82% |
| 9 | NOKSTOCK | bitget | +87.38% |
| 10 | SIREN | bitget | +86.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | okx | -828.08% |
| 2 | MUU | bitget | -547.50% |
| 3 | LAB | bitget | -546.62% |
| 4 | OUST | bitget | -363.65% |
| 5 | AGLD | okx | -307.63% |
| 6 | CARV | bitget | -303.53% |
| 7 | AGLD | bitget | -273.97% |
| 8 | APLD | bitget | -263.68% |
| 9 | O | okx | -222.26% |
| 10 | BICO | bitget | -213.31% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KIOXIA | +351.27% | okx | +351.27% | bitget | +0.00% |
| 2 | KORU | +312.19% | okx | +113.33% | bitget | -198.85% |
| 3 | LAB | +281.46% | bitget | -546.62% | okx | -828.08% |
| 4 | TSEM | +185.82% | okx | +0.00% | bitget | -185.82% |
| 5 | HPE | +177.39% | okx | +0.00% | bitget | -177.39% |
| 6 | BX | +150.08% | okx | -8.37% | bitget | -158.45% |
| 7 | MSTR | +91.65% | okx | +0.00% | bitget | -91.65% |
| 8 | BICO | +88.04% | okx | -125.26% | bitget | -213.31% |
| 9 | RDDT | +87.82% | bitget | +87.82% | okx | +0.00% |
| 10 | SHIB | +85.19% | okx | +10.95% | bitget | -74.24% |
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
