# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-25 17:28 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 龙虾 | bitget | +93.51% |
| 2 | 1MCHEEMS | bitget | +63.18% |
| 3 | XVG | bitget | +59.13% |
| 4 | H | okx | +51.65% |
| 5 | SKHYNIX | okx | +44.43% |
| 6 | SNXX | okx | +43.28% |
| 7 | UNITAS | bitget | +41.28% |
| 8 | ARIA | bitget | +40.08% |
| 9 | 1000RATS | bitget | +36.03% |
| 10 | SONIC | bitget | +32.19% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | DEXE | bitget | -421.47% |
| 2 | PROM | bitget | -272.66% |
| 3 | TLM | bitget | -206.41% |
| 4 | SPELL | bitget | -138.63% |
| 5 | BARD | bitget | -137.53% |
| 6 | VANA | bitget | -129.21% |
| 7 | VANA | okx | -122.41% |
| 8 | BARD | okx | -110.77% |
| 9 | VANRY | bitget | -85.30% |
| 10 | ERA | bitget | -67.45% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | STX | +59.35% | okx | +10.95% | bitget | -48.40% |
| 2 | BEAT | +51.73% | bitget | +5.47% | okx | -46.26% |
| 3 | H | +46.18% | okx | +51.65% | bitget | +5.47% |
| 4 | SKHYNIX | +44.43% | okx | +44.43% | bitget | +0.00% |
| 5 | SNXX | +43.28% | okx | +43.28% | bitget | +0.00% |
| 6 | LINEA | +42.60% | okx | +5.47% | bitget | -37.12% |
| 7 | ZIL | +37.58% | okx | -20.67% | bitget | -58.25% |
| 8 | SOXL | +29.67% | okx | +29.67% | bitget | +0.00% |
| 9 | QNT | +29.13% | okx | +0.00% | bitget | -29.13% |
| 10 | IOST | +28.36% | bitget | +10.95% | okx | -17.41% |
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
