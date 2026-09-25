# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-25 05:09 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1282**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 龙虾 | bitget | +332.99% |
| 2 | SHEIN | okx | +262.33% |
| 3 | SHEINHKD | bitget | +258.53% |
| 4 | XIAOMI | okx | +221.77% |
| 5 | BX | okx | +180.81% |
| 6 | KUAISHOU | bitget | +133.15% |
| 7 | BOT | okx | +129.34% |
| 8 | TMF | okx | +123.58% |
| 9 | BYD | bitget | +114.43% |
| 10 | CYPH | okx | +112.31% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CVC | bitget | -763.54% |
| 2 | STEEM | bitget | -383.47% |
| 3 | ONE | bitget | -326.53% |
| 4 | G | bitget | -292.26% |
| 5 | FLOCK | okx | -173.06% |
| 6 | XAI | bitget | -145.85% |
| 7 | FLOCK | bitget | -132.93% |
| 8 | CSOPSK2LHKD | bitget | -131.07% |
| 9 | CSOPSS2LHKD | bitget | -127.13% |
| 10 | WAXP | bitget | -117.93% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +277.47% | okx | -49.05% | bitget | -326.53% |
| 2 | SHEIN | +262.33% | okx | +262.33% | bitget | +0.00% |
| 3 | BX | +180.81% | okx | +180.81% | bitget | +0.00% |
| 4 | BOT | +129.34% | okx | +129.34% | bitget | +0.00% |
| 5 | TMF | +123.58% | okx | +123.58% | bitget | +0.00% |
| 6 | XIAOMI | +118.07% | okx | +221.77% | bitget | +103.70% |
| 7 | CYPH | +112.31% | okx | +112.31% | bitget | +0.00% |
| 8 | TSEM | +111.03% | okx | +111.03% | bitget | +0.00% |
| 9 | LYTE | +99.38% | okx | +99.38% | bitget | +0.00% |
| 10 | SAMSUNG | +86.45% | okx | +86.45% | bitget | +0.00% |
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
