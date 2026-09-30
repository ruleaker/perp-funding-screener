# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-30 05:47 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1282**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NAVER | bitget | +329.38% |
| 2 | CXMT | okx | +262.38% |
| 3 | CXMT | bitget | +252.73% |
| 4 | SAMSUNGEM | bitget | +237.29% |
| 5 | NAVER | okx | +210.50% |
| 6 | JCT | bitget | +183.96% |
| 7 | ONG | bitget | +168.63% |
| 8 | XIAOMI | okx | +159.31% |
| 9 | HYUNDAI | okx | +135.43% |
| 10 | XIAOMI | bitget | +132.71% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HANMI | okx | -907.25% |
| 2 | HANMI | bitget | -885.09% |
| 3 | MEW | okx | -224.73% |
| 4 | MEW | bitget | -174.98% |
| 5 | KORU | bitget | -155.27% |
| 6 | ZM | okx | -127.62% |
| 7 | NMR | okx | -125.92% |
| 8 | BERA | okx | -108.77% |
| 9 | SOXL | bitget | -65.15% |
| 10 | XDP | okx | -57.79% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KORU | +155.27% | okx | +0.00% | bitget | -155.27% |
| 2 | ZM | +127.62% | bitget | +0.00% | okx | -127.62% |
| 3 | NAVER | +118.88% | bitget | +329.38% | okx | +210.50% |
| 4 | SHEIN | +106.40% | okx | +106.40% | bitget | +0.00% |
| 5 | FET | +82.02% | bitget | +87.49% | okx | +5.47% |
| 6 | PIPPIN | +81.45% | bitget | +121.22% | okx | +39.77% |
| 7 | BOT | +79.66% | okx | +79.66% | bitget | +0.00% |
| 8 | BERA | +75.92% | bitget | -32.85% | okx | -108.77% |
| 9 | NMR | +73.91% | bitget | -52.01% | okx | -125.92% |
| 10 | KSTR | +73.42% | okx | +37.51% | bitget | -35.92% |
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
