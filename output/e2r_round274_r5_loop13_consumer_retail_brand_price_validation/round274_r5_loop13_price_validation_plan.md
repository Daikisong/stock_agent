# Round 274 R5 Loop 13 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_complete
- reported_price_anchor
- reported_return_anchor
- stage2_price_anchor
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_pct
- event_mae_pct
- business_anchor
- sellthrough_or_reorder_anchor
- gross_margin_or_tariff_anchor
- data_or_credit_gate
- price_validation_status
