# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-05-30 04:32 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **909**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AAOI | bitget | +109.50% |
| 2 | BE | bitget | +109.50% |
| 3 | NOKSTOCK | bitget | +109.50% |
| 4 | POET | bitget | +109.50% |
| 5 | CRWV | okx | +95.99% |
| 6 | NOK | okx | +95.00% |
| 7 | AXTI | bitget | +80.48% |
| 8 | NVDA | bitget | +69.97% |
| 9 | GOOGL | bitget | +65.15% |
| 10 | LITE | okx | +55.53% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | VTHO | bitget | -599.40% |
| 2 | ID | bitget | -453.44% |
| 3 | GENIUS | bitget | -355.33% |
| 4 | STXSTOCK | bitget | -109.50% |
| 5 | ZK | bitget | -97.56% |
| 6 | AIGENSYN | bitget | -78.62% |
| 7 | ME | bitget | -77.09% |
| 8 | GLW | okx | -62.48% |
| 9 | ALT | bitget | -59.35% |
| 10 | SKYAI | bitget | -58.47% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | AAOI | +98.55% | bitget | +109.50% | okx | +10.95% |
| 2 | BE | +98.55% | bitget | +109.50% | okx | +10.95% |
| 3 | ZK | +77.00% | okx | -20.56% | bitget | -97.56% |
| 4 | RKLB | +56.50% | okx | +10.95% | bitget | -45.55% |
| 5 | STX | +52.89% | okx | -2.96% | bitget | -55.84% |
| 6 | CRWV | +51.97% | okx | +95.99% | bitget | +44.02% |
| 7 | XPD | +50.19% | okx | +50.19% | bitget | +0.00% |
| 8 | AVGO | +50.18% | okx | +50.18% | bitget | +0.00% |
| 9 | HOME | +48.27% | bitget | +5.47% | okx | -42.79% |
| 10 | USAR | +47.28% | okx | +47.28% | bitget | +0.00% |
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
