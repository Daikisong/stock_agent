# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round: R2
selected_loop: 90
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_TCBONDER_AND_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_WAFER_EQUIPMENT_PRICE_BETA
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

## 1. Current Calibrated Profile Assumption

Current proxy is `e2r_2_1_stock_web_calibrated`. The global axes already applied are treated as existing axes, not as new findings:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD therefore does not claim that the global Stage2 bonus or Green thresholds are newly proven. It tests a narrower C07 residual: **HBM equipment relative strength works only when order/customer-quality bridge exists; late equipment-beta entries without that bridge should be demoted or treated as 4B/weak-watch.**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R2 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH |
| fine_archetype_id | HBM_TCBONDER_AND_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_WAFER_EQUIPMENT_PRICE_BETA |
| round-sector consistency | pass |
| selected priority | Priority 0 |

C07 maps to R2/L2. The selected scope is therefore internally consistent.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C07 current rows | 18 |
| C07 current symbols | 16 |
| C07 need to 30 | 12 |
| top-covered symbols to avoid | 084370, 232140, 036200, 036930, 039030, 039440 |

This run avoids those top-covered symbols and adds:

| symbol | company | novelty |
|---|---|---|
| 042700 | 한미반도체 | new C07 symbol / TC-bonder order route |
| 089030 | 테크윙 | new C07 symbol / HBM test-handler route |
| 319660 | 피에스케이 | new C07 counterexample / wafer equipment beta without HBM order bridge |

Hard duplicate rule checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No row in this MD intentionally repeats a known C07 hard duplicate from the index.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest basis:

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| source basis | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| manifest_max_date | 2026-02-20 |

Symbol profiles checked:

| symbol | profile path | status |
|---|---|---|
| 042700 | atlas/symbol_profiles/042/042700.json | active_like, corporate-action caveat outside 2024 test window |
| 089030 | atlas/symbol_profiles/089/089030.json | active_like, corporate-action caveat outside 2024 test window |
| 319660 | atlas/symbol_profiles/319/319660.json | active_like, corporate-action caveat outside 2024 test window |

## 5. Historical Eligibility Gate

All representative triggers use historical 2024 entry dates and have at least 180 trading days available before the stock-web manifest max date of 2026-02-20. Each trigger uses `tradable_raw` OHLC rows and excludes rows with known corporate-action contamination in the tested 180D window.

| case | entry_date | forward window | calibration usable | block reasons |
|---|---|---:|---|---|
| 042700 | 2024-02-08 | 180D available | true | none |
| 089030 | 2024-02-22 | 180D available | true | none |
| 319660 | 2024-07-11 | 180D available | true | none |

## 6. Canonical Archetype Compression Map

| fine/deep family | compressed canonical |
|---|---|
| HBM TC-bonder order relative strength + customer capacity bridge | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH |
| HBM test-handler order/revenue conversion + late 4B drawdown | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH |
| Wafer/process equipment beta without HBM-specific order bridge | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH counterexample bucket |

Compression rule:

```text
Relative strength alone is not C07 positive evidence.
C07 positive evidence requires at least one non-price bridge:
- order/customer quality
- HBM customer capacity route
- revenue conversion / repeat order
- revision confirmation
```

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | price | result |
|---|---|---|---|---|---:|---|
| C07_R2L90_042700_20240208_STAGE2A | 042700 | 한미반도체 | structural_success | 2024-02-08 | 78,500 | order-backed HBM equipment rerating |
| C07_R2L90_089030_20240222_STAGE2A | 089030 | 테크윙 | structural_success / 4B audit | 2024-02-22 | 22,300 | large MFE but 4B needed after peak |
| C07_R2L90_319660_20240711_FALSE_STAGE2 | 319660 | 피에스케이 | counterexample | 2024-07-11 | 38,600 | price-only equipment beta failed |

## 8. Positive vs Counterexample Balance

| bucket | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 0 |
| calibration_usable_case_count | 3 |

Minimum v12 requirement is satisfied:

