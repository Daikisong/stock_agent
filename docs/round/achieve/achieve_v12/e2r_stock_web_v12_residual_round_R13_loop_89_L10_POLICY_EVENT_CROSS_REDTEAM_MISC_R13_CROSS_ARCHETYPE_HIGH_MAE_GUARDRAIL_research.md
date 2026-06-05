# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R13
scheduled_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id = BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89
loop_objective = cross_archetype_redteam | high_MAE_guardrail | 4B_non_price_requirement_stress_test | stage2_false_positive_review | no_new_case_reuse_only
output_file = e2r_stock_web_v12_residual_round_R13_loop_89_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
```

R13 is a cross-archetype checkpoint, not a new sector round. This file reviews 8 reused loop-89 rows from R9~R12.

```text
is_new_independent_case = false for every row
independent_evidence_weight = 0.0 for every row
do_not_count_as_new_case = true for every row
dedupe_for_aggregate = false for every row
aggregate_group_role = r13_review_only
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes stress-tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R13
scheduled_loop = 89
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_sector_consistency = pass
computed_next_round = R1
computed_next_loop = 90
```

R13 scope is cross-archetype high-MAE and bridge-missing review. The reviewed rows span:

```text
C13 battery utilization / separator
C30 construction PF / political construction
C03 defense export / drone-space defense
C31 policy subsidy / education policy
```

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key is respected:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This file is not claiming new independent cases. It reuses prior loop-89 research rows to test whether the same failure pattern repeats across canonical archetypes. Because the rows are reused, every case/trigger row is explicitly marked as review-only.

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
| tradable_row_count | 14354401 |
| symbol_count | 5414 |

## 5. Historical Eligibility Gate

| review case | symbol | entry_date | forward 180D | OHLC valid | CA clean | calibration_usable | new independent? |
|---|---|---:|---:|---|---|---|---|
| C13 Shinheung battery parts false Stage2 | 243840 | 2024-06-26 | 180 | yes | post-2024-04-26-CA | true | false |
| C13 WCP separator event cap | 393890 | 2024-02-22 | 180 | yes | yes | true | false |
| C30 Dongbu construction beta false Stage2 | 005960 | 2024-02-01 | 180 | yes | yes | true | false |
| C30 Sambu political construction event cap | 001470 | 2024-03-15 | 180 | yes | yes | true | false |
| C03 Firstec drone-defense false Stage2 | 010820 | 2024-01-17 | 180 | yes | yes | true | false |
| C03 Satrec space-defense event cap | 099320 | 2024-07-01 | 180 | yes | post-2024-01-08-CA | true | false |
| C31 Visang education policy false Stage2 | 100220 | 2024-02-20 | 180 | yes | yes | true | false |
| C31 IB Kimyoung digital education event cap | 339950 | 2024-02-22 | 180 | yes | post-2020-SPAC-CA | true | false |

## 6. Canonical Archetype Compression Map

| R13 review bucket | source canonical | compression rule |
|---|---|---|
| bridge_missing_false_stage2 | C13/C30/C03/C31 | Stage2-like signal needs a durable non-price bridge before positive promotion. |
| high_MAE_guardrail | C13/C30/C03/C31 | High MAE after entry overrides temporary MFE unless non-price bridge is durable. |
| event_premium_cap_4B | C13/C30/C03/C31 | Theme, policy, political, space, separator, or education premium near cap routes to 4B/watch. |
| conversion_required | C13/C30/C03/C31 | Each canonical has its own conversion bridge: utilization/margin, PF/cashflow, export/backlog, policy-to-cashflow. |

## 7. Case Selection Summary

| source round | original canonical | symbol | trigger_type | entry_date | entry_price | R13 label |
|---|---|---|---|---:|---:|---|
| R9 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 243840 | Stage2-Actionable | 2024-06-26 | 9640.0 | stage2_false_positive_high_MAE |
| R9 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 393890 | Stage4B | 2024-02-22 | 47100.0 | event_cap_4B_high_MAE |
| R10 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 005960 | Stage2-Actionable | 2024-02-01 | 5430.0 | stage2_false_positive_low_MFE |
| R10 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 001470 | Stage4B | 2024-03-15 | 2690.0 | event_cap_4B_severe_MAE |
| R11 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 010820 | Stage2-Actionable | 2024-01-17 | 3765.0 | stage2_false_positive_bridge_missing |
| R11 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 099320 | Stage4B | 2024-07-01 | 54800.0 | event_cap_4B_high_MAE |
| R12 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 100220 | Stage2-Actionable | 2024-02-20 | 7000.0 | stage2_false_positive_high_MAE |
| R12 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 339950 | Stage4B | 2024-02-22 | 2665.0 | event_cap_4B_high_MAE |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 0
counterexample_count = 8
4B_case_count = 4
4C_case_count = 0
new_independent_case_count = 0
reused_case_count = 8
```

R13 intentionally contains no new sector positive case.

## 9. Evidence Source Map

