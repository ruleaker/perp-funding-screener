# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-11 14:59 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1305**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +1095.00% |
| 2 | NVDL | okx | +57.13% |
| 3 | SNXX | bitget | +46.43% |
| 4 | ARIA | bitget | +43.91% |
| 5 | US500 | okx | +40.43% |
| 6 | US100 | okx | +36.64% |
| 7 | ELSA | bitget | +31.65% |
| 8 | ZEST | bitget | +28.25% |
| 9 | RAVE | okx | +28.15% |
| 10 | UP | okx | +26.79% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MINA | bitget | -194.91% |
| 2 | ERA | bitget | -136.88% |
| 3 | OGN | bitget | -121.00% |
| 4 | MINA | okx | -99.58% |
| 5 | XDP | okx | -85.04% |
| 6 | WAL | bitget | -67.56% |
| 7 | SAND | bitget | -63.73% |
| 8 | WAL | okx | -62.53% |
| 9 | RVN | bitget | -58.69% |
| 10 | ONE | bitget | -54.20% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1095.00% | okx | +1095.00% | bitget | +0.00% |
| 2 | MINA | +95.33% | okx | -99.58% | bitget | -194.91% |
| 3 | ONE | +59.68% | okx | +5.47% | bitget | -54.20% |
| 4 | NVDL | +57.13% | okx | +57.13% | bitget | +0.00% |
| 5 | LA | +39.79% | bitget | -3.83% | okx | -43.62% |
| 6 | S | +36.66% | bitget | +5.47% | okx | -31.18% |
| 7 | CT | +34.14% | bitget | +5.47% | okx | -28.67% |
| 8 | SAND | +32.58% | okx | -31.15% | bitget | -63.73% |
| 9 | SNXX | +28.91% | bitget | +46.43% | okx | +17.52% |
| 10 | QNT | +25.96% | bitget | +0.11% | okx | -25.85% |
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
