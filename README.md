# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-03 04:04 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1154**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SUMIELEC | bitget | +328.28% |
| 2 | SNOW | okx | +233.49% |
| 3 | ESPORTS | bitget | +189.87% |
| 4 | AEHR | okx | +109.40% |
| 5 | EWZ | okx | +70.03% |
| 6 | RDDT | okx | +69.02% |
| 7 | COTI | bitget | +65.48% |
| 8 | 龙虾 | bitget | +62.09% |
| 9 | INX | bitget | +60.12% |
| 10 | XPD | okx | +55.59% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | EUL | bitget | -641.45% |
| 2 | KIOXIA | bitget | -547.50% |
| 3 | KIOXIA | okx | -436.37% |
| 4 | LA | bitget | -404.71% |
| 5 | ON | okx | -394.37% |
| 6 | BICO | okx | -343.67% |
| 7 | VANRY | bitget | -339.67% |
| 8 | LA | okx | -325.68% |
| 9 | SYN | bitget | -300.25% |
| 10 | HYPER | bitget | -248.78% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BICO | +260.78% | bitget | -82.89% | okx | -343.67% |
| 2 | SNOW | +257.58% | okx | +233.49% | bitget | -24.09% |
| 3 | FWDI | +192.83% | bitget | +0.00% | okx | -192.83% |
| 4 | TSEM | +155.46% | bitget | +0.00% | okx | -155.46% |
| 5 | KIOXIA | +111.13% | okx | -436.37% | bitget | -547.50% |
| 6 | AEHR | +109.40% | okx | +109.40% | bitget | +0.00% |
| 7 | LA | +79.04% | okx | -325.68% | bitget | -404.71% |
| 8 | SNXX | +76.36% | bitget | +10.84% | okx | -65.51% |
| 9 | CRO | +72.50% | bitget | +10.95% | okx | -61.55% |
| 10 | RDDT | +69.02% | okx | +69.02% | bitget | +0.00% |
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
