# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-05 18:00 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1164**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +564.36% |
| 2 | BOT | bitget | +214.73% |
| 3 | UNITAS | bitget | +164.80% |
| 4 | 龙虾 | bitget | +91.21% |
| 5 | GOOGL | bitget | +79.17% |
| 6 | BLEND | okx | +71.75% |
| 7 | SAMSUNG | okx | +71.58% |
| 8 | JCT | bitget | +61.76% |
| 9 | JELLYJELLY | okx | +49.24% |
| 10 | BLESS | bitget | +47.41% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | bitget | -306.27% |
| 2 | FIDA | bitget | -292.58% |
| 3 | CYS | bitget | -152.20% |
| 4 | SKR | bitget | -145.63% |
| 5 | TLM | bitget | -144.87% |
| 6 | BIRB | bitget | -102.49% |
| 7 | COTI | bitget | -100.41% |
| 8 | LA | bitget | -94.94% |
| 9 | LA | okx | -86.86% |
| 10 | EUL | bitget | -66.14% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HOME | +256.66% | okx | -49.61% | bitget | -306.27% |
| 2 | BOT | +183.47% | bitget | +214.73% | okx | +31.26% |
| 3 | GOOGL | +79.17% | bitget | +79.17% | okx | +0.00% |
| 4 | SAMSUNG | +71.58% | okx | +71.58% | bitget | +0.00% |
| 5 | KORU | +42.27% | okx | +0.00% | bitget | -42.27% |
| 6 | GPS | +40.08% | okx | +5.47% | bitget | -34.60% |
| 7 | IOTA | +39.25% | okx | +3.22% | bitget | -36.03% |
| 8 | ENSO | +37.52% | bitget | -0.22% | okx | -37.74% |
| 9 | PLUME | +31.95% | okx | +4.03% | bitget | -27.92% |
| 10 | WET | +31.86% | bitget | +37.34% | okx | +5.47% |
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
