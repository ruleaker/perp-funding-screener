# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-23 16:49 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1197**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FIGHT | bitget | +190.64% |
| 2 | 龙虾 | bitget | +149.69% |
| 3 | SSPC | bitget | +98.11% |
| 4 | ONE | bitget | +84.53% |
| 5 | ZHIPU | okx | +75.14% |
| 6 | ESPORTS | bitget | +74.46% |
| 7 | SNXX | okx | +72.57% |
| 8 | SIREN | bitget | +66.03% |
| 9 | SNDK | okx | +62.95% |
| 10 | BEAT | okx | +54.47% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -292.15% |
| 2 | BICO | bitget | -190.31% |
| 3 | UNITREE | okx | -152.23% |
| 4 | RVN | okx | -150.56% |
| 5 | HOME | bitget | -110.05% |
| 6 | MOVE | okx | -108.74% |
| 7 | MOVE | bitget | -100.52% |
| 8 | HOME | okx | -97.56% |
| 9 | COTI | bitget | -92.53% |
| 10 | EPIC | bitget | -83.33% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | UNITREE | +152.23% | bitget | +0.00% | okx | -152.23% |
| 2 | RVN | +143.88% | bitget | -6.68% | okx | -150.56% |
| 3 | BICO | +112.47% | okx | -77.84% | bitget | -190.31% |
| 4 | SNDK | +62.95% | okx | +62.95% | bitget | +0.00% |
| 5 | STX | +54.49% | bitget | +1.10% | okx | -53.39% |
| 6 | SNXX | +53.51% | okx | +72.57% | bitget | +19.05% |
| 7 | SKHY | +49.14% | okx | +49.14% | bitget | +0.00% |
| 8 | USAR | +48.38% | okx | +48.38% | bitget | +0.00% |
| 9 | ZHIPU | +47.66% | okx | +75.14% | bitget | +27.48% |
| 10 | CRCL | +41.52% | okx | +41.52% | bitget | +0.00% |
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
