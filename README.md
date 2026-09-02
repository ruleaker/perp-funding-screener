# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-02 04:50 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1213**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BOT | okx | +218.06% |
| 2 | NES | okx | +144.51% |
| 3 | PIPPIN | bitget | +143.99% |
| 4 | TMF | okx | +126.33% |
| 5 | XPD | okx | +115.53% |
| 6 | BSP | okx | +105.45% |
| 7 | RAM | okx | +104.35% |
| 8 | FIGHT | bitget | +85.52% |
| 9 | XPT | okx | +66.87% |
| 10 | XAG | okx | +58.76% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ACE | bitget | -604.88% |
| 2 | HOME | bitget | -448.29% |
| 3 | HOME | okx | -444.35% |
| 4 | SKDD | okx | -199.63% |
| 5 | LA | okx | -194.01% |
| 6 | LA | bitget | -189.00% |
| 7 | SKR | bitget | -155.16% |
| 8 | FWDI | okx | -142.11% |
| 9 | TRX | okx | -131.49% |
| 10 | TRX | bitget | -125.71% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BOT | +218.06% | okx | +218.06% | bitget | +0.00% |
| 2 | SKDD | +199.63% | bitget | +0.00% | okx | -199.63% |
| 3 | FWDI | +142.11% | bitget | +0.00% | okx | -142.11% |
| 4 | PIPPIN | +135.95% | bitget | +143.99% | okx | +8.05% |
| 5 | TMF | +126.33% | okx | +126.33% | bitget | +0.00% |
| 6 | RAM | +104.35% | okx | +104.35% | bitget | +0.00% |
| 7 | ZM | +97.12% | bitget | +0.00% | okx | -97.12% |
| 8 | MRNA | +76.91% | bitget | +0.00% | okx | -76.91% |
| 9 | XPD | +66.70% | okx | +115.53% | bitget | +48.84% |
| 10 | WEN | +58.15% | bitget | +0.00% | okx | -58.15% |
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
