# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-10 04:31 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1098**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | okx | +757.77% |
| 2 | SKHYNIX | bitget | +547.50% |
| 3 | SAMSUNG | bitget | +451.25% |
| 4 | SAMSUNG | okx | +270.95% |
| 5 | EVAA | bitget | +190.09% |
| 6 | BX | okx | +144.41% |
| 7 | MINIMAX | bitget | +133.37% |
| 8 | RDDT | okx | +88.51% |
| 9 | POWER | bitget | +86.50% |
| 10 | M | bitget | +80.48% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKL | bitget | -672.11% |
| 2 | ON | okx | -362.04% |
| 3 | OGN | bitget | -341.53% |
| 4 | SOFTBANK | okx | -239.95% |
| 5 | GWEI | bitget | -225.46% |
| 6 | OPG | bitget | -209.15% |
| 7 | DATA | okx | -178.16% |
| 8 | ZHIPU | okx | -161.51% |
| 9 | ONG | bitget | -152.53% |
| 10 | VANRY | bitget | -145.09% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +210.27% | okx | +757.77% | bitget | +547.50% |
| 2 | SAMSUNG | +180.30% | bitget | +451.25% | okx | +270.95% |
| 3 | DATA | +150.56% | bitget | -27.59% | okx | -178.16% |
| 4 | BX | +144.41% | okx | +144.41% | bitget | +0.00% |
| 5 | OPG | +101.12% | okx | -108.03% | bitget | -209.15% |
| 6 | MINIMAX | +95.98% | bitget | +133.37% | okx | +37.39% |
| 7 | RDDT | +88.51% | okx | +88.51% | bitget | +0.00% |
| 8 | RKLB | +78.73% | okx | +78.73% | bitget | +0.00% |
| 9 | MUU | +76.56% | okx | +76.56% | bitget | +0.00% |
| 10 | KORU | +75.77% | bitget | +75.77% | okx | +0.00% |
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
