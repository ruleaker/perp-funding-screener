# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-22 10:37 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1129**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FLY | bitget | +191.62% |
| 2 | GEV | okx | +143.98% |
| 3 | BUD | bitget | +135.67% |
| 4 | SKHYNIX | okx | +134.47% |
| 5 | TENCENT | bitget | +125.27% |
| 6 | ASX | bitget | +115.85% |
| 7 | LYN | bitget | +103.81% |
| 8 | LUNR | okx | +83.68% |
| 9 | FWDI | bitget | +77.31% |
| 10 | SAMSUNG | okx | +64.56% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ERA | bitget | -2190.00% |
| 2 | MIRA | bitget | -1061.27% |
| 3 | DEXE | bitget | -817.20% |
| 4 | ONE | bitget | -561.52% |
| 5 | ONE | okx | -547.61% |
| 6 | RDDT | bitget | -447.20% |
| 7 | QNTSTOCK | bitget | -388.29% |
| 8 | LA | bitget | -351.60% |
| 9 | RE | okx | -244.21% |
| 10 | VANRY | bitget | -227.10% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RDDT | +447.20% | okx | +0.00% | bitget | -447.20% |
| 2 | LA | +214.44% | okx | -137.16% | bitget | -351.60% |
| 3 | GEV | +143.98% | okx | +143.98% | bitget | +0.00% |
| 4 | SKHYNIX | +134.47% | okx | +134.47% | bitget | +0.00% |
| 5 | WEN | +123.33% | bitget | +0.00% | okx | -123.33% |
| 6 | BOT | +91.16% | bitget | +0.00% | okx | -91.16% |
| 7 | RDW | +86.73% | bitget | +0.00% | okx | -86.73% |
| 8 | ZHIPU | +83.29% | bitget | +0.00% | okx | -83.29% |
| 9 | QNT | +66.66% | bitget | +10.95% | okx | -55.71% |
| 10 | SAMSUNG | +64.56% | okx | +64.56% | bitget | +0.00% |
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
