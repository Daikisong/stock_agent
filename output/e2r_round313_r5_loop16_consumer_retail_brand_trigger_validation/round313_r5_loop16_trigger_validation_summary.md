# R5 Loop 16 Consumer / Retail / Brands Trigger Validation

This is calibration-only material. Production scoring and candidate generation are unchanged.

Easy example: K-beauty U.S. channel expansion is Stage2 when e-commerce and retailer entry are visible. It is not Green until sell-through, repeat orders and margin are visible.

## Summary
- source_round: `docs/round/round_313.md`
- round_id: `round_241`
- large_sector: `CONSUMER_RETAIL_BRANDS`
- method: `trigger_level_backtest_v1_after_redteam`
- case_candidate_count: `8`
- trigger_count: `9`
- target_archetype_count: `8`
- stage2_actionable_candidate_count: `4`
- stage2_event_candidate_count: `3`
- stage3_yellow_candidate_count: `1`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `5`
- stage4c_watch_count: `3`
- hard_4c_case_count: `2`
- row_separation_required: `True`
- production_scoring_changed: `False`
- candidate_generation_input: `False`
- shadow_weight_only: `True`
- full_adjusted_ohlc_complete: `False`
- price_validation_completed: `partial_with_reported_event_price_anchors`

## Core Finding
- Brand, channel, tourism, JV and user-shift narratives must be separated from company margin, sell-through, GMV and FCF.
- Stage3-Yellow candidates: `Samyang Buldak`.
- Stage3-Green confirmed: `0`.
- Hard 4C references: Coupang breach and Homeplus restructuring.
