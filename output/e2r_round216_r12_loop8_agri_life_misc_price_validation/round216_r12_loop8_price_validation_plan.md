# Round 216 R12 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- r12_default_stage3_bias: conservative_except_recurring_service
- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_return_anchor
- reported_event_mfe_1d_range
- reported_event_mfe_1d_midpoint
- quota_original
- quota_2027
- quota_2030
- quota_increase_pct
- event_duration_days
- uav_counting_accuracy
- uav_weight_estimation_accuracy
- business_anchor
- price_validation_status
