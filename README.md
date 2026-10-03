# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-03 13:34 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1298**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +660.56% |
| 2 | TWLO | okx | +190.58% |
| 3 | NTAP | bitget | +105.89% |
| 4 | AEHR | okx | +97.72% |
| 5 | STONK | bitget | +65.70% |
| 6 | 龙虾 | bitget | +59.90% |
| 7 | MINIMAX | okx | +54.02% |
| 8 | RLS | okx | +48.07% |
| 9 | SPCH | okx | +44.75% |
| 10 | CTR | bitget | +43.80% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | bitget | -1159.06% |
| 2 | SAND | bitget | -626.56% |
| 3 | ARK | bitget | -589.44% |
| 4 | SAND | okx | -418.30% |
| 5 | 2Z | okx | -355.33% |
| 6 | 2Z | bitget | -298.94% |
| 7 | MANA | okx | -192.33% |
| 8 | MANA | bitget | -135.67% |
| 9 | ENJ | okx | -116.35% |
| 10 | ENJ | bitget | -107.20% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +1164.53% | okx | +5.47% | bitget | -1159.06% |
| 2 | H100 | +660.56% | okx | +660.56% | bitget | +0.00% |
| 3 | SAND | +208.26% | okx | -418.30% | bitget | -626.56% |
| 4 | TWLO | +190.58% | okx | +190.58% | bitget | +0.00% |
| 5 | AEHR | +97.72% | okx | +97.72% | bitget | +0.00% |
| 6 | MANA | +56.66% | bitget | -135.67% | okx | -192.33% |
| 7 | 2Z | +56.39% | bitget | -298.94% | okx | -355.33% |
| 8 | MINIMAX | +54.02% | okx | +54.02% | bitget | +0.00% |
| 9 | ENS | +46.03% | bitget | +10.95% | okx | -35.08% |
| 10 | SPCH | +44.75% | okx | +44.75% | bitget | +0.00% |
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
