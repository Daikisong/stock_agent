# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R12_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
scheduled_round = R12
scheduled_loop = 14
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 3 counterexamples, and 3 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does not re-prove the global Stage2 bonus. It stress-tests a narrower C31 residual: when a service/tourism reopening policy headline appears, the score must distinguish a direct booking-volume route from a looser inbound-tourism or domestic-capacity story. In other words, the policy headline is a key; it only opens the door when the company actually stands behind that door.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R12
scheduled_loop = 14
round_schedule_source = local v12 continuation and previous completed R11 Loop 14 state; local registry showed R12 Loop 14 missing while R1~R11 Loop 14 existed
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS
```

R12 may use L10 for agriculture/life-services/miscellaneous event propagation. This file is kept in L10/C31 because the driver is not ordinary consumer export reorder; it is a public travel/reopening policy event.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifact access was limited to calibration registry/representative rows. `data/e2r/calibration/md_registry.jsonl` was read as registry context and `data/e2r/calibration/trigger_rows_representative.jsonl` contained no representative rows in the checked branch. Local v12 continuation files showed previous R12 loops focused on agri/feed, public-health food-safety, and one governance/tender study. No same symbol + trigger_date + entry_date repetition was used here.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = none
new_symbol_count = 4
new_trigger_family_count = 4
new_independent_case_ratio = 1.00
minimum_new_independent_case_ratio = 0.60
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest validation:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema confirms that tradable shards use `d,o,h,l,c,v,a,mc,s,m` and that MFE/MAE are computed from high/low over forward tradable rows. The max date used for forward-window availability is `2026-02-20`, not the current calendar date.

## 5. Historical Eligibility Gate

|case|symbol|profile status|corporate action window|forward 180D|calibration usable|
|---|---|---|---|---|---|
|하나투어 Japan reopening|039130|active_like; last_date 2026-02-20|clean for 2022~2023; old 2003/2004 candidates only|available|true|
|GKL China group tour|114090|active_like; last_date 2026-02-20|clean; corporate_action_candidate_count=0|available|true|
|파라다이스 China group tour|034230|active_like; last_date 2026-02-20|clean; corporate_action_candidate_count=0|available|true|
|강원랜드 domestic reopening|035250|active_like; last_date 2026-02-20|clean for 2022; old 2003 candidate only|available|true|


Every representative trigger has entry row, positive OHLCV, at least 180 forward trading rows, and no 180D corporate-action contamination.

## 6. Canonical Archetype Compression Map

```text
fine_archetype_id = SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
compression_reason = travel reopening, group-tour permission, and distancing removal are policy/event shocks; scoring should compress to C31 with route-directness subguards rather than C18/C20 consumer channel rules.
```

## 7. Case Selection Summary

|case_id|symbol|company|role|new?|reason|
|---|---|---|---|---|---|
|R12L14C31_039130_JAPAN_REOPENING_DIRECT_BOOKING|039130|하나투어|positive|yes|Japan individual tourism/visa-waiver reopening created a direct outbound booking route; actual MFE was meaningful while drawdown stayed contained.|
|R12L14C31_114090_CHINA_GROUP_TOUR_CASINO_FALSE_POSITIVE|114090|GKL|counterexample|yes|China group-tour unban created a headline gap but casino visitation/revenue translation lagged; high MAE argues for route-lag guard.|
|R12L14C31_034230_CHINA_GROUP_TOUR_CASINO_EVENT_FADE|034230|파라다이스|counterexample|yes|Same inbound-tourism event had an opening spike but no durable rerating; price-only event peak should not become Green.|
|R12L14C31_035250_DOMESTIC_REOPENING_CAPACITY_GUARD|035250|강원랜드|counterexample|yes|Domestic distancing removal had weak upside and later drawdown; captive capacity/regulatory constraints blunt the policy headline.|


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 3
4B_case_count = 3
4C_case_count = 0
calibration_usable_case_count = 4
calibration_usable_trigger_count = 7
```

