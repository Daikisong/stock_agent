# Round 244 R1 Loop 11 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.

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
- mfe_30d
- mae_30d
- contract_value_anchor
- ipo_price_anchor
- target_price_anchor
- legal_or_sanction_anchor
- price_validation_status
