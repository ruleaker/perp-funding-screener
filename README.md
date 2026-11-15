# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-15 06:54 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1413**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +425.50% |
| 2 | CROSS | bitget | +134.14% |
| 3 | INTW | okx | +73.46% |
| 4 | BIDU | okx | +67.50% |
| 5 | SPCX | okx | +62.11% |
| 6 | IREN | okx | +61.99% |
| 7 | INTW | bitget | +58.91% |
| 8 | SOFTBANK | okx | +58.16% |
| 9 | O | okx | +57.19% |
| 10 | AXTI | okx | +50.17% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOPH | okx | -963.21% |
| 2 | SOPH | bitget | -955.39% |
| 3 | MSTU | okx | -394.48% |
| 4 | INIT | okx | -310.11% |
| 5 | POWER | bitget | -225.90% |
| 6 | BERA | bitget | -186.81% |
| 7 | BAN | bitget | -168.30% |
| 8 | BARD | okx | -151.79% |
| 9 | BERA | okx | -148.52% |
| 10 | KAVA | bitget | -146.07% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | MSTU | +436.64% | bitget | +42.16% | okx | -394.48% |
| 2 | H100 | +420.03% | okx | +425.50% | bitget | +5.47% |
| 3 | INIT | +277.91% | bitget | -32.19% | okx | -310.11% |
| 4 | HUMA | +78.96% | bitget | -15.99% | okx | -94.95% |
| 5 | SOFTBANK | +58.16% | okx | +58.16% | bitget | +0.00% |
| 6 | ACH | +57.70% | bitget | +5.58% | okx | -52.12% |
| 7 | IREN | +54.87% | okx | +61.99% | bitget | +7.12% |
| 8 | GRT | +52.90% | bitget | -8.98% | okx | -61.88% |
| 9 | ALLO | +52.62% | bitget | +5.47% | okx | -47.14% |
| 10 | O | +51.72% | okx | +57.19% | bitget | +5.47% |
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
