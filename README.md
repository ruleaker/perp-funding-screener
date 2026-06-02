# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-02 05:08 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **928**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AAOI | okx | +593.45% |
| 2 | GEV | okx | +498.69% |
| 3 | MRVL | okx | +480.45% |
| 4 | COHR | okx | +414.76% |
| 5 | VRT | okx | +403.43% |
| 6 | RDW | okx | +396.60% |
| 7 | DELL | okx | +277.90% |
| 8 | WDC | okx | +228.86% |
| 9 | NOK | okx | +209.68% |
| 10 | CRWD | okx | +189.57% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SLX | bitget | -693.90% |
| 2 | LAB | okx | -486.66% |
| 3 | LAB | bitget | -413.25% |
| 4 | SLX | okx | -315.80% |
| 5 | HOME | bitget | -243.86% |
| 6 | ZEC | bitget | -203.12% |
| 7 | GUN | bitget | -181.99% |
| 8 | DRIFT | bitget | -152.64% |
| 9 | IRYS | okx | -151.90% |
| 10 | IRYS | bitget | -144.32% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | AAOI | +483.95% | okx | +593.45% | bitget | +109.50% |
| 2 | VRT | +403.43% | okx | +403.43% | bitget | +0.00% |
| 3 | DELL | +387.40% | okx | +277.90% | bitget | -109.50% |
| 4 | SLX | +378.11% | okx | -315.80% | bitget | -693.90% |
| 5 | MRVL | +370.95% | okx | +480.45% | bitget | +109.50% |
| 6 | COHR | +305.26% | okx | +414.76% | bitget | +109.50% |
| 7 | RDW | +287.10% | okx | +396.60% | bitget | +109.50% |
| 8 | INFQ | +240.01% | okx | +130.51% | bitget | -109.50% |
| 9 | WDC | +228.86% | okx | +228.86% | bitget | +0.00% |
| 10 | ZEC | +214.07% | okx | +10.95% | bitget | -203.12% |
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
