# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-04 19:02 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1233**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MARSCOIN | bitget | +383.25% |
| 2 | ONE | bitget | +251.85% |
| 3 | XMR | bitget | +172.68% |
| 4 | SAMSUNG | okx | +163.95% |
| 5 | GPRO | okx | +154.24% |
| 6 | PONS | bitget | +153.96% |
| 7 | ESPORTS | bitget | +144.21% |
| 8 | SKHYNIX | okx | +130.19% |
| 9 | CSOPSS2LHKD | bitget | +82.78% |
| 10 | IONQ | bitget | +82.67% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -275.06% |
| 2 | CAP | bitget | -273.31% |
| 3 | CAP | okx | -268.73% |
| 4 | ZORA | okx | -215.33% |
| 5 | LA | bitget | -209.25% |
| 6 | ZORA | bitget | -192.17% |
| 7 | INJ | bitget | -135.67% |
| 8 | MINA | bitget | -131.07% |
| 9 | ON | okx | -94.41% |
| 10 | SKR | bitget | -92.53% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +246.38% | bitget | +251.85% | okx | +5.47% |
| 2 | SAMSUNG | +163.95% | okx | +163.95% | bitget | +0.00% |
| 3 | GPRO | +153.58% | okx | +154.24% | bitget | +0.66% |
| 4 | LA | +146.30% | okx | -62.95% | bitget | -209.25% |
| 5 | SKHYNIX | +126.58% | okx | +130.19% | bitget | +3.61% |
| 6 | MINA | +84.96% | okx | -46.11% | bitget | -131.07% |
| 7 | MRNA | +72.16% | bitget | +72.16% | okx | +0.00% |
| 8 | SHEIN | +67.92% | okx | +67.92% | bitget | +0.00% |
| 9 | KIOXIA | +61.94% | okx | +62.82% | bitget | +0.88% |
| 10 | SKDD | +56.73% | okx | +77.09% | bitget | +20.37% |
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
