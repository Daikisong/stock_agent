# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = MEMORY_TESTER_ORDER_CYCLE_BRIDGE_VS_OSAT_TEST_RECOVERY_FALSE_STAGE2_AND_TEST_OUTSOURCING_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_95_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R1 loop 95 is R2 / loop 95. R2 is the L2 AI/semiconductor/electronics round, and this run fills C10 memory recovery equipment cycle rather than repeating the immediately preceding R2 loop 94 C07 HBM-equipment file.

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
scheduled_loop = 95
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
round_sector_consistency = pass
computed_next_round = R3
computed_next_loop = 95
```

C10 is a memory-cycle-to-equipment-earnings bridge. A memory recovery label is only the wave; the surfboard is customer order visibility, delivery cadence, capacity pull-in, utilization, ASP/mix, margin and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE = 29 rows / 18 symbols / good-bad Stage2 15-5 / 4B-4C 1-0
top covered symbols include 089970(3), 281820(3), 319660(3), 042700(2), 064290(2), 079370(2)
previous R2 loop-93 C10 symbols avoided: 003160, 036540, 031980
previous R2 loop-94 C07 symbols avoided: 089030, 253590, 425420
previous R1 loop-95 C02 symbols avoided: 267260, 237750, 017510
```

Selected rows avoid hard duplicates and top repeated C10 symbols:

