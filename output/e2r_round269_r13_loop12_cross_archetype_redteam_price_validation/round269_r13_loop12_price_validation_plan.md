# Round 269 R13 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- r13_default_stage3_bias: redteam_first_after_price_validation
- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_return_anchor
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- mfe_1d
- mae_1d
- peak_return_from_stage3
- market_cap_anchor
- contract_value_anchor
- trust_break_cost_anchor
- macro_cost_anchor
- policy_or_theme_revenue_bridge
- hard_4c_before_price_damage
- price_validation_status
