# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-10 04:55 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **967**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BEAT | okx | +275.03% |
| 2 | RDW | okx | +139.73% |
| 3 | AAOI | okx | +137.06% |
| 4 | SKHYNIX | bitget | +109.50% |
| 5 | URNM | okx | +76.12% |
| 6 | 1MCHEEMS | bitget | +72.27% |
| 7 | FIGHT | bitget | +70.41% |
| 8 | GWEI | bitget | +61.21% |
| 9 | XPD | okx | +57.81% |
| 10 | XVG | bitget | +56.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | -1632.21% |
| 2 | H | okx | -1095.00% |
| 3 | MANTRA | bitget | -710.22% |
| 4 | BLEND | okx | -603.17% |
| 5 | SAHARA | okx | -458.09% |
| 6 | INX | bitget | -406.57% |
| 7 | HOME | okx | -398.85% |
| 8 | SAHARA | bitget | -396.17% |
| 9 | KAT | okx | -322.81% |
| 10 | WAL | bitget | -319.52% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +1096.42% | bitget | +1.42% | okx | -1095.00% |
| 2 | HOME | +304.68% | bitget | -94.17% | okx | -398.85% |
| 3 | WAL | +254.60% | okx | -64.92% | bitget | -319.52% |
| 4 | KAT | +232.25% | bitget | -90.56% | okx | -322.81% |
| 5 | BEAT | +223.13% | okx | +275.03% | bitget | +51.90% |
| 6 | SENT | +173.04% | bitget | +5.47% | okx | -167.57% |
| 7 | RDW | +139.73% | okx | +139.73% | bitget | +0.00% |
| 8 | AAOI | +137.06% | okx | +137.06% | bitget | +0.00% |
| 9 | ZEC | +110.00% | bitget | -34.38% | okx | -144.38% |
| 10 | KSM | +76.06% | okx | +1.27% | bitget | -74.79% |
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
