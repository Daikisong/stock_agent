# R13 Loop 15 Cross-Archetype RedTeam / Price Validation

This is calibration-only material. Production scoring and candidate generation are unchanged.

Easy example: Samyang's ASP/shipment/capacity/OP-estimate bundle can lift Stage2 to Actionable review, while Jensen's fried-chicken event cannot because there is no direct revenue bridge.

## Summary
- source_round: `docs/round/round_308.md`
- round_id: `round_236`
- large_sector: `CROSS_ARCHETYPE_REDTEAM`
- method: `trigger_level_backtest_v1_redteam`
- case_candidate_count: `8`
- trigger_count: `9`
- target_archetype_count: `10`
- stage2_actionable_candidate_count: `3`
- stage3_yellow_candidate_count: `2`
- stage3_green_confirmed_count: `0`
- stage4b_watch_count: `4`
- stage4c_watch_count: `4`
- hard_4c_case_count: `2`
- evidence_good_but_price_failed_count: `1`
- price_moved_without_evidence_count: `1`
- row_separation_required: `True`
- production_scoring_changed: `False`
- candidate_generation_input: `False`
- shadow_weight_only: `True`
- full_adjusted_ohlc_complete: `False`
- price_validation_completed: `partial_with_reported_event_price_anchors`

## Core Finding
- Stage2 can be too conservative when estimate revision, shipment/delivery, capacity and price reaction arrive together.
- CB, control premium, IPO, policy, celebrity and platform-scale headlines need 4B/4C overlays instead of Green promotion.
- Hard 4C: platform security breach and fatal safety incident.
- Stage3-Green confirmed: `0`.
- Case rows, trigger rows and OHLC backfill rows must stay separate.
