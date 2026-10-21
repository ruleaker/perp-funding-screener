# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-21 13:59 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1346**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +1015.91% |
| 2 | FLY | bitget | +302.77% |
| 3 | KORU | bitget | +287.11% |
| 4 | FWDI | okx | +213.78% |
| 5 | GTLB | bitget | +188.34% |
| 6 | ZCSH | bitget | +151.33% |
| 7 | AGPU | bitget | +112.24% |
| 8 | BNC | bitget | +110.92% |
| 9 | ACNSTOCK | bitget | +109.50% |
| 10 | JNJ | okx | +104.80% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BIRB | bitget | -1791.20% |
| 2 | DOOD | bitget | -1670.75% |
| 3 | MEW | bitget | -1355.61% |
| 4 | IOST | bitget | -1206.58% |
| 5 | DOOD | okx | -1095.00% |
| 6 | MEW | okx | -784.27% |
| 7 | IOST | okx | -501.62% |
| 8 | BTW | bitget | -488.15% |
| 9 | ECHO | bitget | -452.24% |
| 10 | TWST | bitget | -432.53% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1010.43% | okx | +1015.91% | bitget | +5.47% |
| 2 | IOST | +704.96% | okx | -501.62% | bitget | -1206.58% |
| 3 | DOOD | +575.75% | okx | -1095.00% | bitget | -1670.75% |
| 4 | MEW | +571.34% | okx | -784.27% | bitget | -1355.61% |
| 5 | TWST | +425.78% | okx | -6.75% | bitget | -432.53% |
| 6 | FLY | +302.77% | bitget | +302.77% | okx | +0.00% |
| 7 | KORU | +278.91% | bitget | +287.11% | okx | +8.20% |
| 8 | FWDI | +213.78% | okx | +213.78% | bitget | +0.00% |
| 9 | GTLB | +188.34% | bitget | +188.34% | okx | +0.00% |
| 10 | DDOG | +142.43% | bitget | +0.00% | okx | -142.43% |
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
