# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-05 16:37 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1409**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +692.97% |
| 2 | LWLG | bitget | +394.20% |
| 3 | OUST | bitget | +319.52% |
| 4 | GFS | bitget | +315.14% |
| 5 | NG | okx | +301.60% |
| 6 | ECHO | bitget | +301.23% |
| 7 | OKTA | bitget | +286.67% |
| 8 | FTNT | bitget | +260.06% |
| 9 | AVAV | bitget | +254.81% |
| 10 | DASHSTOCK | bitget | +253.16% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HUMA | okx | -1023.17% |
| 2 | CSOPSK2LHKD | bitget | -776.03% |
| 3 | CSOPSS2LHKD | bitget | -724.89% |
| 4 | ZHONGJI | bitget | -647.36% |
| 5 | TWASX | bitget | -584.73% |
| 6 | CXMT | okx | -530.73% |
| 7 | ZHONGJI | okx | -514.78% |
| 8 | XTZ | okx | -479.66% |
| 9 | SOFTBANK | bitget | -474.46% |
| 10 | KIOXIA | bitget | -473.37% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HUMA | +703.76% | bitget | -319.41% | okx | -1023.17% |
| 2 | H100 | +687.49% | okx | +692.97% | bitget | +5.47% |
| 3 | SOFTBANK | +474.46% | okx | +0.00% | bitget | -474.46% |
| 4 | KIOXIA | +435.82% | okx | -37.54% | bitget | -473.37% |
| 5 | XTZ | +370.81% | bitget | -108.84% | okx | -479.66% |
| 6 | MURATA | +331.02% | okx | +0.00% | bitget | -331.02% |
| 7 | OUST | +297.29% | bitget | +319.52% | okx | +22.23% |
| 8 | OKTA | +286.67% | bitget | +286.67% | okx | +0.00% |
| 9 | SAMSUNG | +225.83% | bitget | -163.48% | okx | -389.32% |
| 10 | KR200 | +210.71% | okx | +100.45% | bitget | -110.27% |
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
