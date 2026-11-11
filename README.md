# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-11 06:52 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1412**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +1095.00% |
| 2 | LGENERGY | bitget | +649.66% |
| 3 | NAVER | bitget | +531.08% |
| 4 | WUXIBIO | okx | +447.59% |
| 5 | 哈基米 | bitget | +425.74% |
| 6 | LGELECTRONICS | bitget | +368.03% |
| 7 | LYTE | bitget | +348.98% |
| 8 | NG | okx | +284.97% |
| 9 | RAM | bitget | +278.35% |
| 10 | SKUU | bitget | +276.16% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | INIT | bitget | -1173.40% |
| 2 | UNITREE | okx | -1095.00% |
| 3 | AVAV | bitget | -1095.00% |
| 4 | TSEM | bitget | -1095.00% |
| 5 | INIT | okx | -968.42% |
| 6 | AEHR | bitget | -950.90% |
| 7 | POET | bitget | -835.27% |
| 8 | TSEM | okx | -817.47% |
| 9 | UNITREE | bitget | -764.75% |
| 10 | HANMI | okx | -734.76% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1089.53% | okx | +1095.00% | bitget | +5.47% |
| 2 | NAVER | +531.08% | bitget | +531.08% | okx | +0.00% |
| 3 | POET | +509.41% | okx | -325.86% | bitget | -835.27% |
| 4 | HANMI | +488.06% | bitget | -246.70% | okx | -734.76% |
| 5 | SKDD | +376.79% | okx | +0.00% | bitget | -376.79% |
| 6 | LGELECTRONICS | +368.03% | bitget | +368.03% | okx | +0.00% |
| 7 | AEHR | +366.04% | okx | -584.85% | bitget | -950.90% |
| 8 | LYTE | +348.98% | bitget | +348.98% | okx | +0.00% |
| 9 | UNITREE | +330.25% | bitget | -764.75% | okx | -1095.00% |
| 10 | RAM | +278.35% | bitget | +278.35% | okx | +0.00% |
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
