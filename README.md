# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-04 03:46 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1161**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | bitget | +231.70% |
| 2 | SKHYNIX | okx | +184.33% |
| 3 | KR200 | okx | +159.12% |
| 4 | MINIMAX | bitget | +143.44% |
| 5 | SKHYNIX | bitget | +106.43% |
| 6 | RAM | okx | +79.61% |
| 7 | TRUTH | okx | +69.26% |
| 8 | GRIFFAIN | bitget | +68.77% |
| 9 | MINIMAX | okx | +55.63% |
| 10 | ARC | bitget | +49.06% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | WAXP | bitget | -929.33% |
| 2 | KIOXIA | bitget | -470.96% |
| 3 | FWDI | okx | -334.05% |
| 4 | SNXX | okx | -285.49% |
| 5 | KOPN | bitget | -207.72% |
| 6 | VANRY | bitget | -176.73% |
| 7 | BANK | bitget | -174.21% |
| 8 | KORU | bitget | -159.76% |
| 9 | MIRA | bitget | -129.76% |
| 10 | SYN | bitget | -129.43% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | FWDI | +565.75% | bitget | +231.70% | okx | -334.05% |
| 2 | KIOXIA | +375.54% | okx | -95.42% | bitget | -470.96% |
| 3 | SNXX | +190.12% | bitget | -95.37% | okx | -285.49% |
| 4 | KORU | +159.76% | okx | +0.00% | bitget | -159.76% |
| 5 | RAM | +118.26% | okx | +79.61% | bitget | -38.65% |
| 6 | BICO | +106.96% | bitget | -17.30% | okx | -124.26% |
| 7 | MINIMAX | +87.82% | bitget | +143.44% | okx | +55.63% |
| 8 | SKHYNIX | +77.89% | okx | +184.33% | bitget | +106.43% |
| 9 | VANA | +56.83% | okx | +5.47% | bitget | -51.36% |
| 10 | ZIL | +56.00% | bitget | -36.57% | okx | -92.58% |
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
