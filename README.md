# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-05 18:28 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1235**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | PONS | okx | +276.78% |
| 2 | ONE | bitget | +206.74% |
| 3 | ESPORTS | bitget | +197.76% |
| 4 | PONS | bitget | +130.85% |
| 5 | HOOD | okx | +107.62% |
| 6 | USELESS | bitget | +98.77% |
| 7 | BSB | okx | +97.87% |
| 8 | CP | okx | +80.02% |
| 9 | GPRO | okx | +63.60% |
| 10 | USELESS | okx | +59.25% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -311.75% |
| 2 | CAP | okx | -223.27% |
| 3 | CAP | bitget | -220.75% |
| 4 | LA | okx | -198.77% |
| 5 | LA | bitget | -172.57% |
| 6 | FLOCK | bitget | -90.89% |
| 7 | ONG | bitget | -87.05% |
| 8 | RVN | okx | -59.41% |
| 9 | COTI | bitget | -55.41% |
| 10 | TWLO | okx | -43.08% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +188.58% | bitget | +206.74% | okx | +18.16% |
| 2 | PONS | +145.92% | okx | +276.78% | bitget | +130.85% |
| 3 | HOOD | +107.62% | okx | +107.62% | bitget | +0.00% |
| 4 | BSB | +88.67% | okx | +97.87% | bitget | +9.20% |
| 5 | GPRO | +63.60% | okx | +63.60% | bitget | +0.00% |
| 6 | CP | +47.71% | okx | +80.02% | bitget | +32.30% |
| 7 | MSTR | +46.08% | okx | +46.08% | bitget | +0.00% |
| 8 | TWLO | +43.08% | bitget | +0.00% | okx | -43.08% |
| 9 | USELESS | +39.52% | bitget | +98.77% | okx | +59.25% |
| 10 | RVN | +34.77% | bitget | -24.64% | okx | -59.41% |
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
