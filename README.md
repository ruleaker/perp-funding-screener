# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-03 19:21 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **2825**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | RDW | bybit | +245.69% |
| 2 | GPRO | binance | +242.24% |
| 3 | GPRO | bybit | +233.34% |
| 4 | GPRO | bitget | +223.27% |
| 5 | POET | bybit | +220.13% |
| 6 | ONE | okx | +220.11% |
| 7 | CSOPSKHYNIX2L | binance | +210.66% |
| 8 | SOFTBANK | okx | +201.68% |
| 9 | ESPORTS | bybit | +200.46% |
| 10 | ARKK | bybit | +189.47% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ANKR | bybit | -578.10% |
| 2 | ANKR | bitget | -435.59% |
| 3 | PUFFER | bybit | -418.74% |
| 4 | ANKR | binance | -405.46% |
| 5 | CAP | binance | -369.40% |
| 6 | CAP | bitget | -364.96% |
| 7 | ACE | binance | -357.12% |
| 8 | CAP | okx | -348.56% |
| 9 | ACE | bitget | -338.03% |
| 10 | CAP | bybit | -332.68% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | PUFFER | +418.74% | binance | +0.00% | bybit | -418.74% |
| 2 | RDW | +245.69% | bybit | +245.69% | bitget | +0.00% |
| 3 | POET | +220.13% | bybit | +220.13% | okx | +0.00% |
| 4 | ONE | +214.64% | okx | +220.11% | binance | +5.47% |
| 5 | STORJ | +193.02% | binance | +0.00% | bybit | -193.02% |
| 6 | ANKR | +172.64% | binance | -405.46% | bybit | -578.10% |
| 7 | CASHCAT | +167.48% | okx | +172.96% | bybit | +5.48% |
| 8 | CSOPSAMSUNG2L | +150.60% | binance | +150.60% | bybit | +0.00% |
| 9 | ESPORTS | +146.08% | bybit | +200.46% | binance | +54.38% |
| 10 | CSOPSKHYNIX2L | +145.95% | binance | +210.66% | bybit | +64.71% |
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
