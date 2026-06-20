# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-20 17:53 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1021**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BTW | bitget | +352.92% |
| 2 | SIREN | bitget | +236.41% |
| 3 | SKHYNIX | okx | +209.45% |
| 4 | 龙虾 | bitget | +137.64% |
| 5 | SMH | okx | +108.44% |
| 6 | ESPORTS | bitget | +91.54% |
| 7 | MSTR | okx | +74.47% |
| 8 | US | bitget | +73.91% |
| 9 | 4 | bitget | +67.45% |
| 10 | O | okx | +64.08% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H | bitget | -639.15% |
| 2 | H | okx | -401.28% |
| 3 | HOME | okx | -294.33% |
| 4 | BICO | okx | -238.90% |
| 5 | FIDA | bitget | -223.49% |
| 6 | RE | bitget | -174.21% |
| 7 | ALICE | bitget | -144.43% |
| 8 | CHIP | okx | -98.94% |
| 9 | VANRY | bitget | -95.16% |
| 10 | MANA | bitget | -88.91% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BICO | +249.85% | bitget | +10.95% | okx | -238.90% |
| 2 | H | +237.88% | okx | -401.28% | bitget | -639.15% |
| 3 | HOME | +223.38% | bitget | -70.96% | okx | -294.33% |
| 4 | SKHYNIX | +209.45% | okx | +209.45% | bitget | +0.00% |
| 5 | RE | +155.72% | okx | -18.49% | bitget | -174.21% |
| 6 | SMH | +108.44% | okx | +108.44% | bitget | +0.00% |
| 7 | MSTR | +74.47% | okx | +74.47% | bitget | +0.00% |
| 8 | MANA | +62.40% | okx | -26.51% | bitget | -88.91% |
| 9 | SAMSUNG | +48.68% | okx | +48.68% | bitget | +0.00% |
| 10 | LITE | +44.81% | bitget | +0.00% | okx | -44.81% |
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
