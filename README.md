# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-09 21:04 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1305**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +1095.00% |
| 2 | NATGAS | bitget | +547.50% |
| 3 | GPRO | bitget | +234.88% |
| 4 | AGPU | bitget | +147.17% |
| 5 | SKUU | bitget | +99.75% |
| 6 | AEHR | okx | +83.08% |
| 7 | BOT | bitget | +73.80% |
| 8 | AXTI | okx | +73.28% |
| 9 | TLT | bitget | +72.05% |
| 10 | KII | okx | +71.98% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -1095.00% |
| 2 | BZ | bitget | -325.76% |
| 3 | CTSI | bitget | -279.23% |
| 4 | BZ | okx | -260.78% |
| 5 | USO | okx | -259.27% |
| 6 | BWET | bitget | -256.89% |
| 7 | XDP | okx | -167.18% |
| 8 | KAIA | bitget | -145.53% |
| 9 | MINA | bitget | -143.12% |
| 10 | OKTA | okx | -141.14% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1095.00% | bitget | +0.00% | okx | -1095.00% |
| 2 | GPRO | +230.62% | bitget | +234.88% | okx | +4.26% |
| 3 | BWET | +201.75% | okx | -55.14% | bitget | -256.89% |
| 4 | OKTA | +141.14% | bitget | +0.00% | okx | -141.14% |
| 5 | CYPH | +90.45% | okx | +0.00% | bitget | -90.45% |
| 6 | AEHR | +83.08% | okx | +83.08% | bitget | +0.00% |
| 7 | BOT | +73.80% | bitget | +73.80% | okx | +0.00% |
| 8 | SAND | +65.58% | okx | -50.38% | bitget | -115.96% |
| 9 | BZ | +64.99% | okx | -260.78% | bitget | -325.76% |
| 10 | AXTI | +60.90% | okx | +73.28% | bitget | +12.37% |
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
