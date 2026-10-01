# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-01 15:33 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1293**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AGPU | bitget | +491.11% |
| 2 | RDDT | bitget | +254.48% |
| 3 | SECZ | bitget | +208.49% |
| 4 | RUM | bitget | +177.83% |
| 5 | 龙虾 | bitget | +138.96% |
| 6 | OKLO | bitget | +134.14% |
| 7 | SOFTBANK | okx | +118.96% |
| 8 | BNC | bitget | +107.64% |
| 9 | OKLO | okx | +95.10% |
| 10 | CYPH | bitget | +95.05% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ARK | bitget | -312.51% |
| 2 | JNJ | okx | -222.05% |
| 3 | BSP | bitget | -212.87% |
| 4 | BWET | bitget | -205.86% |
| 5 | BLSH | bitget | -152.97% |
| 6 | TBT | bitget | -148.15% |
| 7 | FWDI | okx | -148.08% |
| 8 | CT | okx | -127.08% |
| 9 | KR200 | okx | -110.83% |
| 10 | CSOPSK2LHKD | bitget | -109.50% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RDDT | +221.13% | bitget | +254.48% | okx | +33.34% |
| 2 | BSP | +212.87% | okx | +0.00% | bitget | -212.87% |
| 3 | SOFTBANK | +179.85% | okx | +118.96% | bitget | -60.88% |
| 4 | QNT | +126.51% | okx | +64.20% | bitget | -62.31% |
| 5 | CT | +110.22% | bitget | -16.86% | okx | -127.08% |
| 6 | KR200 | +107.43% | bitget | -3.39% | okx | -110.83% |
| 7 | CXMT | +98.36% | bitget | +0.00% | okx | -98.36% |
| 8 | CYPH | +95.05% | bitget | +95.05% | okx | +0.00% |
| 9 | APLD | +94.28% | bitget | +94.28% | okx | +0.00% |
| 10 | FWDI | +86.76% | bitget | -61.32% | okx | -148.08% |
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
