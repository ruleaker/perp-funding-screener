# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-30 20:56 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1385**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AGPU | bitget | +413.25% |
| 2 | USDESTOCK | bitget | +341.20% |
| 3 | AKE | bitget | +335.95% |
| 4 | ROK | okx | +221.98% |
| 5 | INTW | okx | +190.50% |
| 6 | KSTR | okx | +184.74% |
| 7 | KR200 | okx | +172.23% |
| 8 | XPT | okx | +124.66% |
| 9 | LWLG | bitget | +104.90% |
| 10 | INTW | bitget | +95.05% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SOPH | bitget | -1647.54% |
| 2 | BLUR | bitget | -1377.07% |
| 3 | SOPH | okx | -816.51% |
| 4 | BLUR | okx | -644.13% |
| 5 | HOT | bitget | -357.96% |
| 6 | H100 | okx | -274.23% |
| 7 | TRX | okx | -249.93% |
| 8 | NIL | bitget | -249.88% |
| 9 | ESP | bitget | -163.16% |
| 10 | POWER | bitget | -159.21% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SOPH | +831.03% | okx | -816.51% | bitget | -1647.54% |
| 2 | BLUR | +732.94% | okx | -644.13% | bitget | -1377.07% |
| 3 | AKE | +330.47% | bitget | +335.95% | okx | +5.47% |
| 4 | H100 | +279.70% | bitget | +5.47% | okx | -274.23% |
| 5 | ROK | +221.98% | okx | +221.98% | bitget | +0.00% |
| 6 | TRX | +181.16% | bitget | -68.77% | okx | -249.93% |
| 7 | KR200 | +172.23% | okx | +172.23% | bitget | +0.00% |
| 8 | BX | +140.08% | bitget | +0.00% | okx | -140.08% |
| 9 | KIOXIA | +121.54% | okx | +25.18% | bitget | -96.36% |
| 10 | KSTR | +111.92% | okx | +184.74% | bitget | +72.82% |
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
