# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-14 11:12 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **982**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SHLD | okx | +208.64% |
| 2 | SKHYNIX | okx | +177.17% |
| 3 | AMD | okx | +133.62% |
| 4 | LITE | okx | +117.50% |
| 5 | MRVL | okx | +108.09% |
| 6 | EPIC | bitget | +90.56% |
| 7 | JELLYJELLY | okx | +89.48% |
| 8 | MU | okx | +88.52% |
| 9 | SAMSUNG | okx | +81.73% |
| 10 | CARV | bitget | +68.55% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | HOME | okx | -525.49% |
| 2 | H | okx | -341.07% |
| 3 | SKR | bitget | -327.84% |
| 4 | HOME | bitget | -317.55% |
| 5 | TON | okx | -285.59% |
| 6 | SAHARA | bitget | -166.66% |
| 7 | H | bitget | -144.76% |
| 8 | SAHARA | okx | -143.84% |
| 9 | ZKP | okx | -141.10% |
| 10 | ID | bitget | -111.69% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | TON | +262.60% | bitget | -23.00% | okx | -285.59% |
| 2 | HOME | +207.94% | bitget | -317.55% | okx | -525.49% |
| 3 | H | +196.31% | bitget | -144.76% | okx | -341.07% |
| 4 | SKHYNIX | +177.17% | okx | +177.17% | bitget | +0.00% |
| 5 | AMD | +133.62% | okx | +133.62% | bitget | +0.00% |
| 6 | LITE | +117.50% | okx | +117.50% | bitget | +0.00% |
| 7 | MRVL | +108.09% | okx | +108.09% | bitget | +0.00% |
| 8 | CRO | +89.90% | okx | +10.95% | bitget | -78.95% |
| 9 | ZKP | +88.54% | bitget | -52.56% | okx | -141.10% |
| 10 | MU | +88.52% | okx | +88.52% | bitget | +0.00% |
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
