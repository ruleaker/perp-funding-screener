# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-20 05:06 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1264**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | PIPPIN | bitget | +225.46% |
| 2 | FIGHT | bitget | +215.28% |
| 3 | US500 | okx | +84.07% |
| 4 | SIREN | bitget | +74.24% |
| 5 | CXMT | okx | +69.43% |
| 6 | BAN | bitget | +47.52% |
| 7 | SLX | okx | +47.43% |
| 8 | M | bitget | +47.41% |
| 9 | BILL | okx | +44.80% |
| 10 | PONS | bitget | +40.73% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONG | bitget | -1062.04% |
| 2 | AKE | bitget | -563.92% |
| 3 | AKE | okx | -376.89% |
| 4 | CAP | okx | -319.78% |
| 5 | CAP | bitget | -255.35% |
| 6 | AVA | bitget | -231.26% |
| 7 | F | okx | -223.70% |
| 8 | F | bitget | -220.31% |
| 9 | MSTR | okx | -141.01% |
| 10 | EGLD | bitget | -129.21% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | PIPPIN | +216.70% | bitget | +225.46% | okx | +8.76% |
| 2 | AKE | +187.04% | okx | -376.89% | bitget | -563.92% |
| 3 | EGLD | +140.16% | okx | +10.95% | bitget | -129.21% |
| 4 | ONE | +69.41% | bitget | -2.30% | okx | -71.71% |
| 5 | CAP | +64.42% | bitget | -255.35% | okx | -319.78% |
| 6 | NBIS | +50.28% | bitget | -5.58% | okx | -55.86% |
| 7 | SNDK | +49.25% | bitget | -19.93% | okx | -69.17% |
| 8 | ZIL | +46.16% | bitget | -40.19% | okx | -86.35% |
| 9 | MUU | +45.80% | okx | -19.46% | bitget | -65.26% |
| 10 | CXMT | +45.56% | okx | +69.43% | bitget | +23.87% |
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
