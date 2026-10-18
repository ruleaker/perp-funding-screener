# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-18 04:52 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1328**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | PURR | okx | +236.36% |
| 2 | GWEI | bitget | +113.55% |
| 3 | KORU | okx | +78.49% |
| 4 | MSTU | bitget | +41.61% |
| 5 | CRCL | okx | +39.78% |
| 6 | SECZ | bitget | +38.54% |
| 7 | NVDL | okx | +35.67% |
| 8 | MUU | bitget | +31.65% |
| 9 | ARC | bitget | +30.11% |
| 10 | AKE | bitget | +27.38% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAND | bitget | -1213.48% |
| 2 | SAND | okx | -871.03% |
| 3 | H100 | okx | -408.05% |
| 4 | Q | bitget | -189.76% |
| 5 | POPMART | okx | -176.49% |
| 6 | ERA | bitget | -175.97% |
| 7 | RSR | bitget | -161.29% |
| 8 | PROS | bitget | -132.49% |
| 9 | BLUR | okx | -128.55% |
| 10 | DNA | okx | -121.98% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +408.05% | bitget | +0.00% | okx | -408.05% |
| 2 | SAND | +342.45% | okx | -871.03% | bitget | -1213.48% |
| 3 | PURR | +236.36% | okx | +236.36% | bitget | +0.00% |
| 4 | PROS | +137.97% | okx | +5.47% | bitget | -132.49% |
| 5 | POPMART | +89.77% | bitget | -86.72% | okx | -176.49% |
| 6 | GMT | +84.53% | okx | +5.47% | bitget | -79.06% |
| 7 | RSR | +69.50% | okx | -91.79% | bitget | -161.29% |
| 8 | 1INCH | +57.20% | bitget | +10.95% | okx | -46.25% |
| 9 | KORU | +56.59% | okx | +78.49% | bitget | +21.90% |
| 10 | BLUR | +49.05% | bitget | -79.50% | okx | -128.55% |
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
