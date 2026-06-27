# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-27 10:31 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1050**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | CBRS | okx | +214.56% |
| 2 | 龙虾 | bitget | +89.46% |
| 3 | H | okx | +78.88% |
| 4 | US | bitget | +63.95% |
| 5 | MSTR | okx | +51.34% |
| 6 | SIREN | bitget | +46.21% |
| 7 | XPIN | bitget | +39.97% |
| 8 | GWEI | bitget | +33.84% |
| 9 | UB | okx | +31.24% |
| 10 | ORCL | okx | +29.93% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AGLD | okx | -874.63% |
| 2 | AGLD | bitget | -834.28% |
| 3 | ARK | bitget | -785.66% |
| 4 | LAB | okx | -686.48% |
| 5 | LAB | bitget | -682.62% |
| 6 | GLM | okx | -501.50% |
| 7 | GLM | bitget | -433.07% |
| 8 | CVC | bitget | -219.66% |
| 9 | LA | bitget | -195.79% |
| 10 | RE | bitget | -175.09% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | CBRS | +214.56% | okx | +214.56% | bitget | +0.00% |
| 2 | LA | +83.22% | okx | -112.57% | bitget | -195.79% |
| 3 | H | +73.41% | okx | +78.88% | bitget | +5.47% |
| 4 | GLM | +68.43% | bitget | -433.07% | okx | -501.50% |
| 5 | LAYER | +60.34% | bitget | -35.15% | okx | -95.49% |
| 6 | MSTR | +51.34% | okx | +51.34% | bitget | +0.00% |
| 7 | THETA | +48.01% | bitget | +10.95% | okx | -37.06% |
| 8 | KAT | +45.27% | bitget | +5.47% | okx | -39.79% |
| 9 | AGLD | +40.35% | bitget | -834.28% | okx | -874.63% |
| 10 | BB | +39.97% | okx | +0.00% | bitget | -39.97% |
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
