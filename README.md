# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-07 17:46 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **951**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +365.73% |
| 2 | BEAT | okx | +243.55% |
| 3 | SAHARA | bitget | +208.16% |
| 4 | LITE | okx | +187.70% |
| 5 | CRCL | okx | +175.27% |
| 6 | INX | bitget | +140.60% |
| 7 | QQQ | okx | +139.20% |
| 8 | QNT | okx | +129.27% |
| 9 | EWT | okx | +99.07% |
| 10 | DRAM | okx | +96.13% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | okx | -651.49% |
| 2 | HOME | bitget | -608.93% |
| 3 | SHLD | okx | -344.53% |
| 4 | GUN | bitget | -340.87% |
| 5 | FIDA | bitget | -176.40% |
| 6 | EDEN | okx | -157.26% |
| 7 | GENIUS | bitget | -128.88% |
| 8 | BB | okx | -126.13% |
| 9 | PROS | bitget | -113.55% |
| 10 | ARIA | bitget | -103.92% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BEAT | +225.15% | okx | +243.55% | bitget | +18.40% |
| 2 | LITE | +187.70% | okx | +187.70% | bitget | +0.00% |
| 3 | CRCL | +175.27% | okx | +175.27% | bitget | +0.00% |
| 4 | SAHARA | +145.91% | bitget | +208.16% | okx | +62.25% |
| 5 | QQQ | +139.20% | okx | +139.20% | bitget | +0.00% |
| 6 | QNT | +132.01% | okx | +129.27% | bitget | -2.74% |
| 7 | BB | +119.45% | bitget | -6.68% | okx | -126.13% |
| 8 | APR | +118.15% | okx | +25.52% | bitget | -92.64% |
| 9 | EWT | +99.07% | okx | +99.07% | bitget | +0.00% |
| 10 | DRAM | +96.13% | okx | +96.13% | bitget | +0.00% |
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
