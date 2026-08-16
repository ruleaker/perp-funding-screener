# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-16 16:48 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1185**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LIGHT | okx | +64.34% |
| 2 | RLS | okx | +58.76% |
| 3 | IDOL | bitget | +57.27% |
| 4 | 1MCHEEMS | bitget | +55.08% |
| 5 | ZEST | bitget | +53.00% |
| 6 | UP | okx | +47.66% |
| 7 | ESPORTS | bitget | +45.44% |
| 8 | AIO | bitget | +42.27% |
| 9 | XIAOMI | okx | +39.82% |
| 10 | RIVER | okx | +38.08% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BICO | bitget | -1072.22% |
| 2 | ACE | bitget | -543.78% |
| 3 | BICO | okx | -515.09% |
| 4 | HOME | bitget | -456.51% |
| 5 | HOME | okx | -404.51% |
| 6 | ALICE | bitget | -194.69% |
| 7 | COW | bitget | -187.35% |
| 8 | WAL | okx | -175.07% |
| 9 | WAL | bitget | -153.08% |
| 10 | STABLE | bitget | -120.56% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BICO | +557.14% | okx | -515.09% | bitget | -1072.22% |
| 2 | ARKM | +74.24% | okx | +10.95% | bitget | -63.29% |
| 3 | RVN | +58.97% | bitget | -61.32% | okx | -120.29% |
| 4 | DOS | +58.40% | bitget | -58.91% | okx | -117.31% |
| 5 | HOME | +51.99% | okx | -404.51% | bitget | -456.51% |
| 6 | SENT | +49.17% | okx | +5.47% | bitget | -43.69% |
| 7 | MOVE | +46.16% | bitget | +5.47% | okx | -40.69% |
| 8 | XIAOMI | +39.82% | okx | +39.82% | bitget | +0.00% |
| 9 | MAGIC | +35.59% | okx | +5.47% | bitget | -30.11% |
| 10 | BABY | +33.35% | bitget | +5.47% | okx | -27.88% |
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
