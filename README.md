# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-07-05 10:35 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1078**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SAMSUNG | okx | +68.37% |
| 2 | ESPORTS | bitget | +58.91% |
| 3 | SIREN | bitget | +55.41% |
| 4 | TAG | bitget | +53.11% |
| 5 | TER | okx | +47.65% |
| 6 | 龙虾 | bitget | +46.21% |
| 7 | XVG | bitget | +45.55% |
| 8 | BR | bitget | +44.02% |
| 9 | CYS | bitget | +37.01% |
| 10 | RLS | okx | +36.03% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | AI | okx | -1095.00% |
| 2 | MIRA | bitget | -1048.02% |
| 3 | HOT | bitget | -835.05% |
| 4 | 10000NEX | bitget | -519.69% |
| 5 | ONG | bitget | -428.58% |
| 6 | RPL | bitget | -393.00% |
| 7 | LAB | okx | -356.89% |
| 8 | VANRY | bitget | -196.44% |
| 9 | OGN | bitget | -189.54% |
| 10 | SLX | bitget | -186.48% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | LAB | +327.22% | bitget | -29.67% | okx | -356.89% |
| 2 | SAMSUNG | +68.37% | okx | +68.37% | bitget | +0.00% |
| 3 | CELO | +49.05% | bitget | -14.45% | okx | -63.50% |
| 4 | TER | +47.65% | okx | +47.65% | bitget | +0.00% |
| 5 | 1INCH | +44.57% | okx | +10.95% | bitget | -33.62% |
| 6 | MSTR | +40.66% | bitget | -19.49% | okx | -60.15% |
| 7 | KIOXIA | +34.77% | okx | +34.77% | bitget | +0.00% |
| 8 | RE | +33.86% | bitget | -31.97% | okx | -65.83% |
| 9 | CC | +30.95% | bitget | -38.43% | okx | -69.39% |
| 10 | LTC | +30.53% | okx | -6.26% | bitget | -36.79% |
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
