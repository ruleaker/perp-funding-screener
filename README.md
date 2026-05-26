# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-05-26 20:17 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **903**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | WDC | okx | +192.54% |
| 2 | GLW | okx | +141.42% |
| 3 | 龙虾 | bitget | +118.26% |
| 4 | BEAT | bitget | +111.69% |
| 5 | NOKSTOCK | bitget | +107.75% |
| 6 | NBIS | okx | +101.86% |
| 7 | GEV | okx | +96.26% |
| 8 | LAB | bitget | +94.06% |
| 9 | LITE | okx | +89.49% |
| 10 | MRVL | okx | +83.93% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | -2063.86% |
| 2 | DRIFT | bitget | -579.91% |
| 3 | TON | bitget | -278.46% |
| 4 | TON | okx | -179.78% |
| 5 | HOME | bitget | -136.00% |
| 6 | FIDA | bitget | -134.03% |
| 7 | ERA | bitget | -130.20% |
| 8 | STORJ | bitget | -129.87% |
| 9 | SP500 | bitget | -109.50% |
| 10 | CHIP | bitget | -108.30% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | WDC | +192.54% | okx | +192.54% | bitget | +0.00% |
| 2 | NBIS | +101.86% | okx | +101.86% | bitget | +0.00% |
| 3 | TON | +98.68% | okx | -179.78% | bitget | -278.46% |
| 4 | BEAT | +89.33% | bitget | +111.69% | okx | +22.36% |
| 5 | SOXL | +88.48% | okx | +10.95% | bitget | -77.53% |
| 6 | LITE | +81.39% | okx | +89.49% | bitget | +8.10% |
| 7 | MRVL | +78.89% | okx | +83.93% | bitget | +5.04% |
| 8 | LAB | +75.58% | bitget | +94.06% | okx | +18.48% |
| 9 | CRWV | +74.28% | okx | +74.28% | bitget | +0.00% |
| 10 | AAOI | +70.65% | okx | +70.65% | bitget | +0.00% |
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
