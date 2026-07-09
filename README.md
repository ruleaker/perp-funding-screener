# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-09 04:27 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1098**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOFTBANK | okx | +1095.00% |
| 2 | SKHYNIX | bitget | +547.50% |
| 3 | SAMSUNG | bitget | +499.87% |
| 4 | HYUNDAI | bitget | +391.24% |
| 5 | SKHYNIX | okx | +382.92% |
| 6 | HYUNDAI | okx | +299.56% |
| 7 | SAMSUNG | okx | +279.44% |
| 8 | LAB | okx | +104.43% |
| 9 | APR | okx | +96.70% |
| 10 | KIOXIA | okx | +85.29% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZHIPU | okx | -1095.00% |
| 2 | ZHIPU | bitget | -547.50% |
| 3 | OGN | bitget | -423.98% |
| 4 | SLX | okx | -320.69% |
| 5 | GWEI | bitget | -278.02% |
| 6 | KORU | bitget | -178.27% |
| 7 | GIGADEVICE | bitget | -162.50% |
| 8 | USO | okx | -127.85% |
| 9 | SPELL | bitget | -118.59% |
| 10 | ONG | bitget | -104.68% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ZHIPU | +547.50% | bitget | -547.50% | okx | -1095.00% |
| 2 | KORU | +231.91% | okx | +53.65% | bitget | -178.27% |
| 3 | SLX | +227.94% | bitget | -92.75% | okx | -320.69% |
| 4 | SAMSUNG | +220.43% | bitget | +499.87% | okx | +279.44% |
| 5 | SKHYNIX | +164.58% | bitget | +547.50% | okx | +382.92% |
| 6 | RAM | +103.92% | okx | +0.00% | bitget | -103.92% |
| 7 | LAB | +102.35% | okx | +104.43% | bitget | +2.08% |
| 8 | HYUNDAI | +91.68% | bitget | +391.24% | okx | +299.56% |
| 9 | APR | +91.22% | okx | +96.70% | bitget | +5.47% |
| 10 | EGLD | +75.27% | bitget | -20.37% | okx | -95.64% |
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
