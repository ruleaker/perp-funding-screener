# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-08 18:41 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **967**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | XPD | okx | +148.90% |
| 2 | BEAT | bitget | +124.50% |
| 3 | FOLKS | bitget | +120.23% |
| 4 | POWER | bitget | +115.52% |
| 5 | SAHARA | bitget | +105.89% |
| 6 | NG | okx | +105.61% |
| 7 | XPT | okx | +100.81% |
| 8 | XPD | bitget | +90.56% |
| 9 | BEAT | okx | +81.45% |
| 10 | LAB | bitget | +80.48% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAYER | okx | -1037.40% |
| 2 | ESPORTS | bitget | -1033.68% |
| 3 | LAYER | bitget | -928.67% |
| 4 | HOME | bitget | -390.37% |
| 5 | HOME | okx | -389.35% |
| 6 | H | bitget | -214.40% |
| 7 | H | okx | -125.37% |
| 8 | STABLE | okx | -124.56% |
| 9 | SLX | bitget | -99.10% |
| 10 | NMR | bitget | -94.39% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LAYER | +108.73% | bitget | -928.67% | okx | -1037.40% |
| 2 | SLX | +104.57% | okx | +5.47% | bitget | -99.10% |
| 3 | H | +89.03% | okx | -125.37% | bitget | -214.40% |
| 4 | SAHARA | +82.54% | bitget | +105.89% | okx | +23.34% |
| 5 | NMR | +70.81% | okx | -23.58% | bitget | -94.39% |
| 6 | GOOGL | +66.95% | bitget | +73.80% | okx | +6.85% |
| 7 | STABLE | +66.19% | bitget | -58.36% | okx | -124.56% |
| 8 | SENT | +62.47% | bitget | +5.47% | okx | -56.99% |
| 9 | XPD | +58.34% | okx | +148.90% | bitget | +90.56% |
| 10 | LAB | +57.58% | bitget | +80.48% | okx | +22.90% |
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
