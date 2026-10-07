# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-07 06:15 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1302**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NAVER | bitget | +703.10% |
| 2 | LGELECTRONICS | bitget | +596.34% |
| 3 | NG | okx | +531.13% |
| 4 | SAMSUNGEM | bitget | +496.91% |
| 5 | KIOXIA | bitget | +299.70% |
| 6 | HANMI | bitget | +242.87% |
| 7 | NATGAS | bitget | +241.34% |
| 8 | CSOPSKHYNIX2L | okx | +230.59% |
| 9 | BOT | okx | +215.84% |
| 10 | ACN | okx | +215.62% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -1095.00% |
| 2 | NMR | bitget | -427.49% |
| 3 | BWET | okx | -299.12% |
| 4 | SAND | bitget | -225.35% |
| 5 | API3 | okx | -199.76% |
| 6 | CYPH | bitget | -175.75% |
| 7 | API3 | bitget | -158.99% |
| 8 | SAND | okx | -147.13% |
| 9 | KORU | bitget | -132.71% |
| 10 | UMA | okx | -131.68% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1095.00% | bitget | +0.00% | okx | -1095.00% |
| 2 | NAVER | +489.29% | bitget | +703.10% | okx | +213.81% |
| 3 | LGELECTRONICS | +386.80% | bitget | +596.34% | okx | +209.53% |
| 4 | NMR | +331.25% | okx | -96.24% | bitget | -427.49% |
| 5 | BWET | +299.12% | bitget | +0.00% | okx | -299.12% |
| 6 | HANMI | +242.87% | bitget | +242.87% | okx | +0.00% |
| 7 | BOT | +215.84% | okx | +215.84% | bitget | +0.00% |
| 8 | KIOXIA | +195.45% | bitget | +299.70% | okx | +104.25% |
| 9 | INTW | +171.70% | bitget | +171.70% | okx | +0.00% |
| 10 | CYPH | +169.38% | okx | -6.37% | bitget | -175.75% |
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
