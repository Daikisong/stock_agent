# Round 254 R11 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- hard_4c_confirmed: true
- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_return_anchor
- index_anchor
- fx_anchor
- capital_flow_anchor
- policy_amount_anchor
- stage1_price
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- mfe_1d
- mae_1d
- price_validation_status
