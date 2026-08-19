# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-19 16:54 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1192**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +124.28% |
| 2 | XPD | okx | +104.11% |
| 3 | TRUTH | okx | +97.49% |
| 4 | RAM | okx | +85.96% |
| 5 | FOLKS | bitget | +81.14% |
| 6 | BTW | bitget | +78.07% |
| 7 | 1MCHEEMS | bitget | +73.69% |
| 8 | XPD | bitget | +66.36% |
| 9 | SIREN | bitget | +61.21% |
| 10 | META | bitget | +55.30% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | okx | -299.87% |
| 2 | RVN | okx | -289.28% |
| 3 | HOME | bitget | -267.84% |
| 4 | ACE | bitget | -258.53% |
| 5 | BICO | bitget | -167.97% |
| 6 | UNITREE | okx | -150.59% |
| 7 | PROM | bitget | -109.94% |
| 8 | BNT | bitget | -108.62% |
| 9 | SNXX | okx | -105.17% |
| 10 | SHAZ | okx | -100.87% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RVN | +253.80% | bitget | -35.48% | okx | -289.28% |
| 2 | BICO | +158.14% | okx | -9.84% | bitget | -167.97% |
| 3 | UNITREE | +150.59% | bitget | +0.00% | okx | -150.59% |
| 4 | SNXX | +105.17% | bitget | +0.00% | okx | -105.17% |
| 5 | SHAZ | +100.87% | bitget | +0.00% | okx | -100.87% |
| 6 | RAM | +85.96% | okx | +85.96% | bitget | +0.00% |
| 7 | SKHYNIX | +53.36% | bitget | -8.65% | okx | -62.01% |
| 8 | BOT | +50.15% | okx | +0.00% | bitget | -50.15% |
| 9 | TWLO | +47.81% | bitget | +0.00% | okx | -47.81% |
| 10 | BARD | +39.31% | okx | +5.47% | bitget | -33.84% |
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
