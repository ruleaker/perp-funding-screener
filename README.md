# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-27 18:01 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1138**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | NDX100 | bitget | +185.71% |
| 2 | FWDI | bitget | +182.87% |
| 3 | 龙虾 | bitget | +138.74% |
| 4 | PROS | bitget | +130.09% |
| 5 | KORU | okx | +109.41% |
| 6 | SNXX | okx | +92.27% |
| 7 | SNDK | bitget | +76.32% |
| 8 | SKHY | okx | +63.30% |
| 9 | SKHY | bitget | +60.99% |
| 10 | KORU | bitget | +53.00% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | VANRY | bitget | -514.65% |
| 2 | EUL | bitget | -425.63% |
| 3 | SKHYNIX | okx | -334.52% |
| 4 | SAMSUNG | okx | -231.31% |
| 5 | TLM | bitget | -228.85% |
| 6 | SOXS | okx | -210.91% |
| 7 | BARD | bitget | -194.47% |
| 8 | DEXE | bitget | -168.85% |
| 9 | BARD | okx | -166.64% |
| 10 | T | bitget | -165.67% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +334.52% | bitget | +0.00% | okx | -334.52% |
| 2 | SAMSUNG | +231.31% | bitget | +0.00% | okx | -231.31% |
| 3 | FWDI | +182.87% | bitget | +182.87% | okx | +0.00% |
| 4 | SOXS | +161.09% | bitget | -49.82% | okx | -210.91% |
| 5 | PROS | +122.57% | bitget | +130.09% | okx | +7.51% |
| 6 | SNXX | +92.27% | okx | +92.27% | bitget | +0.00% |
| 7 | WOO | +68.05% | bitget | +10.95% | okx | -57.10% |
| 8 | LPT | +63.52% | okx | -31.85% | bitget | -95.37% |
| 9 | IOST | +59.04% | bitget | +10.95% | okx | -48.09% |
| 10 | KORU | +56.41% | okx | +109.41% | bitget | +53.00% |
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
