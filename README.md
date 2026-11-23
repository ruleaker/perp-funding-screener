# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-23 07:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1423**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BOT | okx | +345.86% |
| 2 | MSTU | bitget | +131.29% |
| 3 | KSTR | okx | +122.80% |
| 4 | FWDI | bitget | +114.43% |
| 5 | BSP | okx | +112.76% |
| 6 | CSOPSS2LHKD | bitget | +112.57% |
| 7 | LYTE | okx | +85.97% |
| 8 | QQQ | bitget | +82.45% |
| 9 | SNXX | bitget | +76.43% |
| 10 | CSOPSK2LHKD | bitget | +74.57% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AVAV | bitget | -772.41% |
| 2 | POET | bitget | -740.22% |
| 3 | BOTZ | bitget | -643.75% |
| 4 | ACE | bitget | -631.92% |
| 5 | EWZS | okx | -621.97% |
| 6 | WUXIBIO | okx | -605.60% |
| 7 | RGTI | bitget | -563.16% |
| 8 | AAL | bitget | -527.90% |
| 9 | POET | okx | -471.69% |
| 10 | RARE | bitget | -432.09% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | EWZS | +621.97% | bitget | +0.00% | okx | -621.97% |
| 2 | COST | +424.18% | bitget | +0.00% | okx | -424.18% |
| 3 | OKTA | +352.97% | bitget | +0.00% | okx | -352.97% |
| 4 | BOT | +345.86% | okx | +345.86% | bitget | +0.00% |
| 5 | ADI | +318.19% | bitget | +0.00% | okx | -318.19% |
| 6 | INFQ | +317.51% | bitget | +0.00% | okx | -317.51% |
| 7 | XLV | +299.35% | bitget | +0.00% | okx | -299.35% |
| 8 | POET | +268.53% | okx | -471.69% | bitget | -740.22% |
| 9 | CYPH | +216.02% | bitget | +43.47% | okx | -172.55% |
| 10 | INIT | +208.20% | bitget | -149.47% | okx | -357.67% |
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
