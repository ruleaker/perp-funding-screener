# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-26 21:06 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1367**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BWET | bitget | +301.78% |
| 2 | BWET | okx | +264.99% |
| 3 | KR200 | okx | +211.54% |
| 4 | KIOXIA | bitget | +186.70% |
| 5 | AXON | bitget | +147.50% |
| 6 | KIOXIA | okx | +146.12% |
| 7 | MSTU | bitget | +143.88% |
| 8 | AGPU | bitget | +115.08% |
| 9 | ZM | bitget | +93.84% |
| 10 | KSTR | bitget | +88.48% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -1095.00% |
| 2 | USDBRL | bitget | -356.09% |
| 3 | DOOD | bitget | -329.92% |
| 4 | DOOD | okx | -319.00% |
| 5 | EIDO | bitget | -302.33% |
| 6 | IRYS | okx | -289.01% |
| 7 | FWDI | okx | -233.34% |
| 8 | CYPH | okx | -216.98% |
| 9 | OSS | bitget | -202.79% |
| 10 | STEEM | bitget | -194.69% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1100.47% | bitget | +5.47% | okx | -1095.00% |
| 2 | IRYS | +229.00% | bitget | -60.01% | okx | -289.01% |
| 3 | KR200 | +211.54% | okx | +211.54% | bitget | +0.00% |
| 4 | CYPH | +167.70% | bitget | -49.27% | okx | -216.98% |
| 5 | UNITREE | +119.15% | bitget | +0.00% | okx | -119.15% |
| 6 | MSTU | +94.96% | bitget | +143.88% | okx | +48.93% |
| 7 | ORDER | +87.06% | bitget | -17.30% | okx | -104.37% |
| 8 | MARA | +80.51% | okx | +80.51% | bitget | +0.00% |
| 9 | BSP | +65.37% | okx | +0.00% | bitget | -65.37% |
| 10 | IOST | +59.74% | bitget | -21.90% | okx | -81.64% |
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
