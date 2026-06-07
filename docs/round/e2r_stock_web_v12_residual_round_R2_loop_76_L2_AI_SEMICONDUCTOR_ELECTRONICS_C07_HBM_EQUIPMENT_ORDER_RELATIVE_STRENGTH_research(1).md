# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
selected_round: R2
selected_loop: 76
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_TCB_BONDER_ORDER_RELATIVE_STRENGTH_4B_WATCH
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual error types for R2/L2/C07.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C07:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C07 -> C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

C07 is interpreted as HBM / advanced packaging / test-handler equipment where order-route and relative strength can be early, but Green requires order conversion, customer/revision bridge, and margin durability.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C07 current rows | 18 |
| C07 current symbols | 16 |
| C07 good/bad Stage2 | 5 / 3 |
| C07 4B/4C | 2 / 1 |
| C07 URL pending/proxy | 18 / 15 |
| top covered symbols | 084370, 232140, 036200, 036930, 039030, 039440 |

Selected symbols avoid the C07 top-covered symbols:

| symbol | company | status |
|---|---|---|
| 042700 | 한미반도체 | new C07 symbol versus top-covered C07 list |
| 089030 | 테크윙 | new C07 symbol versus top-covered C07 list |
| 064290 | 인텍플러스 | new C07 symbol versus top-covered C07 list |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 042700 / 2024-02-08 | true | true | clean_180D_window | true |
| 089030 / 2024-02-22 | true | true | clean_180D_window | true |
| 064290 / 2024-02-20 | true | true | clean_180D_window | true |

Corporate-action notes:

- 한미반도체 has corporate-action candidates in 2006, 2017, and 2022; selected 2024 window is clean.
- 테크윙 has corporate-action candidates in 2011 and 2022; selected 2024 window is clean.
- 인텍플러스 has zero corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| HBM_TCB_BONDER_ORDER_RELATIVE_STRENGTH_4B_WATCH | C07 | HBM bonding equipment order/RS route; 4B audit after rerating |
| HBM_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_4B_WATCH | C07 | HBM test-handler order/RS route; 4B audit after rerating |
| INSPECTION_EQUIPMENT_ORDER_BRIDGE_ABSENT_FALSE_POSITIVE | C07 | inspection-equipment beta without order/revision bridge |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C07_HANMI_042700_2024_02_08_HBM_TCB_BONDER_ORDER_RS | 042700 | 한미반도체 | 4B_overlay_success | positive | extreme HBM equipment MFE but 4B audit required |
| C07_TECHWING_089030_2024_02_22_HBM_TEST_HANDLER_ORDER_RS | 089030 | 테크윙 | high_mae_success | positive | test-handler relative strength produced extreme MFE and later peak drawdown |
| C07_INTEK_064290_2024_02_20_INSPECTION_EQUIP_BETA_FALSE_POSITIVE | 064290 | 인텍플러스 | failed_rerating | counterexample | inspection-equipment beta without bridge produced modest MFE and high MAE |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass:

```text
positive_case_count >= 1
counterexample_count >= 1
calibration_usable_case_count >= 3
new_independent_case_ratio = 1.00
```

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 042700 | source_proxy_only | HBM TCB bonder / equipment order route; order bridge partial | required before promotion |
| 089030 | source_proxy_only | HBM test-handler order route; order bridge partial | required before promotion |
| 064290 | source_proxy_only | inspection-equipment beta but order/revision bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 042700 | atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv | atlas/symbol_profiles/042/042700.json |
| 089030 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json |
| 064290 | atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv | atlas/symbol_profiles/064/064290.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HANMI_042700_2024_02_08_STAGE2A_HBM_TCB_BONDER_ORDER_RS | Stage2-Actionable | 2024-02-08 | 2024-02-08 | 78500 | HBM TCB bonder/order relative strength |
| TECHWING_089030_2024_02_22_STAGE2A_HBM_TEST_HANDLER_ORDER_RS | Stage2-Actionable | 2024-02-22 | 2024-02-22 | 22300 | HBM test-handler order relative strength |
| INTEK_064290_2024_02_20_STAGE2_FALSE_POSITIVE_INSPECTION_EQUIP_BETA | Stage2 | 2024-02-20 | 2024-02-20 | 35750 | inspection-equipment beta without order/revision bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 042700 | 2024-02-08 | 78500 | 49.43 | -9.94 | 150.00 | -9.94 | 150.00 | -9.94 | 2024-06-14 | 196200 | -54.33 |
| 089030 | 2024-02-22 | 22300 | 69.73 | -10.40 | 211.66 | -10.40 | 217.49 | -10.40 | 2024-07-11 | 70800 | -57.63 |
| 064290 | 2024-02-20 | 35750 | 14.27 | -11.47 | 14.27 | -41.26 | 14.27 | -49.51 | 2024-03-06 | 40850 | -55.81 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 042700 | Stage2A/Yellow possible; 4B after rerating | extreme MFE then deep peak drawdown | current_profile_4B_too_late |
| 089030 | Stage2A/Yellow possible; 4B after rerating | extreme MFE then deep peak drawdown | current_profile_4B_too_late |
| 064290 | Stage2 risk if inspection beta is over-credited | modest MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C07 interpretation:

