# Round-24 Price Validation Plan

1. Backfill tradable case price paths where symbols exist.
2. Keep policy, synthetic, and reference counterexamples as `needs_price_backfill` or `missing_price_data`.
3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.
4. Run shadow score-price alignment before production scoring changes.

## Priority Validation
- Rail: signed contract versus delivery, financing, and margin realization.
- Cloud/SaaS: recurring revenue and FCF versus AI-cost or churn pressure.
- Insurance/securities: ROE, capital, PF, cyber, and market-cycle boundaries.
- Solar/battery: policy benefit versus customs, subsidy, EV demand, and CAPA risks.
