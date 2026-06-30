# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-30 04:41 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1062**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | SKHYNIX | bitget | +385.11% |
| 2 | SKHYNIX | okx | +215.76% |
| 3 | SIREN | bitget | +199.18% |
| 4 | KORU | bitget | +172.68% |
| 5 | HYUNDAI | bitget | +161.84% |
| 6 | GLW | okx | +145.21% |
| 7 | HYUNDAI | okx | +108.62% |
| 8 | RDW | okx | +92.85% |
| 9 | US | bitget | +89.68% |
| 10 | FF | bitget | +80.15% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONG | bitget | -1707.43% |
| 2 | AI | okx | -1095.00% |
| 3 | TAIKO | bitget | -834.06% |
| 4 | LAB | bitget | -588.89% |
| 5 | LAB | okx | -578.28% |
| 6 | ZKP | bitget | -346.57% |
| 7 | GAS | okx | -247.49% |
| 8 | SHLD | okx | -242.15% |
| 9 | RE | bitget | -192.50% |
| 10 | GWEI | bitget | -191.19% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ZKP | +345.99% | okx | -0.58% | bitget | -346.57% |
| 2 | GAS | +192.41% | bitget | -55.08% | okx | -247.49% |
| 3 | SKHYNIX | +169.35% | bitget | +385.11% | okx | +215.76% |
| 4 | KORU | +157.45% | bitget | +172.68% | okx | +15.23% |
| 5 | GLW | +145.21% | okx | +145.21% | bitget | +0.00% |
| 6 | ONT | +103.73% | bitget | +5.47% | okx | -98.26% |
| 7 | STRC | +98.26% | bitget | +0.00% | okx | -98.26% |
| 8 | RDW | +92.85% | okx | +92.85% | bitget | +0.00% |
| 9 | SLX | +88.48% | bitget | -63.29% | okx | -151.77% |
| 10 | BAT | +73.95% | bitget | +10.95% | okx | -63.00% |
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
