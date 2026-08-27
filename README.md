# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-27 10:04 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1202**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BOT | okx | +419.54% |
| 2 | MARA | okx | +367.22% |
| 3 | WMT | okx | +160.72% |
| 4 | BOT | bitget | +123.19% |
| 5 | QNT | okx | +119.11% |
| 6 | VRT | okx | +117.85% |
| 7 | ZM | okx | +99.42% |
| 8 | XIAOMI | okx | +98.50% |
| 9 | SNXX | okx | +93.55% |
| 10 | SOFTBANK | okx | +82.88% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | OKTA | okx | -900.08% |
| 2 | ARIA | bitget | -562.50% |
| 3 | BICO | bitget | -439.09% |
| 4 | CXMT | okx | -380.33% |
| 5 | CXMT | bitget | -317.11% |
| 6 | ACE | bitget | -276.38% |
| 7 | ONT | bitget | -265.65% |
| 8 | SAND | bitget | -202.25% |
| 9 | ONT | okx | -201.28% |
| 10 | UNITREE | okx | -152.09% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | MARA | +367.22% | okx | +367.22% | bitget | +0.00% |
| 2 | BICO | +367.08% | okx | -72.01% | bitget | -439.09% |
| 3 | BOT | +296.35% | okx | +419.54% | bitget | +123.19% |
| 4 | WMT | +160.72% | okx | +160.72% | bitget | +0.00% |
| 5 | UNITREE | +149.25% | bitget | -2.85% | okx | -152.09% |
| 6 | APP | +127.74% | bitget | +0.00% | okx | -127.74% |
| 7 | VRT | +117.85% | okx | +117.85% | bitget | +0.00% |
| 8 | BSP | +109.72% | bitget | +56.28% | okx | -53.44% |
| 9 | ZIL | +109.40% | okx | -30.76% | bitget | -140.16% |
| 10 | QNT | +108.16% | okx | +119.11% | bitget | +10.95% |
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
