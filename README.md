# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-13 18:16 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1106**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | okx | +115.64% |
| 2 | 龙虾 | bitget | +90.89% |
| 3 | MUBARAK | bitget | +87.71% |
| 4 | KORU | okx | +80.30% |
| 5 | SOXS | bitget | +77.96% |
| 6 | GOOGL | bitget | +67.34% |
| 7 | RAM | okx | +61.78% |
| 8 | TWLO | okx | +57.07% |
| 9 | LAB | bitget | +56.39% |
| 10 | KORU | bitget | +55.08% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SENT | okx | -521.72% |
| 2 | SENT | bitget | -500.85% |
| 3 | 1000XEC | bitget | -240.57% |
| 4 | NEWT | bitget | -199.07% |
| 5 | VANRY | bitget | -175.53% |
| 6 | HOT | bitget | -172.13% |
| 7 | TLM | bitget | -140.60% |
| 8 | OGN | bitget | -125.16% |
| 9 | BONK | okx | -122.79% |
| 10 | BARD | bitget | -116.29% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | PI | +82.61% | bitget | +5.47% | okx | -77.14% |
| 2 | MUBARAK | +82.23% | bitget | +87.71% | okx | +5.47% |
| 3 | CRO | +77.42% | bitget | +10.95% | okx | -66.47% |
| 4 | CGNX | +67.59% | bitget | +0.00% | okx | -67.59% |
| 5 | GOOGL | +67.34% | bitget | +67.34% | okx | +0.00% |
| 6 | RAM | +61.78% | okx | +61.78% | bitget | +0.00% |
| 7 | ALGO | +60.89% | bitget | +10.95% | okx | -49.94% |
| 8 | LAB | +59.25% | okx | +115.64% | bitget | +56.39% |
| 9 | TWLO | +57.07% | okx | +57.07% | bitget | +0.00% |
| 10 | ESP | +52.27% | okx | -23.72% | bitget | -75.99% |
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
