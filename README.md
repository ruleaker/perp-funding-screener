# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-21 09:06 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1196**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | COPPER | bitget | +547.50% |
| 2 | ZHIPU | okx | +188.16% |
| 3 | ZHIPU | bitget | +148.15% |
| 4 | XPD | okx | +110.24% |
| 5 | GEV | okx | +109.60% |
| 6 | BOT | okx | +108.59% |
| 7 | QNT | okx | +96.19% |
| 8 | POWER | bitget | +91.98% |
| 9 | 4 | bitget | +75.45% |
| 10 | LIGHT | okx | +66.22% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITREE | okx | -966.76% |
| 2 | ONT | bitget | -640.25% |
| 3 | CXMT | okx | -558.29% |
| 4 | CXMT | bitget | -547.50% |
| 5 | BICO | bitget | -392.34% |
| 6 | ONG | bitget | -383.14% |
| 7 | UNITREE | bitget | -301.34% |
| 8 | ONT | okx | -263.99% |
| 9 | RVN | okx | -202.77% |
| 10 | BICO | okx | -187.74% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | UNITREE | +665.42% | bitget | -301.34% | okx | -966.76% |
| 2 | ONT | +376.26% | okx | -263.99% | bitget | -640.25% |
| 3 | BICO | +204.60% | okx | -187.74% | bitget | -392.34% |
| 4 | RVN | +189.08% | bitget | -13.69% | okx | -202.77% |
| 5 | BX | +125.07% | bitget | +0.00% | okx | -125.07% |
| 6 | GEV | +109.60% | okx | +109.60% | bitget | +0.00% |
| 7 | BOT | +108.49% | okx | +108.59% | bitget | +0.11% |
| 8 | FWDI | +86.19% | bitget | +0.00% | okx | -86.19% |
| 9 | QNT | +85.24% | okx | +96.19% | bitget | +10.95% |
| 10 | ICX | +68.56% | bitget | +5.47% | okx | -63.09% |
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
