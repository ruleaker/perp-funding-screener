# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-05-31 17:35 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **909**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | DELL | okx | +367.67% |
| 2 | INX | bitget | +287.11% |
| 3 | DRAM | okx | +238.77% |
| 4 | ESPORTS | bitget | +228.96% |
| 5 | ARM | okx | +163.11% |
| 6 | COST | bitget | +109.50% |
| 7 | ASTS | bitget | +109.50% |
| 8 | IONQ | bitget | +109.50% |
| 9 | ASML | bitget | +109.50% |
| 10 | RDDT | bitget | +109.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | okx | -1050.11% |
| 2 | LAB | bitget | -924.51% |
| 3 | ZORA | bitget | -920.35% |
| 4 | ZORA | okx | -819.98% |
| 5 | AI | okx | -442.10% |
| 6 | AIGENSYN | bitget | -396.28% |
| 7 | PUNDIX | bitget | -337.81% |
| 8 | STEEM | bitget | -244.08% |
| 9 | MANTRA | bitget | -239.59% |
| 10 | HOME | bitget | -201.37% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | DELL | +258.17% | okx | +367.67% | bitget | +109.50% |
| 2 | HOME | +153.03% | okx | -48.34% | bitget | -201.37% |
| 3 | DRAM | +129.27% | okx | +238.77% | bitget | +109.50% |
| 4 | LAB | +125.60% | bitget | -924.51% | okx | -1050.11% |
| 5 | USAR | +109.50% | bitget | +109.50% | okx | +0.00% |
| 6 | COST | +109.50% | bitget | +109.50% | okx | +0.00% |
| 7 | PLTR | +109.50% | bitget | +109.50% | okx | +0.00% |
| 8 | TSM | +109.50% | bitget | +109.50% | okx | +0.00% |
| 9 | CRWV | +109.50% | bitget | +109.50% | okx | +0.00% |
| 10 | MSFT | +102.95% | bitget | +109.50% | okx | +6.55% |
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