| source round | symbol | evidence status | evidence_url_pending | source_proxy_only | R13 usage |
|---|---|---|---|---|---|
| R9 | 243840 | prior v12 source proxy | true | true | high-MAE false Stage2 review |
| R9 | 393890 | prior v12 source proxy | true | true | separator event-cap review |
| R10 | 005960 | prior v12 source proxy | true | true | low-MFE false Stage2 review |
| R10 | 001470 | prior v12 source proxy | true | true | severe-MAE event-cap review |
| R11 | 010820 | prior v12 source proxy | true | true | defense theme false Stage2 review |
| R11 | 099320 | prior v12 source proxy | true | true | space-defense event-cap review |
| R12 | 100220 | prior v12 source proxy | true | true | education policy false Stage2 review |
| R12 | 339950 | prior v12 source proxy | true | true | digital education event-cap review |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 243840 | atlas/ohlcv_tradable_by_symbol_year/243/243840/2024.csv | atlas/symbol_profiles/243/243840.json |
| 393890 | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv | atlas/symbol_profiles/393/393890.json |
| 005960 | atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv | atlas/symbol_profiles/005/005960.json |
| 001470 | atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv | atlas/symbol_profiles/001/001470.json |
| 010820 | atlas/ohlcv_tradable_by_symbol_year/010/010820/2024.csv | atlas/symbol_profiles/010/010820.json |
| 099320 | atlas/ohlcv_tradable_by_symbol_year/099/099320/2024.csv | atlas/symbol_profiles/099/099320.json |
| 100220 | atlas/ohlcv_tradable_by_symbol_year/100/100220/2024.csv | atlas/symbol_profiles/100/100220.json |
| 339950 | atlas/ohlcv_tradable_by_symbol_year/339/339950/2024.csv | atlas/symbol_profiles/339/339950.json |

## 11. Trigger-Level OHLC Backtest Tables

| symbol | original canonical | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 243840 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 9640.0 | 8.61 | -20.54 | 8.61 | -33.82 | 8.61 | -33.82 | 2024-06-26 | 10470.0 | -39.06 |
| 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 47100.0 | 4.88 | -27.07 | 4.88 | -36.41 | 4.88 | -43.52 | 2024-02-22 | 49400.0 | -48.18 |
| 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 5430.0 | 1.29 | -6.08 | 1.29 | -11.79 | 1.29 | -23.11 | 2024-02-19 | 5500.0 | -24.09 |
| 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 2690.0 | 6.51 | -53.72 | 6.51 | -53.72 | 6.51 | -53.72 | 2024-03-15 | 2865.0 | -56.54 |
| 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 3765.0 | 5.98 | -15.94 | 5.98 | -15.94 | 5.98 | -32.14 | 2024-01-17 | 3990.0 | -36.34 |
| 099320 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 54800.0 | 6.75 | -13.5 | 6.75 | -42.34 | 6.75 | -42.34 | 2024-07-01 | 58500.0 | -45.98 |
| 100220 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 7000.0 | 20.29 | -30.71 | 20.29 | -35.71 | 20.29 | -43.0 | 2024-02-21 | 8420.0 | -52.61 |
| 339950 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 2665.0 | 11.26 | -26.49 | 11.26 | -32.16 | 11.26 | -44.47 | 2024-02-26 | 2965.0 | -50.08 |

```text
avg_MFE_90D_pct = 8.2
avg_MAE_90D_pct = -32.74
avg_MFE_180D_pct = 8.2
avg_MAE_180D_pct = -39.52
stage2_false_positive_review_count = 4
event_cap_review_count = 4
high_MAE_review_count = 7 / 8
```

## 12. Current Calibrated Profile Stress Test

| axis | R13 verdict |
|---|---|
| stage2_required_bridge | existing_axis_strengthened: Stage2-like signals require durable non-price bridge before positive promotion. |
| local_4b_watch_guard | existing_axis_strengthened: event premium / theme spike rows should route to 4B/watch near cap. |
| high_MAE_guardrail | existing_axis_strengthened: high MAE blocks promotion unless verified bridge survives the drawdown. |
| full_4b_requires_non_price_evidence | existing_axis_kept. |
| price_only_blowoff_blocks_positive_stage | existing_axis_kept. |
| hard_4c_thesis_break_routes_to_4c | existing_axis_kept; no hard 4C promoted. |

## 13. Stage2 / Yellow / Green Comparison

R13 does not add new Green cases. It reviews cases where Stage2/Yellow-like interpretation would have been dangerous.

| bucket | reviewed rows | interpretation |
|---|---:|---|
| Stage2 false positive | 4 | MFE was too weak or MAE too large without durable bridge. |
| Stage3/Yellow-like event cap | 4 | Event premium should be treated as 4B/watch rather than structural Green. |
| high-MAE guardrail | 7 | Most reviewed rows had MAE90 <= -25% or MAE180 <= -25%. |
| hard 4C | 0 | No new hard thesis-break route proposed. |

```text
green_lateness_ratio = not_applicable
reason = R13 high-MAE guardrail review, no new Stage3-Green trigger
```

## 14. 4B Local vs Full-window Timing Audit

| symbol | original canonical | 4B local proximity | 4B full-window proximity | timing verdict |
|---|---|---:|---:|---|
| 243840 | C13 | 1.00 | 1.00 | battery parts utilization false Stage2 event cap |
| 393890 | C13 | 1.00 | 1.00 | separator utilization event cap |
| 005960 | C30 | 0.01 | 0.01 | construction beta weak-MFE false Stage2 |
| 001470 | C30 | 1.00 | 1.00 | political construction event cap |
| 010820 | C03 | 1.00 | 1.00 | drone-defense theme false Stage2 event cap |
| 099320 | C03 | 1.00 | 1.00 | space-defense event cap |
| 100220 | C31 | 0.83 | 0.83 | education policy false Stage2 event cap |
| 339950 | C31 | 1.00 | 1.00 | digital education event cap |

## 15. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for all review rows
```

This review supports watch/4B/high-MAE guardrail routing. It does not promote hard 4C.

## 16. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = R13 cross-archetype checkpoint; not a sector-specific rule proposal.
```

