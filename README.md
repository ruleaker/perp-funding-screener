# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-01 10:14 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1154**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SNXX | okx | +83.75% |
| 2 | H | bitget | +82.89% |
| 3 | 龙虾 | bitget | +71.17% |
| 4 | ESPORTS | bitget | +67.45% |
| 5 | FIGHT | bitget | +62.09% |
| 6 | SHAZ | okx | +60.66% |
| 7 | LAB | okx | +59.07% |
| 8 | ARIA | bitget | +58.04% |
| 9 | NBIS | okx | +48.69% |
| 10 | SIREN | bitget | +45.99% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SYN | bitget | -414.79% |
| 2 | TLM | bitget | -409.97% |
| 3 | 1000XEC | bitget | -307.04% |
| 4 | MMT | bitget | -304.41% |
| 5 | VANRY | bitget | -296.09% |
| 6 | MMT | okx | -257.88% |
| 7 | EUL | bitget | -244.19% |
| 8 | MIRA | bitget | -224.15% |
| 9 | LA | okx | -199.02% |
| 10 | LA | bitget | -164.36% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | CRO | +89.82% | bitget | +10.95% | okx | -78.87% |
| 2 | SNXX | +83.75% | okx | +83.75% | bitget | +0.00% |
| 3 | BAND | +66.55% | bitget | +10.95% | okx | -55.60% |
| 4 | SHAZ | +60.66% | okx | +60.66% | bitget | +0.00% |
| 5 | H | +55.89% | bitget | +82.89% | okx | +27.00% |
| 6 | ICX | +54.70% | bitget | +5.47% | okx | -49.22% |
| 7 | RAY | +54.03% | bitget | +5.47% | okx | -48.56% |
| 8 | AEON | +50.63% | bitget | -31.54% | okx | -82.16% |
| 9 | NBIS | +48.69% | okx | +48.69% | bitget | +0.00% |
| 10 | MMT | +46.53% | okx | -257.88% | bitget | -304.41% |
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
