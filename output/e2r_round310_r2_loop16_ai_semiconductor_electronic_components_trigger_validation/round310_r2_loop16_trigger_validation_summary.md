# R2 Loop 16 AI Semiconductor / Electronic Components Trigger Validation

This is calibration-only material. Production scoring and candidate generation are unchanged.

Easy example: SK Hynix HBM4 certification can be a Stage3-Yellow candidate because sample/certification/capacity evidence is visible. It is not confirmed Green until volume shipment, margin, customer concentration and full OHLC validation clear.

## Summary
- source_round: `docs/round/round_310.md`
- round_id: `round_238`
- large_sector: `AI_SEMICONDUCTOR_ELECTRONIC_COMPONENTS`
- method: `trigger_level_backtest_v1_after_redteam`
- case_candidate_count: `9`
- trigger_count: `11`
- target_archetype_count: `9`
- stage2_actionable_candidate_count: `4`
- stage2_event_candidate_count: `2`
- stage3_yellow_candidate_count: `4`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `5`
- stage4c_watch_count: `3`
- hard_4c_case_count: `0`
- evidence_good_but_price_failed_count: `3`
- row_separation_required: `True`
- production_scoring_changed: `False`
- candidate_generation_input: `False`
- shadow_weight_only: `True`
- full_adjusted_ohlc_complete: `False`
- price_validation_completed: `partial_with_reported_event_price_anchors`

## Core Finding
- HBM, memory ASP, OpenAI/Stargate, foundry, packaging equipment, export-control, labor and sensor partnership rows must stay separate.
- Stage2-Actionable needs event evidence and direct economic bridge, not only AI semiconductor wording.
- Stage3-Green confirmed: `0`.
- OHLC backfill missing should not downgrade valid Stage2 or Yellow candidates.
