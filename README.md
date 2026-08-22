# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-22 01:56 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1197**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BSP | okx | +532.85% |
| 2 | SHAZ | bitget | +318.10% |
| 3 | ONE | bitget | +216.15% |
| 4 | TRIA | bitget | +126.36% |
| 5 | SKDD | okx | +122.17% |
| 6 | TRIA | okx | +90.07% |
| 7 | ZEST | bitget | +88.80% |
| 8 | WET | bitget | +83.00% |
| 9 | MOCA | bitget | +81.58% |
| 10 | PIPPIN | bitget | +76.65% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONT | bitget | -426.39% |
| 2 | GAS | okx | -265.82% |
| 3 | RVN | okx | -191.55% |
| 4 | PRL | bitget | -179.80% |
| 5 | HOME | okx | -174.59% |
| 6 | ONT | okx | -167.96% |
| 7 | HOME | bitget | -166.88% |
| 8 | SPCH | bitget | -161.40% |
| 9 | COTI | bitget | -160.42% |
| 10 | GAS | bitget | -150.67% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BSP | +532.85% | okx | +532.85% | bitget | +0.00% |
| 2 | SHAZ | +304.20% | bitget | +318.10% | okx | +13.90% |
| 3 | ONT | +258.43% | okx | -167.96% | bitget | -426.39% |
| 4 | ONE | +210.68% | bitget | +216.15% | okx | +5.47% |
| 5 | RVN | +197.03% | bitget | +5.47% | okx | -191.55% |
| 6 | SKDD | +122.17% | okx | +122.17% | bitget | +0.00% |
| 7 | GAS | +115.14% | bitget | -150.67% | okx | -265.82% |
| 8 | WET | +77.53% | bitget | +83.00% | okx | +5.47% |
| 9 | CRCL | +72.98% | okx | +72.98% | bitget | +0.00% |
| 10 | UNITREE | +62.03% | bitget | +0.00% | okx | -62.03% |
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
