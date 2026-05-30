# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-05-30 17:34 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **909**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | DELL | okx | +272.81% |
| 2 | ARM | okx | +154.77% |
| 3 | ESPORTS | bitget | +128.22% |
| 4 | SHLD | okx | +124.81% |
| 5 | ASTS | bitget | +109.50% |
| 6 | RDDT | bitget | +109.50% |
| 7 | AVGO | bitget | +109.50% |
| 8 | AAOI | bitget | +109.50% |
| 9 | RDW | bitget | +109.50% |
| 10 | EWY | bitget | +109.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | VTHO | bitget | -366.93% |
| 2 | PRL | bitget | -289.52% |
| 3 | NATGAS | bitget | -186.48% |
| 4 | ID | bitget | -165.45% |
| 5 | LAB | okx | -151.98% |
| 6 | FLY | bitget | -109.50% |
| 7 | CBRS | bitget | -109.50% |
| 8 | STXSTOCK | bitget | -109.50% |
| 9 | PROS | bitget | -107.64% |
| 10 | CRCL | bitget | -105.34% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | DELL | +163.31% | okx | +272.81% | bitget | +109.50% |
| 2 | CBRS | +120.45% | okx | +10.95% | bitget | -109.50% |
| 3 | PROS | +113.11% | okx | +5.47% | bitget | -107.64% |
| 4 | HOOD | +109.50% | bitget | +109.50% | okx | +0.00% |
| 5 | CRWV | +106.22% | bitget | +109.50% | okx | +3.28% |
| 6 | EWY | +105.81% | bitget | +109.50% | okx | +3.69% |
| 7 | CRCL | +105.34% | okx | +0.00% | bitget | -105.34% |
| 8 | PLTR | +103.37% | bitget | +103.37% | okx | +0.00% |
| 9 | NVDA | +102.41% | bitget | +109.50% | okx | +7.09% |
| 10 | NBIS | +98.55% | bitget | +109.50% | okx | +10.95% |
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
