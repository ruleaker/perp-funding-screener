# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-02 17:30 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1154**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 1MCHEEMS | bitget | +246.92% |
| 2 | 龙虾 | bitget | +124.17% |
| 3 | SNXX | okx | +111.83% |
| 4 | ESPORTS | bitget | +103.37% |
| 5 | SOXL | okx | +93.22% |
| 6 | COTI | bitget | +80.59% |
| 7 | MINIMAX | okx | +71.10% |
| 8 | INX | bitget | +62.09% |
| 9 | H | okx | +59.01% |
| 10 | H | bitget | +53.44% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HYPER | bitget | -531.62% |
| 2 | SYN | bitget | -328.72% |
| 3 | LA | bitget | -308.57% |
| 4 | LA | okx | -255.60% |
| 5 | MANTRA | bitget | -236.08% |
| 6 | VANA | bitget | -180.35% |
| 7 | EUL | bitget | -170.71% |
| 8 | VANRY | bitget | -145.96% |
| 9 | VANA | okx | -112.79% |
| 10 | SLX | bitget | -106.65% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SNXX | +111.83% | okx | +111.83% | bitget | +0.00% |
| 2 | SOXL | +93.22% | okx | +93.22% | bitget | +0.00% |
| 3 | MINIMAX | +71.10% | okx | +71.10% | bitget | +0.00% |
| 4 | VANA | +67.56% | okx | -112.79% | bitget | -180.35% |
| 5 | LA | +52.97% | okx | -255.60% | bitget | -308.57% |
| 6 | AEON | +52.18% | bitget | +5.47% | okx | -46.70% |
| 7 | ZIL | +50.70% | bitget | -17.52% | okx | -68.22% |
| 8 | APE | +49.28% | bitget | +10.95% | okx | -38.33% |
| 9 | KIOXIA | +49.12% | bitget | +0.00% | okx | -49.12% |
| 10 | SLX | +45.78% | okx | -60.87% | bitget | -106.65% |
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
