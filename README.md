# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-16 06:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1413**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LGENERGY | bitget | +1095.00% |
| 2 | LGELECTRONICS | bitget | +1015.72% |
| 3 | SAMSUNGEM | bitget | +983.75% |
| 4 | NAVER | bitget | +703.54% |
| 5 | H100 | okx | +673.20% |
| 6 | HANMI | bitget | +453.66% |
| 7 | BWET | okx | +289.30% |
| 8 | SKDD | bitget | +251.19% |
| 9 | ZHONGJI | bitget | +222.18% |
| 10 | ZHONGJI | okx | +220.77% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKR | bitget | -1553.04% |
| 2 | UNITREE | okx | -761.09% |
| 3 | KAVA | bitget | -712.30% |
| 4 | RARE | bitget | -700.69% |
| 5 | AXIS | okx | -556.26% |
| 6 | AXIS | bitget | -550.89% |
| 7 | BIRB | bitget | -489.90% |
| 8 | SHEINHKD | bitget | -442.60% |
| 9 | NES | okx | -434.15% |
| 10 | SHEIN | okx | -336.01% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LGELECTRONICS | +950.49% | bitget | +1015.72% | okx | +65.23% |
| 2 | NAVER | +729.29% | bitget | +703.54% | okx | -25.75% |
| 3 | H100 | +667.72% | okx | +673.20% | bitget | +5.47% |
| 4 | HANMI | +608.70% | bitget | +453.66% | okx | -155.04% |
| 5 | UNITREE | +440.14% | bitget | -320.94% | okx | -761.09% |
| 6 | SHEIN | +330.21% | bitget | -5.80% | okx | -336.01% |
| 7 | SKDD | +297.16% | bitget | +251.19% | okx | -45.97% |
| 8 | BWET | +154.18% | okx | +289.30% | bitget | +135.12% |
| 9 | FWDI | +147.17% | okx | +96.36% | bitget | -50.81% |
| 10 | LYTE | +144.43% | okx | +0.00% | bitget | -144.43% |
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
