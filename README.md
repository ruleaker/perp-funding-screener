# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-20 04:49 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1021**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BTW | bitget | +358.83% |
| 2 | SKHYNIX | okx | +267.74% |
| 3 | SIREN | bitget | +246.37% |
| 4 | INTC | okx | +211.71% |
| 5 | SAMSUNG | okx | +171.41% |
| 6 | ESPORTS | bitget | +131.07% |
| 7 | DRAM | okx | +131.00% |
| 8 | XPIN | bitget | +122.75% |
| 9 | AXTI | okx | +122.52% |
| 10 | O | okx | +98.12% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RE | bitget | -423.55% |
| 2 | AXS | okx | -366.38% |
| 3 | HOME | okx | -318.48% |
| 4 | H | okx | -305.31% |
| 5 | H | bitget | -288.97% |
| 6 | BICO | okx | -271.27% |
| 7 | BICO | bitget | -220.75% |
| 8 | KAT | okx | -213.42% |
| 9 | RE | okx | -199.97% |
| 10 | AXS | bitget | -156.69% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +267.74% | okx | +267.74% | bitget | +0.00% |
| 2 | RE | +223.57% | okx | -199.97% | bitget | -423.55% |
| 3 | INTC | +211.71% | okx | +211.71% | bitget | +0.00% |
| 4 | AXS | +209.69% | bitget | -156.69% | okx | -366.38% |
| 5 | HOME | +197.05% | bitget | -121.44% | okx | -318.48% |
| 6 | KAT | +181.01% | bitget | -32.41% | okx | -213.42% |
| 7 | SAMSUNG | +171.41% | okx | +171.41% | bitget | +0.00% |
| 8 | DRAM | +131.00% | okx | +131.00% | bitget | +0.00% |
| 9 | AXTI | +122.52% | okx | +122.52% | bitget | +0.00% |
| 10 | SAHARA | +113.39% | bitget | -24.20% | okx | -137.59% |
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
