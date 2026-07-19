# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-19 04:02 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1118**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | WEN | okx | +88.76% |
| 2 | GLW | okx | +78.56% |
| 3 | SOXL | okx | +74.22% |
| 4 | SAMSUNG | okx | +69.76% |
| 5 | MRVL | okx | +64.93% |
| 6 | DRAM | okx | +63.32% |
| 7 | SKHY | okx | +57.92% |
| 8 | XMR | bitget | +56.50% |
| 9 | SKHYNIX | okx | +54.91% |
| 10 | TRUTH | okx | +54.08% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SPELL | bitget | -830.67% |
| 2 | ONG | bitget | -417.74% |
| 3 | TOSHI | bitget | -402.96% |
| 4 | HOME | bitget | -286.34% |
| 5 | ESPORTS | bitget | -185.16% |
| 6 | NEO | okx | -157.63% |
| 7 | TLM | bitget | -150.67% |
| 8 | CRWV | okx | -138.64% |
| 9 | ACE | bitget | -136.11% |
| 10 | HOME | okx | -126.39% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HOME | +159.96% | okx | -126.39% | bitget | -286.34% |
| 2 | CRWV | +138.64% | bitget | +0.00% | okx | -138.64% |
| 3 | PROS | +97.37% | okx | -12.13% | bitget | -109.50% |
| 4 | WEN | +88.76% | okx | +88.76% | bitget | +0.00% |
| 5 | GLW | +78.56% | okx | +78.56% | bitget | +0.00% |
| 6 | SOXL | +74.22% | okx | +74.22% | bitget | +0.00% |
| 7 | SAMSUNG | +69.76% | okx | +69.76% | bitget | +0.00% |
| 8 | MRVL | +64.93% | okx | +64.93% | bitget | +0.00% |
| 9 | DRAM | +63.32% | okx | +63.32% | bitget | +0.00% |
| 10 | QTUM | +62.24% | bitget | +9.42% | okx | -52.82% |
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
