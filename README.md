# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-27 11:48 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1137**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FLY | bitget | +530.75% |
| 2 | FWDI | bitget | +482.24% |
| 3 | SPIR | bitget | +481.47% |
| 4 | RDDT | bitget | +273.86% |
| 5 | FWDI | okx | +178.32% |
| 6 | NTAP | bitget | +170.82% |
| 7 | 龙虾 | bitget | +157.90% |
| 8 | BSP | okx | +108.22% |
| 9 | BMNR | okx | +100.45% |
| 10 | GEV | okx | +89.83% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AEON | okx | -826.38% |
| 2 | NIL | bitget | -544.54% |
| 3 | TLM | bitget | -493.08% |
| 4 | VANRY | bitget | -467.78% |
| 5 | BUD | bitget | -439.20% |
| 6 | EUL | bitget | -214.62% |
| 7 | DEXE | bitget | -176.40% |
| 8 | T | bitget | -152.64% |
| 9 | HOT | bitget | -143.12% |
| 10 | MIRA | bitget | -139.61% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | FLY | +449.11% | bitget | +530.75% | okx | +81.63% |
| 2 | FWDI | +303.92% | bitget | +482.24% | okx | +178.32% |
| 3 | RDDT | +273.86% | bitget | +273.86% | okx | +0.00% |
| 4 | RAY | +115.76% | bitget | +5.47% | okx | -110.28% |
| 5 | BSP | +108.22% | okx | +108.22% | bitget | +0.00% |
| 6 | BMNR | +100.45% | okx | +100.45% | bitget | +0.00% |
| 7 | GEV | +89.83% | okx | +89.83% | bitget | +0.00% |
| 8 | KIOXIA | +73.55% | bitget | +0.00% | okx | -73.55% |
| 9 | TER | +52.38% | okx | +52.38% | bitget | +0.00% |
| 10 | ESP | +48.26% | bitget | -72.16% | okx | -120.42% |
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
