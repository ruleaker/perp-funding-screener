# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-14 20:16 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1322**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AGPU | bitget | +229.95% |
| 2 | JP225 | okx | +122.36% |
| 3 | MP | bitget | +112.24% |
| 4 | GPRO | bitget | +98.77% |
| 5 | SOXL | bitget | +96.47% |
| 6 | GWEI | bitget | +89.46% |
| 7 | US100 | okx | +78.30% |
| 8 | TLT | okx | +73.80% |
| 9 | ARC | bitget | +73.26% |
| 10 | ARIA | bitget | +61.87% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -1095.00% |
| 2 | WAL | bitget | -450.26% |
| 3 | WAL | okx | -419.94% |
| 4 | BLUR | bitget | -215.17% |
| 5 | BLUR | okx | -191.39% |
| 6 | BSP | okx | -168.54% |
| 7 | BSP | bitget | -156.91% |
| 8 | CSOPSS2LHKD | bitget | -137.31% |
| 9 | CSOPSK2LHKD | bitget | -116.18% |
| 10 | OKTA | okx | -115.06% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1095.00% | bitget | +0.00% | okx | -1095.00% |
| 2 | JP225 | +122.36% | okx | +122.36% | bitget | +0.00% |
| 3 | OKTA | +115.06% | bitget | +0.00% | okx | -115.06% |
| 4 | GPRO | +98.77% | bitget | +98.77% | okx | +0.00% |
| 5 | SKHYNIX | +76.44% | bitget | -12.15% | okx | -88.59% |
| 6 | TLT | +73.80% | okx | +73.80% | bitget | +0.00% |
| 7 | KO | +72.40% | bitget | +0.00% | okx | -72.40% |
| 8 | SOXL | +70.85% | bitget | +96.47% | okx | +25.62% |
| 9 | SAMSUNG | +70.25% | bitget | -2.96% | okx | -73.20% |
| 10 | UNITREE | +68.23% | bitget | +0.00% | okx | -68.23% |
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
