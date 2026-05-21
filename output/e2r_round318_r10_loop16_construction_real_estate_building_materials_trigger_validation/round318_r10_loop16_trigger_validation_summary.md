# R10 Loop 16 Construction / Real Estate / Building Materials Trigger Validation

This is calibration-only material. Production scoring and candidate generation are unchanged.

Easy example: a PF support package can be Stage2 relief, but it is not Green until refinancing, write-offs, pre-sales and cashflow are actually visible.

## Summary
- source_round: `docs/round/round_318.md`
- round_id: `round_246`
- large_sector: `CONSTRUCTION_REAL_ESTATE_BUILDING_MATERIALS`
- method: `trigger_level_backtest_v1_after_redteam`
- case_candidate_count: `8`
- trigger_count: `8`
- target_archetype_count: `8`
- stage2_actionable_candidate_count: `2`
- stage2_candidate_count: `6`
- stage3_yellow_candidate_count: `4`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `6`
- stage4c_watch_count: `4`
- hard_4c_case_count: `1`
- evidence_good_but_price_failed_or_unavailable_count: `6`
- row_separation_required: `True`
- production_scoring_changed: `False`
- candidate_generation_input: `False`
- shadow_weight_only: `True`
- full_adjusted_ohlc_complete: `False`
- price_validation_completed: `partial_with_reported_event_price_anchors`
- next_round: `R11 Loop 16`

## Core Finding
- Samsung E&A / Fadhili is the cleanest Stage2-Actionable EPC case.
- Hyundai E&C / Jafurah is Stage2 mega-backlog, but company share, margin and price anchor are missing.
- PF / Taeyoung is 4C-watch with policy relief, not Green.
- Seoul housing supply and reconstruction policy is Stage2, but LTV tightening is demand 4B.
- Construction safety fatality is hard 4C.
- Samsung C&T / P5 is Stage2 AI fab construction until order value and margin are visible.
- Steel plate anti-dumping is supplier Stage2 and builder input-cost 4B.
- BOK rate-cut guidance is macro relief with housing-overheat 4B.
- Stage3-Green confirmed: `0`.
- Hard 4C confirmed: `1`.
