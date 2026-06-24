# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-24 18:16 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1047**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SIREN | bitget | +107.42% |
| 2 | SNDK | okx | +97.77% |
| 3 | ASML | okx | +89.80% |
| 4 | MU | bitget | +87.49% |
| 5 | DRAM | bitget | +70.52% |
| 6 | GLW | okx | +62.30% |
| 7 | MU | okx | +61.73% |
| 8 | XAG | okx | +49.02% |
| 9 | SOXL | bitget | +46.98% |
| 10 | ZEST | bitget | +42.16% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | okx | -877.53% |
| 2 | NES | okx | -675.66% |
| 3 | SATSSTOCK | bitget | -547.50% |
| 4 | LAB | bitget | -415.99% |
| 5 | SKHYNIX | okx | -257.64% |
| 6 | SHLD | okx | -250.16% |
| 7 | TAIKO | bitget | -227.10% |
| 8 | ONG | bitget | -203.34% |
| 9 | SAMSUNG | okx | -183.24% |
| 10 | RE | bitget | -168.85% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LAB | +461.54% | bitget | -415.99% | okx | -877.53% |
| 2 | SKHYNIX | +233.66% | bitget | -23.98% | okx | -257.64% |
| 3 | SAMSUNG | +165.72% | bitget | -17.52% | okx | -183.24% |
| 4 | OP | +106.96% | okx | +0.96% | bitget | -106.00% |
| 5 | ASML | +89.80% | okx | +89.80% | bitget | +0.00% |
| 6 | SNDK | +82.22% | okx | +97.77% | bitget | +15.55% |
| 7 | DRAM | +70.52% | bitget | +70.52% | okx | +0.00% |
| 8 | ARX | +68.27% | okx | -14.18% | bitget | -82.45% |
| 9 | GLW | +62.30% | okx | +62.30% | bitget | +0.00% |
| 10 | IOST | +59.73% | bitget | +10.95% | okx | -48.78% |
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
