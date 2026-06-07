# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-07 05:04 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **951**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BMNR | okx | +293.29% |
| 2 | BEAT | okx | +195.37% |
| 3 | QNT | okx | +174.24% |
| 4 | CRCL | okx | +154.77% |
| 5 | SAHARA | bitget | +129.32% |
| 6 | MRVL | okx | +125.10% |
| 7 | MSTR | okx | +96.93% |
| 8 | CYS | bitget | +89.68% |
| 9 | FOLKS | bitget | +87.16% |
| 10 | NOK | okx | +86.83% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LA | bitget | -542.68% |
| 2 | FIDA | bitget | -475.89% |
| 3 | GUN | bitget | -400.88% |
| 4 | HOME | bitget | -324.67% |
| 5 | EDEN | okx | -320.71% |
| 6 | HOME | okx | -288.30% |
| 7 | LA | okx | -244.96% |
| 8 | STABLE | okx | -214.72% |
| 9 | INX | bitget | -189.76% |
| 10 | STABLE | bitget | -182.10% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LA | +297.72% | okx | -244.96% | bitget | -542.68% |
| 2 | QNT | +181.69% | okx | +174.24% | bitget | -7.45% |
| 3 | BEAT | +172.70% | okx | +195.37% | bitget | +22.67% |
| 4 | CRCL | +154.77% | okx | +154.77% | bitget | +0.00% |
| 5 | MRVL | +125.10% | okx | +125.10% | bitget | +0.00% |
| 6 | SAHARA | +113.67% | bitget | +129.32% | okx | +15.65% |
| 7 | MSTR | +96.93% | okx | +96.93% | bitget | +0.00% |
| 8 | EWY | +85.45% | okx | +85.45% | bitget | +0.00% |
| 9 | USAR | +81.21% | okx | +81.21% | bitget | +0.00% |
| 10 | AMD | +78.53% | okx | +78.53% | bitget | +0.00% |
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
