# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-12 04:48 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1250**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | INDA | bitget | +95.70% |
| 2 | US500 | okx | +84.16% |
| 3 | ONE | okx | +66.80% |
| 4 | SIREN | bitget | +61.21% |
| 5 | AIN | bitget | +40.41% |
| 6 | SONIC | bitget | +39.97% |
| 7 | COOKIE | bitget | +34.82% |
| 8 | TRUTH | okx | +31.15% |
| 9 | BNC | bitget | +24.86% |
| 10 | XCU | okx | +24.36% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | VTHO | bitget | -761.02% |
| 2 | LSK | bitget | -760.92% |
| 3 | IOST | okx | -282.93% |
| 4 | SOPH | okx | -207.48% |
| 5 | ANIME | okx | -201.73% |
| 6 | SOPH | bitget | -186.48% |
| 7 | ANIME | bitget | -182.10% |
| 8 | TREE | bitget | -170.49% |
| 9 | RVN | okx | -134.64% |
| 10 | ACE | bitget | -127.46% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | IOST | +218.54% | bitget | -64.39% | okx | -282.93% |
| 2 | RAY | +79.29% | bitget | -3.61% | okx | -82.90% |
| 3 | MINA | +70.90% | okx | -4.11% | bitget | -75.01% |
| 4 | ONE | +55.85% | okx | +66.80% | bitget | +10.95% |
| 5 | DOOD | +39.29% | bitget | +5.47% | okx | -33.82% |
| 6 | ZIL | +38.59% | bitget | +1.10% | okx | -37.49% |
| 7 | ATOM | +34.73% | bitget | +10.95% | okx | -23.78% |
| 8 | RVN | +34.23% | bitget | -100.41% | okx | -134.64% |
| 9 | GPRO | +34.16% | okx | +0.00% | bitget | -34.16% |
| 10 | BIGTIME | +24.24% | bitget | +5.47% | okx | -18.76% |
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
