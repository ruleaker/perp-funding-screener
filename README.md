# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-01 17:29 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1154**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | APR | bitget | +124.17% |
| 2 | 龙虾 | bitget | +102.60% |
| 3 | ARIA | bitget | +101.94% |
| 4 | US | bitget | +69.53% |
| 5 | LAB | okx | +64.35% |
| 6 | FOLKS | bitget | +41.94% |
| 7 | LIGHT | okx | +41.70% |
| 8 | SOON | bitget | +40.95% |
| 9 | SIREN | bitget | +38.76% |
| 10 | BSB | bitget | +32.74% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SYN | bitget | -250.97% |
| 2 | LA | okx | -200.69% |
| 3 | LA | bitget | -168.30% |
| 4 | MMT | bitget | -142.46% |
| 5 | MMT | okx | -141.92% |
| 6 | EUL | bitget | -139.39% |
| 7 | AEVO | okx | -124.33% |
| 8 | VANRY | bitget | -113.11% |
| 9 | VANA | okx | -110.58% |
| 10 | SKHYNIX | okx | -101.18% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | APR | +118.70% | bitget | +124.17% | okx | +5.47% |
| 2 | SKHYNIX | +101.18% | bitget | +0.00% | okx | -101.18% |
| 3 | BAND | +90.58% | bitget | +10.95% | okx | -79.63% |
| 4 | RAY | +70.54% | bitget | +4.71% | okx | -65.84% |
| 5 | AEVO | +66.85% | bitget | -57.49% | okx | -124.33% |
| 6 | CRO | +66.16% | bitget | +10.07% | okx | -56.09% |
| 7 | DRAM | +51.39% | bitget | +0.00% | okx | -51.39% |
| 8 | LAB | +49.35% | okx | +64.35% | bitget | +15.00% |
| 9 | AEON | +46.99% | bitget | -38.11% | okx | -85.10% |
| 10 | ENS | +46.98% | okx | +10.95% | bitget | -36.03% |
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
