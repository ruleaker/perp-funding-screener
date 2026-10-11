# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-10-11 20:26 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1305**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | H100 | okx | +614.45% |
| 2 | MINIMAX | okx | +86.11% |
| 3 | BILL | okx | +70.85% |
| 4 | ARIA | bitget | +65.37% |
| 5 | MINIMAX | bitget | +64.39% |
| 6 | MINIMAXHKD | bitget | +61.87% |
| 7 | ZEST | bitget | +47.85% |
| 8 | NVDL | okx | +33.19% |
| 9 | ELSA | bitget | +29.89% |
| 10 | RAVE | okx | +22.51% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | MINA | bitget | -216.37% |
| 2 | OGN | bitget | -146.29% |
| 3 | MINA | okx | -129.27% |
| 4 | ERA | bitget | -123.84% |
| 5 | XDP | okx | -98.67% |
| 6 | ONE | bitget | -94.50% |
| 7 | RVN | okx | -81.39% |
| 8 | NG | okx | -77.37% |
| 9 | SAND | bitget | -51.25% |
| 10 | CTSI | bitget | -39.42% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +614.45% | okx | +614.45% | bitget | +0.00% |
| 2 | ONE | +99.97% | okx | +5.47% | bitget | -94.50% |
| 3 | MINA | +87.10% | okx | -129.27% | bitget | -216.37% |
| 4 | BILL | +65.38% | okx | +70.85% | bitget | +5.47% |
| 5 | RVN | +46.24% | bitget | -35.15% | okx | -81.39% |
| 6 | GMT | +40.17% | okx | +4.15% | bitget | -36.03% |
| 7 | NVDL | +33.19% | okx | +33.19% | bitget | +0.00% |
| 8 | TRX | +31.18% | bitget | +8.54% | okx | -22.64% |
| 9 | SAND | +30.27% | okx | -20.97% | bitget | -51.25% |
| 10 | SHEIN | +28.56% | bitget | +0.00% | okx | -28.56% |
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
