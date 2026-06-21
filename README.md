# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-06-21 11:27 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1021**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | 龙虾 | bitget | +174.21% |
| 2 | SIREN | bitget | +167.53% |
| 3 | FIGHT | bitget | +111.25% |
| 4 | SKHYNIX | okx | +106.74% |
| 5 | 4 | bitget | +77.85% |
| 6 | BICO | bitget | +70.74% |
| 7 | ESPORTS | bitget | +67.89% |
| 8 | INFQ | okx | +66.91% |
| 9 | M | bitget | +58.36% |
| 10 | USELESS | bitget | +58.25% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H | bitget | -791.47% |
| 2 | H | okx | -592.61% |
| 3 | TNSR | bitget | -520.89% |
| 4 | FIDA | bitget | -349.09% |
| 5 | ACE | bitget | -326.09% |
| 6 | ALICE | bitget | -289.41% |
| 7 | RE | bitget | -269.92% |
| 8 | HOME | okx | -227.68% |
| 9 | RE | okx | -172.65% |
| 10 | ID | bitget | -116.40% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H | +198.86% | okx | -592.61% | bitget | -791.47% |
| 2 | HOME | +158.48% | bitget | -69.20% | okx | -227.68% |
| 3 | SKHYNIX | +106.74% | okx | +106.74% | bitget | +0.00% |
| 4 | RE | +97.27% | okx | -172.65% | bitget | -269.92% |
| 5 | BICO | +92.82% | bitget | +70.74% | okx | -22.09% |
| 6 | INFQ | +66.91% | okx | +66.91% | bitget | +0.00% |
| 7 | WAL | +60.55% | okx | +5.47% | bitget | -55.08% |
| 8 | USELESS | +52.78% | bitget | +58.25% | okx | +5.47% |
| 9 | OP | +51.90% | okx | +10.95% | bitget | -40.95% |
| 10 | ALLO | +50.70% | bitget | +56.17% | okx | +5.47% |
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
