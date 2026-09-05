# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-05 11:53 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1235**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | bitget | +299.70% |
| 2 | ESPORTS | bitget | +189.44% |
| 3 | PONS | okx | +173.14% |
| 4 | CP | okx | +96.11% |
| 5 | BROCCOLI | bitget | +89.79% |
| 6 | TRUTH | okx | +87.25% |
| 7 | GPRO | okx | +81.50% |
| 8 | XMR | bitget | +80.04% |
| 9 | VELODROME | bitget | +77.64% |
| 10 | SHEIN | okx | +64.94% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LA | okx | -246.30% |
| 2 | CAP | okx | -236.59% |
| 3 | LA | bitget | -227.10% |
| 4 | CAP | bitget | -221.96% |
| 5 | ACE | bitget | -204.33% |
| 6 | AKE | bitget | -149.47% |
| 7 | FLOCK | bitget | -112.46% |
| 8 | ZORA | okx | -91.01% |
| 9 | ICX | okx | -90.81% |
| 10 | ZORA | bitget | -79.61% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +266.94% | bitget | +299.70% | okx | +32.76% |
| 2 | PONS | +128.90% | okx | +173.14% | bitget | +44.24% |
| 3 | CP | +90.64% | okx | +96.11% | bitget | +5.47% |
| 4 | GPRO | +81.50% | okx | +81.50% | bitget | +0.00% |
| 5 | SHEIN | +64.94% | okx | +64.94% | bitget | +0.00% |
| 6 | RKLB | +32.55% | okx | +32.55% | bitget | +0.00% |
| 7 | TWLO | +30.20% | bitget | +0.00% | okx | -30.20% |
| 8 | EDGE | +30.18% | okx | +35.66% | bitget | +5.47% |
| 9 | FET | +29.92% | okx | +40.87% | bitget | +10.95% |
| 10 | SLX | +26.62% | okx | +32.10% | bitget | +5.47% |
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
