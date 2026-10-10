# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-10 14:34 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1305**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | US500 | okx | +67.69% |
| 2 | RAVE | bitget | +47.09% |
| 3 | AAOI | okx | +44.54% |
| 4 | US100 | okx | +35.34% |
| 5 | WET | bitget | +34.93% |
| 6 | DGAI | okx | +34.76% |
| 7 | CNPY | okx | +32.66% |
| 8 | 哈基米 | bitget | +30.44% |
| 9 | AKE | okx | +27.58% |
| 10 | RLS | okx | +27.24% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ERA | bitget | -997.55% |
| 2 | MAGIC | okx | -510.56% |
| 3 | MAGIC | bitget | -486.18% |
| 4 | ARPA | bitget | -469.65% |
| 5 | H100 | okx | -369.53% |
| 6 | BAT | okx | -313.98% |
| 7 | BAT | bitget | -288.86% |
| 8 | SAND | bitget | -131.84% |
| 9 | MINA | bitget | -99.21% |
| 10 | CTSI | bitget | -97.45% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +369.53% | bitget | +0.00% | okx | -369.53% |
| 2 | SAND | +65.93% | okx | -65.91% | bitget | -131.84% |
| 3 | LPT | +58.46% | bitget | +5.47% | okx | -52.99% |
| 4 | ONE | +49.82% | okx | +5.47% | bitget | -44.35% |
| 5 | AAOI | +44.54% | okx | +44.54% | bitget | +0.00% |
| 6 | RAVE | +41.61% | bitget | +47.09% | okx | +5.47% |
| 7 | RAY | +41.08% | bitget | +1.42% | okx | -39.66% |
| 8 | NEO | +29.47% | bitget | +10.95% | okx | -18.52% |
| 9 | WET | +29.46% | bitget | +34.93% | okx | +5.47% |
| 10 | DGAI | +29.29% | okx | +34.76% | bitget | +5.47% |
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
