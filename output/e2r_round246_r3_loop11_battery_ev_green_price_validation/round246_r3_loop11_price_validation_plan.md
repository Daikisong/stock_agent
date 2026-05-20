# Round 246 R3 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.
- Month-only risk events, such as the Hyundai-LG Georgia raid, are stored as metadata rather than fabricated exact dates.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_return_anchor
- stage2_price_anchor
- stage3_price
- stage4b_price
- stage4c_price
- mfe_1d
- mae_1d
- contract_value_anchor
- gwh_or_capacity_anchor
- delivery_or_supply_period_anchor
- utilization_or_labor_execution_anchor
- lost_revenue_or_cancellation_anchor
- price_validation_status
