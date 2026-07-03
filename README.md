# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-03 17:55 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1078**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +94.72% |
| 2 | MSTR | okx | +77.87% |
| 3 | RDW | okx | +54.10% |
| 4 | SIREN | bitget | +51.03% |
| 5 | CRWV | okx | +47.87% |
| 6 | BSB | okx | +46.33% |
| 7 | ORCL | okx | +44.30% |
| 8 | PIPPIN | bitget | +38.11% |
| 9 | TER | okx | +35.64% |
| 10 | CAP | okx | +33.66% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ARPA | bitget | -1669.98% |
| 2 | 10000NEX | bitget | -654.26% |
| 3 | ZKP | okx | -554.76% |
| 4 | ZKP | bitget | -521.88% |
| 5 | THE | bitget | -464.39% |
| 6 | PLTR | bitget | -426.06% |
| 7 | SLX | okx | -275.75% |
| 8 | BIRB | bitget | -217.36% |
| 9 | CRWD | okx | -186.57% |
| 10 | SLX | bitget | -160.64% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | PLTR | +426.06% | okx | +0.00% | bitget | -426.06% |
| 2 | MANA | +133.68% | bitget | +10.95% | okx | -122.73% |
| 3 | SLX | +115.11% | bitget | -160.64% | okx | -275.75% |
| 4 | KSM | +114.80% | okx | -8.50% | bitget | -123.30% |
| 5 | PENDLE | +78.62% | okx | +5.47% | bitget | -73.15% |
| 6 | MSTR | +77.87% | okx | +77.87% | bitget | +0.00% |
| 7 | ATOM | +68.65% | okx | +8.75% | bitget | -59.90% |
| 8 | RDW | +54.10% | okx | +54.10% | bitget | +0.00% |
| 9 | CRWV | +47.87% | okx | +47.87% | bitget | +0.00% |
| 10 | ORCL | +44.30% | okx | +44.30% | bitget | +0.00% |
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
