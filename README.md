# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-24 10:31 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | bitget | +307.80% |
| 2 | BOT | bitget | +253.49% |
| 3 | BOT | okx | +124.46% |
| 4 | SKHYNIX | okx | +118.32% |
| 5 | XPD | okx | +110.60% |
| 6 | UNITAS | bitget | +83.22% |
| 7 | QNTSTOCK | bitget | +76.10% |
| 8 | SIREN | bitget | +72.60% |
| 9 | LYN | bitget | +68.88% |
| 10 | COP | bitget | +67.67% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BARD | bitget | -708.25% |
| 2 | TLM | bitget | -647.69% |
| 3 | VANRY | bitget | -530.53% |
| 4 | PROM | bitget | -412.92% |
| 5 | BARD | okx | -308.67% |
| 6 | STX | okx | -269.65% |
| 7 | ORDER | okx | -209.57% |
| 8 | ORDER | bitget | -199.84% |
| 9 | O | okx | -192.86% |
| 10 | O | bitget | -192.61% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BARD | +399.58% | okx | -308.67% | bitget | -708.25% |
| 2 | STX | +202.41% | bitget | -67.23% | okx | -269.65% |
| 3 | BOT | +129.03% | bitget | +253.49% | okx | +124.46% |
| 4 | ALAB | +123.50% | bitget | +0.00% | okx | -123.50% |
| 5 | SKHYNIX | +118.32% | okx | +118.32% | bitget | +0.00% |
| 6 | DATA | +99.96% | bitget | -83.99% | okx | -183.95% |
| 7 | ONE | +89.34% | okx | -30.02% | bitget | -119.36% |
| 8 | QNT | +68.84% | okx | +62.60% | bitget | -6.24% |
| 9 | ZIL | +61.52% | okx | -37.58% | bitget | -99.10% |
| 10 | SAND | +61.11% | bitget | +9.09% | okx | -52.02% |
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
