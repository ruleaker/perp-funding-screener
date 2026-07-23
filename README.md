# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-23 03:52 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | bitget | +104.90% |
| 2 | SKHYNIX | bitget | +103.81% |
| 3 | SAMSUNG | bitget | +96.25% |
| 4 | EPIC | bitget | +86.72% |
| 5 | MINIMAX | bitget | +63.62% |
| 6 | SAMSUNG | okx | +59.88% |
| 7 | WET | bitget | +56.06% |
| 8 | MINIMAX | okx | +52.66% |
| 9 | SNXX | okx | +49.23% |
| 10 | POWER | bitget | +46.43% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | DEXE | bitget | -1154.02% |
| 2 | MIRA | bitget | -800.12% |
| 3 | O | okx | -718.66% |
| 4 | O | bitget | -647.36% |
| 5 | ERA | bitget | -372.08% |
| 6 | PROS | okx | -298.01% |
| 7 | PROS | bitget | -252.29% |
| 8 | TLM | bitget | -210.35% |
| 9 | SPELL | bitget | -196.66% |
| 10 | ONE | bitget | -152.86% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +94.37% | okx | -58.49% | bitget | -152.86% |
| 2 | RDW | +83.36% | bitget | +0.00% | okx | -83.36% |
| 3 | SKHYNIX | +78.86% | bitget | +103.81% | okx | +24.94% |
| 4 | O | +71.29% | bitget | -647.36% | okx | -718.66% |
| 5 | BSP | +60.63% | bitget | +0.00% | okx | -60.63% |
| 6 | MUBARAK | +50.78% | okx | -11.85% | bitget | -62.63% |
| 7 | WET | +50.59% | bitget | +56.06% | okx | +5.47% |
| 8 | SNXX | +49.23% | okx | +49.23% | bitget | +0.00% |
| 9 | PROS | +45.72% | bitget | -252.29% | okx | -298.01% |
| 10 | RAY | +45.14% | bitget | +5.47% | okx | -39.67% |
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
