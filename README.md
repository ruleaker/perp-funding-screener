# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-25 09:06 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1199**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | QNT | okx | +266.98% |
| 2 | XIAOMI | okx | +232.48% |
| 3 | FIGHT | bitget | +170.05% |
| 4 | VRT | okx | +159.92% |
| 5 | MINIMAX | okx | +136.41% |
| 6 | POPMART | okx | +121.70% |
| 7 | QNTSTOCK | bitget | +104.79% |
| 8 | MINIMAX | bitget | +103.92% |
| 9 | ZHIPU | okx | +92.15% |
| 10 | XPD | okx | +91.88% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | STORJ | bitget | -1496.32% |
| 2 | UNITREE | okx | -898.26% |
| 3 | ACE | bitget | -507.09% |
| 4 | CXMT | okx | -321.47% |
| 5 | SUPER | bitget | -302.44% |
| 6 | ONT | okx | -266.11% |
| 7 | CXMT | bitget | -262.80% |
| 8 | UNITREE | bitget | -230.06% |
| 9 | ONT | bitget | -208.38% |
| 10 | BICO | bitget | -188.78% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | UNITREE | +668.20% | bitget | -230.06% | okx | -898.26% |
| 2 | QNT | +256.03% | okx | +266.98% | bitget | +10.95% |
| 3 | XIAOMI | +205.87% | okx | +232.48% | bitget | +26.61% |
| 4 | VRT | +159.92% | okx | +159.92% | bitget | +0.00% |
| 5 | POPMART | +112.07% | okx | +121.70% | bitget | +9.64% |
| 6 | SHAZ | +101.16% | bitget | +40.41% | okx | -60.75% |
| 7 | SKDD | +90.91% | okx | +64.85% | bitget | -26.06% |
| 8 | APP | +85.61% | okx | +85.61% | bitget | +0.00% |
| 9 | BICO | +77.69% | okx | -111.09% | bitget | -188.78% |
| 10 | XPD | +68.44% | okx | +91.88% | bitget | +23.43% |
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
