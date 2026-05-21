# Round 323 Row Separation Plan

AI semiconductor rows must separate case evidence, trigger anchors and full adjusted OHLC backfill.

Easy example: SK Hynix record profit is good evidence, but a -4% event reaction means it stays evidence-good/price-failed until later price and revision evidence repairs it.

- case_library_row_describes_stage_candidate_and_evidence_quality
- trigger_calibration_row_stores_reported_event_return_market_relative_return_customer_and_supply_metrics
- ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown
- do_not_create_MFE_MAE_without_full_adjusted_OHLC
- do_not_treat_HBM_mass_production_certification_LOI_or_record_profit_as_Green_without_volume_yield_ASP_margin_capacity_and_risk_resolution
