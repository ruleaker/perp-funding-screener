# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-27 00:42 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1436**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | EWZS | bitget | +109.28% |
| 2 | TLT | okx | +107.48% |
| 3 | H100 | okx | +96.82% |
| 4 | EWZ | bitget | +94.17% |
| 5 | EWZ | okx | +79.51% |
| 6 | UP | okx | +75.54% |
| 7 | SKDD | bitget | +57.93% |
| 8 | KR200 | bitget | +53.76% |
| 9 | GRVT | okx | +52.03% |
| 10 | UMC | okx | +51.27% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ME | okx | -733.17% |
| 2 | MOVE | bitget | -524.83% |
| 3 | MOVE | okx | -498.89% |
| 4 | ONE | okx | -402.19% |
| 5 | ONE | bitget | -392.23% |
| 6 | ME | bitget | -373.94% |
| 7 | SKHYNIX | okx | -234.66% |
| 8 | MANTRA | bitget | -215.28% |
| 9 | BIGTIME | bitget | -179.03% |
| 10 | SLX | okx | -172.97% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ME | +359.23% | bitget | -373.94% | okx | -733.17% |
| 2 | SKHYNIX | +234.66% | bitget | +0.00% | okx | -234.66% |
| 3 | SKHY | +151.19% | bitget | -8.76% | okx | -159.95% |
| 4 | EWZS | +109.28% | bitget | +109.28% | okx | +0.00% |
| 5 | TLT | +107.48% | okx | +107.48% | bitget | +0.00% |
| 6 | HYUNDAI | +93.44% | bitget | +0.00% | okx | -93.44% |
| 7 | H100 | +91.35% | okx | +96.82% | bitget | +5.47% |
| 8 | SSV | +72.37% | okx | -66.80% | bitget | -139.17% |
| 9 | INIT | +69.53% | okx | +5.47% | bitget | -64.06% |
| 10 | SKDD | +54.18% | bitget | +57.93% | okx | +3.75% |
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
