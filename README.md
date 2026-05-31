# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-05-31 04:58 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **909**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | DELL | okx | +498.48% |
| 2 | ARM | okx | +200.15% |
| 3 | COST | bitget | +109.50% |
| 4 | ASTS | bitget | +109.50% |
| 5 | IONQ | bitget | +109.50% |
| 6 | ASML | bitget | +109.50% |
| 7 | RDDT | bitget | +109.50% |
| 8 | AVGO | bitget | +109.50% |
| 9 | AAOI | bitget | +109.50% |
| 10 | CRCL | bitget | +109.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | PUNDIX | bitget | -1646.00% |
| 2 | HIVE | bitget | -1078.03% |
| 3 | STG | bitget | -621.74% |
| 4 | ID | bitget | -376.13% |
| 5 | LAB | okx | -225.22% |
| 6 | VTHO | bitget | -162.17% |
| 7 | FLY | bitget | -109.50% |
| 8 | STXSTOCK | bitget | -108.51% |
| 9 | OPG | okx | -107.55% |
| 10 | LAB | bitget | -98.99% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | DELL | +388.98% | okx | +498.48% | bitget | +109.50% |
| 2 | LAB | +126.23% | bitget | -98.99% | okx | -225.22% |
| 3 | COST | +109.50% | bitget | +109.50% | okx | +0.00% |
| 4 | PLTR | +109.50% | bitget | +109.50% | okx | +0.00% |
| 5 | COIN | +109.50% | bitget | +109.50% | okx | +0.00% |
| 6 | NVDA | +109.50% | bitget | +109.50% | okx | +0.00% |
| 7 | MSFT | +109.50% | bitget | +109.50% | okx | +0.00% |
| 8 | EWY | +109.12% | bitget | +109.50% | okx | +0.38% |
| 9 | RKLB | +98.55% | bitget | +109.50% | okx | +10.95% |
| 10 | CBRS | +98.55% | bitget | +109.50% | okx | +10.95% |
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
