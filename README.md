# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-31 05:51 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1209**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | XIAOMI | okx | +216.33% |
| 2 | UNITAS | bitget | +181.55% |
| 3 | UP | okx | +146.04% |
| 4 | KIOXIA | okx | +135.49% |
| 5 | SHOP | okx | +115.75% |
| 6 | XMR | bitget | +104.90% |
| 7 | MVLL | okx | +90.20% |
| 8 | BRKB | okx | +88.23% |
| 9 | RDW | okx | +80.17% |
| 10 | EWZ | okx | +78.47% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZORA | bitget | -2177.19% |
| 2 | ZORA | okx | -1095.00% |
| 3 | ZKP | bitget | -514.76% |
| 4 | BICO | bitget | -495.05% |
| 5 | ZKP | okx | -422.73% |
| 6 | SKR | bitget | -402.52% |
| 7 | TUT | bitget | -348.65% |
| 8 | SAND | okx | -334.08% |
| 9 | BICO | okx | -318.74% |
| 10 | FLOCK | bitget | -312.18% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ZORA | +1082.19% | okx | -1095.00% | bitget | -2177.19% |
| 2 | SAND | +251.07% | bitget | -83.00% | okx | -334.08% |
| 3 | SKDD | +236.20% | bitget | +0.00% | okx | -236.20% |
| 4 | BOT | +220.10% | bitget | +0.00% | okx | -220.10% |
| 5 | BICO | +176.31% | okx | -318.74% | bitget | -495.05% |
| 6 | XIAOMI | +163.88% | okx | +216.33% | bitget | +52.45% |
| 7 | 0G | +138.88% | bitget | +5.47% | okx | -133.40% |
| 8 | SHOP | +115.75% | okx | +115.75% | bitget | +0.00% |
| 9 | KIOXIA | +111.62% | okx | +135.49% | bitget | +23.87% |
| 10 | ZKP | +92.03% | okx | -422.73% | bitget | -514.76% |
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
