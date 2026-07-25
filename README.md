# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-25 10:06 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FIGHT | bitget | +149.58% |
| 2 | UNITAS | bitget | +92.09% |
| 3 | 1MCHEEMS | bitget | +67.67% |
| 4 | LYN | bitget | +66.58% |
| 5 | UP | okx | +44.10% |
| 6 | TRUTH | okx | +40.21% |
| 7 | BSB | okx | +39.14% |
| 8 | SIREN | bitget | +30.33% |
| 9 | M | bitget | +25.73% |
| 10 | MYX | bitget | +25.40% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GWEI | bitget | -675.94% |
| 2 | PROM | bitget | -592.61% |
| 3 | BARD | bitget | -403.29% |
| 4 | BARD | okx | -394.98% |
| 5 | ACE | bitget | -276.60% |
| 6 | TLM | bitget | -203.67% |
| 7 | MORPHO | okx | -179.76% |
| 8 | MORPHO | bitget | -168.30% |
| 9 | TNSR | bitget | -150.67% |
| 10 | BE | okx | -116.88% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BE | +116.88% | bitget | +0.00% | okx | -116.88% |
| 2 | PENG | +96.62% | okx | +15.80% | bitget | -80.81% |
| 3 | SSV | +73.38% | bitget | +10.95% | okx | -62.43% |
| 4 | RVN | +54.31% | bitget | +5.47% | okx | -48.84% |
| 5 | BEAT | +51.78% | bitget | +5.47% | okx | -46.31% |
| 6 | PENDLE | +49.93% | okx | +5.47% | bitget | -44.46% |
| 7 | ONE | +41.30% | bitget | +10.95% | okx | -30.35% |
| 8 | BSB | +33.66% | okx | +39.14% | bitget | +5.47% |
| 9 | RSR | +31.31% | bitget | +10.95% | okx | -20.36% |
| 10 | ESP | +30.62% | bitget | -14.23% | okx | -44.86% |
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
