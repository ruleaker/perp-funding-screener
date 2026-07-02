# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-02 18:10 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1076**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SNDK | bitget | +145.63% |
| 2 | EVAA | bitget | +135.12% |
| 3 | 龙虾 | bitget | +119.03% |
| 4 | SNDK | okx | +103.31% |
| 5 | SPCX | bitget | +97.24% |
| 6 | KLAC | okx | +94.36% |
| 7 | SOXL | bitget | +94.06% |
| 8 | SOXL | okx | +90.08% |
| 9 | TTMI | okx | +85.52% |
| 10 | MU | bitget | +82.89% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | okx | -1095.00% |
| 2 | BIRB | bitget | -609.37% |
| 3 | BREV | bitget | -562.50% |
| 4 | TLM | bitget | -557.14% |
| 5 | LAB | bitget | -432.85% |
| 6 | SKHYNIX | okx | -378.05% |
| 7 | SAMSUNG | okx | -374.40% |
| 8 | ME | bitget | -362.23% |
| 9 | ARX | bitget | -245.28% |
| 10 | ARX | okx | -234.28% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LAB | +662.15% | bitget | -432.85% | okx | -1095.00% |
| 2 | BREV | +442.93% | okx | -119.57% | bitget | -562.50% |
| 3 | SAMSUNG | +374.40% | bitget | +0.00% | okx | -374.40% |
| 4 | SKHYNIX | +315.09% | bitget | -62.96% | okx | -378.05% |
| 5 | ME | +206.71% | okx | -155.52% | bitget | -362.23% |
| 6 | MINIMAX | +102.48% | okx | -6.37% | bitget | -108.84% |
| 7 | KLAC | +94.36% | okx | +94.36% | bitget | +0.00% |
| 8 | GOOGL | +74.46% | bitget | +74.46% | okx | +0.00% |
| 9 | MU | +73.52% | bitget | +82.89% | okx | +9.38% |
| 10 | KIOXIA | +72.72% | okx | +72.72% | bitget | +0.00% |
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
