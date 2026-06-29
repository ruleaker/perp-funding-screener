# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-29 18:28 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1062**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KIOXIA | okx | +405.80% |
| 2 | TTMI | okx | +220.41% |
| 3 | 龙虾 | bitget | +168.96% |
| 4 | SIREN | bitget | +130.52% |
| 5 | US | bitget | +90.12% |
| 6 | SKHYNIX | okx | +83.84% |
| 7 | STRC | bitget | +65.15% |
| 8 | XPIN | bitget | +63.95% |
| 9 | UB | okx | +61.20% |
| 10 | O | okx | +58.20% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LAB | bitget | -391.35% |
| 2 | LAB | okx | -360.81% |
| 3 | SHLD | okx | -279.58% |
| 4 | POWR | bitget | -257.33% |
| 5 | RE | bitget | -202.68% |
| 6 | TAIKO | bitget | -153.96% |
| 7 | GWEI | bitget | -144.10% |
| 8 | M | bitget | -131.62% |
| 9 | RE | okx | -123.35% |
| 10 | SLX | bitget | -120.01% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KIOXIA | +405.80% | okx | +405.80% | bitget | +0.00% |
| 2 | SKHYNIX | +83.84% | okx | +83.84% | bitget | +0.00% |
| 3 | RE | +79.34% | okx | -123.35% | bitget | -202.68% |
| 4 | ALGO | +66.49% | bitget | +10.95% | okx | -55.54% |
| 5 | STRC | +63.22% | bitget | +65.15% | okx | +1.93% |
| 6 | SLX | +58.57% | okx | -61.45% | bitget | -120.01% |
| 7 | SAMSUNG | +56.12% | okx | +56.12% | bitget | +0.00% |
| 8 | UB | +55.73% | okx | +61.20% | bitget | +5.47% |
| 9 | ARM | +53.09% | okx | +53.09% | bitget | +0.00% |
| 10 | CELO | +48.27% | bitget | -12.15% | okx | -60.43% |
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
