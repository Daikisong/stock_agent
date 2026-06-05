# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = MEMORY_TESTER_EQUIPMENT_RECOVERY_BRIDGE_VS_OSAT_MEMORY_THEME_FALSE_STAGE2_AND_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_93_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R1 loop 93 is R2 / loop 93. R2 is the L2 AI / semiconductor / electronics round, and this run uses C10 memory recovery equipment-cycle behavior after recent R2 loops covered C07, C06, and C08.

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
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R2
scheduled_loop = 93
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
round_sector_consistency = pass
computed_next_round = R3
computed_next_loop = 93
```

R2 loop 90 used C07, loop 91 used C06, and loop 92 used C08. This loop moves into C10 and tests memory-tester recovery vs OSAT memory-recovery false Stage2 vs advanced packaging equipment 4B cap behavior.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE = 29 rows / 18 symbols / good-bad Stage2 15-5 / 4B-4C 1-0
top covered symbols include 089970(3), 281820(3), 319660(3), 042700(2), 064290(2), 079370(2)
previous R2 loop-90 C07 symbols avoided: 232140, 036200, 039440
previous R2 loop-91 C06 symbols avoided: 000660, 080220, 253590
previous R2 loop-92 C08 symbols avoided: 058470, 098120, 080580
previous R1 loop-93 C05 symbols avoided: 100840, 094820, 010960
```

Selected rows avoid hard duplicates and top repeated C10 symbols:

```text
003160 / Stage2-Actionable / 2024-02-19
036540 / Stage2-Actionable / 2024-01-24
031980 / Stage4B / 2024-06-19
```

