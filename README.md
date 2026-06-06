# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-06 04:34 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **951**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BEAT | bitget | +187.57% |
| 2 | MU | okx | +108.26% |
| 3 | EPIC | bitget | +70.85% |
| 4 | ESPORTS | bitget | +61.32% |
| 5 | LAB | bitget | +41.72% |
| 6 | SAHARA | bitget | +38.22% |
| 7 | SIREN | bitget | +30.55% |
| 8 | SNDK | okx | +28.91% |
| 9 | BEAT | okx | +25.16% |
| 10 | QQQ | okx | +20.53% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -1367.22% |
| 2 | HOME | okx | -1019.14% |
| 3 | STABLE | bitget | -341.53% |
| 4 | CBRS | okx | -259.55% |
| 5 | GENIUS | bitget | -234.11% |
| 6 | PROS | okx | -220.83% |
| 7 | AMD | okx | -216.74% |
| 8 | CRWV | okx | -214.10% |
| 9 | PROS | bitget | -174.00% |
| 10 | LPT | bitget | -172.46% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HOME | +348.07% | okx | -1019.14% | bitget | -1367.22% |
| 2 | CBRS | +259.55% | bitget | +0.00% | okx | -259.55% |
| 3 | AMD | +216.74% | bitget | +0.00% | okx | -216.74% |
| 4 | STABLE | +214.76% | okx | -126.77% | bitget | -341.53% |
| 5 | CRWV | +214.10% | bitget | +0.00% | okx | -214.10% |
| 6 | EWJ | +166.49% | bitget | +0.00% | okx | -166.49% |
| 7 | BEAT | +162.42% | bitget | +187.57% | okx | +25.16% |
| 8 | ASTS | +160.90% | bitget | +0.00% | okx | -160.90% |
| 9 | MSTR | +147.68% | bitget | +0.00% | okx | -147.68% |
| 10 | COIN | +143.98% | bitget | +0.00% | okx | -143.98% |
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
