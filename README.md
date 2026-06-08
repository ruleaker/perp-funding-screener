# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-08 05:10 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **951**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +766.94% |
| 2 | AAOI | okx | +227.60% |
| 3 | CRWD | okx | +227.40% |
| 4 | SHLD | okx | +183.68% |
| 5 | SKHYNIX | bitget | +109.50% |
| 6 | SAMSUNG | bitget | +109.50% |
| 7 | GWEI | bitget | +101.73% |
| 8 | URNM | okx | +100.06% |
| 9 | MRVL | okx | +92.65% |
| 10 | XLE | okx | +90.77% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -990.54% |
| 2 | HOME | okx | -915.63% |
| 3 | VRT | okx | -314.16% |
| 4 | ARIA | bitget | -291.71% |
| 5 | HPE | okx | -172.84% |
| 6 | RDW | okx | -148.33% |
| 7 | MOVE | okx | -144.64% |
| 8 | GEV | okx | -141.21% |
| 9 | PROVE | bitget | -139.50% |
| 10 | PROS | bitget | -124.06% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | VRT | +314.16% | bitget | +0.00% | okx | -314.16% |
| 2 | AAOI | +227.60% | okx | +227.60% | bitget | +0.00% |
| 3 | RDW | +148.33% | bitget | +0.00% | okx | -148.33% |
| 4 | MOVE | +141.57% | bitget | -3.07% | okx | -144.64% |
| 5 | MRVL | +92.65% | okx | +92.65% | bitget | +0.00% |
| 6 | MU | +82.33% | okx | +82.33% | bitget | +0.00% |
| 7 | HOME | +74.91% | okx | -915.63% | bitget | -990.54% |
| 8 | OP | +58.87% | okx | +7.29% | bitget | -51.57% |
| 9 | AMAT | +56.63% | okx | +56.63% | bitget | +0.00% |
| 10 | SAHARA | +52.57% | bitget | +66.14% | okx | +13.57% |
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
