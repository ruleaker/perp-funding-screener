# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-01 15:21 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1385**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GIGADEV | okx | +227.04% |
| 2 | OFC | okx | +83.30% |
| 3 | ARIA | bitget | +59.13% |
| 4 | KII | okx | +55.62% |
| 5 | ZHONGJI | bitget | +53.87% |
| 6 | ZHONGJI | okx | +53.26% |
| 7 | XVG | bitget | +51.36% |
| 8 | DNA | okx | +50.34% |
| 9 | FIGHT | bitget | +46.10% |
| 10 | SIREN | bitget | +45.88% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | POWR | bitget | -1658.38% |
| 2 | FLOCK | bitget | -491.87% |
| 3 | FLOCK | okx | -457.59% |
| 4 | G | bitget | -270.57% |
| 5 | AKE | okx | -243.23% |
| 6 | POWER | bitget | -146.40% |
| 7 | LSK | bitget | -142.35% |
| 8 | 1MBABYDOGE | bitget | -98.00% |
| 9 | BLUR | bitget | -97.56% |
| 10 | COW | bitget | -96.69% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | AKE | +248.70% | bitget | +5.47% | okx | -243.23% |
| 2 | BX | +77.15% | bitget | +0.00% | okx | -77.15% |
| 3 | IOST | +69.29% | bitget | -15.88% | okx | -85.17% |
| 4 | UNITREE | +63.02% | bitget | +0.00% | okx | -63.02% |
| 5 | ATOM | +43.61% | bitget | -12.04% | okx | -55.66% |
| 6 | MANA | +41.77% | bitget | +10.95% | okx | -30.82% |
| 7 | AERO | +35.00% | okx | +1.93% | bitget | -33.07% |
| 8 | FLOCK | +34.28% | okx | -457.59% | bitget | -491.87% |
| 9 | O | +33.17% | okx | +38.64% | bitget | +5.47% |
| 10 | SOXL | +30.46% | bitget | +0.00% | okx | -30.46% |
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
