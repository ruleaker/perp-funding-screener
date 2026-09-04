# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-04 12:49 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1231**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AMC | bitget | +547.50% |
| 2 | GTLB | bitget | +375.26% |
| 3 | GPRO | bitget | +342.95% |
| 4 | BNC | bitget | +217.58% |
| 5 | ONE | bitget | +196.11% |
| 6 | XMR | bitget | +163.92% |
| 7 | SHEIN | okx | +138.93% |
| 8 | IONQ | okx | +137.63% |
| 9 | ZS | bitget | +137.42% |
| 10 | ESPORTS | bitget | +132.06% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -346.68% |
| 2 | ICX | okx | -329.66% |
| 3 | LA | bitget | -301.78% |
| 4 | CYS | bitget | -286.45% |
| 5 | SIGN | okx | -250.06% |
| 6 | CAP | bitget | -241.12% |
| 7 | CAP | okx | -220.56% |
| 8 | SIGN | bitget | -194.91% |
| 9 | BX | okx | -174.76% |
| 10 | LA | okx | -168.48% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | AMC | +460.09% | bitget | +547.50% | okx | +87.41% |
| 2 | ONE | +190.64% | bitget | +196.11% | okx | +5.47% |
| 3 | BX | +174.76% | bitget | +0.00% | okx | -174.76% |
| 4 | BSP | +163.71% | bitget | +0.00% | okx | -163.71% |
| 5 | LA | +133.30% | okx | -168.48% | bitget | -301.78% |
| 6 | FLY | +110.05% | bitget | +110.05% | okx | +0.00% |
| 7 | KIOXIA | +101.17% | okx | +101.17% | bitget | +0.00% |
| 8 | SKHYNIX | +93.65% | bitget | -39.97% | okx | -133.61% |
| 9 | SHEIN | +91.52% | okx | +138.93% | bitget | +47.41% |
| 10 | CP | +75.97% | okx | +81.45% | bitget | +5.47% |
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
