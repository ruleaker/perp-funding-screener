# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-23 04:38 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1033**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RDW | okx | +635.43% |
| 2 | SKHYNIX | okx | +570.77% |
| 3 | SAMSUNG | okx | +335.35% |
| 4 | SIREN | bitget | +226.23% |
| 5 | POET | okx | +184.21% |
| 6 | HYUNDAI | okx | +171.87% |
| 7 | BMNR | okx | +148.93% |
| 8 | CIEN | okx | +118.76% |
| 9 | BEAT | bitget | +115.52% |
| 10 | KIOXIA | bitget | +109.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAYER | bitget | -1016.93% |
| 2 | LAYER | okx | -445.40% |
| 3 | TAIKO | bitget | -343.28% |
| 4 | ARX | okx | -296.54% |
| 5 | RE | bitget | -194.91% |
| 6 | H | bitget | -180.68% |
| 7 | RE | okx | -178.26% |
| 8 | ID | bitget | -166.22% |
| 9 | FIDA | bitget | -159.76% |
| 10 | SYN | bitget | -158.67% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RDW | +635.43% | okx | +635.43% | bitget | +0.00% |
| 2 | LAYER | +571.53% | okx | -445.40% | bitget | -1016.93% |
| 3 | SKHYNIX | +461.27% | okx | +570.77% | bitget | +109.50% |
| 4 | ARX | +343.18% | bitget | +46.65% | okx | -296.54% |
| 5 | SAMSUNG | +225.85% | okx | +335.35% | bitget | +109.50% |
| 6 | POET | +184.21% | okx | +184.21% | bitget | +0.00% |
| 7 | BMNR | +148.93% | okx | +148.93% | bitget | +0.00% |
| 8 | CIEN | +118.76% | okx | +118.76% | bitget | +0.00% |
| 9 | TER | +89.85% | okx | +89.85% | bitget | +0.00% |
| 10 | PROS | +88.15% | bitget | +93.62% | okx | +5.47% |
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
