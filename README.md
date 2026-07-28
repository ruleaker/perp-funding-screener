# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-28 10:56 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1138**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ARQQ | bitget | +389.60% |
| 2 | SKHYNIX | okx | +366.09% |
| 3 | KR200 | okx | +261.29% |
| 4 | MINIMAX | okx | +253.74% |
| 5 | SAMSUNG | okx | +239.40% |
| 6 | FWDI | okx | +229.64% |
| 7 | BUD | bitget | +220.75% |
| 8 | KIOXIA | okx | +198.26% |
| 9 | NDX100 | bitget | +174.76% |
| 10 | ZHIPU | okx | +164.38% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LA | bitget | -1590.16% |
| 2 | VANRY | bitget | -1002.91% |
| 3 | LA | okx | -598.91% |
| 4 | BOT | bitget | -469.76% |
| 5 | TLM | bitget | -355.44% |
| 6 | SOXS | okx | -250.96% |
| 7 | AEON | bitget | -207.61% |
| 8 | SPELL | bitget | -176.84% |
| 9 | BOT | okx | -168.62% |
| 10 | COTI | bitget | -147.39% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LA | +991.25% | okx | -598.91% | bitget | -1590.16% |
| 2 | SKHYNIX | +366.09% | okx | +366.09% | bitget | +0.00% |
| 3 | BOT | +301.13% | okx | -168.62% | bitget | -469.76% |
| 4 | FWDI | +245.30% | okx | +229.64% | bitget | -15.66% |
| 5 | SAMSUNG | +239.40% | okx | +239.40% | bitget | +0.00% |
| 6 | SOXS | +235.96% | bitget | -15.00% | okx | -250.96% |
| 7 | KIOXIA | +198.26% | okx | +198.26% | bitget | +0.00% |
| 8 | ROK | +141.44% | bitget | +0.00% | okx | -141.44% |
| 9 | SNXX | +133.59% | okx | +133.59% | bitget | +0.00% |
| 10 | MINIMAX | +115.34% | okx | +253.74% | bitget | +138.41% |
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
