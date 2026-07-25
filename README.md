# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-25 03:45 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1132**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | bitget | +376.35% |
| 2 | QNT | okx | +184.73% |
| 3 | SKHYNIX | okx | +146.80% |
| 4 | BANK | bitget | +123.41% |
| 5 | SAMSUNG | okx | +97.67% |
| 6 | KORU | bitget | +94.06% |
| 7 | BSP | okx | +84.54% |
| 8 | MU | okx | +81.67% |
| 9 | SNDK | okx | +78.41% |
| 10 | CBRS | okx | +74.04% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MIRA | bitget | -641.78% |
| 2 | GWEI | bitget | -600.28% |
| 3 | PROM | bitget | -331.35% |
| 4 | ACE | bitget | -289.63% |
| 5 | TLM | bitget | -279.44% |
| 6 | BARD | bitget | -204.44% |
| 7 | ZKC | bitget | -200.60% |
| 8 | STX | okx | -157.28% |
| 9 | ERA | bitget | -147.06% |
| 10 | STX | bitget | -118.37% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | QNT | +173.78% | okx | +184.73% | bitget | +10.95% |
| 2 | SKHYNIX | +146.80% | okx | +146.80% | bitget | +0.00% |
| 3 | BARD | +117.77% | okx | -86.66% | bitget | -204.44% |
| 4 | SAMSUNG | +97.67% | okx | +97.67% | bitget | +0.00% |
| 5 | KORU | +94.06% | bitget | +94.06% | okx | +0.00% |
| 6 | BEAT | +85.77% | bitget | +5.47% | okx | -80.29% |
| 7 | BSP | +84.54% | okx | +84.54% | bitget | +0.00% |
| 8 | MU | +81.67% | okx | +81.67% | bitget | +0.00% |
| 9 | SNDK | +78.41% | okx | +78.41% | bitget | +0.00% |
| 10 | CBRS | +74.04% | okx | +74.04% | bitget | +0.00% |
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
