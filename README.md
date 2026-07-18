# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-18 03:40 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1118**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | APR | bitget | +130.20% |
| 2 | BANK | bitget | +116.95% |
| 3 | SAMSUNG | okx | +84.08% |
| 4 | 龙虾 | bitget | +82.89% |
| 5 | LYN | bitget | +73.69% |
| 6 | XMR | bitget | +71.83% |
| 7 | SIREN | bitget | +66.14% |
| 8 | ESPORTS | bitget | +64.61% |
| 9 | EWY | okx | +47.82% |
| 10 | MSTR | okx | +44.19% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -1323.20% |
| 2 | HOME | okx | -628.49% |
| 3 | SPELL | bitget | -443.80% |
| 4 | TOSHI | bitget | -275.83% |
| 5 | T | bitget | -244.95% |
| 6 | LRC | okx | -200.71% |
| 7 | GWEI | bitget | -160.31% |
| 8 | DATA | bitget | -158.23% |
| 9 | FLOCK | bitget | -149.47% |
| 10 | DATA | okx | -141.04% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HOME | +694.71% | okx | -628.49% | bitget | -1323.20% |
| 2 | APR | +124.72% | bitget | +130.20% | okx | +5.47% |
| 3 | SLX | +91.74% | okx | -11.41% | bitget | -103.15% |
| 4 | SAMSUNG | +84.08% | okx | +84.08% | bitget | +0.00% |
| 5 | PROS | +72.13% | bitget | -4.93% | okx | -77.05% |
| 6 | TSEM | +71.16% | bitget | +0.00% | okx | -71.16% |
| 7 | BICO | +51.14% | okx | +10.95% | bitget | -40.19% |
| 8 | ALGO | +49.89% | bitget | +10.95% | okx | -38.94% |
| 9 | ESP | +49.09% | bitget | +5.47% | okx | -43.62% |
| 10 | EWY | +47.82% | okx | +47.82% | bitget | +0.00% |
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
