# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-20 13:43 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1344**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SDGR | bitget | +541.04% |
| 2 | JMKE | bitget | +423.33% |
| 3 | ETN | bitget | +408.54% |
| 4 | ECHO | bitget | +396.17% |
| 5 | KOPN | bitget | +351.71% |
| 6 | CYPH | bitget | +245.61% |
| 7 | KSTR | okx | +203.65% |
| 8 | USDESTOCK | bitget | +200.71% |
| 9 | SIREN | bitget | +181.44% |
| 10 | BWET | okx | +174.41% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -1027.74% |
| 2 | CVNA | okx | -363.18% |
| 3 | VLO | bitget | -335.18% |
| 4 | BTW | bitget | -310.76% |
| 5 | TWST | bitget | -284.15% |
| 6 | BWET | bitget | -261.05% |
| 7 | BOT | bitget | -249.66% |
| 8 | BP | bitget | -235.21% |
| 9 | CT | bitget | -200.93% |
| 10 | SAND | bitget | -185.93% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1033.22% | bitget | +5.47% | okx | -1027.74% |
| 2 | BWET | +435.46% | okx | +174.41% | bitget | -261.05% |
| 3 | TWST | +284.15% | okx | +0.00% | bitget | -284.15% |
| 4 | BOT | +260.98% | okx | +11.32% | bitget | -249.66% |
| 5 | CYPH | +229.50% | bitget | +245.61% | okx | +16.11% |
| 6 | CVNA | +190.83% | bitget | -172.35% | okx | -363.18% |
| 7 | UNITREE | +159.30% | bitget | +0.00% | okx | -159.30% |
| 8 | KSTR | +141.34% | okx | +203.65% | bitget | +62.31% |
| 9 | KR200 | +137.13% | okx | +137.13% | bitget | +0.00% |
| 10 | DKNG | +136.25% | bitget | +162.83% | okx | +26.58% |
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
