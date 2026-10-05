# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-05 05:59 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1298**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +1095.00% |
| 2 | XIAOMI | okx | +291.66% |
| 3 | ACN | okx | +290.74% |
| 4 | NKE | okx | +266.66% |
| 5 | XIAOMI | bitget | +258.20% |
| 6 | BYD | bitget | +161.51% |
| 7 | WMT | okx | +160.81% |
| 8 | SECZ | okx | +155.25% |
| 9 | KUAISHOU | bitget | +139.72% |
| 10 | EWZ | okx | +131.89% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CARV | bitget | -1160.92% |
| 2 | ONE | bitget | -381.17% |
| 3 | QNT | bitget | -300.25% |
| 4 | ORCA | bitget | -140.49% |
| 5 | QUANT | okx | -125.31% |
| 6 | SAND | bitget | -121.11% |
| 7 | CSOPSAMSUNG2L | okx | -99.78% |
| 8 | SAND | okx | -86.17% |
| 9 | USO | okx | -82.73% |
| 10 | GFS | bitget | -70.30% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1095.00% | okx | +1095.00% | bitget | +0.00% |
| 2 | ONE | +389.58% | okx | +8.41% | bitget | -381.17% |
| 3 | QNT | +311.88% | okx | +11.64% | bitget | -300.25% |
| 4 | NKE | +266.66% | okx | +266.66% | bitget | +0.00% |
| 5 | WMT | +160.81% | okx | +160.81% | bitget | +0.00% |
| 6 | SECZ | +147.80% | okx | +155.25% | bitget | +7.45% |
| 7 | EWZ | +131.89% | okx | +131.89% | bitget | +0.00% |
| 8 | TMF | +127.82% | okx | +127.82% | bitget | +0.00% |
| 9 | BWET | +86.42% | okx | +64.08% | bitget | -22.34% |
| 10 | RDW | +73.09% | okx | +73.09% | bitget | +0.00% |
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
