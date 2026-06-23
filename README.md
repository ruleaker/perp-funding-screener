# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-23 18:18 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1037**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H | okx | +121.59% |
| 2 | ESPORTS | bitget | +70.96% |
| 3 | SIREN | bitget | +64.93% |
| 4 | XPD | okx | +60.61% |
| 5 | SNDK | okx | +58.09% |
| 6 | SOXL | okx | +51.97% |
| 7 | XPD | bitget | +49.82% |
| 8 | MU | bitget | +47.52% |
| 9 | BMNR | okx | +47.12% |
| 10 | XAG | okx | +35.89% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MTL | bitget | -595.57% |
| 2 | LRC | okx | -506.83% |
| 3 | SYN | bitget | -352.04% |
| 4 | TAIKO | bitget | -345.58% |
| 5 | RTXSTOCK | bitget | -330.14% |
| 6 | SHLD | okx | -310.11% |
| 7 | QNT | okx | -238.72% |
| 8 | RE | okx | -236.99% |
| 9 | XLU | bitget | -208.71% |
| 10 | TTMI | okx | -204.61% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | QNT | +249.67% | bitget | +10.95% | okx | -238.72% |
| 2 | H | +116.12% | okx | +121.59% | bitget | +5.47% |
| 3 | LAB | +74.58% | bitget | -113.99% | okx | -188.57% |
| 4 | BEAT | +73.91% | bitget | +12.15% | okx | -61.76% |
| 5 | LA | +69.82% | bitget | +5.47% | okx | -64.35% |
| 6 | RVN | +64.81% | bitget | +5.47% | okx | -59.34% |
| 7 | LAYER | +60.53% | bitget | +4.93% | okx | -55.60% |
| 8 | SKHYNIX | +58.14% | okx | +0.00% | bitget | -58.14% |
| 9 | SNDK | +58.09% | okx | +58.09% | bitget | +0.00% |
| 10 | CHIP | +54.82% | bitget | -25.40% | okx | -80.22% |
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
