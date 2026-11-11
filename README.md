# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-11 16:25 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1412**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NG | okx | +844.63% |
| 2 | NATGAS | bitget | +528.56% |
| 3 | CSOPSS2LHKD | bitget | +295.87% |
| 4 | CXMT | okx | +236.35% |
| 5 | KIOXIA | bitget | +234.44% |
| 6 | SHAZ | bitget | +217.14% |
| 7 | CSOPSK2LHKD | bitget | +217.03% |
| 8 | AGPU | bitget | +195.13% |
| 9 | SOFTBANK | bitget | +186.37% |
| 10 | CSOPSAMSUNG2L | okx | +181.64% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | XNDU | bitget | -838.66% |
| 2 | ETN | bitget | -550.24% |
| 3 | FTNT | bitget | -478.62% |
| 4 | SMR | bitget | -336.06% |
| 5 | OSS | bitget | -314.27% |
| 6 | RGTI | bitget | -263.57% |
| 7 | ASX | bitget | -224.48% |
| 8 | SATL | bitget | -211.77% |
| 9 | ACHR | bitget | -211.23% |
| 10 | AEHR | bitget | -209.36% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SMR | +297.73% | okx | -38.32% | bitget | -336.06% |
| 2 | SHAZ | +228.01% | bitget | +217.14% | okx | -10.87% |
| 3 | H100 | +213.30% | bitget | +5.47% | okx | -207.82% |
| 4 | AEHR | +209.36% | okx | +0.00% | bitget | -209.36% |
| 5 | POET | +201.48% | okx | +0.00% | bitget | -201.48% |
| 6 | SOFTBANK | +186.37% | bitget | +186.37% | okx | +0.00% |
| 7 | OUST | +164.14% | okx | +0.00% | bitget | -164.14% |
| 8 | SIMO | +162.72% | okx | +0.00% | bitget | -162.72% |
| 9 | UNITREE | +160.08% | bitget | +0.00% | okx | -160.08% |
| 10 | INFQ | +138.08% | okx | +0.00% | bitget | -138.08% |
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