092870 was inspected but rejected for this loop because its 2024-07-31 corporate-action candidate contaminates the likely 180D calibration window.

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
| 003160 | atlas/symbol_profiles/003/003160.json | selected 2024 window clean after old 1997~1999 CA candidates |
| 036540 | atlas/symbol_profiles/036/036540.json | selected 2024 window clean after old 2003~2016 CA candidates |
| 031980 | atlas/symbol_profiles/031/031980.json | selected 2024/2025 180D window clean after old 1998~2020 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L93_C10_DI_2024_MEMORY_TESTER_EQUIPMENT_RECOVERY_POSITIVE | 003160 | 2024-02-19 | yes | 180 | yes | yes | true |
| R2L93_C10_SFASEMI_2024_OSAT_MEMORY_RECOVERY_FALSE_STAGE2 | 036540 | 2024-01-24 | yes | 180 | yes | yes | true |
| R2L93_C10_PSKHOLDINGS_2024_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP_4B | 031980 | 2024-06-19 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | MEMORY_TESTER_EQUIPMENT_RECOVERY_BRIDGE | Positive Stage2 requires memory tester/equipment order, customer capacity pull-in, utilization, margin and revision bridge. |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | OSAT_MEMORY_THEME_FALSE_STAGE2 | OSAT/memory recovery label without order-utilization-margin bridge can become false Stage2. |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP_4B | Advanced packaging equipment premium should route to 4B when order/customer/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L93_C10_DI_2024_MEMORY_TESTER_EQUIPMENT_RECOVERY_POSITIVE | 003160 | 디아이 | positive | Memory tester / HBM-adjacent equipment recovery produced explosive forward MFE. |
| R2L93_C10_SFASEMI_2024_OSAT_MEMORY_RECOVERY_FALSE_STAGE2 | 036540 | SFA반도체 | counterexample | OSAT memory-recovery spike had low MFE and persistent MAE without order/utilization bridge. |
| R2L93_C10_PSKHOLDINGS_2024_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP_4B | 031980 | 피에스케이홀딩스 | counterexample / 4B | Advanced packaging equipment premium capped around the June spike and then suffered severe MAE. |

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
| DI memory tester recovery bridge | historical public/report proxy | true | true | shadow-only positive |
| SFA Semiconductor OSAT memory false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| PSK Holdings advanced-packaging cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 003160 | atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv | atlas/symbol_profiles/003/003160.json |
| 036540 | atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv | atlas/symbol_profiles/036/036540.json |
| 031980 | atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv and 2025.csv | atlas/symbol_profiles/031/031980.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L93_C10_DI_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_EQUIPMENT_RECOVERY | 003160 | Stage2-Actionable | 2024-02-19 | 7160 | positive | memory tester/equipment recovery bridge worked |
| R2L93_C10_SFASEMI_2024_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY_THEME | 036540 | Stage2-Actionable | 2024-01-24 | 7480 | counterexample | OSAT memory-recovery false Stage2 |
| R2L93_C10_PSKHOLDINGS_2024_STAGE4B_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP | 031980 | Stage4B | 2024-06-19 | 76500 | counterexample/4B | advanced packaging equipment event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L93_C10_DI_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_EQUIPMENT_RECOVERY | 7160 | 95.95 | -13.83 | 330.17 | -13.83 | 330.17 | -13.83 | 2024-06-27 | 30800 | -49.51 |
| R2L93_C10_SFASEMI_2024_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY_THEME | 7480 | 8.96 | -21.12 | 8.96 | -28.21 | 8.96 | -35.43 | 2024-01-24 | 8150 | -40.74 |
| R2L93_C10_PSKHOLDINGS_2024_STAGE4B_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP | 76500 | 11.50 | -25.49 | 11.50 | -52.81 | 11.50 | -54.90 | 2024-06-19 | 85300 | -59.55 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C10 Stage2 needs order / customer capacity / utilization / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing memory equipment premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE OSAT/equipment rows cannot promote without durable bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is memory-equipment bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 003160 | good_stage2_with_later_watch | Memory tester/equipment recovery produced extreme MFE, but post-peak drawdown requires later 4B valuation watch. |
| 036540 | bad_stage2 | OSAT memory recovery theme lacked order/utilization bridge and had low forward MFE. |
| 031980 | good_4B | Advanced packaging equipment event premium capped around entry and then suffered severe MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 036540 OSAT memory false Stage2 | 0.92 | 0.92 | false Stage2 due missing order/utilization/margin bridge |
| 031980 advanced packaging cap | 0.90 | 0.90 | good 4B timing after severe MAE confirmed cap |
| 003160 memory tester bridge | n/a | n/a | positive Stage2, but later equipment valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 036540 / 031980
```

No hard 4C candidate is proposed. R2 loop 93 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 memory recovery equipment-cycle cases, Stage2 requires verified tester/equipment order, customer capacity pull-in, packaging/test utilization, margin recovery, or revision bridge. Memory, OSAT, HBM sympathy, advanced packaging, or semiconductor equipment label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
rule = C10 should split true memory tester/equipment order positives from OSAT memory-recovery false Stage2 and advanced packaging/equipment event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 116.88 | -31.62 | 0.67 | mixed; C10 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 116.88 | -31.62 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L2 order/utilization/margin bridge required | 2 | 169.57 | -21.02 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C10 bridge vs event-cap split | 2 | 169.57 | -21.02 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing memory-equipment themes as positive | 1 | 330.17 | -13.83 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 003160 memory tester bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 330.17 | -13.83 | memory_tester_equipment_recovery_positive |
| 036540 OSAT false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 8.96 | -28.21 | OSAT_memory_recovery_false_stage2 |
| 031980 advanced packaging cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 11.50 | -52.81 | advanced_packaging_equipment_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_EQUIPMENT_RECOVERY_BRIDGE_VS_OSAT_MEMORY_THEME_FALSE_STAGE2_AND_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C10 memory tester/equipment recovery positive, OSAT memory recovery false Stage2, and advanced packaging equipment event-cap 4B split while avoiding top repeated C10 symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: memory_tester_equipment_recovery_positive, OSAT_memory_recovery_false_stage2, advanced_packaging_equipment_event_cap_4B
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
- C10 memory recovery equipment-cycle bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,configured,C10_requires_memory_order_customer_capacity_utilization_margin_revision_bridge,0,"C10 Stage2 should require tester/equipment order visibility, customer capacity pull-in, utilization, margin, or revision bridge, not memory/OSAT/equipment label alone","DI positive worked; SFA Semiconductor and PSK Holdings event/theme rows failed positive-stage promotion","R2L93_C10_DI_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_EQUIPMENT_RECOVERY|R2L93_C10_SFASEMI_2024_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY_THEME|R2L93_C10_PSKHOLDINGS_2024_STAGE4B_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,configured,cap_bridge_missing_memory_equipment_and_packaging_event_premiums_as_4B_watch,0,"Memory/advanced-packaging equipment premiums can peak before order and margin bridge is proven","SFA had low forward MFE and deep MAE; PSK Holdings showed 4B event-cap behavior after June spike","R2L93_C10_SFASEMI_2024_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY_THEME|R2L93_C10_PSKHOLDINGS_2024_STAGE4B_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,configured,block_positive_stage_when_memory_recovery_theme_has_high_MAE_without_order_margin_bridge,0,"High MAE after bridge-missing memory/equipment entries should block Stage2/Stage3 promotion unless order, utilization and margin evidence survives","SFA MAE90=-28.21 and PSK Holdings MAE90=-52.81","R2L93_C10_SFASEMI_2024_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY_THEME|R2L93_C10_PSKHOLDINGS_2024_STAGE4B_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L93_C10_DI_2024_MEMORY_TESTER_EQUIPMENT_RECOVERY_POSITIVE", "symbol": "003160", "company_name": "디아이", "round": "R2", "loop": "93", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_EQUIPMENT_RECOVERY_BRIDGE_VS_OSAT_MEMORY_THEME_FALSE_STAGE2_AND_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP", "case_type": "structural_success_with_later_equipment_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R2L93_C10_DI_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_EQUIPMENT_RECOVERY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Memory tester / HBM-adjacent equipment recovery bridge produced explosive 30D/90D/180D MFE, but later peak drawdown confirms the need for a 4B valuation watch after the positive bridge has already worked.", "current_profile_verdict": "current_profile_kept_but_C10_positive_requires_memory_tester_order_customer_capacity_margin_revision_bridge_not_memory_theme_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1997~1999 CA candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R2L93_C10_SFASEMI_2024_OSAT_MEMORY_RECOVERY_FALSE_STAGE2", "symbol": "036540", "company_name": "SFA반도체", "round": "R2", "loop": "93", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_EQUIPMENT_RECOVERY_BRIDGE_VS_OSAT_MEMORY_THEME_FALSE_STAGE2_AND_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP", "case_type": "failed_rerating_OSAT_memory_recovery_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R2L93_C10_SFASEMI_2024_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "OSAT / memory recovery theme spike produced low forward MFE and persistent 90D/180D MAE. C10 Stage2 should not be awarded from memory-cycle sympathy without customer order, utilization, tester/packaging capacity, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_OSAT_memory_recovery_theme_counts_without_order_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2003~2016 CA candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R2L93_C10_PSKHOLDINGS_2024_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP_4B", "symbol": "031980", "company_name": "피에스케이홀딩스", "round": "R2", "loop": "93", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_EQUIPMENT_RECOVERY_BRIDGE_VS_OSAT_MEMORY_THEME_FALSE_STAGE2_AND_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L93_C10_PSKHOLDINGS_2024_STAGE4B_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Advanced packaging / memory equipment premium capped around the June spike and then produced severe 90D/180D MAE. C10 should route bridge-missing equipment event premiums to 4B unless order backlog, customer capacity pull-in, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_advanced_packaging_equipment_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1998~2020 CA candidates. 2025 forward window checked for 180D path. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L93_C10_DI_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_EQUIPMENT_RECOVERY", "case_id": "R2L93_C10_DI_2024_MEMORY_TESTER_EQUIPMENT_RECOVERY_POSITIVE", "symbol": "003160", "company_name": "디아이", "round": "R2", "loop": "93", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_EQUIPMENT_RECOVERY_BRIDGE_VS_OSAT_MEMORY_THEME_FALSE_STAGE2_AND_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP", "sector": "memory_tester_equipment_recovery_HBM_adjacent", "primary_archetype": "memory_tester_order_customer_capacity_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-19", "entry_date": "2024-02-19", "entry_price": 7160.0, "evidence_available_at_that_date": "memory tester / HBM-adjacent equipment recovery, customer capacity expansion, tester order and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["memory_tester_order_proxy", "HBM_adjacent_capacity_proxy", "customer_capacity_pull_in_proxy", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "very_high_MFE180"], "stage4b_evidence_fields": ["later_equipment_valuation_watch", "post_peak_drawdown_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv", "profile_path": "atlas/symbol_profiles/003/003160.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 95.95, "MFE_90D_pct": 330.17, "MFE_180D_pct": 330.17, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -13.83, "MAE_90D_pct": -13.83, "MAE_180D_pct": -13.83, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-27", "peak_price": 30800.0, "drawdown_after_peak_pct": -49.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_memory_equipment_valuation_4B_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "memory_equipment_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_memory_tester_equipment_recovery_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1997_1999_CA", "same_entry_group_id": "R2L93_C10_003160_2024-02-19_7160", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L93_C10_SFASEMI_2024_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY_THEME", "case_id": "R2L93_C10_SFASEMI_2024_OSAT_MEMORY_RECOVERY_FALSE_STAGE2", "symbol": "036540", "company_name": "SFA반도체", "round": "R2", "loop": "93", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_EQUIPMENT_RECOVERY_BRIDGE_VS_OSAT_MEMORY_THEME_FALSE_STAGE2_AND_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP", "sector": "OSAT_memory_recovery_theme", "primary_archetype": "OSAT_memory_recovery_without_order_utilization_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 7480.0, "evidence_available_at_that_date": "OSAT / memory recovery theme, packaging demand recovery and utilization expectation proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["OSAT_memory_recovery_theme", "packaging_utilization_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_forward_MFE", "high_MAE90", "order_utilization_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv", "profile_path": "atlas/symbol_profiles/036/036540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.96, "MFE_90D_pct": 8.96, "MFE_180D_pct": 8.96, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -21.12, "MAE_90D_pct": -28.21, "MAE_180D_pct": -35.43, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-24", "peak_price": 8150.0, "drawdown_after_peak_pct": -40.74, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "OSAT_memory_recovery_theme_was_false_stage2_due_missing_order_utilization_margin_bridge", "four_b_evidence_type": ["memory_recovery_theme_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_OSAT_memory_recovery_without_order_utilization_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_OSAT_memory_recovery_theme_counts_without_order_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2003_2016_CA", "same_entry_group_id": "R2L93_C10_036540_2024-01-24_7480", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L93_C10_PSKHOLDINGS_2024_STAGE4B_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP", "case_id": "R2L93_C10_PSKHOLDINGS_2024_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP_4B", "symbol": "031980", "company_name": "피에스케이홀딩스", "round": "R2", "loop": "93", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_EQUIPMENT_RECOVERY_BRIDGE_VS_OSAT_MEMORY_THEME_FALSE_STAGE2_AND_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP", "sector": "advanced_packaging_memory_equipment_event_premium", "primary_archetype": "advanced_packaging_equipment_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-19", "entry_date": "2024-06-19", "entry_price": 76500.0, "evidence_available_at_that_date": "advanced packaging / memory equipment event premium after June spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["advanced_packaging_equipment_event", "memory_equipment_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "order_customer_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv", "profile_path": "atlas/symbol_profiles/031/031980.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.5, "MFE_90D_pct": 11.5, "MFE_180D_pct": 11.5, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -25.49, "MAE_90D_pct": -52.81, "MAE_180D_pct": -54.9, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 85300.0, "drawdown_after_peak_pct": -59.55, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "good_full_window_4B_timing_advanced_packaging_equipment_event_cap", "four_b_evidence_type": ["memory_equipment_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_advanced_packaging_memory_equipment_premium", "current_profile_verdict": "current_profile_4B_too_late_if_advanced_packaging_equipment_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1998_2020_CA", "same_entry_group_id": "R2L93_C10_031980_2024-06-19_76500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L93_C10_DI_2024_MEMORY_TESTER_EQUIPMENT_RECOVERY_POSITIVE", "trigger_id": "R2L93_C10_DI_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_EQUIPMENT_RECOVERY", "symbol": "003160", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 80, "customer_quality_score": 50, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "memory_tester_equipment_recovery_positive", "MFE_90D_pct": 330.17, "MAE_90D_pct": -13.83, "score_return_alignment_label": "memory_tester_equipment_recovery_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L93_C10_SFASEMI_2024_OSAT_MEMORY_RECOVERY_FALSE_STAGE2", "trigger_id": "R2L93_C10_SFASEMI_2024_STAGE2_FALSE_POSITIVE_OSAT_MEMORY_RECOVERY_THEME", "symbol": "036540", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "OSAT_memory_recovery_false_stage2", "MFE_90D_pct": 8.96, "MAE_90D_pct": -28.21, "score_return_alignment_label": "OSAT_memory_recovery_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_OSAT_memory_recovery_theme_counts_without_order_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L93_C10_PSKHOLDINGS_2024_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP_4B", "trigger_id": "R2L93_C10_PSKHOLDINGS_2024_STAGE4B_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP", "symbol": "031980", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "advanced_packaging_equipment_event_cap_4B_guard", "MFE_90D_pct": 11.5, "MAE_90D_pct": -52.81, "score_return_alignment_label": "advanced_packaging_equipment_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_advanced_packaging_equipment_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "93", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_EQUIPMENT_RECOVERY_BRIDGE_VS_OSAT_MEMORY_THEME_FALSE_STAGE2_AND_ADVANCED_PACKAGING_EQUIPMENT_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["memory_tester_equipment_recovery_positive", "OSAT_memory_recovery_false_stage2", "advanced_packaging_equipment_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
10. Add tests that bridge-missing C10 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 93
next_round = R3
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