- Stage2A can work when HBM equipment relative strength is backed by an order/customer route.
- Yellow/Green require order conversion, revision bridge, and margin durability.
- Equipment beta without order/revision bridge should not be upgraded.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 042700 | 1.00 | 1.00 | valuation / positioning | good 4B audit after HBM equipment rerating |
| 089030 | 1.00 | 1.00 | valuation / positioning | good 4B audit after HBM test-handler rerating |
| 064290 | 1.00 | 1.00 | price_only / bridge absent | local peak without order bridge is not full 4B |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 042700 | thesis_break_watch_only | not hard 4C, but valuation cap needed |
| 089030 | thesis_break_watch_only | not hard 4C, but valuation cap needed |
| 064290 | hard_4c_late | order/revision bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = low_to_medium
```

Candidate:

> In L2 HBM equipment names, Stage2A can be supported by order-route relative strength. However, Stage3-Yellow/Green requires order conversion, named customer capacity bridge, revision, and margin durability. If the signal is only inspection-equipment beta or relative strength without order/revision bridge, cap at Stage1/Stage2-watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
confidence = low_to_medium
```

Candidate C07 rule:

```text
C07_order_relative_strength_bridge_required =
  hbm_equipment_order_route
  AND (customer_capacity_bridge OR order_conversion OR confirmed_revision OR margin_bridge)

if equipment_beta_or_relative_strength and order_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 80 and drawdown_after_peak < -40:
    add C07_peak_proximity_4B_audit = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 125.31 | -20.53 | 127.25 | -23.28 | 1 | useful but order bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 125.31 | -20.53 | 127.25 | -23.28 | 1 | over-credits equipment beta |
| P1 sector_specific_candidate_profile | L2 | 2 promoted + 1 guard | 180.83 | -10.17 | 183.75 | -10.17 | 0 | better after bridge gate |
| P2 canonical_archetype_candidate_profile | C07 | 2 promoted + 1 guard | 180.83 | -10.17 | 183.75 | -10.17 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C07 guard | 2 promoted + 1 guard | 180.83 | -10.17 | 183.75 | -10.17 | 0 | adds order/revision bridge gate |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 042700 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 089030 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 064290 | Stage2 false positive if order bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | mixed C07 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | 18 -> projected 21 rows; still need 9 to reach 30 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed: C07_order_relative_strength_bridge_required|C07_peak_proximity_4B_audit
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable OHLC rows.
- Uses manifest max_date 2026-02-20.
- Uses clean 180D windows.
- Uses C07 Priority 0 coverage gap.
- Uses three symbols not listed among C07 top-covered symbols.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C07_order_relative_strength_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"064290 shows equipment beta can fail without order/revision bridge","blocks 064290 false positive while preserving 042700/089030 Stage2A","HANMI_042700_2024_02_08_STAGE2A_HBM_TCB_BONDER_ORDER_RS|TECHWING_089030_2024_02_22_STAGE2A_HBM_TEST_HANDLER_ORDER_RS|INTEK_064290_2024_02_20_STAGE2_FALSE_POSITIVE_INSPECTION_EQUIP_BETA",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C07_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"042700/089030 extreme HBM equipment MFE still needed 4B audit after valuation extension","adds 4B audit after large C07 MFE without turning price-only peaks into full 4B","HANMI_042700_2024_02_08_STAGE2A_HBM_TCB_BONDER_ORDER_RS|TECHWING_089030_2024_02_22_STAGE2A_HBM_TEST_HANDLER_ORDER_RS",2,2,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C07_HANMI_042700_2024_02_08_HBM_TCB_BONDER_ORDER_RS","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCB_BONDER_ORDER_RELATIVE_STRENGTH_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"HANMI_042700_2024_02_08_STAGE2A_HBM_TCB_BONDER_ORDER_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2A captured exceptional HBM equipment rerating; later peak-to-drawdown requires C07 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C07 symbol versus top-covered C07 list; source_proxy_only evidence, URL repair required before promotion"}
{"row_type":"case","case_id":"C07_TECHWING_089030_2024_02_22_HBM_TEST_HANDLER_ORDER_RS","symbol":"089030","company_name":"테크윙","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_4B_WATCH","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TECHWING_089030_2024_02_22_STAGE2A_HBM_TEST_HANDLER_ORDER_RS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"HBM test-handler relative strength produced extreme MFE but needed 4B audit after peak","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C07 symbol; source_proxy_only evidence"}
{"row_type":"case","case_id":"C07_INTEK_064290_2024_02_20_INSPECTION_EQUIP_BETA_FALSE_POSITIVE","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"INSPECTION_EQUIPMENT_ORDER_BRIDGE_ABSENT_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"INTEK_064290_2024_02_20_STAGE2_FALSE_POSITIVE_INSPECTION_EQUIP_BETA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Inspection-equipment beta showed only modest MFE and then large MAE when order/revision bridge did not appear","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C07 symbol; counterexample for equipment beta without order/revision bridge"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HANMI_042700_2024_02_08_STAGE2A_HBM_TCB_BONDER_ORDER_RS","case_id":"C07_HANMI_042700_2024_02_08_HBM_TCB_BONDER_ORDER_RS","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TCB_BONDER_ORDER_RELATIVE_STRENGTH_4B_WATCH","sector":"AI/semiconductor/electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","entry_date":"2024-02-08","entry_price":78500.0,"evidence_available_at_that_date":"source_proxy_only: HBM TCB bonder / advanced packaging equipment order narrative and clear relative strength; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_equipment_route","order_route","relative_strength","customer_capacity_beta"],"stage3_evidence_fields":["order_conversion_partial","revision_bridge_pending","margin_bridge_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":49.43,"MFE_90D_pct":150.0,"MFE_180D_pct":150.0,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-9.94,"MAE_90D_pct":-9.94,"MAE_180D_pct":-9.94,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":196200.0,"drawdown_after_peak_pct":-54.33,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_HBM_equipment_order_rerating","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C07_042700_2024_02_08_78500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TECHWING_089030_2024_02_22_STAGE2A_HBM_TEST_HANDLER_ORDER_RS","case_id":"C07_TECHWING_089030_2024_02_22_HBM_TEST_HANDLER_ORDER_RS","symbol":"089030","company_name":"테크윙","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_TEST_HANDLER_ORDER_RELATIVE_STRENGTH_4B_WATCH","sector":"AI/semiconductor/electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":22300.0,"evidence_available_at_that_date":"source_proxy_only: HBM test-handler equipment route and strong relative strength; order/revision bridge partial; URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_test_handler_route","order_route","relative_strength","sector_hbm_beta"],"stage3_evidence_fields":["order_conversion_partial","revision_bridge_pending","margin_bridge_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":69.73,"MFE_90D_pct":211.66,"MFE_180D_pct":217.49,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-10.4,"MAE_90D_pct":-10.4,"MAE_180D_pct":-10.4,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800.0,"drawdown_after_peak_pct":-57.63,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_HBM_test_handler_order_rerating","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C07_089030_2024_02_22_22300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"INTEK_064290_2024_02_20_STAGE2_FALSE_POSITIVE_INSPECTION_EQUIP_BETA","case_id":"C07_INTEK_064290_2024_02_20_INSPECTION_EQUIP_BETA_FALSE_POSITIVE","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"INSPECTION_EQUIPMENT_ORDER_BRIDGE_ABSENT_FALSE_POSITIVE","sector":"AI/semiconductor/electronics","primary_archetype":"hbm_equipment_order_relative_strength","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":35750.0,"evidence_available_at_that_date":"source_proxy_only: semiconductor inspection equipment beta and relative strength, but order/revision bridge absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["inspection_equipment_beta","relative_strength"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_only_local_peak","order_bridge_absent"],"stage4c_evidence_fields":["order_revision_bridge_absent","margin_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.27,"MFE_90D_pct":14.27,"MFE_180D_pct":14.27,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-11.47,"MAE_90D_pct":-41.26,"MAE_180D_pct":-49.51,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-06","peak_price":40850.0,"drawdown_after_peak_pct":-55.81,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_without_order_bridge_not_full_4B","four_b_evidence_type":["price_only","order_bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_modest_mfe_high_mae_order_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C07_064290_2024_02_20_35750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_HANMI_042700_2024_02_08_HBM_TCB_BONDER_ORDER_RS","trigger_id":"HANMI_042700_2024_02_08_STAGE2A_HBM_TCB_BONDER_ORDER_RS","symbol":"042700","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":10,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":10,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable with mandatory 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Extreme MFE confirms HBM equipment order RS worked, but rapid valuation extension must cap Green and trigger 4B audit.","MFE_90D_pct":150.0,"MAE_90D_pct":-9.94,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_TECHWING_089030_2024_02_22_HBM_TEST_HANDLER_ORDER_RS","trigger_id":"TECHWING_089030_2024_02_22_STAGE2A_HBM_TEST_HANDLER_ORDER_RS","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable with mandatory 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"HBM test-handler route produced very high MFE; valuation room should decay after peak proximity without confirmed full order/revision bridge.","MFE_90D_pct":211.66,"MAE_90D_pct":-10.4,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_INTEK_064290_2024_02_20_INSPECTION_EQUIP_BETA_FALSE_POSITIVE","trigger_id":"INTEK_064290_2024_02_20_STAGE2_FALSE_POSITIVE_INSPECTION_EQUIP_BETA","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":64,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":51,"stage_label_after":"Stage1/4B-watch, not Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Inspection-equipment beta without order/revision bridge created only modest MFE and then deep MAE.","MFE_90D_pct":14.27,"MAE_90D_pct":-41.26,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R2
completed_loop = 76
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C, C11_BATTERY_ORDERBOOK_RERATING
```

If this loop is accepted, C07 moves from 18 to a projected 21 rows. It remains below 30-row minimum stability, but the next run should re-read the latest No-Repeat Index before selecting another C07 case.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/042/042700.json
  - atlas/symbol_profiles/089/089030.json
  - atlas/symbol_profiles/064/064290.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
