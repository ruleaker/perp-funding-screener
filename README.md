# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-02 11:04 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1074**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +640.83% |
| 2 | FOXA | bitget | +547.50% |
| 3 | HYUNDAI | okx | +318.18% |
| 4 | KIOXIA | okx | +281.92% |
| 5 | CRWD | okx | +208.12% |
| 6 | SOXL | bitget | +167.64% |
| 7 | HPE | bitget | +161.62% |
| 8 | MU | bitget | +141.91% |
| 9 | SAMSUNG | okx | +133.63% |
| 10 | CRCL | bitget | +132.06% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BREV | bitget | -1816.71% |
| 2 | TAIKO | bitget | -814.79% |
| 3 | BIRB | bitget | -704.96% |
| 4 | ME | bitget | -704.19% |
| 5 | GWEI | bitget | -574.44% |
| 6 | OUST | bitget | -547.50% |
| 7 | LAB | okx | -514.32% |
| 8 | ME | okx | -379.91% |
| 9 | BREV | okx | -351.86% |
| 10 | ALAB | bitget | -345.80% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BREV | +1464.86% | okx | -351.86% | bitget | -1816.71% |
| 2 | SKHYNIX | +640.83% | okx | +640.83% | bitget | +0.00% |
| 3 | ALAB | +346.30% | okx | +0.50% | bitget | -345.80% |
| 4 | LAB | +339.34% | bitget | -174.98% | okx | -514.32% |
| 5 | ME | +324.28% | okx | -379.91% | bitget | -704.19% |
| 6 | HYUNDAI | +318.18% | okx | +318.18% | bitget | +0.00% |
| 7 | KIOXIA | +281.92% | okx | +281.92% | bitget | +0.00% |
| 8 | ROK | +194.47% | okx | +0.00% | bitget | -194.47% |
| 9 | HPE | +161.62% | bitget | +161.62% | okx | +0.00% |
| 10 | SAMSUNG | +133.63% | okx | +133.63% | bitget | +0.00% |
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
