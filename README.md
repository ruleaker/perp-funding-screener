# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-16 17:45 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1114**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | XPD | okx | +128.06% |
| 2 | KORU | okx | +117.03% |
| 3 | 龙虾 | bitget | +105.01% |
| 4 | SNXX | okx | +94.00% |
| 5 | SNDK | bitget | +85.30% |
| 6 | XPD | bitget | +82.12% |
| 7 | KORU | bitget | +78.73% |
| 8 | SOXL | bitget | +76.43% |
| 9 | US | bitget | +76.32% |
| 10 | SPCX | bitget | +69.75% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -569.84% |
| 2 | DISK | bitget | -541.48% |
| 3 | HOME | okx | -514.03% |
| 4 | BONK | okx | -510.34% |
| 5 | MANTRA | bitget | -448.07% |
| 6 | 1000BONK | bitget | -336.49% |
| 7 | TLM | bitget | -139.17% |
| 8 | VANRY | bitget | -137.31% |
| 9 | SAMSUNG | okx | -137.26% |
| 10 | SKHYNIX | okx | -136.89% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SAMSUNG | +137.26% | bitget | +0.00% | okx | -137.26% |
| 2 | SKHYNIX | +136.89% | bitget | +0.00% | okx | -136.89% |
| 3 | BSP | +114.87% | okx | +0.00% | bitget | -114.87% |
| 4 | SNXX | +79.33% | okx | +94.00% | bitget | +14.67% |
| 5 | RAM | +66.76% | okx | +66.76% | bitget | +0.00% |
| 6 | TQQQ | +66.24% | okx | +66.24% | bitget | +0.00% |
| 7 | ALGO | +65.93% | bitget | +10.95% | okx | -54.98% |
| 8 | RAVE | +60.48% | okx | +65.95% | bitget | +5.47% |
| 9 | BAND | +59.90% | bitget | +10.95% | okx | -48.95% |
| 10 | HOME | +55.81% | okx | -514.03% | bitget | -569.84% |
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
