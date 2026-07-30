# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-30 17:54 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1153**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZHIPU | okx | +689.09% |
| 2 | FWDI | bitget | +442.82% |
| 3 | SKHYNIX | okx | +429.44% |
| 4 | SAMSUNG | okx | +391.33% |
| 5 | KR200 | okx | +321.73% |
| 6 | KIOXIA | okx | +315.94% |
| 7 | ZHIPU | bitget | +152.42% |
| 8 | SHAZ | bitget | +133.37% |
| 9 | MINIMAX | okx | +123.27% |
| 10 | ZHIPUHKD | bitget | +102.93% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LA | bitget | -989.55% |
| 2 | LA | okx | -395.97% |
| 3 | GRVT | okx | -371.27% |
| 4 | DEXE | bitget | -335.51% |
| 5 | VANRY | bitget | -315.80% |
| 6 | INTW | okx | -232.73% |
| 7 | EUL | bitget | -218.23% |
| 8 | ESP | okx | -187.57% |
| 9 | KOPN | bitget | -152.42% |
| 10 | GRVT | bitget | -145.20% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LA | +593.58% | okx | -395.97% | bitget | -989.55% |
| 2 | ZHIPU | +536.66% | okx | +689.09% | bitget | +152.42% |
| 3 | FWDI | +442.82% | bitget | +442.82% | okx | +0.00% |
| 4 | SAMSUNG | +391.33% | okx | +391.33% | bitget | +0.00% |
| 5 | SKHYNIX | +370.53% | okx | +429.44% | bitget | +58.91% |
| 6 | KIOXIA | +315.94% | okx | +315.94% | bitget | +0.00% |
| 7 | GRVT | +226.07% | bitget | -145.20% | okx | -371.27% |
| 8 | INTW | +188.49% | bitget | -44.24% | okx | -232.73% |
| 9 | BOT | +136.00% | okx | +0.00% | bitget | -136.00% |
| 10 | SHAZ | +133.37% | bitget | +133.37% | okx | +0.00% |
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
