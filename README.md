# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-01 13:35 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1212**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TMF | okx | +129.77% |
| 2 | VST | bitget | +127.13% |
| 3 | KIOXIA | okx | +121.15% |
| 4 | M | bitget | +92.97% |
| 5 | NOK | okx | +82.82% |
| 6 | QNT | okx | +80.63% |
| 7 | CXMT | okx | +80.61% |
| 8 | MVLL | okx | +77.43% |
| 9 | XAU | okx | +76.67% |
| 10 | LYN | bitget | +65.48% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -1456.79% |
| 2 | BSP | okx | -488.80% |
| 3 | ONG | bitget | -397.92% |
| 4 | SKR | bitget | -365.84% |
| 5 | BSP | bitget | -356.97% |
| 6 | FLY | bitget | -290.07% |
| 7 | TUT | bitget | -239.04% |
| 8 | RVN | bitget | -227.54% |
| 9 | RDDT | bitget | -225.90% |
| 10 | FWDI | okx | -204.59% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | FLY | +290.07% | okx | +0.00% | bitget | -290.07% |
| 2 | RDDT | +225.90% | okx | +0.00% | bitget | -225.90% |
| 3 | FWDI | +204.59% | bitget | +0.00% | okx | -204.59% |
| 4 | GLW | +184.66% | okx | -3.57% | bitget | -188.23% |
| 5 | CGNX | +161.62% | okx | +0.00% | bitget | -161.62% |
| 6 | CIEN | +139.72% | okx | +0.00% | bitget | -139.72% |
| 7 | BSP | +131.83% | bitget | -356.97% | okx | -488.80% |
| 8 | TMF | +129.77% | okx | +129.77% | bitget | +0.00% |
| 9 | KIOXIA | +121.15% | okx | +121.15% | bitget | +0.00% |
| 10 | ALAB | +119.90% | okx | -7.12% | bitget | -127.02% |
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
