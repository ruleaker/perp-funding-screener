# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-12 17:30 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1102**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 龙虾 | bitget | +74.13% |
| 2 | LAB | okx | +61.78% |
| 3 | US | bitget | +53.87% |
| 4 | DEXE | bitget | +41.28% |
| 5 | SIREN | bitget | +40.30% |
| 6 | M | bitget | +40.19% |
| 7 | NOK | okx | +39.28% |
| 8 | H | okx | +39.23% |
| 9 | ESPORTS | bitget | +37.45% |
| 10 | BE | okx | +33.60% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SXT | bitget | -521.44% |
| 2 | T | bitget | -477.53% |
| 3 | GWEI | bitget | -396.06% |
| 4 | TLM | bitget | -373.29% |
| 5 | OGN | bitget | -293.57% |
| 6 | AGLD | bitget | -244.84% |
| 7 | VANRY | bitget | -228.85% |
| 8 | SPELL | bitget | -174.10% |
| 9 | PUNDIX | bitget | -151.00% |
| 10 | ANKR | bitget | -148.59% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | AGLD | +127.76% | okx | -117.08% | bitget | -244.84% |
| 2 | ACH | +59.93% | bitget | +10.95% | okx | -48.98% |
| 3 | BAT | +56.70% | bitget | +10.95% | okx | -45.75% |
| 4 | MOVE | +53.11% | bitget | +5.47% | okx | -47.64% |
| 5 | ALGO | +52.12% | bitget | +10.95% | okx | -41.17% |
| 6 | SOPH | +50.84% | bitget | +5.47% | okx | -45.36% |
| 7 | NEO | +44.06% | bitget | +10.95% | okx | -33.11% |
| 8 | BARD | +38.65% | bitget | +2.63% | okx | -36.03% |
| 9 | SENT | +36.76% | okx | -11.09% | bitget | -47.85% |
| 10 | H | +33.75% | okx | +39.23% | bitget | +5.47% |
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