The balance is intentionally counterexample-heavy. The residual problem is not that reopening headlines never work; the 하나투어 case shows that a direct booking route can work. The problem is that a looser tourism headline can dress up weak conversion as if it were Stage3 evidence.

## 9. Evidence Source Map

| Evidence family | Trigger date | Evidence available then | Score use |
|---|---|---|---|
| Japan visa-free / individual tourism reopening | 2022-10-11 | Japan resumed individual inbound travel and visa waivers from this date; outbound Korea travel agencies had direct booking exposure. | Stage2 direct-route positive, not Green without revision. |
| Korea domestic social-distancing removal | 2022-04-18 | Korea removed most distancing limits, creating reopening optionality for offline leisure/casino. | Stage2 watch only when capacity/regulatory constraints limit earnings pass-through. |
| China group-tour resumption to Korea | 2023-08-10 | China outbound group-tour approval for Korea triggered immediate casino/travel-service relative strength. | Counterexample guard: indirect inbound route needs revenue conversion evidence. |
| Event price peak after headline | 2023-08~09 / 2023-03 | Local price highs appeared before durable revenue/revision confirmation. | 4B overlay only; price-only peak cannot promote Stage3/Green. |

## 10. Price Data Source Map

|symbol|company|price_shard_path|profile_path|
|---|---|---|---|
|039130|하나투어|atlas/ohlcv_tradable_by_symbol_year/039/039130/2022.csv|atlas/symbol_profiles/039/039130.json|
|114090|GKL|atlas/ohlcv_tradable_by_symbol_year/114/114090/2023.csv|atlas/symbol_profiles/114/114090.json|
|034230|파라다이스|atlas/ohlcv_tradable_by_symbol_year/034/034230/2023.csv|atlas/symbol_profiles/034/034230.json|
|035250|강원랜드|atlas/ohlcv_tradable_by_symbol_year/035/035250/2022.csv|atlas/symbol_profiles/035/035250.json|


## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|type|entry|MFE90|MAE90|MFE180|MAE180|peak|current verdict|aggregate|
|---|---|---|---|---|---|---|---|---|---|---|
|R12L14C31_039130_T_STAGE2_20221011|039130|Stage2-Actionable|2022-10-11 @ 50600|29.45|-6.82|31.82|-6.82|2023-03-02 / 66700|current_profile_correct|representative|
|R12L14C31_039130_T_4B_20230302|039130|Stage4B-overlay|2023-03-02 @ 65100|2.46|-11.52|2.46|-11.52|2023-03-02 / 66700|current_profile_4B_too_late|4B_overlay_only|
|R12L14C31_114090_T_STAGE2_20230810|114090|Stage2-Actionable|2023-08-10 @ 15900|13.65|-17.92|13.65|-24.84|2023-09-12 / 18070|current_profile_false_positive|representative|
|R12L14C31_114090_T_4B_20230911|114090|Stage4B-overlay|2023-09-11 @ 17690|2.15|-32.45|2.15|-32.45|2023-09-12 / 18070|current_profile_4B_too_late|4B_overlay_only|
|R12L14C31_034230_T_STAGE2_20230810|034230|Stage2-Actionable|2023-08-10 @ 17070|8.67|-22.91|8.67|-28.47|2023-08-14 / 18550|current_profile_false_positive|representative|
|R12L14C31_034230_T_4B_20230814|034230|Stage4B-overlay|2023-08-14 @ 18010|3.0|-32.2|3.0|-32.2|2023-08-14 / 18550|current_profile_4B_too_late|4B_overlay_only|
|R12L14C31_035250_T_STAGE2_20220418|035250|Stage2-Watch|2022-04-18 @ 27250|5.14|-14.13|5.14|-17.06|2022-06-10 / 28650|current_profile_false_positive|representative|


## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|entry_price|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|below_entry_90D|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|
|R12L14C31_039130_T_STAGE2_20221011|50600|7.51|29.45|31.82|-6.82|-6.82|-6.82|True|-14.47|
|R12L14C31_039130_T_4B_20230302|65100|2.46|2.46|2.46|-11.52|-11.52|-11.52|True|-14.47|
|R12L14C31_114090_T_STAGE2_20230810|15900|13.65|13.65|13.65|-8.11|-17.92|-24.84|True|-33.87|
|R12L14C31_114090_T_4B_20230911|17690|2.15|2.15|2.15|-26.23|-32.45|-32.45|True|-33.87|
|R12L14C31_034230_T_STAGE2_20230810|17070|8.67|8.67|8.67|-9.08|-22.91|-28.47|True|-34.18|
|R12L14C31_034230_T_4B_20230814|18010|3.0|3.0|3.0|-26.93|-32.2|-32.2|True|-34.18|
|R12L14C31_035250_T_STAGE2_20220418|27250|4.22|5.14|5.14|-9.17|-14.13|-17.06|True|-21.12|


The key contrast is visible in the first and second rows. 하나투어's direct booking route had 29.45% MFE90 with -6.82% MAE90. GKL and 파라다이스 also had headline gaps, but their MFE was consumed quickly while 90D/180D MAE expanded. 강원랜드 had reopening optionality but too little upside against drawdown.

## 13. Current Calibrated Profile Stress Test

| case | current calibrated profile judgment | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| 하나투어 | Stage2-Actionable; no Green without revision. | Correct: MFE90 29.45%, MAE90 -6.82%. | current_profile_correct |
| GKL | Could over-promote if policy + relative strength were treated as enough for Yellow. | Wrong: MFE90 13.65%, MAE180 -24.84%; reward-to-drawdown deteriorated. | current_profile_false_positive |
| 파라다이스 | Same China group-tour headline could look like reopening Stage2/Yellow. | Wrong: MFE90 8.67%, MAE180 -28.47%; high-MAE fade. | current_profile_false_positive |
| 강원랜드 | Domestic reopening headline could become a weak Stage2. | Too generous: MFE90 5.14%, MAE180 -17.06%. | current_profile_false_positive |

Existing axis status:

```text
stage2_actionable_evidence_bonus = existing_axis_tested; kept for direct booking route, guarded for indirect route
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_strengthened for service reopening
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is assigned. The audit conclusion is that reopening headlines are usually Stage2-Watch or Stage2-Actionable until booking/revenue conversion or revision evidence arrives. The Green threshold is not too strict for this sub-archetype; if anything, Green should remain hard because event windows can fade like a wave that reaches shore before the ship arrives.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger in clean evidence set
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 039130 March 2023 overlay | 0.901 | 0.901 | price_only + positioning_overheat | Good local overlay, but still not full 4B without non-price evidence. |
| 114090 September 2023 overlay | 0.825 | 0.825 | price_only + positioning_overheat | Good local 4B, supports event-age cap. |
| 034230 August 2023 overlay | 0.635 | 0.635 | price_only + positioning_overheat | Too early as full 4B; useful as watch/overlay only. |

## 16. 4C Protection Audit

No hard 4C was assigned. The false positives were not thesis-break failures; they were event-conversion failures. Label: `thesis_break_watch_only` for all rows. A later hard 4C would require evidence such as cancelled travel policy, regulatory reclosure, or confirmed earnings deterioration.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = true
rule_name = service_reopening_direct_booking_route_score
positive_delta = +8 for direct outbound booking / directly monetized reopening route
negative_guards = inbound_group_tour_lag_penalty -8; captive_capacity_regulation_guard -8
```

