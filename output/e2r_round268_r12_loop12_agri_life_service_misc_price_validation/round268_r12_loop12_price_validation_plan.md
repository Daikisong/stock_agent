# Round 268 R12 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- hard_4c_confirmed: false
- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_return_anchor
- business_metric_anchor
- policy_metric_anchor
- input_cost_anchor
- stage1_price
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- mfe_event
- mae_event
- price_validation_status
