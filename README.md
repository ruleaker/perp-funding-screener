# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-14 05:14 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **982**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SHLD | okx | +341.57% |
| 2 | AMD | okx | +135.08% |
| 3 | EPIC | bitget | +84.21% |
| 4 | TRUTH | okx | +81.56% |
| 5 | ASR | bitget | +76.98% |
| 6 | CARV | bitget | +74.35% |
| 7 | PROS | bitget | +70.52% |
| 8 | HIMS | okx | +68.51% |
| 9 | RAVE | okx | +59.71% |
| 10 | ROK | okx | +54.75% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H | okx | -486.16% |
| 2 | HOME | okx | -402.94% |
| 3 | STG | bitget | -396.06% |
| 4 | ESPORTS | bitget | -312.62% |
| 5 | HOME | bitget | -205.53% |
| 6 | ZKP | bitget | -179.80% |
| 7 | ZKP | okx | -165.98% |
| 8 | BEAT | okx | -151.31% |
| 9 | TON | okx | -117.66% |
| 10 | GENIUS | bitget | -95.05% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +397.69% | bitget | -88.48% | okx | -486.16% |
| 2 | HOME | +197.40% | bitget | -205.53% | okx | -402.94% |
| 3 | AMD | +135.08% | okx | +135.08% | bitget | +0.00% |
| 4 | BEAT | +129.30% | bitget | -22.01% | okx | -151.31% |
| 5 | TON | +123.13% | bitget | +5.47% | okx | -117.66% |
| 6 | ALGO | +75.76% | bitget | +10.95% | okx | -64.81% |
| 7 | PROS | +65.04% | bitget | +70.52% | okx | +5.47% |
| 8 | RAVE | +54.23% | okx | +59.71% | bitget | +5.47% |
| 9 | SKHYNIX | +51.66% | okx | +51.66% | bitget | +0.00% |
| 10 | CHZ | +44.34% | bitget | +10.29% | okx | -34.04% |
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
