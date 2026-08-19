# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-19 09:02 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1192**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SNXX | bitget | +311.31% |
| 2 | SKUU | bitget | +285.47% |
| 3 | KORU | bitget | +278.13% |
| 4 | KR200 | okx | +256.55% |
| 5 | SKHYNIX | bitget | +253.27% |
| 6 | BOT | okx | +209.69% |
| 7 | SKHY | bitget | +190.64% |
| 8 | ZHIPU | okx | +148.05% |
| 9 | MUU | bitget | +142.79% |
| 10 | GIGADEVICE | bitget | +133.70% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITREE | okx | -1095.00% |
| 2 | UNITREE | bitget | -400.00% |
| 3 | SKDD | bitget | -357.96% |
| 4 | PROM | bitget | -253.05% |
| 5 | HOME | okx | -239.43% |
| 6 | RVN | okx | -230.15% |
| 7 | BICO | bitget | -227.76% |
| 8 | HOME | bitget | -199.73% |
| 9 | CXMT | okx | -196.62% |
| 10 | CXMT | bitget | -189.98% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | UNITREE | +695.00% | bitget | -400.00% | okx | -1095.00% |
| 2 | SKDD | +372.74% | okx | +14.78% | bitget | -357.96% |
| 3 | KORU | +278.13% | bitget | +278.13% | okx | +0.00% |
| 4 | SNXX | +273.03% | bitget | +311.31% | okx | +38.28% |
| 5 | BICO | +229.91% | okx | +2.15% | bitget | -227.76% |
| 6 | KR200 | +211.33% | okx | +256.55% | bitget | +45.22% |
| 7 | SKUU | +210.62% | bitget | +285.47% | okx | +74.85% |
| 8 | BOT | +209.69% | okx | +209.69% | bitget | +0.00% |
| 9 | RVN | +192.26% | bitget | -37.89% | okx | -230.15% |
| 10 | SKHY | +190.64% | bitget | +190.64% | okx | +0.00% |
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
