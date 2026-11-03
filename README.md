# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-03 16:24 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1393**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TWUMC | bitget | +204.33% |
| 2 | AMGN | bitget | +192.72% |
| 3 | NOC | bitget | +159.65% |
| 4 | TWASX | bitget | +155.60% |
| 5 | ABBV | bitget | +152.10% |
| 6 | XLV | bitget | +151.22% |
| 7 | USDESTOCK | bitget | +150.89% |
| 8 | RTXSTOCK | bitget | +147.50% |
| 9 | BAC | bitget | +146.29% |
| 10 | KSTR | okx | +139.77% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | -806.77% |
| 2 | KOPN | bitget | -624.26% |
| 3 | LWLG | bitget | -530.31% |
| 4 | EUV | bitget | -479.50% |
| 5 | SATL | bitget | -449.50% |
| 6 | CLS | bitget | -415.44% |
| 7 | 1000CAT | bitget | -411.72% |
| 8 | XNDU | bitget | -389.16% |
| 9 | GFS | bitget | -369.67% |
| 10 | GNRC | bitget | -359.93% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +806.88% | bitget | +0.11% | okx | -806.77% |
| 2 | SIMO | +356.31% | okx | +0.00% | bitget | -356.31% |
| 3 | OUST | +224.02% | okx | -2.31% | bitget | -226.34% |
| 4 | RUM | +162.83% | okx | +0.00% | bitget | -162.83% |
| 5 | CGNX | +160.97% | okx | +0.00% | bitget | -160.97% |
| 6 | ABBV | +152.10% | bitget | +152.10% | okx | +0.00% |
| 7 | BAC | +146.29% | bitget | +146.29% | okx | +0.00% |
| 8 | KSTR | +134.30% | okx | +139.77% | bitget | +5.47% |
| 9 | KR200 | +119.21% | okx | +119.21% | bitget | +0.00% |
| 10 | ADI | +110.70% | okx | +0.00% | bitget | -110.70% |
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
