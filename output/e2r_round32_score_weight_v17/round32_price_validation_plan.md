# Round-32 Price Validation Plan

1. Backfill tradable case price paths where symbols exist.
2. Keep synthetic, global reference, and theme counterexamples as `needs_price_backfill` or `missing_price_data`.
3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.
4. Run shadow score-price alignment before any production scoring change.

## Priority Validation
- Trading/resource: long-term contracts and capital return versus commodity cycle and conglomerate discount.
- Energy/LNG/gas: pass-through and FCF versus tariff, receivables, inventory, and geopolitics.
- OLED/components: customer orders and margins versus CAPEX, price competition, inventory, and supply chain risk.
- Digital healthcare and AI chip: recurring revenue, reimbursement, contracts, validation, yield, and EPS conversion before Green-like interpretation.
