# Round-25 Price Validation Plan

1. Backfill tradable case price paths where symbols exist.
2. Keep policy, synthetic, and reference counterexamples as `needs_price_backfill` or `missing_price_data`.
3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.
4. Run shadow score-price alignment before production scoring changes.

## Priority Validation
- AI cooling: order/delivery/service revenue versus AI CAPEX delay and project margin damage.
- Security: recurring subscription versus major outage and legal trust break.
- HBM: structural EPS success versus crowding, market-cap saturation, and capex reversal.
- Solar/battery: policy benefit versus customs, subsidy, EV demand, and CAPA risks.
