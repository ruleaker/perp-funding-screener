# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-09 13:03 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1247**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +417.43% |
| 2 | BOT | okx | +286.61% |
| 3 | GTLB | bitget | +259.30% |
| 4 | GPRO | okx | +251.61% |
| 5 | ZS | bitget | +237.18% |
| 6 | NATGAS | bitget | +185.16% |
| 7 | GPRO | bitget | +171.59% |
| 8 | ROK | okx | +161.27% |
| 9 | TEAM | bitget | +108.08% |
| 10 | IONQ | okx | +95.64% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AKE | bitget | -219.22% |
| 2 | BZ | okx | -203.11% |
| 3 | BZ | bitget | -199.07% |
| 4 | CL | bitget | -178.70% |
| 5 | CL | okx | -168.63% |
| 6 | USO | okx | -156.77% |
| 7 | FWDI | okx | -131.82% |
| 8 | IOST | okx | -110.56% |
| 9 | ACE | bitget | -110.05% |
| 10 | RAY | okx | -106.36% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BOT | +286.61% | okx | +286.61% | bitget | +0.00% |
| 2 | ROK | +161.27% | okx | +161.27% | bitget | +0.00% |
| 3 | FWDI | +131.82% | bitget | +0.00% | okx | -131.82% |
| 4 | RAY | +111.84% | bitget | +5.47% | okx | -106.36% |
| 5 | ZIL | +110.31% | bitget | +5.47% | okx | -104.84% |
| 6 | IOST | +108.48% | bitget | -2.08% | okx | -110.56% |
| 7 | SOPH | +97.75% | bitget | -6.68% | okx | -104.43% |
| 8 | GPRO | +80.02% | okx | +251.61% | bitget | +171.59% |
| 9 | CRDO | +63.23% | okx | +69.25% | bitget | +6.02% |
| 10 | SHAZ | +61.10% | bitget | +0.00% | okx | -61.10% |
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
