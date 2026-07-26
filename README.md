# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-26 10:16 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LYN | bitget | +125.71% |
| 2 | XVG | bitget | +84.53% |
| 3 | 1000RATS | bitget | +53.98% |
| 4 | KIOXIA | okx | +46.16% |
| 5 | RAVE | okx | +44.64% |
| 6 | SNXX | okx | +44.04% |
| 7 | ACU | bitget | +35.26% |
| 8 | H | okx | +35.10% |
| 9 | 1MCHEEMS | bitget | +34.71% |
| 10 | M | bitget | +31.97% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | EUL | bitget | -1572.64% |
| 2 | DEXE | bitget | -761.79% |
| 3 | TLM | bitget | -694.34% |
| 4 | VANRY | bitget | -639.48% |
| 5 | LPT | okx | -223.45% |
| 6 | LPT | bitget | -213.53% |
| 7 | BARD | okx | -157.89% |
| 8 | HOT | bitget | -139.07% |
| 9 | BARD | bitget | -139.07% |
| 10 | PROM | bitget | -134.03% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BEAT | +74.20% | bitget | +5.47% | okx | -68.73% |
| 2 | PI | +65.50% | bitget | +5.47% | okx | -60.03% |
| 3 | ZIL | +64.61% | okx | +5.47% | bitget | -59.13% |
| 4 | CHZ | +50.78% | bitget | +10.95% | okx | -39.83% |
| 5 | BZ | +48.20% | bitget | +0.00% | okx | -48.20% |
| 6 | ESP | +46.87% | okx | +5.47% | bitget | -41.39% |
| 7 | KIOXIA | +46.16% | okx | +46.16% | bitget | +0.00% |
| 8 | PIEVERSE | +44.29% | bitget | +5.47% | okx | -38.82% |
| 9 | SNXX | +44.04% | okx | +44.04% | bitget | +0.00% |
| 10 | CL | +39.52% | bitget | +0.00% | okx | -39.52% |
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
