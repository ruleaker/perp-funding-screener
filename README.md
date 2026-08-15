# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-15 16:47 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1185**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +213.63% |
| 2 | POWER | bitget | +116.84% |
| 3 | ARIA | bitget | +75.23% |
| 4 | ONE | okx | +68.03% |
| 5 | WET | bitget | +58.69% |
| 6 | RAVE | okx | +55.58% |
| 7 | LIGHT | okx | +55.44% |
| 8 | TRUTH | okx | +47.67% |
| 9 | SYRUP | okx | +44.06% |
| 10 | BEAT | okx | +37.91% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -1426.46% |
| 2 | COW | bitget | -1403.35% |
| 3 | WAL | bitget | -763.11% |
| 4 | WAL | okx | -471.22% |
| 5 | HOME | bitget | -357.30% |
| 6 | HOME | okx | -320.17% |
| 7 | ALICE | bitget | -241.34% |
| 8 | GWEI | bitget | -200.49% |
| 9 | RVN | okx | -186.61% |
| 10 | CAP | okx | -185.39% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | WAL | +291.89% | okx | -471.22% | bitget | -763.11% |
| 2 | RVN | +121.79% | bitget | -64.82% | okx | -186.61% |
| 3 | ONE | +117.74% | okx | +68.03% | bitget | -49.71% |
| 4 | AEON | +59.91% | bitget | +5.47% | okx | -54.44% |
| 5 | INJ | +57.23% | bitget | -0.11% | okx | -57.34% |
| 6 | WET | +53.22% | bitget | +58.69% | okx | +5.47% |
| 7 | NEO | +50.10% | bitget | +10.95% | okx | -39.15% |
| 8 | GALA | +40.59% | bitget | +10.95% | okx | -29.64% |
| 9 | SYRUP | +38.59% | okx | +44.06% | bitget | +5.47% |
| 10 | HOME | +37.13% | okx | -320.17% | bitget | -357.30% |
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
