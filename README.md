# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-01 20:40 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1385**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | POWER | bitget | +74.90% |
| 2 | GIGADEV | okx | +63.33% |
| 3 | DNA | okx | +47.20% |
| 4 | US100 | okx | +43.45% |
| 5 | KII | okx | +38.84% |
| 6 | FIGHT | bitget | +31.10% |
| 7 | ZEST | bitget | +28.91% |
| 8 | XVG | bitget | +27.27% |
| 9 | BEAT | bitget | +26.83% |
| 10 | SIREN | bitget | +24.20% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOT | bitget | -1600.01% |
| 2 | POWR | bitget | -566.66% |
| 3 | H100 | okx | -425.67% |
| 4 | AKE | okx | -406.64% |
| 5 | COW | bitget | -251.74% |
| 6 | LSK | bitget | -202.47% |
| 7 | AKE | bitget | -178.70% |
| 8 | BX | okx | -140.64% |
| 9 | UNITREE | okx | -121.79% |
| 10 | Q | bitget | -106.87% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +431.15% | bitget | +5.47% | okx | -425.67% |
| 2 | AKE | +227.94% | bitget | -178.70% | okx | -406.64% |
| 3 | BX | +140.64% | bitget | +0.00% | okx | -140.64% |
| 4 | UNITREE | +125.51% | bitget | +3.72% | okx | -121.79% |
| 5 | SOXL | +57.09% | bitget | -18.62% | okx | -75.71% |
| 6 | GMX | +51.01% | bitget | +10.95% | okx | -40.06% |
| 7 | ATOM | +47.16% | bitget | -9.20% | okx | -56.36% |
| 8 | KMNO | +43.48% | bitget | +5.47% | okx | -38.00% |
| 9 | SPCX | +34.38% | bitget | +0.00% | okx | -34.38% |
| 10 | PROS | +33.25% | bitget | +5.47% | okx | -27.77% |
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
