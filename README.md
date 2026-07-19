# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-19 10:05 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1118**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | INTC | okx | +74.01% |
| 2 | SKHYNIX | okx | +72.30% |
| 3 | NBIS | okx | +66.52% |
| 4 | LAB | okx | +64.73% |
| 5 | LITE | okx | +60.30% |
| 6 | FIGHT | bitget | +58.91% |
| 7 | SKHY | okx | +58.25% |
| 8 | SAMSUNG | okx | +52.87% |
| 9 | GEV | okx | +50.52% |
| 10 | 龙虾 | bitget | +49.49% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | -919.58% |
| 2 | TLM | bitget | -654.15% |
| 3 | SPELL | bitget | -308.35% |
| 4 | NEO | okx | -240.63% |
| 5 | NEO | bitget | -211.77% |
| 6 | YB | okx | -115.15% |
| 7 | SENT | okx | -113.43% |
| 8 | SENT | bitget | -111.80% |
| 9 | GWEI | bitget | -106.76% |
| 10 | BILL | okx | -106.27% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | YB | +120.63% | bitget | +5.47% | okx | -115.15% |
| 2 | INTC | +74.01% | okx | +74.01% | bitget | +0.00% |
| 3 | SKHYNIX | +72.30% | okx | +72.30% | bitget | +0.00% |
| 4 | NBIS | +66.52% | okx | +66.52% | bitget | +0.00% |
| 5 | LITE | +60.30% | okx | +60.30% | bitget | +0.00% |
| 6 | SKHY | +58.25% | okx | +58.25% | bitget | +0.00% |
| 7 | SAMSUNG | +52.87% | okx | +52.87% | bitget | +0.00% |
| 8 | DATA | +52.13% | bitget | -27.92% | okx | -80.05% |
| 9 | GEV | +50.52% | okx | +50.52% | bitget | +0.00% |
| 10 | SOPH | +47.69% | bitget | +5.47% | okx | -42.22% |
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
