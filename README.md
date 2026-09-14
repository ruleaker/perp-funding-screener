# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-14 05:12 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1251**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAMSUNGEM | bitget | +448.29% |
| 2 | HANMI | bitget | +312.07% |
| 3 | ZHIPU | okx | +248.87% |
| 4 | SHEINHKD | bitget | +237.62% |
| 5 | ZHONGJI | okx | +223.78% |
| 6 | SKHYNIX | okx | +223.32% |
| 7 | ZHIPU | bitget | +217.25% |
| 8 | SHEIN | okx | +209.46% |
| 9 | CONL | bitget | +162.72% |
| 10 | NG | okx | +148.57% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | STEEM | bitget | -1885.92% |
| 2 | POWR | bitget | -1003.57% |
| 3 | GLM | bitget | -967.21% |
| 4 | UNITREE | okx | -820.12% |
| 5 | LSK | bitget | -810.41% |
| 6 | BSP | okx | -764.57% |
| 7 | CVC | bitget | -760.26% |
| 8 | PUNDIX | bitget | -734.64% |
| 9 | GLM | okx | -485.09% |
| 10 | UNITREE | bitget | -411.61% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BSP | +764.57% | bitget | +0.00% | okx | -764.57% |
| 2 | GLM | +482.12% | okx | -485.09% | bitget | -967.21% |
| 3 | UNITREE | +408.51% | bitget | -411.61% | okx | -820.12% |
| 4 | APP | +255.08% | bitget | +17.74% | okx | -237.35% |
| 5 | IOST | +233.69% | bitget | -55.52% | okx | -289.20% |
| 6 | AEHR | +161.29% | okx | +0.00% | bitget | -161.29% |
| 7 | KORU | +154.39% | okx | +0.00% | bitget | -154.39% |
| 8 | ZIL | +152.62% | bitget | +5.47% | okx | -147.15% |
| 9 | XIAOMI | +141.59% | okx | +141.59% | bitget | +0.00% |
| 10 | RAM | +133.32% | okx | +56.23% | bitget | -77.09% |
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
