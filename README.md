# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-27 04:31 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1050**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SIREN | bitget | +125.38% |
| 2 | 龙虾 | bitget | +70.30% |
| 3 | MSTR | okx | +62.06% |
| 4 | US | bitget | +55.95% |
| 5 | SAMSUNG | okx | +51.92% |
| 6 | KORU | okx | +50.40% |
| 7 | CRCL | okx | +49.49% |
| 8 | MU | okx | +38.94% |
| 9 | UP | okx | +33.56% |
| 10 | FIGHT | bitget | +32.52% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ARK | bitget | -2099.22% |
| 2 | AGLD | bitget | -717.88% |
| 3 | AGLD | okx | -630.09% |
| 4 | LAB | okx | -460.46% |
| 5 | LAB | bitget | -412.27% |
| 6 | BICO | okx | -367.68% |
| 7 | BICO | bitget | -290.61% |
| 8 | BTW | bitget | -277.58% |
| 9 | RE | bitget | -244.08% |
| 10 | RE | okx | -236.09% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | O | +222.98% | bitget | +2.63% | okx | -220.35% |
| 2 | LA | +149.02% | okx | -2.74% | bitget | -151.77% |
| 3 | GLM | +147.96% | okx | +2.11% | bitget | -145.85% |
| 4 | AGLD | +87.80% | okx | -630.09% | bitget | -717.88% |
| 5 | BABY | +78.62% | okx | +5.47% | bitget | -73.15% |
| 6 | BICO | +77.07% | bitget | -290.61% | okx | -367.68% |
| 7 | QNT | +66.63% | bitget | +10.95% | okx | -55.68% |
| 8 | MSTR | +62.06% | okx | +62.06% | bitget | +0.00% |
| 9 | CELO | +53.60% | bitget | +10.95% | okx | -42.65% |
| 10 | SAMSUNG | +51.92% | okx | +51.92% | bitget | +0.00% |
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
