# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-15 08:52 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1185**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ESPORTS | bitget | +128.88% |
| 2 | APR | okx | +104.41% |
| 3 | APR | bitget | +100.96% |
| 4 | ARIA | bitget | +74.90% |
| 5 | SKYAI | bitget | +71.72% |
| 6 | RAVE | okx | +67.38% |
| 7 | POWER | bitget | +60.55% |
| 8 | LAB | bitget | +51.25% |
| 9 | SIREN | bitget | +48.29% |
| 10 | BROCCOLI | bitget | +45.88% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -2190.00% |
| 2 | ALICE | bitget | -709.34% |
| 3 | CAP | okx | -616.53% |
| 4 | CAP | bitget | -594.91% |
| 5 | BICO | okx | -523.49% |
| 6 | BICO | bitget | -498.66% |
| 7 | HOME | bitget | -307.91% |
| 8 | HOME | okx | -269.10% |
| 9 | RVN | okx | -201.06% |
| 10 | PROM | bitget | -136.11% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RVN | +118.49% | bitget | -82.56% | okx | -201.06% |
| 2 | DOS | +53.06% | bitget | -24.86% | okx | -77.92% |
| 3 | ATOM | +47.52% | okx | +10.95% | bitget | -36.57% |
| 4 | COMP | +43.66% | bitget | +10.95% | okx | -32.71% |
| 5 | RAVE | +43.07% | okx | +67.38% | bitget | +24.31% |
| 6 | STABLE | +42.69% | bitget | -47.74% | okx | -90.43% |
| 7 | HOME | +38.81% | okx | -269.10% | bitget | -307.91% |
| 8 | H | +38.42% | okx | +43.90% | bitget | +5.47% |
| 9 | BABY | +37.98% | bitget | +5.47% | okx | -32.50% |
| 10 | APT | +35.90% | okx | +8.64% | bitget | -27.27% |
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
