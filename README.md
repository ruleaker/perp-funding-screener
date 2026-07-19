# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-19 17:30 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1118**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BE | okx | +275.50% |
| 2 | LAB | okx | +79.91% |
| 3 | O | okx | +73.92% |
| 4 | XMR | bitget | +64.93% |
| 5 | BANK | bitget | +60.66% |
| 6 | NBIS | okx | +56.90% |
| 7 | IDOL | bitget | +51.57% |
| 8 | QNT | okx | +48.56% |
| 9 | LYN | bitget | +38.22% |
| 10 | SIREN | bitget | +36.79% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TLM | bitget | -424.64% |
| 2 | SKL | bitget | -163.26% |
| 3 | SPELL | bitget | -130.52% |
| 4 | VANRY | bitget | -120.89% |
| 5 | NEO | bitget | -102.93% |
| 6 | SOXL | okx | -100.42% |
| 7 | RE | okx | -98.30% |
| 8 | CHZ | bitget | -93.62% |
| 9 | CHZ | okx | -89.22% |
| 10 | RE | bitget | -87.05% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BE | +275.50% | okx | +275.50% | bitget | +0.00% |
| 2 | SOXL | +100.42% | bitget | +0.00% | okx | -100.42% |
| 3 | LAB | +67.76% | okx | +79.91% | bitget | +12.15% |
| 4 | CBRS | +67.73% | bitget | +0.00% | okx | -67.73% |
| 5 | NBIS | +56.90% | okx | +56.90% | bitget | +0.00% |
| 6 | O | +52.79% | okx | +73.92% | bitget | +21.13% |
| 7 | YB | +48.42% | bitget | +5.47% | okx | -42.94% |
| 8 | 1INCH | +47.63% | okx | +10.95% | bitget | -36.68% |
| 9 | NEO | +46.24% | okx | -56.69% | bitget | -102.93% |
| 10 | IOST | +38.17% | okx | +9.81% | bitget | -28.36% |
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
