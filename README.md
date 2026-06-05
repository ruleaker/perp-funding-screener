# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-05 11:40 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **951**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +165.24% |
| 2 | 龙虾 | bitget | +141.58% |
| 3 | AAOI | okx | +139.31% |
| 4 | NOK | okx | +117.26% |
| 5 | GEV | okx | +105.74% |
| 6 | XCU | okx | +104.48% |
| 7 | DRAM | okx | +96.28% |
| 8 | QNTSTOCK | bitget | +95.59% |
| 9 | INX | bitget | +87.49% |
| 10 | MU | okx | +87.41% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BABY | bitget | -2190.00% |
| 2 | LA | bitget | -1695.17% |
| 3 | BABY | okx | -1095.00% |
| 4 | LA | okx | -1095.00% |
| 5 | PROS | okx | -416.41% |
| 6 | PROS | bitget | -369.34% |
| 7 | HOME | bitget | -236.41% |
| 8 | HOME | okx | -189.55% |
| 9 | CL | bitget | -131.62% |
| 10 | MEME | okx | -121.38% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BABY | +1095.00% | okx | -1095.00% | bitget | -2190.00% |
| 2 | LA | +600.17% | okx | -1095.00% | bitget | -1695.17% |
| 3 | EWT | +192.57% | okx | +83.07% | bitget | -109.50% |
| 4 | AAOI | +139.31% | okx | +139.31% | bitget | +0.00% |
| 5 | DRAM | +96.28% | okx | +96.28% | bitget | +0.00% |
| 6 | MU | +86.43% | okx | +87.41% | bitget | +0.99% |
| 7 | NOW | +70.79% | okx | +70.79% | bitget | +0.00% |
| 8 | LPT | +62.74% | bitget | -2.52% | okx | -65.26% |
| 9 | ZEC | +62.32% | bitget | +4.82% | okx | -57.50% |
| 10 | AVGO | +55.93% | okx | +55.93% | bitget | +0.00% |
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
