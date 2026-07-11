# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-11 17:28 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1102**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SIREN | bitget | +96.25% |
| 2 | LAB | okx | +89.51% |
| 3 | 龙虾 | bitget | +74.24% |
| 4 | BTW | bitget | +54.97% |
| 5 | LAB | bitget | +53.76% |
| 6 | TRUTH | okx | +46.05% |
| 7 | 1000RATS | bitget | +44.13% |
| 8 | TUT | bitget | +43.03% |
| 9 | FIGHT | bitget | +38.87% |
| 10 | M | bitget | +33.95% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SXT | bitget | -627.65% |
| 2 | T | bitget | -597.87% |
| 3 | PARTI | okx | -428.68% |
| 4 | ANKR | bitget | -240.79% |
| 5 | HOT | bitget | -219.11% |
| 6 | PARTI | bitget | -175.64% |
| 7 | VANRY | bitget | -140.49% |
| 8 | DATA | bitget | -110.70% |
| 9 | UMA | okx | -108.94% |
| 10 | TLM | bitget | -108.30% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | PARTI | +253.04% | bitget | -175.64% | okx | -428.68% |
| 2 | UMA | +81.13% | bitget | -27.81% | okx | -108.94% |
| 3 | KAT | +56.18% | okx | -44.99% | bitget | -101.18% |
| 4 | PI | +54.14% | bitget | +5.47% | okx | -48.67% |
| 5 | BAT | +50.83% | okx | +2.98% | bitget | -47.85% |
| 6 | THETA | +49.50% | bitget | -38.32% | okx | -87.82% |
| 7 | IOTA | +39.49% | bitget | -3.07% | okx | -42.56% |
| 8 | BAND | +37.77% | bitget | +10.95% | okx | -26.82% |
| 9 | LAB | +35.75% | okx | +89.51% | bitget | +53.76% |
| 10 | SUSHI | +32.41% | okx | +10.95% | bitget | -21.46% |
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
