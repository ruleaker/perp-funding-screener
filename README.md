# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-09 06:25 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1301**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +1095.00% |
| 2 | NG | okx | +579.47% |
| 3 | NATGAS | bitget | +284.59% |
| 4 | CXMT | okx | +262.75% |
| 5 | KSTR | okx | +241.17% |
| 6 | SHAZ | okx | +237.92% |
| 7 | USDESTOCK | bitget | +224.80% |
| 8 | SECZ | okx | +218.39% |
| 9 | CXMT | bitget | +203.01% |
| 10 | SOXL | bitget | +182.97% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BWET | okx | -867.34% |
| 2 | CTSI | bitget | -682.29% |
| 3 | SKL | bitget | -335.73% |
| 4 | MINA | bitget | -216.37% |
| 5 | SAND | bitget | -208.16% |
| 6 | SOXS | bitget | -189.65% |
| 7 | ERA | bitget | -175.42% |
| 8 | SAND | okx | -126.83% |
| 9 | OGN | bitget | -103.59% |
| 10 | MINA | okx | -99.99% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1095.00% | okx | +1095.00% | bitget | +0.00% |
| 2 | BWET | +867.34% | bitget | +0.00% | okx | -867.34% |
| 3 | SECZ | +218.39% | okx | +218.39% | bitget | +0.00% |
| 4 | SHAZ | +216.13% | okx | +237.92% | bitget | +21.79% |
| 5 | KSTR | +213.47% | okx | +241.17% | bitget | +27.70% |
| 6 | SOXS | +189.65% | okx | +0.00% | bitget | -189.65% |
| 7 | SOXL | +182.97% | bitget | +182.97% | okx | +0.00% |
| 8 | GPRO | +178.22% | okx | +178.22% | bitget | +0.00% |
| 9 | BOT | +166.38% | okx | +166.38% | bitget | +0.00% |
| 10 | MUU | +145.74% | bitget | +145.74% | okx | +0.00% |
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
