# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-03 11:53 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1154**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | QNTSTOCK | bitget | +543.56% |
| 2 | KR200 | okx | +461.61% |
| 3 | RDDT | bitget | +281.41% |
| 4 | BSP | okx | +128.70% |
| 5 | FLY | bitget | +117.60% |
| 6 | QNT | okx | +113.44% |
| 7 | COP | bitget | +91.32% |
| 8 | FWDI | bitget | +90.45% |
| 9 | RAM | okx | +87.06% |
| 10 | ZHIPU | bitget | +65.81% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | WAXP | bitget | -1656.30% |
| 2 | MIRA | bitget | -489.57% |
| 3 | ALAB | bitget | -405.59% |
| 4 | KIOXIA | okx | -388.68% |
| 5 | DEXE | bitget | -216.15% |
| 6 | SYN | bitget | -215.28% |
| 7 | SAMSUNG | okx | -211.77% |
| 8 | ACE | bitget | -196.66% |
| 9 | NIL | bitget | -184.40% |
| 10 | LA | okx | -173.87% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ALAB | +405.59% | okx | +0.00% | bitget | -405.59% |
| 2 | BSP | +293.50% | okx | +128.70% | bitget | -164.80% |
| 3 | RDDT | +281.41% | bitget | +281.41% | okx | +0.00% |
| 4 | KIOXIA | +257.28% | bitget | -131.40% | okx | -388.68% |
| 5 | SAMSUNG | +211.77% | bitget | +0.00% | okx | -211.77% |
| 6 | FWDI | +141.49% | bitget | +90.45% | okx | -51.04% |
| 7 | FLY | +117.60% | bitget | +117.60% | okx | +0.00% |
| 8 | QNT | +102.49% | okx | +113.44% | bitget | +10.95% |
| 9 | SHAZ | +101.34% | bitget | +0.00% | okx | -101.34% |
| 10 | UNH | +94.50% | okx | +0.00% | bitget | -94.50% |
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
