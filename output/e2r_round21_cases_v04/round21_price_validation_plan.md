# Round-21 Price Validation Plan

1. Backfill official price paths for every `cases_v04_round21` record where a tradable symbol exists.
2. Keep private/reference cases as `missing_price_data` or `needs_price_backfill` until usable data exists.
3. Calculate stage price, peak price, MFE/MAE, and drawdown only from source data.
4. Compare shadow score weight hypotheses against price-path and EPS/FCF evidence.
5. Promote no weight to production until the archetype has enough success and counterexample coverage.

## Priority Checks
- AI cooling: real customers/orders versus cooling theme only.
- Waste/recycling: processing volume and FCF versus capacity theme.
- CDMO: utilization and customer diversification versus capacity overbuild.
- Rare metals: FCF/governance rerating versus tender-offer event premium.
