# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-18 13:03 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1257**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MCD | bitget | +111.91% |
| 2 | OSS | bitget | +89.57% |
| 3 | 哈基米 | bitget | +76.98% |
| 4 | AAOI | okx | +76.69% |
| 5 | ZBT | okx | +74.22% |
| 6 | BRKB | okx | +73.05% |
| 7 | GPRO | okx | +72.83% |
| 8 | SHEINHKD | bitget | +69.86% |
| 9 | EVEX | bitget | +63.40% |
| 10 | NG | okx | +62.54% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AVA | bitget | -729.60% |
| 2 | ETN | bitget | -414.13% |
| 3 | ZHIPUHKD | bitget | -246.27% |
| 4 | IOST | okx | -243.39% |
| 5 | ZHIPU | bitget | -234.11% |
| 6 | IOST | bitget | -214.07% |
| 7 | ZHIPU | okx | -195.84% |
| 8 | ONE | bitget | -188.67% |
| 9 | LSK | bitget | -188.23% |
| 10 | CSOPSK2LHKD | bitget | -131.18% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | GPRO | +123.75% | okx | +72.83% | bitget | -50.92% |
| 2 | ONE | +112.07% | okx | -76.60% | bitget | -188.67% |
| 3 | ZBT | +68.75% | okx | +74.22% | bitget | +5.47% |
| 4 | UNITREE | +64.00% | bitget | +0.00% | okx | -64.00% |
| 5 | HYUNDAI | +62.20% | okx | +62.20% | bitget | +0.00% |
| 6 | ZM | +57.81% | okx | +57.81% | bitget | +0.00% |
| 7 | EGLD | +50.58% | bitget | -5.58% | okx | -56.16% |
| 8 | SOFTBANK | +42.93% | okx | +42.93% | bitget | +0.00% |
| 9 | ROK | +42.84% | bitget | +0.00% | okx | -42.84% |
| 10 | ZHIPU | +38.27% | okx | -195.84% | bitget | -234.11% |
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
