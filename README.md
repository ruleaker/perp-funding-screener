# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-07 10:39 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **951**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MSTR | okx | +156.79% |
| 2 | QNT | okx | +152.47% |
| 3 | BMNR | okx | +148.26% |
| 4 | NOK | okx | +134.78% |
| 5 | FOLKS | bitget | +95.48% |
| 6 | SAHARA | bitget | +89.57% |
| 7 | SIREN | bitget | +88.48% |
| 8 | LITE | okx | +72.47% |
| 9 | ESPORTS | bitget | +65.15% |
| 10 | ZBT | bitget | +63.73% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -840.19% |
| 2 | HOME | okx | -786.17% |
| 3 | EDEN | okx | -763.88% |
| 4 | FIDA | bitget | -487.60% |
| 5 | GUN | bitget | -332.66% |
| 6 | INX | bitget | -208.71% |
| 7 | STABLE | okx | -133.19% |
| 8 | STABLE | bitget | -124.06% |
| 9 | PROS | okx | -112.25% |
| 10 | PROS | bitget | -105.12% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | MSTR | +156.79% | okx | +156.79% | bitget | +0.00% |
| 2 | QNT | +141.52% | okx | +152.47% | bitget | +10.95% |
| 3 | LDO | +85.63% | okx | -16.54% | bitget | -102.16% |
| 4 | LITE | +72.47% | okx | +72.47% | bitget | +0.00% |
| 5 | SAHARA | +64.10% | bitget | +89.57% | okx | +25.47% |
| 6 | ZBT | +58.25% | bitget | +63.73% | okx | +5.47% |
| 7 | CRCL | +55.68% | okx | +55.68% | bitget | +0.00% |
| 8 | GLM | +54.42% | okx | +5.47% | bitget | -48.95% |
| 9 | HOME | +54.03% | okx | -786.17% | bitget | -840.19% |
| 10 | BABY | +52.39% | bitget | -39.09% | okx | -91.48% |
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
