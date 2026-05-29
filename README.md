# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-05-29 19:06 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **909**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AAOI | okx | +412.06% |
| 2 | IBM | okx | +388.20% |
| 3 | GLW | okx | +350.34% |
| 4 | NOK | okx | +305.05% |
| 5 | DELL | okx | +293.72% |
| 6 | COHR | okx | +264.65% |
| 7 | INX | bitget | +244.40% |
| 8 | NBIS | okx | +200.71% |
| 9 | HMSTR | okx | +170.95% |
| 10 | INFQ | okx | +164.57% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GENIUS | bitget | -230.39% |
| 2 | ID | bitget | -198.74% |
| 3 | HOME | okx | -141.57% |
| 4 | LAB | okx | -138.81% |
| 5 | DRIFT | bitget | -105.89% |
| 6 | CTR | bitget | -74.46% |
| 7 | HOME | bitget | -67.23% |
| 8 | AI | okx | -63.46% |
| 9 | STORJ | bitget | -59.46% |
| 10 | COMP | bitget | -57.05% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | AAOI | +302.56% | okx | +412.06% | bitget | +109.50% |
| 2 | DELL | +293.72% | okx | +293.72% | bitget | +0.00% |
| 3 | COHR | +264.65% | okx | +264.65% | bitget | +0.00% |
| 4 | INFQ | +164.57% | okx | +164.57% | bitget | +0.00% |
| 5 | NBIS | +158.44% | okx | +200.71% | bitget | +42.27% |
| 6 | LITE | +116.62% | okx | +116.62% | bitget | +0.00% |
| 7 | LAB | +110.45% | bitget | -28.36% | okx | -138.81% |
| 8 | HOME | +74.34% | bitget | -67.23% | okx | -141.57% |
| 9 | BSB | +60.46% | bitget | +5.47% | okx | -54.98% |
| 10 | XPD | +59.08% | okx | +59.08% | bitget | +0.00% |
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
