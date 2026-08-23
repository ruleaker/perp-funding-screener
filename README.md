# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-23 02:07 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1197**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SHAZ | okx | +210.30% |
| 2 | 龙虾 | bitget | +98.66% |
| 3 | NBIS | okx | +74.89% |
| 4 | CRCL | okx | +70.95% |
| 5 | BEAT | okx | +66.33% |
| 6 | ONE | bitget | +61.32% |
| 7 | KIOXIA | okx | +54.59% |
| 8 | AAOI | okx | +54.10% |
| 9 | FIGHT | bitget | +48.40% |
| 10 | UP | okx | +47.96% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MOVE | okx | -1075.85% |
| 2 | MOVE | bitget | -1043.97% |
| 3 | COTI | bitget | -196.77% |
| 4 | ONG | bitget | -195.24% |
| 5 | RVN | okx | -191.25% |
| 6 | ONT | okx | -176.95% |
| 7 | GAS | okx | -171.91% |
| 8 | BICO | bitget | -145.31% |
| 9 | LUNC | bitget | -143.77% |
| 10 | ONT | bitget | -142.68% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SHAZ | +210.30% | okx | +210.30% | bitget | +0.00% |
| 2 | RVN | +159.71% | bitget | -31.54% | okx | -191.25% |
| 3 | GAS | +117.16% | bitget | -54.75% | okx | -171.91% |
| 4 | BICO | +113.43% | okx | -31.88% | bitget | -145.31% |
| 5 | NBIS | +74.89% | okx | +74.89% | bitget | +0.00% |
| 6 | CRCL | +70.95% | okx | +70.95% | bitget | +0.00% |
| 7 | UNITREE | +59.91% | bitget | +0.00% | okx | -59.91% |
| 8 | KIOXIA | +54.59% | okx | +54.59% | bitget | +0.00% |
| 9 | AAOI | +54.10% | okx | +54.10% | bitget | +0.00% |
| 10 | BEAT | +51.88% | okx | +66.33% | bitget | +14.45% |
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
