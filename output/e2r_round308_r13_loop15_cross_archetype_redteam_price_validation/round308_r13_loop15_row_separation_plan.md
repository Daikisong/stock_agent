# Round 308 Row Separation Plan

Case evidence, trigger anchors and full OHLC windows must be separate rows.

Easy example: Samyang can be a valid Stage2-Actionable case even if 30D/90D OHLC has not been backfilled yet.

- case_library_row_describes_what_happened_and_stage_candidate
- trigger_calibration_row_stores_entry_anchor_and_reported_event_return
- ohlc_backfill_row_stores_adjusted_OHLC_MFE_MAE_below_entry_peak_drawdown
- do_not_downgrade_valid_Stage2_or_Yellow_candidate_only_because_OHLC_backfill_is_missing
