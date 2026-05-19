# Round 215 R11 Price Validation Plan

- price_validation_completed: partial_with_reported_price_anchors
- full_ohlc_complete: false
- r11_default_stage3_bias: very_conservative
- Do not invent OHLC, peak, MFE, or MAE where raw adjusted daily prices are unavailable.

## Backfill Fields

- price_data_source
- full_ohlc_available
- reported_price_anchor
- reported_return_anchor
- event_peak_price
- event_mfe_1d_pct
- reported_mfe_3m_pct
- macro_market_mae_pct
- contract_or_budget_amount
- event_duration_days
- validation_or_replication_status
- price_validation_status
