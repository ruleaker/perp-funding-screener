# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-02 10:13 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1154**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOXL | okx | +172.77% |
| 2 | ISRG | okx | +94.36% |
| 3 | 1MCHEEMS | bitget | +89.35% |
| 4 | 龙虾 | bitget | +72.93% |
| 5 | H | bitget | +67.12% |
| 6 | UNITAS | bitget | +59.35% |
| 7 | EPIC | bitget | +58.47% |
| 8 | FF | bitget | +43.03% |
| 9 | US | bitget | +39.20% |
| 10 | COTI | bitget | +38.54% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HYPER | bitget | -1121.39% |
| 2 | EUL | bitget | -557.14% |
| 3 | SYN | bitget | -283.60% |
| 4 | LA | okx | -227.74% |
| 5 | LA | bitget | -210.79% |
| 6 | VANRY | bitget | -130.20% |
| 7 | DEXE | bitget | -116.95% |
| 8 | ZIL | okx | -113.08% |
| 9 | VANA | bitget | -106.32% |
| 10 | MANTRA | bitget | -102.71% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SOXL | +172.77% | okx | +172.77% | bitget | +0.00% |
| 2 | ISRG | +94.36% | okx | +94.36% | bitget | +0.00% |
| 3 | GRVT | +82.98% | bitget | +5.47% | okx | -77.50% |
| 4 | HOME | +79.06% | bitget | -19.71% | okx | -98.77% |
| 5 | ZIL | +55.05% | bitget | -58.04% | okx | -113.08% |
| 6 | SOXS | +54.04% | bitget | -7.01% | okx | -61.05% |
| 7 | IOST | +52.36% | bitget | -25.19% | okx | -77.55% |
| 8 | RAY | +50.53% | bitget | +5.47% | okx | -45.06% |
| 9 | H | +42.30% | bitget | +67.12% | okx | +24.82% |
| 10 | CFX | +40.92% | okx | -19.19% | bitget | -60.12% |
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
