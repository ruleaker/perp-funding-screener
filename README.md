# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-14 17:39 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1110**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +158.46% |
| 2 | SAMSUNG | okx | +150.08% |
| 3 | ESPORTS | bitget | +90.56% |
| 4 | BOT | bitget | +89.35% |
| 5 | KORU | okx | +72.02% |
| 6 | LAB | bitget | +64.39% |
| 7 | SITM | bitget | +61.54% |
| 8 | CRCL | bitget | +57.93% |
| 9 | 龙虾 | bitget | +56.94% |
| 10 | IBM | okx | +54.89% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | VANRY | bitget | -894.51% |
| 2 | SOXS | bitget | -347.88% |
| 3 | TLM | bitget | -295.76% |
| 4 | SXT | bitget | -244.73% |
| 5 | SKHY | okx | -172.62% |
| 6 | GWEI | bitget | -133.70% |
| 7 | VANA | okx | -117.07% |
| 8 | VANA | bitget | -107.97% |
| 9 | NEWT | bitget | -98.88% |
| 10 | LRC | okx | -87.39% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +158.46% | okx | +158.46% | bitget | +0.00% |
| 2 | SAMSUNG | +150.08% | okx | +150.08% | bitget | +0.00% |
| 3 | SKHY | +109.54% | bitget | -63.07% | okx | -172.62% |
| 4 | BOT | +89.35% | bitget | +89.35% | okx | +0.00% |
| 5 | IBM | +54.89% | okx | +54.89% | bitget | +0.00% |
| 6 | RDDT | +51.46% | okx | +0.00% | bitget | -51.46% |
| 7 | GLW | +50.79% | okx | +50.79% | bitget | +0.00% |
| 8 | RAY | +45.04% | okx | +5.07% | bitget | -39.97% |
| 9 | BMNR | +44.42% | okx | +44.42% | bitget | +0.00% |
| 10 | ESP | +41.79% | okx | -10.66% | bitget | -52.45% |
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
