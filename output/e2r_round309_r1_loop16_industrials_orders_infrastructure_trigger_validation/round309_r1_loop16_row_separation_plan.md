# Round 309 Row Separation Plan

Case evidence, trigger anchors and full OHLC windows must be separate rows.

Easy example: LS Electric can be a valid Stage2 grid event even if 30D/90D OHLC is not backfilled yet. It still cannot become Green without company backlog, capacity and margin.

- case_library_row_describes_what_happened_and_stage_candidate
- trigger_calibration_row_stores_event_anchor_contract_value_and_reported_return
- ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown
- do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing
