# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-01 18:21 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1062**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SHLD | okx | +790.99% |
| 2 | GLW | okx | +312.68% |
| 3 | ESPORTS | bitget | +119.14% |
| 4 | WEN | okx | +115.40% |
| 5 | MU | okx | +110.29% |
| 6 | KLAC | okx | +101.30% |
| 7 | GOOGL | bitget | +95.70% |
| 8 | EPIC | bitget | +93.08% |
| 9 | FIGHT | bitget | +91.21% |
| 10 | MRVL | bitget | +89.13% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CELO | bitget | -449.72% |
| 2 | TAIKO | bitget | -418.40% |
| 3 | CELO | okx | -279.56% |
| 4 | GWEI | bitget | -278.68% |
| 5 | ONG | bitget | -160.42% |
| 6 | LAB | okx | -124.26% |
| 7 | UNITAS | bitget | -118.81% |
| 8 | LAB | bitget | -115.19% |
| 9 | SLX | okx | -102.94% |
| 10 | RE | bitget | -99.43% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | GLW | +241.62% | okx | +312.68% | bitget | +71.07% |
| 2 | CELO | +170.16% | okx | -279.56% | bitget | -449.72% |
| 3 | WEN | +115.40% | okx | +115.40% | bitget | +0.00% |
| 4 | KLAC | +101.30% | okx | +101.30% | bitget | +0.00% |
| 5 | CRO | +83.06% | okx | -9.25% | bitget | -92.31% |
| 6 | MUBARAK | +75.67% | okx | +81.15% | bitget | +5.47% |
| 7 | GOOGL | +74.76% | bitget | +95.70% | okx | +20.94% |
| 8 | KIOXIA | +65.69% | okx | +65.69% | bitget | +0.00% |
| 9 | SLX | +56.95% | bitget | -45.99% | okx | -102.94% |
| 10 | BB | +56.63% | bitget | +5.47% | okx | -51.15% |
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
