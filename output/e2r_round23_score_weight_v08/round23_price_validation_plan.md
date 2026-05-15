# Round-23 Price Validation Plan

1. Backfill tradable case price paths where symbols exist.
2. Keep reference, policy, and synthetic counterexample cases as `needs_price_backfill` or `missing_price_data`.
3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.
4. Run shadow score-price alignment before production scoring changes.

## Priority Validation
- Medical AI: clinical proof versus reimbursement and paid usage.
- Telecom/6G: CAPEX theme versus actual orders/revenue.
- Media/content: repeat IP monetization versus hit-driven risk.
- HBM/data-center: structural EPS evidence versus 4B crowding.
