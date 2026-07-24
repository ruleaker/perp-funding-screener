# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-24 17:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITAS | bitget | +137.42% |
| 2 | NDX100 | bitget | +103.70% |
| 3 | XPD | okx | +99.55% |
| 4 | XPD | bitget | +85.96% |
| 5 | BOT | bitget | +67.78% |
| 6 | SIREN | bitget | +61.10% |
| 7 | RLS | okx | +56.97% |
| 8 | BANK | bitget | +53.22% |
| 9 | PIPPIN | bitget | +51.79% |
| 10 | ESPORTS | bitget | +47.19% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -953.31% |
| 2 | BARD | bitget | -277.14% |
| 3 | STX | okx | -222.02% |
| 4 | TLM | bitget | -200.06% |
| 5 | PROM | bitget | -192.83% |
| 6 | GWEI | bitget | -189.22% |
| 7 | STX | bitget | -177.06% |
| 8 | BARD | okx | -134.02% |
| 9 | VANRY | bitget | -133.04% |
| 10 | O | okx | -115.03% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BARD | +143.12% | okx | -134.02% | bitget | -277.14% |
| 2 | SKHYNIX | +110.00% | bitget | +0.00% | okx | -110.00% |
| 3 | SAMSUNG | +93.24% | bitget | +0.00% | okx | -93.24% |
| 4 | BOT | +67.78% | bitget | +67.78% | okx | +0.00% |
| 5 | O | +66.30% | bitget | -48.73% | okx | -115.03% |
| 6 | DATA | +52.38% | okx | -34.67% | bitget | -87.05% |
| 7 | PIPPIN | +46.32% | bitget | +51.79% | okx | +5.47% |
| 8 | STX | +44.96% | bitget | -177.06% | okx | -222.02% |
| 9 | LDO | +44.94% | okx | +10.33% | bitget | -34.60% |
| 10 | AAPL | +38.49% | bitget | +0.00% | okx | -38.49% |
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
