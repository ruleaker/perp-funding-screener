# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-29 07:13 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1208**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITAS | bitget | +108.08% |
| 2 | TRUTH | okx | +79.56% |
| 3 | KORU | okx | +76.94% |
| 4 | LIGHT | okx | +65.71% |
| 5 | ONE | okx | +61.18% |
| 6 | LYN | bitget | +60.99% |
| 7 | ARIA | bitget | +59.13% |
| 8 | DOS | okx | +54.67% |
| 9 | BTW | bitget | +53.11% |
| 10 | BEAT | bitget | +48.40% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAND | okx | -162.85% |
| 2 | RVN | okx | -143.37% |
| 3 | SKR | bitget | -133.15% |
| 4 | HOME | okx | -100.05% |
| 5 | BICO | bitget | -96.25% |
| 6 | HOME | bitget | -90.23% |
| 7 | GWEI | bitget | -83.55% |
| 8 | 1000SATS | bitget | -75.55% |
| 9 | BICO | okx | -73.76% |
| 10 | ATOM | bitget | -58.36% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RVN | +148.84% | bitget | +5.47% | okx | -143.37% |
| 2 | SAND | +134.81% | bitget | -28.03% | okx | -162.85% |
| 3 | KORU | +76.94% | okx | +76.94% | bitget | +0.00% |
| 4 | ONE | +50.23% | okx | +61.18% | bitget | +10.95% |
| 5 | ATOM | +45.62% | okx | -12.75% | bitget | -58.36% |
| 6 | ALGO | +43.13% | bitget | +10.95% | okx | -32.18% |
| 7 | BEAT | +42.92% | bitget | +48.40% | okx | +5.47% |
| 8 | BB | +39.61% | okx | +45.09% | bitget | +5.47% |
| 9 | DOS | +32.66% | okx | +54.67% | bitget | +22.01% |
| 10 | CXMT | +31.74% | okx | +31.74% | bitget | +0.00% |
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
