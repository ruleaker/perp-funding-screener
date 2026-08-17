# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-17 16:53 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1193**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BSP | bitget | +211.01% |
| 2 | VST | bitget | +102.82% |
| 3 | MELI | bitget | +98.44% |
| 4 | SAMSUNG | okx | +91.14% |
| 5 | SKHYNIX | okx | +88.42% |
| 6 | BOT | bitget | +87.49% |
| 7 | ESPORTS | bitget | +87.38% |
| 8 | BOT | okx | +79.74% |
| 9 | SIREN | bitget | +73.69% |
| 10 | BRKB | bitget | +68.11% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BICO | bitget | -340.76% |
| 2 | SKUU | bitget | -336.49% |
| 3 | ONG | bitget | -333.65% |
| 4 | COW | bitget | -264.77% |
| 5 | ACE | bitget | -250.10% |
| 6 | HOME | bitget | -213.53% |
| 7 | CAP | bitget | -208.05% |
| 8 | HOME | okx | -203.51% |
| 9 | CAP | okx | -185.35% |
| 10 | AEHR | okx | -154.49% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKUU | +276.63% | okx | -59.86% | bitget | -336.49% |
| 2 | BICO | +231.60% | okx | -109.17% | bitget | -340.76% |
| 3 | AEHR | +154.49% | bitget | +0.00% | okx | -154.49% |
| 4 | BSP | +146.88% | bitget | +211.01% | okx | +64.12% |
| 5 | RVN | +143.50% | bitget | +4.05% | okx | -139.45% |
| 6 | DOS | +95.61% | okx | -13.13% | bitget | -108.73% |
| 7 | SAMSUNG | +89.28% | okx | +91.14% | bitget | +1.86% |
| 8 | GPS | +72.99% | bitget | -19.16% | okx | -92.16% |
| 9 | WAL | +57.63% | okx | -29.53% | bitget | -87.16% |
| 10 | THETA | +55.69% | bitget | -5.04% | okx | -60.73% |
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
