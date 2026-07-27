# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-27 04:11 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +340.23% |
| 2 | SAMSUNG | okx | +227.99% |
| 3 | SKHYNIX | bitget | +223.05% |
| 4 | 1MCHEEMS | bitget | +160.64% |
| 5 | SAMSUNG | bitget | +153.19% |
| 6 | RAM | okx | +119.06% |
| 7 | XPD | okx | +87.94% |
| 8 | HYUNDAI | bitget | +79.39% |
| 9 | HYUNDAI | okx | +78.47% |
| 10 | XPD | bitget | +58.14% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | VANRY | bitget | -926.04% |
| 2 | EUL | bitget | -493.52% |
| 3 | HOT | bitget | -327.62% |
| 4 | T | bitget | -325.54% |
| 5 | PENG | okx | -282.39% |
| 6 | TLM | bitget | -281.52% |
| 7 | MIRA | bitget | -157.68% |
| 8 | ESP | bitget | -138.19% |
| 9 | ZIL | bitget | -126.25% |
| 10 | SOXS | okx | -120.61% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | PENG | +282.39% | bitget | +0.00% | okx | -282.39% |
| 2 | SOXS | +120.61% | bitget | +0.00% | okx | -120.61% |
| 3 | RAM | +119.06% | okx | +119.06% | bitget | +0.00% |
| 4 | SKHYNIX | +117.18% | okx | +340.23% | bitget | +223.05% |
| 5 | SHAZ | +111.35% | bitget | +0.00% | okx | -111.35% |
| 6 | IRYS | +109.64% | bitget | -4.05% | okx | -113.69% |
| 7 | ZIL | +108.69% | okx | -17.56% | bitget | -126.25% |
| 8 | KORU | +92.53% | okx | +0.00% | bitget | -92.53% |
| 9 | SAMSUNG | +74.80% | okx | +227.99% | bitget | +153.19% |
| 10 | VRT | +53.61% | okx | +53.61% | bitget | +0.00% |
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
