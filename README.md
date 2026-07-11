# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-11 03:50 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1102**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | okx | +91.24% |
| 2 | SIREN | bitget | +83.33% |
| 3 | ESPORTS | bitget | +81.80% |
| 4 | SPCX | okx | +78.77% |
| 5 | LAB | bitget | +70.19% |
| 6 | MSTR | okx | +65.36% |
| 7 | STRC | okx | +60.39% |
| 8 | TUT | bitget | +52.12% |
| 9 | AAOI | okx | +47.63% |
| 10 | PIPPIN | bitget | +46.54% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | PARTI | bitget | -663.24% |
| 2 | PARTI | okx | -638.53% |
| 3 | SKL | bitget | -463.08% |
| 4 | IOTA | okx | -256.76% |
| 5 | IOTA | bitget | -216.70% |
| 6 | GWEI | bitget | -149.58% |
| 7 | RE | okx | -132.12% |
| 8 | KAT | bitget | -132.06% |
| 9 | AI | okx | -108.36% |
| 10 | VANRY | bitget | -105.67% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KAT | +86.58% | okx | -45.48% | bitget | -132.06% |
| 2 | LA | +85.30% | okx | +5.47% | bitget | -79.83% |
| 3 | SPCX | +78.77% | okx | +78.77% | bitget | +0.00% |
| 4 | RVN | +69.00% | bitget | +5.37% | okx | -63.64% |
| 5 | MSTR | +65.36% | okx | +65.36% | bitget | +0.00% |
| 6 | STRC | +60.39% | okx | +60.39% | bitget | +0.00% |
| 7 | AAOI | +47.63% | okx | +47.63% | bitget | +0.00% |
| 8 | RE | +44.74% | bitget | -87.38% | okx | -132.12% |
| 9 | IOTA | +40.06% | bitget | -216.70% | okx | -256.76% |
| 10 | BAT | +38.76% | okx | +10.95% | bitget | -27.81% |
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
