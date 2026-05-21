# R4 Loop 17 Materials / Spreads / Strategic Resources Trigger Validation

This is calibration-only material. Production scoring and candidate generation are unchanged.

Easy example: anti-dumping can be Stage2 when tariff and price reaction are clear, but it is not Green until actual margin recovery is visible.

## Summary
- source_round: `docs/round/round_325.md`
- round_id: `round_253`
- loop_name: `R4 Loop 17`
- large_sector: `MATERIALS_SPREADS_STRATEGIC_RESOURCES`
- method: `trigger_level_backtest_v1_after_redteam`
- case_candidate_count: `9`
- trigger_count: `13`
- target_archetype_count: `10`
- stage2_actionable_candidate_count: `1`
- stage2_candidate_count: `6`
- stage3_yellow_candidate_count: `5`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `8`
- hard_4c_confirmed_count: `0`
- strong_4c_watch_count: `5`
- row_separation_required: `True`
- production_scoring_changed: `False`
- candidate_generation_input: `False`
- shadow_weight_only: `True`
- full_adjusted_ohlc_complete: `False`
- price_validation_completed: `partial_with_reported_event_price_anchors`
- next_round: `R5 Loop 17`

## Core Finding
- Korea Zinc control premium is Stage2, not operating Green.
- Korea Zinc TC cut is a smelter-margin 4B.
- Korea Zinc U.S. critical-minerals plant is Stage2 with capex/dilution 4B.
- Hyundai Steel/POSCO anti-dumping is the cleanest Stage2-Actionable trigger.
- Hyundai/POSCO Louisiana steel plant is localization Stage2 with tariff 4B.
- Petrochemical oversupply is failed rerating with restructuring relief only.
- SK Innovation refining spread is a mixed recovery candidate.
- POSCO/MinRes lithium JV is upstream Stage2 with no POSCO direct price validation.
- China rare-earth export control is sector-wide 4B.
- Stage3-Green confirmed: `0`.
