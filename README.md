# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-30 05:36 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1208**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KORU | okx | +119.89% |
| 2 | ESPORTS | bitget | +80.15% |
| 3 | UNITAS | bitget | +70.08% |
| 4 | TAG | bitget | +55.19% |
| 5 | ARIA | bitget | +50.04% |
| 6 | PIPPIN | bitget | +49.93% |
| 7 | ONE | okx | +49.90% |
| 8 | TRUTH | okx | +47.75% |
| 9 | QNT | okx | +46.85% |
| 10 | 龙虾 | bitget | +45.77% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TUT | bitget | -891.77% |
| 2 | BICO | bitget | -594.80% |
| 3 | BICO | okx | -478.99% |
| 4 | HOME | okx | -247.43% |
| 5 | HOME | bitget | -242.00% |
| 6 | ZKC | bitget | -204.44% |
| 7 | SAND | okx | -178.73% |
| 8 | ACE | bitget | -112.35% |
| 9 | JST | bitget | -101.40% |
| 10 | 1000SATS | bitget | -100.96% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SAND | +189.68% | bitget | +10.95% | okx | -178.73% |
| 2 | KORU | +119.89% | okx | +119.89% | bitget | +0.00% |
| 3 | BICO | +115.81% | okx | -478.99% | bitget | -594.80% |
| 4 | RVN | +88.94% | bitget | +3.29% | okx | -85.66% |
| 5 | PROS | +70.08% | okx | +5.47% | bitget | -64.61% |
| 6 | NOW | +59.72% | bitget | +0.00% | okx | -59.72% |
| 7 | ZKP | +48.58% | bitget | -45.33% | okx | -93.92% |
| 8 | PIPPIN | +44.46% | bitget | +49.93% | okx | +5.47% |
| 9 | ONE | +38.95% | okx | +49.90% | bitget | +10.95% |
| 10 | QNT | +35.90% | okx | +46.85% | bitget | +10.95% |
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
