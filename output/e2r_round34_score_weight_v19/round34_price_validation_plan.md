# Round-34 Price Validation Plan

1. Backfill tradable case price paths where symbols exist.
2. Keep synthetic, global reference, event, and theme cases as `needs_price_backfill` or `missing_price_data`.
3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.
4. Run shadow score-price alignment before any production scoring change.

## Priority Validation
- Carbon/payment: recurring compliance or fintech FCF versus policy, greenwashing, take-rate, security, and credit risk.
- Optical/telecom: hyperscaler delivery economics versus telecom CAPEX cycle and geopolitics.
- Lithium/appliance/mobility: FCF defense and unit economics versus price cycle, hardware cycle, and regulatory cost.
- AI accelerator: revenue, customer validation, yield, and margin versus valuation overheat.
