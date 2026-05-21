# R4 Loop 16 Materials / Spread / Strategic Resources Trigger Validation

This is calibration-only material. Production scoring and candidate generation are unchanged.

Easy example: copper price can rise while smelter TC/RC collapses. In that case a copper headline is not company margin evidence.

## Summary
- source_round: `docs/round/round_312.md`
- round_id: `round_240`
- large_sector: `MATERIALS_SPREAD_STRATEGIC_RESOURCES`
- method: `trigger_level_backtest_v1_after_redteam`
- case_candidate_count: `9`
- trigger_count: `11`
- target_archetype_count: `9`
- stage2_actionable_candidate_count: `2`
- stage2_event_candidate_count: `5`
- stage3_yellow_candidate_count: `0`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `5`
- stage4c_watch_count: `4`
- hard_4c_case_count: `0`
- evidence_good_but_price_failed_or_muted_count: `3`
- row_separation_required: `True`
- production_scoring_changed: `False`
- candidate_generation_input: `False`
- shadow_weight_only: `True`
- full_adjusted_ohlc_complete: `False`
- price_validation_completed: `partial_with_reported_event_price_anchors`

## Core Finding
- Commodity price, policy, capex, restructuring and strategic-resource headlines must be separated from company spread, margin, offtake and FCF.
- Stage3-Green confirmed: `0`.
- Strong 4B/4C watch items: U.S. steel tariffs, petrochemical oversupply, Korea Zinc dilution/governance and copper TC/RC compression.
