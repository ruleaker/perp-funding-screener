# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-19 05:32 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1021**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +563.29% |
| 2 | SAMSUNG | okx | +431.43% |
| 3 | BTW | bitget | +321.16% |
| 4 | SIREN | bitget | +214.95% |
| 5 | ESPORTS | bitget | +135.67% |
| 6 | SKHYNIX | bitget | +109.50% |
| 7 | SAMSUNG | bitget | +109.50% |
| 8 | ASR | bitget | +99.64% |
| 9 | HYUNDAI | okx | +90.87% |
| 10 | TAG | bitget | +70.41% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BLEND | okx | -612.66% |
| 2 | RE | okx | -439.16% |
| 3 | PRL | bitget | -403.95% |
| 4 | RE | bitget | -401.10% |
| 5 | HOME | okx | -280.11% |
| 6 | BX | okx | -245.06% |
| 7 | SAHARA | bitget | -242.65% |
| 8 | MRVL | okx | -235.05% |
| 9 | TRUST | okx | -227.44% |
| 10 | FIDA | bitget | -226.99% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +453.79% | okx | +563.29% | bitget | +109.50% |
| 2 | SAMSUNG | +321.93% | okx | +431.43% | bitget | +109.50% |
| 3 | BX | +245.06% | bitget | +0.00% | okx | -245.06% |
| 4 | MRVL | +228.59% | bitget | -6.46% | okx | -235.05% |
| 5 | HOME | +206.53% | bitget | -73.58% | okx | -280.11% |
| 6 | MU | +195.69% | bitget | -12.15% | okx | -207.85% |
| 7 | GME | +191.22% | bitget | +0.00% | okx | -191.22% |
| 8 | EWY | +185.34% | bitget | +0.00% | okx | -185.34% |
| 9 | INTC | +106.16% | bitget | -9.42% | okx | -115.57% |
| 10 | CRWV | +100.06% | bitget | +0.00% | okx | -100.06% |
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
