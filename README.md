# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-20 10:56 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1021**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BTW | bitget | +409.86% |
| 2 | US | bitget | +152.10% |
| 3 | SKHYNIX | okx | +129.56% |
| 4 | SMH | okx | +113.77% |
| 5 | SIREN | bitget | +108.51% |
| 6 | ESPORTS | bitget | +96.47% |
| 7 | O | okx | +91.41% |
| 8 | URNM | okx | +85.31% |
| 9 | MSTR | okx | +74.52% |
| 10 | INTC | okx | +52.59% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H | okx | -1095.00% |
| 2 | HOME | okx | -455.84% |
| 3 | H | bitget | -454.64% |
| 4 | BICO | okx | -348.08% |
| 5 | RE | bitget | -305.61% |
| 6 | ALICE | bitget | -278.02% |
| 7 | FIDA | bitget | -250.54% |
| 8 | RARE | bitget | -230.83% |
| 9 | SAHARA | okx | -137.35% |
| 10 | SPELL | bitget | -97.02% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +640.36% | bitget | -454.64% | okx | -1095.00% |
| 2 | HOME | +368.35% | bitget | -87.49% | okx | -455.84% |
| 3 | BICO | +359.03% | bitget | +10.95% | okx | -348.08% |
| 4 | RE | +233.88% | okx | -71.74% | bitget | -305.61% |
| 5 | SKHYNIX | +129.56% | okx | +129.56% | bitget | +0.00% |
| 6 | SMH | +113.77% | okx | +113.77% | bitget | +0.00% |
| 7 | MSTR | +74.52% | okx | +74.52% | bitget | +0.00% |
| 8 | AXS | +71.12% | bitget | +4.27% | okx | -66.85% |
| 9 | SAHARA | +68.15% | bitget | -69.20% | okx | -137.35% |
| 10 | ANIME | +67.28% | bitget | -23.32% | okx | -90.60% |
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
