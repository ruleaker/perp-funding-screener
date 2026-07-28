# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-28 17:50 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1147**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KR200 | okx | +517.58% |
| 2 | KIOXIA | okx | +176.06% |
| 3 | SNDK | bitget | +139.72% |
| 4 | SKHYNIX | okx | +133.22% |
| 5 | SNXX | okx | +123.70% |
| 6 | NDX100 | bitget | +116.40% |
| 7 | SNDK | okx | +96.05% |
| 8 | SKHY | bitget | +95.16% |
| 9 | FWDI | bitget | +89.24% |
| 10 | SOXL | bitget | +75.34% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LA | bitget | -1141.21% |
| 2 | LA | okx | -531.28% |
| 3 | HOT | bitget | -342.74% |
| 4 | STORJ | bitget | -247.47% |
| 5 | VANRY | bitget | -218.56% |
| 6 | ZIL | bitget | -170.82% |
| 7 | ZIL | okx | -165.40% |
| 8 | TLM | bitget | -120.89% |
| 9 | AEON | bitget | -117.93% |
| 10 | AEON | okx | -108.03% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LA | +609.93% | okx | -531.28% | bitget | -1141.21% |
| 2 | KIOXIA | +176.06% | okx | +176.06% | bitget | +0.00% |
| 3 | SKHYNIX | +133.22% | okx | +133.22% | bitget | +0.00% |
| 4 | FWDI | +89.24% | bitget | +89.24% | okx | +0.00% |
| 5 | SNXX | +84.94% | okx | +123.70% | bitget | +38.76% |
| 6 | BOT | +65.48% | okx | +0.00% | bitget | -65.48% |
| 7 | AIXBT | +57.23% | bitget | +5.47% | okx | -51.75% |
| 8 | CHZ | +54.05% | bitget | +10.95% | okx | -43.10% |
| 9 | SHAZ | +51.68% | okx | +0.00% | bitget | -51.68% |
| 10 | BIO | +50.91% | bitget | +5.47% | okx | -45.43% |
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
