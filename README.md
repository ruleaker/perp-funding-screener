# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-10 17:23 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1171**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 龙虾 | bitget | +268.06% |
| 2 | NG | okx | +202.17% |
| 3 | SIREN | bitget | +148.15% |
| 4 | UNITAS | bitget | +107.75% |
| 5 | NATGAS | bitget | +96.47% |
| 6 | ELSA | bitget | +88.69% |
| 7 | BEAT | okx | +79.90% |
| 8 | GOOGL | bitget | +76.10% |
| 9 | XCU | okx | +75.71% |
| 10 | SKHYNIX | okx | +63.34% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KAITO | bitget | -2047.21% |
| 2 | KAITO | okx | -436.85% |
| 3 | BOT | bitget | -174.00% |
| 4 | BZ | bitget | -135.67% |
| 5 | BZ | okx | -132.77% |
| 6 | DOS | okx | -98.00% |
| 7 | TWLO | okx | -87.07% |
| 8 | IOTX | bitget | -77.64% |
| 9 | CL | bitget | -71.07% |
| 10 | CL | okx | -68.53% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KAITO | +1610.36% | okx | -436.85% | bitget | -2047.21% |
| 2 | BOT | +118.64% | okx | -55.36% | bitget | -174.00% |
| 3 | TWLO | +87.07% | bitget | +0.00% | okx | -87.07% |
| 4 | GOOGL | +63.96% | bitget | +76.10% | okx | +12.14% |
| 5 | SKHYNIX | +63.34% | okx | +63.34% | bitget | +0.00% |
| 6 | BICO | +59.49% | bitget | +30.99% | okx | -28.50% |
| 7 | KGEN | +56.75% | okx | +62.22% | bitget | +5.47% |
| 8 | BSP | +55.63% | okx | +55.63% | bitget | +0.00% |
| 9 | ZIL | +50.83% | bitget | -1.42% | okx | -52.26% |
| 10 | BEAT | +45.30% | okx | +79.90% | bitget | +34.60% |
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
