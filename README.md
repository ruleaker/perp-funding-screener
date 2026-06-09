# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-09 11:37 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **967**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CRWD | okx | +132.61% |
| 2 | 龙虾 | bitget | +128.12% |
| 3 | GLW | okx | +110.80% |
| 4 | EWT | okx | +90.13% |
| 5 | HIMS | okx | +87.23% |
| 6 | FOLKS | bitget | +82.02% |
| 7 | POWER | bitget | +80.26% |
| 8 | ORCL | okx | +74.82% |
| 9 | LAB | bitget | +74.02% |
| 10 | MRVL | okx | +69.93% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H | okx | -1095.00% |
| 2 | MOVE | bitget | -402.74% |
| 3 | SAHARA | okx | -373.71% |
| 4 | CTR | bitget | -254.26% |
| 5 | MOVE | okx | -227.42% |
| 6 | ESPORTS | bitget | -156.37% |
| 7 | HOME | bitget | -146.51% |
| 8 | SAHARA | bitget | -135.45% |
| 9 | SIREN | bitget | -133.37% |
| 10 | HOME | okx | -124.43% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +1096.42% | bitget | +1.42% | okx | -1095.00% |
| 2 | SAHARA | +238.26% | bitget | -135.45% | okx | -373.71% |
| 3 | MOVE | +175.32% | okx | -227.42% | bitget | -402.74% |
| 4 | CRWD | +132.61% | okx | +132.61% | bitget | +0.00% |
| 5 | EWT | +90.13% | okx | +90.13% | bitget | +0.00% |
| 6 | ORCL | +74.82% | okx | +74.82% | bitget | +0.00% |
| 7 | MRVL | +69.93% | okx | +69.93% | bitget | +0.00% |
| 8 | BSB | +60.13% | okx | +65.61% | bitget | +5.47% |
| 9 | LAYER | +56.63% | okx | -46.41% | bitget | -103.04% |
| 10 | LAB | +53.94% | bitget | +74.02% | okx | +20.09% |
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