The rule is sector-specific because it concerns travel/casino/service reopening mechanics. A headline is not a cash register. It becomes one only when the route from policy to booking, visitation, or revenue is short and observable.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = true
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rule_name = policy_route_directness_guard
```

For C31, a public policy event should be split into three lanes:

1. `direct_monetization_route`: can be Stage2-Actionable.
2. `indirect_recovery_route`: stays Stage2-Watch until conversion evidence.
3. `capacity_or_regulatory_constraint_route`: capped or blocked unless the constraint is explicitly removed and financial visibility follows.

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|FP rate|verdict|
|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_proxy|4|14.23|-15.45|14.82|-19.3|0.75|mixed; direct route works, casino/group-tour/captive-capacity false positives remain|
|P0b_e2r_2_0_baseline_reference|rollback_reference|4|14.23|-15.45|14.82|-19.3|0.5|avoids some false positives but misses direct route earlier|
|P1_sector_service_reopening_shadow|sector_specific|4|29.45|-6.82|31.82|-6.82|0.0|improved; only direct route promoted|
|P2_C31_service_policy_route_shadow|canonical_archetype_specific|4|29.45|-6.82|31.82|-6.82|0.0|best candidate for canonical C31 sub-rule|
|P3_counterexample_guard_profile|counterexample_guard|3|9.15|-18.32|9.15|-23.46|0.0|guard removes high-MAE false positives|


## 20. Score-Return Alignment Matrix

| symbol | before score / label | after score / label | MFE90 / MAE90 | alignment verdict |
|---:|---|---|---|---|
| 039130 | 77 / Stage2-Actionable | 84 / Stage2-Actionable | 29.45 / -6.82 | Keep positive Stage2, no Green. |
| 114090 | 78 / Stage3-Yellow risk | 62 / Stage2-Watch/Blocked | 13.65 / -17.92 | Guard improves false-positive control. |
| 034230 | 77 / Stage3-Yellow risk | 61 / Stage2-Watch/Blocked | 8.67 / -22.91 | Guard improves false-positive control. |
| 035250 | 73 / Stage2-Watch | 56 / Stage2-Watch/Blocked | 5.14 / -14.13 | Capacity/regulation guard improves alignment. |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L10_POLICY_EVENT_CROSS_REDTEAM_MISC|C31_POLICY_SUBSIDY_LEGISLATION_EVENT|SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS|1|3|3|0|4|0|7|4|3|true|true|service reopening route covered; still needs more positive direct-booking cases|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: indirect_policy_headline_false_positive, inbound_group_tour_revenue_lag, captive_capacity_regulation_guard, price_only_event_peak_4B_late
new_axis_proposed: service_reopening_direct_booking_route_score; inbound_group_tour_lag_penalty; captive_capacity_regulation_guard
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; stage3_green_revision_min
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: sector_specific_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical trigger-level OHLC backtest only.
- Stock-Web tradable_raw shard rows only.
- Past policy/reopening events only.
- Shadow-only sector/canonical rule proposal.
```

Non-validation scope:

