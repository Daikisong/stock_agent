# R3 Loop 17 Secondary Battery / EV / Green Trigger Validation

This is calibration-only material. Production scoring and candidate generation are unchanged.

Easy example: an ESS contract can promote Stage2 when contract value and event return are clear, but it is not Green until customer, utilization and margin are confirmed.

## Summary
- source_round: `docs/round/round_324.md`
- round_id: `round_252`
- loop_name: `R3 Loop 17`
- large_sector: `SECONDARY_BATTERY_EV_GREEN`
- method: `trigger_level_backtest_v1_after_redteam`
- case_candidate_count: `8`
- trigger_count: `9`
- target_archetype_count: `8`
- stage2_actionable_candidate_count: `1`
- stage2_candidate_count: `5`
- stage3_yellow_candidate_count: `4`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `5`
- stage4c_watch_count: `1`
- strong_4c_case_count: `1`
- policy_credit_4b_count: `1`
- cyclical_stage2_count: `1`
- row_separation_required: `True`
- production_scoring_changed: `False`
- candidate_generation_input: `False`
- shadow_weight_only: `True`
- full_adjusted_ohlc_complete: `False`
- price_validation_completed: `partial_with_reported_event_price_anchors`
- next_round: `R4 Loop 17`

## Core Finding
- Samsung SDI ESS LFP is the cleanest Stage2-Actionable anchor.
- LGES Ford/Freudenberg cancellations are a strong 4C contract-quality break.
- SK On ESS pivot is Stage2, but parent readthrough and losses remain 4B.
- POSCO Future M / L&F lithium rebound is cyclical Stage2, not Green.
- Samsung SDI solid-state timeline is a Stage3-Yellow candidate, not Green before pilot yield and revenue.
- LGES AMPC earnings are policy-credit 4B because ex-AMPC margin is near zero.
- Samsung SDI capital raise is dilution 4B.
- POSCO / MinRes lithium JV is Stage2 no-price until direct KRX price, offtake and margin are available.
- Stage3-Green confirmed: `0`.
- Strong 4C case count: `1`.
