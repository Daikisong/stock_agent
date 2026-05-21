# R1 Loop 17 Industrials / Orders / Infrastructure Trigger Validation

This is calibration-only material. Production scoring and candidate generation are unchanged.

Easy example: a shipbuilding merger can be Stage2-Actionable when price reacts strongly, but it is not Green until actual orders, workshare, margin and legal gates close.

## Summary
- source_round: `docs/round/round_322.md`
- round_id: `round_250`
- loop_name: `R1 Loop 17`
- large_sector: `INDUSTRIALS_ORDERS_INFRASTRUCTURE`
- method: `trigger_level_backtest_v1_after_redteam`
- case_candidate_count: `8`
- trigger_count: `10`
- target_archetype_count: `8`
- stage2_actionable_candidate_count: `3`
- stage2_candidate_count: `7`
- stage2_promote_candidate_count: `1`
- stage3_yellow_candidate_count: `4`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `7`
- stage4c_watch_count: `2`
- strong_4c_case_count: `1`
- evidence_good_but_price_failed_count: `1`
- row_separation_required: `True`
- production_scoring_changed: `False`
- candidate_generation_input: `False`
- shadow_weight_only: `True`
- full_adjusted_ohlc_complete: `False`
- price_validation_completed: `partial_with_reported_event_price_anchors`
- next_round: `R2 Loop 17`

## Core Finding
- HD Hyundai Heavy / Mipo is the cleanest Stage2-Actionable anchor, but U.S. order/workshare and post-merger margin are still gates.
- Hanwha Ocean is Stage2 naval optionality with China sanction 4B.
- Hyundai Rotem is a Stage3-Yellow candidate because repeat K2 export and local production are visible, but margin and delivery remain gates.
- HD Hyundai Electric is a Stage2 promote / missed-structural risk if AI power-equipment demand is ignored.
- LS Electric is evidence-good but price-failed.
- Hyosung Heavy is transformer capacity Stage2 without direct price/orderbook validation.
- Doosan Enerbility is SMR/AI-power Stage2, not Green before final equipment contract and workshare.
- Samsung Heavy Zvezda cancellation is the strong 4C backlog-quality break.
- Stage3-Green confirmed: `0`.
- Strong 4C case count: `1`.
