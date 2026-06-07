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
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_TESTER_POST_CA_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | HBM_equipment_order_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_98_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. A duplicate local C01 artifact was generated during the run but is not the final selection because C01 was already produced immediately before. After local C08/C09/C01 supplementation, C07 is the next thin Priority 0 archetype that has not just been finalized.

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
HBM_equipment_order_guardrail = existing_axis_strengthened
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
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C07 is a relative-strength to order-conversion archetype. Relative strength is only the smoke; the usable signal is confirmed when customer order, delivery, utilization, margin and revision are the fire underneath.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH = 18 rows / Priority 0
previous R2 loop-96 C08 symbols avoided: 424980, 098120, 080580
previous R2 loop-97 C06 symbols avoided: 031980, 036540, 080220
previous local C08/C09/C01 artifacts accounted for but not duplicated
```

Selected rows avoid hard duplicates and add new C07 trigger families:

```text
003160 / Stage2-Actionable / 2024-02-19
092870 / Stage2-Actionable / 2024-08-01
089790 / Stage4B / 2024-04-12
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
| 003160 | atlas/symbol_profiles/003/003160.json | selected 2024 window clean after old 1997/1998/1999 CA candidates |
| 092870 | atlas/symbol_profiles/092/092870.json | selected after 2024-07-31 CA candidate; post-CA forward window |
| 089790 | atlas/symbol_profiles/089/089790.json | selected 2024 window clean after old 2010 CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L98_C07_DI_2024_HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE_POSITIVE | 003160 | 2024-02-19 | yes | 180 | yes | yes | true |
| R2L98_C07_EXICON_2024_HBM_TESTER_POST_CA_LOW_MFE_FALSE_STAGE2 | 092870 | 2024-08-01 | yes | 180 | yes | post-CA clean | true |
| R2L98_C07_JT_2024_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP_4B | 089790 | 2024-04-12 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE | Positive Stage2 requires customer order, delivery, utilization, margin and revision bridge. |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | HBM_TESTER_POST_CA_FALSE_STAGE2 | Post-CA tester relative-strength watch without customer order/qualification bridge can become false Stage2. |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | TEST_HANDLER_EVENT_CAP_4B | Test-handler/HBM-equipment premium should route to 4B when qualification/reorder bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L98_C07_DI_2024_HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE_POSITIVE | 003160 | 디아이 | positive | HBM test-equipment order/relative-strength bridge produced very strong MFE with shallow early MAE. |
| R2L98_C07_EXICON_2024_HBM_TESTER_POST_CA_LOW_MFE_FALSE_STAGE2 | 092870 | 엑시콘 | counterexample | Post-CA HBM tester watch had low MFE and high MAE without customer-order/qualification bridge. |
| R2L98_C07_JT_2024_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP_4B | 089790 | 제이티 | counterexample / 4B | Test-handler/HBM equipment premium capped at the April spike and then de-rated. |

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
| DI HBM test-equipment order relative-strength bridge | historical public/news-report proxy | true | true | shadow-only positive |
| Exicon HBM tester post-CA false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| JT test-handler/HBM equipment event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 003160 | atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv | atlas/symbol_profiles/003/003160.json |
| 092870 | atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv | atlas/symbol_profiles/092/092870.json |
| 089790 | atlas/ohlcv_tradable_by_symbol_year/089/089790/2024.csv | atlas/symbol_profiles/089/089790.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L98_C07_DI_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE | 003160 | Stage2-Actionable | 2024-02-19 | 7160 | positive | HBM equipment order/relative-strength bridge worked |
| R2L98_C07_EXICON_2024_STAGE2_FALSE_POSITIVE_HBM_TESTER_POST_CA_RS_WATCH | 092870 | Stage2-Actionable | 2024-08-01 | 17840 | counterexample | post-CA HBM tester false Stage2 |
| R2L98_C07_JT_2024_STAGE4B_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP | 089790 | Stage4B | 2024-04-12 | 11040 | counterexample/4B | test-handler/HBM equipment event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L98_C07_DI_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE | 7160 | 95.95 | -0.28 | 157.96 | -0.28 | 157.96 | -0.28 | 2024-04-11 | 18470 | n/a |
| R2L98_C07_EXICON_2024_STAGE2_FALSE_POSITIVE_HBM_TESTER_POST_CA_RS_WATCH | 17840 | 7.57 | -38.06 | 7.57 | -41.70 | 7.57 | -41.70 | 2024-08-01 | 19190 | -45.81 |
| R2L98_C07_JT_2024_STAGE4B_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP | 11040 | 2.90 | -28.17 | 2.90 | -39.31 | 2.90 | -39.31 | 2024-04-12 | 11360 | -41.02 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C07 Stage2 needs customer order / qualification / delivery / utilization / margin / revision bridge |
| HBM_equipment_order_guardrail | strengthen: HBM equipment or relative-strength labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing tester and handler premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C07 rows cannot promote without durable order/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether HBM equipment relative strength becomes customer order, delivery and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 003160 | good_stage2_with_later_watch | Order/relative-strength bridge produced very strong MFE and shallow MAE, but later valuation watch remains necessary. |
| 092870 | bad_stage2 | Post-CA tester watch lacked customer-order/qualification bridge and produced low MFE with high MAE. |
| 089790 | good_4B | Test-handler event premium peaked immediately and later drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 092870 HBM tester post-CA false Stage2 | 0.93 | 0.93 | false Stage2 due missing customer order / qualification / utilization / margin bridge |
| 089790 test-handler HBM cap | 0.97 | 0.97 | good full-window 4B timing after test-handler/HBM equipment event premium |
| 003160 HBM equipment order bridge | n/a | n/a | positive Stage2, but later HBM equipment valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 092870 / 089790
```

No hard 4C candidate is introduced in this C07 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 HBM equipment order relative-strength cases, Stage2 requires verified customer order, qualification, delivery visibility, utilization, ASP/mix, margin, or revision bridge. HBM equipment, tester, handler, relative strength, AI semiconductor equipment or price breakout label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
rule = C07 should split true customer-order/delivery/utilization positives from post-CA tester false Stage2 and test-handler event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 56.14 | -27.10 | 0.67 | mixed; C07 bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 56.14 | -27.10 | 0.67 | weaker C07 bridge split |
| P1 sector_specific_candidate_profile | L2 HBM customer-order/delivery bridge required | 2 | 82.77 | -20.99 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C07 bridge vs event-cap split | 2 | 82.77 | -20.99 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing HBM equipment themes as positive | 1 | 157.96 | -0.28 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 003160 HBM equipment bridge | 66 | Stage2-Watch | 80 | Stage2-Actionable | 157.96 | -0.28 | HBM_equipment_order_RS_positive |
| 092870 HBM tester false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 7.57 | -41.70 | HBM_tester_RS_false_stage2 |
| 089790 test-handler cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.90 | -39.31 | test_handler_HBM_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_TESTER_POST_CA_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C07 is the next thin Priority 0 archetype after local C08/C09/C01 supplementation. This run adds DI, Exicon, and JT rows while avoiding recent R2 C08/C09 rows and top repeated C07 symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, HBM_equipment_order_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: HBM_equipment_order_RS_positive, HBM_tester_RS_false_stage2, test_handler_HBM_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, HBM_equipment_order_guardrail, high_MAE_guardrail
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
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,configured,C07_requires_customer_order_delivery_utilization_margin_revision_bridge,0,"C07 Stage2 should require customer order, qualification, delivery visibility, utilization, margin, or revision bridge, not HBM equipment/relative-strength label alone","DI positive worked; Exicon and JT event/watch rows failed positive-stage promotion","R2L98_C07_DI_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE|R2L98_C07_EXICON_2024_STAGE2_FALSE_POSITIVE_HBM_TESTER_POST_CA_RS_WATCH|R2L98_C07_JT_2024_STAGE4B_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,configured,cap_bridge_missing_HBM_tester_and_test_handler_event_premiums_as_4B_watch,0,"HBM tester and test-handler premiums can peak before customer qualification, repeat order, delivery, utilization and margin bridge is proven","Exicon had low MFE and high MAE after post-CA tester watch; JT showed 4B event-cap behavior after the April handler spike","R2L98_C07_EXICON_2024_STAGE2_FALSE_POSITIVE_HBM_TESTER_POST_CA_RS_WATCH|R2L98_C07_JT_2024_STAGE4B_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,configured,block_positive_stage_when_HBM_equipment_theme_has_high_or_persistent_MAE_without_order_bridge,0,"High or persistent MAE after bridge-missing C07 entries should block Stage2/Stage3 promotion unless customer order, delivery/utilization and margin evidence survives","Exicon MAE90=-41.70 and JT MAE90=-39.31","R2L98_C07_EXICON_2024_STAGE2_FALSE_POSITIVE_HBM_TESTER_POST_CA_RS_WATCH|R2L98_C07_JT_2024_STAGE4B_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L98_C07_DI_2024_HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE_POSITIVE", "symbol": "003160", "company_name": "디아이", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_TESTER_POST_CA_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "case_type": "structural_success_with_later_HBM_equipment_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R2L98_C07_DI_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "HBM test-equipment order/relative-strength bridge produced very strong forward MFE after the February breakout, with shallow initial MAE. C07 works when relative strength is tied to customer order, delivery, utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C07_positive_requires_customer_order_delivery_utilization_margin_revision_bridge_not_HBM_RS_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1997/1998/1999 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R2L98_C07_EXICON_2024_HBM_TESTER_POST_CA_LOW_MFE_FALSE_STAGE2", "symbol": "092870", "company_name": "엑시콘", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_TESTER_POST_CA_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "case_type": "failed_rerating_HBM_tester_post_CA_order_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R2L98_C07_EXICON_2024_STAGE2_FALSE_POSITIVE_HBM_TESTER_POST_CA_RS_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "HBM tester / post-CA relative-strength watch after the July reset had only small MFE and then persistent drawdown. C07 Stage2 should not be awarded without customer order, qualification, delivery/utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_HBM_tester_RS_watch_counts_without_customer_order_qualification_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Entry selected after 2024-07-31 corporate-action candidate boundary. Source-proxy only."}
{"row_type": "case", "case_id": "R2L98_C07_JT_2024_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP_4B", "symbol": "089790", "company_name": "제이티", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_TESTER_POST_CA_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L98_C07_JT_2024_STAGE4B_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Test-handler/HBM-equipment event premium capped at the April spike and then de-rated sharply. C07 should route bridge-missing test-handler equipment premiums to 4B unless customer qualification, repeat order, delivery, utilization, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_test_handler_HBM_equipment_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2010 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L98_C07_DI_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE", "case_id": "R2L98_C07_DI_2024_HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE_POSITIVE", "symbol": "003160", "company_name": "디아이", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_TESTER_POST_CA_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "sector": "HBM_test_equipment_order_relative_strength", "primary_archetype": "customer_order_delivery_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | HBM_equipment_order_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-19", "entry_date": "2024-02-19", "entry_price": 7160.0, "evidence_available_at_that_date": "HBM test-equipment customer-order and delivery/utilization bridge proxy after February relative-strength breakout; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_report_proxy", "stage2_evidence_fields": ["HBM_test_equipment_proxy", "customer_order_proxy", "delivery_visibility_proxy", "utilization_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["very_strong_MFE30", "very_strong_MFE90", "shallow_initial_MAE"], "stage4b_evidence_fields": ["later_HBM_equipment_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv", "profile_path": "atlas/symbol_profiles/003/003160.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 95.95, "MFE_90D_pct": 157.96, "MFE_180D_pct": 157.96, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -0.28, "MAE_90D_pct": -0.28, "MAE_180D_pct": -0.28, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-11", "peak_price": 18470.0, "drawdown_after_peak_pct": "not_calculated", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_HBM_equipment_valuation_4B_watch_needed", "four_b_evidence_type": ["HBM_equipment_order_bridge", "relative_strength", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_HBM_test_equipment_order_relative_strength_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1997_1998_1999_CA", "same_entry_group_id": "R2L98_C07_003160_2024-02-19_7160", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L98_C07_EXICON_2024_STAGE2_FALSE_POSITIVE_HBM_TESTER_POST_CA_RS_WATCH", "case_id": "R2L98_C07_EXICON_2024_HBM_TESTER_POST_CA_LOW_MFE_FALSE_STAGE2", "symbol": "092870", "company_name": "엑시콘", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_TESTER_POST_CA_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "sector": "HBM_tester_post_CA_relative_strength_watch", "primary_archetype": "HBM_tester_watch_without_customer_order_qualification_utilization_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | HBM_equipment_order_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-01", "entry_date": "2024-08-01", "entry_price": 17840.0, "evidence_available_at_that_date": "HBM tester / post-CA relative-strength watch without confirmed customer qualification, repeat order, delivery, utilization, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["HBM_tester_watch", "post_CA_reset_watch", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "high_MAE90", "customer_order_qualification_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv", "profile_path": "atlas/symbol_profiles/092/092870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.57, "MFE_90D_pct": 7.57, "MFE_180D_pct": 7.57, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -38.06, "MAE_90D_pct": -41.7, "MAE_180D_pct": -41.7, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-01", "peak_price": 19190.0, "drawdown_after_peak_pct": -45.81, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "HBM_tester_post_CA_watch_was_false_stage2_due_missing_customer_order_qualification_utilization_margin_bridge", "four_b_evidence_type": ["HBM_tester_post_CA_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_HBM_tester_post_CA_RS_watch_without_customer_order_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_HBM_tester_RS_watch_counts_without_customer_order_qualification_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "post_2024-07-31_CA_boundary_clean_180D_window", "same_entry_group_id": "R2L98_C07_092870_2024-08-01_17840", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L98_C07_JT_2024_STAGE4B_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP", "case_id": "R2L98_C07_JT_2024_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP_4B", "symbol": "089790", "company_name": "제이티", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_TESTER_POST_CA_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "sector": "test_handler_HBM_equipment_event_premium", "primary_archetype": "test_handler_HBM_equipment_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | HBM_equipment_order_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-12", "entry_date": "2024-04-12", "entry_price": 11040.0, "evidence_available_at_that_date": "test-handler / HBM equipment event premium without confirmed customer qualification, repeat order, delivery, utilization, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["test_handler_event", "HBM_equipment_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "qualification_reorder_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089790/2024.csv", "profile_path": "atlas/symbol_profiles/089/089790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.9, "MFE_90D_pct": 2.9, "MFE_180D_pct": 2.9, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -28.17, "MAE_90D_pct": -39.31, "MAE_180D_pct": -39.31, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-12", "peak_price": 11360.0, "drawdown_after_peak_pct": -41.02, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "good_full_window_4B_timing_test_handler_HBM_equipment_event_cap_due_missing_customer_qualification_reorder_margin_bridge", "four_b_evidence_type": ["test_handler_HBM_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_test_handler_HBM_equipment_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_test_handler_HBM_equipment_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2010_CA", "same_entry_group_id": "R2L98_C07_089790_2024-04-12_11040", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R2L98_C07_DI_2024_HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE_POSITIVE", "trigger_id": "R2L98_C07_DI_2024_STAGE2_ACTIONABLE_HBM_TEST_EQUIPMENT_ORDER_RS_BRIDGE", "symbol": "003160", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 85, "customer_quality_score": 60, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "HBM_test_equipment_order_relative_strength_positive", "MFE_90D_pct": 157.96, "MAE_90D_pct": -0.28, "score_return_alignment_label": "HBM_equipment_order_RS_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R2L98_C07_EXICON_2024_HBM_TESTER_POST_CA_LOW_MFE_FALSE_STAGE2", "trigger_id": "R2L98_C07_EXICON_2024_STAGE2_FALSE_POSITIVE_HBM_TESTER_POST_CA_RS_WATCH", "symbol": "092870", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 60, "customer_quality_score": 30, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "HBM_tester_post_CA_false_stage2", "MFE_90D_pct": 7.57, "MAE_90D_pct": -41.7, "score_return_alignment_label": "HBM_tester_RS_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_HBM_tester_RS_watch_counts_without_customer_order_qualification_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R2L98_C07_JT_2024_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP_4B", "trigger_id": "R2L98_C07_JT_2024_STAGE4B_TEST_HANDLER_HBM_EQUIPMENT_EVENT_CAP", "symbol": "089790", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "test_handler_HBM_equipment_event_cap_4B_guard", "MFE_90D_pct": 2.9, "MAE_90D_pct": -39.31, "score_return_alignment_label": "test_handler_HBM_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_test_handler_HBM_equipment_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_TESTER_POST_CA_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "HBM_equipment_order_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["HBM_equipment_order_RS_positive", "HBM_tester_RS_false_stage2", "test_handler_HBM_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C07 rows need explicit customer order, qualification, delivery visibility, utilization, ASP/mix, margin or revision bridge before positive promotion.
- In C07, bridge-missing HBM equipment event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C07 HBM equipment order relative-strength rows cannot promote positive stages.

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
completed_canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
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
