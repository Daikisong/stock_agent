# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R2
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_VS_SILICON_PARTS_LOW_MFE_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | test_socket_customer_quality_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
```

This execution follows the coverage-index scheduler, not the mechanical R1→R13 cycle. The no-repeat index marks C08 as Priority 0 with only 14 rows, so the selected round is R2 because C08 maps to L2 AI/semiconductor/electronics.

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
test_socket_customer_quality_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R2
scheduled_loop = 97
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C08 is a customer-quality / repeat-consumable archetype. The test/socket label is only the package. The usable signal appears when customer qualification, repeat demand, utilization, margin and revision move together.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY = 14 rows / Priority 0
top covered symbols include UNKNOWN_SYMBOL, 089030, 095340, 131290, 252990, 058470
previous R2 loop-96 C08 symbols avoided: 424980, 098120, 080580
previous R2 loop-97 C06 symbols avoided: 031980, 036540, 080220
previous R2 loop-98 C09 symbols avoided in local run: 110990, 405100, 389020
```

Selected rows avoid hard duplicates and top repeated C08 symbols:

```text
074600 / Stage2-Actionable / 2024-03-20
101160 / Stage2-Actionable / 2024-03-21
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
| 074600 | atlas/symbol_profiles/074/074600.json | selected 2024 window clean after old 2004/2017 CA candidates |
| 101160 | atlas/symbol_profiles/101/101160.json | selected 2024 window clean after old 2014 CA candidate |
| 089790 | atlas/symbol_profiles/089/089790.json | selected 2024 window clean after old 2010 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R2L97_C08_WONIKQNC_2024_QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_POSITIVE | 074600 | 2024-03-20 | yes | 180 | yes | yes | true |
| R2L97_C08_WORLDEX_2024_SILICON_PARTS_LOW_MFE_FALSE_STAGE2 | 101160 | 2024-03-21 | yes | 180 | yes | yes | true |
| R2L97_C08_JT_2024_TEST_HANDLER_EVENT_CAP_4B | 089790 | 2024-04-12 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE | Positive Stage2 requires customer quality, consumable reorder, utilization, margin and revision bridge. |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | SILICON_PARTS_LOW_MFE_FALSE_STAGE2 | Silicon-parts quality watch without qualification/reorder/margin bridge can become false Stage2. |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | TEST_HANDLER_EVENT_CAP_4B | Test-handler event premium should route to 4B when customer qualification and repeat demand are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R2L97_C08_WONIKQNC_2024_QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_POSITIVE | 074600 | 원익QnC | positive | Quartz/semiconductor consumable bridge produced positive MFE with controlled early MAE. |
| R2L97_C08_WORLDEX_2024_SILICON_PARTS_LOW_MFE_FALSE_STAGE2 | 101160 | 월덱스 | counterexample | Silicon-parts quality watch had low MFE and persistent drawdown without qualification/reorder evidence. |
| R2L97_C08_JT_2024_TEST_HANDLER_EVENT_CAP_4B | 089790 | 제이티 | counterexample / 4B | Test-handler premium capped at the April event spike and then de-rated deeply. |

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
| Wonik QnC quartz consumable customer-quality bridge | historical public/report proxy | true | true | shadow-only positive |
| Worldex silicon-parts low-MFE false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| JT test-handler event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 074600 | atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv | atlas/symbol_profiles/074/074600.json |
| 101160 | atlas/ohlcv_tradable_by_symbol_year/101/101160/2024.csv | atlas/symbol_profiles/101/101160.json |
| 089790 | atlas/ohlcv_tradable_by_symbol_year/089/089790/2024.csv | atlas/symbol_profiles/089/089790.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R2L97_C08_WONIKQNC_2024_STAGE2_ACTIONABLE_QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE | 074600 | Stage2-Actionable | 2024-03-20 | 30750 | positive | quartz consumable customer-quality bridge worked |
| R2L97_C08_WORLDEX_2024_STAGE2_FALSE_POSITIVE_SILICON_PARTS_CUSTOMER_QUALITY_WATCH | 101160 | Stage2-Actionable | 2024-03-21 | 25150 | counterexample | silicon-parts low-MFE false Stage2 |
| R2L97_C08_JT_2024_STAGE4B_TEST_HANDLER_EVENT_CAP | 089790 | Stage4B | 2024-04-12 | 11040 | counterexample/4B | test-handler event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R2L97_C08_WONIKQNC_2024_STAGE2_ACTIONABLE_QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE | 30750 | 15.12 | -2.11 | 33.33 | -4.72 | 33.33 | -27.00 | 2024-06-07 | 41000 | -45.24 |
| R2L97_C08_WORLDEX_2024_STAGE2_FALSE_POSITIVE_SILICON_PARTS_CUSTOMER_QUALITY_WATCH | 25150 | 3.98 | -6.56 | 3.98 | -14.91 | 5.37 | -16.10 | 2024-04-02 | 26150 | -18.36 |
| R2L97_C08_JT_2024_STAGE4B_TEST_HANDLER_EVENT_CAP | 11040 | 2.90 | -28.17 | 2.90 | -39.31 | 2.90 | -39.31 | 2024-04-12 | 11360 | -41.02 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C08 Stage2 needs customer qualification / repeat demand / utilization / margin / revision bridge |
| test_socket_customer_quality_guardrail | strengthen: socket/test/parts labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing silicon-parts and test-handler event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C08 rows cannot promote without durable qualification/reorder bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether semiconductor test/socket narrative becomes customer qualification and repeat-consumable economics.

| symbol | stage quality | explanation |
|---|---|---|
| 074600 | good_stage2_with_later_watch | Customer-quality and consumable bridge produced positive MFE, but later cycle drawdown requires 4B valuation watch. |
| 101160 | bad_stage2 | Silicon-parts quality watch lacked customer qualification/reorder bridge and produced low MFE. |
| 089790 | good_4B | Test-handler event premium peaked immediately and later drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 101160 silicon-parts false Stage2 | 0.96 | 0.96 | false Stage2 due missing customer qualification / reorder / utilization / margin bridge |
| 089790 test-handler event cap | 0.97 | 0.97 | good full-window 4B timing after test-handler event premium |
| 074600 quartz consumable bridge | n/a | n/a | positive Stage2, but later semiconductor consumable valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 101160 / 089790
```

