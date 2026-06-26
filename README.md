# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-26 04:48 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1051**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +576.72% |
| 2 | SKHYNIX | bitget | +547.50% |
| 3 | HYUNDAI | bitget | +297.29% |
| 4 | KORU | okx | +293.39% |
| 5 | GLW | okx | +267.28% |
| 6 | VRT | okx | +247.13% |
| 7 | HYUNDAI | okx | +247.01% |
| 8 | POET | okx | +232.12% |
| 9 | SAMSUNG | bitget | +190.42% |
| 10 | RDW | okx | +183.06% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | okx | -362.10% |
| 2 | CARV | bitget | -323.79% |
| 3 | M | bitget | -308.90% |
| 4 | KORU | bitget | -212.10% |
| 5 | LAB | bitget | -184.95% |
| 6 | TAIKO | bitget | -146.29% |
| 7 | O | bitget | -125.92% |
| 8 | RE | bitget | -117.17% |
| 9 | IP | okx | -109.86% |
| 10 | O | okx | -93.76% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KORU | +505.49% | okx | +293.39% | bitget | -212.10% |
| 2 | GLW | +279.22% | okx | +267.28% | bitget | -11.94% |
| 3 | VRT | +247.13% | okx | +247.13% | bitget | +0.00% |
| 4 | POET | +232.12% | okx | +232.12% | bitget | +0.00% |
| 5 | RDW | +183.06% | okx | +183.06% | bitget | +0.00% |
| 6 | LAB | +177.16% | bitget | -184.95% | okx | -362.10% |
| 7 | SOXL | +145.37% | okx | +89.53% | bitget | -55.84% |
| 8 | KIOXIA | +105.42% | okx | +105.42% | bitget | +0.00% |
| 9 | INFQ | +84.26% | okx | +84.26% | bitget | +0.00% |
| 10 | ACU | +79.50% | okx | +5.47% | bitget | -74.02% |
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
