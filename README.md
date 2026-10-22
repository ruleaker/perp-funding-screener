# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-22 13:58 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1359**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SATL | bitget | +1095.00% |
| 2 | XNDU | bitget | +1095.00% |
| 3 | VALE | bitget | +1042.44% |
| 4 | FCX | bitget | +979.81% |
| 5 | SIMO | bitget | +959.11% |
| 6 | INFQ | bitget | +910.71% |
| 7 | EUV | bitget | +875.78% |
| 8 | SITM | bitget | +767.59% |
| 9 | BLSH | bitget | +682.73% |
| 10 | GFS | bitget | +678.24% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AXIS | okx | -1095.00% |
| 2 | AXIS | bitget | -1058.54% |
| 3 | H100 | okx | -843.45% |
| 4 | VLO | bitget | -682.51% |
| 5 | BOT | bitget | -647.14% |
| 6 | BP | bitget | -561.08% |
| 7 | BWET | okx | -489.55% |
| 8 | FWDI | bitget | -436.69% |
| 9 | NOC | bitget | -333.21% |
| 10 | BOT | okx | -307.40% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SIMO | +959.11% | bitget | +959.11% | okx | +0.00% |
| 2 | H100 | +848.93% | bitget | +5.47% | okx | -843.45% |
| 3 | INFQ | +803.70% | bitget | +910.71% | okx | +107.02% |
| 4 | BWET | +683.48% | bitget | +193.92% | okx | -489.55% |
| 5 | FWDI | +420.10% | okx | -16.58% | bitget | -436.69% |
| 6 | BOT | +339.75% | okx | -307.40% | bitget | -647.14% |
| 7 | CGNX | +335.07% | bitget | +335.07% | okx | +0.00% |
| 8 | SOFTBANK | +305.25% | okx | +305.25% | bitget | +0.00% |
| 9 | PURR | +293.35% | bitget | +293.35% | okx | +0.00% |
| 10 | OUST | +258.09% | bitget | +258.09% | okx | +0.00% |
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
