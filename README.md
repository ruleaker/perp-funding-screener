# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-01 19:27 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1212**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GEV | okx | +121.80% |
| 2 | QNT | okx | +114.24% |
| 3 | M | bitget | +99.86% |
| 4 | XPD | okx | +85.43% |
| 5 | JCT | bitget | +75.12% |
| 6 | SIREN | bitget | +74.79% |
| 7 | 牛来 | bitget | +65.04% |
| 8 | NOK | okx | +64.80% |
| 9 | NG | okx | +60.65% |
| 10 | XAU | okx | +52.29% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -642.00% |
| 2 | TRX | okx | -245.52% |
| 3 | TRX | bitget | -239.70% |
| 4 | ZHIPU | okx | -181.45% |
| 5 | ONG | bitget | -153.41% |
| 6 | ONT | bitget | -117.06% |
| 7 | ZHIPU | bitget | -115.74% |
| 8 | RVN | okx | -110.03% |
| 9 | SAMSUNG | okx | -106.37% |
| 10 | ONT | okx | -101.56% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | GEV | +121.80% | okx | +121.80% | bitget | +0.00% |
| 2 | SAMSUNG | +106.37% | bitget | +0.00% | okx | -106.37% |
| 3 | QNT | +103.29% | okx | +114.24% | bitget | +10.95% |
| 4 | UNITREE | +98.44% | bitget | +0.00% | okx | -98.44% |
| 5 | ZHIPU | +65.71% | bitget | -115.74% | okx | -181.45% |
| 6 | SAND | +63.88% | bitget | -5.91% | okx | -69.80% |
| 7 | XPD | +56.63% | okx | +85.43% | bitget | +28.80% |
| 8 | SHOP | +48.32% | okx | +48.32% | bitget | +0.00% |
| 9 | MINA | +48.20% | okx | -4.91% | bitget | -53.11% |
| 10 | RDDT | +43.76% | okx | +43.76% | bitget | +0.00% |
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
