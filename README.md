# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-29 11:00 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1148**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | FWDI | bitget | +547.50% |
| 2 | SAMSUNG | okx | +469.97% |
| 3 | KIOXIA | okx | +352.96% |
| 4 | SKHYNIX | okx | +338.70% |
| 5 | KR200 | okx | +316.28% |
| 6 | ZHIPU | bitget | +208.05% |
| 7 | SNXX | okx | +183.55% |
| 8 | ZHIPU | okx | +181.84% |
| 9 | KORU | bitget | +169.62% |
| 10 | TTWO | okx | +136.97% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LA | bitget | -1453.28% |
| 2 | LA | okx | -717.72% |
| 3 | BOT | bitget | -443.58% |
| 4 | BANK | bitget | -341.31% |
| 5 | ZIL | bitget | -290.61% |
| 6 | ZIL | okx | -287.31% |
| 7 | EUL | bitget | -267.18% |
| 8 | TLM | bitget | -198.52% |
| 9 | ACH | okx | -171.25% |
| 10 | STORJ | bitget | -164.36% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LA | +735.57% | okx | -717.72% | bitget | -1453.28% |
| 2 | FWDI | +670.88% | bitget | +547.50% | okx | -123.38% |
| 3 | SAMSUNG | +469.97% | okx | +469.97% | bitget | +0.00% |
| 4 | KIOXIA | +352.96% | okx | +352.96% | bitget | +0.00% |
| 5 | BOT | +347.28% | okx | -96.30% | bitget | -443.58% |
| 6 | SKHYNIX | +338.70% | okx | +338.70% | bitget | +0.00% |
| 7 | TTWO | +136.97% | okx | +136.97% | bitget | +0.00% |
| 8 | KORU | +130.34% | bitget | +169.62% | okx | +39.27% |
| 9 | TER | +119.57% | okx | +0.00% | bitget | -119.57% |
| 10 | WEN | +88.03% | bitget | +0.00% | okx | -88.03% |
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