```text
- No current/live stock discovery.
- No investment recommendation.
- No stock_agent code read or patch.
- No production scoring change.
- No broker/API/autotrading action.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,service_reopening_direct_booking_route_score,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,+8,+8,"Direct outbound booking route had 29.45% MFE90 and contained MAE; promote Stage2 only, not Green without revision.","Improves alignment by isolating 039130 from indirect casino/captive cases",R12L14C31_039130_T_STAGE2_20221011,4,4,3,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,inbound_group_tour_lag_penalty,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,-8,-8,"China group-tour headline caused opening gaps but GKL/Paradise had high MAE and no immediate revenue conversion proof.","Blocks two false-positive Yellow/Green promotions",R12L14C31_114090_T_STAGE2_20230810|R12L14C31_034230_T_STAGE2_20230810,4,4,3,medium,canonical_shadow_only,"not production; policy route-lag guard"
shadow_weight,captive_capacity_regulation_guard,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,-8,-8,"Domestic reopening does not automatically unlock earnings when capacity/regulatory constraints dominate.","Blocks weak MFE / high MAE reopening false positive",R12L14C31_035250_T_STAGE2_20220418,4,4,3,low,sector_shadow_only,"needs more domestic service cases"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L14C31_039130_JAPAN_REOPENING_DIRECT_BOOKING", "symbol": "039130", "company_name": "하나투어", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "R12L14C31_039130_T_STAGE2_20221011", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_direct_route", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Japan individual tourism/visa-waiver reopening created a direct outbound booking route; actual MFE was meaningful while drawdown stayed contained."}
{"row_type": "case", "case_id": "R12L14C31_114090_CHINA_GROUP_TOUR_CASINO_FALSE_POSITIVE", "symbol": "114090", "company_name": "GKL", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L14C31_114090_T_STAGE2_20230810", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "China group-tour unban created a headline gap but casino visitation/revenue translation lagged; high MAE argues for route-lag guard."}
{"row_type": "case", "case_id": "R12L14C31_034230_CHINA_GROUP_TOUR_CASINO_EVENT_FADE", "symbol": "034230", "company_name": "파라다이스", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L14C31_034230_T_STAGE2_20230810", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Same inbound-tourism event had an opening spike but no durable rerating; price-only event peak should not become Green."}
{"row_type": "case", "case_id": "R12L14C31_035250_DOMESTIC_REOPENING_CAPACITY_GUARD", "symbol": "035250", "company_name": "강원랜드", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R12L14C31_035250_T_STAGE2_20220418", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Domestic distancing removal had weak upside and later drawdown; captive capacity/regulatory constraints blunt the policy headline."}
{"row_type": "trigger", "trigger_id": "R12L14C31_039130_T_STAGE2_20221011", "case_id": "R12L14C31_039130_JAPAN_REOPENING_DIRECT_BOOKING", "symbol": "039130", "company_name": "하나투어", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS", "sector": "농업·생활서비스·기타 / 관광·카지노·여행서비스", "primary_archetype": "service_reopening_policy_demand_route", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-10-11", "evidence_available_at_that_date": "Japan reopened visa-free individual travel on 2022-10-11; a listed outbound travel agency had a direct booking-volume route.", "evidence_source": "public policy/travel reopening news family; exact URL in Source Notes; stock-web row verified", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["financial_visibility_watch_only", "unknown_or_not_supported_confirmed_revision"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039130/2022.csv", "profile_path": "atlas/symbol_profiles/039/039130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-10-11", "entry_price": 50600, "MFE_30D_pct": 7.51, "MFE_90D_pct": 29.45, "MFE_180D_pct": 31.82, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.82, "MAE_90D_pct": -6.82, "MAE_180D_pct": -6.82, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-02", "peak_price": 66700, "drawdown_after_peak_pct": -14.47, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_direct_route_with_contained_MAE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14C31_039130_JAPAN_REOPENING_DIRECT_BOOKING_2022-10-11_C50600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L14C31_039130_T_4B_20230302", "case_id": "R12L14C31_039130_JAPAN_REOPENING_DIRECT_BOOKING", "symbol": "039130", "company_name": "하나투어", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS", "sector": "농업·생활서비스·기타 / 관광·카지노·여행서비스", "primary_archetype": "service_reopening_policy_demand_route", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-03-02", "evidence_available_at_that_date": "By early March 2023 price had consumed most reopening upside while no durable revision bridge was yet established.", "evidence_source": "public policy/travel reopening news family; exact URL in Source Notes; stock-web row verified", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039130/2023.csv", "profile_path": "atlas/symbol_profiles/039/039130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-02", "entry_price": 65100, "MFE_30D_pct": 2.46, "MFE_90D_pct": 2.46, "MFE_180D_pct": 2.46, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.52, "MAE_90D_pct": -11.52, "MAE_180D_pct": -11.52, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-02", "peak_price": 66700, "drawdown_after_peak_pct": -14.47, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.901, "four_b_full_window_peak_proximity": 0.901, "four_b_timing_verdict": "price_only_local_4B_requires_non_price_confirmation", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14C31_039130_JAPAN_REOPENING_DIRECT_BOOKING_2023-03-02_C65100", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L14C31_114090_T_STAGE2_20230810", "case_id": "R12L14C31_114090_CHINA_GROUP_TOUR_CASINO_FALSE_POSITIVE", "symbol": "114090", "company_name": "GKL", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS", "sector": "농업·생활서비스·기타 / 관광·카지노·여행서비스", "primary_archetype": "service_reopening_policy_demand_route", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-08-10", "evidence_available_at_that_date": "China resumed outbound group-tour approvals to South Korea in August 2023; casino/inbound service names gapped on policy optionality.", "evidence_source": "public policy/travel reopening news family; exact URL in Source Notes; stock-web row verified", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["unknown_or_not_supported_repeat_order_or_conversion", "unknown_or_not_supported_financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/114/114090/2023.csv", "profile_path": "atlas/symbol_profiles/114/114090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-08-10", "entry_price": 15900, "MFE_30D_pct": 13.65, "MFE_90D_pct": 13.65, "MFE_180D_pct": 13.65, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.11, "MAE_90D_pct": -17.92, "MAE_180D_pct": -24.84, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-12", "peak_price": 18070, "drawdown_after_peak_pct": -33.87, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "headline_policy_gap_faded_with_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14C31_114090_CHINA_GROUP_TOUR_CASINO_FALSE_POSITIVE_2023-08-10_C15900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L14C31_114090_T_4B_20230911", "case_id": "R12L14C31_114090_CHINA_GROUP_TOUR_CASINO_FALSE_POSITIVE", "symbol": "114090", "company_name": "GKL", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS", "sector": "농업·생활서비스·기타 / 관광·카지노·여행서비스", "primary_archetype": "service_reopening_policy_demand_route", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-09-11", "evidence_available_at_that_date": "The policy headline had already repriced into the local high before revenue conversion evidence arrived.", "evidence_source": "public policy/travel reopening news family; exact URL in Source Notes; stock-web row verified", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/114/114090/2023.csv", "profile_path": "atlas/symbol_profiles/114/114090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-09-11", "entry_price": 17690, "MFE_30D_pct": 2.15, "MFE_90D_pct": 2.15, "MFE_180D_pct": 2.15, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -26.23, "MAE_90D_pct": -32.45, "MAE_180D_pct": -32.45, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-12", "peak_price": 18070, "drawdown_after_peak_pct": -33.87, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.825, "four_b_full_window_peak_proximity": 0.825, "four_b_timing_verdict": "good_local_4B_but_price_only_not_full_stage_exit", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14C31_114090_CHINA_GROUP_TOUR_CASINO_FALSE_POSITIVE_2023-09-11_C17690", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L14C31_034230_T_STAGE2_20230810", "case_id": "R12L14C31_034230_CHINA_GROUP_TOUR_CASINO_EVENT_FADE", "symbol": "034230", "company_name": "파라다이스", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS", "sector": "농업·생활서비스·기타 / 관광·카지노·여행서비스", "primary_archetype": "service_reopening_policy_demand_route", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-08-10", "evidence_available_at_that_date": "China group-tour resumption was public and immediately visible in casino/travel-service price action, but direct revenue confirmation was not yet available.", "evidence_source": "public policy/travel reopening news family; exact URL in Source Notes; stock-web row verified", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["unknown_or_not_supported_financial_visibility", "unknown_or_not_supported_durable_customer_confirmation"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034230/2023.csv", "profile_path": "atlas/symbol_profiles/034/034230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-08-10", "entry_price": 17070, "MFE_30D_pct": 8.67, "MFE_90D_pct": 8.67, "MFE_180D_pct": 8.67, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.08, "MAE_90D_pct": -22.91, "MAE_180D_pct": -28.47, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-14", "peak_price": 18550, "drawdown_after_peak_pct": -34.18, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "opening_gap_low_residual_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14C31_034230_CHINA_GROUP_TOUR_CASINO_EVENT_FADE_2023-08-10_C17070", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L14C31_034230_T_4B_20230814", "case_id": "R12L14C31_034230_CHINA_GROUP_TOUR_CASINO_EVENT_FADE", "symbol": "034230", "company_name": "파라다이스", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS", "sector": "농업·생활서비스·기타 / 관광·카지노·여행서비스", "primary_archetype": "service_reopening_policy_demand_route", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-08-14", "evidence_available_at_that_date": "Three sessions after the policy headline, the local high was price-only and lacked non-price conversion evidence.", "evidence_source": "public policy/travel reopening news family; exact URL in Source Notes; stock-web row verified", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034230/2023.csv", "profile_path": "atlas/symbol_profiles/034/034230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-08-14", "entry_price": 18010, "MFE_30D_pct": 3.0, "MFE_90D_pct": 3.0, "MFE_180D_pct": 3.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -26.93, "MAE_90D_pct": -32.2, "MAE_180D_pct": -32.2, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-14", "peak_price": 18550, "drawdown_after_peak_pct": -34.18, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.635, "four_b_full_window_peak_proximity": 0.635, "four_b_timing_verdict": "price_only_local_4B_too_early_without_non_price_evidence", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14C31_034230_CHINA_GROUP_TOUR_CASINO_EVENT_FADE_2023-08-14_C18010", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L14C31_035250_T_STAGE2_20220418", "case_id": "R12L14C31_035250_DOMESTIC_REOPENING_CAPACITY_GUARD", "symbol": "035250", "company_name": "강원랜드", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "SERVICE_TOURISM_REOPENING_POLICY_ROUTE_DIRECTNESS", "sector": "농업·생활서비스·기타 / 관광·카지노·여행서비스", "primary_archetype": "service_reopening_policy_demand_route", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Watch", "trigger_date": "2022-04-18", "evidence_available_at_that_date": "South Korea removed most social-distancing rules on 2022-04-18; casino footfall optionality existed, but domestic casino capacity/regulatory route was constrained.", "evidence_source": "public policy/travel reopening news family; exact URL in Source Notes; stock-web row verified", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["unknown_or_not_supported_confirmed_revision", "unknown_or_not_supported_margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035250/2022.csv", "profile_path": "atlas/symbol_profiles/035/035250.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-04-18", "entry_price": 27250, "MFE_30D_pct": 4.22, "MFE_90D_pct": 5.14, "MFE_180D_pct": 5.14, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.17, "MAE_90D_pct": -14.13, "MAE_180D_pct": -17.06, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-06-10", "peak_price": 28650, "drawdown_after_peak_pct": -21.12, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "domestic_reopening_weak_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L14C31_035250_DOMESTIC_REOPENING_CAPACITY_GUARD_2022-04-18_C27250", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L14C31_039130_JAPAN_REOPENING_DIRECT_BOOKING", "trigger_id": "R12L14C31_039130_T_STAGE2_20221011", "symbol": "039130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 4, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 14, "policy_or_regulatory_score": 20, "valuation_repricing_score": 4, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "service_reopening_direct_booking_route_score": 8, "inbound_group_tour_lag_penalty": 0, "captive_capacity_regulation_guard": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable", "changed_components": ["service_reopening_direct_booking_route_score", "inbound_group_tour_lag_penalty", "captive_capacity_regulation_guard", "execution_risk_score"], "component_delta_explanation": "Service reopening headlines are promoted only when the route is direct booking/volume conversion; inbound group-tour and captive-capacity cases receive route-lag/constraint guards until non-price revenue evidence appears.", "MFE_90D_pct": 29.45, "MAE_90D_pct": -6.82, "score_return_alignment_label": "positive_direct_route", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L14C31_114090_CHINA_GROUP_TOUR_CASINO_FALSE_POSITIVE", "trigger_id": "R12L14C31_114090_T_STAGE2_20230810", "symbol": "114090", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 16, "customer_quality_score": 6, "policy_or_regulatory_score": 20, "valuation_repricing_score": 8, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow/False-positive risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 4, "policy_or_regulatory_score": 13, "valuation_repricing_score": 2, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "service_reopening_direct_booking_route_score": 0, "inbound_group_tour_lag_penalty": -8, "captive_capacity_regulation_guard": 0}, "weighted_score_after": 62, "stage_label_after": "Stage2-Watch/Blocked", "changed_components": ["service_reopening_direct_booking_route_score", "inbound_group_tour_lag_penalty", "captive_capacity_regulation_guard", "execution_risk_score"], "component_delta_explanation": "Service reopening headlines are promoted only when the route is direct booking/volume conversion; inbound group-tour and captive-capacity cases receive route-lag/constraint guards until non-price revenue evidence appears.", "MFE_90D_pct": 13.65, "MAE_90D_pct": -17.92, "score_return_alignment_label": "counterexample_guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L14C31_034230_CHINA_GROUP_TOUR_CASINO_EVENT_FADE", "trigger_id": "R12L14C31_034230_T_STAGE2_20230810", "symbol": "034230", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 14, "customer_quality_score": 6, "policy_or_regulatory_score": 20, "valuation_repricing_score": 8, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow/False-positive risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 4, "policy_or_regulatory_score": 13, "valuation_repricing_score": 2, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "service_reopening_direct_booking_route_score": 0, "inbound_group_tour_lag_penalty": -8, "captive_capacity_regulation_guard": 0}, "weighted_score_after": 61, "stage_label_after": "Stage2-Watch/Blocked", "changed_components": ["service_reopening_direct_booking_route_score", "inbound_group_tour_lag_penalty", "captive_capacity_regulation_guard", "execution_risk_score"], "component_delta_explanation": "Service reopening headlines are promoted only when the route is direct booking/volume conversion; inbound group-tour and captive-capacity cases receive route-lag/constraint guards until non-price revenue evidence appears.", "MFE_90D_pct": 8.67, "MAE_90D_pct": -22.91, "score_return_alignment_label": "counterexample_guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L14C31_035250_DOMESTIC_REOPENING_CAPACITY_GUARD", "trigger_id": "R12L14C31_035250_T_STAGE2_20220418", "symbol": "035250", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 4, "policy_or_regulatory_score": 18, "valuation_repricing_score": 0, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 73, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 2, "policy_or_regulatory_score": 10, "valuation_repricing_score": 0, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "service_reopening_direct_booking_route_score": 0, "inbound_group_tour_lag_penalty": 0, "captive_capacity_regulation_guard": -8}, "weighted_score_after": 56, "stage_label_after": "Stage2-Watch/Blocked", "changed_components": ["service_reopening_direct_booking_route_score", "inbound_group_tour_lag_penalty", "captive_capacity_regulation_guard", "execution_risk_score"], "component_delta_explanation": "Service reopening headlines are promoted only when the route is direct booking/volume conversion; inbound group-tour and captive-capacity cases receive route-lag/constraint guards until non-price revenue evidence appears.", "MFE_90D_pct": 5.14, "MAE_90D_pct": -14.13, "score_return_alignment_label": "counterexample_guard_improves_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R12", "loop": "14", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["indirect_policy_headline_false_positive", "inbound_group_tour_revenue_lag", "captive_capacity_regulation_guard", "price_only_event_peak_4B_late"], "loop_contribution_label": "sector_specific_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R12
completed_loop = 14
next_round = R13
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web checked files:

```text
Songdaiki/stock-web atlas/manifest.json
Songdaiki/stock-web atlas/schema.json
Songdaiki/stock-web atlas/universe/all_symbols.csv
Songdaiki/stock-web atlas/symbol_profiles/039/039130.json
Songdaiki/stock-web atlas/symbol_profiles/114/114090.json
Songdaiki/stock-web atlas/symbol_profiles/034/034230.json
Songdaiki/stock-web atlas/symbol_profiles/035/035250.json
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/039/039130/2022.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/039/039130/2023.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/114/114090/2023.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/114/114090/2024.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/034/034230/2023.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/034/034230/2024.csv
Songdaiki/stock-web atlas/ohlcv_tradable_by_symbol_year/035/035250/2022.csv
```

External event references used for narrative context:

```text
- Japan travel reopening / visa-waiver resumption on 2022-10-11: Axios, 2022-09-22; also Japan government travel-reopening news family.
- Korea social-distancing removal / endemic transition in April 2022: Korea public health/COVID policy news family and public chronology.
- China group-tour resumption to Korea in August 2023: China outbound group-tour approval / Korea tourism news family; exact URL enrichment recommended before production ingestion.
```

Caveat: price calculations use raw/unadjusted marcap OHLC. This MD is a research artifact, not a production scoring patch or investment recommendation.
