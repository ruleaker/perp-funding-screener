# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-01 05:22 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **909**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +771.97% |
| 2 | IBM | okx | +651.21% |
| 3 | GEV | okx | +547.57% |
| 4 | AAOI | okx | +427.68% |
| 5 | GLW | okx | +328.82% |
| 6 | INX | bitget | +279.44% |
| 7 | DELL | okx | +271.42% |
| 8 | NBIS | okx | +264.49% |
| 9 | WDC | okx | +244.93% |
| 10 | H | okx | +237.55% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | okx | -1642.50% |
| 2 | LAB | bitget | -1176.03% |
| 3 | GUN | bitget | -764.42% |
| 4 | HOME | bitget | -670.47% |
| 5 | HOME | okx | -499.81% |
| 6 | GENIUS | bitget | -292.91% |
| 7 | PUNDIX | bitget | -204.55% |
| 8 | SOXS | bitget | -109.50% |
| 9 | DRIFT | bitget | -106.65% |
| 10 | STEEM | bitget | -94.94% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LAB | +466.47% | bitget | -1176.03% | okx | -1642.50% |
| 2 | AAOI | +318.18% | okx | +427.68% | bitget | +109.50% |
| 3 | H | +232.08% | okx | +237.55% | bitget | +5.47% |
| 4 | VRT | +186.74% | okx | +186.74% | bitget | +0.00% |
| 5 | HOME | +170.65% | okx | -499.81% | bitget | -670.47% |
| 6 | DELL | +161.92% | okx | +271.42% | bitget | +109.50% |
| 7 | NBIS | +154.99% | okx | +264.49% | bitget | +109.50% |
| 8 | GME | +149.37% | okx | +149.37% | bitget | +0.00% |
| 9 | WDC | +135.43% | okx | +244.93% | bitget | +109.50% |
| 10 | INFQ | +129.60% | okx | +129.60% | bitget | +0.00% |
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
