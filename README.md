# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-30 13:53 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1209**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 牛来 | bitget | +166.33% |
| 2 | ESPORTS | bitget | +95.27% |
| 3 | ARIA | bitget | +93.51% |
| 4 | TRUTH | okx | +70.93% |
| 5 | LYN | bitget | +63.40% |
| 6 | XMR | bitget | +60.01% |
| 7 | CRCL | okx | +48.22% |
| 8 | MINIMAX | okx | +44.96% |
| 9 | MSTR | okx | +44.93% |
| 10 | POWER | bitget | +40.52% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TUT | bitget | -1229.58% |
| 2 | SKR | bitget | -652.29% |
| 3 | ZKC | bitget | -348.98% |
| 4 | ZKP | okx | -304.91% |
| 5 | ZKP | bitget | -250.75% |
| 6 | BICO | bitget | -250.54% |
| 7 | SAND | okx | -161.25% |
| 8 | BICO | okx | -134.49% |
| 9 | ACE | bitget | -109.50% |
| 10 | RVN | okx | -101.17% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SAND | +172.20% | bitget | +10.95% | okx | -161.25% |
| 2 | BICO | +116.05% | okx | -134.49% | bitget | -250.54% |
| 3 | RVN | +88.14% | bitget | -13.03% | okx | -101.17% |
| 4 | EGLD | +54.60% | bitget | +10.95% | okx | -43.65% |
| 5 | ZKP | +54.16% | bitget | -250.75% | okx | -304.91% |
| 6 | ZORA | +52.33% | bitget | +3.61% | okx | -48.72% |
| 7 | AUCTION | +52.04% | bitget | -9.96% | okx | -62.01% |
| 8 | CRCL | +48.22% | okx | +48.22% | bitget | +0.00% |
| 9 | MINIMAX | +44.96% | okx | +44.96% | bitget | +0.00% |
| 10 | MSTR | +44.93% | okx | +44.93% | bitget | +0.00% |
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
