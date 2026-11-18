# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-11-18 07:47 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1415**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | LGENERGY | bitget | +977.29% |
| 2 | H100 | okx | +953.38% |
| 3 | ZHONGJI | bitget | +233.13% |
| 4 | CSOPSS2LHKD | bitget | +212.76% |
| 5 | GIGADEVICE | bitget | +210.35% |
| 6 | CSOPSK2LHKD | bitget | +193.49% |
| 7 | ZHONGJI | okx | +185.71% |
| 8 | MINIMAX | bitget | +168.52% |
| 9 | FCX | bitget | +161.84% |
| 10 | MINIMAX | okx | +155.88% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ZKP | bitget | -1023.28% |
| 2 | ZKP | okx | -1020.26% |
| 3 | AXIS | bitget | -642.22% |
| 4 | AXIS | okx | -605.68% |
| 5 | BREV | okx | -388.38% |
| 6 | BREV | bitget | -370.00% |
| 7 | UVXY | okx | -334.89% |
| 8 | UVXY | bitget | -325.54% |
| 9 | NIO | bitget | -317.77% |
| 10 | KAVA | bitget | -294.99% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | H100 | +947.91% | okx | +953.38% | bitget | +5.47% |
| 2 | HANMI | +247.27% | bitget | +6.13% | okx | -241.13% |
| 3 | NAVER | +184.11% | bitget | +127.35% | okx | -56.76% |
| 4 | POET | +175.75% | okx | +0.00% | bitget | -175.75% |
| 5 | SKDD | +165.70% | bitget | +6.68% | okx | -159.02% |
| 6 | UNITREE | +106.45% | bitget | -33.73% | okx | -140.18% |
| 7 | HUMA | +101.66% | bitget | -38.76% | okx | -140.42% |
| 8 | GPRO | +89.28% | okx | +89.28% | bitget | +0.00% |
| 9 | SOPH | +78.69% | bitget | +0.77% | okx | -77.92% |
| 10 | SHEIN | +61.65% | bitget | +0.00% | okx | -61.65% |
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
