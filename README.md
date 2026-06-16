# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-16 19:54 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1007**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SIREN | bitget | +374.05% |
| 2 | TER | okx | +262.12% |
| 3 | BMNR | okx | +163.91% |
| 4 | H | okx | +115.11% |
| 5 | FOLKS | bitget | +94.17% |
| 6 | NOK | okx | +76.71% |
| 7 | SOON | okx | +73.16% |
| 8 | MU | bitget | +71.50% |
| 9 | ESPORTS | bitget | +69.53% |
| 10 | LAB | bitget | +56.28% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SPELL | bitget | -1675.35% |
| 2 | SENT | bitget | -361.90% |
| 3 | SENT | okx | -323.33% |
| 4 | HOME | okx | -223.74% |
| 5 | SAHARA | bitget | -199.84% |
| 6 | SKHYNIX | okx | -197.22% |
| 7 | SPACE | bitget | -181.66% |
| 8 | SAHARA | okx | -138.38% |
| 9 | FIDA | bitget | -127.24% |
| 10 | HOME | bitget | -126.36% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +197.22% | bitget | +0.00% | okx | -197.22% |
| 2 | BMNR | +163.91% | okx | +163.91% | bitget | +0.00% |
| 3 | SPACE | +130.67% | okx | -50.99% | bitget | -181.66% |
| 4 | H | +109.63% | okx | +115.11% | bitget | +5.47% |
| 5 | HOME | +97.38% | bitget | -126.36% | okx | -223.74% |
| 6 | MU | +71.50% | bitget | +71.50% | okx | +0.00% |
| 7 | SAHARA | +61.45% | okx | -138.38% | bitget | -199.84% |
| 8 | SAMSUNG | +56.88% | bitget | +0.00% | okx | -56.88% |
| 9 | PLUME | +55.74% | okx | +5.47% | bitget | -50.26% |
| 10 | SOON | +50.60% | okx | +73.16% | bitget | +22.56% |
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
