# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-31 06:01 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1385**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AKE | bitget | +403.95% |
| 2 | DGAI | okx | +77.50% |
| 3 | US100 | okx | +53.51% |
| 4 | ECHO | bitget | +49.17% |
| 5 | MU | okx | +46.21% |
| 6 | ZEST | bitget | +45.55% |
| 7 | ARIA | bitget | +43.03% |
| 8 | APR | okx | +39.41% |
| 9 | FIGHT | bitget | +37.12% |
| 10 | AAOI | okx | +35.49% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | WET | okx | -725.21% |
| 2 | LSK | bitget | -705.51% |
| 3 | WET | bitget | -681.97% |
| 4 | SOPH | bitget | -449.72% |
| 5 | NIL | bitget | -346.57% |
| 6 | BLUR | bitget | -312.07% |
| 7 | TRX | okx | -264.76% |
| 8 | BLUR | okx | -157.99% |
| 9 | Q | bitget | -130.63% |
| 10 | BTW | bitget | -129.87% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | AKE | +398.47% | bitget | +403.95% | okx | +5.47% |
| 2 | SOPH | +387.15% | okx | -62.56% | bitget | -449.72% |
| 3 | TRX | +249.32% | bitget | -15.44% | okx | -264.76% |
| 4 | BLUR | +154.09% | okx | -157.99% | bitget | -312.07% |
| 5 | BTW | +116.58% | okx | -13.29% | bitget | -129.87% |
| 6 | BX | +101.49% | bitget | +0.00% | okx | -101.49% |
| 7 | H100 | +81.52% | bitget | +5.47% | okx | -76.04% |
| 8 | DGAI | +72.02% | okx | +77.50% | bitget | +5.47% |
| 9 | CELO | +65.29% | bitget | +9.42% | okx | -55.87% |
| 10 | SAND | +51.45% | okx | -34.50% | bitget | -85.96% |
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
