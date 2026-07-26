# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-26 04:04 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 1MCHEEMS | bitget | +133.70% |
| 2 | SOXL | okx | +108.75% |
| 3 | NOK | okx | +100.68% |
| 4 | LYN | bitget | +88.15% |
| 5 | CRCL | okx | +83.83% |
| 6 | SKHY | okx | +74.89% |
| 7 | AIN | bitget | +67.89% |
| 8 | SNXX | okx | +67.60% |
| 9 | 龙虾 | bitget | +50.26% |
| 10 | ARIA | bitget | +45.66% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | EUL | bitget | -1274.91% |
| 2 | TLM | bitget | -358.83% |
| 3 | DEXE | bitget | -309.99% |
| 4 | SPELL | bitget | -194.91% |
| 5 | PROM | bitget | -152.64% |
| 6 | BLEND | okx | -151.98% |
| 7 | VANRY | bitget | -149.91% |
| 8 | GWEI | bitget | -137.64% |
| 9 | MIRA | bitget | -128.55% |
| 10 | BARD | bitget | -124.94% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SAHARA | +120.20% | bitget | +5.47% | okx | -114.72% |
| 2 | SOXL | +108.75% | okx | +108.75% | bitget | +0.00% |
| 3 | CRCL | +83.83% | okx | +83.83% | bitget | +0.00% |
| 4 | BEAT | +78.06% | bitget | -10.40% | okx | -88.46% |
| 5 | SKHY | +74.89% | okx | +74.89% | bitget | +0.00% |
| 6 | SOXS | +68.69% | bitget | +0.00% | okx | -68.69% |
| 7 | SNXX | +67.60% | okx | +67.60% | bitget | +0.00% |
| 8 | STX | +58.03% | okx | -4.27% | bitget | -62.31% |
| 9 | 1INCH | +57.93% | okx | +10.95% | bitget | -46.98% |
| 10 | ZIL | +50.59% | okx | +5.47% | bitget | -45.11% |
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
