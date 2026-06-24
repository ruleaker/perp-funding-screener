# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-24 04:45 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1037**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | bitget | +547.50% |
| 2 | SKHYNIX | okx | +519.47% |
| 3 | SAMSUNG | bitget | +517.17% |
| 4 | HYUNDAI | bitget | +398.25% |
| 5 | 龙虾 | bitget | +356.42% |
| 6 | SAMSUNG | okx | +327.15% |
| 7 | HYUNDAI | okx | +267.10% |
| 8 | RDW | okx | +215.62% |
| 9 | SIREN | bitget | +198.19% |
| 10 | FOLKS | bitget | +101.07% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | TAIKO | bitget | -326.09% |
| 2 | LAYER | okx | -311.53% |
| 3 | ID | bitget | -239.81% |
| 4 | LAYER | bitget | -230.39% |
| 5 | SYN | bitget | -188.67% |
| 6 | HOME | bitget | -164.47% |
| 7 | RE | bitget | -158.67% |
| 8 | FIDA | bitget | -134.90% |
| 9 | RE | okx | -127.20% |
| 10 | GUN | bitget | -97.24% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | RDW | +215.62% | okx | +215.62% | bitget | +0.00% |
| 2 | SAMSUNG | +190.02% | bitget | +517.17% | okx | +327.15% |
| 3 | HYUNDAI | +131.16% | bitget | +398.25% | okx | +267.10% |
| 4 | KLAC | +100.51% | okx | +100.51% | bitget | +0.00% |
| 5 | MUBARAK | +83.88% | okx | +5.47% | bitget | -78.40% |
| 6 | LAYER | +81.15% | bitget | -230.39% | okx | -311.53% |
| 7 | BX | +79.90% | okx | +79.90% | bitget | +0.00% |
| 8 | RDDT | +79.14% | okx | +79.14% | bitget | +0.00% |
| 9 | HOME | +77.64% | okx | -86.83% | bitget | -164.47% |
| 10 | QNT | +73.44% | bitget | +10.95% | okx | -62.49% |
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
