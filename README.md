# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-29 13:54 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1208**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TRUTH | okx | +76.08% |
| 2 | ONE | okx | +73.39% |
| 3 | BTW | bitget | +72.16% |
| 4 | ESPORTS | bitget | +62.96% |
| 5 | BEAT | bitget | +45.66% |
| 6 | LYN | bitget | +44.13% |
| 7 | RLS | okx | +42.10% |
| 8 | ARIA | bitget | +39.53% |
| 9 | 龙虾 | bitget | +39.31% |
| 10 | XMR | bitget | +38.98% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TUT | bitget | -1436.42% |
| 2 | SAND | bitget | -652.84% |
| 3 | ONT | bitget | -184.18% |
| 4 | SAND | okx | -153.82% |
| 5 | ONG | bitget | -143.23% |
| 6 | ONT | okx | -140.04% |
| 7 | HOME | bitget | -106.00% |
| 8 | RVN | okx | -102.35% |
| 9 | HOME | okx | -101.28% |
| 10 | ACE | bitget | -80.48% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SAND | +499.02% | okx | -153.82% | bitget | -652.84% |
| 2 | RVN | +107.82% | bitget | +5.47% | okx | -102.35% |
| 3 | ONE | +62.44% | okx | +73.39% | bitget | +10.95% |
| 4 | ONT | +44.14% | okx | -140.04% | bitget | -184.18% |
| 5 | ALGO | +42.52% | bitget | +8.65% | okx | -33.87% |
| 6 | BREV | +42.49% | okx | +5.47% | bitget | -37.01% |
| 7 | GRVT | +41.66% | bitget | +2.41% | okx | -39.25% |
| 8 | BEAT | +37.80% | bitget | +45.66% | okx | +7.86% |
| 9 | AAOI | +36.63% | bitget | +0.00% | okx | -36.63% |
| 10 | PIPPIN | +30.07% | bitget | +38.22% | okx | +8.15% |
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
