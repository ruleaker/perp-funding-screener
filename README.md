# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-14 10:14 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1107**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | KORU | okx | +224.59% |
| 2 | TKO | bitget | +213.09% |
| 3 | MINIMAX | bitget | +154.39% |
| 4 | SKHYNIX | okx | +118.17% |
| 5 | AAOI | okx | +74.64% |
| 6 | QNT | okx | +72.97% |
| 7 | POPMART | bitget | +70.85% |
| 8 | EWY | okx | +64.36% |
| 9 | ESPORTS | bitget | +61.54% |
| 10 | CRCL | okx | +55.91% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SXT | bitget | -1005.65% |
| 2 | SOXS | bitget | -547.50% |
| 3 | FWDI | bitget | -547.50% |
| 4 | BOT | bitget | -547.50% |
| 5 | BUD | bitget | -360.25% |
| 6 | TSEM | okx | -259.93% |
| 7 | VANA | okx | -240.33% |
| 8 | KUAISHOU | bitget | -238.49% |
| 9 | PI | bitget | -189.54% |
| 10 | ICX | bitget | -185.93% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BOT | +421.76% | okx | -125.74% | bitget | -547.50% |
| 2 | TSEM | +259.93% | bitget | +0.00% | okx | -259.93% |
| 3 | KORU | +224.59% | okx | +224.59% | bitget | +0.00% |
| 4 | ICX | +191.41% | okx | +5.47% | bitget | -185.93% |
| 5 | MINIMAX | +154.39% | bitget | +154.39% | okx | +0.00% |
| 6 | VANA | +152.73% | bitget | -87.60% | okx | -240.33% |
| 7 | ROK | +140.35% | bitget | +0.00% | okx | -140.35% |
| 8 | SKHYNIX | +118.17% | okx | +118.17% | bitget | +0.00% |
| 9 | GEV | +92.34% | bitget | +0.00% | okx | -92.34% |
| 10 | AAOI | +74.64% | okx | +74.64% | bitget | +0.00% |
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
