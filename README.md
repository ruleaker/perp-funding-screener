# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-22 08:55 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1197**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | XMR | bitget | +124.83% |
| 2 | MUBARAK | okx | +51.00% |
| 3 | KGEN | okx | +50.75% |
| 4 | SHELL | bitget | +50.37% |
| 5 | BEAT | okx | +46.65% |
| 6 | ONE | okx | +43.33% |
| 7 | WAXP | bitget | +42.38% |
| 8 | TRUTH | okx | +40.02% |
| 9 | PROM | bitget | +39.64% |
| 10 | CARV | bitget | +35.26% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | COTI | bitget | -617.69% |
| 2 | MOVE | okx | -585.26% |
| 3 | MOVE | bitget | -431.87% |
| 4 | BICO | bitget | -221.74% |
| 5 | ACE | bitget | -213.42% |
| 6 | RVN | okx | -147.65% |
| 7 | BMNR | okx | -119.20% |
| 8 | ONT | bitget | -113.66% |
| 9 | BOT | okx | -109.84% |
| 10 | ONG | bitget | -103.48% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BICO | +172.22% | okx | -49.52% | bitget | -221.74% |
| 2 | MOVE | +153.40% | bitget | -431.87% | okx | -585.26% |
| 3 | RVN | +153.12% | bitget | +5.47% | okx | -147.65% |
| 4 | BOT | +109.84% | bitget | +0.00% | okx | -109.84% |
| 5 | BMNR | +106.28% | bitget | -12.92% | okx | -119.20% |
| 6 | CRCL | +99.66% | bitget | +0.00% | okx | -99.66% |
| 7 | AAOI | +87.58% | bitget | -3.94% | okx | -91.52% |
| 8 | COHR | +81.95% | bitget | -5.37% | okx | -87.31% |
| 9 | COIN | +74.18% | bitget | +0.00% | okx | -74.18% |
| 10 | GAS | +70.79% | bitget | -4.38% | okx | -75.17% |
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
