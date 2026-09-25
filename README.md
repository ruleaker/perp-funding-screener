# Perp Funding Screener

> Cross-venue perpetual funding rate screener. Auto-updated every 8 hours via GitHub Actions.

<!-- BEGIN:STAMP -->
_Last update: **2026-09-25 14:01 UTC**  ·  Venues: binance · bybit · okx · bitget  ·  Pairs scanned: **1282**_
<!-- END:STAMP -->

Funding rates reveal positioning skew long before price tells the story. When perps trade rich to spot, longs pay shorts — and that flow has a cost of carry that compounds. Cross-venue divergence tells you where positioning is most stretched and where the cheap-borrow / expensive-borrow opportunities live.

This screener pulls every USDT-margined linear perp from four major venues, annualizes the funding rate, and surfaces the extremes.

## Highest annualized funding

Longs are paying the most premium on these markets.

<!-- BEGIN:TOP_HIGH -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | BLESS | bitget | +393.98% |
| 2 | 龙虾 | bitget | +190.31% |
| 3 | PIPPIN | bitget | +169.51% |
| 4 | SOON | bitget | +153.85% |
| 5 | QNT | okx | +153.21% |
| 6 | SECZ | bitget | +150.89% |
| 7 | RAVE | okx | +141.69% |
| 8 | OKLO | okx | +136.24% |
| 9 | NAORIS | bitget | +134.58% |
| 10 | AIO | bitget | +124.50% |
<!-- END:TOP_HIGH -->

## Lowest annualized funding

Shorts are paying the most premium on these markets — often a contrarian long-bias signal.

<!-- BEGIN:TOP_LOW -->
| Rank | Symbol | Venue | Funding (annualized) |
|------|--------|-------|---------------------:|
| 1 | ONE | bitget | -745.37% |
| 2 | SDGR | bitget | -465.05% |
| 3 | JMKE | bitget | -432.74% |
| 4 | ECHO | bitget | -273.75% |
| 5 | WAXP | bitget | -240.24% |
| 6 | ONE | okx | -149.33% |
| 7 | LSK | bitget | -148.04% |
| 8 | G | bitget | -92.75% |
| 9 | CVC | bitget | -86.50% |
| 10 | STEEM | bitget | -86.40% |
<!-- END:TOP_LOW -->

## Biggest cross-venue spreads

Same symbol, different venue. Large spreads can indicate routing inefficiency, liquidity asymmetry, or a venue-specific position dislocation. Not a direct arbitrage signal — but the starting point for further analysis.

<!-- BEGIN:TOP_SPREADS -->
| Rank | Symbol | Spread | High venue | High rate | Low venue | Low rate |
|------|--------|-------:|------------|----------:|-----------|---------:|
| 1 | ONE | +596.04% | okx | -149.33% | bitget | -745.37% |
| 2 | QNT | +172.37% | okx | +153.21% | bitget | -19.16% |
| 3 | PIPPIN | +149.21% | bitget | +169.51% | okx | +20.29% |
| 4 | OKLO | +136.24% | okx | +136.24% | bitget | +0.00% |
| 5 | SOON | +125.35% | bitget | +153.85% | okx | +28.50% |
| 6 | MSTR | +111.77% | bitget | +115.19% | okx | +3.43% |
| 7 | KSTR | +104.37% | okx | +104.37% | bitget | +0.00% |
| 8 | LAB | +97.82% | okx | +103.30% | bitget | +5.47% |
| 9 | SONY | +92.64% | bitget | +92.64% | okx | +0.00% |
| 10 | BB | +75.86% | okx | +81.33% | bitget | +5.47% |
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
