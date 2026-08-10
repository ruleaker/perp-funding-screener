# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-10 09:55 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1167**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 龙虾 | bitget | +560.53% |
| 2 | BICO | bitget | +244.84% |
| 3 | BOT | okx | +183.06% |
| 4 | TUT | bitget | +178.70% |
| 5 | KOPN | bitget | +144.76% |
| 6 | SIREN | bitget | +143.34% |
| 7 | SKHYNIX | okx | +141.33% |
| 8 | SOON | bitget | +133.81% |
| 9 | ARQQ | bitget | +128.01% |
| 10 | BSP | okx | +120.90% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KAITO | bitget | -1251.48% |
| 2 | KAITO | okx | -604.54% |
| 3 | FWDI | bitget | -323.57% |
| 4 | BICO | okx | -133.70% |
| 5 | DEXE | bitget | -104.57% |
| 6 | RE | okx | -91.43% |
| 7 | ZIL | okx | -88.18% |
| 8 | COTI | bitget | -84.75% |
| 9 | BZ | bitget | -82.45% |
| 10 | ESP | okx | -81.15% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KAITO | +646.93% | okx | -604.54% | bitget | -1251.48% |
| 2 | BICO | +378.54% | bitget | +244.84% | okx | -133.70% |
| 3 | FWDI | +323.57% | okx | +0.00% | bitget | -323.57% |
| 4 | SKHYNIX | +141.33% | okx | +141.33% | bitget | +0.00% |
| 5 | BOT | +136.96% | okx | +183.06% | bitget | +46.10% |
| 6 | SOON | +128.33% | bitget | +133.81% | okx | +5.47% |
| 7 | BSP | +120.90% | okx | +120.90% | bitget | +0.00% |
| 8 | SKUU | +118.47% | okx | +118.47% | bitget | +0.00% |
| 9 | KIOXIA | +67.05% | okx | +67.05% | bitget | +0.00% |
| 10 | ZIL | +66.72% | bitget | -21.46% | okx | -88.18% |
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
