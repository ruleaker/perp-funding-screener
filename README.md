# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-17 05:23 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1007**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SIREN | bitget | +249.00% |
| 2 | RDW | okx | +248.96% |
| 3 | H | okx | +182.32% |
| 4 | SKHYNIX | bitget | +109.50% |
| 5 | HYUNDAI | bitget | +109.50% |
| 6 | ALAB | okx | +104.80% |
| 7 | SAMSUNG | bitget | +101.94% |
| 8 | BMNR | okx | +91.36% |
| 9 | XVG | bitget | +81.69% |
| 10 | BB | okx | +73.99% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SPACE | bitget | -521.88% |
| 2 | HOME | okx | -352.17% |
| 3 | SPACE | okx | -272.35% |
| 4 | HOME | bitget | -209.36% |
| 5 | SPELL | bitget | -195.90% |
| 6 | FIDA | bitget | -192.94% |
| 7 | ID | bitget | -166.77% |
| 8 | SAHARA | bitget | -162.39% |
| 9 | ORCA | bitget | -127.57% |
| 10 | GWEI | bitget | -116.95% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SPACE | +249.53% | okx | -272.35% | bitget | -521.88% |
| 2 | RDW | +248.96% | okx | +248.96% | bitget | +0.00% |
| 3 | H | +176.85% | okx | +182.32% | bitget | +5.47% |
| 4 | HOME | +142.80% | bitget | -209.36% | okx | -352.17% |
| 5 | BMNR | +91.36% | okx | +91.36% | bitget | +0.00% |
| 6 | SAHARA | +80.63% | okx | -81.76% | bitget | -162.39% |
| 7 | BB | +68.52% | okx | +73.99% | bitget | +5.47% |
| 8 | QNT | +62.27% | bitget | +10.73% | okx | -51.54% |
| 9 | AXTI | +54.15% | okx | +54.15% | bitget | +0.00% |
| 10 | BARD | +52.42% | bitget | +5.47% | okx | -46.94% |
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
