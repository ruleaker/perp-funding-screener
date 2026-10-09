# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-09 15:25 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1305**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +926.14% |
| 2 | SECZ | bitget | +554.07% |
| 3 | NATGAS | bitget | +547.50% |
| 4 | AGPU | bitget | +374.27% |
| 5 | BSP | bitget | +262.36% |
| 6 | GPRO | bitget | +170.71% |
| 7 | RDDT | bitget | +165.78% |
| 8 | SOFTBANK | okx | +130.68% |
| 9 | CRML | bitget | +127.02% |
| 10 | USDESTOCK | bitget | +127.02% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -1095.00% |
| 2 | KOPN | bitget | -919.03% |
| 3 | CTSI | bitget | -565.79% |
| 4 | BWET | okx | -560.65% |
| 5 | ECHO | bitget | -482.35% |
| 6 | JMKE | bitget | -440.08% |
| 7 | BWET | bitget | -396.94% |
| 8 | XDP | okx | -368.43% |
| 9 | SKL | bitget | -360.04% |
| 10 | KSTR | bitget | -345.91% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1095.00% | bitget | +0.00% | okx | -1095.00% |
| 2 | SECZ | +554.07% | bitget | +554.07% | okx | +0.00% |
| 3 | BSP | +262.36% | bitget | +262.36% | okx | +0.00% |
| 4 | RDDT | +174.59% | bitget | +165.78% | okx | -8.81% |
| 5 | BWET | +163.71% | bitget | -396.94% | okx | -560.65% |
| 6 | GPRO | +159.43% | bitget | +170.71% | okx | +11.28% |
| 7 | KSTR | +158.28% | okx | -187.63% | bitget | -345.91% |
| 8 | FWDI | +146.98% | bitget | -10.40% | okx | -157.38% |
| 9 | SOFTBANK | +130.68% | okx | +130.68% | bitget | +0.00% |
| 10 | WEN | +93.18% | bitget | +93.18% | okx | +0.00% |
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
