# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-18 09:01 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1194**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RAM | okx | +323.24% |
| 2 | XIAOMI | okx | +110.54% |
| 3 | ZHIPU | okx | +86.39% |
| 4 | 1MCHEEMS | bitget | +77.53% |
| 5 | TOKYOEL | bitget | +75.77% |
| 6 | BSB | okx | +65.06% |
| 7 | ZHIPU | bitget | +62.74% |
| 8 | LIGHT | okx | +62.24% |
| 9 | DOOSBOT | bitget | +54.86% |
| 10 | ESPORTS | bitget | +51.46% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -601.26% |
| 2 | CXMT | bitget | -547.50% |
| 3 | BICO | bitget | -527.79% |
| 4 | RED | bitget | -412.71% |
| 5 | BOT | okx | -275.82% |
| 6 | HOME | okx | -254.48% |
| 7 | HOME | bitget | -226.12% |
| 8 | BICO | okx | -218.83% |
| 9 | EDEN | okx | -208.69% |
| 10 | CXMT | okx | -182.01% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | CXMT | +365.49% | okx | -182.01% | bitget | -547.50% |
| 2 | RAM | +323.24% | okx | +323.24% | bitget | +0.00% |
| 3 | BICO | +308.96% | okx | -218.83% | bitget | -527.79% |
| 4 | BOT | +275.82% | bitget | +0.00% | okx | -275.82% |
| 5 | RVN | +182.87% | bitget | +3.29% | okx | -179.58% |
| 6 | AEHR | +117.60% | bitget | +0.00% | okx | -117.60% |
| 7 | XIAOMI | +110.54% | okx | +110.54% | bitget | +0.00% |
| 8 | KORU | +83.44% | okx | +0.00% | bitget | -83.44% |
| 9 | SAMSUNG | +79.25% | bitget | -42.16% | okx | -121.41% |
| 10 | GPS | +77.28% | bitget | -16.32% | okx | -93.60% |
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
