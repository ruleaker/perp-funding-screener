# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-25 17:03 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1200**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | GFS | bitget | +342.41% |
| 2 | QNT | okx | +129.70% |
| 3 | GEV | okx | +119.21% |
| 4 | SOFTBANK | okx | +102.83% |
| 5 | ESPORTS | bitget | +93.62% |
| 6 | LYTE | okx | +91.34% |
| 7 | FIGHT | bitget | +88.80% |
| 8 | UNITREE | okx | +79.73% |
| 9 | CBRS | bitget | +79.50% |
| 10 | INFQ | okx | +69.27% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | STORJ | bitget | -832.64% |
| 2 | TLM | bitget | -442.71% |
| 3 | RVN | bitget | -257.43% |
| 4 | RVN | okx | -184.21% |
| 5 | KR200 | okx | -173.75% |
| 6 | BICO | bitget | -126.91% |
| 7 | ONT | okx | -122.37% |
| 8 | HOME | bitget | -116.95% |
| 9 | ONT | bitget | -116.62% |
| 10 | HOME | okx | -110.73% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | KR200 | +173.75% | bitget | +0.00% | okx | -173.75% |
| 2 | GEV | +119.21% | okx | +119.21% | bitget | +0.00% |
| 3 | QNT | +118.75% | okx | +129.70% | bitget | +10.95% |
| 4 | LYTE | +91.34% | okx | +91.34% | bitget | +0.00% |
| 5 | RVN | +73.23% | okx | -184.21% | bitget | -257.43% |
| 6 | BICO | +72.16% | okx | -54.76% | bitget | -126.91% |
| 7 | INFQ | +69.27% | okx | +69.27% | bitget | +0.00% |
| 8 | UNITREE | +53.01% | okx | +79.73% | bitget | +26.72% |
| 9 | STABLE | +51.57% | okx | +1.42% | bitget | -50.15% |
| 10 | MUU | +48.40% | okx | +0.00% | bitget | -48.40% |
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
