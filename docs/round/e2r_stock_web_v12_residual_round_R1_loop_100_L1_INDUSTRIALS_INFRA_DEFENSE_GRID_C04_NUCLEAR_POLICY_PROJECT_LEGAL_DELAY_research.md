# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 100
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_VS_NUCLEAR_INSPECTION_LOW_MFE_FALSE_STAGE2_AND_BOP_EPC_EVENT_CAP
loop_objective = priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | nuclear_policy_project_execution_guardrail | legal_delay_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R1_loop_100_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. Priority 0 has been locally supplemented, and Priority 1 already added C03 and C16. C04 is the next unsupplemented Priority 1 gap still below the 50-row practical calibration zone. Since R1 loop99 was used locally for C03, this file uses R1 loop100 to avoid local round-loop collision.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_1_stock_web_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
nuclear_policy_project_execution_guardrail = existing_axis_strengthened
legal_delay_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R1
scheduled_loop = 100
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C04 is a nuclear policy / project execution / legal-delay archetype. Policy is the switchyard blueprint; the investable signal is whether project order, licensing clarity, delivery schedule, customer quality, margin and revision actually light the grid.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY = 31 rows / Priority 1
top covered C04 symbols avoided: 052690, 051600, 105840, 130660, 094820, 019990
recent local Priority 0/1 artifacts accounted for: C08, C09, C01, C07, C06, C10, C14, C11, C02, C13, C19, C27, C12, C24, C28, C17, C23, C03, C16
```

Selected rows avoid hard duplicates and add new C04 trigger families:

```text
034020 / Stage2-Actionable / 2024-04-22
046120 / Stage2-Actionable / 2024-02-16
083650 / Stage4B / 2024-05-27
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
| 034020 | atlas/symbol_profiles/034/034020.json | selected 2024 window clean after old 2019/2020 CA candidates |
| 046120 | atlas/symbol_profiles/046/046120.json | selected 2024 window clean after old 2017 CA candidate |
| 083650 | atlas/symbol_profiles/083/083650.json | selected 2024 window clean after old 2006/2015 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R1L100_C04_DOOSANENER_2024_NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_POSITIVE | 034020 | 2024-04-22 | yes | 180 | yes | yes | true |
| R1L100_C04_ORBITEC_2024_NUCLEAR_INSPECTION_POLICY_LOW_MFE_FALSE_STAGE2 | 046120 | 2024-02-16 | yes | 180 | yes | yes | true |
| R1L100_C04_BHI_2024_NUCLEAR_BOP_EPC_EVENT_CAP_4B | 083650 | 2024-05-27 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE | Positive Stage2 requires project order, execution schedule, licensing/legal clarity, customer quality, margin and revision bridge. |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_INSPECTION_FALSE_STAGE2 | Nuclear inspection/policy watch without contract conversion and utilization/margin bridge can become false Stage2. |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_BOP_EPC_EVENT_CAP_4B | Nuclear BOP/EPC policy premium should route to 4B when project award, legal clarity and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R1L100_C04_DOOSANENER_2024_NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_POSITIVE | 034020 | 두산에너빌리티 | positive | Nuclear project/order execution bridge produced strong MFE with controlled initial MAE. |
| R1L100_C04_ORBITEC_2024_NUCLEAR_INSPECTION_POLICY_LOW_MFE_FALSE_STAGE2 | 046120 | 오르비텍 | counterexample | Nuclear inspection policy watch produced tiny MFE and meaningful MAE without contract/utilization bridge. |
| R1L100_C04_BHI_2024_NUCLEAR_BOP_EPC_EVENT_CAP_4B | 083650 | 비에이치아이 | counterexample / 4B | Nuclear BOP/EPC policy premium capped near late-May high and then drew down. |

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
| Doosan Enerbility nuclear project/order execution bridge | historical public/report proxy | true | true | shadow-only positive |
| Orbitec nuclear inspection false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| BHI nuclear BOP/EPC policy event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 034020 | atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv | atlas/symbol_profiles/034/034020.json |
| 046120 | atlas/ohlcv_tradable_by_symbol_year/046/046120/2024.csv | atlas/symbol_profiles/046/046120.json |
| 083650 | atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv | atlas/symbol_profiles/083/083650.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R1L100_C04_DOOSANENER_2024_STAGE2_ACTIONABLE_NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE | 034020 | Stage2-Actionable | 2024-04-22 | 15730 | positive | nuclear project execution bridge worked |
| R1L100_C04_ORBITEC_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_POLICY_WATCH | 046120 | Stage2-Actionable | 2024-02-16 | 3515 | counterexample | nuclear inspection false Stage2 |
| R1L100_C04_BHI_2024_STAGE4B_NUCLEAR_BOP_EPC_POLICY_EVENT_CAP | 083650 | Stage4B | 2024-05-27 | 11360 | counterexample/4B | nuclear BOP/EPC event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L100_C04_DOOSANENER_2024_STAGE2_ACTIONABLE_NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE | 15730 | 39.86 | -4.96 | 58.93 | -4.96 | 58.93 | -4.96 | 2024-07-18 | 25000 | -23.12 |
| R1L100_C04_ORBITEC_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_POLICY_WATCH | 3515 | 0.57 | -6.97 | 0.57 | -15.50 | 0.57 | -15.50 | 2024-02-19 | 3535 | -16.82 |
| R1L100_C04_BHI_2024_STAGE4B_NUCLEAR_BOP_EPC_POLICY_EVENT_CAP | 11360 | 7.13 | -12.59 | 7.13 | -28.96 | 7.13 | -28.96 | 2024-05-27 | 12170 | -33.69 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C04 Stage2 needs project order / execution schedule / licensing clarity / customer quality / margin / revision bridge |
| nuclear_policy_project_execution_guardrail | strengthen: nuclear policy label alone cannot promote positive stage |
| legal_delay_guardrail | strengthen: licensing/legal-delay risk must keep policy-only setups in watch/4B |
| local_4b_watch_guard | strengthen: bridge-missing nuclear inspection and BOP/EPC premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C04 rows cannot promote without durable project/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether nuclear policy narrative becomes order, licensing, execution and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 034020 | good_stage2_with_later_watch | Project/order execution bridge produced strong MFE, but later policy valuation watch remains necessary. |
| 046120 | bad_stage2 | Inspection/policy watch lacked contract conversion and utilization/margin bridge, producing tiny MFE. |
| 083650 | good_4B | BOP/EPC policy premium peaked near late-May and later drew down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 046120 nuclear inspection false Stage2 | 0.99 | 0.99 | false Stage2 due missing contract conversion / utilization / margin bridge |
| 083650 nuclear BOP/EPC cap | 0.93 | 0.93 | good 4B timing after nuclear BOP/EPC policy premium |
| 034020 nuclear project bridge | n/a | n/a | positive Stage2, but later nuclear-policy valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = legal_delay_watch_only for 046120 / 083650
```

No hard 4C candidate is introduced in this C04 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 nuclear policy/project cases, Stage2 requires verified project order, execution schedule, licensing or legal clarity, customer/utility quality, margin and revision bridge. Nuclear policy, inspection, SMR, EPC/BOP, legal approval, export framework or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
rule = C04 should split true project-order/execution/margin positives from nuclear inspection false Stage2 and BOP/EPC event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 22.21 | -16.47 | 0.67 | mixed; C04 project/legal bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 22.21 | -16.47 | 0.67 | weaker C04 bridge split |
| P1 sector_specific_candidate_profile | L1 nuclear project/execution bridge required | 2 | 29.75 | -10.23 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C04 bridge vs event-cap split | 2 | 29.75 | -10.23 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing nuclear policy themes as positive | 1 | 58.93 | -4.96 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 034020 nuclear project bridge | 66 | Stage2-Watch | 80 | Stage2-Actionable | 58.93 | -4.96 | nuclear_policy_project_positive |
| 046120 nuclear inspection false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 0.57 | -15.50 | nuclear_inspection_false_stage2 |
| 083650 BOP/EPC event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 7.13 | -28.96 | nuclear_BOP_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_VS_NUCLEAR_INSPECTION_LOW_MFE_FALSE_STAGE2_AND_BOP_EPC_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C04 is the next unsupplemented Priority 1 archetype after C03/C16 and still remains below the practical 50-row calibration zone. This run adds Doosan Enerbility, Orbitec, and BHI while avoiding top-covered C04 symbols 052690, 051600, 105840, 130660, 094820 and 019990."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, nuclear_policy_project_execution_guardrail, legal_delay_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: nuclear_policy_project_positive, nuclear_inspection_false_stage2, nuclear_BOP_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, nuclear_policy_project_execution_guardrail, legal_delay_guardrail, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: priority1_canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C04 nuclear policy project legal-delay bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,configured,C04_requires_project_order_execution_schedule_licensing_customer_margin_revision_bridge,0,"C04 Stage2 should require project order, execution schedule, licensing or legal clarity, customer/utility quality, margin and revision bridge, not nuclear policy label alone","Doosan Enerbility positive worked; Orbitec and BHI event/watch rows failed positive-stage promotion","R1L100_C04_DOOSANENER_2024_STAGE2_ACTIONABLE_NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE|R1L100_C04_ORBITEC_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_POLICY_WATCH|R1L100_C04_BHI_2024_STAGE4B_NUCLEAR_BOP_EPC_POLICY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,configured,cap_bridge_missing_nuclear_inspection_and_BOP_EPC_event_premiums_as_4B_watch,0,"Nuclear inspection and BOP/EPC premiums can peak before project award, licensing clarity, utilization and margin bridge is proven","Orbitec had tiny MFE after February policy watch; BHI showed 4B event-cap behavior after late-May nuclear BOP/EPC premium","R1L100_C04_ORBITEC_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_POLICY_WATCH|R1L100_C04_BHI_2024_STAGE4B_NUCLEAR_BOP_EPC_POLICY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,configured,block_positive_stage_when_nuclear_policy_theme_has_high_or_persistent_MAE_without_project_execution_bridge,0,"High or persistent MAE after bridge-missing C04 entries should block Stage2/Stage3 promotion unless project execution, licensing and margin evidence survives","Orbitec MAE90=-15.50 and BHI MAE90=-28.96","R1L100_C04_ORBITEC_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_POLICY_WATCH|R1L100_C04_BHI_2024_STAGE4B_NUCLEAR_BOP_EPC_POLICY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R1L100_C04_DOOSANENER_2024_NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_POSITIVE", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_VS_NUCLEAR_INSPECTION_LOW_MFE_FALSE_STAGE2_AND_BOP_EPC_EVENT_CAP", "case_type": "structural_success_with_later_nuclear_policy_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L100_C04_DOOSANENER_2024_STAGE2_ACTIONABLE_NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Nuclear policy / large project / turbine-BOP execution bridge produced strong 30D/90D/180D MFE after the April project-policy base, with manageable initial MAE. C04 works when policy momentum is tied to actual project order, execution schedule, customer/utility quality, licensing path, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C04_positive_requires_project_order_execution_schedule_licensing_customer_margin_revision_bridge_not_nuclear_policy_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2019/2020 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R1L100_C04_ORBITEC_2024_NUCLEAR_INSPECTION_POLICY_LOW_MFE_FALSE_STAGE2", "symbol": "046120", "company_name": "오르비텍", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_VS_NUCLEAR_INSPECTION_LOW_MFE_FALSE_STAGE2_AND_BOP_EPC_EVENT_CAP", "case_type": "failed_rerating_nuclear_inspection_policy_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R1L100_C04_ORBITEC_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_POLICY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Nuclear inspection / policy watch around the February bounce produced almost no forward MFE and then meaningful MAE. C04 Stage2 should not be awarded without explicit inspection/service contract conversion, licensing schedule, utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_nuclear_policy_inspection_watch_counts_without_contract_conversion_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2017 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R1L100_C04_BHI_2024_NUCLEAR_BOP_EPC_EVENT_CAP_4B", "symbol": "083650", "company_name": "비에이치아이", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_VS_NUCLEAR_INSPECTION_LOW_MFE_FALSE_STAGE2_AND_BOP_EPC_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L100_C04_BHI_2024_STAGE4B_NUCLEAR_BOP_EPC_POLICY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Nuclear BOP / EPC / policy event premium capped near the late-May high and then drew down sharply. C04 should route bridge-missing nuclear equipment/EPC policy premiums to 4B unless project award, delivery schedule, legal/licensing clarity, working-capital control, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_BOP_EPC_policy_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2006/2015 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R1L100_C04_DOOSANENER_2024_STAGE2_ACTIONABLE_NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE", "case_id": "R1L100_C04_DOOSANENER_2024_NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_POSITIVE", "symbol": "034020", "company_name": "두산에너빌리티", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_VS_NUCLEAR_INSPECTION_LOW_MFE_FALSE_STAGE2_AND_BOP_EPC_EVENT_CAP", "sector": "nuclear_policy_project_order_execution_margin", "primary_archetype": "project_order_execution_schedule_licensing_customer_margin_revision_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | nuclear_policy_project_execution_guardrail | legal_delay_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-22", "entry_date": "2024-04-22", "entry_price": 15730.0, "evidence_available_at_that_date": "nuclear policy/project order execution, utility/customer quality, licensing path and turbine-BOP margin/revision bridge proxy after April policy base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["nuclear_project_order_proxy", "execution_schedule_proxy", "utility_customer_quality_proxy", "licensing_path_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "manageable_initial_MAE"], "stage4b_evidence_fields": ["later_nuclear_policy_valuation_watch", "project_execution_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv", "profile_path": "atlas/symbol_profiles/034/034020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 39.86, "MFE_90D_pct": 58.93, "MFE_180D_pct": 58.93, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.96, "MAE_90D_pct": -4.96, "MAE_180D_pct": -4.96, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 25000.0, "drawdown_after_peak_pct": -23.12, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_nuclear_policy_valuation_4B_watch_needed", "four_b_evidence_type": ["nuclear_project_order_bridge", "execution_margin", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_nuclear_project_policy_order_execution_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2019_2020_CA", "same_entry_group_id": "R1L100_C04_034020_2024-04-22_15730", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L100_C04_ORBITEC_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_POLICY_WATCH", "case_id": "R1L100_C04_ORBITEC_2024_NUCLEAR_INSPECTION_POLICY_LOW_MFE_FALSE_STAGE2", "symbol": "046120", "company_name": "오르비텍", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_VS_NUCLEAR_INSPECTION_LOW_MFE_FALSE_STAGE2_AND_BOP_EPC_EVENT_CAP", "sector": "nuclear_inspection_service_policy_watch", "primary_archetype": "nuclear_inspection_watch_without_contract_conversion_utilization_margin_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | nuclear_policy_project_execution_guardrail | legal_delay_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-16", "entry_date": "2024-02-16", "entry_price": 3515.0, "evidence_available_at_that_date": "nuclear inspection / service-policy watch after February nuclear-policy bounce without confirmed inspection contract conversion, licensing schedule, utilization, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["nuclear_policy_watch", "inspection_service_theme", "relative_strength_bounce"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tiny_MFE90", "meaningful_MAE90", "contract_conversion_utilization_margin_bridge_missing"], "stage4c_evidence_fields": ["legal_delay_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/046/046120/2024.csv", "profile_path": "atlas/symbol_profiles/046/046120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.57, "MFE_90D_pct": 0.57, "MFE_180D_pct": 0.57, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.97, "MAE_90D_pct": -15.5, "MAE_180D_pct": -15.5, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 3535.0, "drawdown_after_peak_pct": -16.82, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "nuclear_inspection_policy_watch_was_false_stage2_due_missing_contract_conversion_utilization_margin_bridge", "four_b_evidence_type": ["nuclear_inspection_policy_premium", "bridge_missing", "tiny_MFE"], "four_c_protection_label": "legal_delay_watch_only", "trigger_outcome_label": "bad_stage2_nuclear_inspection_policy_watch_without_contract_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_nuclear_policy_inspection_watch_counts_without_contract_conversion_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2017_CA", "same_entry_group_id": "R1L100_C04_046120_2024-02-16_3515", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L100_C04_BHI_2024_STAGE4B_NUCLEAR_BOP_EPC_POLICY_EVENT_CAP", "case_id": "R1L100_C04_BHI_2024_NUCLEAR_BOP_EPC_EVENT_CAP_4B", "symbol": "083650", "company_name": "비에이치아이", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_VS_NUCLEAR_INSPECTION_LOW_MFE_FALSE_STAGE2_AND_BOP_EPC_EVENT_CAP", "sector": "nuclear_BOP_EPC_policy_event_premium", "primary_archetype": "nuclear_BOP_EPC_policy_event_cap_4B", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | nuclear_policy_project_execution_guardrail | legal_delay_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-27", "entry_date": "2024-05-27", "entry_price": 11360.0, "evidence_available_at_that_date": "nuclear BOP/EPC policy event premium without confirmed project award, delivery schedule, legal/licensing clarity, working-capital control, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["nuclear_BOP_EPC_event", "policy_project_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "project_award_margin_bridge_recheck"], "stage4c_evidence_fields": ["legal_delay_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv", "profile_path": "atlas/symbol_profiles/083/083650.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.13, "MFE_90D_pct": 7.13, "MFE_180D_pct": 7.13, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -12.59, "MAE_90D_pct": -28.96, "MAE_180D_pct": -28.96, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-27", "peak_price": 12170.0, "drawdown_after_peak_pct": -33.69, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing_nuclear_BOP_EPC_policy_event_cap_due_missing_project_award_legal_margin_bridge", "four_b_evidence_type": ["nuclear_BOP_EPC_policy_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "legal_delay_watch_only", "trigger_outcome_label": "event_cap_4B_success_nuclear_BOP_EPC_policy_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_BOP_EPC_policy_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2006_2015_CA", "same_entry_group_id": "R1L100_C04_083650_2024-05-27_11360", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R1L100_C04_DOOSANENER_2024_NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_POSITIVE", "trigger_id": "R1L100_C04_DOOSANENER_2024_STAGE2_ACTIONABLE_NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE", "symbol": "034020", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 80, "customer_quality_score": 60, "policy_or_regulatory_score": 70, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "nuclear_project_order_execution_positive", "MFE_90D_pct": 58.93, "MAE_90D_pct": -4.96, "score_return_alignment_label": "nuclear_policy_project_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R1L100_C04_ORBITEC_2024_NUCLEAR_INSPECTION_POLICY_LOW_MFE_FALSE_STAGE2", "trigger_id": "R1L100_C04_ORBITEC_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_POLICY_WATCH", "symbol": "046120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 55, "customer_quality_score": 25, "policy_or_regulatory_score": 55, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 15, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "nuclear_inspection_policy_false_stage2", "MFE_90D_pct": 0.57, "MAE_90D_pct": -15.5, "score_return_alignment_label": "nuclear_inspection_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_nuclear_policy_inspection_watch_counts_without_contract_conversion_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R1L100_C04_BHI_2024_NUCLEAR_BOP_EPC_EVENT_CAP_4B", "trigger_id": "R1L100_C04_BHI_2024_STAGE4B_NUCLEAR_BOP_EPC_POLICY_EVENT_CAP", "symbol": "083650", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 75, "customer_quality_score": 30, "policy_or_regulatory_score": 60, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 65, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "nuclear_BOP_EPC_event_cap_4B_guard", "MFE_90D_pct": 7.13, "MAE_90D_pct": -28.96, "score_return_alignment_label": "nuclear_BOP_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_BOP_EPC_policy_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_PROJECT_POLICY_ORDER_EXECUTION_BRIDGE_VS_NUCLEAR_INSPECTION_LOW_MFE_FALSE_STAGE2_AND_BOP_EPC_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "nuclear_policy_project_execution_guardrail", "legal_delay_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["nuclear_policy_project_positive", "nuclear_inspection_false_stage2", "nuclear_BOP_event_cap_4B"], "loop_contribution_label": "priority1_canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile.

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
- C04 rows need explicit project order, execution schedule, licensing or legal clarity, customer/utility quality, margin and revision bridge before positive promotion.
- In C04, bridge-missing nuclear policy/project event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C04 nuclear policy project legal-delay rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R1
completed_loop = 100
completed_canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 1 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
