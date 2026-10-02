# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-02 14:50 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1298**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AGPU | bitget | +386.86% |
| 2 | SECZ | bitget | +301.67% |
| 3 | BOT | bitget | +283.39% |
| 4 | ROK | okx | +147.60% |
| 5 | SECZ | okx | +144.74% |
| 6 | SAMSUNG | okx | +123.11% |
| 7 | TWST | bitget | +119.14% |
| 8 | 龙虾 | bitget | +107.09% |
| 9 | ZEST | bitget | +101.40% |
| 10 | OKLO | okx | +99.02% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAND | bitget | -1445.40% |
| 2 | SAND | okx | -1095.00% |
| 3 | H100 | okx | -1095.00% |
| 4 | BLSH | bitget | -1023.28% |
| 5 | MANA | okx | -656.62% |
| 6 | MANA | bitget | -565.46% |
| 7 | KOPN | bitget | -358.17% |
| 8 | ARK | bitget | -300.58% |
| 9 | NKE | bitget | -268.82% |
| 10 | BSP | bitget | -185.49% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1095.00% | bitget | +0.00% | okx | -1095.00% |
| 2 | SAND | +350.40% | okx | -1095.00% | bitget | -1445.40% |
| 3 | BOT | +283.39% | bitget | +283.39% | okx | +0.00% |
| 4 | NKE | +282.74% | okx | +13.92% | bitget | -268.82% |
| 5 | SECZ | +156.93% | bitget | +301.67% | okx | +144.74% |
| 6 | BSP | +148.99% | okx | -36.50% | bitget | -185.49% |
| 7 | ROK | +147.60% | okx | +147.60% | bitget | +0.00% |
| 8 | GPRO | +120.89% | okx | +0.00% | bitget | -120.89% |
| 9 | SHEIN | +98.31% | okx | +98.31% | bitget | +0.00% |
| 10 | SAMSUNG | +93.99% | okx | +123.11% | bitget | +29.13% |
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