```text
positive_case_count >= 1
counterexample_count >= 1
calibration_usable_case_count >= 3
```

## 9. Evidence Source Map

| symbol | evidence family | evidence status |
|---|---|---|
| 042700 | hbm_tcbond_order_relative_strength_with_customer_capacity_bridge | source_proxy_only / URL pending |
| 089030 | hbm_test_handler_order_relative_strength_with_late_4b_drawdown | source_proxy_only / URL pending |
| 319660 | wafer_equipment_price_beta_without_hbm_order_bridge | source_proxy_only / URL pending |

This MD uses public-event/source-name-level proxies for the non-price evidence field. The quantitative path is not a proxy: it is based on stock-web OHLC rows.

## 10. Price Data Source Map

| symbol | price shard | profile |
|---|---|---|
| 042700 | atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv | atlas/symbol_profiles/042/042700.json |
| 089030 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json |
| 319660 | atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv | atlas/symbol_profiles/319/319660.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | symbol | entry_date | evidence | aggregate role |
|---|---|---|---|---|---|
| C07_R2L90_042700_20240208_STAGE2A | Stage2-Actionable | 042700 | 2024-02-08 | HBM TC-bonder order bridge | representative |
| C07_R2L90_042700_20240614_STAGE4B_OVERLAY | Stage4B | 042700 | 2024-06-14 | valuation/positioning overheat after order-backed rerating | 4B_overlay_only |
| C07_R2L90_089030_20240222_STAGE2A | Stage2-Actionable | 089030 | 2024-02-22 | HBM test-handler order route | representative |
| C07_R2L90_089030_20240711_STAGE4B_OVERLAY | Stage4B | 089030 | 2024-07-11 | full-window 4B after high-MFE rerating | 4B_overlay_only |
| C07_R2L90_319660_20240711_STAGE2_FALSE_POSITIVE | Stage2 | 319660 | 2024-07-11 | wafer equipment price beta without HBM order bridge | representative |

## 12. Trigger-Level OHLC Backtest Tables

Representative triggers:

| symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | DD after peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 042700 | 2024-02-08 | 78,500 | 37.32 | -23.06 | 149.94 | -23.06 | 149.94 | -23.06 | 2024-06-14 | 196,200 | -24.26 |
| 089030 | 2024-02-22 | 22,300 | 69.73 | -10.40 | 217.49 | -10.40 | 217.49 | -10.40 | 2024-07-11 | 70,800 | -60.10 |
| 319660 | 2024-07-11 | 38,600 | 1.30 | -37.82 | 1.30 | -46.89 | 1.30 | -47.15 | 2024-07-11 | 39,100 | -47.83 |

4B overlays:

| symbol | 4B_date | 4B_entry | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---:|---|
| 042700 | 2024-06-14 | 179,900 | 0.86 | 0.86 | good_full_window_4B_timing |
| 089030 | 2024-07-11 | 68,700 | 0.96 | 0.96 | good_full_window_4B_timing_after_stage2_success |

## 13. Current Calibrated Profile Stress Test

| case | current proxy verdict | actual path | residual |
|---|---|---|---|
| 042700 | too late if waiting for full Green | very large MFE after order-backed Stage2 | missed earlier Stage2-Actionable confirmation |
| 089030 | Stage2 worked, but 4B too late | MFE90 > 200%, then deep drawdown | need C07-specific 4B timing audit |
| 319660 | false positive if relative strength alone promoted | MFE90 1.3%, MAE90 -46.89% | price-only equipment beta must not promote |

## 14. Stage2 / Yellow / Green Comparison

Green lateness is not the main new axis here. The residual is narrower:

```text
C07 Stage2-Actionable should appear when relative strength is paired with order/customer-quality bridge.
C07 Stage3-Green should still require confirmed revision, repeat order/revenue conversion, and low red-team risk.
```

For 042700 and 089030, Stage2-Actionable was the useful early label. For 319660, relative strength without HBM order bridge was not enough.

## 15. 4B Local vs Full-window Timing Audit

