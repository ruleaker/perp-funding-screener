# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-03 04:24 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1077**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | bitget | +547.50% |
| 2 | SKHYNIX | okx | +360.69% |
| 3 | MRVL | okx | +211.74% |
| 4 | KORU | okx | +194.99% |
| 5 | SAMSUNG | bitget | +174.65% |
| 6 | EWY | okx | +173.52% |
| 7 | SNDK | okx | +163.89% |
| 8 | SAMSUNG | okx | +151.33% |
| 9 | HYUNDAI | bitget | +148.48% |
| 10 | BOT | okx | +142.22% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZKP | bitget | -2190.00% |
| 2 | MIRA | bitget | -1340.06% |
| 3 | ZKP | okx | -1095.00% |
| 4 | BIRB | bitget | -1062.26% |
| 5 | LAB | bitget | -797.60% |
| 6 | GWEI | bitget | -795.74% |
| 7 | LAB | okx | -792.15% |
| 8 | BLEND | okx | -720.49% |
| 9 | 10000NEX | bitget | -410.73% |
| 10 | SLX | okx | -398.68% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ZKP | +1095.00% | okx | -1095.00% | bitget | -2190.00% |
| 2 | MRVL | +194.33% | okx | +211.74% | bitget | +17.41% |
| 3 | SKHYNIX | +186.81% | bitget | +547.50% | okx | +360.69% |
| 4 | EWY | +173.52% | okx | +173.52% | bitget | +0.00% |
| 5 | KORU | +168.60% | okx | +194.99% | bitget | +26.39% |
| 6 | SLX | +164.25% | bitget | -234.44% | okx | -398.68% |
| 7 | SNDK | +157.98% | okx | +163.89% | bitget | +5.91% |
| 8 | ME | +130.44% | okx | -140.24% | bitget | -270.68% |
| 9 | MU | +120.42% | okx | +120.42% | bitget | +0.00% |
| 10 | PLTR | +110.16% | bitget | +110.16% | okx | +0.00% |
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
