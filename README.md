# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-26 18:12 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1199**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZHIPU | okx | +166.42% |
| 2 | NET | okx | +76.44% |
| 3 | AVGO | bitget | +69.42% |
| 4 | CBRS | bitget | +68.11% |
| 5 | KIOXIA | okx | +62.69% |
| 6 | ESPORTS | bitget | +61.10% |
| 7 | GFS | bitget | +51.68% |
| 8 | SIREN | bitget | +51.46% |
| 9 | AVGO | okx | +49.44% |
| 10 | ZHIPUHKD | bitget | +48.29% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONG | bitget | -2190.00% |
| 2 | BICO | bitget | -2021.81% |
| 3 | BICO | okx | -1095.00% |
| 4 | EDEN | okx | -895.28% |
| 5 | ACE | bitget | -377.45% |
| 6 | ONT | okx | -355.07% |
| 7 | ONT | bitget | -288.75% |
| 8 | HOME | okx | -285.49% |
| 9 | HOME | bitget | -268.93% |
| 10 | KR200 | okx | -164.06% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BICO | +926.81% | okx | -1095.00% | bitget | -2021.81% |
| 2 | KR200 | +164.06% | bitget | +0.00% | okx | -164.06% |
| 3 | ZHIPU | +128.97% | okx | +166.42% | bitget | +37.45% |
| 4 | SHAZ | +115.75% | bitget | +0.00% | okx | -115.75% |
| 5 | RVN | +100.74% | bitget | -10.84% | okx | -111.58% |
| 6 | TWLO | +80.70% | bitget | +0.00% | okx | -80.70% |
| 7 | ZIL | +78.09% | okx | -3.93% | bitget | -82.02% |
| 8 | NET | +76.44% | okx | +76.44% | bitget | +0.00% |
| 9 | CBRS | +68.11% | bitget | +68.11% | okx | +0.00% |
| 10 | ONT | +66.32% | bitget | -288.75% | okx | -355.07% |
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
