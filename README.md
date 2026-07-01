# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-01 05:02 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1062**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +548.78% |
| 2 | SKHYNIX | bitget | +547.50% |
| 3 | SAMSUNG | bitget | +351.28% |
| 4 | SAMSUNG | okx | +311.03% |
| 5 | HYUNDAI | bitget | +157.24% |
| 6 | HYUNDAI | okx | +154.93% |
| 7 | KIOXIA | okx | +151.09% |
| 8 | CRCL | okx | +101.86% |
| 9 | ESPORTS | bitget | +87.93% |
| 10 | RDW | okx | +87.21% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | bitget | -584.40% |
| 2 | SHLD | okx | -538.73% |
| 3 | ONG | bitget | -514.54% |
| 4 | LAB | okx | -452.29% |
| 5 | SLX | okx | -343.64% |
| 6 | CELO | bitget | -252.95% |
| 7 | LUNR | okx | -244.99% |
| 8 | CELO | okx | -229.13% |
| 9 | GWEI | bitget | -188.56% |
| 10 | SLX | bitget | -181.00% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SLX | +162.64% | bitget | -181.00% | okx | -343.64% |
| 2 | KIOXIA | +151.09% | okx | +151.09% | bitget | +0.00% |
| 3 | LAB | +132.11% | okx | -452.29% | bitget | -584.40% |
| 4 | CRCL | +101.86% | okx | +101.86% | bitget | +0.00% |
| 5 | GLM | +92.61% | okx | -70.54% | bitget | -163.16% |
| 6 | RDW | +87.21% | okx | +87.21% | bitget | +0.00% |
| 7 | KORU | +80.59% | okx | +80.59% | bitget | +0.00% |
| 8 | SONY | +70.42% | okx | +70.42% | bitget | +0.00% |
| 9 | ME | +60.73% | bitget | -10.29% | okx | -71.02% |
| 10 | BB | +59.44% | bitget | +5.47% | okx | -53.97% |
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
