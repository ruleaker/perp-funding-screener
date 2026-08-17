# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-17 01:59 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1185**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SHAZ | okx | +408.03% |
| 2 | JNJ | okx | +199.26% |
| 3 | RLS | okx | +187.33% |
| 4 | BRKB | okx | +78.11% |
| 5 | XIAOMI | okx | +73.96% |
| 6 | SIREN | bitget | +73.47% |
| 7 | IDOL | bitget | +66.79% |
| 8 | LYN | bitget | +65.48% |
| 9 | RDW | okx | +65.37% |
| 10 | SAMSUNGEM | bitget | +62.85% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BICO | bitget | -1115.48% |
| 2 | BICO | okx | -700.57% |
| 3 | ACE | bitget | -506.88% |
| 4 | HOME | bitget | -176.84% |
| 5 | HOME | okx | -163.50% |
| 6 | RIOT | okx | -156.30% |
| 7 | COW | bitget | -153.19% |
| 8 | STABLE | bitget | -140.05% |
| 9 | BOT | okx | -99.20% |
| 10 | CAP | okx | -97.60% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BICO | +414.90% | okx | -700.57% | bitget | -1115.48% |
| 2 | SHAZ | +408.03% | okx | +408.03% | bitget | +0.00% |
| 3 | BOT | +99.20% | bitget | +0.00% | okx | -99.20% |
| 4 | BRKB | +78.11% | okx | +78.11% | bitget | +0.00% |
| 5 | XIAOMI | +73.96% | okx | +73.96% | bitget | +0.00% |
| 6 | RAY | +66.97% | okx | +9.49% | bitget | -57.49% |
| 7 | RDW | +65.37% | okx | +65.37% | bitget | +0.00% |
| 8 | SNDK | +57.56% | bitget | +0.00% | okx | -57.56% |
| 9 | STABLE | +56.91% | okx | -83.14% | bitget | -140.05% |
| 10 | THETA | +54.14% | bitget | +10.95% | okx | -43.19% |
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
