# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-15 21:07 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1413**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NVDL | bitget | +244.19% |
| 2 | SOXL | okx | +244.00% |
| 3 | NVDL | okx | +235.52% |
| 4 | KORU | okx | +203.01% |
| 5 | SHEIN | okx | +185.65% |
| 6 | NVDA | okx | +184.38% |
| 7 | SOXL | bitget | +166.77% |
| 8 | CRWV | okx | +165.45% |
| 9 | KORU | bitget | +164.91% |
| 10 | NVDA | bitget | +114.87% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RARE | bitget | -1263.30% |
| 2 | TLM | bitget | -585.72% |
| 3 | KAVA | bitget | -511.15% |
| 4 | BLUR | okx | -312.29% |
| 5 | BLUR | bitget | -283.60% |
| 6 | SOPH | bitget | -215.39% |
| 7 | SOPH | okx | -196.12% |
| 8 | INIT | okx | -190.09% |
| 9 | SOXS | okx | -159.79% |
| 10 | RUNE | bitget | -150.23% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | INIT | +191.51% | bitget | +1.42% | okx | -190.09% |
| 2 | SHEIN | +185.65% | okx | +185.65% | bitget | +0.00% |
| 3 | ONE | +112.01% | okx | -9.65% | bitget | -121.65% |
| 4 | HUMA | +103.44% | bitget | -32.19% | okx | -135.63% |
| 5 | SOXL | +77.23% | okx | +244.00% | bitget | +166.77% |
| 6 | MSTU | +71.17% | bitget | +71.17% | okx | +0.00% |
| 7 | NVDA | +69.52% | okx | +184.38% | bitget | +114.87% |
| 8 | KIOXIA | +61.83% | okx | +61.83% | bitget | +0.00% |
| 9 | SKHYNIX | +61.81% | okx | +67.18% | bitget | +5.37% |
| 10 | SMH | +61.32% | okx | +61.32% | bitget | +0.00% |
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
