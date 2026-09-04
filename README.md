# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-04 04:50 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1230**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | okx | +182.18% |
| 2 | AMC | bitget | +154.94% |
| 3 | ZHIPU | okx | +141.38% |
| 4 | ONE | okx | +133.91% |
| 5 | ESPORTS | bitget | +131.84% |
| 6 | BOT | okx | +129.27% |
| 7 | RAM | okx | +120.35% |
| 8 | ZHIPU | bitget | +107.75% |
| 9 | ONE | bitget | +102.60% |
| 10 | IONQ | okx | +94.78% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LA | bitget | -854.32% |
| 2 | HIVE | bitget | -716.35% |
| 3 | LA | okx | -336.64% |
| 4 | CAP | okx | -322.59% |
| 5 | CAP | bitget | -280.21% |
| 6 | ACE | bitget | -234.11% |
| 7 | ONG | bitget | -209.25% |
| 8 | ANKR | bitget | -200.82% |
| 9 | LPT | okx | -196.87% |
| 10 | TUT | bitget | -167.97% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LA | +517.68% | okx | -336.64% | bitget | -854.32% |
| 2 | FWDI | +182.18% | okx | +182.18% | bitget | +0.00% |
| 3 | BOT | +129.27% | okx | +129.27% | bitget | +0.00% |
| 4 | BSP | +124.58% | bitget | +0.00% | okx | -124.58% |
| 5 | RAM | +120.35% | okx | +120.35% | bitget | +0.00% |
| 6 | SKUU | +98.12% | bitget | +0.00% | okx | -98.12% |
| 7 | IONQ | +94.78% | okx | +94.78% | bitget | +0.00% |
| 8 | QNT | +76.25% | okx | +87.20% | bitget | +10.95% |
| 9 | UNITREE | +64.10% | okx | +90.17% | bitget | +26.06% |
| 10 | CIEN | +62.28% | okx | +62.28% | bitget | +0.00% |
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
