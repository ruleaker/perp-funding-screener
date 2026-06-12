# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-12 11:57 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **982**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BEAT | okx | +415.27% |
| 2 | SKHYNIX | okx | +401.37% |
| 3 | SHLD | okx | +281.81% |
| 4 | BEAT | bitget | +239.26% |
| 5 | SAMSUNG | okx | +140.83% |
| 6 | GWEI | bitget | +108.30% |
| 7 | 龙虾 | bitget | +88.15% |
| 8 | AMD | okx | +82.63% |
| 9 | HYUNDAI | okx | +78.76% |
| 10 | SKYAI | bitget | +75.99% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | STG | bitget | -947.61% |
| 2 | ESPORTS | bitget | -872.50% |
| 3 | HOME | okx | -436.76% |
| 4 | HOME | bitget | -433.84% |
| 5 | SAHARA | okx | -231.13% |
| 6 | H | okx | -227.09% |
| 7 | SAHARA | bitget | -212.54% |
| 8 | TRUMP | okx | -202.83% |
| 9 | TRUMP | bitget | -175.31% |
| 10 | ID | bitget | -139.94% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | SKHYNIX | +401.37% | okx | +401.37% | bitget | +0.00% |
| 2 | H | +224.79% | bitget | -2.30% | okx | -227.09% |
| 3 | BEAT | +176.01% | okx | +415.27% | bitget | +239.26% |
| 4 | SAMSUNG | +140.83% | okx | +140.83% | bitget | +0.00% |
| 5 | SOPH | +139.61% | bitget | +5.47% | okx | -134.13% |
| 6 | TON | +89.76% | bitget | -17.30% | okx | -107.07% |
| 7 | AMD | +82.63% | okx | +82.63% | bitget | +0.00% |
| 8 | HYUNDAI | +78.76% | okx | +78.76% | bitget | +0.00% |
| 9 | ATOM | +73.91% | okx | +10.95% | bitget | -62.96% |
| 10 | LAB | +70.19% | bitget | +75.66% | okx | +5.47% |
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
