# Round 253 R10 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_adjusted_ohlc_complete: false
- hard_4c_confirmed: true
- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.

## Backfill Fields

- price_data_source
- full_adjusted_ohlc_available
- reported_price_anchor
- reported_return_anchor
- stage1_price
- stage2_price
- stage3_price
- stage4b_price
- stage4c_price
- event_mfe_1d
- event_mae_1d
- relative_outperformance_pp
- contract_policy_safety_or_pf_anchor
- tenant_noi_affo_anchor
- price_validation_status
