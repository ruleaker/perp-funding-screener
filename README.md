# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-31 14:38 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1385**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AKE | bitget | +217.25% |
| 2 | GIGADEV | okx | +71.00% |
| 3 | ARIA | bitget | +49.93% |
| 4 | FIGHT | bitget | +48.62% |
| 5 | ZEST | bitget | +40.41% |
| 6 | APR | okx | +37.73% |
| 7 | CHILLGUY | bitget | +35.92% |
| 8 | US100 | okx | +33.44% |
| 9 | DNA | okx | +31.39% |
| 10 | TRIA | okx | +27.92% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | WET | okx | -791.19% |
| 2 | WET | bitget | -749.64% |
| 3 | H100 | okx | -528.14% |
| 4 | COW | bitget | -300.69% |
| 5 | LSK | bitget | -224.48% |
| 6 | BLUR | bitget | -215.82% |
| 7 | HOT | bitget | -211.88% |
| 8 | TRX | okx | -178.24% |
| 9 | STX | okx | -130.81% |
| 10 | CVC | bitget | -118.37% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +533.62% | bitget | +5.47% | okx | -528.14% |
| 2 | AKE | +211.77% | bitget | +217.25% | okx | +5.47% |
| 3 | BLUR | +125.02% | okx | -90.81% | bitget | -215.82% |
| 4 | TRX | +112.65% | bitget | -65.59% | okx | -178.24% |
| 5 | SHEIN | +97.50% | bitget | +0.00% | okx | -97.50% |
| 6 | BX | +85.57% | bitget | +0.00% | okx | -85.57% |
| 7 | GRT | +68.13% | bitget | -1.97% | okx | -70.10% |
| 8 | IOST | +62.63% | bitget | +0.33% | okx | -62.30% |
| 9 | STX | +57.01% | bitget | -73.80% | okx | -130.81% |
| 10 | UNITREE | +50.48% | bitget | +0.00% | okx | -50.48% |
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
