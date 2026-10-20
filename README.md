# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-20 05:04 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1340**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LGELECTRONICS | bitget | +435.48% |
| 2 | NAVER | bitget | +344.05% |
| 3 | KR200 | okx | +284.98% |
| 4 | SIREN | bitget | +227.54% |
| 5 | LGENERGY | bitget | +223.16% |
| 6 | SAMSUNGEM | bitget | +212.76% |
| 7 | SKDD | bitget | +206.85% |
| 8 | SKHYNIX | okx | +200.91% |
| 9 | CYPH | okx | +185.02% |
| 10 | SAMSUNG | okx | +179.94% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITREE | okx | -1095.00% |
| 2 | UNITREE | bitget | -613.64% |
| 3 | CSOPSK2LHKD | bitget | -383.14% |
| 4 | BTW | bitget | -282.51% |
| 5 | SKUU | bitget | -270.79% |
| 6 | CT | bitget | -266.63% |
| 7 | SKDD | okx | -218.74% |
| 8 | SAND | bitget | -206.30% |
| 9 | ERA | bitget | -181.99% |
| 10 | CT | okx | -171.90% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | UNITREE | +481.36% | bitget | -613.64% | okx | -1095.00% |
| 2 | SKDD | +425.58% | bitget | +206.85% | okx | -218.74% |
| 3 | LGELECTRONICS | +394.99% | bitget | +435.48% | okx | +40.49% |
| 4 | NAVER | +344.05% | bitget | +344.05% | okx | +0.00% |
| 5 | SKUU | +310.84% | okx | +40.04% | bitget | -270.79% |
| 6 | AXTI | +169.18% | okx | +0.00% | bitget | -169.18% |
| 7 | ZM | +166.53% | okx | +166.53% | bitget | +0.00% |
| 8 | CYPH | +164.00% | okx | +185.02% | bitget | +21.02% |
| 9 | SAND | +156.74% | okx | -49.56% | bitget | -206.30% |
| 10 | RAM | +155.71% | okx | +0.00% | bitget | -155.71% |
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
