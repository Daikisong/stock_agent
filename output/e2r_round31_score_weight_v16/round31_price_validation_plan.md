# Round-31 Price Validation Plan

1. Backfill tradable case price paths where symbols exist.
2. Keep synthetic, theme, and reference counterexamples as `needs_price_backfill` or `missing_price_data`.
3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.
4. Run shadow score-price alignment before any production scoring change.

## Priority Validation
- Data-center REIT: lease/occupancy/FFO/AFFO versus power/water and funding-cost 4C.
- Waste: permits/utilization/recurring FCF versus low utilization and CAPEX pressure.
- Medical device: export/consumables/OPM versus VBP, approval delay, and ASP pressure.
- Regulated consumer and apparel: approval/channel/brand growth versus bans, IP litigation, markdown, and inventory.
- AI infrastructure/value-up: split evidence axes and prove execution before Green-like interpretation.
