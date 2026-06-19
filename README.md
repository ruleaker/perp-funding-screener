# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-19 18:14 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1021**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SIREN | bitget | +204.11% |
| 2 | BTW | bitget | +182.32% |
| 3 | ESPORTS | bitget | +164.03% |
| 4 | XPT | okx | +121.37% |
| 5 | O | okx | +107.32% |
| 6 | QNT | okx | +106.31% |
| 7 | SKHYNIX | okx | +97.03% |
| 8 | CRCL | okx | +70.48% |
| 9 | XVG | bitget | +66.90% |
| 10 | XMR | bitget | +62.85% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H | okx | -904.59% |
| 2 | RE | bitget | -764.53% |
| 3 | HOME | okx | -427.78% |
| 4 | BICO | okx | -423.71% |
| 5 | H | bitget | -408.76% |
| 6 | RE | okx | -392.04% |
| 7 | BICO | bitget | -273.64% |
| 8 | SAHARA | okx | -245.11% |
| 9 | SAHARA | bitget | -241.23% |
| 10 | SPELL | bitget | -161.51% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +495.82% | bitget | -408.76% | okx | -904.59% |
| 2 | RE | +372.49% | okx | -392.04% | bitget | -764.53% |
| 3 | HOME | +305.14% | bitget | -122.64% | okx | -427.78% |
| 4 | BICO | +150.07% | bitget | -273.64% | okx | -423.71% |
| 5 | TRUST | +126.44% | bitget | +5.47% | okx | -120.97% |
| 6 | XPT | +121.37% | okx | +121.37% | bitget | +0.00% |
| 7 | SKHYNIX | +97.03% | okx | +97.03% | bitget | +0.00% |
| 8 | QNT | +95.36% | okx | +106.31% | bitget | +10.95% |
| 9 | CRCL | +70.48% | okx | +70.48% | bitget | +0.00% |
| 10 | BAT | +67.60% | okx | +3.65% | bitget | -63.95% |
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
