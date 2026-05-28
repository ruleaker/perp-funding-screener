# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-05-28 19:08 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **907**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GLW | okx | +442.03% |
| 2 | IBM | okx | +416.24% |
| 3 | ESPORTS | bitget | +331.02% |
| 4 | GEV | okx | +319.10% |
| 5 | NOK | okx | +286.88% |
| 6 | AAOI | okx | +135.28% |
| 7 | SOXS | bitget | +109.50% |
| 8 | NOKSTOCK | bitget | +109.50% |
| 9 | INX | bitget | +106.76% |
| 10 | AAOI | bitget | +73.91% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | DRIFT | bitget | -137.42% |
| 2 | SP500 | bitget | -109.50% |
| 3 | BEAT | bitget | -95.48% |
| 4 | ALLO | okx | -95.02% |
| 5 | HOME | okx | -91.01% |
| 6 | INJ | bitget | -90.67% |
| 7 | ARPA | bitget | -80.04% |
| 8 | BAT | okx | -77.69% |
| 9 | OP | bitget | -52.12% |
| 10 | JTO | okx | -45.50% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BEAT | +107.49% | okx | +12.00% | bitget | -95.48% |
| 2 | ALLO | +100.50% | bitget | +5.47% | okx | -95.02% |
| 3 | OP | +63.07% | okx | +10.95% | bitget | -52.12% |
| 4 | AAOI | +61.37% | okx | +135.28% | bitget | +73.91% |
| 5 | BAT | +57.43% | bitget | -20.26% | okx | -77.69% |
| 6 | HOME | +50.83% | bitget | -40.19% | okx | -91.01% |
| 7 | OPG | +50.59% | okx | +5.47% | bitget | -45.11% |
| 8 | INJ | +49.78% | okx | -40.89% | bitget | -90.67% |
| 9 | BSB | +45.07% | okx | +50.54% | bitget | +5.47% |
| 10 | LITE | +44.28% | okx | +44.28% | bitget | +0.00% |
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
