# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-05 04:44 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1235**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BROCCOLI | bitget | +231.59% |
| 2 | ONE | bitget | +214.07% |
| 3 | ESPORTS | bitget | +186.92% |
| 4 | XMR | bitget | +159.43% |
| 5 | GPRO | okx | +152.52% |
| 6 | PONS | okx | +136.85% |
| 7 | PONS | bitget | +129.76% |
| 8 | CP | okx | +108.61% |
| 9 | UP | okx | +102.96% |
| 10 | FIGHT | bitget | +81.36% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ICX | okx | -595.50% |
| 2 | CAP | bitget | -509.39% |
| 3 | CAP | okx | -486.68% |
| 4 | LA | okx | -462.13% |
| 5 | LA | bitget | -409.64% |
| 6 | ACE | bitget | -298.39% |
| 7 | AKE | bitget | -99.10% |
| 8 | CYS | bitget | -98.00% |
| 9 | ONG | bitget | -96.58% |
| 10 | ZORA | okx | -92.74% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +191.69% | bitget | +214.07% | okx | +22.38% |
| 2 | GPRO | +152.52% | okx | +152.52% | bitget | +0.00% |
| 3 | CP | +103.14% | okx | +108.61% | bitget | +5.47% |
| 4 | TWLO | +91.43% | okx | +0.00% | bitget | -91.43% |
| 5 | EWZ | +60.50% | bitget | +0.00% | okx | -60.50% |
| 6 | LA | +52.49% | bitget | -409.64% | okx | -462.13% |
| 7 | MINA | +50.46% | okx | -36.15% | bitget | -86.61% |
| 8 | SLX | +47.06% | okx | +54.72% | bitget | +7.66% |
| 9 | SHAZ | +44.71% | bitget | +0.00% | okx | -44.71% |
| 10 | SIMO | +39.18% | okx | +39.18% | bitget | +0.00% |
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
