# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-11 06:05 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1305**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 哈基米 | bitget | +74.24% |
| 2 | TRUTH | okx | +57.58% |
| 3 | CTR | bitget | +57.38% |
| 4 | NVDL | okx | +55.98% |
| 5 | BAN | bitget | +54.64% |
| 6 | UP | okx | +53.44% |
| 7 | US100 | okx | +50.88% |
| 8 | US500 | okx | +47.55% |
| 9 | XPIN | bitget | +33.18% |
| 10 | LAB | okx | +23.30% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ERA | bitget | -1275.46% |
| 2 | MINA | bitget | -520.12% |
| 3 | H100 | okx | -402.58% |
| 4 | WAL | bitget | -349.85% |
| 5 | WAL | okx | -340.64% |
| 6 | LA | bitget | -307.04% |
| 7 | LA | okx | -269.50% |
| 8 | MINA | okx | -264.63% |
| 9 | MAGIC | okx | -231.99% |
| 10 | MAGIC | bitget | -199.51% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +402.58% | bitget | +0.00% | okx | -402.58% |
| 2 | MINA | +255.50% | okx | -264.63% | bitget | -520.12% |
| 3 | NVDL | +55.98% | okx | +55.98% | bitget | +0.00% |
| 4 | 1INCH | +42.69% | bitget | +6.35% | okx | -36.34% |
| 5 | ONE | +42.16% | okx | +5.47% | bitget | -36.68% |
| 6 | TSLL | +40.87% | bitget | +0.00% | okx | -40.87% |
| 7 | LA | +37.54% | okx | -269.50% | bitget | -307.04% |
| 8 | CT | +33.54% | bitget | +3.50% | okx | -30.04% |
| 9 | MAGIC | +32.48% | bitget | -199.51% | okx | -231.99% |
| 10 | LPT | +29.69% | bitget | +5.47% | okx | -24.21% |
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
