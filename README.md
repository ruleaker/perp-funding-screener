# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-11 12:54 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1250**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +353.83% |
| 2 | NKE | bitget | +207.72% |
| 3 | NATGAS | bitget | +204.00% |
| 4 | GPRO | okx | +179.92% |
| 5 | GPRO | bitget | +123.84% |
| 6 | GTLB | bitget | +116.84% |
| 7 | FLY | bitget | +112.89% |
| 8 | RDDT | bitget | +96.36% |
| 9 | VRT | okx | +95.43% |
| 10 | SIREN | bitget | +70.30% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | VTHO | bitget | -1065.11% |
| 2 | ETN | bitget | -411.28% |
| 3 | ICX | okx | -402.40% |
| 4 | USO | okx | -318.80% |
| 5 | RVN | okx | -299.98% |
| 6 | RVN | bitget | -241.23% |
| 7 | BZ | okx | -181.89% |
| 8 | BZ | bitget | -179.58% |
| 9 | CL | bitget | -175.09% |
| 10 | CL | okx | -172.63% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | FLY | +112.89% | bitget | +112.89% | okx | +0.00% |
| 2 | VRT | +95.43% | okx | +95.43% | bitget | +0.00% |
| 3 | UNITREE | +94.70% | bitget | +0.00% | okx | -94.70% |
| 4 | RDDT | +85.07% | bitget | +96.36% | okx | +11.29% |
| 5 | WEN | +78.90% | bitget | +0.00% | okx | -78.90% |
| 6 | PI | +70.50% | okx | -21.26% | bitget | -91.76% |
| 7 | ZIL | +65.22% | okx | -47.79% | bitget | -113.00% |
| 8 | SKUU | +61.21% | bitget | +61.21% | okx | +0.00% |
| 9 | ONE | +59.31% | okx | +70.26% | bitget | +10.95% |
| 10 | RVN | +58.75% | bitget | -241.23% | okx | -299.98% |
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
