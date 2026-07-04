# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-04 04:09 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1078**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | EVAA | bitget | +110.92% |
| 2 | XPIN | bitget | +99.64% |
| 3 | RDW | okx | +92.15% |
| 4 | RIVN | okx | +84.29% |
| 5 | US | bitget | +77.20% |
| 6 | USAR | okx | +72.63% |
| 7 | KORU | okx | +68.11% |
| 8 | SOXL | okx | +64.56% |
| 9 | PIPPIN | bitget | +52.12% |
| 10 | SNDK | okx | +51.40% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MIRA | bitget | -1119.75% |
| 2 | ZKP | okx | -392.51% |
| 3 | SLX | okx | -366.12% |
| 4 | 10000NEX | bitget | -294.77% |
| 5 | LA | okx | -271.01% |
| 6 | RE | okx | -245.57% |
| 7 | RE | bitget | -232.25% |
| 8 | ARPA | bitget | -211.77% |
| 9 | SLX | bitget | -192.83% |
| 10 | LA | bitget | -151.55% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ZKP | +345.53% | bitget | -46.98% | okx | -392.51% |
| 2 | SLX | +173.29% | bitget | -192.83% | okx | -366.12% |
| 3 | LA | +119.46% | bitget | -151.55% | okx | -271.01% |
| 4 | KSM | +104.26% | okx | -1.41% | bitget | -105.67% |
| 5 | LAB | +101.22% | bitget | -7.77% | okx | -108.99% |
| 6 | RDW | +92.15% | okx | +92.15% | bitget | +0.00% |
| 7 | ARX | +81.57% | bitget | -6.24% | okx | -87.81% |
| 8 | USAR | +72.63% | okx | +72.63% | bitget | +0.00% |
| 9 | ATOM | +72.37% | okx | +7.43% | bitget | -64.93% |
| 10 | KORU | +68.11% | okx | +68.11% | bitget | +0.00% |
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
