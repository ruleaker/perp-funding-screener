# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-10 19:09 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **974**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 龙虾 | bitget | +173.67% |
| 2 | BEAT | bitget | +139.83% |
| 3 | GWEI | bitget | +106.00% |
| 4 | LITE | okx | +103.39% |
| 5 | MU | okx | +84.12% |
| 6 | BMNR | okx | +76.16% |
| 7 | QNT | okx | +67.25% |
| 8 | SKYAI | bitget | +54.75% |
| 9 | GOOGL | bitget | +52.56% |
| 10 | NG | okx | +49.60% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | -726.97% |
| 2 | SAHARA | bitget | -344.27% |
| 3 | SAHARA | okx | -234.74% |
| 4 | BLEND | okx | -189.33% |
| 5 | HOME | okx | -177.23% |
| 6 | H | okx | -140.22% |
| 7 | MANTRA | bitget | -136.77% |
| 8 | STG | bitget | -135.56% |
| 9 | CTR | bitget | -108.08% |
| 10 | HOME | bitget | -96.58% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +141.64% | bitget | +1.42% | okx | -140.22% |
| 2 | BEAT | +127.93% | bitget | +139.83% | okx | +11.90% |
| 3 | SAHARA | +109.53% | okx | -234.74% | bitget | -344.27% |
| 4 | LITE | +103.39% | okx | +103.39% | bitget | +0.00% |
| 5 | HOME | +80.65% | bitget | -96.58% | okx | -177.23% |
| 6 | QNT | +60.57% | okx | +67.25% | bitget | +6.68% |
| 7 | GOOGL | +52.56% | bitget | +52.56% | okx | +0.00% |
| 8 | MSFT | +49.17% | bitget | +49.17% | okx | +0.00% |
| 9 | THETA | +43.37% | okx | -7.98% | bitget | -51.36% |
| 10 | QQQ | +40.19% | okx | +40.19% | bitget | +0.00% |
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
