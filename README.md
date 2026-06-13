# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-13 04:58 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **982**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BMNR | okx | +621.13% |
| 2 | 1000RATS | bitget | +107.75% |
| 3 | FOLKS | bitget | +106.43% |
| 4 | POWER | bitget | +101.94% |
| 5 | SLX | bitget | +77.96% |
| 6 | 龙虾 | bitget | +74.02% |
| 7 | US | bitget | +68.99% |
| 8 | SKHYNIX | okx | +67.78% |
| 9 | AMD | okx | +58.63% |
| 10 | LAB | bitget | +57.27% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | STG | bitget | -1963.44% |
| 2 | AXL | bitget | -406.03% |
| 3 | SOPH | okx | -361.21% |
| 4 | SOPH | bitget | -345.91% |
| 5 | ENJ | bitget | -230.17% |
| 6 | ENJ | okx | -212.07% |
| 7 | HOME | bitget | -191.84% |
| 8 | HOME | okx | -169.38% |
| 9 | SAHARA | bitget | -120.01% |
| 10 | BABY | bitget | -99.54% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SLX | +72.49% | bitget | +77.96% | okx | +5.47% |
| 2 | SKHYNIX | +67.78% | okx | +67.78% | bitget | +0.00% |
| 3 | ALGO | +63.97% | bitget | +10.95% | okx | -53.02% |
| 4 | BEAT | +60.72% | bitget | +5.47% | okx | -55.24% |
| 5 | BAND | +59.93% | okx | -9.61% | bitget | -69.53% |
| 6 | BABY | +58.73% | okx | -40.81% | bitget | -99.54% |
| 7 | AMD | +58.63% | okx | +58.63% | bitget | +0.00% |
| 8 | LAB | +51.79% | bitget | +57.27% | okx | +5.47% |
| 9 | CHZ | +50.44% | okx | -43.08% | bitget | -93.51% |
| 10 | ZEC | +37.12% | bitget | +1.97% | okx | -35.15% |
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
