# Round-28 Price Validation Plan

1. Backfill tradable case price paths where symbols exist.
2. Keep synthetic, policy, and reference counterexamples as `needs_price_backfill` or `missing_price_data`.
3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.
4. Run shadow score-price alignment before production scoring changes.

## Priority Validation
- Nuclear/SMR: PPA and restart economics versus cost, licensing, and financing failure.
- Strategic metals: government support/offtake/price floor versus commodity price and governance events.
- Data-center REIT and utilities: FFO/AFFO, PPA, tariff, funding cost, debt, and CAPEX risk.
- RedTeam-first themes: North Korea, NFT/metaverse, advanced materials, and price-only rallies.
- AI infrastructure: integrated power/cooling/REIT/PPA evidence versus overbuild and grid-delay 4C cases.
