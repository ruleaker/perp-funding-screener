# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-02 12:24 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **935**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HPE | okx | +918.56% |
| 2 | NOK | okx | +513.56% |
| 3 | LUNR | okx | +435.74% |
| 4 | MRVL | okx | +369.19% |
| 5 | AAOI | okx | +365.47% |
| 6 | ASTS | okx | +350.63% |
| 7 | NOW | okx | +308.52% |
| 8 | COHR | okx | +296.69% |
| 9 | GLW | okx | +287.63% |
| 10 | INX | bitget | +251.19% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SLX | bitget | -1184.68% |
| 2 | LAB | okx | -1095.00% |
| 3 | SLX | okx | -867.35% |
| 4 | LAB | bitget | -608.71% |
| 5 | HOME | bitget | -546.08% |
| 6 | HOME | okx | -263.34% |
| 7 | SIGN | bitget | -165.89% |
| 8 | SIGN | okx | -160.86% |
| 9 | GUN | bitget | -115.30% |
| 10 | SP500 | bitget | -109.50% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LAB | +486.29% | bitget | -608.71% | okx | -1095.00% |
| 2 | AAOI | +328.24% | okx | +365.47% | bitget | +37.23% |
| 3 | SLX | +317.33% | okx | -867.35% | bitget | -1184.68% |
| 4 | NOW | +308.52% | okx | +308.52% | bitget | +0.00% |
| 5 | ASTS | +305.96% | okx | +350.63% | bitget | +44.68% |
| 6 | HOME | +282.73% | okx | -263.34% | bitget | -546.08% |
| 7 | COHR | +280.48% | okx | +296.69% | bitget | +16.21% |
| 8 | MRVL | +259.69% | okx | +369.19% | bitget | +109.50% |
| 9 | COST | +167.68% | okx | +167.68% | bitget | +0.00% |
| 10 | BB | +126.35% | okx | +131.83% | bitget | +5.47% |
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
