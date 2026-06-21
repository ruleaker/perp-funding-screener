# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-21 05:24 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1021**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +222.18% |
| 2 | INFQ | okx | +185.81% |
| 3 | SIREN | bitget | +119.90% |
| 4 | ESPORTS | bitget | +102.82% |
| 5 | HIMS | okx | +67.23% |
| 6 | CRCL | okx | +64.73% |
| 7 | USAR | okx | +64.36% |
| 8 | GWEI | bitget | +59.57% |
| 9 | AXTI | okx | +51.71% |
| 10 | INTC | okx | +51.29% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -1185.01% |
| 2 | H | bitget | -749.75% |
| 3 | H | okx | -448.78% |
| 4 | AXS | bitget | -367.81% |
| 5 | AXS | okx | -325.67% |
| 6 | ALICE | bitget | -293.57% |
| 7 | FIDA | bitget | -226.01% |
| 8 | HOME | okx | -206.09% |
| 9 | RE | bitget | -198.74% |
| 10 | BICO | okx | -99.23% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +300.96% | okx | -448.78% | bitget | -749.75% |
| 2 | SKHYNIX | +222.18% | okx | +222.18% | bitget | +0.00% |
| 3 | INFQ | +185.81% | okx | +185.81% | bitget | +0.00% |
| 4 | HOME | +153.09% | bitget | -53.00% | okx | -206.09% |
| 5 | RE | +114.14% | okx | -84.60% | bitget | -198.74% |
| 6 | BICO | +110.62% | bitget | +11.39% | okx | -99.23% |
| 7 | CRCL | +64.73% | okx | +64.73% | bitget | +0.00% |
| 8 | USAR | +64.36% | okx | +64.36% | bitget | +0.00% |
| 9 | SAND | +64.11% | bitget | -30.55% | okx | -94.66% |
| 10 | MANA | +58.09% | bitget | +10.95% | okx | -47.14% |
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