## 17. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
rule = Across C13/C30/C03/C31, if a signal is bridge-missing and then produces high MAE or low MFE, block Stage2/Stage3 positive promotion and route to watch/4B unless durable non-price evidence appears.
proposal_status = guardrail_stress_test_only_not_production
```

## 18. Before / After Backtest Comparison

| profile | hypothesis | reviewed triggers | avg_MFE90 | avg_MAE90 | high_MAE_count | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 8 | 8.2 | -32.74 | 7/8 | guardrails needed |
| P0b e2r_2_0_baseline_reference | older baseline | 8 | 8.2 | -32.74 | 7/8 | weaker bridge/cap handling |
| P1 cross_guard_candidate_profile | cross high-MAE guard | 8 | 8.2 | -32.74 | 7/8 | improves rejection alignment |
| P2 archetype_specific_candidate_profile | original canonical bridge requirements | 8 | 8.2 | -32.74 | 7/8 | best explanatory fit |
| P3 counterexample_guard_profile | reject all reviewed positives | 8 | 8.2 | -32.74 | 7/8 | safest but review-only |

## 19. Score-Return Alignment Matrix

| symbol | original canonical | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---|---:|---|---:|---|---:|---:|---|
| 243840 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 66 | Stage2-Actionable | 53 | Stage1/Watch | 8.61 | -33.82 | r13_high_MAE_guardrail_improves_rejection_alignment |
| 393890 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 4.88 | -36.41 | r13_high_MAE_guardrail_improves_rejection_alignment |
| 005960 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 66 | Stage2-Actionable | 53 | Stage1/Watch | 1.29 | -11.79 | r13_high_MAE_guardrail_improves_rejection_alignment |
| 001470 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 6.51 | -53.72 | r13_high_MAE_guardrail_improves_rejection_alignment |
| 010820 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 66 | Stage2-Actionable | 53 | Stage1/Watch | 5.98 | -15.94 | r13_high_MAE_guardrail_improves_rejection_alignment |
| 099320 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 6.75 | -42.34 | r13_high_MAE_guardrail_improves_rejection_alignment |
| 100220 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 66 | Stage2-Actionable | 53 | Stage1/Watch | 20.29 | -35.71 | r13_high_MAE_guardrail_improves_rejection_alignment |
| 339950 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 11.26 | -32.16 | r13_high_MAE_guardrail_improves_rejection_alignment |

## 20. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "positive_case_count": 0, "counterexample_count": 8, "4B_case_count": 4, "4C_case_count": 0, "new_independent_case_count": 0, "reused_case_count": 8, "calibration_usable_trigger_count": 8, "representative_trigger_count": 0, "current_profile_error_count": 8, "sector_rule_candidate": false, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "R13 cross-review validates high-MAE and bridge-missing guardrails across C13/C30/C03/C31 using loop-89 reused rows only."}
```

## 21. Residual Contribution Summary

```text
new_independent_case_count: 0
reused_case_count: 8
reused_case_ids: R9L89_C13_SHINHEUNG_2024_BATTERY_PARTS_CALL_OFF_FALSE_STAGE2, R9L89_C13_WCP_2024_SEPARATOR_CUSTOMER_UTILIZATION_EVENT_CAP_4B, R10L89_C30_DONGBU_2024_CONSTRUCTION_BETA_FALSE_STAGE2, R10L89_C30_SAMBU_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B, R11L89_C03_FIRSTEC_2024_DRONE_DEFENSE_THEME_FALSE_STAGE2, R11L89_C03_SATRECINITIATIVE_2024_SPACE_DEFENSE_THEME_EVENT_CAP_4B, R12L89_C31_VISANG_2024_EDUCATION_POLICY_FALSE_STAGE2, R12L89_C31_IBKIMYOUNG_2024_DIGITAL_EDU_POLICY_EVENT_CAP_4B
new_symbol_count: 0
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 0
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: bridge_missing_false_stage2, event_premium_cap_4B, high_MAE_rejection_guardrail, theme_or_policy_without_conversion
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: R13 review-only rows cannot add independent evidence weight
loop_contribution_label: axis_stress_test_passed
do_not_propose_new_weight_delta: true
```

