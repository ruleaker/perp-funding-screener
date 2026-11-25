# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-25 00:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1429**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +233.70% |
| 2 | URNM | okx | +180.01% |
| 3 | AXON | bitget | +134.90% |
| 4 | FWDI | bitget | +119.25% |
| 5 | BNC | bitget | +113.00% |
| 6 | ROK | okx | +106.75% |
| 7 | CXMT | okx | +105.89% |
| 8 | INIT | okx | +81.39% |
| 9 | BX | okx | +76.76% |
| 10 | URNM | bitget | +65.15% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | okx | -770.20% |
| 2 | SAHARA | okx | -754.93% |
| 3 | SAHARA | bitget | -697.41% |
| 4 | SKDD | okx | -331.73% |
| 5 | JNJ | okx | -302.05% |
| 6 | FLEX | okx | -299.38% |
| 7 | SKDD | bitget | -257.22% |
| 8 | EWZS | okx | -253.83% |
| 9 | BIGTIME | okx | -242.08% |
| 10 | VICR | okx | -225.56% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | FWDI | +889.45% | bitget | +119.25% | okx | -770.20% |
| 2 | FLEX | +276.60% | bitget | -22.78% | okx | -299.38% |
| 3 | EWZS | +253.83% | bitget | +0.00% | okx | -253.83% |
| 4 | H100 | +228.22% | okx | +233.70% | bitget | +5.47% |
| 5 | BWET | +218.42% | bitget | +0.00% | okx | -218.42% |
| 6 | JNJ | +201.53% | bitget | -100.52% | okx | -302.05% |
| 7 | DDOG | +195.71% | bitget | +0.00% | okx | -195.71% |
| 8 | BIGTIME | +175.06% | bitget | -67.01% | okx | -242.08% |
| 9 | XOM | +173.52% | bitget | +0.00% | okx | -173.52% |
| 10 | IBKR | +168.57% | bitget | +0.00% | okx | -168.57% |
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
