# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-30 18:17 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1062**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +167.97% |
| 2 | KIOXIA | okx | +154.01% |
| 3 | GOOGL | bitget | +104.46% |
| 4 | CRCL | okx | +97.54% |
| 5 | ZBT | bitget | +95.59% |
| 6 | DRAM | bitget | +94.39% |
| 7 | MRVL | bitget | +93.18% |
| 8 | CRCL | bitget | +92.97% |
| 9 | CBRS | bitget | +89.90% |
| 10 | GLW | okx | +84.55% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | IN | bitget | -2190.00% |
| 2 | GLM | bitget | -1991.15% |
| 3 | GLM | okx | -1095.00% |
| 4 | SLX | okx | -766.27% |
| 5 | LAB | bitget | -554.07% |
| 6 | ESP | okx | -484.36% |
| 7 | LAB | okx | -480.77% |
| 8 | SLX | bitget | -435.15% |
| 9 | GRAM | bitget | -370.77% |
| 10 | ESP | bitget | -356.53% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | GLM | +896.15% | okx | -1095.00% | bitget | -1991.15% |
| 2 | GRAM | +376.24% | okx | +5.47% | bitget | -370.77% |
| 3 | SLX | +331.12% | bitget | -435.15% | okx | -766.27% |
| 4 | KIOXIA | +154.01% | okx | +154.01% | bitget | +0.00% |
| 5 | ESP | +127.83% | bitget | -356.53% | okx | -484.36% |
| 6 | GOOGL | +104.46% | bitget | +104.46% | okx | +0.00% |
| 7 | ZBT | +90.12% | bitget | +95.59% | okx | +5.47% |
| 8 | CBRS | +80.27% | bitget | +89.90% | okx | +9.63% |
| 9 | LAB | +73.30% | okx | -480.77% | bitget | -554.07% |
| 10 | DRAM | +67.58% | bitget | +94.39% | okx | +26.81% |
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
