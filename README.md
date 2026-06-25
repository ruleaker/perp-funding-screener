# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-25 18:30 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1050**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | WEN | okx | +506.74% |
| 2 | H | okx | +111.02% |
| 3 | GLW | okx | +109.20% |
| 4 | 龙虾 | bitget | +82.12% |
| 5 | SPCX | bitget | +72.49% |
| 6 | ARM | okx | +69.35% |
| 7 | BTW | bitget | +64.61% |
| 8 | SPCX | okx | +59.34% |
| 9 | CRCL | bitget | +57.71% |
| 10 | SMCI | okx | +55.44% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SATSSTOCK | bitget | -547.50% |
| 2 | USO | okx | -380.12% |
| 3 | TNSR | bitget | -333.76% |
| 4 | LAB | okx | -303.39% |
| 5 | RE | okx | -262.76% |
| 6 | NES | okx | -227.19% |
| 7 | RE | bitget | -207.06% |
| 8 | TAIKO | bitget | -132.39% |
| 9 | AGLD | okx | -122.44% |
| 10 | CHIP | okx | -115.81% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LAB | +192.36% | bitget | -111.03% | okx | -303.39% |
| 2 | AGLD | +133.39% | bitget | +10.95% | okx | -122.44% |
| 3 | GLW | +109.20% | okx | +109.20% | bitget | +0.00% |
| 4 | H | +105.54% | okx | +111.02% | bitget | +5.47% |
| 5 | IOST | +77.27% | bitget | +10.95% | okx | -66.32% |
| 6 | ARM | +69.35% | okx | +69.35% | bitget | +0.00% |
| 7 | BB | +68.70% | bitget | +5.47% | okx | -63.22% |
| 8 | BEAT | +56.58% | bitget | +5.47% | okx | -51.11% |
| 9 | RE | +55.70% | bitget | -207.06% | okx | -262.76% |
| 10 | SMCI | +55.44% | okx | +55.44% | bitget | +0.00% |
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
