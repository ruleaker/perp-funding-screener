# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-04 06:07 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1298**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CBRS | okx | +138.95% |
| 2 | CBRS | bitget | +111.25% |
| 3 | TSLL | okx | +103.32% |
| 4 | ARIA | bitget | +90.34% |
| 5 | TRIA | okx | +76.43% |
| 6 | PIPPIN | bitget | +74.57% |
| 7 | 哈基米 | bitget | +64.61% |
| 8 | ZBT | okx | +46.54% |
| 9 | AEON | okx | +46.23% |
| 10 | 1000000MOG | bitget | +43.36% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -1034.36% |
| 2 | ONE | bitget | -636.20% |
| 3 | SAND | bitget | -414.90% |
| 4 | SAND | okx | -170.10% |
| 5 | 2Z | okx | -161.49% |
| 6 | 2Z | bitget | -128.66% |
| 7 | ARK | bitget | -100.96% |
| 8 | MANA | okx | -82.86% |
| 9 | POPMART | okx | -68.93% |
| 10 | ESP | okx | -65.70% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1034.36% | bitget | +0.00% | okx | -1034.36% |
| 2 | ONE | +663.32% | okx | +27.12% | bitget | -636.20% |
| 3 | SAND | +244.80% | okx | -170.10% | bitget | -414.90% |
| 4 | TSLL | +103.32% | okx | +103.32% | bitget | +0.00% |
| 5 | ESP | +71.17% | bitget | +5.47% | okx | -65.70% |
| 6 | POPMART | +68.93% | bitget | +0.00% | okx | -68.93% |
| 7 | TRIA | +65.81% | okx | +76.43% | bitget | +10.62% |
| 8 | PIPPIN | +62.06% | bitget | +74.57% | okx | +12.51% |
| 9 | AXS | +59.55% | bitget | +5.47% | okx | -54.08% |
| 10 | MANA | +50.78% | bitget | -32.08% | okx | -82.86% |
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
