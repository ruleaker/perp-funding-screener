# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-09 04:43 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **967**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 龙虾 | bitget | +283.06% |
| 2 | FOLKS | bitget | +162.94% |
| 3 | BEAT | bitget | +153.41% |
| 4 | ACU | bitget | +124.39% |
| 5 | SKHYNIX | bitget | +109.50% |
| 6 | XPD | okx | +93.38% |
| 7 | SAMSUNG | bitget | +89.35% |
| 8 | XPD | bitget | +77.96% |
| 9 | BEAT | okx | +74.82% |
| 10 | LYN | bitget | +64.17% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H | okx | -1095.00% |
| 2 | CTR | bitget | -374.16% |
| 3 | ME | okx | -216.50% |
| 4 | SAHARA | okx | -200.03% |
| 5 | HOME | bitget | -199.84% |
| 6 | HOME | okx | -178.19% |
| 7 | SIREN | bitget | -177.94% |
| 8 | STABLE | okx | -167.50% |
| 9 | STABLE | bitget | -148.48% |
| 10 | ESPORTS | bitget | -144.21% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +1096.42% | bitget | +1.42% | okx | -1095.00% |
| 2 | ME | +167.56% | bitget | -48.95% | okx | -216.50% |
| 3 | SAHARA | +119.55% | bitget | -80.48% | okx | -200.03% |
| 4 | ACU | +118.92% | bitget | +124.39% | okx | +5.47% |
| 5 | BEAT | +78.59% | bitget | +153.41% | okx | +74.82% |
| 6 | INFQ | +72.80% | bitget | +0.00% | okx | -72.80% |
| 7 | LAYER | +61.35% | okx | -60.41% | bitget | -121.76% |
| 8 | ZEC | +60.23% | bitget | -56.17% | okx | -116.40% |
| 9 | BAT | +59.11% | bitget | +10.95% | okx | -48.16% |
| 10 | MOVE | +53.66% | bitget | -52.78% | okx | -106.43% |
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
