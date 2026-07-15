# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-15 03:43 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1110**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | WEN | okx | +169.89% |
| 2 | HYUNDAI | okx | +121.41% |
| 3 | BSP | bitget | +118.81% |
| 4 | ESPORTS | bitget | +114.76% |
| 5 | HYUNDAI | bitget | +112.13% |
| 6 | BSP | okx | +73.75% |
| 7 | RKLB | okx | +70.03% |
| 8 | TSM | okx | +66.33% |
| 9 | TUT | bitget | +65.04% |
| 10 | SNDK | okx | +60.09% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MUU | okx | -930.61% |
| 2 | DATA | okx | -818.86% |
| 3 | DATA | bitget | -693.57% |
| 4 | VANA | okx | -352.38% |
| 5 | KORU | okx | -306.12% |
| 6 | VANRY | bitget | -183.74% |
| 7 | VANA | bitget | -175.31% |
| 8 | ZHIPU | bitget | -169.40% |
| 9 | QNT | okx | -159.59% |
| 10 | ZHIPU | okx | -156.17% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | MUU | +930.61% | bitget | +0.00% | okx | -930.61% |
| 2 | KORU | +326.05% | bitget | +19.93% | okx | -306.12% |
| 3 | VANA | +177.07% | bitget | -175.31% | okx | -352.38% |
| 4 | QNT | +170.54% | bitget | +10.95% | okx | -159.59% |
| 5 | WEN | +169.89% | okx | +169.89% | bitget | +0.00% |
| 6 | DATA | +125.29% | bitget | -693.57% | okx | -818.86% |
| 7 | SKHYNIX | +106.48% | bitget | +0.00% | okx | -106.48% |
| 8 | SKHY | +81.20% | bitget | +0.00% | okx | -81.20% |
| 9 | RKLB | +70.03% | okx | +70.03% | bitget | +0.00% |
| 10 | TSM | +66.33% | okx | +66.33% | bitget | +0.00% |
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
