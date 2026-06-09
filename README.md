# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-09 18:29 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **967**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 龙虾 | bitget | +131.51% |
| 2 | EPIC | bitget | +121.55% |
| 3 | NG | okx | +111.26% |
| 4 | GWEI | bitget | +76.43% |
| 5 | MRVL | okx | +71.07% |
| 6 | FOLKS | bitget | +68.99% |
| 7 | GLW | okx | +68.52% |
| 8 | SOXL | okx | +63.39% |
| 9 | ARIA | bitget | +59.46% |
| 10 | RAVE | okx | +55.12% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SENT | bitget | -1328.78% |
| 2 | H | okx | -1095.00% |
| 3 | SENT | okx | -1095.00% |
| 4 | HOME | okx | -398.30% |
| 5 | SAHARA | okx | -378.88% |
| 6 | ESPORTS | bitget | -230.28% |
| 7 | SAHARA | bitget | -218.78% |
| 8 | STABLE | bitget | -197.87% |
| 9 | SIREN | bitget | -197.54% |
| 10 | STABLE | okx | -169.53% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +1096.42% | bitget | +1.42% | okx | -1095.00% |
| 2 | HOME | +235.59% | bitget | -162.72% | okx | -398.30% |
| 3 | SENT | +233.78% | okx | -1095.00% | bitget | -1328.78% |
| 4 | SAHARA | +160.09% | bitget | -218.78% | okx | -378.88% |
| 5 | MRVL | +71.07% | okx | +71.07% | bitget | +0.00% |
| 6 | ZEC | +63.20% | bitget | -30.99% | okx | -94.19% |
| 7 | SOXL | +61.97% | okx | +63.39% | bitget | +1.42% |
| 8 | LAYER | +51.71% | okx | -92.39% | bitget | -144.10% |
| 9 | RAVE | +49.64% | okx | +55.12% | bitget | +5.47% |
| 10 | CRCL | +46.47% | okx | +46.47% | bitget | +0.00% |
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
