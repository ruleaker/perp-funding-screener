# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-20 18:27 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1125**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BANK | bitget | +105.78% |
| 2 | FIGHT | bitget | +88.80% |
| 3 | AMC | bitget | +77.96% |
| 4 | MINIMAX | okx | +73.19% |
| 5 | INX | bitget | +70.41% |
| 6 | TSM | bitget | +58.14% |
| 7 | XPD | bitget | +49.06% |
| 8 | GLW | bitget | +48.51% |
| 9 | 龙虾 | bitget | +45.99% |
| 10 | SIREN | bitget | +45.22% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -506.98% |
| 2 | OUST | bitget | -440.74% |
| 3 | OSS | bitget | -321.71% |
| 4 | AEHR | bitget | -250.10% |
| 5 | SOXS | bitget | -241.67% |
| 6 | RE | okx | -158.57% |
| 7 | RE | bitget | -141.91% |
| 8 | HOME | bitget | -137.31% |
| 9 | PL | bitget | -126.58% |
| 10 | VANRY | bitget | -114.43% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SOXS | +241.67% | okx | +0.00% | bitget | -241.67% |
| 2 | SKHYNIX | +98.76% | bitget | +0.00% | okx | -98.76% |
| 3 | MINIMAX | +73.19% | okx | +73.19% | bitget | +0.00% |
| 4 | GALA | +55.52% | okx | +10.95% | bitget | -44.57% |
| 5 | GLW | +48.51% | bitget | +48.51% | okx | +0.00% |
| 6 | TSM | +45.91% | bitget | +58.14% | okx | +12.23% |
| 7 | HOME | +43.31% | okx | -94.00% | bitget | -137.31% |
| 8 | SPCX | +39.97% | bitget | +39.97% | okx | +0.00% |
| 9 | INJ | +37.99% | okx | -6.91% | bitget | -44.90% |
| 10 | XTZ | +36.14% | okx | +10.95% | bitget | -25.19% |
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
