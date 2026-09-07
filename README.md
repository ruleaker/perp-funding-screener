# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-07 20:04 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1238**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KORU | okx | +253.77% |
| 2 | ONE | bitget | +148.04% |
| 3 | SOFTBANK | okx | +95.41% |
| 4 | PIPPIN | bitget | +91.98% |
| 5 | XCU | okx | +81.50% |
| 6 | ESPORTS | bitget | +63.95% |
| 7 | PONS | okx | +62.48% |
| 8 | XPD | okx | +60.50% |
| 9 | ZEST | bitget | +55.84% |
| 10 | INTC | okx | +55.42% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -1005.65% |
| 2 | KR200 | okx | -183.42% |
| 3 | T | bitget | -168.30% |
| 4 | ORCA | bitget | -132.82% |
| 5 | PURR | bitget | -105.56% |
| 6 | MINA | bitget | -92.53% |
| 7 | LA | bitget | -85.08% |
| 8 | ONG | bitget | -74.24% |
| 9 | LA | okx | -72.04% |
| 10 | CFG | bitget | -60.44% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KORU | +208.00% | okx | +253.77% | bitget | +45.77% |
| 2 | KR200 | +183.42% | bitget | +0.00% | okx | -183.42% |
| 3 | ONE | +142.57% | bitget | +148.04% | okx | +5.47% |
| 4 | PURR | +105.56% | okx | +0.00% | bitget | -105.56% |
| 5 | PIPPIN | +66.91% | bitget | +91.98% | okx | +25.07% |
| 6 | XPD | +60.50% | okx | +60.50% | bitget | +0.00% |
| 7 | INTC | +55.42% | okx | +55.42% | bitget | +0.00% |
| 8 | SOFTBANK | +55.23% | okx | +95.41% | bitget | +40.19% |
| 9 | AXTI | +50.91% | okx | +50.91% | bitget | +0.00% |
| 10 | MINA | +42.45% | okx | -50.08% | bitget | -92.53% |
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
