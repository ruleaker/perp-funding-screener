# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-24 11:21 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1046**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TWLO | bitget | +547.50% |
| 2 | DRAM | bitget | +310.10% |
| 3 | SATSSTOCK | bitget | +219.88% |
| 4 | TSEM | bitget | +162.83% |
| 5 | SKHYNIX | okx | +155.55% |
| 6 | NOKSTOCK | bitget | +137.53% |
| 7 | AAOI | okx | +127.22% |
| 8 | DRAM | okx | +126.52% |
| 9 | H | okx | +121.95% |
| 10 | HYUNDAI | okx | +110.08% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | bitget | -606.85% |
| 2 | SOXS | bitget | -547.50% |
| 3 | SIMO | bitget | -547.50% |
| 4 | SITM | bitget | -539.62% |
| 5 | ALICE | bitget | -521.55% |
| 6 | LAB | okx | -519.71% |
| 7 | SAHARA | okx | -463.80% |
| 8 | QNT | okx | -294.23% |
| 9 | MUU | bitget | -259.52% |
| 10 | USO | okx | -240.17% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | TWLO | +547.50% | bitget | +547.50% | okx | +0.00% |
| 2 | QNT | +305.18% | bitget | +10.95% | okx | -294.23% |
| 3 | SAHARA | +235.27% | bitget | -228.53% | okx | -463.80% |
| 4 | DRAM | +183.58% | bitget | +310.10% | okx | +126.52% |
| 5 | SKHYNIX | +155.55% | okx | +155.55% | bitget | +0.00% |
| 6 | SMCI | +134.18% | okx | +105.60% | bitget | -28.58% |
| 7 | KORU | +131.02% | bitget | +0.00% | okx | -131.02% |
| 8 | H | +126.22% | okx | +121.95% | bitget | -4.27% |
| 9 | HYUNDAI | +110.08% | okx | +110.08% | bitget | +0.00% |
| 10 | O | +101.02% | okx | -24.03% | bitget | -125.05% |
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
