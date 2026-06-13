# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-13 17:51 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **982**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | USO | okx | +117.96% |
| 2 | GME | okx | +98.73% |
| 3 | 龙虾 | bitget | +92.86% |
| 4 | SIREN | bitget | +72.38% |
| 5 | ASR | bitget | +67.56% |
| 6 | 1000RATS | bitget | +66.47% |
| 7 | ASML | okx | +64.25% |
| 8 | AMD | okx | +58.76% |
| 9 | COAI | okx | +57.84% |
| 10 | BTW | bitget | +57.82% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H | okx | -1077.31% |
| 2 | AXL | bitget | -387.96% |
| 3 | HOME | okx | -346.61% |
| 4 | ESPORTS | bitget | -319.30% |
| 5 | STG | bitget | -209.80% |
| 6 | IWM | okx | -203.67% |
| 7 | HOME | bitget | -179.58% |
| 8 | SAHARA | bitget | -153.63% |
| 9 | SAHARA | okx | -124.18% |
| 10 | TON | okx | -118.28% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +1064.50% | bitget | -12.81% | okx | -1077.31% |
| 2 | IWM | +214.18% | bitget | +10.51% | okx | -203.67% |
| 3 | HOME | +167.03% | bitget | -179.58% | okx | -346.61% |
| 4 | GME | +98.73% | okx | +98.73% | bitget | +0.00% |
| 5 | TON | +95.39% | bitget | -22.89% | okx | -118.28% |
| 6 | ASML | +64.25% | okx | +64.25% | bitget | +0.00% |
| 7 | OP | +62.96% | okx | +6.79% | bitget | -56.17% |
| 8 | AMD | +58.76% | okx | +58.76% | bitget | +0.00% |
| 9 | CHZ | +54.23% | okx | -51.44% | bitget | -105.67% |
| 10 | COAI | +52.37% | okx | +57.84% | bitget | +5.47% |
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
