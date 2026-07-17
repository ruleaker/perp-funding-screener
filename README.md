# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-17 17:35 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1118**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAMSUNG | okx | +658.45% |
| 2 | KIOXIA | okx | +462.84% |
| 3 | SKHYNIX | okx | +210.57% |
| 4 | FIGHT | bitget | +164.69% |
| 5 | XPD | okx | +121.27% |
| 6 | ZHIPU | okx | +120.68% |
| 7 | RAVE | okx | +112.24% |
| 8 | TUT | bitget | +77.96% |
| 9 | US | bitget | +76.21% |
| 10 | XPD | bitget | +74.24% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -569.29% |
| 2 | HOME | okx | -348.87% |
| 3 | TKO | bitget | -309.23% |
| 4 | LRC | okx | -297.32% |
| 5 | BONK | okx | -224.91% |
| 6 | 1000BONK | bitget | -201.92% |
| 7 | GWEI | bitget | -153.74% |
| 8 | FLOCK | bitget | -153.52% |
| 9 | EWH | bitget | -136.22% |
| 10 | OGN | bitget | -95.48% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SAMSUNG | +658.45% | okx | +658.45% | bitget | +0.00% |
| 2 | KIOXIA | +462.84% | okx | +462.84% | bitget | +0.00% |
| 3 | HOME | +220.42% | okx | -348.87% | bitget | -569.29% |
| 4 | SKHYNIX | +210.57% | okx | +210.57% | bitget | +0.00% |
| 5 | ZHIPU | +120.68% | okx | +120.68% | bitget | +0.00% |
| 6 | RAVE | +106.77% | okx | +112.24% | bitget | +5.47% |
| 7 | RDDT | +94.50% | okx | +0.00% | bitget | -94.50% |
| 8 | PROS | +50.06% | bitget | +5.47% | okx | -44.59% |
| 9 | XPD | +47.03% | okx | +121.27% | bitget | +74.24% |
| 10 | BSB | +37.58% | okx | +43.06% | bitget | +5.47% |
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