C07 has a special 4B shape: early price-only local 4B can be too early, but once a true order-backed rerating has already delivered most of the full-window move, valuation/positioning 4B becomes useful.

| symbol | Stage2 entry | 4B entry | peak | full-window proximity | interpretation |
|---|---:|---:|---:|---:|---|
| 042700 | 78,500 | 179,900 | 196,200 | 0.86 | good timing, but not a Stage2 demotion |
| 089030 | 22,300 | 68,700 | 70,800 | 0.96 | good timing, would reduce post-peak drawdown |
| 319660 | 38,600 | n/a | 39,100 | 1.00 | entry itself was price-only late chase, not positive Stage2 |

## 16. 4C Protection Audit

No hard 4C row is proposed. 319660 is a high-MAE Stage2 false positive / weak-watch demotion, not a hard thesis-break 4C. The evidence problem is missing HBM-specific bridge, not a confirmed contract cancellation.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
candidate = L2 relative-strength-only semi-equipment entries need customer/order bridge before Stage2-Actionable promotion.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
candidate = c07_order_customer_bridge_required_for_stage2_actionable_shadow_only
```

Rule wording:

```text
For C07, Stage2-Actionable can be awarded when relative_strength_score is backed by at least one of:
- HBM order/customer-quality disclosure
- HBM customer capacity route
- order-to-revenue conversion evidence
- early revision/repeat-order confirmation

If only price/relative strength exists, keep as Stage1/weak-watch or 4B watch, not Stage2-Actionable.
```

## 19. Before / After Backtest Comparison

| profile | eligible representative triggers | avg MFE90 | avg MAE90 | false positive count | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 122.91 | -26.78 | 1 | current profile still admits one price-only beta |
| P1 C07 bridge-required shadow | 2 positive promoted, 1 demoted | 183.72 on promoted | -16.73 on promoted | 0 promoted false positives | better score-return alignment |
| P3 counterexample guard | 1 weak-watch demotion | 1.30 on demoted case | -46.89 on demoted case | prevents bad Stage2 | useful |

## 20. Score-Return Alignment Matrix

| symbol | before score | before label | after score | after label | alignment |
|---|---:|---|---:|---|---|
| 042700 | 72 | Stage2-Actionable | 78 | Stage2-Actionable | improved confidence |
| 089030 | 72 | Stage2-Actionable | 78 | Stage2-Actionable | improved confidence + 4B overlay |
| 319660 | 68 | Stage2 | 59 | Stage1/weak-watch | corrected false positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | HBM_TCBONDER_AND_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_WAFER_EQUIPMENT_PRICE_BETA | 2 | 1 | 2 | 0 | 3 | 0 | 5 | 3 | 2 | true | true | C07 rows 18 -> +3 representative cases; still below 30-row minimum |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, full_4b_requires_non_price_evidence
residual_error_types_found: relative_strength_only_false_positive, late_4b_after_successful_stage2
new_axis_proposed: c07_order_customer_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C07 full-window overheat audit
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- historical price-path calculation from stock-web tradable_raw OHLC
- C07 scope consistency
- duplicate avoidance by symbol/trigger/date
- Stage2-Actionable vs weak-watch differentiation
- 4B timing overlay after successful Stage2 rerating
```

Non-validation scope:

