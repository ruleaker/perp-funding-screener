# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-08-24 17:03 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1199**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BSP | bitget | +143.77% |
| 2 | SCRT | bitget | +103.70% |
| 3 | QNT | okx | +93.33% |
| 4 | GEV | okx | +89.19% |
| 5 | SHOP | okx | +68.32% |
| 6 | ESPORTS | bitget | +57.93% |
| 7 | MRNA | okx | +53.50% |
| 8 | CBRS | bitget | +50.70% |
| 9 | QQQ | bitget | +47.85% |
| 10 | RAM | okx | +46.78% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | STORJ | bitget | -953.31% |
| 2 | SUPER | bitget | -339.23% |
| 3 | BICO | bitget | -239.81% |
| 4 | SAND | bitget | -226.45% |
| 5 | NES | okx | -223.16% |
| 6 | ACE | bitget | -219.77% |
| 7 | SKDD | bitget | -210.90% |
| 8 | HOME | bitget | -150.56% |
| 9 | HOME | okx | -147.23% |
| 10 | BICO | okx | -139.41% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | BSP | +143.77% | bitget | +143.77% | okx | +0.00% |
| 2 | UNITREE | +129.12% | bitget | +0.00% | okx | -129.12% |
| 3 | SAND | +101.36% | okx | -125.08% | bitget | -226.45% |
| 4 | BICO | +100.39% | okx | -139.41% | bitget | -239.81% |
| 5 | SKDD | +95.40% | okx | -115.50% | bitget | -210.90% |
| 6 | GEV | +89.19% | okx | +89.19% | bitget | +0.00% |
| 7 | QNT | +82.38% | okx | +93.33% | bitget | +10.95% |
| 8 | TWLO | +77.05% | bitget | +0.00% | okx | -77.05% |
| 9 | RVN | +73.89% | bitget | -53.76% | okx | -127.66% |
| 10 | SHOP | +68.32% | okx | +68.32% | bitget | +0.00% |
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
