# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-21 15:13 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1274**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HPQ | bitget | +319.08% |
| 2 | CIEN | bitget | +306.16% |
| 3 | NKE | bitget | +281.63% |
| 4 | RDDT | bitget | +194.03% |
| 5 | SHLD | okx | +182.50% |
| 6 | SOFTBANK | bitget | +182.43% |
| 7 | MCD | bitget | +179.69% |
| 8 | SOFTBANK | okx | +144.20% |
| 9 | CRO | bitget | +135.12% |
| 10 | AMC | bitget | +132.06% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CELR | bitget | -1048.90% |
| 2 | ONE | okx | -772.49% |
| 3 | ETN | bitget | -480.16% |
| 4 | SPIR | bitget | -361.02% |
| 5 | FIGHT | bitget | -275.50% |
| 6 | PROVE | okx | -217.98% |
| 7 | PROVE | bitget | -203.78% |
| 8 | ONG | bitget | -114.10% |
| 9 | AVA | bitget | -87.38% |
| 10 | G | bitget | -83.44% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +756.94% | bitget | -15.55% | okx | -772.49% |
| 2 | CIEN | +306.16% | bitget | +306.16% | okx | +0.00% |
| 3 | RDDT | +194.03% | bitget | +194.03% | okx | +0.00% |
| 4 | AMC | +132.06% | bitget | +132.06% | okx | +0.00% |
| 5 | CRO | +124.17% | bitget | +135.12% | okx | +10.95% |
| 6 | FLY | +93.95% | bitget | +93.95% | okx | +0.00% |
| 7 | GPRO | +80.47% | okx | +128.44% | bitget | +47.96% |
| 8 | KR200 | +79.60% | okx | +79.60% | bitget | +0.00% |
| 9 | INTC | +79.32% | bitget | +87.16% | okx | +7.84% |
| 10 | ROK | +75.69% | bitget | +0.00% | okx | -75.69% |
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
