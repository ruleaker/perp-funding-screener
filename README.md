# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-22 19:52 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1033**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | USO | okx | +193.94% |
| 2 | SPCX | okx | +164.82% |
| 3 | SIREN | bitget | +129.87% |
| 4 | INX | bitget | +110.38% |
| 5 | QNTSTOCK | bitget | +109.50% |
| 6 | SPCX | bitget | +83.11% |
| 7 | GOOGL | okx | +80.54% |
| 8 | GRAM | bitget | +73.91% |
| 9 | US | bitget | +62.85% |
| 10 | 龙虾 | bitget | +60.12% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FIDA | bitget | -1694.62% |
| 2 | RE | okx | -1086.01% |
| 3 | SYN | bitget | -931.30% |
| 4 | RE | bitget | -808.22% |
| 5 | ARX | okx | -441.12% |
| 6 | H | bitget | -363.65% |
| 7 | TAIKO | bitget | -340.00% |
| 8 | H | okx | -275.21% |
| 9 | LAYER | bitget | -271.45% |
| 10 | LAYER | okx | -182.92% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ARX | +297.56% | bitget | -143.55% | okx | -441.12% |
| 2 | RE | +277.79% | bitget | -808.22% | okx | -1086.01% |
| 3 | BAT | +103.37% | okx | +10.95% | bitget | -92.42% |
| 4 | BICO | +95.27% | okx | +10.95% | bitget | -84.31% |
| 5 | LAYER | +88.53% | okx | -182.92% | bitget | -271.45% |
| 6 | H | +88.44% | okx | -275.21% | bitget | -363.65% |
| 7 | SPCX | +81.71% | okx | +164.82% | bitget | +83.11% |
| 8 | HOME | +73.06% | bitget | -30.00% | okx | -103.07% |
| 9 | BREV | +65.40% | bitget | -2.74% | okx | -68.14% |
| 10 | GRAM | +60.67% | bitget | +73.91% | okx | +13.25% |
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