No hard 4C candidate is introduced in this C08 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L2 semiconductor test/socket customer-quality cases, Stage2 requires verified customer qualification, repeat consumable/socket demand, utilization, ASP/mix, margin, or revision bridge. Test/socket, silicon parts, handler, customer quality, probe, consumable or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
rule = C08 should split true customer-quality/consumable-reorder/margin positives from silicon-parts low-MFE false Stage2 and test-handler event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 13.40 | -19.65 | 0.67 | mixed; C08 bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 13.40 | -19.65 | 0.67 | weaker C08 bridge split |
| P1 sector_specific_candidate_profile | L2 customer-quality/reorder bridge required | 2 | 18.66 | -9.82 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C08 bridge vs event-cap split | 2 | 18.66 | -9.82 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing test/socket themes as positive | 1 | 33.33 | -4.72 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 074600 quartz consumable bridge | 66 | Stage2-Watch | 77 | Stage2-Actionable | 33.33 | -4.72 | semi_consumable_customer_quality_positive |
| 101160 silicon-parts false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 3.98 | -14.91 | silicon_parts_quality_false_stage2 |
| 089790 test-handler cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.90 | -39.31 | test_handler_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_VS_SILICON_PARTS_LOW_MFE_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C08 had only 14 rows in Priority 0; this run adds three new C08 symbols and three new trigger families while avoiding top-covered C08 symbols and prior R2 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, test_socket_customer_quality_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: semi_consumable_customer_quality_positive, silicon_parts_quality_false_stage2, test_handler_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, test_socket_customer_quality_guardrail, high_MAE_guardrail
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
- C08 semiconductor test/socket customer-quality bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,configured,C08_requires_customer_qualification_reorder_utilization_margin_revision_bridge,0,"C08 Stage2 should require customer qualification, repeat consumable or socket demand, utilization, margin, or revision bridge, not semiconductor test/socket label alone","Wonik QnC positive worked; Worldex and JT event/watch rows failed positive-stage promotion","R2L97_C08_WONIKQNC_2024_STAGE2_ACTIONABLE_QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE|R2L97_C08_WORLDEX_2024_STAGE2_FALSE_POSITIVE_SILICON_PARTS_CUSTOMER_QUALITY_WATCH|R2L97_C08_JT_2024_STAGE4B_TEST_HANDLER_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,configured,cap_bridge_missing_silicon_parts_and_test_handler_event_premiums_as_4B_watch,0,"Silicon-parts and test-handler premiums can peak before customer qualification, reorder, utilization and margin bridge is proven","Worldex had low MFE after parts-quality watch; JT showed 4B event-cap behavior after the April test-handler spike","R2L97_C08_WORLDEX_2024_STAGE2_FALSE_POSITIVE_SILICON_PARTS_CUSTOMER_QUALITY_WATCH|R2L97_C08_JT_2024_STAGE4B_TEST_HANDLER_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,configured,block_positive_stage_when_test_socket_theme_has_high_or_persistent_MAE_without_customer_quality_bridge,0,"High or persistent MAE after bridge-missing C08 entries should block Stage2/Stage3 promotion unless customer qualification and reorder/margin evidence survives","JT MAE90=-39.31; Worldex low-MFE row also remains false Stage2","R2L97_C08_WORLDEX_2024_STAGE2_FALSE_POSITIVE_SILICON_PARTS_CUSTOMER_QUALITY_WATCH|R2L97_C08_JT_2024_STAGE4B_TEST_HANDLER_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R2L97_C08_WONIKQNC_2024_QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_POSITIVE", "symbol": "074600", "company_name": "원익QnC", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_VS_SILICON_PARTS_LOW_MFE_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "case_type": "moderate_structural_success_with_later_semiconductor_consumable_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R2L97_C08_WONIKQNC_2024_STAGE2_ACTIONABLE_QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Quartz/semiconductor consumable customer-quality bridge produced a clean 30D/90D MFE path from the March retest with limited early MAE, but later cycle drawdown still requires valuation and customer-order watch.", "current_profile_verdict": "current_profile_kept_but_C08_positive_requires_customer_quality_consumable_reorder_utilization_margin_revision_bridge_not_socket_or_test_theme_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2004/2017 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R2L97_C08_WORLDEX_2024_SILICON_PARTS_LOW_MFE_FALSE_STAGE2", "symbol": "101160", "company_name": "월덱스", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_VS_SILICON_PARTS_LOW_MFE_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "case_type": "failed_rerating_silicon_parts_customer_quality_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R2L97_C08_WORLDEX_2024_STAGE2_FALSE_POSITIVE_SILICON_PARTS_CUSTOMER_QUALITY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Silicon-parts / consumable-quality watch after the March spike had low MFE and persistent drawdown. C08 Stage2 should not be awarded without confirmed customer qualification, socket/parts reorder, utilization, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_silicon_parts_quality_watch_counts_without_customer_qualification_reorder_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2014 corporate-action candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R2L97_C08_JT_2024_TEST_HANDLER_EVENT_CAP_4B", "symbol": "089790", "company_name": "제이티", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_VS_SILICON_PARTS_LOW_MFE_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R2L97_C08_JT_2024_STAGE4B_TEST_HANDLER_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Semiconductor test-handler / test-equipment event premium capped in the April spike and then de-rated sharply. C08 should route bridge-missing test-handler premiums to 4B unless customer qualification, repeat demand, utilization, order visibility, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_test_handler_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2010 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R2L97_C08_WONIKQNC_2024_STAGE2_ACTIONABLE_QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE", "case_id": "R2L97_C08_WONIKQNC_2024_QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_POSITIVE", "symbol": "074600", "company_name": "원익QnC", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_VS_SILICON_PARTS_LOW_MFE_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "sector": "semi_quartz_consumable_customer_quality_utilization_margin", "primary_archetype": "customer_quality_consumable_reorder_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | test_socket_customer_quality_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-20", "entry_date": "2024-03-20", "entry_price": 30750.0, "evidence_available_at_that_date": "semiconductor quartz consumable / customer quality / utilization recovery and margin/revision bridge proxy after March retest; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["customer_quality_proxy", "consumable_reorder_proxy", "utilization_recovery_proxy", "margin_bridge_proxy", "revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "limited_initial_MAE"], "stage4b_evidence_fields": ["later_semiconductor_consumable_valuation_watch", "cycle_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv", "profile_path": "atlas/symbol_profiles/074/074600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.12, "MFE_90D_pct": 33.33, "MFE_180D_pct": 33.33, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -2.11, "MAE_90D_pct": -4.72, "MAE_180D_pct": -27.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-07", "peak_price": 41000.0, "drawdown_after_peak_pct": -45.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_semiconductor_consumable_valuation_4B_watch_needed", "four_b_evidence_type": ["customer_quality_reorder_bridge", "utilization_margin", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_quartz_consumable_customer_quality_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2004_2017_CA", "same_entry_group_id": "R2L97_C08_074600_2024-03-20_30750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L97_C08_WORLDEX_2024_STAGE2_FALSE_POSITIVE_SILICON_PARTS_CUSTOMER_QUALITY_WATCH", "case_id": "R2L97_C08_WORLDEX_2024_SILICON_PARTS_LOW_MFE_FALSE_STAGE2", "symbol": "101160", "company_name": "월덱스", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_VS_SILICON_PARTS_LOW_MFE_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "sector": "silicon_parts_semiconductor_consumable_quality_watch", "primary_archetype": "silicon_parts_watch_without_customer_qualification_reorder_utilization_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | test_socket_customer_quality_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-21", "entry_date": "2024-03-21", "entry_price": 25150.0, "evidence_available_at_that_date": "silicon parts / consumable quality watch after March semiconductor materials spike without confirmed customer qualification, repeat order, utilization or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["silicon_parts_quality_watch", "semiconductor_consumable_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "persistent_MAE90", "customer_qualification_reorder_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/101/101160/2024.csv", "profile_path": "atlas/symbol_profiles/101/101160.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.98, "MFE_90D_pct": 3.98, "MFE_180D_pct": 5.37, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.56, "MAE_90D_pct": -14.91, "MAE_180D_pct": -16.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-02", "peak_price": 26150.0, "drawdown_after_peak_pct": -18.36, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "silicon_parts_quality_watch_was_false_stage2_due_missing_customer_qualification_reorder_utilization_margin_bridge", "four_b_evidence_type": ["silicon_parts_premium", "bridge_missing", "low_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_silicon_parts_quality_watch_without_reorder_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_silicon_parts_quality_watch_counts_without_customer_qualification_reorder_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2014_CA", "same_entry_group_id": "R2L97_C08_101160_2024-03-21_25150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R2L97_C08_JT_2024_STAGE4B_TEST_HANDLER_EVENT_CAP", "case_id": "R2L97_C08_JT_2024_TEST_HANDLER_EVENT_CAP_4B", "symbol": "089790", "company_name": "제이티", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_VS_SILICON_PARTS_LOW_MFE_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "sector": "semiconductor_test_handler_equipment_event_premium", "primary_archetype": "test_handler_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | test_socket_customer_quality_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-12", "entry_date": "2024-04-12", "entry_price": 11040.0, "evidence_available_at_that_date": "semiconductor test-handler / test-equipment event premium without confirmed customer qualification, repeat order, delivery, utilization, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["test_handler_event", "semiconductor_test_equipment_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "qualification_reorder_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089790/2024.csv", "profile_path": "atlas/symbol_profiles/089/089790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.9, "MFE_90D_pct": 2.9, "MFE_180D_pct": 2.9, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -28.17, "MAE_90D_pct": -39.31, "MAE_180D_pct": -39.31, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-12", "peak_price": 11360.0, "drawdown_after_peak_pct": -41.02, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "good_full_window_4B_timing_test_handler_event_cap_due_missing_customer_qualification_reorder_margin_bridge", "four_b_evidence_type": ["test_handler_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_test_handler_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_test_handler_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2010_CA", "same_entry_group_id": "R2L97_C08_089790_2024-04-12_11040", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R2L97_C08_WONIKQNC_2024_QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_POSITIVE", "trigger_id": "R2L97_C08_WONIKQNC_2024_STAGE2_ACTIONABLE_QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE", "symbol": "074600", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 60, "customer_quality_score": 50, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 65, "policy_or_regulatory_score": 10, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "quartz_consumable_customer_quality_positive", "MFE_90D_pct": 33.33, "MAE_90D_pct": -4.72, "score_return_alignment_label": "semi_consumable_customer_quality_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R2L97_C08_WORLDEX_2024_SILICON_PARTS_LOW_MFE_FALSE_STAGE2", "trigger_id": "R2L97_C08_WORLDEX_2024_STAGE2_FALSE_POSITIVE_SILICON_PARTS_CUSTOMER_QUALITY_WATCH", "symbol": "101160", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "silicon_parts_quality_low_MFE_false_stage2", "MFE_90D_pct": 3.98, "MAE_90D_pct": -14.91, "score_return_alignment_label": "silicon_parts_quality_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_silicon_parts_quality_watch_counts_without_customer_qualification_reorder_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R2L97_C08_JT_2024_TEST_HANDLER_EVENT_CAP_4B", "trigger_id": "R2L97_C08_JT_2024_STAGE4B_TEST_HANDLER_EVENT_CAP", "symbol": "089790", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "test_handler_event_cap_4B_guard", "MFE_90D_pct": 2.9, "MAE_90D_pct": -39.31, "score_return_alignment_label": "test_handler_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_test_handler_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "QUARTZ_CONSUMABLE_CUSTOMER_QUALITY_BRIDGE_VS_SILICON_PARTS_LOW_MFE_FALSE_STAGE2_AND_TEST_HANDLER_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "test_socket_customer_quality_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["semi_consumable_customer_quality_positive", "silicon_parts_quality_false_stage2", "test_handler_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- C08 rows need explicit customer qualification, repeat consumable/socket demand, utilization, ASP/mix, margin or revision bridge before positive promotion.
- In C08, bridge-missing semiconductor test/socket event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C08 semiconductor test/socket customer-quality rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R2
completed_loop = 97
completed_canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 0
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
