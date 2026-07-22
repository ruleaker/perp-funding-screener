# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-22 17:47 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZHIPU | okx | +141.50% |
| 2 | BANK | bitget | +119.25% |
| 3 | SKHYNIX | okx | +110.12% |
| 4 | SAMSUNG | okx | +108.50% |
| 5 | 龙虾 | bitget | +98.77% |
| 6 | EPIC | bitget | +84.75% |
| 7 | SPCX | bitget | +69.75% |
| 8 | GOOGL | bitget | +65.70% |
| 9 | QNTSTOCK | bitget | +65.04% |
| 10 | BUD | bitget | +61.65% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MIRA | bitget | -2190.00% |
| 2 | ONE | bitget | -820.59% |
| 3 | DEXE | bitget | -792.56% |
| 4 | ONE | okx | -354.97% |
| 5 | RDDT | bitget | -261.81% |
| 6 | TLM | bitget | -239.70% |
| 7 | ERA | bitget | -177.83% |
| 8 | RE | bitget | -130.85% |
| 9 | T | bitget | -129.54% |
| 10 | RE | okx | -103.72% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +465.62% | okx | -354.97% | bitget | -820.59% |
| 2 | RDDT | +261.81% | okx | +0.00% | bitget | -261.81% |
| 3 | ZHIPU | +141.50% | okx | +141.50% | bitget | +0.00% |
| 4 | SKHYNIX | +110.12% | okx | +110.12% | bitget | +0.00% |
| 5 | SAMSUNG | +108.50% | okx | +108.50% | bitget | +0.00% |
| 6 | RAY | +55.12% | bitget | +5.47% | okx | -49.64% |
| 7 | SPCX | +53.49% | bitget | +69.75% | okx | +16.26% |
| 8 | ZIL | +50.39% | okx | -47.40% | bitget | -97.78% |
| 9 | DATA | +50.15% | bitget | -0.66% | okx | -50.80% |
| 10 | COIN | +39.31% | bitget | +39.31% | okx | +0.00% |
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
