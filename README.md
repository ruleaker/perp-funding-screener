# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-21 18:02 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1021**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +147.29% |
| 2 | BICO | bitget | +107.31% |
| 3 | INFQ | okx | +105.40% |
| 4 | SIREN | bitget | +86.07% |
| 5 | ESPORTS | bitget | +64.06% |
| 6 | SOON | okx | +56.34% |
| 7 | BEAT | okx | +52.59% |
| 8 | M | bitget | +51.57% |
| 9 | UB | okx | +50.52% |
| 10 | FOLKS | bitget | +41.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H | bitget | -771.97% |
| 2 | TNSR | bitget | -635.43% |
| 3 | H | okx | -429.28% |
| 4 | RE | bitget | -289.52% |
| 5 | RE | okx | -239.93% |
| 6 | HOME | okx | -209.29% |
| 7 | FIDA | bitget | -203.89% |
| 8 | BAND | bitget | -159.87% |
| 9 | 2Z | okx | -154.05% |
| 10 | SPELL | bitget | -143.77% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +342.69% | okx | -429.28% | bitget | -771.97% |
| 2 | BAND | +170.82% | okx | +10.95% | bitget | -159.87% |
| 3 | SKHYNIX | +147.29% | okx | +147.29% | bitget | +0.00% |
| 4 | BICO | +138.51% | bitget | +107.31% | okx | -31.20% |
| 5 | HOME | +129.68% | bitget | -79.61% | okx | -209.29% |
| 6 | INFQ | +105.40% | okx | +105.40% | bitget | +0.00% |
| 7 | ACU | +103.48% | okx | +5.47% | bitget | -98.00% |
| 8 | RESOLV | +55.51% | bitget | -1.53% | okx | -57.05% |
| 9 | SOON | +50.86% | okx | +56.34% | bitget | +5.47% |
| 10 | RE | +49.58% | okx | -239.93% | bitget | -289.52% |
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
