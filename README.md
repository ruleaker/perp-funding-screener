# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-08 15:45 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1301**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +1095.00% |
| 2 | NATGAS | bitget | +547.50% |
| 3 | BLSH | bitget | +529.87% |
| 4 | BOT | bitget | +381.50% |
| 5 | ECHO | bitget | +316.35% |
| 6 | BUD | bitget | +297.29% |
| 7 | MSTU | okx | +160.74% |
| 8 | GPRO | bitget | +145.42% |
| 9 | PIPPIN | bitget | +133.81% |
| 10 | ETN | bitget | +121.11% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BWET | okx | -1095.00% |
| 2 | CTSI | bitget | -1050.32% |
| 3 | BWET | bitget | -1011.12% |
| 4 | OGN | bitget | -662.15% |
| 5 | USDESTOCK | bitget | -606.74% |
| 6 | H100 | okx | -492.47% |
| 7 | SKL | bitget | -487.60% |
| 8 | ERA | bitget | -331.89% |
| 9 | BZ | okx | -273.20% |
| 10 | MINA | bitget | -241.23% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +492.47% | bitget | +0.00% | okx | -492.47% |
| 2 | BOT | +298.70% | bitget | +381.50% | okx | +82.80% |
| 3 | FWDI | +195.65% | bitget | -33.07% | okx | -228.72% |
| 4 | MSTU | +160.74% | okx | +160.74% | bitget | +0.00% |
| 5 | ONE | +155.69% | okx | +21.77% | bitget | -133.92% |
| 6 | PIPPIN | +128.33% | bitget | +133.81% | okx | +5.47% |
| 7 | GPRO | +117.88% | bitget | +145.42% | okx | +27.53% |
| 8 | AMC | +106.11% | okx | +0.00% | bitget | -106.11% |
| 9 | BSP | +98.44% | okx | +0.00% | bitget | -98.44% |
| 10 | BZ | +98.00% | bitget | -175.20% | okx | -273.20% |
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
