# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-04 22:02 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1397**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AGPU | bitget | +275.28% |
| 2 | 哈基米 | bitget | +151.33% |
| 3 | KR200 | okx | +126.35% |
| 4 | CPNG | bitget | +123.84% |
| 5 | EWZS | bitget | +116.73% |
| 6 | USDESTOCK | bitget | +103.59% |
| 7 | DELL | bitget | +88.48% |
| 8 | MSTU | okx | +78.67% |
| 9 | SOXL | bitget | +75.45% |
| 10 | SOXL | okx | +68.97% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LSK | bitget | -256.45% |
| 2 | HUMA | okx | -230.53% |
| 3 | 1MBABYDOGE | bitget | -226.66% |
| 4 | POWER | bitget | -219.33% |
| 5 | ERA | bitget | -202.90% |
| 6 | HUMA | bitget | -196.00% |
| 7 | ADI | okx | -174.86% |
| 8 | ACN | okx | -158.02% |
| 9 | TWLO | okx | -140.86% |
| 10 | BNC | bitget | -138.19% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | TWLO | +140.86% | bitget | +0.00% | okx | -140.86% |
| 2 | RUM | +134.69% | okx | +0.00% | bitget | -134.69% |
| 3 | CGNX | +127.36% | bitget | +0.00% | okx | -127.36% |
| 4 | KR200 | +126.35% | okx | +126.35% | bitget | +0.00% |
| 5 | IRYS | +67.46% | bitget | -18.72% | okx | -86.18% |
| 6 | JP225 | +49.65% | okx | +49.65% | bitget | +0.00% |
| 7 | MARA | +45.15% | okx | +45.15% | bitget | +0.00% |
| 8 | SOFTBANK | +45.14% | bitget | -59.90% | okx | -105.04% |
| 9 | ADI | +43.14% | bitget | -131.73% | okx | -174.86% |
| 10 | ARM | +41.39% | bitget | +41.39% | okx | +0.00% |
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
