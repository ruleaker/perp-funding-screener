# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-17 12:34 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1009**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SIREN | bitget | +352.81% |
| 2 | US | bitget | +195.90% |
| 3 | BB | okx | +135.18% |
| 4 | INX | bitget | +111.25% |
| 5 | KOPN | bitget | +109.50% |
| 6 | EWT | bitget | +109.50% |
| 7 | ZEST | bitget | +99.64% |
| 8 | ACU | bitget | +88.26% |
| 9 | QNT | okx | +85.87% |
| 10 | ESPORTS | bitget | +81.69% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ID | bitget | -726.20% |
| 2 | H | okx | -405.51% |
| 3 | ORCA | bitget | -315.14% |
| 4 | HOME | okx | -230.76% |
| 5 | SPELL | bitget | -167.43% |
| 6 | SPACE | bitget | -149.14% |
| 7 | 龙虾 | bitget | -134.90% |
| 8 | SAHARA | okx | -124.49% |
| 9 | HOME | bitget | -110.27% |
| 10 | SOXS | bitget | -109.50% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +410.98% | bitget | +5.47% | okx | -405.51% |
| 2 | BB | +129.70% | okx | +135.18% | bitget | +5.47% |
| 3 | HOME | +120.50% | bitget | -110.27% | okx | -230.76% |
| 4 | EWT | +109.50% | bitget | +109.50% | okx | +0.00% |
| 5 | QNT | +98.02% | okx | +85.87% | bitget | -12.15% |
| 6 | HYUNDAI | +87.25% | bitget | +0.00% | okx | -87.25% |
| 7 | ACU | +82.78% | bitget | +88.26% | okx | +5.47% |
| 8 | SPACE | +74.54% | okx | -74.60% | bitget | -149.14% |
| 9 | BEAT | +67.33% | okx | -9.43% | bitget | -76.76% |
| 10 | LAB | +60.71% | bitget | +71.94% | okx | +11.23% |
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
