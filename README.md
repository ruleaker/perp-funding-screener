# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-26 17:32 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MAGMA | bitget | +188.67% |
| 2 | KIOXIA | okx | +113.90% |
| 3 | NOK | okx | +72.56% |
| 4 | XVG | bitget | +71.61% |
| 5 | 龙虾 | bitget | +69.64% |
| 6 | GEV | okx | +64.80% |
| 7 | 1MCHEEMS | bitget | +63.84% |
| 8 | FIGHT | bitget | +56.17% |
| 9 | ARIA | bitget | +49.93% |
| 10 | M | bitget | +45.00% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | VANRY | bitget | -1111.42% |
| 2 | EUL | bitget | -676.16% |
| 3 | ESP | bitget | -611.12% |
| 4 | TLM | bitget | -404.49% |
| 5 | DEXE | bitget | -368.47% |
| 6 | T | bitget | -215.06% |
| 7 | HOT | bitget | -204.87% |
| 8 | ESP | okx | -202.27% |
| 9 | BARD | okx | -189.29% |
| 10 | BARD | bitget | -180.13% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ESP | +408.85% | okx | -202.27% | bitget | -611.12% |
| 2 | KIOXIA | +113.90% | okx | +113.90% | bitget | +0.00% |
| 3 | ZIL | +66.79% | okx | +5.47% | bitget | -61.32% |
| 4 | GEV | +64.80% | okx | +64.80% | bitget | +0.00% |
| 5 | MINA | +43.13% | okx | -10.85% | bitget | -53.98% |
| 6 | ONE | +40.92% | okx | +4.46% | bitget | -36.46% |
| 7 | VANA | +40.62% | okx | +5.47% | bitget | -35.15% |
| 8 | APR | +35.59% | okx | +5.47% | bitget | -30.11% |
| 9 | LQTY | +33.80% | bitget | +10.95% | okx | -22.85% |
| 10 | TSM | +30.35% | okx | +30.35% | bitget | +0.00% |
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
