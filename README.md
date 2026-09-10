# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-10 12:59 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1250**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KR200 | okx | +594.74% |
| 2 | NG | okx | +415.97% |
| 3 | PEP | bitget | +210.46% |
| 4 | NATGAS | bitget | +204.11% |
| 5 | RDDT | bitget | +194.80% |
| 6 | ETN | bitget | +151.88% |
| 7 | GPRO | okx | +129.30% |
| 8 | ROK | okx | +111.69% |
| 9 | TEAM | bitget | +94.94% |
| 10 | ONE | okx | +91.67% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | VTHO | bitget | -1812.33% |
| 2 | RVN | okx | -1095.00% |
| 3 | RVN | bitget | -714.71% |
| 4 | IOST | okx | -563.30% |
| 5 | ANIME | okx | -438.91% |
| 6 | ANIME | bitget | -395.51% |
| 7 | NEWT | bitget | -310.87% |
| 8 | REZ | bitget | -301.89% |
| 9 | 牛来 | bitget | -298.72% |
| 10 | USO | okx | -276.96% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KR200 | +598.90% | okx | +594.74% | bitget | -4.16% |
| 2 | RVN | +380.29% | bitget | -714.71% | okx | -1095.00% |
| 3 | IOST | +300.83% | bitget | -262.47% | okx | -563.30% |
| 4 | BSP | +245.28% | bitget | +0.00% | okx | -245.28% |
| 5 | RDDT | +170.44% | bitget | +194.80% | okx | +24.36% |
| 6 | FWDI | +145.89% | bitget | +0.00% | okx | -145.89% |
| 7 | SOPH | +137.28% | bitget | -29.02% | okx | -166.30% |
| 8 | SHAZ | +133.00% | bitget | +0.00% | okx | -133.00% |
| 9 | UNITREE | +125.64% | bitget | +0.00% | okx | -125.64% |
| 10 | ROK | +111.69% | okx | +111.69% | bitget | +0.00% |
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
