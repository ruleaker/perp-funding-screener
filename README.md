# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-28 17:42 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1049**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +121.33% |
| 2 | KORU | okx | +108.35% |
| 3 | SAMSUNG | okx | +96.52% |
| 4 | 龙虾 | bitget | +78.18% |
| 5 | XVG | bitget | +73.58% |
| 6 | SOXL | okx | +50.38% |
| 7 | H | okx | +48.14% |
| 8 | GWEI | bitget | +36.03% |
| 9 | ESPORTS | bitget | +35.92% |
| 10 | TAG | bitget | +35.59% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | POWR | bitget | -1623.99% |
| 2 | MAGIC | bitget | -657.55% |
| 3 | RE | okx | -630.35% |
| 4 | RE | bitget | -570.28% |
| 5 | MAGIC | okx | -425.58% |
| 6 | LAB | okx | -174.90% |
| 7 | LAB | bitget | -159.32% |
| 8 | AGLD | bitget | -140.16% |
| 9 | TAIKO | bitget | -129.65% |
| 10 | RPL | bitget | -122.09% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | MAGIC | +231.97% | okx | -425.58% | bitget | -657.55% |
| 2 | SKHYNIX | +121.33% | okx | +121.33% | bitget | +0.00% |
| 3 | KORU | +108.35% | okx | +108.35% | bitget | +0.00% |
| 4 | SAMSUNG | +96.52% | okx | +96.52% | bitget | +0.00% |
| 5 | MSTR | +61.66% | bitget | -24.64% | okx | -86.30% |
| 6 | DOT | +61.34% | okx | +2.65% | bitget | -58.69% |
| 7 | RE | +60.07% | bitget | -570.28% | okx | -630.35% |
| 8 | LA | +57.78% | bitget | +5.47% | okx | -52.31% |
| 9 | ORDER | +54.75% | okx | +5.47% | bitget | -49.27% |
| 10 | CRO | +51.54% | okx | -66.06% | bitget | -117.60% |
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