```text
232140 / Stage2-Actionable / 2024-02-28
330860 / Stage2-Actionable / 2024-02-22
200470 / Stage4B / 2024-06-04
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
| 232140 | atlas/symbol_profiles/232/232140.json | selected 2024 window clean after old 2017 CA candidate and 2024 rename continuity |
| 330860 | atlas/symbol_profiles/330/330860.json | no corporate-action candidate |
| 200470 | atlas/symbol_profiles/200/200470.json | selected 2024 window clean after old 2022 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L95_C10_YC_2024_MEMORY_TESTER_ORDER_CYCLE_POSITIVE | 232140 | 2024-02-28 | yes | 180 | yes | yes | true |
| R2L95_C10_NEPESARK_2024_OSAT_TEST_RECOVERY_FALSE_STAGE2 | 330860 | 2024-02-22 | yes | 180 | yes | yes | true |
| R2L95_C10_AFACT_2024_TEST_OUTSOURCING_MEMORY_EVENT_CAP_4B | 200470 | 2024-06-04 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | MEMORY_TESTER_ORDER_CYCLE_BRIDGE | Positive Stage2 requires memory tester customer order visibility, delivery cadence, capacity pull-in, utilization, margin and revision bridge. |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | OSAT_TEST_RECOVERY_FALSE_STAGE2 | OSAT/test recovery watch without customer order and utilization bridge can become false Stage2. |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | TEST_OUTSOURCING_EVENT_CAP_4B | Test-outsourcing memory recovery event premium should route to 4B when order/utilization/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L95_C10_YC_2024_MEMORY_TESTER_ORDER_CYCLE_POSITIVE | 232140 | 와이씨 | positive | Memory-tester customer order cycle produced extreme MFE with controlled early MAE. |
| R2L95_C10_NEPESARK_2024_OSAT_TEST_RECOVERY_FALSE_STAGE2 | 330860 | 네패스아크 | counterexample | OSAT/test recovery watch had temporary MFE but later severe MAE. |
| R2L95_C10_AFACT_2024_TEST_OUTSOURCING_MEMORY_EVENT_CAP_4B | 200470 | 에이팩트 | counterexample / 4B | Test-outsourcing memory recovery premium capped on the June spike and then de-rated. |

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
| YC memory tester order-cycle bridge | historical public/report proxy | true | true | shadow-only positive |
| Nepes Ark OSAT/test recovery false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Afact test-outsourcing event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 232140 | atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv | atlas/symbol_profiles/232/232140.json |
| 330860 | atlas/ohlcv_tradable_by_symbol_year/330/330860/2024.csv | atlas/symbol_profiles/330/330860.json |
| 200470 | atlas/ohlcv_tradable_by_symbol_year/200/200470/2024.csv | atlas/symbol_profiles/200/200470.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L95_C10_YC_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_ORDER_CYCLE_BRIDGE | 232140 | Stage2-Actionable | 2024-02-28 | 6690 | positive | memory tester order-cycle bridge worked |
| R2L95_C10_NEPESARK_2024_STAGE2_FALSE_POSITIVE_OSAT_TEST_RECOVERY_WATCH | 330860 | Stage2-Actionable | 2024-02-22 | 39150 | counterexample | OSAT/test recovery false Stage2 |
| R2L95_C10_AFACT_2024_STAGE4B_TEST_OUTSOURCING_MEMORY_EVENT_CAP | 200470 | Stage4B | 2024-06-04 | 7250 | counterexample/4B | test-outsourcing memory event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L95_C10_YC_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_ORDER_CYCLE_BRIDGE | 6690 | 26.61 | -7.77 | 243.05 | -7.77 | 243.05 | -7.77 | 2024-06-13 | 22950 | -38.52 |
| R2L95_C10_NEPESARK_2024_STAGE2_FALSE_POSITIVE_OSAT_TEST_RECOVERY_WATCH | 39150 | 18.52 | -17.50 | 18.52 | -51.39 | 18.52 | -51.39 | 2024-03-12 | 46400 | -58.99 |
| R2L95_C10_AFACT_2024_STAGE4B_TEST_OUTSOURCING_MEMORY_EVENT_CAP | 7250 | 0.00 | -26.48 | 0.00 | -36.69 | 0.00 | -36.69 | 2024-06-04 | 7250 | -36.69 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C10 Stage2 needs memory tester/customer order / delivery / utilization / margin / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing OSAT/test-outsourcing event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE memory-test rows cannot promote without durable customer/order bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether memory recovery becomes customer order and utilization.

| symbol | stage quality | explanation |
|---|---|---|
| 232140 | good_stage2_with_later_watch | Memory tester order-cycle bridge produced extreme MFE with controlled early MAE. |
| 330860 | bad_stage2 | OSAT/test recovery watch lacked customer order/utilization bridge and later suffered severe MAE. |
| 200470 | good_4B | Test-outsourcing memory premium capped on the June event spike and then drew down sharply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 330860 OSAT/test recovery false Stage2 | 0.84 | 0.84 | false Stage2 due missing customer order/utilization/margin bridge |
| 200470 test-outsourcing event cap | 1.00 | 1.00 | good full-window 4B timing after June memory-test event spike |
| 232140 memory tester order bridge | n/a | n/a | positive Stage2, but later memory-tester valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 330860 / 200470
```

