# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-12 04:05 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1102**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | okx | +117.44% |
| 2 | US | bitget | +101.62% |
| 3 | SKHYNIX | okx | +92.29% |
| 4 | ESPORTS | bitget | +75.12% |
| 5 | BX | okx | +67.99% |
| 6 | BTW | bitget | +66.90% |
| 7 | CRCL | okx | +64.28% |
| 8 | SIREN | bitget | +63.62% |
| 9 | H | okx | +56.05% |
| 10 | 龙虾 | bitget | +43.14% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SXT | bitget | -753.91% |
| 2 | T | bitget | -711.09% |
| 3 | GWEI | bitget | -468.11% |
| 4 | ANKR | bitget | -351.06% |
| 5 | SLX | okx | -143.27% |
| 6 | SPELL | bitget | -142.68% |
| 7 | DATA | bitget | -116.18% |
| 8 | SLX | bitget | -111.69% |
| 9 | AI | okx | -106.07% |
| 10 | SNX | okx | -104.30% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LAB | +99.26% | okx | +117.44% | bitget | +18.18% |
| 2 | SKHYNIX | +92.29% | okx | +92.29% | bitget | +0.00% |
| 3 | SNX | +82.40% | bitget | -21.90% | okx | -104.30% |
| 4 | BX | +67.99% | okx | +67.99% | bitget | +0.00% |
| 5 | CRCL | +64.28% | okx | +64.28% | bitget | +0.00% |
| 6 | THETA | +50.64% | bitget | +10.95% | okx | -39.69% |
| 7 | H | +50.58% | okx | +56.05% | bitget | +5.47% |
| 8 | ESP | +49.77% | bitget | +5.47% | okx | -44.29% |
| 9 | PI | +46.66% | bitget | -0.88% | okx | -47.53% |
| 10 | DATA | +45.29% | okx | -70.89% | bitget | -116.18% |
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
