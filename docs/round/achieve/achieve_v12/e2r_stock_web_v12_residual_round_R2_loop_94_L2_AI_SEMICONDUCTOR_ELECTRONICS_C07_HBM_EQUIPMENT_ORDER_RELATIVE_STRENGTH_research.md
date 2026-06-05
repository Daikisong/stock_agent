# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE_VS_MEMORY_TESTER_HEADLINE_FALSE_STAGE2_AND_SOCKET_PACKAGE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_94_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
```

This file is the corrected final output for this execution. The scheduler state after R1 loop 94 is R2 / loop 94. R2 is the L2 AI/semiconductor/electronics round, and this run fills C07 HBM equipment order relative-strength behavior while avoiding the previous R2 loop 93 C10 memory-cycle file and top repeated C07 symbols.

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
scheduled_loop = 94
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
round_sector_consistency = pass
computed_next_round = R3
computed_next_loop = 94
```

C07 is not just a price-strength bucket. The useful residual split is whether HBM equipment strength is anchored to customer orders, delivery and margin bridge, or is only a headline/event premium.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH = 11 rows / 9 symbols / good-bad Stage2 7-0 / 4B-4C 1-0
top covered symbols include 042700(2), 064760(2), 003160(1), 036200(1), 036540(1), 039440(1)
previous R2 loop-90 C07 symbols avoided: prior C07 family
previous R2 loop-91 C06 symbols avoided: C06 family
previous R2 loop-92 C08 symbols avoided: C08 family
previous R2 loop-93 C10 symbols avoided: 003160, 036540, 031980
previous R1 loop-94 C03 symbols avoided: 077970, 361390, 024740
```

Selected rows avoid hard duplicates and top repeated C07 symbols:

```text
089030 / Stage2-Actionable / 2024-02-14
253590 / Stage2-Actionable / 2024-03-20
425420 / Stage4B / 2024-03-20
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
| 253590 | atlas/symbol_profiles/253/253590.json | selected 2024 window clean after old 2019 CA candidate |
| 425420 | atlas/symbol_profiles/425/425420.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L94_C07_TECHWING_2024_HBM_TEST_HANDLER_ORDER_CAPACITY_POSITIVE | 089030 | 2024-02-14 | yes | 180 | yes | yes | true |
| R2L94_C07_NEOSEM_2024_MEMORY_TESTER_HEADLINE_FALSE_STAGE2 | 253590 | 2024-03-20 | yes | 180 | yes | yes | true |
| R2L94_C07_TFE_2024_HBM_SOCKET_PACKAGE_EVENT_CAP_4B | 425420 | 2024-03-20 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE | Positive Stage2 requires customer order, HBM capacity pull-in, delivery cadence, utilization, margin and revision bridge. |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | MEMORY_TESTER_HEADLINE_FALSE_STAGE2 | Memory/HBM tester headline without customer order and delivery bridge can become false Stage2. |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | SOCKET_PACKAGE_EVENT_CAP_4B | HBM socket/package event premium should route to 4B when qualification/order/margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L94_C07_TECHWING_2024_HBM_TEST_HANDLER_ORDER_CAPACITY_POSITIVE | 089030 | 테크윙 | positive | HBM test-handler order/capacity bridge produced very high MFE with controlled MAE. |
| R2L94_C07_NEOSEM_2024_MEMORY_TESTER_HEADLINE_FALSE_STAGE2 | 253590 | 네오셈 | counterexample | Tester headline rebound had tiny MFE and severe MAE without delivery/margin bridge. |
| R2L94_C07_TFE_2024_HBM_SOCKET_PACKAGE_EVENT_CAP_4B | 425420 | 티에프이 | counterexample / 4B | HBM socket/package premium capped near the March spike and then de-rated deeply. |

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
| Techwing HBM test-handler order/capacity bridge | historical public/report proxy | true | true | shadow-only positive |
| NeoSem memory tester headline false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| TFE HBM socket/package event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 089030 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json |
| 253590 | atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv | atlas/symbol_profiles/253/253590.json |
| 425420 | atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv | atlas/symbol_profiles/425/425420.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L94_C07_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE | 089030 | Stage2-Actionable | 2024-02-14 | 18900 | positive | HBM test-handler order/capacity bridge worked |
| R2L94_C07_NEOSEM_2024_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_HEADLINE | 253590 | Stage2-Actionable | 2024-03-20 | 15810 | counterexample | memory tester headline false Stage2 |
| R2L94_C07_TFE_2024_STAGE4B_HBM_SOCKET_PACKAGE_EVENT_CAP | 425420 | Stage4B | 2024-03-20 | 43100 | counterexample/4B | HBM socket/package event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L94_C07_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE | 18900 | 90.48 | -7.09 | 139.15 | -7.09 | 274.60 | -7.09 | 2024-07-11 | 70800 | -53.18 |
| R2L94_C07_NEOSEM_2024_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_HEADLINE | 15810 | 2.09 | -32.01 | 9.23 | -40.86 | 9.23 | -40.86 | 2024-07-04 | 17270 | -46.73 |
| R2L94_C07_TFE_2024_STAGE4B_HBM_SOCKET_PACKAGE_EVENT_CAP | 43100 | 1.97 | -21.81 | 1.97 | -49.54 | 1.97 | -65.85 | 2024-03-21 | 43950 | -66.51 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C07 Stage2 needs HBM customer order / capacity / delivery / utilization / margin bridge |
| local_4b_watch_guard | strengthen: bridge-missing HBM equipment/socket event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE HBM equipment rows cannot promote without durable customer/order bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is HBM equipment bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 089030 | good_stage2_with_later_watch | HBM order/capacity bridge produced very high MFE, but later valuation watch remains necessary. |
| 253590 | bad_stage2 | Memory tester headline had tiny sustainable MFE and severe MAE without customer/order bridge. |
| 425420 | good_4B | HBM socket/package premium capped near the March spike and then de-rated deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 253590 memory tester false Stage2 | 0.92 | 0.92 | false Stage2 due missing customer order/delivery/margin bridge |
| 425420 HBM socket/package cap | 0.98 | 0.98 | good full-window 4B timing after March event spike |
| 089030 HBM handler bridge | n/a | n/a | positive Stage2, but later HBM equipment valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 253590 / 425420
```

No hard 4C candidate is proposed. R2 loop 94 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 HBM equipment relative-strength cases, Stage2 requires verified HBM customer order, capacity expansion, equipment delivery cadence, utilization, customer quality, margin, or revision bridge. HBM, tester, socket, package, equipment, memory or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
rule = C07 should split true HBM order/capacity/delivery positives from memory-tester headline false Stage2 and HBM socket/package event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 50.12 | -32.50 | 0.67 | mixed; C07 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 50.12 | -32.50 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L2 customer/order/delivery bridge required | 2 | 74.19 | -23.98 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C07 bridge vs event-cap split | 2 | 74.19 | -23.98 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing HBM equipment headlines as positive | 1 | 139.15 | -7.09 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 089030 HBM handler bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 139.15 | -7.09 | HBM_test_handler_order_capacity_positive |
| 253590 tester headline false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 9.23 | -40.86 | memory_tester_headline_false_stage2 |
| 425420 socket/package cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.97 | -49.54 | HBM_socket_package_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE_VS_MEMORY_TESTER_HEADLINE_FALSE_STAGE2_AND_SOCKET_PACKAGE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C07 HBM test-handler order/capacity positive, memory-tester headline false Stage2, and HBM socket/package event-cap 4B split while avoiding top repeated C07 symbols."}
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
residual_error_types_found: HBM_test_handler_order_capacity_positive, memory_tester_headline_false_stage2, HBM_socket_package_event_cap_4B
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
- C07 HBM equipment order relative-strength bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,configured,C07_requires_HBM_customer_order_capacity_delivery_utilization_margin_revision_bridge,0,"C07 Stage2 should require HBM customer/order visibility, equipment delivery cadence, capacity pull-in, utilization, margin, or revision bridge, not HBM/equipment/headline relative strength alone","Techwing positive worked; NeoSem and TFE event/headline rows failed positive-stage promotion","R2L94_C07_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE|R2L94_C07_NEOSEM_2024_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_HEADLINE|R2L94_C07_TFE_2024_STAGE4B_HBM_SOCKET_PACKAGE_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,configured,cap_bridge_missing_HBM_equipment_socket_event_premiums_as_4B_watch,0,"HBM equipment/socket event premiums can peak before customer order, delivery and margin bridge is proven","NeoSem had tiny sustainable MFE and severe MAE; TFE showed clean 4B event-cap behavior after March HBM socket spike","R2L94_C07_NEOSEM_2024_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_HEADLINE|R2L94_C07_TFE_2024_STAGE4B_HBM_SOCKET_PACKAGE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,configured,block_positive_stage_when_HBM_equipment_headline_has_high_MAE_without_order_margin_bridge,0,"High or persistent MAE after bridge-missing HBM equipment/socket entries should block Stage2/Stage3 promotion unless customer, delivery, utilization and margin evidence survives","NeoSem MAE90=-40.86 and TFE MAE90=-49.54","R2L94_C07_NEOSEM_2024_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_HEADLINE|R2L94_C07_TFE_2024_STAGE4B_HBM_SOCKET_PACKAGE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L94_C07_TECHWING_2024_HBM_TEST_HANDLER_ORDER_CAPACITY_POSITIVE", "symbol": "089030", "company_name": "테크윙", "round": "R2", "loop": "94", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE_VS_MEMORY_TESTER_HEADLINE_FALSE_STAGE2_AND_SOCKET_PACKAGE_EVENT_CAP", "case_type": "structural_success_with_later_HBM_equipment_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R2L94_C07_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "HBM test-handler / customer-capacity / equipment-order bridge produced very high 30D/90D/180D MFE with controlled entry MAE. C07 works when HBM equipment relative strength maps into customer capacity expansion, order visibility, delivery cadence, utilization and margin/revision bridge.", "current_profile_verdict": "current_profile_kept_but_C07_positive_requires_HBM_customer_order_capacity_delivery_margin_bridge_not_equipment_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2011/2022 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R2L94_C07_NEOSEM_2024_MEMORY_TESTER_HEADLINE_FALSE_STAGE2", "symbol": "253590", "company_name": "네오셈", "round": "R2", "loop": "94", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE_VS_MEMORY_TESTER_HEADLINE_FALSE_STAGE2_AND_SOCKET_PACKAGE_EVENT_CAP", "case_type": "failed_rerating_memory_tester_headline_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R2L94_C07_NEOSEM_2024_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_HEADLINE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Memory-tester / HBM tester headline rebound had only tiny sustainable MFE and then severe 30D/90D/180D MAE. C07 Stage2 should not be awarded without explicit customer order, tester delivery schedule, capacity pull-in, utilization and margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_memory_tester_headline_counts_without_customer_order_delivery_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2019 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R2L94_C07_TFE_2024_HBM_SOCKET_PACKAGE_EVENT_CAP_4B", "symbol": "425420", "company_name": "티에프이", "round": "R2", "loop": "94", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE_VS_MEMORY_TESTER_HEADLINE_FALSE_STAGE2_AND_SOCKET_PACKAGE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L94_C07_TFE_2024_STAGE4B_HBM_SOCKET_PACKAGE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "HBM socket/package-test event premium capped near the March spike and then suffered deep 90D/180D MAE. C07 should route bridge-missing HBM parts/socket event premiums to 4B unless customer order, qualification, delivery cadence, utilization and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_HBM_socket_package_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L94_C07_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE", "case_id": "R2L94_C07_TECHWING_2024_HBM_TEST_HANDLER_ORDER_CAPACITY_POSITIVE", "symbol": "089030", "company_name": "테크윙", "round": "R2", "loop": "94", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE_VS_MEMORY_TESTER_HEADLINE_FALSE_STAGE2_AND_SOCKET_PACKAGE_EVENT_CAP", "sector": "HBM_test_handler_equipment_order_capacity", "primary_archetype": "HBM_customer_order_capacity_delivery_utilization_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-14", "entry_date": "2024-02-14", "entry_price": 18900.0, "evidence_available_at_that_date": "HBM test-handler customer capacity expansion, equipment order visibility, delivery cadence, utilization and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["HBM_customer_capacity_proxy", "equipment_order_visibility_proxy", "delivery_cadence_proxy", "utilization_margin_bridge_proxy", "relative_strength_confirmation"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "very_high_MFE180", "controlled_initial_MAE"], "stage4b_evidence_fields": ["later_HBM_equipment_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv", "profile_path": "atlas/symbol_profiles/089/089030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 90.48, "MFE_90D_pct": 139.15, "MFE_180D_pct": 274.6, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.09, "MAE_90D_pct": -7.09, "MAE_180D_pct": -7.09, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 70800.0, "drawdown_after_peak_pct": -53.18, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_HBM_equipment_valuation_4B_watch_needed", "four_b_evidence_type": ["HBM_equipment_order_bridge", "relative_strength", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_HBM_test_handler_order_capacity_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2011_2022_CA", "same_entry_group_id": "R2L94_C07_089030_2024-02-14_18900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L94_C07_NEOSEM_2024_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_HEADLINE", "case_id": "R2L94_C07_NEOSEM_2024_MEMORY_TESTER_HEADLINE_FALSE_STAGE2", "symbol": "253590", "company_name": "네오셈", "round": "R2", "loop": "94", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE_VS_MEMORY_TESTER_HEADLINE_FALSE_STAGE2_AND_SOCKET_PACKAGE_EVENT_CAP", "sector": "memory_tester_HBM_headline_rebound", "primary_archetype": "memory_tester_headline_without_customer_order_delivery_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-20", "entry_date": "2024-03-20", "entry_price": 15810.0, "evidence_available_at_that_date": "memory/HBM tester headline rebound and relative-strength watch without confirmed customer order, delivery schedule or margin bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["memory_tester_headline", "HBM_tester_expectation", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tiny_MFE30", "deep_MAE90", "customer_order_delivery_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv", "profile_path": "atlas/symbol_profiles/253/253590.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.09, "MFE_90D_pct": 9.23, "MFE_180D_pct": 9.23, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -32.01, "MAE_90D_pct": -40.86, "MAE_180D_pct": -40.86, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-04", "peak_price": 17270.0, "drawdown_after_peak_pct": -46.73, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "memory_tester_headline_was_false_stage2_due_missing_customer_order_delivery_margin_bridge", "four_b_evidence_type": ["memory_tester_headline_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_memory_tester_headline_without_customer_order_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_memory_tester_headline_counts_without_customer_order_delivery_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2019_CA", "same_entry_group_id": "R2L94_C07_253590_2024-03-20_15810", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L94_C07_TFE_2024_STAGE4B_HBM_SOCKET_PACKAGE_EVENT_CAP", "case_id": "R2L94_C07_TFE_2024_HBM_SOCKET_PACKAGE_EVENT_CAP_4B", "symbol": "425420", "company_name": "티에프이", "round": "R2", "loop": "94", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE_VS_MEMORY_TESTER_HEADLINE_FALSE_STAGE2_AND_SOCKET_PACKAGE_EVENT_CAP", "sector": "HBM_socket_package_test_event_premium", "primary_archetype": "HBM_socket_package_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-20", "entry_date": "2024-03-20", "entry_price": 43100.0, "evidence_available_at_that_date": "HBM socket/package-test event premium after March spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["HBM_socket_package_event", "test_socket_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE90", "customer_qualification_order_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv", "profile_path": "atlas/symbol_profiles/425/425420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.97, "MFE_90D_pct": 1.97, "MFE_180D_pct": 1.97, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -21.81, "MAE_90D_pct": -49.54, "MAE_180D_pct": -65.85, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-21", "peak_price": 43950.0, "drawdown_after_peak_pct": -66.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_HBM_socket_package_event_cap", "four_b_evidence_type": ["HBM_socket_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_HBM_socket_package_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_HBM_socket_package_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R2L94_C07_425420_2024-03-20_43100", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L94_C07_TECHWING_2024_HBM_TEST_HANDLER_ORDER_CAPACITY_POSITIVE", "trigger_id": "R2L94_C07_TECHWING_2024_STAGE2_ACTIONABLE_HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE", "symbol": "089030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 75, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 70, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 75, "customer_quality_score": 60, "policy_or_regulatory_score": 10, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "HBM_test_handler_order_capacity_positive", "MFE_90D_pct": 139.15, "MAE_90D_pct": -7.09, "score_return_alignment_label": "HBM_test_handler_order_capacity_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L94_C07_NEOSEM_2024_MEMORY_TESTER_HEADLINE_FALSE_STAGE2", "trigger_id": "R2L94_C07_NEOSEM_2024_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_HEADLINE", "symbol": "253590", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 75, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "memory_tester_headline_false_stage2", "MFE_90D_pct": 9.23, "MAE_90D_pct": -40.86, "score_return_alignment_label": "memory_tester_headline_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_memory_tester_headline_counts_without_customer_order_delivery_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L94_C07_TFE_2024_HBM_SOCKET_PACKAGE_EVENT_CAP_4B", "trigger_id": "R2L94_C07_TFE_2024_STAGE4B_HBM_SOCKET_PACKAGE_EVENT_CAP", "symbol": "425420", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 75, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "HBM_socket_package_event_cap_4B_guard", "MFE_90D_pct": 1.97, "MAE_90D_pct": -49.54, "score_return_alignment_label": "HBM_socket_package_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_HBM_socket_package_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "94", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_HANDLER_ORDER_CAPACITY_BRIDGE_VS_MEMORY_TESTER_HEADLINE_FALSE_STAGE2_AND_SOCKET_PACKAGE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["HBM_test_handler_order_capacity_positive", "memory_tester_headline_false_stage2", "HBM_socket_package_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C07 rows need explicit HBM customer/order, capacity, delivery, utilization, customer quality or margin bridge before positive promotion.
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
10. Add tests that bridge-missing C07 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 94
next_round = R3
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
