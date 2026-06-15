# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_VS_SCRUBBER_CHILLER_LOW_MFE_FALSE_STAGE2_AND_CVD_EQUIPMENT_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | memory_recovery_order_cycle_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_98_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. A duplicate C06 artifact was generated during this run but is not the final artifact because C06 was already finalized immediately before. After local C08/C09/C01/C07/C06 supplementation, C10 is the next thin Priority 0 archetype.

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
memory_recovery_order_cycle_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R2
scheduled_loop = 98
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C10 is a memory recovery / equipment cycle archetype. The cycle headline is the tide; the usable signal is whether actual customer orders, delivery slots, fab utilization, equipment mix, margin and revision float with it.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE = 21 rows / Priority 0
top covered symbols include 036930, 074600, 003160, 031980, 036540, 039030
recent local C08/C09/C01/C07/C06 artifacts accounted for but not duplicated
```

Selected rows avoid hard duplicates and add new C10 trigger families:

```text
089030 / Stage2-Actionable / 2024-03-12
036200 / Stage2-Actionable / 2024-05-29
095610 / Stage4B / 2024-04-17
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
| 089030 | atlas/symbol_profiles/089/089030.json | selected 2024 window clean after old 2011/2022 CA candidates |
| 036200 | atlas/symbol_profiles/036/036200.json | selected 2024 window clean after old 2000/2016/2017 CA candidates |
| 095610 | atlas/symbol_profiles/095/095610.json | selected 2024 window clean after old 2011/2016 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L98_C10_TECHWING_2024_HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_POSITIVE | 089030 | 2024-03-12 | yes | 180 | yes | yes | true |
| R2L98_C10_UNISEM_2024_SCRUBBER_CHILLER_MEMORY_RECOVERY_LOW_MFE_FALSE_STAGE2 | 036200 | 2024-05-29 | yes | 180 | yes | yes | true |
| R2L98_C10_TES_2024_CVD_MEMORY_RECOVERY_EVENT_CAP_4B | 095610 | 2024-04-17 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE | Positive Stage2 requires customer order, delivery, utilization, equipment mix, margin and revision bridge. |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | SCRUBBER_CHILLER_LOW_MFE_FALSE_STAGE2 | Scrubber/chiller cycle watch without order/utilization/margin bridge can become false Stage2. |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | CVD_EQUIPMENT_EVENT_CAP_4B | CVD/deposition equipment premium should route to 4B when order delivery and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L98_C10_TECHWING_2024_HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_POSITIVE | 089030 | 테크윙 | positive | HBM test-handler / memory recovery bridge produced very strong MFE with contained early MAE. |
| R2L98_C10_UNISEM_2024_SCRUBBER_CHILLER_MEMORY_RECOVERY_LOW_MFE_FALSE_STAGE2 | 036200 | 유니셈 | counterexample | Scrubber/chiller cycle watch had low MFE and persistent MAE without order/utilization bridge. |
| R2L98_C10_TES_2024_CVD_MEMORY_RECOVERY_EVENT_CAP_4B | 095610 | 테스 | counterexample / 4B | CVD/deposition equipment premium capped around the April spike and then de-rated. |

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
| Techwing HBM test-handler memory recovery bridge | historical public/report proxy | true | true | shadow-only positive |
| Unisem scrubber/chiller false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| TES CVD/deposition equipment event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 089030 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json |
| 036200 | atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv | atlas/symbol_profiles/036/036200.json |
| 095610 | atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv | atlas/symbol_profiles/095/095610.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L98_C10_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE | 089030 | Stage2-Actionable | 2024-03-12 | 26850 | positive | memory recovery equipment bridge worked |
| R2L98_C10_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_CHILLER_MEMORY_RECOVERY_WATCH | 036200 | Stage2-Actionable | 2024-05-29 | 11940 | counterexample | scrubber/chiller low-MFE false Stage2 |
| R2L98_C10_TES_2024_STAGE4B_CVD_MEMORY_RECOVERY_EQUIPMENT_EVENT_CAP | 095610 | Stage4B | 2024-04-17 | 29300 | counterexample/4B | CVD memory recovery equipment event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L98_C10_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE | 26850 | 40.97 | -6.15 | 163.69 | -6.15 | 163.69 | -6.15 | 2024-07-11 | 70800 | -57.63 |
| R2L98_C10_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_CHILLER_MEMORY_RECOVERY_WATCH | 11940 | 4.52 | -17.84 | 4.52 | -23.79 | 4.52 | -25.00 | 2024-07-04 | 12480 | -31.89 |
| R2L98_C10_TES_2024_STAGE4B_CVD_MEMORY_RECOVERY_EQUIPMENT_EVENT_CAP | 29300 | 12.29 | -23.55 | 12.29 | -27.65 | 12.29 | -27.65 | 2024-04-17 | 32900 | -35.56 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C10 Stage2 needs customer order / delivery / utilization / equipment mix / margin / revision bridge |
| memory_recovery_order_cycle_guardrail | strengthen: memory recovery or equipment-cycle labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing scrubber/chiller and CVD premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C10 rows cannot promote without durable order/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether memory recovery narrative becomes order, delivery, utilization and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 089030 | good_stage2_with_later_watch | HBM test-handler bridge produced very strong MFE, but later valuation watch remains necessary. |
| 036200 | bad_stage2 | Scrubber/chiller watch lacked order/utilization bridge and produced low MFE. |
| 095610 | good_4B | CVD equipment event premium peaked immediately and later drew down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 036200 scrubber/chiller false Stage2 | 0.96 | 0.96 | false Stage2 due missing customer order / utilization / margin bridge |
| 095610 CVD equipment cap | 0.89 | 0.89 | good full-window 4B timing after CVD memory-recovery equipment event premium |
| 089030 HBM test-handler bridge | n/a | n/a | positive Stage2, but later memory-equipment valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 036200 / 095610
```

No hard 4C candidate is introduced in this C10 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 memory recovery equipment-cycle cases, Stage2 requires verified customer order, delivery visibility, fab utilization, equipment mix, ASP/mix, margin, or revision bridge. Memory recovery, equipment cycle, HBM handler, scrubber/chiller, CVD/deposition or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
rule = C10 should split true order/delivery/utilization/margin positives from scrubber/chiller low-MFE false Stage2 and CVD equipment event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 60.17 | -19.20 | 0.67 | mixed; C10 bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 60.17 | -19.20 | 0.67 | weaker C10 bridge split |
| P1 sector_specific_candidate_profile | L2 memory-equipment order/utilization bridge required | 2 | 84.11 | -14.97 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C10 bridge vs event-cap split | 2 | 84.11 | -14.97 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing memory-equipment themes as positive | 1 | 163.69 | -6.15 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 089030 HBM handler bridge | 66 | Stage2-Watch | 81 | Stage2-Actionable | 163.69 | -6.15 | memory_recovery_equipment_positive |
| 036200 scrubber/chiller false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 4.52 | -23.79 | scrubber_chiller_false_stage2 |
| 095610 CVD equipment cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 12.29 | -27.65 | CVD_memory_recovery_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_VS_SCRUBBER_CHILLER_LOW_MFE_FALSE_STAGE2_AND_CVD_EQUIPMENT_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C10 remains a thin Priority 0 archetype after local C08/C09/C01/C07/C06 supplementation. This run adds Techwing, Unisem, and TES rows while avoiding top-covered C10 names and recent local C06/C07/C08/C09 symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, memory_recovery_order_cycle_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: memory_recovery_equipment_positive, scrubber_chiller_false_stage2, CVD_memory_recovery_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, memory_recovery_order_cycle_guardrail, high_MAE_guardrail
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
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,configured,C10_requires_customer_order_delivery_utilization_equipment_mix_margin_revision_bridge,0,"C10 Stage2 should require customer order, delivery visibility, utilization, equipment mix, margin, or revision bridge, not memory recovery/equipment cycle label alone","Techwing positive worked; Unisem and TES event/watch rows failed positive-stage promotion","R2L98_C10_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE|R2L98_C10_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_CHILLER_MEMORY_RECOVERY_WATCH|R2L98_C10_TES_2024_STAGE4B_CVD_MEMORY_RECOVERY_EQUIPMENT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,configured,cap_bridge_missing_scrubber_chiller_and_CVD_memory_recovery_event_premiums_as_4B_watch,0,"Scrubber/chiller and CVD memory-recovery premiums can peak before customer order, delivery, utilization and margin bridge is proven","Unisem had low MFE and persistent MAE after the May spike; TES showed 4B event-cap behavior after the April CVD/deposition spike","R2L98_C10_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_CHILLER_MEMORY_RECOVERY_WATCH|R2L98_C10_TES_2024_STAGE4B_CVD_MEMORY_RECOVERY_EQUIPMENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,configured,block_positive_stage_when_memory_recovery_theme_has_high_or_persistent_MAE_without_order_margin_bridge,0,"High or persistent MAE after bridge-missing C10 entries should block Stage2/Stage3 promotion unless customer order, utilization and margin evidence survives","Unisem MAE90=-23.79 and TES MAE90=-27.65","R2L98_C10_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_CHILLER_MEMORY_RECOVERY_WATCH|R2L98_C10_TES_2024_STAGE4B_CVD_MEMORY_RECOVERY_EQUIPMENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L98_C10_TECHWING_2024_HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_POSITIVE", "symbol": "089030", "company_name": "테크윙", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_VS_SCRUBBER_CHILLER_LOW_MFE_FALSE_STAGE2_AND_CVD_EQUIPMENT_EVENT_CAP", "case_type": "structural_success_with_later_memory_equipment_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R2L98_C10_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "HBM test-handler / memory recovery equipment-cycle bridge produced very strong 30D/90D/180D MFE from the March recovery base, with contained early MAE. C10 works when the memory-cycle recovery label is tied to actual customer order, delivery, utilization, handler/test mix, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C10_positive_requires_customer_order_delivery_utilization_equipment_mix_margin_revision_bridge_not_memory_recovery_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2011/2022 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R2L98_C10_UNISEM_2024_SCRUBBER_CHILLER_MEMORY_RECOVERY_LOW_MFE_FALSE_STAGE2", "symbol": "036200", "company_name": "유니셈", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_VS_SCRUBBER_CHILLER_LOW_MFE_FALSE_STAGE2_AND_CVD_EQUIPMENT_EVENT_CAP", "case_type": "failed_rerating_scrubber_chiller_memory_cycle_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R2L98_C10_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_CHILLER_MEMORY_RECOVERY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Scrubber/chiller memory-recovery watch around the May spike had low forward MFE and then high MAE. C10 Stage2 should not be awarded without confirmed order conversion, customer fab utilization, delivery, service/consumable pull-through, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_scrubber_chiller_memory_recovery_watch_counts_without_customer_order_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2000/2016/2017 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R2L98_C10_TES_2024_CVD_MEMORY_RECOVERY_EVENT_CAP_4B", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_VS_SCRUBBER_CHILLER_LOW_MFE_FALSE_STAGE2_AND_CVD_EQUIPMENT_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L98_C10_TES_2024_STAGE4B_CVD_MEMORY_RECOVERY_EQUIPMENT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "CVD/deposition memory-recovery equipment premium capped around the April spike and then de-rated. C10 should route bridge-missing equipment-cycle premiums to 4B unless actual order intake, delivery slot, customer utilization, ASP/mix, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_CVD_memory_recovery_equipment_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2011/2016 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L98_C10_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE", "case_id": "R2L98_C10_TECHWING_2024_HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_POSITIVE", "symbol": "089030", "company_name": "테크윙", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_VS_SCRUBBER_CHILLER_LOW_MFE_FALSE_STAGE2_AND_CVD_EQUIPMENT_EVENT_CAP", "sector": "HBM_test_handler_memory_recovery_equipment_cycle", "primary_archetype": "customer_order_delivery_utilization_equipment_mix_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | memory_recovery_order_cycle_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-12", "entry_date": "2024-03-12", "entry_price": 26850.0, "evidence_available_at_that_date": "HBM test-handler / memory recovery equipment-cycle order, delivery, utilization, handler/test mix and margin/revision bridge proxy after March recovery base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["HBM_test_handler_proxy", "customer_order_proxy", "delivery_visibility_proxy", "utilization_recovery_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "very_strong_MFE90", "very_strong_MFE180", "contained_initial_MAE"], "stage4b_evidence_fields": ["later_memory_equipment_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv", "profile_path": "atlas/symbol_profiles/089/089030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 40.97, "MFE_90D_pct": 163.69, "MFE_180D_pct": 163.69, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.15, "MAE_90D_pct": -6.15, "MAE_180D_pct": -6.15, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 70800.0, "drawdown_after_peak_pct": -57.63, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_memory_equipment_valuation_4B_watch_needed", "four_b_evidence_type": ["memory_equipment_order_bridge", "HBM_test_handler_mix", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_HBM_test_handler_memory_recovery_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2011_2022_CA", "same_entry_group_id": "R2L98_C10_089030_2024-03-12_26850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L98_C10_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_CHILLER_MEMORY_RECOVERY_WATCH", "case_id": "R2L98_C10_UNISEM_2024_SCRUBBER_CHILLER_MEMORY_RECOVERY_LOW_MFE_FALSE_STAGE2", "symbol": "036200", "company_name": "유니셈", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_VS_SCRUBBER_CHILLER_LOW_MFE_FALSE_STAGE2_AND_CVD_EQUIPMENT_EVENT_CAP", "sector": "scrubber_chiller_memory_recovery_equipment_watch", "primary_archetype": "scrubber_chiller_watch_without_customer_order_utilization_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | memory_recovery_order_cycle_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-29", "entry_date": "2024-05-29", "entry_price": 11940.0, "evidence_available_at_that_date": "scrubber/chiller memory-recovery equipment-cycle watch after May equipment spike without confirmed customer order conversion, fab utilization, delivery, service pull-through, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["scrubber_chiller_memory_cycle_watch", "equipment_recovery_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "persistent_MAE90", "customer_order_utilization_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv", "profile_path": "atlas/symbol_profiles/036/036200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.52, "MFE_90D_pct": 4.52, "MFE_180D_pct": 4.52, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -17.84, "MAE_90D_pct": -23.79, "MAE_180D_pct": -25.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-04", "peak_price": 12480.0, "drawdown_after_peak_pct": -31.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "scrubber_chiller_memory_cycle_watch_was_false_stage2_due_missing_customer_order_utilization_margin_revision_bridge", "four_b_evidence_type": ["scrubber_chiller_cycle_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_scrubber_chiller_memory_recovery_watch_without_order_utilization_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_scrubber_chiller_memory_recovery_watch_counts_without_customer_order_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2000_2016_2017_CA", "same_entry_group_id": "R2L98_C10_036200_2024-05-29_11940", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L98_C10_TES_2024_STAGE4B_CVD_MEMORY_RECOVERY_EQUIPMENT_EVENT_CAP", "case_id": "R2L98_C10_TES_2024_CVD_MEMORY_RECOVERY_EVENT_CAP_4B", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_VS_SCRUBBER_CHILLER_LOW_MFE_FALSE_STAGE2_AND_CVD_EQUIPMENT_EVENT_CAP", "sector": "CVD_deposition_memory_recovery_equipment_event_premium", "primary_archetype": "CVD_memory_recovery_equipment_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | memory_recovery_order_cycle_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-17", "entry_date": "2024-04-17", "entry_price": 29300.0, "evidence_available_at_that_date": "CVD/deposition memory-recovery equipment premium without confirmed order intake, delivery slot, customer utilization, ASP/mix, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["CVD_memory_recovery_event", "equipment_cycle_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE30", "high_MAE90", "order_delivery_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv", "profile_path": "atlas/symbol_profiles/095/095610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.29, "MFE_90D_pct": 12.29, "MFE_180D_pct": 12.29, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -23.55, "MAE_90D_pct": -27.65, "MAE_180D_pct": -27.65, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-17", "peak_price": 32900.0, "drawdown_after_peak_pct": -35.56, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.89, "four_b_full_window_peak_proximity": 0.89, "four_b_timing_verdict": "good_full_window_4B_timing_CVD_memory_recovery_equipment_event_cap_due_missing_order_delivery_margin_bridge", "four_b_evidence_type": ["CVD_memory_recovery_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_CVD_memory_recovery_equipment_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_CVD_memory_recovery_equipment_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2011_2016_CA", "same_entry_group_id": "R2L98_C10_095610_2024-04-17_29300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R2L98_C10_TECHWING_2024_HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_POSITIVE", "trigger_id": "R2L98_C10_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE", "symbol": "089030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 85, "customer_quality_score": 60, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 81, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "HBM_test_handler_memory_recovery_positive", "MFE_90D_pct": 163.69, "MAE_90D_pct": -6.15, "score_return_alignment_label": "memory_recovery_equipment_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R2L98_C10_UNISEM_2024_SCRUBBER_CHILLER_MEMORY_RECOVERY_LOW_MFE_FALSE_STAGE2", "trigger_id": "R2L98_C10_UNISEM_2024_STAGE2_FALSE_POSITIVE_SCRUBBER_CHILLER_MEMORY_RECOVERY_WATCH", "symbol": "036200", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 30, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "scrubber_chiller_memory_recovery_false_stage2", "MFE_90D_pct": 4.52, "MAE_90D_pct": -23.79, "score_return_alignment_label": "scrubber_chiller_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_scrubber_chiller_memory_recovery_watch_counts_without_customer_order_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R2L98_C10_TES_2024_CVD_MEMORY_RECOVERY_EVENT_CAP_4B", "trigger_id": "R2L98_C10_TES_2024_STAGE4B_CVD_MEMORY_RECOVERY_EQUIPMENT_EVENT_CAP", "symbol": "095610", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "CVD_memory_recovery_event_cap_4B_guard", "MFE_90D_pct": 12.29, "MAE_90D_pct": -27.65, "score_return_alignment_label": "CVD_memory_recovery_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_CVD_memory_recovery_equipment_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "HBM_TEST_HANDLER_MEMORY_RECOVERY_BRIDGE_VS_SCRUBBER_CHILLER_LOW_MFE_FALSE_STAGE2_AND_CVD_EQUIPMENT_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "memory_recovery_order_cycle_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["memory_recovery_equipment_positive", "scrubber_chiller_false_stage2", "CVD_memory_recovery_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C10 rows need explicit customer order, delivery visibility, fab utilization, equipment mix, ASP/mix, margin or revision bridge before positive promotion.
- In C10, bridge-missing memory recovery equipment-cycle event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C10 memory recovery equipment cycle rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R2
completed_loop = 98
completed_canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 0 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
