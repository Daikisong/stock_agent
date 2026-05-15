# Round-29 Price Validation Plan

1. Backfill tradable case price paths where symbols exist.
2. Keep synthetic, theme, and reference counterexamples as `needs_price_backfill` or `missing_price_data`.
3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.
4. Run shadow score-price alignment before any production scoring change.

## Priority Validation
- Defense: Romania K9/order backlog versus dilution and capital allocation risk.
- Shipbuilding: newbuilding price and orderbook quality versus low-margin backlog and cost inflation.
- K-food: export/ASP/OPM/CAPA versus single-product, recall, inventory, and channel-stuffing risks.
- Chemicals and batteries: spread/ESS candidates versus supply glut, EV slowdown, CAPEX overbuild, and mineral-price risk.
- Finance/value-up: ROE, capital ratio, CSM, actual cancellation, and shareholder-return execution.