No hard 4C candidate is proposed. R2 loop 95 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 memory-recovery equipment-cycle cases, Stage2 requires verified customer order visibility, tester delivery cadence, capacity pull-in, utilization recovery, ASP/mix, margin, or revision bridge. Memory recovery, HBM, OSAT, tester, outsourcing, equipment or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
rule = C10 should split true memory-tester order/utilization positives from OSAT recovery false Stage2 and test-outsourcing event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 87.19 | -31.95 | 0.67 | mixed; C10 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 87.19 | -31.95 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L2 customer/order/utilization bridge required | 2 | 130.79 | -29.58 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C10 bridge vs event-cap split | 2 | 130.79 | -29.58 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing memory-test themes as positive | 1 | 243.05 | -7.77 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 232140 memory tester order bridge | 66 | Stage2-Watch | 80 | Stage2-Actionable | 243.05 | -7.77 | memory_tester_order_cycle_positive |
| 330860 OSAT/test false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 18.52 | -51.39 | OSAT_test_recovery_false_stage2 |
| 200470 test-outsourcing cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 0.00 | -36.69 | test_outsourcing_memory_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_ORDER_CYCLE_BRIDGE_VS_OSAT_TEST_RECOVERY_FALSE_STAGE2_AND_TEST_OUTSOURCING_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C10 YC memory-tester order-cycle positive, Nepes Ark OSAT/test recovery false Stage2, and Afact test-outsourcing memory event-cap 4B split while avoiding top repeated C10 symbols and previous R2 loop93~94 symbols."}
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
residual_error_types_found: memory_tester_order_cycle_positive, OSAT_test_recovery_false_stage2, test_outsourcing_memory_event_cap_4B
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
- C10 memory recovery equipment cycle bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,configured,C10_requires_memory_tester_order_customer_delivery_utilization_margin_revision_bridge,0,"C10 Stage2 should require memory tester/customer order visibility, delivery cadence, capacity pull-in, utilization, margin, or revision bridge, not memory recovery or tester label alone","YC positive worked; Nepes Ark and Afact event/watch rows failed positive-stage promotion","R2L95_C10_YC_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_ORDER_CYCLE_BRIDGE|R2L95_C10_NEPESARK_2024_STAGE2_FALSE_POSITIVE_OSAT_TEST_RECOVERY_WATCH|R2L95_C10_AFACT_2024_STAGE4B_TEST_OUTSOURCING_MEMORY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,configured,cap_bridge_missing_OSAT_test_and_test_outsourcing_event_premiums_as_4B_watch,0,"Memory-test outsourcing and OSAT recovery premiums can peak before customer order, utilization and margin bridge is proven","Nepes Ark had temporary MFE then severe MAE; Afact showed clean 4B event-cap behavior after the June memory-test spike","R2L95_C10_NEPESARK_2024_STAGE2_FALSE_POSITIVE_OSAT_TEST_RECOVERY_WATCH|R2L95_C10_AFACT_2024_STAGE4B_TEST_OUTSOURCING_MEMORY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,configured,block_positive_stage_when_memory_test_theme_has_high_or_persistent_MAE_without_order_margin_bridge,0,"High or persistent MAE after bridge-missing memory-test entries should block Stage2/Stage3 promotion unless customer, delivery, utilization and margin evidence survives","Nepes Ark MAE90=-51.39 and Afact MAE90=-36.69","R2L95_C10_NEPESARK_2024_STAGE2_FALSE_POSITIVE_OSAT_TEST_RECOVERY_WATCH|R2L95_C10_AFACT_2024_STAGE4B_TEST_OUTSOURCING_MEMORY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L95_C10_YC_2024_MEMORY_TESTER_ORDER_CYCLE_POSITIVE", "symbol": "232140", "company_name": "와이씨", "round": "R2", "loop": "95", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_ORDER_CYCLE_BRIDGE_VS_OSAT_TEST_RECOVERY_FALSE_STAGE2_AND_TEST_OUTSOURCING_EVENT_CAP", "case_type": "structural_success_with_later_memory_tester_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R2L95_C10_YC_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_ORDER_CYCLE_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Memory tester / HBM-related customer order cycle bridge produced very high 30D/90D/180D MFE with controlled early MAE. C10 works when memory recovery narrative maps into confirmed customer order visibility, tester delivery cadence, customer capacity pull-in, utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C10_positive_requires_memory_tester_order_customer_delivery_margin_revision_bridge_not_memory_recovery_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2017 corporate-action candidate and 2024 rename continuity. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R2L95_C10_NEPESARK_2024_OSAT_TEST_RECOVERY_FALSE_STAGE2", "symbol": "330860", "company_name": "네패스아크", "round": "R2", "loop": "95", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_ORDER_CYCLE_BRIDGE_VS_OSAT_TEST_RECOVERY_FALSE_STAGE2_AND_TEST_OUTSOURCING_EVENT_CAP", "case_type": "failed_rerating_OSAT_test_recovery_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R2L95_C10_NEPESARK_2024_STAGE2_FALSE_POSITIVE_OSAT_TEST_RECOVERY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "OSAT/test recovery watch had a temporary rebound but later suffered severe 90D/180D MAE. C10 Stage2 should not be awarded without confirmed tester/customer order, utilization recovery, delivery schedule, pricing/mix, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_OSAT_test_recovery_watch_counts_without_customer_order_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R2L95_C10_AFACT_2024_TEST_OUTSOURCING_MEMORY_EVENT_CAP_4B", "symbol": "200470", "company_name": "에이팩트", "round": "R2", "loop": "95", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_ORDER_CYCLE_BRIDGE_VS_OSAT_TEST_RECOVERY_FALSE_STAGE2_AND_TEST_OUTSOURCING_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L95_C10_AFACT_2024_STAGE4B_TEST_OUTSOURCING_MEMORY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Test-outsourcing / memory recovery event premium capped on the June spike and then de-rated. C10 should route bridge-missing memory-test outsourcing event premiums to 4B unless confirmed customer order recovery, utilization, ASP/mix, delivery and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_memory_test_outsourcing_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2022 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L95_C10_YC_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_ORDER_CYCLE_BRIDGE", "case_id": "R2L95_C10_YC_2024_MEMORY_TESTER_ORDER_CYCLE_POSITIVE", "symbol": "232140", "company_name": "와이씨", "round": "R2", "loop": "95", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_ORDER_CYCLE_BRIDGE_VS_OSAT_TEST_RECOVERY_FALSE_STAGE2_AND_TEST_OUTSOURCING_EVENT_CAP", "sector": "memory_tester_order_cycle_HBM_capacity_pullin", "primary_archetype": "memory_tester_order_customer_delivery_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-28", "entry_date": "2024-02-28", "entry_price": 6690.0, "evidence_available_at_that_date": "memory tester / HBM customer order cycle, capacity pull-in, tester delivery cadence, utilization and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["memory_tester_order_visibility_proxy", "HBM_customer_capacity_proxy", "delivery_cadence_proxy", "utilization_margin_bridge_proxy", "revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "extreme_MFE90", "extreme_MFE180", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_memory_tester_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "profile_path": "atlas/symbol_profiles/232/232140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 26.61, "MFE_90D_pct": 243.05, "MFE_180D_pct": 243.05, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.77, "MAE_90D_pct": -7.77, "MAE_180D_pct": -7.77, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 22950.0, "drawdown_after_peak_pct": -38.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_memory_tester_valuation_4B_watch_needed", "four_b_evidence_type": ["memory_tester_order_bridge", "customer_capacity_cycle", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_memory_tester_order_cycle_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2017_CA_and_2024_rename_continuity", "same_entry_group_id": "R2L95_C10_232140_2024-02-28_6690", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L95_C10_NEPESARK_2024_STAGE2_FALSE_POSITIVE_OSAT_TEST_RECOVERY_WATCH", "case_id": "R2L95_C10_NEPESARK_2024_OSAT_TEST_RECOVERY_FALSE_STAGE2", "symbol": "330860", "company_name": "네패스아크", "round": "R2", "loop": "95", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_ORDER_CYCLE_BRIDGE_VS_OSAT_TEST_RECOVERY_FALSE_STAGE2_AND_TEST_OUTSOURCING_EVENT_CAP", "sector": "OSAT_memory_test_recovery_watch", "primary_archetype": "OSAT_test_recovery_without_customer_order_utilization_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 39150.0, "evidence_available_at_that_date": "OSAT/test recovery and memory-test utilization watch without confirmed customer order, delivery schedule or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["OSAT_test_recovery_watch", "memory_test_utilization_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["temporary_MFE_then_deep_MAE", "customer_order_utilization_margin_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/330/330860/2024.csv", "profile_path": "atlas/symbol_profiles/330/330860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.52, "MFE_90D_pct": 18.52, "MFE_180D_pct": 18.52, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -17.5, "MAE_90D_pct": -51.39, "MAE_180D_pct": -51.39, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-12", "peak_price": 46400.0, "drawdown_after_peak_pct": -58.99, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.84, "four_b_full_window_peak_proximity": 0.84, "four_b_timing_verdict": "OSAT_test_recovery_watch_was_false_stage2_due_missing_customer_order_utilization_margin_bridge", "four_b_evidence_type": ["OSAT_test_recovery_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_OSAT_test_recovery_without_customer_order_utilization_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_OSAT_test_recovery_watch_counts_without_customer_order_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R2L95_C10_330860_2024-02-22_39150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L95_C10_AFACT_2024_STAGE4B_TEST_OUTSOURCING_MEMORY_EVENT_CAP", "case_id": "R2L95_C10_AFACT_2024_TEST_OUTSOURCING_MEMORY_EVENT_CAP_4B", "symbol": "200470", "company_name": "에이팩트", "round": "R2", "loop": "95", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_ORDER_CYCLE_BRIDGE_VS_OSAT_TEST_RECOVERY_FALSE_STAGE2_AND_TEST_OUTSOURCING_EVENT_CAP", "sector": "test_outsourcing_memory_recovery_event_premium", "primary_archetype": "test_outsourcing_memory_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-04", "entry_date": "2024-06-04", "entry_price": 7250.0, "evidence_available_at_that_date": "test-outsourcing / memory recovery event premium after June spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["memory_test_outsourcing_event", "memory_recovery_beta", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "customer_order_utilization_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/200/200470/2024.csv", "profile_path": "atlas/symbol_profiles/200/200470.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "MFE_180D_pct": 0.0, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -26.48, "MAE_90D_pct": -36.69, "MAE_180D_pct": -36.69, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-04", "peak_price": 7250.0, "drawdown_after_peak_pct": -36.69, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_test_outsourcing_memory_event_cap", "four_b_evidence_type": ["memory_test_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_test_outsourcing_memory_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_memory_test_outsourcing_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_CA", "same_entry_group_id": "R2L95_C10_200470_2024-06-04_7250", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L95_C10_YC_2024_MEMORY_TESTER_ORDER_CYCLE_POSITIVE", "trigger_id": "R2L95_C10_YC_2024_STAGE2_ACTIONABLE_MEMORY_TESTER_ORDER_CYCLE_BRIDGE", "symbol": "232140", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 70, "margin_bridge_score": 65, "revision_score": 65, "relative_strength_score": 80, "customer_quality_score": 65, "policy_or_regulatory_score": 10, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "memory_tester_order_cycle_positive", "MFE_90D_pct": 243.05, "MAE_90D_pct": -7.77, "score_return_alignment_label": "memory_tester_order_cycle_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L95_C10_NEPESARK_2024_OSAT_TEST_RECOVERY_FALSE_STAGE2", "trigger_id": "R2L95_C10_NEPESARK_2024_STAGE2_FALSE_POSITIVE_OSAT_TEST_RECOVERY_WATCH", "symbol": "330860", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "OSAT_test_recovery_false_stage2", "MFE_90D_pct": 18.52, "MAE_90D_pct": -51.39, "score_return_alignment_label": "OSAT_test_recovery_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_OSAT_test_recovery_watch_counts_without_customer_order_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L95_C10_AFACT_2024_TEST_OUTSOURCING_MEMORY_EVENT_CAP_4B", "trigger_id": "R2L95_C10_AFACT_2024_STAGE4B_TEST_OUTSOURCING_MEMORY_EVENT_CAP", "symbol": "200470", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "test_outsourcing_memory_event_cap_4B_guard", "MFE_90D_pct": 0.0, "MAE_90D_pct": -36.69, "score_return_alignment_label": "test_outsourcing_memory_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_memory_test_outsourcing_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "95", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_TESTER_ORDER_CYCLE_BRIDGE_VS_OSAT_TEST_RECOVERY_FALSE_STAGE2_AND_TEST_OUTSOURCING_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["memory_tester_order_cycle_positive", "OSAT_test_recovery_false_stage2", "test_outsourcing_memory_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C10 rows need explicit customer order visibility, tester delivery cadence, capacity pull-in, utilization, ASP/mix, margin or revision bridge before positive promotion.
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
completed_loop = 95
next_round = R3
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
