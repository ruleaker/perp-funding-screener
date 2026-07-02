# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-02 04:38 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1062**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | bitget | +547.50% |
| 2 | SKHYNIX | okx | +488.77% |
| 3 | SAMSUNG | bitget | +390.26% |
| 4 | SAMSUNG | okx | +359.95% |
| 5 | HYUNDAI | bitget | +310.32% |
| 6 | HYUNDAI | okx | +183.35% |
| 7 | STRC | okx | +159.17% |
| 8 | INFQ | okx | +144.83% |
| 9 | EVAA | bitget | +125.38% |
| 10 | GLW | okx | +112.55% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TAIKO | bitget | -2183.10% |
| 2 | LAB | okx | -900.66% |
| 3 | LAB | bitget | -316.67% |
| 4 | CELO | okx | -207.59% |
| 5 | QNT | okx | -170.81% |
| 6 | ARX | bitget | -156.69% |
| 7 | CELO | bitget | -152.53% |
| 8 | BB | okx | -144.63% |
| 9 | RE | okx | -125.16% |
| 10 | RE | bitget | -115.30% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LAB | +583.99% | bitget | -316.67% | okx | -900.66% |
| 2 | QNT | +181.76% | bitget | +10.95% | okx | -170.81% |
| 3 | STRC | +159.17% | okx | +159.17% | bitget | +0.00% |
| 4 | BB | +150.10% | bitget | +5.47% | okx | -144.63% |
| 5 | INFQ | +144.83% | okx | +144.83% | bitget | +0.00% |
| 6 | HYUNDAI | +126.97% | bitget | +310.32% | okx | +183.35% |
| 7 | GLW | +112.55% | okx | +112.55% | bitget | +0.00% |
| 8 | KIOXIA | +96.55% | okx | +96.55% | bitget | +0.00% |
| 9 | SOXL | +83.80% | okx | +80.51% | bitget | -3.29% |
| 10 | SPCX | +82.23% | okx | +82.23% | bitget | +0.00% |
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