## 22. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Reused stock-web tradable raw OHLC paths
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- high-MAE and bridge-missing guardrail cross-archetype review
- R13 no-new-case enforcement
```

Non-validation scope:

```text
- No new sector-specific positive case.
- Exact as-of evidence URLs remain pending for reused rows.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 23. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,configured,keep_bridge_required_before_positive_stage,0,"Across C13/C30/C03/C31 loop-89 rows, Stage2-like signals without durable customer/margin/PF/export/policy-to-cashflow bridge were weak-MFE or high-MAE","avg_MFE90=8.2; avg_MAE90=-32.74; high_MAE_count=7/8","R13L89_REVIEW_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION|R13L89_REVIEW_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA|R13L89_REVIEW_C03_FIRSTEC_2024_STAGE2_FALSE_POSITIVE_DRONE_DEFENSE_THEME|R13L89_REVIEW_C31_VISANG_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME",8,0,8,medium,r13_guardrail_review_only,"do_not_count_as_new_case=true; no production delta"
shadow_weight,local_4b_watch_guard,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,configured,keep_event_premium_cap_as_4B_watch,0,"Separator utilization, political construction, space-defense, and digital-education premiums reached local/full-window peaks near trigger and then drew down","Stage4B review rows=4; avg_MFE180=8.2; avg_MAE180=-39.52","R13L89_REVIEW_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP|R13L89_REVIEW_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP|R13L89_REVIEW_C03_SATREC_2024_STAGE4B_SPACE_DEFENSE_THEME_CAP|R13L89_REVIEW_C31_IBKIMYOUNG_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP",8,0,8,medium,r13_guardrail_review_only,"R13 review rows must not add independent case weight"
shadow_weight,high_MAE_guardrail,cross_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,configured,block_positive_stage_when_MAE90_or_MAE180_is_high_without_non_price_bridge,0,"High MAE after bridge-missing theme/event entry should override temporary MFE unless a durable non-price bridge is verified","high_MAE_count=7/8; avg_MAE180=-39.52","R13L89_REVIEW_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION|R13L89_REVIEW_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP|R13L89_REVIEW_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP|R13L89_REVIEW_C03_SATREC_2024_STAGE4B_SPACE_DEFENSE_THEME_CAP|R13L89_REVIEW_C31_VISANG_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME|R13L89_REVIEW_C31_IBKIMYOUNG_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP",8,0,8,medium,r13_guardrail_review_only,"review-only; production scoring unchanged"
```

## 24. Machine-Readable Rows

### 24.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 24.2 case rows

```jsonl
{"row_type": "case", "case_id": "R13L89_REVIEW_C13_SHINHEUNG_2024_BATTERY_PARTS_FALSE_STAGE2", "symbol": "243840", "company_name": "신흥에스이씨", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "case_type": "r13_cross_archetype_high_MAE_guardrail_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L89_REVIEW_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R9 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA / R9L89_C13_SHINHEUNG_2024_BATTERY_PARTS_CALL_OFF_FALSE_STAGE2", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_false_positive_if_battery_parts_utilization_theme_counts_without_customer_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_battery_parts_utilization_theme_counts_without_customer_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "R13 high-MAE cross-review row; reused prior loop-89 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L89_REVIEW_C13_WCP_2024_SEPARATOR_EVENT_CAP_4B", "symbol": "393890", "company_name": "더블유씨피", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "case_type": "r13_cross_archetype_high_MAE_guardrail_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L89_REVIEW_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R9 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA / R9L89_C13_WCP_2024_SEPARATOR_CUSTOMER_UTILIZATION_EVENT_CAP_4B", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_4B_too_late_if_separator_utilization_event_premium_not_capped", "current_profile_verdict": "current_profile_4B_too_late_if_separator_utilization_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "R13 high-MAE cross-review row; reused prior loop-89 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L89_REVIEW_C30_DONGBU_2024_CONSTRUCTION_BETA_FALSE_STAGE2", "symbol": "005960", "company_name": "동부건설", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "case_type": "r13_cross_archetype_high_MAE_guardrail_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L89_REVIEW_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK / R10L89_C30_DONGBU_2024_CONSTRUCTION_BETA_FALSE_STAGE2", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_false_positive_if_construction_beta_counts_without_PF_cashflow_balance_bridge", "current_profile_verdict": "current_profile_false_positive_if_construction_beta_counts_without_PF_cashflow_balance_bridge", "price_source": "Songdaiki/stock-web", "notes": "R13 high-MAE cross-review row; reused prior loop-89 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L89_REVIEW_C30_SAMBU_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B", "symbol": "001470", "company_name": "삼부토건", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "case_type": "r13_cross_archetype_high_MAE_guardrail_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L89_REVIEW_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK / R10L89_C30_SAMBU_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_4B_too_late_if_political_construction_event_premium_not_capped", "current_profile_verdict": "current_profile_4B_too_late_if_political_construction_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "R13 high-MAE cross-review row; reused prior loop-89 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L89_REVIEW_C03_FIRSTEC_2024_DRONE_DEFENSE_FALSE_STAGE2", "symbol": "010820", "company_name": "퍼스텍", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "case_type": "r13_cross_archetype_high_MAE_guardrail_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L89_REVIEW_C03_FIRSTEC_2024_STAGE2_FALSE_POSITIVE_DRONE_DEFENSE_THEME", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R11 / C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG / R11L89_C03_FIRSTEC_2024_DRONE_DEFENSE_THEME_FALSE_STAGE2", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_false_positive_if_drone_defense_theme_counts_without_export_backlog_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_drone_defense_theme_counts_without_export_backlog_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "R13 high-MAE cross-review row; reused prior loop-89 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L89_REVIEW_C03_SATREC_2024_SPACE_DEFENSE_EVENT_CAP_4B", "symbol": "099320", "company_name": "쎄트렉아이", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "case_type": "r13_cross_archetype_high_MAE_guardrail_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L89_REVIEW_C03_SATREC_2024_STAGE4B_SPACE_DEFENSE_THEME_CAP", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R11 / C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG / R11L89_C03_SATRECINITIATIVE_2024_SPACE_DEFENSE_THEME_EVENT_CAP_4B", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_4B_too_late_if_space_defense_theme_premium_not_capped", "current_profile_verdict": "current_profile_4B_too_late_if_space_defense_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "R13 high-MAE cross-review row; reused prior loop-89 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L89_REVIEW_C31_VISANG_2024_EDUCATION_POLICY_FALSE_STAGE2", "symbol": "100220", "company_name": "비상교육", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "case_type": "r13_cross_archetype_high_MAE_guardrail_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L89_REVIEW_C31_VISANG_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / R12L89_C31_VISANG_2024_EDUCATION_POLICY_FALSE_STAGE2", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_or_subsidy_bridge", "current_profile_verdict": "current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_or_subsidy_bridge", "price_source": "Songdaiki/stock-web", "notes": "R13 high-MAE cross-review row; reused prior loop-89 evidence only; not a new independent case."}
{"row_type": "case", "case_id": "R13L89_REVIEW_C31_IBKIMYOUNG_2024_DIGITAL_EDU_EVENT_CAP_4B", "symbol": "339950", "company_name": "아이비김영", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "case_type": "r13_cross_archetype_high_MAE_guardrail_review", "positive_or_counterexample": "counterexample", "best_trigger": "R13L89_REVIEW_C31_IBKIMYOUNG_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "R13 review of R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT / R12L89_C31_IBKIMYOUNG_2024_DIGITAL_EDU_POLICY_EVENT_CAP_4B", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "score_price_alignment": "current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped", "current_profile_verdict": "current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "R13 high-MAE cross-review row; reused prior loop-89 evidence only; not a new independent case."}
```

### 24.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R13L89_REVIEW_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION", "case_id": "R13L89_REVIEW_C13_SHINHEUNG_2024_BATTERY_PARTS_FALSE_STAGE2", "symbol": "243840", "company_name": "신흥에스이씨", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "sector": "cross_archetype_high_MAE_guardrail", "primary_archetype": "bridge_missing_event_premium_high_MAE_review", "original_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "original_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "original_case_id": "R9L89_C13_SHINHEUNG_2024_BATTERY_PARTS_CALL_OFF_FALSE_STAGE2", "original_trigger_id": "R9L89_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION", "loop_objective": "cross_archetype_redteam | high_MAE_guardrail | 4B_non_price_requirement_stress_test | stage2_false_positive_review | no_new_case_reuse_only", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-26", "entry_date": "2024-06-26", "entry_price": 9640.0, "evidence_available_at_that_date": "reused evidence from prior loop-89 v12 sector research; R13 red-team high-MAE guardrail review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["battery_parts_utilization_theme", "customer_demand_recovery_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "deep_MAE90", "customer_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/243/243840/2024.csv", "profile_path": "atlas/symbol_profiles/243/243840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.61, "MFE_90D_pct": 8.61, "MFE_180D_pct": 8.61, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -20.54, "MAE_90D_pct": -33.82, "MAE_180D_pct": -33.82, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 10470.0, "drawdown_after_peak_pct": -39.06, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "battery_parts_utilization_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["price_only", "positioning_overheat", "customer_margin_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_stage2_false_positive_high_MAE", "current_profile_verdict": "current_profile_false_positive_if_battery_parts_utilization_theme_counts_without_customer_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-04-26_CA_window", "same_entry_group_id": "R13L89_REVIEW_243840_2024-06-26_9640.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R9L89_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "stage2_false_positive_high_MAE"}
{"row_type": "trigger", "trigger_id": "R13L89_REVIEW_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP", "case_id": "R13L89_REVIEW_C13_WCP_2024_SEPARATOR_EVENT_CAP_4B", "symbol": "393890", "company_name": "더블유씨피", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "sector": "cross_archetype_high_MAE_guardrail", "primary_archetype": "bridge_missing_event_premium_high_MAE_review", "original_large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "original_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "original_case_id": "R9L89_C13_WCP_2024_SEPARATOR_CUSTOMER_UTILIZATION_EVENT_CAP_4B", "original_trigger_id": "R9L89_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP", "loop_objective": "cross_archetype_redteam | high_MAE_guardrail | 4B_non_price_requirement_stress_test | stage2_false_positive_review | no_new_case_reuse_only", "trigger_type": "Stage4B", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 47100.0, "evidence_available_at_that_date": "reused evidence from prior loop-89 v12 sector research; R13 red-team high-MAE guardrail review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["separator_utilization_premium", "customer_demand_recovery_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.88, "MFE_90D_pct": 4.88, "MFE_180D_pct": 4.88, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.07, "MAE_90D_pct": -36.41, "MAE_180D_pct": -43.52, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-22", "peak_price": 49400.0, "drawdown_after_peak_pct": -48.18, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_separator_customer_utilization_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "customer_utilization_risk"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_event_cap_4B_high_MAE", "current_profile_verdict": "current_profile_4B_too_late_if_separator_utilization_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L89_REVIEW_393890_2024-02-22_47100.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R9L89_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "event_cap_4B_high_MAE"}
{"row_type": "trigger", "trigger_id": "R13L89_REVIEW_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA", "case_id": "R13L89_REVIEW_C30_DONGBU_2024_CONSTRUCTION_BETA_FALSE_STAGE2", "symbol": "005960", "company_name": "동부건설", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "sector": "cross_archetype_high_MAE_guardrail", "primary_archetype": "bridge_missing_event_premium_high_MAE_review", "original_large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "original_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "original_case_id": "R10L89_C30_DONGBU_2024_CONSTRUCTION_BETA_FALSE_STAGE2", "original_trigger_id": "R10L89_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA", "loop_objective": "cross_archetype_redteam | high_MAE_guardrail | 4B_non_price_requirement_stress_test | stage2_false_positive_review | no_new_case_reuse_only", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 5430.0, "evidence_available_at_that_date": "reused evidence from prior loop-89 v12 sector research; R13 red-team high-MAE guardrail review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["construction_beta", "PF_normalization_watch", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "cashflow_balance_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv", "profile_path": "atlas/symbol_profiles/005/005960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.29, "MFE_90D_pct": 1.29, "MFE_180D_pct": 1.29, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.08, "MAE_90D_pct": -11.79, "MAE_180D_pct": -23.11, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 5500.0, "drawdown_after_peak_pct": -24.09, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.01, "four_b_full_window_peak_proximity": 0.01, "four_b_timing_verdict": "construction_beta_watch_was_false_stage2_due_missing_PF_cashflow_bridge", "four_b_evidence_type": ["price_only", "positioning_overheat", "cashflow_balance_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_stage2_false_positive_low_MFE", "current_profile_verdict": "current_profile_false_positive_if_construction_beta_counts_without_PF_cashflow_balance_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L89_REVIEW_005960_2024-02-01_5430.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R10L89_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "stage2_false_positive_low_MFE"}
{"row_type": "trigger", "trigger_id": "R13L89_REVIEW_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP", "case_id": "R13L89_REVIEW_C30_SAMBU_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B", "symbol": "001470", "company_name": "삼부토건", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "sector": "cross_archetype_high_MAE_guardrail", "primary_archetype": "bridge_missing_event_premium_high_MAE_review", "original_large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "original_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "original_case_id": "R10L89_C30_SAMBU_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B", "original_trigger_id": "R10L89_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP", "loop_objective": "cross_archetype_redteam | high_MAE_guardrail | 4B_non_price_requirement_stress_test | stage2_false_positive_review | no_new_case_reuse_only", "trigger_type": "Stage4B", "trigger_date": "2024-03-15", "entry_date": "2024-03-15", "entry_price": 2690.0, "evidence_available_at_that_date": "reused evidence from prior loop-89 v12 sector research; R13 red-team high-MAE guardrail review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["political_construction_theme", "contract_event_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv", "profile_path": "atlas/symbol_profiles/001/001470.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.51, "MFE_90D_pct": 6.51, "MFE_180D_pct": 6.51, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -53.72, "MAE_90D_pct": -53.72, "MAE_180D_pct": -53.72, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-15", "peak_price": 2865.0, "drawdown_after_peak_pct": -56.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_political_construction_event_cap", "four_b_evidence_type": ["event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_event_cap_4B_severe_MAE", "current_profile_verdict": "current_profile_4B_too_late_if_political_construction_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L89_REVIEW_001470_2024-03-15_2690.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R10L89_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "event_cap_4B_severe_MAE"}
{"row_type": "trigger", "trigger_id": "R13L89_REVIEW_C03_FIRSTEC_2024_STAGE2_FALSE_POSITIVE_DRONE_DEFENSE_THEME", "case_id": "R13L89_REVIEW_C03_FIRSTEC_2024_DRONE_DEFENSE_FALSE_STAGE2", "symbol": "010820", "company_name": "퍼스텍", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "sector": "cross_archetype_high_MAE_guardrail", "primary_archetype": "bridge_missing_event_premium_high_MAE_review", "original_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "original_canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "original_case_id": "R11L89_C03_FIRSTEC_2024_DRONE_DEFENSE_THEME_FALSE_STAGE2", "original_trigger_id": "R11L89_C03_FIRSTEC_2024_STAGE2_FALSE_POSITIVE_DRONE_DEFENSE_THEME", "loop_objective": "cross_archetype_redteam | high_MAE_guardrail | 4B_non_price_requirement_stress_test | stage2_false_positive_review | no_new_case_reuse_only", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-17", "entry_date": "2024-01-17", "entry_price": 3765.0, "evidence_available_at_that_date": "reused evidence from prior loop-89 v12 sector research; R13 red-team high-MAE guardrail review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["drone_defense_theme", "relative_strength_spike", "policy_event_premium"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "export_backlog_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010820/2024.csv", "profile_path": "atlas/symbol_profiles/010/010820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.98, "MFE_90D_pct": 5.98, "MFE_180D_pct": 5.98, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.94, "MAE_90D_pct": -15.94, "MAE_180D_pct": -32.14, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-17", "peak_price": 3990.0, "drawdown_after_peak_pct": -36.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "drone_defense_theme_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_stage2_false_positive_bridge_missing", "current_profile_verdict": "current_profile_false_positive_if_drone_defense_theme_counts_without_export_backlog_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L89_REVIEW_010820_2024-01-17_3765.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R11L89_C03_FIRSTEC_2024_STAGE2_FALSE_POSITIVE_DRONE_DEFENSE_THEME", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "stage2_false_positive_bridge_missing"}
{"row_type": "trigger", "trigger_id": "R13L89_REVIEW_C03_SATREC_2024_STAGE4B_SPACE_DEFENSE_THEME_CAP", "case_id": "R13L89_REVIEW_C03_SATREC_2024_SPACE_DEFENSE_EVENT_CAP_4B", "symbol": "099320", "company_name": "쎄트렉아이", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "sector": "cross_archetype_high_MAE_guardrail", "primary_archetype": "bridge_missing_event_premium_high_MAE_review", "original_large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "original_canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "original_case_id": "R11L89_C03_SATRECINITIATIVE_2024_SPACE_DEFENSE_THEME_EVENT_CAP_4B", "original_trigger_id": "R11L89_C03_SATRECINITIATIVE_2024_STAGE4B_SPACE_DEFENSE_THEME_CAP", "loop_objective": "cross_archetype_redteam | high_MAE_guardrail | 4B_non_price_requirement_stress_test | stage2_false_positive_review | no_new_case_reuse_only", "trigger_type": "Stage4B", "trigger_date": "2024-07-01", "entry_date": "2024-07-01", "entry_price": 54800.0, "evidence_available_at_that_date": "reused evidence from prior loop-89 v12 sector research; R13 red-team high-MAE guardrail review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["space_defense_theme", "satellite_policy_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/099/099320/2024.csv", "profile_path": "atlas/symbol_profiles/099/099320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.75, "MFE_90D_pct": 6.75, "MFE_180D_pct": 6.75, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -13.5, "MAE_90D_pct": -42.34, "MAE_180D_pct": -42.34, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-01", "peak_price": 58500.0, "drawdown_after_peak_pct": -45.98, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_space_defense_theme_event_cap", "four_b_evidence_type": ["policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_event_cap_4B_high_MAE", "current_profile_verdict": "current_profile_4B_too_late_if_space_defense_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-01-08_CA_window", "same_entry_group_id": "R13L89_REVIEW_099320_2024-07-01_54800.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R11L89_C03_SATRECINITIATIVE_2024_STAGE4B_SPACE_DEFENSE_THEME_CAP", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "event_cap_4B_high_MAE"}
{"row_type": "trigger", "trigger_id": "R13L89_REVIEW_C31_VISANG_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "case_id": "R13L89_REVIEW_C31_VISANG_2024_EDUCATION_POLICY_FALSE_STAGE2", "symbol": "100220", "company_name": "비상교육", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "sector": "cross_archetype_high_MAE_guardrail", "primary_archetype": "bridge_missing_event_premium_high_MAE_review", "original_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "original_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "original_case_id": "R12L89_C31_VISANG_2024_EDUCATION_POLICY_FALSE_STAGE2", "original_trigger_id": "R12L89_C31_VISANG_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "loop_objective": "cross_archetype_redteam | high_MAE_guardrail | 4B_non_price_requirement_stress_test | stage2_false_positive_review | no_new_case_reuse_only", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-20", "entry_date": "2024-02-20", "entry_price": 7000.0, "evidence_available_at_that_date": "reused evidence from prior loop-89 v12 sector research; R13 red-team high-MAE guardrail review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["education_policy_theme", "digital_textbook_or_curriculum_policy", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["theme_spike", "weak_conversion_bridge", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100220/2024.csv", "profile_path": "atlas/symbol_profiles/100/100220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.29, "MFE_90D_pct": 20.29, "MFE_180D_pct": 20.29, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -30.71, "MAE_90D_pct": -35.71, "MAE_180D_pct": -43.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-21", "peak_price": 8420.0, "drawdown_after_peak_pct": -52.61, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.83, "four_b_full_window_peak_proximity": 0.83, "four_b_timing_verdict": "education_policy_theme_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_stage2_false_positive_high_MAE", "current_profile_verdict": "current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_or_subsidy_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L89_REVIEW_100220_2024-02-20_7000.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R12L89_C31_VISANG_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "stage2_false_positive_high_MAE"}
{"row_type": "trigger", "trigger_id": "R13L89_REVIEW_C31_IBKIMYOUNG_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "case_id": "R13L89_REVIEW_C31_IBKIMYOUNG_2024_DIGITAL_EDU_EVENT_CAP_4B", "symbol": "339950", "company_name": "아이비김영", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "sector": "cross_archetype_high_MAE_guardrail", "primary_archetype": "bridge_missing_event_premium_high_MAE_review", "original_large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "original_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "original_case_id": "R12L89_C31_IBKIMYOUNG_2024_DIGITAL_EDU_POLICY_EVENT_CAP_4B", "original_trigger_id": "R12L89_C31_IBKIMYOUNG_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "loop_objective": "cross_archetype_redteam | high_MAE_guardrail | 4B_non_price_requirement_stress_test | stage2_false_positive_review | no_new_case_reuse_only", "trigger_type": "Stage4B", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 2665.0, "evidence_available_at_that_date": "reused evidence from prior loop-89 v12 sector research; R13 red-team high-MAE guardrail review only", "evidence_source": "prior_v12_research_row_with_stock_web_price_path", "stage2_evidence_fields": ["digital_education_policy_theme", "relative_strength_spike", "policy_event_premium"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/339/339950/2024.csv", "profile_path": "atlas/symbol_profiles/339/339950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.26, "MFE_90D_pct": 11.26, "MFE_180D_pct": 11.26, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -26.49, "MAE_90D_pct": -32.16, "MAE_180D_pct": -44.47, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-26", "peak_price": 2965.0, "drawdown_after_peak_pct": -50.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_digital_education_policy_theme_cap", "four_b_evidence_type": ["policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "r13_review_event_cap_4B_high_MAE", "current_profile_verdict": "current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2020_SPAC_CA", "same_entry_group_id": "R13L89_REVIEW_339950_2024-02-22_2665.0", "dedupe_for_aggregate": false, "aggregate_group_role": "r13_review_only", "is_new_independent_case": false, "reuse_reason": "R13 cross-review of R12L89_C31_IBKIMYOUNG_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true, "r13_review_label": "event_cap_4B_high_MAE"}
```

### 24.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L89_REVIEW_C13_SHINHEUNG_2024_BATTERY_PARTS_FALSE_STAGE2", "trigger_id": "R13L89_REVIEW_C13_SHINHEUNG_2024_STAGE2_FALSE_POSITIVE_BATTERY_PARTS_UTILIZATION", "symbol": "243840", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: bridge-missing theme/event premium with high MAE or low MFE is blocked from positive Stage2/Stage3 promotion.", "MFE_90D_pct": 8.61, "MAE_90D_pct": -33.82, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_rejection_alignment", "current_profile_verdict": "current_profile_false_positive_if_battery_parts_utilization_theme_counts_without_customer_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L89_REVIEW_C13_WCP_2024_SEPARATOR_EVENT_CAP_4B", "trigger_id": "R13L89_REVIEW_C13_WCP_2024_STAGE4B_SEPARATOR_UTILIZATION_CAP", "symbol": "393890", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: bridge-missing theme/event premium with high MAE or low MFE is blocked from positive Stage2/Stage3 promotion.", "MFE_90D_pct": 4.88, "MAE_90D_pct": -36.41, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_rejection_alignment", "current_profile_verdict": "current_profile_4B_too_late_if_separator_utilization_event_premium_not_capped"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L89_REVIEW_C30_DONGBU_2024_CONSTRUCTION_BETA_FALSE_STAGE2", "trigger_id": "R13L89_REVIEW_C30_DONGBU_2024_STAGE2_FALSE_POSITIVE_CONSTRUCTION_BETA", "symbol": "005960", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: bridge-missing theme/event premium with high MAE or low MFE is blocked from positive Stage2/Stage3 promotion.", "MFE_90D_pct": 1.29, "MAE_90D_pct": -11.79, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_rejection_alignment", "current_profile_verdict": "current_profile_false_positive_if_construction_beta_counts_without_PF_cashflow_balance_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L89_REVIEW_C30_SAMBU_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B", "trigger_id": "R13L89_REVIEW_C30_SAMBU_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP", "symbol": "001470", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: bridge-missing theme/event premium with high MAE or low MFE is blocked from positive Stage2/Stage3 promotion.", "MFE_90D_pct": 6.51, "MAE_90D_pct": -53.72, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_rejection_alignment", "current_profile_verdict": "current_profile_4B_too_late_if_political_construction_event_premium_not_capped"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L89_REVIEW_C03_FIRSTEC_2024_DRONE_DEFENSE_FALSE_STAGE2", "trigger_id": "R13L89_REVIEW_C03_FIRSTEC_2024_STAGE2_FALSE_POSITIVE_DRONE_DEFENSE_THEME", "symbol": "010820", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: bridge-missing theme/event premium with high MAE or low MFE is blocked from positive Stage2/Stage3 promotion.", "MFE_90D_pct": 5.98, "MAE_90D_pct": -15.94, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_rejection_alignment", "current_profile_verdict": "current_profile_false_positive_if_drone_defense_theme_counts_without_export_backlog_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L89_REVIEW_C03_SATREC_2024_SPACE_DEFENSE_EVENT_CAP_4B", "trigger_id": "R13L89_REVIEW_C03_SATREC_2024_STAGE4B_SPACE_DEFENSE_THEME_CAP", "symbol": "099320", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: bridge-missing theme/event premium with high MAE or low MFE is blocked from positive Stage2/Stage3 promotion.", "MFE_90D_pct": 6.75, "MAE_90D_pct": -42.34, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_rejection_alignment", "current_profile_verdict": "current_profile_4B_too_late_if_space_defense_theme_premium_not_capped"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L89_REVIEW_C31_VISANG_2024_EDUCATION_POLICY_FALSE_STAGE2", "trigger_id": "R13L89_REVIEW_C31_VISANG_2024_STAGE2_FALSE_POSITIVE_EDUCATION_POLICY_THEME", "symbol": "100220", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: bridge-missing theme/event premium with high MAE or low MFE is blocked from positive Stage2/Stage3 promotion.", "MFE_90D_pct": 20.29, "MAE_90D_pct": -35.71, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_rejection_alignment", "current_profile_verdict": "current_profile_false_positive_if_education_policy_theme_counts_without_revenue_contract_or_subsidy_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L89_REVIEW_C31_IBKIMYOUNG_2024_DIGITAL_EDU_EVENT_CAP_4B", "trigger_id": "R13L89_REVIEW_C31_IBKIMYOUNG_2024_STAGE4B_DIGITAL_EDU_POLICY_THEME_CAP", "symbol": "339950", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "original_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "R13 cross-review: bridge-missing theme/event premium with high MAE or low MFE is blocked from positive Stage2/Stage3 promotion.", "MFE_90D_pct": 11.26, "MAE_90D_pct": -32.16, "score_return_alignment_label": "r13_high_MAE_guardrail_improves_rejection_alignment", "current_profile_verdict": "current_profile_4B_too_late_if_digital_education_policy_theme_premium_not_capped"}
```

### 24.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "89", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "BRIDGE_MISSING_HIGH_MAE_EVENT_CAP_REVIEW_AFTER_R9_R12_LOOP89", "new_independent_case_count": 0, "reused_case_count": 8, "new_symbol_count": 0, "same_archetype_new_symbol_count": 0, "same_archetype_new_trigger_family_count": 0, "new_trigger_family_count": 0, "positive_case_count": 0, "counterexample_count": 8, "4B_case_count": 4, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["bridge_missing_false_stage2", "event_premium_cap_4B", "high_MAE_rejection_guardrail", "theme_or_policy_without_conversion"], "loop_contribution_label": "axis_stress_test_passed", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 8, "evidence_url_pending_count": 8}
```

### 24.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","reason":"R13 review rows reuse already computed stock-web 180D windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 25. Deferred Coding Agent Handoff Prompt

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
- R13 review rows with `do_not_count_as_new_case=true` must not add weight.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- High-MAE guardrail rows are rejection/risk calibration only.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
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
10. Add tests that R13 review-only rows cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 26. Next Round State

```text
completed_round = R13
completed_loop = 89
next_round = R1
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```

## 27. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This R13 file contains no new independent case, no investment recommendation, and no production scoring change.
