# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-05-27 18:37 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **902**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NOK | okx | +446.46% |
| 2 | BLESS | bitget | +289.63% |
| 3 | MRVL | okx | +125.45% |
| 4 | GLW | okx | +123.63% |
| 5 | 龙虾 | bitget | +116.51% |
| 6 | MU | okx | +110.35% |
| 7 | NOKSTOCK | bitget | +109.50% |
| 8 | MRVL | bitget | +103.15% |
| 9 | AAOI | okx | +98.63% |
| 10 | SOXL | okx | +98.07% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | INX | bitget | -466.03% |
| 2 | ESPORTS | bitget | -372.41% |
| 3 | PRL | bitget | -263.13% |
| 4 | ALT | bitget | -257.00% |
| 5 | 1MCHEEMS | bitget | -235.97% |
| 6 | CHIP | okx | -88.85% |
| 7 | ONG | bitget | -87.93% |
| 8 | FIDA | bitget | -84.42% |
| 9 | ESP | okx | -82.82% |
| 10 | CHIP | bitget | -82.23% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | AAOI | +98.63% | okx | +98.63% | bitget | +0.00% |
| 2 | SOXL | +98.07% | okx | +98.07% | bitget | +0.00% |
| 3 | GOOGL | +85.52% | bitget | +85.52% | okx | +0.00% |
| 4 | ESP | +75.59% | bitget | -7.23% | okx | -82.82% |
| 5 | ONT | +64.42% | bitget | +5.47% | okx | -58.95% |
| 6 | THETA | +63.40% | okx | +10.95% | bitget | -52.45% |
| 7 | BSB | +63.14% | okx | +66.97% | bitget | +3.83% |
| 8 | MU | +58.66% | okx | +110.35% | bitget | +51.68% |
| 9 | TSM | +56.65% | bitget | +79.17% | okx | +22.52% |
| 10 | METIS | +54.85% | bitget | +5.47% | okx | -49.37% |
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
