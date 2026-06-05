# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-05 04:54 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **950**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | INX | bitget | +366.61% |
| 2 | DRIFT | bitget | +193.71% |
| 3 | SAHARA | bitget | +128.99% |
| 4 | APR | bitget | +128.55% |
| 5 | ESPORTS | bitget | +115.74% |
| 6 | QNTSTOCK | bitget | +109.50% |
| 7 | SOXS | bitget | +109.50% |
| 8 | SKHYNIX | bitget | +109.50% |
| 9 | SAMSUNG | bitget | +109.50% |
| 10 | BB | okx | +107.47% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -210.02% |
| 2 | HOME | okx | -174.52% |
| 3 | HPE | okx | -145.09% |
| 4 | IRYS | bitget | -144.98% |
| 5 | TRX | bitget | -123.19% |
| 6 | TRX | okx | -120.25% |
| 7 | ASTS | bitget | -109.50% |
| 8 | IONQ | bitget | -109.50% |
| 9 | RDDT | bitget | -109.50% |
| 10 | AAOI | bitget | -109.50% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | AAOI | +214.56% | okx | +105.06% | bitget | -109.50% |
| 2 | COHR | +120.45% | okx | +10.95% | bitget | -109.50% |
| 3 | NBIS | +120.45% | okx | +10.95% | bitget | -109.50% |
| 4 | SOXL | +120.45% | okx | +10.95% | bitget | -109.50% |
| 5 | INFQ | +120.45% | okx | +10.95% | bitget | -109.50% |
| 6 | ASTS | +120.45% | okx | +10.95% | bitget | -109.50% |
| 7 | EWT | +120.45% | okx | +10.95% | bitget | -109.50% |
| 8 | APR | +117.93% | bitget | +128.55% | okx | +10.62% |
| 9 | BE | +113.77% | okx | +10.95% | bitget | -102.82% |
| 10 | SAHARA | +112.04% | bitget | +128.99% | okx | +16.95% |
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
