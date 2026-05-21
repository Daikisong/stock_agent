# R3 Loop 16 Secondary Battery / EV / Green Trigger Validation

This is calibration-only material. Production scoring and candidate generation are unchanged.

Easy example: Samsung SDI's LFP ESS contract is Stage2-Actionable because contract value, delivery period, line conversion and price reaction are visible. It is not Green until ESS margin, line-retrofit yield and repeat orders are verified.

## Summary
- source_round: `docs/round/round_311.md`
- round_id: `round_239`
- large_sector: `SECONDARY_BATTERY_EV_GREEN`
- method: `trigger_level_backtest_v1_after_redteam`
- case_candidate_count: `8`
- trigger_count: `9`
- target_archetype_count: `8`
- stage2_actionable_candidate_count: `1`
- stage2_event_candidate_count: `3`
- stage3_yellow_candidate_count: `0`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `4`
- stage4c_watch_count: `3`
- hard_4c_case_count: `1`
- evidence_good_but_price_muted_count: `2`
- row_separation_required: `True`
- production_scoring_changed: `False`
- candidate_generation_input: `False`
- shadow_weight_only: `True`
- full_adjusted_ohlc_complete: `False`
- price_validation_completed: `partial_with_reported_event_price_anchors`

## Core Finding
- EV cell contracts, ESS conversion, lithium beta, restructuring relief, dilution and safety incidents must be separated.
- GWh or capex headline is not utilization, margin or FCF.
- Stage3-Green confirmed: `0`.
- Battery factory fire and quality failure are hard 4C safety evidence.
