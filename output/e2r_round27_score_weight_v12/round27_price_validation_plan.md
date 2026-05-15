# Round-27 Price Validation Plan

1. Backfill tradable case price paths where symbols exist.
2. Keep synthetic, policy, and reference counterexamples as `needs_price_backfill` or `missing_price_data`.
3. Calculate MFE/MAE, peak, drawdown, and below-entry flags only from source data.
4. Run shadow score-price alignment before production scoring changes.

## Priority Validation
- Game/IP: downloads and regional expansion versus monetization, OP, regulation, and single-IP risk.
- Medical device: export/device demand versus recurring procedure or consumables, approval, safety, and competition.
- Medical AI: external validation versus paid workflow, reimbursement, subgroup performance, and liability.
- Retail/e-commerce: store/logistics scale versus inventory, supplier regulation, data security, and FCF.
- Telecom/grid: AI grid need versus equipment order, margin, CAPEX burden, and regulation.
