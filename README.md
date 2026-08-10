# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-10 02:39 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1164**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TUT | bitget | +502.93% |
| 2 | 龙虾 | bitget | +463.19% |
| 3 | SKHYNIX | okx | +205.25% |
| 4 | UNITAS | bitget | +193.27% |
| 5 | SKHYNIX | bitget | +188.89% |
| 6 | US | bitget | +180.02% |
| 7 | SIREN | bitget | +170.27% |
| 8 | ZEST | bitget | +161.40% |
| 9 | SHOP | okx | +145.45% |
| 10 | ELSA | bitget | +128.55% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KAITO | bitget | -475.78% |
| 2 | BICO | okx | -299.36% |
| 3 | KAITO | okx | -183.17% |
| 4 | ON | okx | -144.54% |
| 5 | ZBT | bitget | -124.72% |
| 6 | RE | okx | -121.49% |
| 7 | ZBT | okx | -120.36% |
| 8 | DEXE | bitget | -117.71% |
| 9 | RE | bitget | -84.42% |
| 10 | KORU | bitget | -81.36% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BICO | +330.46% | bitget | +31.10% | okx | -299.36% |
| 2 | KAITO | +292.61% | okx | -183.17% | bitget | -475.78% |
| 3 | SHOP | +145.45% | okx | +145.45% | bitget | +0.00% |
| 4 | BRKB | +85.93% | okx | +85.93% | bitget | +0.00% |
| 5 | KORU | +81.36% | okx | +0.00% | bitget | -81.36% |
| 6 | FWDI | +73.20% | bitget | +50.70% | okx | -22.50% |
| 7 | SNOW | +71.45% | bitget | +0.00% | okx | -71.45% |
| 8 | USELESS | +51.00% | bitget | +61.98% | okx | +10.98% |
| 9 | MINIMAX | +49.14% | okx | +49.14% | bitget | +0.00% |
| 10 | BAND | +45.80% | bitget | -2.85% | okx | -48.65% |
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
