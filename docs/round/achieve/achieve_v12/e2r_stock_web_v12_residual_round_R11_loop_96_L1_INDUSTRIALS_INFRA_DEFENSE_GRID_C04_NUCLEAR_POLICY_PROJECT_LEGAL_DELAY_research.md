# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R11
scheduled_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2_AND_ACTUATOR_POLICY_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_legal_delay_watch | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R11_loop_96_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
```

This file is the corrected final output for this execution. The scheduler state after R10 loop 96 is R11 / loop 96. R11 allows the L10 policy/event route or the L1 policy/defense-linked route. This run uses the L1 nuclear-policy route and fills C04 nuclear policy/project/legal-delay behavior rather than repeating the immediately preceding R11 loop 95 C03 defense-export file or R11 loop 94 C31 policy-event file.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R11
scheduled_loop = 96
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
round_sector_consistency = pass
computed_next_round = R12
computed_next_loop = 96
```

C04 is a nuclear-policy-to-project bridge archetype. The policy headline is the reactor start button; the actual current must pass through project pipeline, customer order, permitting/legal visibility, delivery schedule, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY = 12 rows / 7 symbols / good-bad Stage2 5-3 / 4B-4C 1-0
top covered symbols include 011700(4), 083650(3), 006910(1), 034020(1), 042370(1), 046120(1)
previous R11 loop-89 C03 symbols avoided: 064350, 010820, 099320
previous R11 loop-91 C03 symbols avoided: 012450, 214430, 013810
previous R11 loop-94 C31 symbols avoided: 034020, 126880, 119850
previous R11 loop-95 C03 symbols avoided: 272210, 211270, 451760
previous R10 loop-96 C30 symbols avoided: 010960, 017000, 091590
```

Selected rows avoid hard duplicates and top repeated C04 symbols:

```text
052690 / Stage2-Actionable / 2024-04-22
105840 / Stage2-Actionable / 2024-01-15
019990 / Stage4B / 2024-01-15
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 052690 | atlas/symbol_profiles/052/052690.json | no corporate-action candidate |
| 105840 | atlas/symbol_profiles/105/105840.json | selected 2024 window clean after old 2012 CA candidates |
| 019990 | atlas/symbol_profiles/019/019990.json | selected 2024 window clean after old 2016 CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R11L96_C04_KEPCOE_C_2024_NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_POSITIVE | 052690 | 2024-04-22 | yes | 180 | yes | yes | true |
| R11L96_C04_WOOJIN_2024_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2 | 105840 | 2024-01-15 | yes | 180 | yes | yes | true |
| R11L96_C04_ENERTORK_2024_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP_4B | 019990 | 2024-01-15 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE | Positive Stage2 requires project pipeline, EPC/design scope, customer order path, permitting/legal visibility, margin and revision bridge. |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_INSTRUMENTATION_FALSE_STAGE2 | Instrumentation/component policy watch without project/order/margin bridge can become false Stage2. |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_ACTUATOR_EVENT_CAP_4B | Actuator/valve component policy premium should route to 4B when project award and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R11L96_C04_KEPCOE_C_2024_NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_POSITIVE | 052690 | 한전기술 | positive | Nuclear engineering/project bridge produced strong MFE with shallow early MAE. |
| R11L96_C04_WOOJIN_2024_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2 | 105840 | 우진 | counterexample | Nuclear instrumentation policy spike had low MFE and later drawdown without project/order bridge. |
| R11L96_C04_ENERTORK_2024_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP_4B | 019990 | 에너토크 | counterexample / 4B | Nuclear actuator policy premium capped near January spike and then de-rated. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| KEPCO E&C nuclear engineering project bridge | historical public/report proxy | true | true | shadow-only positive |
| Woojin nuclear instrumentation false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Enertork nuclear actuator event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 052690 | atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv | atlas/symbol_profiles/052/052690.json |
| 105840 | atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv | atlas/symbol_profiles/105/105840.json |
| 019990 | atlas/ohlcv_tradable_by_symbol_year/019/019990/2024.csv | atlas/symbol_profiles/019/019990.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R11L96_C04_KEPCOE_C_2024_STAGE2_ACTIONABLE_NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE | 052690 | Stage2-Actionable | 2024-04-22 | 59200 | positive | nuclear engineering policy/project bridge worked |
| R11L96_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENTATION_POLICY_WATCH | 105840 | Stage2-Actionable | 2024-01-15 | 10050 | counterexample | nuclear instrumentation policy false Stage2 |
| R11L96_C04_ENERTORK_2024_STAGE4B_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP | 019990 | Stage4B | 2024-01-15 | 7110 | counterexample/4B | nuclear actuator policy event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R11L96_C04_KEPCOE_C_2024_STAGE2_ACTIONABLE_NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE | 59200 | 25.34 | -1.86 | 65.71 | -1.86 | 65.71 | -1.86 | 2024-07-18 | 98100 | -35.37 |
| R11L96_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENTATION_POLICY_WATCH | 10050 | 4.48 | -19.90 | 4.48 | -23.18 | 4.48 | -28.36 | 2024-01-24 | 10500 | -29.90 |
| R11L96_C04_ENERTORK_2024_STAGE4B_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP | 7110 | 2.39 | -12.38 | 2.39 | -20.53 | 2.39 | -24.61 | 2024-01-19 | 7280 | -26.10 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C04 Stage2 needs project pipeline / permit-legal visibility / customer order / delivery / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing nuclear component premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: policy-premium drawdown blocks promotion without project/order bridge |
| hard_4c_thesis_break_routes_to_4c | keep; legal delay remains watch-only in these cases |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether nuclear policy becomes project/order/permitting evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 052690 | good_stage2_with_later_watch | Project bridge produced strong MFE and shallow MAE, but later legal/valuation watch remains necessary. |
| 105840 | bad_stage2 | Policy watch lacked confirmed project/order bridge and gave low MFE with drawdown. |
| 019990 | good_4B | Component policy premium capped early and later de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 105840 nuclear instrumentation false Stage2 | 0.96 | 0.96 | false Stage2 due missing project/order/permitting/margin bridge |
| 019990 nuclear actuator cap | 0.98 | 0.98 | acceptable 4B because project-award/delivery bridge was missing |
| 052690 nuclear engineering project bridge | n/a | n/a | positive Stage2, but later legal-delay/valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = legal_delay_watch_only for all rows
```

No hard 4C candidate is introduced in this R11 loop 96 file. The guardrail is that policy/project legal delay must remain a negative overlay unless the project pipeline, permit and order bridge is confirmed.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 nuclear policy/project cases, Stage2 requires verified project pipeline, EPC/design scope, customer order path, permitting/legal visibility, delivery schedule, margin, or revision bridge. Nuclear policy, SMR, component, instrumentation, actuator, valve, export, project or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
rule = C04 should split true project/permitting/order bridge positives from component-policy false Stage2 and event caps. Event-cap rows are 4B overlay/risk calibration, while legal-delay confirmation should route to 4C only when a hard project thesis break appears.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 24.19 | -15.19 | 0.67 | mixed; C04 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 24.19 | -15.19 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L1 project/permitting/order bridge required | 2 | 35.10 | -12.52 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C04 bridge vs event-cap split | 2 | 35.10 | -12.52 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing nuclear policy/component themes as positive | 1 | 65.71 | -1.86 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 052690 nuclear project bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 65.71 | -1.86 | nuclear_engineering_project_policy_positive |
| 105840 instrumentation false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 4.48 | -23.18 | nuclear_instrumentation_policy_false_stage2 |
| 019990 actuator cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.39 | -20.53 | nuclear_actuator_policy_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2_AND_ACTUATOR_POLICY_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C04 KEPCO E&C nuclear engineering policy/project positive, Woojin nuclear instrumentation false Stage2, and Enertork nuclear actuator policy event-cap 4B while avoiding top repeated C04 and previous R11/R10 loop symbols."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: nuclear_engineering_project_policy_positive, nuclear_instrumentation_policy_false_stage2, nuclear_actuator_policy_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C04 nuclear policy/project/legal-delay bridge vs false Stage2 / event-cap split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,configured,C04_requires_project_pipeline_permit_legal_visibility_customer_order_margin_revision_bridge,0,"C04 Stage2 should require project pipeline, EPC/design scope, customer order path, permitting/legal visibility, delivery schedule, margin, or revision bridge, not nuclear-policy label alone","KEPCO E&C positive worked; Woojin and Enertork event/watch rows failed positive-stage promotion","R11L96_C04_KEPCOE_C_2024_STAGE2_ACTIONABLE_NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE|R11L96_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENTATION_POLICY_WATCH|R11L96_C04_ENERTORK_2024_STAGE4B_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,configured,cap_bridge_missing_nuclear_component_policy_event_premiums_as_4B_watch,0,"Nuclear instrumentation, actuator and component premiums can peak before project award, delivery and margin bridge is proven","Woojin had low MFE and drawdown after January policy spike; Enertork showed 4B event-cap behavior after January nuclear-policy spike","R11L96_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENTATION_POLICY_WATCH|R11L96_C04_ENERTORK_2024_STAGE4B_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,configured,block_positive_stage_when_nuclear_policy_theme_has_high_or_persistent_MAE_without_project_bridge,0,"High or persistent MAE after bridge-missing C04 entries should block Stage2/Stage3 promotion unless project, permitting/legal and margin evidence survives","Woojin MAE180=-28.36 and Enertork MAE180=-24.61","R11L96_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENTATION_POLICY_WATCH|R11L96_C04_ENERTORK_2024_STAGE4B_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R11L96_C04_KEPCOE_C_2024_NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_POSITIVE", "symbol": "052690", "company_name": "한전기술", "round": "R11", "loop": "96", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2_AND_ACTUATOR_POLICY_EVENT_CAP", "case_type": "structural_success_with_later_nuclear_project_valuation_and_legal_delay_watch", "positive_or_counterexample": "positive", "best_trigger": "R11L96_C04_KEPCOE_C_2024_STAGE2_ACTIONABLE_NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Nuclear engineering / policy project bridge produced strong 30D/90D MFE with controlled early MAE. C04 can work when policy support maps into project pipeline, EPC/design scope, legal/permitting visibility, customer order path, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C04_positive_requires_project_pipeline_permit_legal_visibility_customer_order_margin_revision_bridge_not_nuclear_policy_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R11L96_C04_WOOJIN_2024_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2", "symbol": "105840", "company_name": "우진", "round": "R11", "loop": "96", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2_AND_ACTUATOR_POLICY_EVENT_CAP", "case_type": "failed_rerating_nuclear_instrumentation_policy_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R11L96_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENTATION_POLICY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Nuclear instrumentation / policy watch spiked in January but did not prove durable project order, delivery, permitting or margin-revision bridge. C04 Stage2 should not be awarded on policy heat alone.", "current_profile_verdict": "current_profile_false_positive_if_nuclear_instrumentation_policy_watch_counts_without_project_order_delivery_permit_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2012 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R11L96_C04_ENERTORK_2024_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP_4B", "symbol": "019990", "company_name": "에너토크", "round": "R11", "loop": "96", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2_AND_ACTUATOR_POLICY_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R11L96_C04_ENERTORK_2024_STAGE4B_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Nuclear actuator / valve policy event premium capped near the January spike and then de-rated. C04 should route bridge-missing nuclear-component policy premiums to 4B unless project award, order backlog, delivery, permitting/legal and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_actuator_policy_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2016 corporate-action candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R11L96_C04_KEPCOE_C_2024_STAGE2_ACTIONABLE_NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE", "case_id": "R11L96_C04_KEPCOE_C_2024_NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_POSITIVE", "symbol": "052690", "company_name": "한전기술", "round": "R11", "loop": "96", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2_AND_ACTUATOR_POLICY_EVENT_CAP", "sector": "nuclear_engineering_policy_project_pipeline", "primary_archetype": "project_pipeline_permit_legal_visibility_customer_order_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_legal_delay_watch | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-22", "entry_date": "2024-04-22", "entry_price": 59200.0, "evidence_available_at_that_date": "nuclear engineering/project policy bridge with design/EPC scope, project pipeline, permitting/legal visibility, customer order path and margin/revision proxy after April washout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["project_pipeline_proxy", "EPC_design_scope_proxy", "permitting_legal_visibility_proxy", "customer_order_path_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_nuclear_project_valuation_watch", "legal_delay_recheck"], "stage4c_evidence_fields": ["legal_delay_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv", "profile_path": "atlas/symbol_profiles/052/052690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 25.34, "MFE_90D_pct": 65.71, "MFE_180D_pct": 65.71, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.86, "MAE_90D_pct": -1.86, "MAE_180D_pct": -1.86, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 98100.0, "drawdown_after_peak_pct": -35.37, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_nuclear_project_valuation_and_legal_delay_4B_watch_needed", "four_b_evidence_type": ["project_pipeline_bridge", "permitting_legal_visibility", "valuation_watch"], "four_c_protection_label": "legal_delay_watch_only", "trigger_outcome_label": "good_stage2_nuclear_engineering_policy_project_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R11L96_C04_052690_2024-04-22_59200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L96_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENTATION_POLICY_WATCH", "case_id": "R11L96_C04_WOOJIN_2024_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2", "symbol": "105840", "company_name": "우진", "round": "R11", "loop": "96", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2_AND_ACTUATOR_POLICY_EVENT_CAP", "sector": "nuclear_instrumentation_policy_project_watch", "primary_archetype": "nuclear_instrumentation_watch_without_project_order_permit_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_legal_delay_watch | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-15", "entry_date": "2024-01-15", "entry_price": 10050.0, "evidence_available_at_that_date": "nuclear instrumentation / policy event watch without confirmed project award, customer order, delivery schedule, permitting/legal visibility or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["nuclear_instrumentation_policy_watch", "project_theme_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["brief_MFE_then_MAE", "project_order_margin_bridge_missing"], "stage4c_evidence_fields": ["legal_delay_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv", "profile_path": "atlas/symbol_profiles/105/105840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.48, "MFE_90D_pct": 4.48, "MFE_180D_pct": 4.48, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -19.9, "MAE_90D_pct": -23.18, "MAE_180D_pct": -28.36, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-24", "peak_price": 10500.0, "drawdown_after_peak_pct": -29.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "nuclear_instrumentation_policy_watch_was_false_stage2_due_missing_project_order_permit_margin_bridge", "four_b_evidence_type": ["nuclear_policy_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "legal_delay_watch_only", "trigger_outcome_label": "bad_stage2_nuclear_instrumentation_policy_watch_without_project_order_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_nuclear_instrumentation_policy_watch_counts_without_project_order_delivery_permit_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2012_CA", "same_entry_group_id": "R11L96_C04_105840_2024-01-15_10050", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L96_C04_ENERTORK_2024_STAGE4B_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP", "case_id": "R11L96_C04_ENERTORK_2024_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP_4B", "symbol": "019990", "company_name": "에너토크", "round": "R11", "loop": "96", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2_AND_ACTUATOR_POLICY_EVENT_CAP", "sector": "nuclear_actuator_valve_policy_event_premium", "primary_archetype": "nuclear_actuator_policy_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_legal_delay_watch | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-15", "entry_date": "2024-01-15", "entry_price": 7110.0, "evidence_available_at_that_date": "nuclear actuator / valve policy event premium after January nuclear-policy spike without confirmed project award, delivery backlog or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["nuclear_actuator_policy_event", "component_policy_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "MAE90", "project_order_margin_bridge_recheck"], "stage4c_evidence_fields": ["legal_delay_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/019/019990/2024.csv", "profile_path": "atlas/symbol_profiles/019/019990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.39, "MFE_90D_pct": 2.39, "MFE_180D_pct": 2.39, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -12.38, "MAE_90D_pct": -20.53, "MAE_180D_pct": -24.61, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-19", "peak_price": 7280.0, "drawdown_after_peak_pct": -26.1, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "acceptable_4B_timing_nuclear_actuator_policy_event_cap_due_missing_project_award_delivery_margin_bridge", "four_b_evidence_type": ["nuclear_actuator_policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "legal_delay_watch_only", "trigger_outcome_label": "event_cap_4B_success_nuclear_actuator_policy_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_actuator_policy_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2016_CA", "same_entry_group_id": "R11L96_C04_019990_2024-01-15_7110", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L96_C04_KEPCOE_C_2024_NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_POSITIVE", "trigger_id": "R11L96_C04_KEPCOE_C_2024_STAGE2_ACTIONABLE_NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE", "symbol": "052690", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 60, "customer_quality_score": 45, "policy_or_regulatory_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 50, "backlog_visibility_score": 55, "margin_bridge_score": 50, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 55, "policy_or_regulatory_score": 70, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "nuclear_engineering_project_policy_positive", "MFE_90D_pct": 65.71, "MAE_90D_pct": -1.86, "score_return_alignment_label": "nuclear_engineering_project_policy_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L96_C04_WOOJIN_2024_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2", "trigger_id": "R11L96_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENTATION_POLICY_WATCH", "symbol": "105840", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 65, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "nuclear_instrumentation_policy_false_stage2", "MFE_90D_pct": 4.48, "MAE_90D_pct": -23.18, "score_return_alignment_label": "nuclear_instrumentation_policy_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_nuclear_instrumentation_policy_watch_counts_without_project_order_delivery_permit_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L96_C04_ENERTORK_2024_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP_4B", "trigger_id": "R11L96_C04_ENERTORK_2024_STAGE4B_NUCLEAR_ACTUATOR_POLICY_EVENT_CAP", "symbol": "019990", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 65, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "nuclear_actuator_policy_event_cap_4B_guard", "MFE_90D_pct": 2.39, "MAE_90D_pct": -20.53, "score_return_alignment_label": "nuclear_actuator_policy_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_actuator_policy_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": "96", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_ENGINEERING_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSTRUMENTATION_POLICY_FALSE_STAGE2_AND_ACTUATOR_POLICY_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_thesis_break_routes_to_4c", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["nuclear_engineering_project_policy_positive", "nuclear_instrumentation_policy_false_stage2", "nuclear_actuator_policy_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C04 rows need explicit project pipeline, EPC/design scope, customer order path, permitting/legal visibility, delivery schedule, margin or revision bridge before positive promotion.
- In C04, bridge-missing nuclear policy/component event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C04 nuclear policy/project rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R11
completed_loop = 96
next_round = R12
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
