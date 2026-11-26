# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-26 08:41 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1436**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BYD | bitget | +154.50% |
| 2 | KR200 | okx | +104.11% |
| 3 | INIT | okx | +100.22% |
| 4 | BIDU | okx | +97.25% |
| 5 | SKDD | bitget | +90.78% |
| 6 | CSOPSS2LHKD | bitget | +84.75% |
| 7 | KUAISHOU | bitget | +79.61% |
| 8 | MEITUAN | okx | +73.73% |
| 9 | CSOPSAMSUNG2L | okx | +62.63% |
| 10 | GIGADEVICE | bitget | +53.33% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MOVE | okx | -985.41% |
| 2 | MOVE | bitget | -983.75% |
| 3 | H100 | okx | -697.67% |
| 4 | MANTRA | bitget | -631.05% |
| 5 | LAYER | okx | -493.24% |
| 6 | LAYER | bitget | -458.59% |
| 7 | BABY | okx | -426.41% |
| 8 | ME | okx | -423.18% |
| 9 | ME | bitget | -417.96% |
| 10 | BABY | bitget | -392.56% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +703.14% | bitget | +5.47% | okx | -697.67% |
| 2 | SKHYNIX | +279.15% | bitget | -62.09% | okx | -341.24% |
| 3 | SLX | +142.44% | bitget | -241.34% | okx | -383.78% |
| 4 | DOS | +134.06% | bitget | -27.48% | okx | -161.54% |
| 5 | INIT | +120.59% | okx | +100.22% | bitget | -20.37% |
| 6 | ANIME | +112.59% | bitget | -146.40% | okx | -258.99% |
| 7 | KR200 | +93.60% | okx | +104.11% | bitget | +10.51% |
| 8 | SNXX | +90.11% | okx | -6.80% | bitget | -96.91% |
| 9 | RAM | +87.82% | okx | +0.00% | bitget | -87.82% |
| 10 | UNITREE | +85.79% | bitget | -38.43% | okx | -124.23% |
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
