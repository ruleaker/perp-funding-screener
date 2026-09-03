# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-03 12:55 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1229**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | okx | +278.78% |
| 2 | IONQ | okx | +198.61% |
| 3 | BOT | okx | +142.32% |
| 4 | GLW | bitget | +127.68% |
| 5 | SKHYNIX | okx | +104.61% |
| 6 | ZM | okx | +100.71% |
| 7 | NKE | bitget | +92.53% |
| 8 | SHAZ | okx | +85.62% |
| 9 | 牛来 | bitget | +83.55% |
| 10 | OKTA | okx | +72.98% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ANKR | bitget | -809.53% |
| 2 | NTAP | bitget | -547.50% |
| 3 | ACE | bitget | -542.46% |
| 4 | LA | bitget | -340.98% |
| 5 | HIVE | bitget | -316.56% |
| 6 | LA | okx | -242.26% |
| 7 | CAP | bitget | -231.59% |
| 8 | CAP | okx | -223.10% |
| 9 | DDOG | okx | -218.30% |
| 10 | T | bitget | -199.84% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | FWDI | +278.78% | okx | +278.78% | bitget | +0.00% |
| 2 | DDOG | +218.30% | bitget | +0.00% | okx | -218.30% |
| 3 | SNOW | +184.75% | bitget | +0.00% | okx | -184.75% |
| 4 | IONQ | +160.72% | okx | +198.61% | bitget | +37.89% |
| 5 | BOT | +142.32% | okx | +142.32% | bitget | +0.00% |
| 6 | LRCX | +135.05% | bitget | +0.00% | okx | -135.05% |
| 7 | GLW | +127.68% | bitget | +127.68% | okx | +0.00% |
| 8 | ROK | +103.36% | bitget | +0.00% | okx | -103.36% |
| 9 | ZM | +100.71% | okx | +100.71% | bitget | +0.00% |
| 10 | LA | +98.72% | okx | -242.26% | bitget | -340.98% |
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
