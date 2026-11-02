# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-02 06:33 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1385**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KSTR | okx | +234.00% |
| 2 | SAMSUNGEM | bitget | +201.92% |
| 3 | SKUU | bitget | +196.55% |
| 4 | CSOPSK2LHKD | bitget | +188.12% |
| 5 | CSOPSS2LHKD | bitget | +183.19% |
| 6 | EWJ | okx | +176.87% |
| 7 | CXMT | okx | +172.14% |
| 8 | XVG | bitget | +170.05% |
| 9 | SECZ | bitget | +159.21% |
| 10 | TQQQ | okx | +145.05% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITREE | okx | -1095.00% |
| 2 | UNITREE | bitget | -1095.00% |
| 3 | JIO | bitget | -1095.00% |
| 4 | HOT | bitget | -978.38% |
| 5 | H100 | okx | -631.37% |
| 6 | POWR | bitget | -426.06% |
| 7 | AKE | okx | -279.63% |
| 8 | WUXIBIO | okx | -249.88% |
| 9 | POWER | bitget | -247.14% |
| 10 | SKDD | bitget | -204.87% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +636.85% | bitget | +5.47% | okx | -631.37% |
| 2 | SKDD | +265.67% | okx | +60.79% | bitget | -204.87% |
| 3 | KSTR | +222.06% | okx | +234.00% | bitget | +11.94% |
| 4 | SKUU | +196.55% | bitget | +196.55% | okx | +0.00% |
| 5 | TQQQ | +145.05% | okx | +145.05% | bitget | +0.00% |
| 6 | GPRO | +141.58% | okx | +126.69% | bitget | -14.89% |
| 7 | GTLB | +127.81% | okx | +127.81% | bitget | +0.00% |
| 8 | RAM | +121.71% | bitget | +133.48% | okx | +11.77% |
| 9 | AKE | +117.90% | bitget | -161.73% | okx | -279.63% |
| 10 | LYTE | +109.39% | bitget | +109.39% | okx | +0.00% |
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
