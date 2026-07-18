# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-18 09:52 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1118**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | XMR | bitget | +95.05% |
| 2 | O | okx | +65.90% |
| 3 | SIREN | bitget | +64.06% |
| 4 | BTW | bitget | +50.59% |
| 5 | RAVE | okx | +44.30% |
| 6 | BANK | bitget | +42.38% |
| 7 | LAB | okx | +35.90% |
| 8 | US | bitget | +33.40% |
| 9 | LAB | bitget | +31.10% |
| 10 | SOON | bitget | +27.27% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SPELL | bitget | -1018.02% |
| 2 | HOME | bitget | -978.93% |
| 3 | TOSHI | bitget | -488.70% |
| 4 | HOME | okx | -351.91% |
| 5 | BONK | okx | -190.76% |
| 6 | 1000BONK | bitget | -164.25% |
| 7 | DATA | okx | -100.16% |
| 8 | TLM | bitget | -98.00% |
| 9 | T | bitget | -87.27% |
| 10 | RE | bitget | -78.62% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | HOME | +627.02% | okx | -351.91% | bitget | -978.93% |
| 2 | DATA | +83.19% | bitget | -16.97% | okx | -100.16% |
| 3 | ESP | +61.56% | bitget | +5.47% | okx | -56.09% |
| 4 | O | +60.42% | okx | +65.90% | bitget | +5.47% |
| 5 | RSR | +57.33% | bitget | +10.95% | okx | -46.38% |
| 6 | CHZ | +55.89% | bitget | +1.53% | okx | -54.35% |
| 7 | ALGO | +55.66% | bitget | +10.95% | okx | -44.71% |
| 8 | LDO | +55.23% | okx | +4.75% | bitget | -50.48% |
| 9 | SAHARA | +52.91% | bitget | +5.47% | okx | -47.44% |
| 10 | DELL | +43.68% | bitget | +0.00% | okx | -43.68% |
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
