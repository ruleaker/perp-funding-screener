# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-04 16:27 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1397**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LNG | bitget | +243.64% |
| 2 | VLO | bitget | +232.47% |
| 3 | KTOS | bitget | +218.89% |
| 4 | NOC | bitget | +208.93% |
| 5 | GPRO | bitget | +207.06% |
| 6 | KR200 | okx | +199.56% |
| 7 | PBR | bitget | +167.86% |
| 8 | CORZ | bitget | +159.98% |
| 9 | JPSONY | bitget | +157.68% |
| 10 | LMT | bitget | +154.94% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LSK | bitget | -737.15% |
| 2 | H100 | okx | -551.75% |
| 3 | NU | bitget | -438.00% |
| 4 | CCL | bitget | -425.85% |
| 5 | CSTOCK | bitget | -392.45% |
| 6 | ERA | bitget | -379.09% |
| 7 | SDGR | bitget | -364.09% |
| 8 | CSOPSK2LHKD | bitget | -357.85% |
| 9 | VEEV | bitget | -335.51% |
| 10 | HLT | bitget | -334.96% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +557.22% | bitget | +5.47% | okx | -551.75% |
| 2 | OUST | +223.38% | okx | +0.00% | bitget | -223.38% |
| 3 | KR200 | +218.61% | okx | +199.56% | bitget | -19.05% |
| 4 | ABBV | +210.79% | okx | +0.00% | bitget | -210.79% |
| 5 | GPRO | +207.06% | bitget | +207.06% | okx | +0.00% |
| 6 | AMC | +169.51% | okx | +0.00% | bitget | -169.51% |
| 7 | FWDI | +169.01% | okx | -34.11% | bitget | -203.12% |
| 8 | GILD | +145.74% | okx | +0.00% | bitget | -145.74% |
| 9 | SKHYNIX | +138.06% | bitget | -89.02% | okx | -227.08% |
| 10 | BX | +109.20% | bitget | +143.99% | okx | +34.79% |
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
