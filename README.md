# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-16 18:44 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1415**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | USDESTOCK | bitget | +155.60% |
| 2 | POWER | bitget | +145.09% |
| 3 | BWET | okx | +132.84% |
| 4 | UP | okx | +104.44% |
| 5 | BNC | bitget | +84.64% |
| 6 | AGPU | bitget | +77.64% |
| 7 | NVDL | okx | +46.37% |
| 8 | DNA | okx | +45.89% |
| 9 | XPT | okx | +44.08% |
| 10 | TLT | okx | +42.83% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RARE | bitget | -974.44% |
| 2 | HUMA | okx | -650.12% |
| 3 | SKR | bitget | -539.07% |
| 4 | KAVA | bitget | -490.45% |
| 5 | INIT | okx | -461.98% |
| 6 | AXIS | bitget | -193.38% |
| 7 | ERA | bitget | -185.27% |
| 8 | SOPH | okx | -182.49% |
| 9 | AXIS | okx | -168.48% |
| 10 | HUMA | bitget | -130.85% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HUMA | +519.26% | bitget | -130.85% | okx | -650.12% |
| 2 | INIT | +337.48% | bitget | -124.50% | okx | -461.98% |
| 3 | SOPH | +141.97% | bitget | -40.52% | okx | -182.49% |
| 4 | BWET | +132.84% | okx | +132.84% | bitget | +0.00% |
| 5 | H100 | +73.82% | bitget | +5.47% | okx | -68.34% |
| 6 | WOO | +63.61% | bitget | +10.95% | okx | -52.66% |
| 7 | CHZ | +63.39% | bitget | +10.95% | okx | -52.44% |
| 8 | IOTA | +58.45% | okx | -22.25% | bitget | -80.70% |
| 9 | ONE | +55.62% | okx | -46.10% | bitget | -101.73% |
| 10 | PEOPLE | +44.32% | bitget | -4.60% | okx | -48.92% |
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
