# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-11 02:33 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1171**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +231.50% |
| 2 | BOT | bitget | +173.78% |
| 3 | SKHYNIX | bitget | +160.20% |
| 4 | UNITAS | bitget | +159.65% |
| 5 | 龙虾 | bitget | +140.38% |
| 6 | NG | okx | +115.23% |
| 7 | ELSA | bitget | +110.81% |
| 8 | KORU | bitget | +105.78% |
| 9 | SIREN | bitget | +98.00% |
| 10 | BOT | okx | +96.90% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | PROM | bitget | -2053.12% |
| 2 | KAITO | bitget | -908.08% |
| 3 | EUL | bitget | -313.39% |
| 4 | DOS | okx | -262.88% |
| 5 | HOME | bitget | -260.94% |
| 6 | HOME | okx | -234.20% |
| 7 | KAITO | okx | -222.88% |
| 8 | FWDI | bitget | -106.11% |
| 9 | SOXS | bitget | -65.81% |
| 10 | RE | okx | -64.37% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KAITO | +685.20% | okx | -222.88% | bitget | -908.08% |
| 2 | FWDI | +106.11% | okx | +0.00% | bitget | -106.11% |
| 3 | BICO | +100.41% | bitget | +78.73% | okx | -21.68% |
| 4 | KORU | +92.06% | bitget | +105.78% | okx | +13.72% |
| 5 | BOT | +76.87% | bitget | +173.78% | okx | +96.90% |
| 6 | SOXL | +76.52% | bitget | +92.86% | okx | +16.34% |
| 7 | SKHYNIX | +71.30% | okx | +231.50% | bitget | +160.20% |
| 8 | ME | +66.22% | bitget | +5.47% | okx | -60.75% |
| 9 | SOXS | +65.81% | okx | +0.00% | bitget | -65.81% |
| 10 | PROS | +60.83% | bitget | +20.48% | okx | -40.36% |
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
