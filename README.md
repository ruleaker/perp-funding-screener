# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-16 05:43 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **993**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SIREN | bitget | +245.83% |
| 2 | RDW | okx | +190.75% |
| 3 | HYUNDAI | okx | +158.26% |
| 4 | SAMSUNG | okx | +129.20% |
| 5 | BMNR | okx | +123.28% |
| 6 | SKHYNIX | bitget | +109.50% |
| 7 | SAMSUNG | bitget | +109.50% |
| 8 | GEV | okx | +102.35% |
| 9 | GLW | okx | +92.11% |
| 10 | AMD | okx | +75.21% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SPACE | bitget | -1318.05% |
| 2 | HOME | okx | -809.82% |
| 3 | SYN | bitget | -719.42% |
| 4 | SPACE | okx | -672.88% |
| 5 | HOME | bitget | -401.54% |
| 6 | FIDA | bitget | -322.70% |
| 7 | STG | bitget | -289.96% |
| 8 | SAHARA | bitget | -276.60% |
| 9 | SAHARA | okx | -207.37% |
| 10 | SPELL | bitget | -146.40% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SPACE | +645.17% | okx | -672.88% | bitget | -1318.05% |
| 2 | HOME | +408.28% | bitget | -401.54% | okx | -809.82% |
| 3 | RDW | +190.75% | okx | +190.75% | bitget | +0.00% |
| 4 | QNT | +115.26% | bitget | +7.01% | okx | -108.25% |
| 5 | HYUNDAI | +92.56% | okx | +158.26% | bitget | +65.70% |
| 6 | GLW | +92.11% | okx | +92.11% | bitget | +0.00% |
| 7 | BEAT | +88.80% | bitget | +0.88% | okx | -87.93% |
| 8 | AMD | +75.21% | okx | +75.21% | bitget | +0.00% |
| 9 | MOVE | +71.50% | bitget | -45.55% | okx | -117.05% |
| 10 | SAHARA | +69.22% | okx | -207.37% | bitget | -276.60% |
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
