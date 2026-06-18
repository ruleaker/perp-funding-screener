# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-18 12:00 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1015**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +221.85% |
| 2 | SMH | okx | +190.00% |
| 3 | TER | okx | +163.29% |
| 4 | RDDT | okx | +136.15% |
| 5 | BLESS | bitget | +129.65% |
| 6 | O | okx | +107.53% |
| 7 | DRAM | okx | +104.04% |
| 8 | INTC | okx | +103.41% |
| 9 | AXTI | okx | +102.12% |
| 10 | IBM | okx | +98.40% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SYN | bitget | -768.25% |
| 2 | PRL | bitget | -496.80% |
| 3 | MTL | bitget | -274.08% |
| 4 | 龙虾 | bitget | -207.28% |
| 5 | HOME | okx | -195.67% |
| 6 | SAHARA | bitget | -191.73% |
| 7 | STABLE | bitget | -184.40% |
| 8 | SAHARA | okx | -177.67% |
| 9 | ID | bitget | -175.42% |
| 10 | ORCA | bitget | -132.17% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +221.85% | okx | +221.85% | bitget | +0.00% |
| 2 | SMH | +190.00% | okx | +190.00% | bitget | +0.00% |
| 3 | HOME | +168.73% | bitget | -26.94% | okx | -195.67% |
| 4 | RDDT | +136.15% | okx | +136.15% | bitget | +0.00% |
| 5 | H | +130.58% | okx | +1.37% | bitget | -129.21% |
| 6 | STABLE | +121.17% | okx | -63.23% | bitget | -184.40% |
| 7 | STRK | +114.11% | okx | -4.48% | bitget | -118.59% |
| 8 | EIGEN | +106.00% | okx | +5.47% | bitget | -100.52% |
| 9 | DRAM | +104.04% | okx | +104.04% | bitget | +0.00% |
| 10 | QNT | +102.90% | okx | +90.97% | bitget | -11.94% |
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
