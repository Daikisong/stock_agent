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
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_VS_TEST_RELIABILITY_FALSE_STAGE2_AND_AI_SEMICONDUCTOR_IP_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | advanced_equipment_valuation_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_98_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
```

This file is the corrected final output for this execution. The scheduler state after R1 loop 98 is R2 / loop 98. R2 is the L2 AI/semiconductor/electronics round, and this run fills C09 advanced-equipment valuation blowoff behavior rather than repeating the immediately preceding R2 loop 97 C06 HBM customer-capacity file or the older R2 loop 96 C08 / R2 loop 95 C10 files.

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
advanced_equipment_valuation_guardrail = existing_axis_strengthened
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
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
round_sector_consistency = pass
computed_next_round = R3
computed_next_loop = 98
```

C09 is an advanced-equipment valuation and blowoff archetype. The HBM or AI semiconductor label is the spark; the usable signal needs customer order, delivery slot, utilization, ASP/mix, margin and revision before promotion.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF = 17 rows / 11 symbols / good-bad Stage2 7-3 / 4B-4C 1-0
top covered symbols include 322310(3), 348210(3), 089030(2), 140860(2), 031980(1), 064290(1)
previous R2 loop-95 C10 symbols avoided: 232140, 330860, 200470
previous R2 loop-96 C08 symbols avoided: 424980, 098120, 080580
previous R2 loop-97 C06 symbols avoided: 031980, 036540, 080220
previous R1 loop-98 C02 symbols avoided: 010120, 037030, 024840
```

Selected rows avoid hard duplicates and top repeated C09 symbols:

```text
110990 / Stage2-Actionable / 2024-04-09
405100 / Stage2-Actionable / 2024-02-27
389020 / Stage4B / 2024-04-11
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
| 110990 | atlas/symbol_profiles/110/110990.json | no corporate-action candidate |
| 405100 | atlas/symbol_profiles/405/405100.json | selected 2024 window clean after old 2022/2023 CA candidates |
| 389020 | atlas/symbol_profiles/389/389020.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L98_C09_DIT_2024_HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_POSITIVE | 110990 | 2024-04-09 | yes | 180 | yes | yes | true |
| R2L98_C09_QRT_2024_TEST_RELIABILITY_EQUIPMENT_FALSE_STAGE2 | 405100 | 2024-02-27 | yes | 180 | yes | yes | true |
| R2L98_C09_ZARAM_2024_AI_SEMICONDUCTOR_IP_EVENT_CAP_4B | 389020 | 2024-04-11 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE | Positive Stage2 requires customer order, delivery, utilization, margin and revision bridge; later valuation watch still required. |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | TEST_RELIABILITY_EQUIPMENT_FALSE_STAGE2 | Test/reliability equipment watch without customer order and margin bridge can become false Stage2. |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | AI_SEMICONDUCTOR_IP_EVENT_CAP_4B | AI semiconductor/IP premium should route to 4B when license/design-win and revenue bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L98_C09_DIT_2024_HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_POSITIVE | 110990 | 디아이티 | positive | HBM laser-annealing/advanced equipment bridge produced strong MFE with shallow early MAE. |
| R2L98_C09_QRT_2024_TEST_RELIABILITY_EQUIPMENT_FALSE_STAGE2 | 405100 | 큐알티 | counterexample | Test/reliability equipment watch had brief follow-through and then high MAE. |
| R2L98_C09_ZARAM_2024_AI_SEMICONDUCTOR_IP_EVENT_CAP_4B | 389020 | 자람테크놀로지 | counterexample / 4B | AI semiconductor/IP event premium capped around the April spike and then de-rated sharply. |

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
| DIT HBM laser-annealing advanced-equipment bridge | historical public/report proxy | true | true | shadow-only positive |
| QRT test/reliability equipment false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Zaram AI semiconductor/IP event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 110990 | atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv | atlas/symbol_profiles/110/110990.json |
| 405100 | atlas/ohlcv_tradable_by_symbol_year/405/405100/2024.csv | atlas/symbol_profiles/405/405100.json |
| 389020 | atlas/ohlcv_tradable_by_symbol_year/389/389020/2024.csv | atlas/symbol_profiles/389/389020.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L98_C09_DIT_2024_STAGE2_ACTIONABLE_HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE | 110990 | Stage2-Actionable | 2024-04-09 | 20200 | positive | advanced-equipment bridge worked, later valuation watch required |
| R2L98_C09_QRT_2024_STAGE2_FALSE_POSITIVE_TEST_RELIABILITY_EQUIPMENT_WATCH | 405100 | Stage2-Actionable | 2024-02-27 | 37300 | counterexample | test/reliability equipment false Stage2 |
| R2L98_C09_ZARAM_2024_STAGE4B_AI_SEMICONDUCTOR_IP_EVENT_CAP | 389020 | Stage4B | 2024-04-11 | 117600 | counterexample/4B | AI semiconductor/IP event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L98_C09_DIT_2024_STAGE2_ACTIONABLE_HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE | 20200 | 60.15 | -5.20 | 60.15 | -5.20 | 60.15 | -47.28 | 2024-04-26 | 32350 | -67.08 |
| R2L98_C09_QRT_2024_STAGE2_FALSE_POSITIVE_TEST_RELIABILITY_EQUIPMENT_WATCH | 37300 | 16.62 | -17.69 | 16.62 | -33.24 | 16.62 | -55.76 | 2024-03-05 | 43500 | -64.85 |
| R2L98_C09_ZARAM_2024_STAGE4B_AI_SEMICONDUCTOR_IP_EVENT_CAP | 117600 | 11.39 | -27.81 | 11.39 | -55.70 | 11.39 | -69.31 | 2024-04-19 | 131000 | -72.75 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C09 Stage2 needs order / customer / delivery / utilization / margin / revision bridge |
| advanced_equipment_valuation_guardrail | strengthen: advanced-equipment labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing test-equipment and AI semiconductor/IP premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C09 rows cannot promote without durable order/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether advanced-equipment narrative becomes order, delivery and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 110990 | good_stage2_with_later_watch | Equipment order bridge produced strong MFE and shallow early MAE, but later drawdown requires valuation watch. |
| 405100 | bad_stage2 | Test/reliability equipment watch lacked customer order/utilization/margin bridge and suffered high MAE. |
| 389020 | good_4B | AI semiconductor/IP premium capped around the April event high and then de-rated sharply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 405100 test/reliability false Stage2 | 0.86 | 0.86 | false Stage2 due missing customer order / utilization / margin bridge |
| 389020 AI semiconductor/IP cap | 0.90 | 0.90 | good full-window 4B timing after AI semiconductor/IP event premium |
| 110990 advanced equipment bridge | n/a | n/a | positive Stage2, but later advanced-equipment valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 405100 / 389020
```

No hard 4C candidate is introduced in this R2 loop 98 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 advanced-equipment valuation/blowoff cases, Stage2 requires verified customer order, delivery visibility, utilization, ASP/mix, margin, or revision bridge. HBM, advanced equipment, laser annealing, test/reliability equipment, AI semiconductor/IP, design-win or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
rule = C09 should split true customer-order/delivery/margin positives from test-equipment false Stage2 and AI semiconductor/IP event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 29.39 | -31.38 | 0.67 | mixed; C09 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 29.39 | -31.38 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L2 order/delivery/margin bridge required | 2 | 38.39 | -19.22 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C09 bridge vs event-cap split | 2 | 38.39 | -19.22 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing advanced-equipment themes as positive | 1 | 60.15 | -5.20 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 110990 advanced-equipment bridge | 66 | Stage2-Watch | 79 | Stage2-Actionable | 60.15 | -5.20 | advanced_equipment_order_bridge_positive |
| 405100 test/reliability false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 16.62 | -33.24 | test_reliability_equipment_false_stage2 |
| 389020 AI semiconductor/IP cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 11.39 | -55.70 | AI_semiconductor_IP_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_VS_TEST_RELIABILITY_FALSE_STAGE2_AND_AI_SEMICONDUCTOR_IP_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds R2 loop98 C09: DIT HBM laser-annealing/advanced-equipment positive, QRT test/reliability equipment false Stage2, and Zaram Technology AI semiconductor/IP event-cap 4B while avoiding top repeated C09 and previous R2/R1 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, advanced_equipment_valuation_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: advanced_equipment_order_bridge_positive, test_reliability_equipment_false_stage2, AI_semiconductor_IP_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, advanced_equipment_valuation_guardrail, high_MAE_guardrail
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
- C09 advanced-equipment valuation/blowoff bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,configured,C09_requires_customer_order_delivery_utilization_margin_revision_bridge_and_valuation_watch,0,"C09 Stage2 should require customer order, delivery visibility, utilization, ASP/mix, margin, or revision bridge, not advanced equipment/HBM/AI semiconductor label alone","DIT positive worked; QRT and Zaram event/watch rows failed positive-stage promotion","R2L98_C09_DIT_2024_STAGE2_ACTIONABLE_HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE|R2L98_C09_QRT_2024_STAGE2_FALSE_POSITIVE_TEST_RELIABILITY_EQUIPMENT_WATCH|R2L98_C09_ZARAM_2024_STAGE4B_AI_SEMICONDUCTOR_IP_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,configured,cap_bridge_missing_test_equipment_and_AI_semiconductor_IP_event_premiums_as_4B_watch,0,"Test/reliability equipment and AI semiconductor/IP premiums can peak before customer order, license/design-win, revenue conversion and margin bridge is proven","QRT had high MAE after a brief equipment spike; Zaram showed 4B event-cap behavior after the April AI semiconductor/IP spike","R2L98_C09_QRT_2024_STAGE2_FALSE_POSITIVE_TEST_RELIABILITY_EQUIPMENT_WATCH|R2L98_C09_ZARAM_2024_STAGE4B_AI_SEMICONDUCTOR_IP_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,configured,block_positive_stage_when_advanced_equipment_theme_has_high_or_persistent_MAE_without_order_margin_bridge,0,"High or persistent MAE after bridge-missing C09 entries should block Stage2/Stage3 promotion unless order, delivery, customer and margin evidence survives","QRT MAE90=-33.24 and Zaram MAE90=-55.70","R2L98_C09_QRT_2024_STAGE2_FALSE_POSITIVE_TEST_RELIABILITY_EQUIPMENT_WATCH|R2L98_C09_ZARAM_2024_STAGE4B_AI_SEMICONDUCTOR_IP_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L98_C09_DIT_2024_HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_POSITIVE", "symbol": "110990", "company_name": "디아이티", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_VS_TEST_RELIABILITY_FALSE_STAGE2_AND_AI_SEMICONDUCTOR_IP_EVENT_CAP", "case_type": "structural_success_with_later_advanced_equipment_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R2L98_C09_DIT_2024_STAGE2_ACTIONABLE_HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "HBM / laser annealing / advanced-equipment order bridge produced strong 30D/90D MFE with shallow early MAE after the April retest. Later 180D drawdown shows the row is Stage2-positive with mandatory valuation and 4B watch, not unconditional Green.", "current_profile_verdict": "current_profile_kept_but_C09_positive_requires_equipment_order_customer_delivery_margin_revision_bridge_and_later_valuation_watch", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R2L98_C09_QRT_2024_TEST_RELIABILITY_EQUIPMENT_FALSE_STAGE2", "symbol": "405100", "company_name": "큐알티", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_VS_TEST_RELIABILITY_FALSE_STAGE2_AND_AI_SEMICONDUCTOR_IP_EVENT_CAP", "case_type": "failed_rerating_test_reliability_equipment_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R2L98_C09_QRT_2024_STAGE2_FALSE_POSITIVE_TEST_RELIABILITY_EQUIPMENT_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Semiconductor test/reliability equipment watch had a short HBM/advanced-test follow-through but then suffered high MAE. C09 Stage2 should not be awarded without confirmed customer order, utilization, delivery, ASP/mix, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_test_reliability_equipment_watch_counts_without_customer_order_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2022/2023 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R2L98_C09_ZARAM_2024_AI_SEMICONDUCTOR_IP_EVENT_CAP_4B", "symbol": "389020", "company_name": "자람테크놀로지", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_VS_TEST_RELIABILITY_FALSE_STAGE2_AND_AI_SEMICONDUCTOR_IP_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L98_C09_ZARAM_2024_STAGE4B_AI_SEMICONDUCTOR_IP_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "AI semiconductor/IP event premium capped around the April spike and then de-rated sharply. C09 should route bridge-missing AI semiconductor/IP premiums to 4B unless license/customer design-win, tape-out or mass-production path, revenue conversion, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_AI_semiconductor_IP_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L98_C09_DIT_2024_STAGE2_ACTIONABLE_HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE", "case_id": "R2L98_C09_DIT_2024_HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_POSITIVE", "symbol": "110990", "company_name": "디아이티", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_VS_TEST_RELIABILITY_FALSE_STAGE2_AND_AI_SEMICONDUCTOR_IP_EVENT_CAP", "sector": "HBM_laser_annealing_advanced_equipment_order_margin", "primary_archetype": "equipment_order_customer_delivery_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | advanced_equipment_valuation_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-09", "entry_date": "2024-04-09", "entry_price": 20200.0, "evidence_available_at_that_date": "HBM / laser annealing / advanced-equipment customer order and process bottleneck bridge proxy after April retest; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["HBM_laser_annealing_proxy", "advanced_equipment_order_proxy", "customer_quality_proxy", "delivery_visibility_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["later_advanced_equipment_valuation_watch", "180D_drawdown_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv", "profile_path": "atlas/symbol_profiles/110/110990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 60.15, "MFE_90D_pct": 60.15, "MFE_180D_pct": 60.15, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.2, "MAE_90D_pct": -5.2, "MAE_180D_pct": -47.28, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-26", "peak_price": 32350.0, "drawdown_after_peak_pct": -67.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_advanced_equipment_valuation_4B_watch_needed", "four_b_evidence_type": ["equipment_order_bridge", "customer_delivery_visibility", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_HBM_laser_annealing_advanced_equipment_bridge_success_with_later_4B_watch", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R2L98_C09_110990_2024-04-09_20200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L98_C09_QRT_2024_STAGE2_FALSE_POSITIVE_TEST_RELIABILITY_EQUIPMENT_WATCH", "case_id": "R2L98_C09_QRT_2024_TEST_RELIABILITY_EQUIPMENT_FALSE_STAGE2", "symbol": "405100", "company_name": "큐알티", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_VS_TEST_RELIABILITY_FALSE_STAGE2_AND_AI_SEMICONDUCTOR_IP_EVENT_CAP", "sector": "semiconductor_test_reliability_equipment_HBM_watch", "primary_archetype": "test_reliability_equipment_watch_without_customer_order_utilization_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | advanced_equipment_valuation_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-27", "entry_date": "2024-02-27", "entry_price": 37300.0, "evidence_available_at_that_date": "semiconductor test/reliability equipment and HBM quality-assurance sympathy watch without confirmed customer order, utilization, delivery, ASP/mix or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["test_reliability_equipment_watch", "HBM_quality_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["brief_MFE_then_high_MAE", "customer_order_utilization_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/405/405100/2024.csv", "profile_path": "atlas/symbol_profiles/405/405100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.62, "MFE_90D_pct": 16.62, "MFE_180D_pct": 16.62, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -17.69, "MAE_90D_pct": -33.24, "MAE_180D_pct": -55.76, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-05", "peak_price": 43500.0, "drawdown_after_peak_pct": -64.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.86, "four_b_full_window_peak_proximity": 0.86, "four_b_timing_verdict": "test_reliability_equipment_watch_was_false_stage2_due_missing_customer_order_utilization_margin_bridge", "four_b_evidence_type": ["test_equipment_premium", "bridge_missing", "high_MAE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_test_reliability_equipment_watch_without_order_utilization_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_test_reliability_equipment_watch_counts_without_customer_order_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_2023_CA", "same_entry_group_id": "R2L98_C09_405100_2024-02-27_37300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L98_C09_ZARAM_2024_STAGE4B_AI_SEMICONDUCTOR_IP_EVENT_CAP", "case_id": "R2L98_C09_ZARAM_2024_AI_SEMICONDUCTOR_IP_EVENT_CAP_4B", "symbol": "389020", "company_name": "자람테크놀로지", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_VS_TEST_RELIABILITY_FALSE_STAGE2_AND_AI_SEMICONDUCTOR_IP_EVENT_CAP", "sector": "AI_semiconductor_IP_design_win_event_premium", "primary_archetype": "AI_semiconductor_IP_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | advanced_equipment_valuation_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-11", "entry_date": "2024-04-11", "entry_price": 117600.0, "evidence_available_at_that_date": "AI semiconductor/IP event premium without confirmed license/design-win, tape-out, mass-production path, revenue conversion, customer backlog or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["AI_semiconductor_IP_event", "design_win_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "license_revenue_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/389/389020/2024.csv", "profile_path": "atlas/symbol_profiles/389/389020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.39, "MFE_90D_pct": 11.39, "MFE_180D_pct": 11.39, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.81, "MAE_90D_pct": -55.7, "MAE_180D_pct": -69.31, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-19", "peak_price": 131000.0, "drawdown_after_peak_pct": -72.75, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "good_full_window_4B_timing_AI_semiconductor_IP_event_cap_due_missing_license_revenue_margin_bridge", "four_b_evidence_type": ["AI_semiconductor_IP_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_AI_semiconductor_IP_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_AI_semiconductor_IP_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R2L98_C09_389020_2024-04-11_117600", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L98_C09_DIT_2024_HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_POSITIVE", "trigger_id": "R2L98_C09_DIT_2024_STAGE2_ACTIONABLE_HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE", "symbol": "110990", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 75, "customer_quality_score": 60, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "HBM_laser_annealing_advanced_equipment_positive", "MFE_90D_pct": 60.15, "MAE_90D_pct": -5.2, "score_return_alignment_label": "advanced_equipment_order_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L98_C09_QRT_2024_TEST_RELIABILITY_EQUIPMENT_FALSE_STAGE2", "trigger_id": "R2L98_C09_QRT_2024_STAGE2_FALSE_POSITIVE_TEST_RELIABILITY_EQUIPMENT_WATCH", "symbol": "405100", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 10, "valuation_repricing_score": 65, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "test_reliability_equipment_false_stage2", "MFE_90D_pct": 16.62, "MAE_90D_pct": -33.24, "score_return_alignment_label": "test_reliability_equipment_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_test_reliability_equipment_watch_counts_without_customer_order_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L98_C09_ZARAM_2024_AI_SEMICONDUCTOR_IP_EVENT_CAP_4B", "trigger_id": "R2L98_C09_ZARAM_2024_STAGE4B_AI_SEMICONDUCTOR_IP_EVENT_CAP", "symbol": "389020", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 25, "policy_or_regulatory_score": 15, "valuation_repricing_score": 70, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 95, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "AI_semiconductor_IP_event_cap_4B_guard", "MFE_90D_pct": 11.39, "MAE_90D_pct": -55.7, "score_return_alignment_label": "AI_semiconductor_IP_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_AI_semiconductor_IP_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "98", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_BRIDGE_VS_TEST_RELIABILITY_FALSE_STAGE2_AND_AI_SEMICONDUCTOR_IP_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "advanced_equipment_valuation_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["advanced_equipment_order_bridge_positive", "test_reliability_equipment_false_stage2", "AI_semiconductor_IP_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C09 rows need explicit customer order, delivery visibility, utilization, ASP/mix, margin or revision bridge before positive promotion.
- In C09, bridge-missing advanced-equipment or AI semiconductor event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C09 advanced-equipment valuation/blowoff rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 98
next_round = R3
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
