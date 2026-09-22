# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-22 13:31 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1273**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ETN | bitget | +395.40% |
| 2 | NKE | bitget | +282.07% |
| 3 | GPRO | bitget | +169.18% |
| 4 | GPRO | okx | +159.73% |
| 5 | KR200 | okx | +133.75% |
| 6 | UVXY | okx | +115.02% |
| 7 | STG | bitget | +103.04% |
| 8 | BROCCOLI | bitget | +97.78% |
| 9 | HPQ | bitget | +96.25% |
| 10 | MCD | bitget | +92.31% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KERNEL | bitget | -1222.79% |
| 2 | CELR | bitget | -706.49% |
| 3 | COTI | bitget | -374.27% |
| 4 | ONE | okx | -246.46% |
| 5 | BOT | okx | -140.11% |
| 6 | SAMSUNG | okx | -131.36% |
| 7 | SOPH | okx | -131.05% |
| 8 | SOPH | bitget | -116.73% |
| 9 | MINA | bitget | -87.16% |
| 10 | IOST | okx | -79.22% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +251.94% | bitget | +5.47% | okx | -246.46% |
| 2 | BOT | +140.11% | bitget | +0.00% | okx | -140.11% |
| 3 | KR200 | +133.75% | okx | +133.75% | bitget | +0.00% |
| 4 | SAMSUNG | +131.36% | bitget | +0.00% | okx | -131.36% |
| 5 | UVXY | +115.02% | okx | +115.02% | bitget | +0.00% |
| 6 | BB | +64.13% | okx | +69.61% | bitget | +5.47% |
| 7 | MINA | +60.51% | okx | -26.65% | bitget | -87.16% |
| 8 | INTC | +57.62% | bitget | +65.81% | okx | +8.19% |
| 9 | HUT | +54.63% | okx | +54.63% | bitget | +0.00% |
| 10 | SHEIN | +53.49% | okx | +53.49% | bitget | +0.00% |
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
