# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-01 20:42 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **928**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +625.90% |
| 2 | SHLD | okx | +410.36% |
| 3 | INX | bitget | +331.24% |
| 4 | GLW | okx | +318.72% |
| 5 | GEV | okx | +198.14% |
| 6 | COHR | okx | +157.19% |
| 7 | LYN | bitget | +151.55% |
| 8 | RKLB | okx | +150.06% |
| 9 | AAOI | okx | +146.82% |
| 10 | URNM | okx | +130.70% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -847.53% |
| 2 | HOME | okx | -547.23% |
| 3 | GUN | bitget | -240.57% |
| 4 | SLX | bitget | -229.51% |
| 5 | DRIFT | bitget | -227.21% |
| 6 | SLX | okx | -74.30% |
| 7 | AI | okx | -71.35% |
| 8 | TRX | bitget | -65.81% |
| 9 | ACU | bitget | -55.84% |
| 10 | STG | bitget | -54.42% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HOME | +300.30% | okx | -547.23% | bitget | -847.53% |
| 2 | COHR | +157.19% | okx | +157.19% | bitget | +0.00% |
| 3 | SLX | +155.21% | okx | -74.30% | bitget | -229.51% |
| 4 | RKLB | +150.06% | okx | +150.06% | bitget | +0.00% |
| 5 | AAOI | +146.82% | okx | +146.82% | bitget | +0.00% |
| 6 | DELL | +104.69% | okx | +104.69% | bitget | +0.00% |
| 7 | LAB | +102.28% | okx | +108.08% | bitget | +5.80% |
| 8 | BEAT | +87.90% | bitget | +116.73% | okx | +28.82% |
| 9 | NBIS | +87.58% | okx | +87.58% | bitget | +0.00% |
| 10 | RAVE | +81.42% | okx | +86.89% | bitget | +5.47% |
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
