# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-15 10:18 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1110**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MUU | okx | +249.14% |
| 2 | LUNR | okx | +190.96% |
| 3 | QNT | okx | +129.79% |
| 4 | ESPORTS | bitget | +88.48% |
| 5 | MSFT | okx | +77.38% |
| 6 | XBI | okx | +67.70% |
| 7 | LAB | okx | +57.75% |
| 8 | 龙虾 | bitget | +55.19% |
| 9 | NTAP | bitget | +54.97% |
| 10 | TUT | bitget | +53.87% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | VANRY | bitget | -465.59% |
| 2 | VANA | bitget | -419.93% |
| 3 | VANA | okx | -395.01% |
| 4 | BOT | bitget | -339.01% |
| 5 | ETN | bitget | -237.40% |
| 6 | 1000XEC | bitget | -223.49% |
| 7 | TLM | bitget | -186.15% |
| 8 | XNDU | bitget | -150.12% |
| 9 | BONK | okx | -148.16% |
| 10 | GWEI | bitget | -145.53% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | MUU | +249.14% | okx | +249.14% | bitget | +0.00% |
| 2 | BOT | +241.38% | okx | -97.63% | bitget | -339.01% |
| 3 | QNT | +118.84% | okx | +129.79% | bitget | +10.95% |
| 4 | DATA | +86.57% | bitget | -53.44% | okx | -140.01% |
| 5 | SAMSUNG | +84.32% | bitget | +0.00% | okx | -84.32% |
| 6 | MSFT | +77.38% | okx | +77.38% | bitget | +0.00% |
| 7 | XBI | +67.70% | okx | +67.70% | bitget | +0.00% |
| 8 | SKHYNIX | +65.64% | bitget | +0.00% | okx | -65.64% |
| 9 | SKHY | +64.57% | bitget | +0.00% | okx | -64.57% |
| 10 | KIOXIA | +48.61% | okx | +48.61% | bitget | +0.00% |
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
