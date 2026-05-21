# R2 Loop 17 AI Semiconductor / Electronic Components Trigger Validation

This is calibration-only material. Production scoring and candidate generation are unchanged.

Easy example: OpenAI Stargate demand can be Stage2-Actionable, but a LOI is not a binding order, so Green remains blocked until volume, price and delivery economics are confirmed.

## Summary
- source_round: `docs/round/round_323.md`
- round_id: `round_251`
- loop_name: `R2 Loop 17`
- large_sector: `AI_SEMICONDUCTOR_ELECTRONIC_COMPONENTS`
- method: `trigger_level_backtest_v1_after_redteam`
- case_candidate_count: `8`
- trigger_count: `8`
- target_archetype_count: `8`
- stage2_actionable_candidate_count: `3`
- stage2_candidate_count: `5`
- stage3_yellow_candidate_count: `4`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `6`
- stage4c_watch_count: `0`
- strong_4c_case_count: `0`
- evidence_good_but_price_failed_count: `1`
- row_separation_required: `True`
- production_scoring_changed: `False`
- candidate_generation_input: `False`
- shadow_weight_only: `True`
- full_adjusted_ohlc_complete: `False`
- price_validation_completed: `partial_with_reported_event_price_anchors`
- next_round: `R3 Loop 17`

## Core Finding
- SK Hynix HBM3E mass production is Stage2-Actionable, not Green before customer volume/yield/ASP/margin.
- SK Hynix HBM4 certification is a Stage3-Yellow candidate, not Green before top-customer volume and capacity ramp.
- OpenAI Stargate memory LOI is a demand shock with 4B overlay because the order is not binding.
- Samsung HBM catch-up is Stage2 with labor and volume/yield gates.
- Hanmi Semiconductor is HBM packaging Stage2-Actionable with customer concentration and export-control gates.
- SK Hynix record profit with negative event return is evidence-good but price-failed.
- China export control and Samsung labor disruption are 4B overlays, not positive Green evidence.
- Stage3-Green confirmed: `0`.
- Strong 4C case count: `0`.
