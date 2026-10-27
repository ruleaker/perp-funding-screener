# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-27 05:20 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1369**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LGENERGY | bitget | +180.68% |
| 2 | MSTU | okx | +169.61% |
| 3 | CSOPSKHYNIX2L | okx | +168.59% |
| 4 | MEITUAN | bitget | +167.97% |
| 5 | KR200 | okx | +142.06% |
| 6 | CSOPSK2LHKD | bitget | +136.88% |
| 7 | HONHAI | bitget | +133.59% |
| 8 | SHLD | okx | +130.69% |
| 9 | MARA | okx | +124.45% |
| 10 | CXMT | bitget | +115.74% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | UNITREE | okx | -1095.00% |
| 2 | H100 | okx | -1095.00% |
| 3 | IRYS | okx | -757.08% |
| 4 | UNITREE | bitget | -670.69% |
| 5 | DOOD | bitget | -632.58% |
| 6 | DOOD | okx | -615.08% |
| 7 | BIRB | bitget | -485.85% |
| 8 | IOST | okx | -423.36% |
| 9 | HANMI | okx | -306.71% |
| 10 | RUM | okx | -274.82% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +1100.47% | bitget | +5.47% | okx | -1095.00% |
| 2 | IRYS | +584.95% | bitget | -172.13% | okx | -757.08% |
| 3 | UNITREE | +424.31% | bitget | -670.69% | okx | -1095.00% |
| 4 | IOST | +284.41% | bitget | -138.96% | okx | -423.36% |
| 5 | RUM | +267.59% | bitget | -7.23% | okx | -274.82% |
| 6 | MSTU | +169.61% | okx | +169.61% | bitget | +0.00% |
| 7 | BOT | +140.52% | bitget | +0.00% | okx | -140.52% |
| 8 | ORDER | +137.55% | bitget | -27.27% | okx | -164.81% |
| 9 | URNM | +137.50% | bitget | +0.00% | okx | -137.50% |
| 10 | MARA | +124.45% | okx | +124.45% | bitget | +0.00% |
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
