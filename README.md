# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-29 15:21 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1380**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LWLG | bitget | +511.91% |
| 2 | GFS | bitget | +393.87% |
| 3 | BOTZ | bitget | +389.16% |
| 4 | JOBY | bitget | +368.47% |
| 5 | CLSK | bitget | +340.00% |
| 6 | NTAP | bitget | +322.26% |
| 7 | BLSH | bitget | +315.58% |
| 8 | VEEV | bitget | +311.09% |
| 9 | POET | bitget | +291.38% |
| 10 | NIO | bitget | +278.90% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | JIO | bitget | -1041.02% |
| 2 | TSTOCK | bitget | -511.69% |
| 3 | BLUR | bitget | -497.35% |
| 4 | DHR | bitget | -483.55% |
| 5 | GILD | bitget | -428.91% |
| 6 | CSTOCK | bitget | -423.87% |
| 7 | CSX | bitget | -373.61% |
| 8 | SBUX | bitget | -352.15% |
| 9 | ABBV | bitget | -303.97% |
| 10 | XLV | bitget | -302.00% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | POET | +291.38% | bitget | +291.38% | okx | +0.00% |
| 2 | BLUR | +282.01% | okx | -215.34% | bitget | -497.35% |
| 3 | ABBV | +225.50% | okx | -78.47% | bitget | -303.97% |
| 4 | TWLO | +218.45% | bitget | +218.45% | okx | +0.00% |
| 5 | UNITREE | +198.26% | bitget | +65.48% | okx | -132.78% |
| 6 | FLY | +194.69% | bitget | +194.69% | okx | +0.00% |
| 7 | SIMO | +174.00% | okx | +0.00% | bitget | -174.00% |
| 8 | OUST | +172.78% | bitget | +199.62% | okx | +26.84% |
| 9 | H100 | +140.92% | okx | +146.39% | bitget | +5.47% |
| 10 | GPRO | +137.62% | bitget | +201.59% | okx | +63.97% |
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
