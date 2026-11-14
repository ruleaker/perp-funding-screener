# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-14 15:14 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1413**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +186.12% |
| 2 | UMC | okx | +99.43% |
| 3 | DNA | okx | +25.26% |
| 4 | O | okx | +19.59% |
| 5 | SKDD | bitget | +16.75% |
| 6 | THE | bitget | +13.14% |
| 7 | BILL | okx | +11.33% |
| 8 | ATOM | okx | +10.95% |
| 9 | BAND | okx | +10.95% |
| 10 | BAT | okx | +10.95% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOPH | okx | -787.88% |
| 2 | SOPH | bitget | -641.45% |
| 3 | BARD | bitget | -452.67% |
| 4 | MSTU | bitget | -280.43% |
| 5 | BERA | bitget | -278.90% |
| 6 | INIT | okx | -221.89% |
| 7 | MSTR | okx | -171.14% |
| 8 | MSTU | okx | -136.27% |
| 9 | MSTR | bitget | -133.26% |
| 10 | BNC | bitget | -127.68% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BARD | +350.76% | okx | -101.91% | bitget | -452.67% |
| 2 | H100 | +180.65% | okx | +186.12% | bitget | +5.47% |
| 3 | BERA | +156.46% | okx | -122.43% | bitget | -278.90% |
| 4 | SOPH | +146.43% | bitget | -641.45% | okx | -787.88% |
| 5 | MSTU | +144.15% | okx | -136.27% | bitget | -280.43% |
| 6 | INIT | +137.36% | bitget | -84.53% | okx | -221.89% |
| 7 | HUMA | +81.84% | bitget | -34.49% | okx | -116.33% |
| 8 | BMNR | +59.96% | okx | -53.27% | bitget | -113.22% |
| 9 | LUNA | +54.81% | bitget | +5.47% | okx | -49.33% |
| 10 | PI | +44.46% | okx | +5.47% | bitget | -38.98% |
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
