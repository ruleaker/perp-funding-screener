# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-15 01:55 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1185**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LGELECTRONICS | bitget | +129.54% |
| 2 | URNM | okx | +84.83% |
| 3 | SIREN | bitget | +75.77% |
| 4 | SKYAI | bitget | +73.04% |
| 5 | ARIA | bitget | +72.93% |
| 6 | RAM | okx | +70.79% |
| 7 | UNITAS | bitget | +65.81% |
| 8 | ESPORTS | bitget | +65.04% |
| 9 | LAB | okx | +61.16% |
| 10 | LAB | bitget | +60.77% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CAP | okx | -1095.00% |
| 2 | CAP | bitget | -1030.94% |
| 3 | HOME | bitget | -810.52% |
| 4 | BICO | okx | -766.79% |
| 5 | HOME | okx | -765.19% |
| 6 | BICO | bitget | -633.35% |
| 7 | ALICE | bitget | -626.34% |
| 8 | PROM | bitget | -406.79% |
| 9 | 2Z | okx | -217.88% |
| 10 | 2Z | bitget | -202.47% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BICO | +133.44% | bitget | -633.35% | okx | -766.79% |
| 2 | RAM | +70.79% | okx | +70.79% | bitget | +0.00% |
| 3 | SKUU | +69.18% | bitget | -43.69% | okx | -112.87% |
| 4 | CAP | +64.06% | bitget | -1030.94% | okx | -1095.00% |
| 5 | BE | +60.75% | okx | +60.75% | bitget | +0.00% |
| 6 | NBIS | +46.72% | bitget | +0.00% | okx | -46.72% |
| 7 | FWDI | +46.15% | bitget | +0.00% | okx | -46.15% |
| 8 | SNXX | +45.69% | bitget | -15.99% | okx | -61.68% |
| 9 | HOME | +45.33% | okx | -765.19% | bitget | -810.52% |
| 10 | GLM | +45.07% | okx | -5.74% | bitget | -50.81% |
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