```text
- live/current investment recommendation
- current valuation view
- production scoring update
- external URL-level evidence audit
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c07_order_customer_bridge_required_for_stage2_actionable,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"C07 winners required order/customer-quality bridge; price-only equipment beta created high-MAE false positive.","keeps 042700/089030 positive; demotes 319660 relative-strength-only late entry","C07_R2L90_042700_20240208_STAGE2A|C07_R2L90_089030_20240222_STAGE2A|C07_R2L90_319660_20240711_STAGE2_FALSE_POSITIVE",3,3,1,medium,canonical_shadow_only,"not production; v12 residual candidate"
shadow_weight,full_4b_requires_non_price_evidence,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,1,1,0,"C07 4B should not be price-only, but once valuation/positioning overheat follows an order-backed rerating, timing was useful.","flags 042700 and 089030 near full-window peak without weakening Stage2 bridge","C07_R2L90_042700_20240614_STAGE4B_OVERLAY|C07_R2L90_089030_20240711_STAGE4B_OVERLAY",2,0,0,medium,existing_axis_kept,"stress test only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C07_R2L90_042700_20240208_STAGE2A","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_AND_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_WAFER_EQUIPMENT_PRICE_BETA","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C07_R2L90_042700_20240208_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_with_high_MAE_entry","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"HBM TC-bonder order/relative-strength route; order-quality and customer-capacity bridge visible before later EPS/FCF confirmation"}
{"row_type":"case","case_id":"C07_R2L90_089030_20240222_STAGE2A","symbol":"089030","company_name":"테크윙","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_AND_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_WAFER_EQUIPMENT_PRICE_BETA","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C07_R2L90_089030_20240222_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_but_4b_needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"HBM test-handler / high-performance memory test equipment relative-strength route; order conversion must be separated from generic AI equipment beta"}
{"row_type":"case","case_id":"C07_R2L90_319660_20240711_FALSE_STAGE2","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_AND_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_WAFER_EQUIPMENT_PRICE_BETA","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C07_R2L90_319660_20240711_STAGE2_FALSE_POSITIVE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_MAE_price_only_equipment_beta","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"wafer/process equipment relative-strength label without HBM-specific order bridge; price-only equipment beta failed after entry"}
{"row_type":"trigger","trigger_id":"C07_R2L90_042700_20240208_STAGE2A","case_id":"C07_R2L90_042700_20240208_STAGE2A","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_AND_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_WAFER_EQUIPMENT_PRICE_BETA","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","entry_date":"2024-02-08","entry_price":78500,"evidence_available_at_that_date":"HBM TC-bonder order/relative-strength route; order-quality and customer-capacity bridge visible before later EPS/FCF confirmation","evidence_source":"source_proxy_only__public_order_relative_strength_context__url_pending","evidence_family":"hbm_tcbond_order_relative_strength_with_customer_capacity_bridge","stage2_evidence_fields":["relative_strength","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["confirmed_revision","repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":37.32,"MFE_90D_pct":149.94,"MFE_180D_pct":149.94,"MAE_30D_pct":-23.06,"MAE_90D_pct":-23.06,"MAE_180D_pct":-23.06,"peak_date":"2024-06-14","peak_price":196200,"drawdown_after_peak_pct":-24.26,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"structural_success_with_high_MAE_entry","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C07_R2L90_042700_20240208_STAGE2A","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C07_R2L90_089030_20240222_STAGE2A","case_id":"C07_R2L90_089030_20240222_STAGE2A","symbol":"089030","company_name":"테크윙","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_AND_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_WAFER_EQUIPMENT_PRICE_BETA","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":22300,"evidence_available_at_that_date":"HBM test-handler / high-performance memory test equipment relative-strength route; order conversion must be separated from generic AI equipment beta","evidence_source":"source_proxy_only__public_order_relative_strength_context__url_pending","evidence_family":"hbm_test_handler_order_relative_strength_with_late_4b_drawdown","stage2_evidence_fields":["relative_strength","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["confirmed_revision","repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":69.73,"MFE_90D_pct":217.49,"MFE_180D_pct":217.49,"MAE_30D_pct":-10.4,"MAE_90D_pct":-10.4,"MAE_180D_pct":-10.4,"peak_date":"2024-07-11","peak_price":70800,"drawdown_after_peak_pct":-60.1,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"structural_success_but_4b_needed","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C07_R2L90_089030_20240222_STAGE2A","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C07_R2L90_319660_20240711_STAGE2_FALSE_POSITIVE","case_id":"C07_R2L90_319660_20240711_FALSE_STAGE2","symbol":"319660","company_name":"피에스케이","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_AND_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_WAFER_EQUIPMENT_PRICE_BETA","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-07-11","entry_date":"2024-07-11","entry_price":38600,"evidence_available_at_that_date":"wafer/process equipment relative-strength label without HBM-specific order bridge; price-only equipment beta failed after entry","evidence_source":"source_proxy_only__public_order_relative_strength_context__url_pending","evidence_family":"wafer_equipment_price_beta_without_hbm_order_bridge","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","profile_path":"atlas/symbol_profiles/319/319660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.3,"MFE_90D_pct":1.3,"MFE_180D_pct":1.3,"MAE_30D_pct":-37.82,"MAE_90D_pct":-46.89,"MAE_180D_pct":-47.15,"peak_date":"2024-07-11","peak_price":39100,"drawdown_after_peak_pct":-47.83,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"counterexample_high_MAE_price_only_equipment_beta","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C07_R2L90_319660_20240711_FALSE_STAGE2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C07_R2L90_042700_20240614_STAGE4B_OVERLAY","case_id":"C07_R2L90_042700_20240208_STAGE2A","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_AND_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_WAFER_EQUIPMENT_PRICE_BETA","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":179900,"evidence_available_at_that_date":"valuation/positioning overheat after HBM TC-bonder rerating; full 4B requires non-price order/revision slowdown overlay, not price alone","evidence_source":"source_proxy_only__valuation_positioning_context__url_pending","evidence_family":"hbm_equipment_full_window_4b_after_order_rerating","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.06,"MFE_90D_pct":9.06,"MFE_180D_pct":9.06,"MAE_30D_pct":-17.4,"MAE_90D_pct":-17.4,"MAE_180D_pct":-17.4,"peak_date":"2024-06-14","peak_price":196200,"drawdown_after_peak_pct":-24.26,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.86,"trigger_outcome_label":"good_full_window_4B_timing","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C07_R2L90_042700_20240208_STAGE2A","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same structural case, separate 4B timing overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"C07_R2L90_089030_20240711_STAGE4B_OVERLAY","case_id":"C07_R2L90_089030_20240222_STAGE2A","symbol":"089030","company_name":"테크윙","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_AND_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_WAFER_EQUIPMENT_PRICE_BETA","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-07-11","entry_date":"2024-07-11","entry_price":68700,"evidence_available_at_that_date":"test-handler rerating had reached full-window price proximity; non-price 4B overlay should watch order/revision slowdown and positioning","evidence_source":"source_proxy_only__valuation_positioning_context__url_pending","evidence_family":"hbm_test_handler_full_window_4b_after_order_rerating","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.06,"MFE_90D_pct":3.06,"MFE_180D_pct":3.06,"MAE_30D_pct":-24.31,"MAE_90D_pct":-47.17,"MAE_180D_pct":-58.88,"peak_date":"2024-07-11","peak_price":70800,"drawdown_after_peak_pct":-60.1,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":0.96,"trigger_outcome_label":"good_full_window_4B_timing_after_stage2_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C07_R2L90_089030_20240222_STAGE2A","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same structural case, separate 4B timing overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_R2L90_042700_20240208_STAGE2A","trigger_id":"C07_R2L90_042700_20240208_STAGE2A","symbol":"042700","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":60,"margin_bridge_score":45,"revision_score":50,"relative_strength_score":85,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":35,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":65,"backlog_visibility_score":68,"margin_bridge_score":55,"revision_score":58,"relative_strength_score":85,"customer_quality_score":80,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":30,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C07 shadow profile rewards order/customer-quality bridge and penalizes relative-strength-only equipment beta.","MFE_90D_pct":149.94,"MAE_90D_pct":-23.06,"score_return_alignment_label":"structural_success_with_high_MAE_entry","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_R2L90_089030_20240222_STAGE2A","trigger_id":"C07_R2L90_089030_20240222_STAGE2A","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":60,"margin_bridge_score":45,"revision_score":50,"relative_strength_score":85,"customer_quality_score":70,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":35,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":65,"backlog_visibility_score":68,"margin_bridge_score":55,"revision_score":58,"relative_strength_score":85,"customer_quality_score":80,"policy_or_regulatory_score":0,"valuation_repricing_score":60,"execution_risk_score":30,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C07 shadow profile rewards order/customer-quality bridge and penalizes relative-strength-only equipment beta.","MFE_90D_pct":217.49,"MAE_90D_pct":-10.4,"score_return_alignment_label":"structural_success_but_4b_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_R2L90_319660_20240711_FALSE_STAGE2","trigger_id":"C07_R2L90_319660_20240711_STAGE2_FALSE_POSITIVE","symbol":"319660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":85,"customer_quality_score":25,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":70,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":85,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":80,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":59,"stage_label_after":"Stage1/weak-watch","changed_components":["customer_quality_score","backlog_visibility_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"C07 shadow profile rewards order/customer-quality bridge and penalizes relative-strength-only equipment beta.","MFE_90D_pct":1.3,"MAE_90D_pct":-46.89,"score_return_alignment_label":"counterexample_high_MAE_price_only_equipment_beta","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"coverage_matrix","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCBONDER_AND_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_VS_WAFER_EQUIPMENT_PRICE_BETA","positive_case_count":2,"counterexample_count":1,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":5,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":true,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C07 rows 18 -> +3 representative cases; still below 30-row minimum"}
{"row_type":"residual_contribution","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","full_4b_requires_non_price_evidence"],"residual_error_types_found":["relative_strength_only_false_positive","late_4b_after_successful_stage2"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"C07_R2L90_SOURCE_NOTE","symbol":"MULTI","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","reason":"Evidence URLs remain pending/source-proxy-only; quantitative price paths are stock-web rows, not live investment evidence.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
{"row_type":"shadow_weight","axis":"c07_order_customer_bridge_required_for_stage2_actionable","scope":"canonical_archetype_specific","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","baseline_value":0,"tested_value":1,"delta":"+1","reason":"C07 winners required order/customer-quality bridge; price-only equipment beta created high-MAE false positive.","backtest_effect":"keeps 042700/089030 positive; demotes 319660 relative-strength-only late entry","trigger_ids":"C07_R2L90_042700_20240208_STAGE2A|C07_R2L90_089030_20240222_STAGE2A|C07_R2L90_319660_20240711_STAGE2_FALSE_POSITIVE","calibration_usable_count":3,"new_independent_case_count":3,"counterexample_count":1,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"not production; v12 residual candidate"}
{"row_type":"shadow_weight","axis":"full_4b_requires_non_price_evidence","scope":"canonical_archetype_specific","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","baseline_value":1,"tested_value":1,"delta":"0","reason":"C07 4B should not be price-only, but once valuation/positioning overheat follows an order-backed rerating, the 4B timing was useful.","backtest_effect":"flags 042700 and 089030 near full-window peak without weakening Stage2 bridge","trigger_ids":"C07_R2L90_042700_20240614_STAGE4B_OVERLAY|C07_R2L90_089030_20240711_STAGE4B_OVERLAY","calibration_usable_count":2,"new_independent_case_count":0,"counterexample_count":0,"confidence":"medium","proposal_type":"existing_axis_kept","notes":"stress test only"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
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
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
next_recommended_archetypes:
- C06_HBM_MEMORY_CUSTOMER_CAPACITY
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
- C14_EV_DEMAND_SLOWDOWN_4B_4C
```

## 28. Source Notes

Stock-web row snippets used:

```text
042700 entry row: 2024-02-08 close 78,500; later peak row: 2024-06-14 high 196,200.
089030 entry row: 2024-02-22 close 22,300; later peak row: 2024-07-11 high 70,800; later drawdown row: 2024-12-11 low 28,250.
319660 counterexample row: 2024-07-11 close 38,600 / high 39,100; later drawdown rows include 2024-08-05 low 24,000 and 2024-10-23 low near 20,400.
```

All price rows are from `Songdaiki/stock-web` `atlas/ohlcv_tradable_by_symbol_year` using `tradable_raw` and `raw_unadjusted_marcap`.
