# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-12 18:22 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **982**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 龙虾 | bitget | +194.80% |
| 2 | SAMSUNG | okx | +179.69% |
| 3 | ROK | okx | +173.84% |
| 4 | SKHYNIX | okx | +154.19% |
| 5 | BEAT | okx | +120.03% |
| 6 | GWEI | bitget | +118.59% |
| 7 | VELVET | bitget | +88.59% |
| 8 | BLESS | bitget | +80.26% |
| 9 | DEXE | bitget | +74.90% |
| 10 | ARIA | bitget | +74.46% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | STG | bitget | -2299.50% |
| 2 | ESPORTS | bitget | -780.08% |
| 3 | H | okx | -605.82% |
| 4 | ENJ | okx | -290.88% |
| 5 | ENJ | bitget | -282.84% |
| 6 | HOME | bitget | -264.00% |
| 7 | HOME | okx | -234.40% |
| 8 | SAHARA | bitget | -158.67% |
| 9 | SAHARA | okx | -148.96% |
| 10 | SOPH | okx | -127.48% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +587.32% | bitget | -18.51% | okx | -605.82% |
| 2 | SAMSUNG | +179.69% | okx | +179.69% | bitget | +0.00% |
| 3 | SKHYNIX | +154.19% | okx | +154.19% | bitget | +0.00% |
| 4 | SOPH | +132.96% | bitget | +5.47% | okx | -127.48% |
| 5 | BEAT | +114.56% | okx | +120.03% | bitget | +5.47% |
| 6 | AAOI | +67.02% | okx | +67.02% | bitget | +0.00% |
| 7 | GLW | +54.54% | okx | +54.54% | bitget | +0.00% |
| 8 | CRV | +50.59% | okx | +10.95% | bitget | -39.64% |
| 9 | LITE | +50.27% | okx | +50.27% | bitget | +0.00% |
| 10 | META | +50.06% | bitget | +53.33% | okx | +3.27% |
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
