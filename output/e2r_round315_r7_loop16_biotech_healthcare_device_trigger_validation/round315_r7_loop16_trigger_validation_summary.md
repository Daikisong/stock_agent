# R7 Loop 16 Bio / Healthcare / Medical Device Trigger Validation

This is calibration-only material. Production scoring and candidate generation are unchanged.

Easy example: FDA approval is Stage2 evidence. It becomes Green only after royalty, sales, utilization, patent and manufacturing gates close.

## Summary
- source_round: `docs/round/round_315.md`
- round_id: `round_243`
- large_sector: `BIO_HEALTHCARE_MEDICAL_DEVICE`
- method: `trigger_level_backtest_v1_after_redteam`
- case_candidate_count: `9`
- trigger_count: `9`
- target_archetype_count: `9`
- stage2_actionable_candidate_count: `3`
- stage2_policy_or_localization_candidate_count: `4`
- stage3_yellow_candidate_count: `1`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `6`
- stage4c_watch_count: `3`
- hard_4c_case_count: `0`
- evidence_good_but_price_failed_or_muted_count: `3`
- row_separation_required: `True`
- production_scoring_changed: `False`
- candidate_generation_input: `False`
- shadow_weight_only: `True`
- full_adjusted_ohlc_complete: `False`
- price_validation_completed: `partial_with_reported_event_price_anchors`
- next_round: `R8 Loop 16`

## Core Finding
- Alteogen / Keytruda Qlex is the strongest Stage3-Yellow candidate, but direct KRX price and royalty economics are missing.
- SK Bioscience / IDT Biologika is Stage2-Actionable because deal value and +11.7% event reaction are visible.
- Samsung Biologics, Celltrion and pharma tariff cases are Stage2 localization or policy hedge until utilization and margin close.
- Samsung Bioepis / Amgen litigation and Yuhan / SC Rybrevant manufacturing observation remain 4B/4C-watch gates.
- Stage3-Green confirmed: `0`.
- Hard 4C confirmed: `0`.
