# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-30 19:22 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1209**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | XMR | bitget | +196.77% |
| 2 | ARIA | bitget | +105.56% |
| 3 | LUMIA | bitget | +74.57% |
| 4 | ESPORTS | bitget | +66.25% |
| 5 | UNITAS | bitget | +64.82% |
| 6 | 牛来 | bitget | +63.73% |
| 7 | TOWNS | bitget | +57.05% |
| 8 | XCU | okx | +50.59% |
| 9 | ICX | okx | +45.97% |
| 10 | 龙虾 | bitget | +45.66% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TUT | bitget | -1035.98% |
| 2 | SKR | bitget | -1025.69% |
| 3 | ERA | bitget | -537.21% |
| 4 | RVN | okx | -291.51% |
| 5 | BICO | bitget | -263.89% |
| 6 | SAND | okx | -158.35% |
| 7 | ACE | bitget | -155.49% |
| 8 | AUCTION | okx | -144.44% |
| 9 | BICO | okx | -138.41% |
| 10 | 1000SATS | bitget | -136.98% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RVN | +296.98% | bitget | +5.47% | okx | -291.51% |
| 2 | SAND | +169.30% | bitget | +10.95% | okx | -158.35% |
| 3 | BICO | +125.49% | okx | -138.41% | bitget | -263.89% |
| 4 | STRC | +70.80% | bitget | +0.00% | okx | -70.80% |
| 5 | SLX | +61.54% | okx | +5.47% | bitget | -56.06% |
| 6 | AUCTION | +53.23% | bitget | -91.21% | okx | -144.44% |
| 7 | STX | +49.09% | bitget | +10.95% | okx | -38.14% |
| 8 | UNITREE | +44.44% | bitget | +0.00% | okx | -44.44% |
| 9 | MAGIC | +42.48% | okx | -35.26% | bitget | -77.75% |
| 10 | ONE | +37.77% | bitget | +10.95% | okx | -26.82% |
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
