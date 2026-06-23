# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-23 11:37 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1037**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOXS | bitget | +547.50% |
| 2 | OSS | bitget | +547.50% |
| 3 | LRCX | okx | +537.15% |
| 4 | SKHYNIX | okx | +317.40% |
| 5 | VRT | okx | +229.19% |
| 6 | SAMSUNG | okx | +220.88% |
| 7 | HYUNDAI | okx | +215.45% |
| 8 | RDW | okx | +167.07% |
| 9 | SIREN | bitget | +151.22% |
| 10 | TTMI | okx | +141.83% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ARX | okx | -708.27% |
| 2 | FIDA | bitget | -652.95% |
| 3 | LAYER | bitget | -580.46% |
| 4 | MTL | bitget | -570.17% |
| 5 | FLY | bitget | -547.50% |
| 6 | AMC | bitget | -547.50% |
| 7 | NTAP | bitget | -489.03% |
| 8 | ARX | bitget | -425.74% |
| 9 | LAYER | okx | -322.90% |
| 10 | SHLD | okx | -322.70% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LRCX | +537.15% | okx | +537.15% | bitget | +0.00% |
| 2 | SKHYNIX | +317.40% | okx | +317.40% | bitget | +0.00% |
| 3 | ARX | +282.53% | bitget | -425.74% | okx | -708.27% |
| 4 | LAYER | +257.56% | okx | -322.90% | bitget | -580.46% |
| 5 | VRT | +229.19% | okx | +229.19% | bitget | +0.00% |
| 6 | SAMSUNG | +220.88% | okx | +220.88% | bitget | +0.00% |
| 7 | HYUNDAI | +215.45% | okx | +215.45% | bitget | +0.00% |
| 8 | RDW | +167.07% | okx | +167.07% | bitget | +0.00% |
| 9 | BX | +133.84% | okx | -41.90% | bitget | -175.75% |
| 10 | IOST | +103.28% | bitget | +10.95% | okx | -92.33% |
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
