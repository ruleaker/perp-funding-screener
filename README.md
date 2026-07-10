# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-10 11:22 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1101**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +732.85% |
| 2 | SOXS | bitget | +547.50% |
| 3 | BNC | bitget | +539.51% |
| 4 | RDDT | bitget | +281.31% |
| 5 | KORU | bitget | +262.58% |
| 6 | FWDI | bitget | +116.07% |
| 7 | 1MCHEEMS | bitget | +108.84% |
| 8 | GOOGL | bitget | +106.32% |
| 9 | APLD | okx | +88.81% |
| 10 | QNTSTOCK | bitget | +88.04% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKL | bitget | -1328.13% |
| 2 | KAT | okx | -738.80% |
| 3 | KAT | bitget | -634.11% |
| 4 | EWH | bitget | -547.50% |
| 5 | GUN | bitget | -370.88% |
| 6 | IOTA | bitget | -365.95% |
| 7 | IOTA | okx | -278.52% |
| 8 | VANRY | bitget | -246.37% |
| 9 | PENG | okx | -214.36% |
| 10 | STXSTOCK | bitget | -212.76% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +732.85% | okx | +732.85% | bitget | +0.00% |
| 2 | RDDT | +281.31% | bitget | +281.31% | okx | +0.00% |
| 3 | KORU | +187.09% | bitget | +262.58% | okx | +75.49% |
| 4 | RVN | +116.95% | bitget | -7.66% | okx | -124.61% |
| 5 | GMX | +113.44% | okx | -1.32% | bitget | -114.76% |
| 6 | KAT | +104.68% | bitget | -634.11% | okx | -738.80% |
| 7 | POET | +91.84% | okx | +9.71% | bitget | -82.12% |
| 8 | APLD | +88.81% | okx | +88.81% | bitget | +0.00% |
| 9 | GOOGL | +88.55% | bitget | +106.32% | okx | +17.77% |
| 10 | IOTA | +87.42% | okx | -278.52% | bitget | -365.95% |
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
