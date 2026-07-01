# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-01 11:37 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1062**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FLY | bitget | +547.50% |
| 2 | KIOXIA | okx | +522.58% |
| 3 | SKHYNIX | okx | +341.31% |
| 4 | OKLO | bitget | +135.45% |
| 5 | SAMSUNG | okx | +127.68% |
| 6 | ESPORTS | bitget | +113.44% |
| 7 | GOOGL | bitget | +109.83% |
| 8 | HYUNDAI | okx | +103.45% |
| 9 | MRVL | bitget | +103.04% |
| 10 | GLW | bitget | +90.67% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TAIKO | bitget | -2005.16% |
| 2 | SHLD | okx | -1083.44% |
| 3 | NKE | bitget | -547.50% |
| 4 | CELO | okx | -531.10% |
| 5 | BUD | bitget | -509.83% |
| 6 | CELO | bitget | -390.48% |
| 7 | GWEI | bitget | -312.73% |
| 8 | MUU | bitget | -251.74% |
| 9 | ONG | bitget | -230.28% |
| 10 | ADI | bitget | -192.94% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KIOXIA | +522.58% | okx | +522.58% | bitget | +0.00% |
| 2 | SKHYNIX | +341.31% | okx | +341.31% | bitget | +0.00% |
| 3 | RDDT | +149.69% | okx | +0.00% | bitget | -149.69% |
| 4 | AXTI | +143.79% | okx | +12.28% | bitget | -131.51% |
| 5 | CELO | +140.62% | bitget | -390.48% | okx | -531.10% |
| 6 | SAMSUNG | +127.68% | okx | +127.68% | bitget | +0.00% |
| 7 | STRC | +104.82% | bitget | +0.00% | okx | -104.82% |
| 8 | HYUNDAI | +103.45% | okx | +103.45% | bitget | +0.00% |
| 9 | MRVL | +103.04% | bitget | +103.04% | okx | +0.00% |
| 10 | SLX | +83.39% | bitget | -105.23% | okx | -188.62% |
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
