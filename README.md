# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-16 13:09 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **997**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SIREN | bitget | +518.70% |
| 2 | GLW | okx | +195.67% |
| 3 | TER | okx | +145.47% |
| 4 | SKHYNIX | okx | +140.22% |
| 5 | SOON | bitget | +136.66% |
| 6 | XVG | bitget | +118.81% |
| 7 | BB | okx | +94.90% |
| 8 | POET | okx | +94.45% |
| 9 | QNTSTOCK | bitget | +92.09% |
| 10 | RKLB | okx | +90.95% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H | okx | -575.11% |
| 2 | SPACE | bitget | -553.30% |
| 3 | HOME | okx | -370.67% |
| 4 | SAHARA | okx | -272.41% |
| 5 | SPACE | okx | -240.93% |
| 6 | HOME | bitget | -193.49% |
| 7 | SAHARA | bitget | -185.16% |
| 8 | MIRA | bitget | -162.72% |
| 9 | FIDA | bitget | -134.25% |
| 10 | STG | bitget | -90.01% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +580.58% | bitget | +5.47% | okx | -575.11% |
| 2 | SPACE | +312.37% | okx | -240.93% | bitget | -553.30% |
| 3 | GLW | +195.67% | okx | +195.67% | bitget | +0.00% |
| 4 | HOME | +177.18% | bitget | -193.49% | okx | -370.67% |
| 5 | SKHYNIX | +140.22% | okx | +140.22% | bitget | +0.00% |
| 6 | SOON | +100.20% | bitget | +136.66% | okx | +36.46% |
| 7 | POET | +94.45% | okx | +94.45% | bitget | +0.00% |
| 8 | RKLB | +90.95% | okx | +90.95% | bitget | +0.00% |
| 9 | BB | +89.42% | okx | +94.90% | bitget | +5.47% |
| 10 | SAHARA | +87.25% | bitget | -185.16% | okx | -272.41% |
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
