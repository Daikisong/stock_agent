# R1 Loop 16 Industrials / Orders / Infrastructure Trigger Validation

This is calibration-only material. Production scoring and candidate generation are unchanged.

Easy example: Samsung E&A's Fadhili order can be Stage2-Actionable because contract value and relative price reaction are clear. It is not Stage3-Green until margin and cash conversion are verified.

## Summary
- source_round: `docs/round/round_309.md`
- round_id: `round_237`
- large_sector: `INDUSTRIALS_ORDERS_INFRASTRUCTURE`
- method: `trigger_level_backtest_v1_after_redteam`
- case_candidate_count: `8`
- trigger_count: `8`
- target_archetype_count: `9`
- stage2_actionable_candidate_count: `3`
- stage2_event_candidate_count: `3`
- stage3_yellow_candidate_count: `4`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `4`
- stage4c_watch_count: `2`
- hard_4c_case_count: `0`
- evidence_good_but_price_muted_count: `2`
- row_separation_required: `True`
- production_scoring_changed: `False`
- candidate_generation_input: `False`
- shadow_weight_only: `True`
- full_adjusted_ohlc_complete: `False`
- price_validation_completed: `partial_with_reported_event_price_anchors`

## Core Finding
- Signed order, merger, transformer shortage, robotics stake, or cooling M&A headlines are not enough for Green.
- Stage2-Actionable needs contract size, event strength, company-specific backlog and no 4C overlay.
- Stage3-Green confirmed: `0`.
- Case rows, trigger rows and OHLC backfill rows must stay separate.
