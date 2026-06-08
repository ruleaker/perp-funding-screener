# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-08 12:44 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **967**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BEAT | okx | +234.41% |
| 2 | AAOI | okx | +217.05% |
| 3 | INX | bitget | +115.52% |
| 4 | LAB | bitget | +106.98% |
| 5 | MU | okx | +102.39% |
| 6 | MAGMA | bitget | +74.35% |
| 7 | VELVET | bitget | +74.13% |
| 8 | APR | okx | +71.47% |
| 9 | MRVL | okx | +69.39% |
| 10 | GME | okx | +69.38% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MOVE | okx | -599.15% |
| 2 | HOME | bitget | -536.55% |
| 3 | HOME | okx | -529.24% |
| 4 | MOVE | bitget | -438.77% |
| 5 | ME | okx | -156.81% |
| 6 | FIDA | bitget | -151.55% |
| 7 | H | bitget | -120.67% |
| 8 | ZEC | okx | -111.02% |
| 9 | STABLE | okx | -105.24% |
| 10 | SIREN | bitget | -102.05% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | AAOI | +217.05% | okx | +217.05% | bitget | +0.00% |
| 2 | BEAT | +193.24% | okx | +234.41% | bitget | +41.17% |
| 3 | MOVE | +160.38% | bitget | -438.77% | okx | -599.15% |
| 4 | LAB | +101.51% | bitget | +106.98% | okx | +5.47% |
| 5 | ME | +72.06% | bitget | -84.75% | okx | -156.81% |
| 6 | MRVL | +69.39% | okx | +69.39% | bitget | +0.00% |
| 7 | GME | +69.38% | okx | +69.38% | bitget | +0.00% |
| 8 | APR | +66.00% | okx | +71.47% | bitget | +5.47% |
| 9 | STABLE | +65.93% | bitget | -39.31% | okx | -105.24% |
| 10 | MU | +64.39% | okx | +102.39% | bitget | +38.00% |
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
