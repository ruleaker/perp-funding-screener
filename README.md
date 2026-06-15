# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-15 20:01 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **993**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SIREN | bitget | +488.04% |
| 2 | FOLKS | bitget | +210.68% |
| 3 | SKHYNIX | okx | +118.35% |
| 4 | XVG | bitget | +112.68% |
| 5 | SAMSUNG | okx | +100.64% |
| 6 | GEV | okx | +99.55% |
| 7 | EPIC | bitget | +94.50% |
| 8 | CARV | bitget | +91.10% |
| 9 | DRAM | bitget | +86.29% |
| 10 | MU | bitget | +79.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FIDA | bitget | -1397.33% |
| 2 | SPELL | bitget | -335.18% |
| 3 | HOME | okx | -281.19% |
| 4 | ZKC | bitget | -279.23% |
| 5 | STG | bitget | -236.08% |
| 6 | SAHARA | okx | -234.50% |
| 7 | SAHARA | bitget | -188.78% |
| 8 | HOME | bitget | -165.78% |
| 9 | TON | okx | -127.44% |
| 10 | SYN | bitget | -96.36% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +118.35% | okx | +118.35% | bitget | +0.00% |
| 2 | HOME | +115.41% | bitget | -165.78% | okx | -281.19% |
| 3 | SAMSUNG | +100.64% | okx | +100.64% | bitget | +0.00% |
| 4 | MOODENG | +70.08% | okx | +5.47% | bitget | -64.61% |
| 5 | H | +69.69% | okx | +71.12% | bitget | +1.42% |
| 6 | OPG | +63.25% | bitget | +5.47% | okx | -57.78% |
| 7 | ORDI | +62.41% | okx | +5.47% | bitget | -56.94% |
| 8 | 0G | +62.09% | okx | +5.47% | bitget | -56.61% |
| 9 | MRVL | +61.21% | bitget | +61.21% | okx | +0.00% |
| 10 | MU | +60.70% | bitget | +79.50% | okx | +18.80% |
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
