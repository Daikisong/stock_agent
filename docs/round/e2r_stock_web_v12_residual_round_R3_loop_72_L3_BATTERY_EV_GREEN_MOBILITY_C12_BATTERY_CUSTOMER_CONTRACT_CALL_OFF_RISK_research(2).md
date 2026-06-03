# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R3
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R4
computed_next_loop: 72
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: C12_CUSTOMER_CAPEX_ORDER_TO_REVENUE_CALLOFF_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

## 2. Round / Large Sector / Canonical Archetype Scope

R3 maps to `L3_BATTERY_EV_GREEN_MOBILITY`. Inside R3, C12 has enough 4B/4C rows but relatively few bad Stage2 rows versus its positive narrative. This run therefore uses non-top-covered battery-equipment names to test the residual that customer contract / CAPEX optionality must survive call-off and demand-schedule risk before Stage2 can travel into Yellow/Green.

| layer | id | definition |
|---|---|---|
| round | R3 | battery / EV / green mobility |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | battery, EV, green mobility, battery equipment |
| canonical | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | customer contract, call-off, OEM/customer demand risk |
| fine | C12_CUSTOMER_CAPEX_ORDER_TO_REVENUE_CALLOFF_GUARD | customer CAPEX/order-to-revenue must survive call-off risk |
| deep | COATER_CALENDER_EQUIPMENT_CUSTOMER_CAPEX_VISIBILITY | successful equipment order bridge |
| deep | EQUIPMENT_CONTRACT_OPTIONALITY_WITH_CUSTOMER_DEMAND_RISK | contract optionality blowoff / demand risk |
| deep | CUSTOMER_CAPEX_OPTIONALITY_WITHOUT_ORDER_TO_REVENUE_BRIDGE | false-start equipment capex theme |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C12 top-covered symbols are `361610`, `393890`, `336370`, `006110`, `011790`, and `003670`. This run avoids that cluster and fills new-symbol C12 equipment/call-off residual evidence.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C12 | 137400 | new independent | not top-covered C12 symbol; customer CAPEX/order bridge positive |
| C12 | 299030 | new independent | not top-covered C12 symbol; contract optionality / call-off risk blowoff |
| C12 | 131390 | new independent | not top-covered C12 symbol; battery equipment CAPEX false start |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 137400 | 피엔티 | Stage2-Actionable | 2023-05-19 | 51400 | customer CAPEX/order bridge worked |
| failed_rerating_high_MAE_after_blowoff | 299030 | 하나기술 | Stage2-Actionable | 2023-07-24 | 137900 | contract optionality blew off without call-off guard |
| failed_rerating_low_MFE_high_MAE | 131390 | 원익피앤이 | Stage2-Actionable | 2022-01-13 | 31900 | customer CAPEX optionality false start |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 137400 | 피엔티 | Stage2-Actionable | 2023-05-19 | 51400 | 14.98 | 67.51 | 67.51 | -3.11 | -3.11 | -3.11 | 2023-07-26 | 86100 | -37.05 |
| 299030 | 하나기술 | Stage2-Actionable | 2023-07-24 | 137900 | 6.6 | 6.6 | 6.6 | -27.56 | -53.59 | -53.59 | 2023-07-24 | 147000 | -56.46 |
| 131390 | 원익피앤이 | Stage2-Actionable | 2022-01-13 | 31900 | 2.66 | 2.66 | 2.66 | -20.06 | -36.68 | -38.09 | 2022-01-17 | 32750 | -39.69 |

## 9. Case-by-Case Notes

### 9.1 137400 / 피엔티 — customer CAPEX order bridge positive

The entry row is 2023-05-19 at 51,400. The path reaches 86,100 by the 90D/180D window while the initial drawdown remains contained. This is the valid C12 bridge: customer CAPEX/order visibility is the spine; relative strength is only the muscle around it.

### 9.2 299030 / 하나기술 — contract optionality blowoff with call-off risk

The entry row is 2023-07-24 at 137,900, near a local contract/optionality peak. The later path shows shallow additional MFE but deep MAE. This is the classic C12 trap: contract optionality sounds like future revenue, but if customer call-off and demand schedule are not guarded, the price path turns into a cliff.

### 9.3 131390 / 원익피앤이 — battery equipment CAPEX false start

The entry row is 2022-01-13 at 31,900. The 30D/90D/180D MFE stays shallow while MAE deepens quickly. This is not a clean Stage2-to-Yellow path; it is a high-MAE watch pattern caused by customer CAPEX optionality without order-to-revenue conversion.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C12 treats customer contract/CAPEX optionality as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C12 should require call-off-resistant order-to-revenue bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 299030 near the local blowoff. |
| Full 4B non-price requirement appropriate? | Yes. 137400 has a better non-price bridge; 299030/131390 do not. |
| 4C timing issue? | High-MAE watch is useful; no hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
137400:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after customer CAPEX/order bridge
  Stage3-Green = wait for earnings/FCF durability and post-MFE 4B risk check

299030:
  Stage2-Actionable = too generous if based on contract optionality and price strength near peak
  Stage3-Yellow = reject without call-off/demand-schedule protection
  Stage3-Green = reject

131390:
  Stage2-Actionable = too generous if based only on battery equipment CAPEX theme
  Stage3-Yellow = reject without order-to-revenue conversion
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 137400 | 0.93 | 1.00 | good full-window 4B watch after customer CAPEX/order bridge |
| 299030 | 1.00 | 1.00 | price/contract blowoff local 4B watch, not positive stage |
| 131390 | 1.00 | 1.00 | low-MFE high-MAE watch, not full success |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c12_requires_customer_capex_order_to_revenue_calloff_guard

rule:
  For C12 battery-equipment/customer-contract rows, do not promote customer contract or CAPEX optionality
  from Stage2-Actionable into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  call-off-resistant order, customer delivery schedule, order-to-revenue conversion,
  confirmed customer CAPEX restart, recurring order visibility, or margin/FCF conversion.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 25.59 | -31.13 | 66.7% | too generous to optionality / blowoff rows |
| P0b e2r_2_0_baseline_reference | 3 | 25.59 | -31.13 | 33.3% | safer but may miss 137400 |
| P1 sector_specific_candidate_profile | 3 | 25.59 | -31.13 | 66.7% | no broad L3 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 67.51 | -3.11 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected | 4.63 | -45.14 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 137400 | current_profile_correct | customer CAPEX/order bridge aligned with strong MFE |
| 299030 | current_profile_false_positive | contract optionality at blowoff created high MAE |
| 131390 | current_profile_false_positive | CAPEX theme produced low MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12_CUSTOMER_CAPEX_ORDER_TO_REVENUE_CALLOFF_GUARD | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 2 | false | true | C12 non-top-covered equipment/call-off residual reduced |

## 17. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
residual_error_types_found:
- customer contract optionality without call-off guard
- battery equipment false start with low MFE / high MAE
- successful customer CAPEX bridge still needs 4B watch
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- round/sector/canonical consistency
- duplicate avoidance at symbol level
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c12_requires_customer_capex_order_to_revenue_calloff_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"C12 battery-equipment/customer-contract rows should not promote toward Stage3-Yellow/Green unless customer CAPEX/order-to-revenue evidence survives call-off or demand-schedule risk","137400 survives with strong MFE and contained MAE; 299030 and 131390 show price/theme optionality with high MAE or low MFE","TRG_R3L72_C12_137400_20230519_COATER_CAPEX_ORDER_BRIDGE|TRG_R3L72_C12_299030_20230724_CUSTOMER_CONTRACT_BLOWOFF_CALLOFF_RISK|TRG_R3L72_C12_131390_20220113_BATTERY_EQUIPMENT_CAPEX_FALSE_START",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c12_battery_contract_blowoff_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,1,1,0,"Battery equipment contract/capex rows can peak before demand schedule is confirmed; local 4B/high-MAE watch must stay active","prevents 299030 and 131390 from positive Stage3 routing while preserving 137400 positive","TRG_R3L72_C12_137400_20230519_COATER_CAPEX_ORDER_BRIDGE|TRG_R3L72_C12_299030_20230724_CUSTOMER_CONTRACT_BLOWOFF_CALLOFF_RISK|TRG_R3L72_C12_131390_20220113_BATTERY_EQUIPMENT_CAPEX_FALSE_START",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R3L72_C12_137400_20230519_COATER_CAPEX_ORDER_BRIDGE","symbol":"137400","company_name":"피엔티","round":"R3","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_BATTERY_EQUIPMENT_CUSTOMER_CAPEX_ORDER_BRIDGE","deep_sub_archetype_id":"COATER_CALENDER_EQUIPMENT_CUSTOMER_CAPEX_VISIBILITY","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C12 battery-equipment rows require customer CAPEX/order-to-revenue bridge and call-off/demand-schedule guard before Stage2 can travel toward Yellow/Green."}
{"row_type":"case","case_id":"R3L72_C12_299030_20230724_CUSTOMER_CONTRACT_BLOWOFF_CALLOFF_RISK","symbol":"299030","company_name":"하나기술","round":"R3","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_BATTERY_EQUIPMENT_CONTRACT_BLOWOFF_CALLOFF_RISK","deep_sub_archetype_id":"EQUIPMENT_CONTRACT_OPTIONALITY_WITH_CUSTOMER_DEMAND_RISK","case_type":"failed_rerating_high_MAE_after_blowoff","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C12 battery-equipment rows require customer CAPEX/order-to-revenue bridge and call-off/demand-schedule guard before Stage2 can travel toward Yellow/Green."}
{"row_type":"case","case_id":"R3L72_C12_131390_20220113_BATTERY_EQUIPMENT_CAPEX_FALSE_START","symbol":"131390","company_name":"원익피앤이","round":"R3","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_BATTERY_EQUIPMENT_CAPEX_FALSE_START_GUARD","deep_sub_archetype_id":"CUSTOMER_CAPEX_OPTIONALITY_WITHOUT_ORDER_TO_REVENUE_BRIDGE","case_type":"failed_rerating_low_MFE_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C12 battery-equipment rows require customer CAPEX/order-to-revenue bridge and call-off/demand-schedule guard before Stage2 can travel toward Yellow/Green."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R3L72_C12_137400_20230519_COATER_CAPEX_ORDER_BRIDGE","case_id":"R3L72_C12_137400_20230519_COATER_CAPEX_ORDER_BRIDGE","symbol":"137400","company_name":"피엔티","round":"R3","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_BATTERY_EQUIPMENT_CUSTOMER_CAPEX_ORDER_BRIDGE","deep_sub_archetype_id":"COATER_CALENDER_EQUIPMENT_CUSTOMER_CAPEX_VISIBILITY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-19","entry_date":"2023-05-19","entry_price":51400,"evidence_available_at_that_date":"source_proxy_battery_equipment_customer_capex_order_bridge; evidence_url_pending","evidence_source":"source_proxy_battery_equipment_customer_capex_order_bridge; evidence_url_pending","bridge_summary":"battery equipment customer CAPEX/order bridge survived the 90D path and converted into strong MFE","stage2_evidence_fields":["customer_capex_visibility","battery_equipment_order_bridge","relative_strength","non_price_order_quality"],"stage3_evidence_fields":["order_to_revenue_visibility","customer_delivery_schedule","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","customer_capex_cycle_crowding"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/137/137400/2023.csv","profile_path":"atlas/symbol_profiles/137/137400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.98,"MFE_90D_pct":67.51,"MFE_180D_pct":67.51,"MFE_1Y_pct":67.51,"MFE_2Y_pct":67.51,"MAE_30D_pct":-3.11,"MAE_90D_pct":-3.11,"MAE_180D_pct":-3.11,"MAE_1Y_pct":-3.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":86100,"drawdown_after_peak_pct":-37.05,"green_lateness_ratio":"0.31","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_customer_capex_order_bridge","four_b_evidence_type":"non_price_customer_capex_order_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L72_C12_137400_20230519_COATER_CAPEX_ORDER_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R3L72_C12_299030_20230724_CUSTOMER_CONTRACT_BLOWOFF_CALLOFF_RISK","case_id":"R3L72_C12_299030_20230724_CUSTOMER_CONTRACT_BLOWOFF_CALLOFF_RISK","symbol":"299030","company_name":"하나기술","round":"R3","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_BATTERY_EQUIPMENT_CONTRACT_BLOWOFF_CALLOFF_RISK","deep_sub_archetype_id":"EQUIPMENT_CONTRACT_OPTIONALITY_WITH_CUSTOMER_DEMAND_RISK","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-07-24","entry_date":"2023-07-24","entry_price":137900,"evidence_available_at_that_date":"source_proxy_battery_equipment_contract_optionality_without_customer_calloff_guard; evidence_url_pending","evidence_source":"source_proxy_battery_equipment_contract_optionality_without_customer_calloff_guard; evidence_url_pending","bridge_summary":"contract optionality and price strength lacked customer call-off / demand-schedule protection and reversed into high MAE","stage2_evidence_fields":["battery_equipment_contract_optionality","relative_strength","price_blowoff"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","customer_calloff_or_demand_risk","valuation_blowoff"],"stage4c_evidence_fields":["high_MAE_after_contract_optional_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/299/299030/2023.csv","profile_path":"atlas/symbol_profiles/299/299030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.6,"MFE_90D_pct":6.6,"MFE_180D_pct":6.6,"MFE_1Y_pct":6.6,"MFE_2Y_pct":6.6,"MAE_30D_pct":-27.56,"MAE_90D_pct":-53.59,"MAE_180D_pct":-53.59,"MAE_1Y_pct":-53.59,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-24","peak_price":147000,"drawdown_after_peak_pct":-56.46,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_contract_blowoff_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_or_theme_without_calloff_guard","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L72_C12_299030_20230724_CUSTOMER_CONTRACT_BLOWOFF_CALLOFF_RISK_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R3L72_C12_131390_20220113_BATTERY_EQUIPMENT_CAPEX_FALSE_START","case_id":"R3L72_C12_131390_20220113_BATTERY_EQUIPMENT_CAPEX_FALSE_START","symbol":"131390","company_name":"원익피앤이","round":"R3","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_BATTERY_EQUIPMENT_CAPEX_FALSE_START_GUARD","deep_sub_archetype_id":"CUSTOMER_CAPEX_OPTIONALITY_WITHOUT_ORDER_TO_REVENUE_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2022-01-13","entry_date":"2022-01-13","entry_price":31900,"evidence_available_at_that_date":"source_proxy_battery_equipment_customer_capex_optionality_without_order_revenue_bridge; evidence_url_pending","evidence_source":"source_proxy_battery_equipment_customer_capex_optionality_without_order_revenue_bridge; evidence_url_pending","bridge_summary":"battery equipment / customer CAPEX optionality lacked order-to-revenue bridge and produced low MFE with deep MAE","stage2_evidence_fields":["battery_equipment_capex_theme","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","high_MAE_watch"],"stage4c_evidence_fields":["bridge_absent_customer_capex_slowdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131390/2022.csv","profile_path":"atlas/symbol_profiles/131/131390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.66,"MFE_90D_pct":2.66,"MFE_180D_pct":2.66,"MFE_1Y_pct":2.66,"MFE_2Y_pct":2.66,"MAE_30D_pct":-20.06,"MAE_90D_pct":-36.68,"MAE_180D_pct":-38.09,"MAE_1Y_pct":-38.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-01-17","peak_price":32750,"drawdown_after_peak_pct":-39.69,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_MFE_high_MAE_watch_not_full_success","four_b_evidence_type":"price_or_theme_without_calloff_guard","four_c_protection_label":"bridge_absent_watch","trigger_outcome_label":"failed_rerating_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L72_C12_131390_20220113_BATTERY_EQUIPMENT_CAPEX_FALSE_START_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L72_C12_137400_20230519_COATER_CAPEX_ORDER_BRIDGE","trigger_id":"TRG_R3L72_C12_137400_20230519_COATER_CAPEX_ORDER_BRIDGE","symbol":"137400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"customer_capex_visibility_score":12,"contract_calloff_risk_score":8,"order_to_revenue_score":12,"relative_strength_score":10,"valuation_repricing_score":6,"risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"customer_capex_visibility_score":15,"contract_calloff_risk_score":12,"order_to_revenue_score":15,"relative_strength_score":8,"valuation_repricing_score":6,"risk_penalty":4},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["customer_capex_visibility_score","contract_calloff_risk_score","order_to_revenue_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C12 row is promoted only when customer CAPEX/order-to-revenue bridge survives call-off risk.","MFE_90D_pct":67.51,"MAE_90D_pct":-3.11,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L72_C12_299030_20230724_CUSTOMER_CONTRACT_BLOWOFF_CALLOFF_RISK","trigger_id":"TRG_R3L72_C12_299030_20230724_CUSTOMER_CONTRACT_BLOWOFF_CALLOFF_RISK","symbol":"299030","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"customer_capex_visibility_score":8,"contract_calloff_risk_score":1,"order_to_revenue_score":2,"relative_strength_score":11,"valuation_repricing_score":7,"risk_penalty":7},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"customer_capex_visibility_score":4,"contract_calloff_risk_score":0,"order_to_revenue_score":0,"relative_strength_score":5,"valuation_repricing_score":2,"risk_penalty":14},"weighted_score_after":42,"stage_label_after":"Stage1-Watch","changed_components":["customer_capex_visibility_score","contract_calloff_risk_score","order_to_revenue_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C12 guard demotes battery equipment rows when customer call-off/demand schedule and order-to-revenue bridge are absent.","MFE_90D_pct":6.6,"MAE_90D_pct":-53.59,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L72_C12_131390_20220113_BATTERY_EQUIPMENT_CAPEX_FALSE_START","trigger_id":"TRG_R3L72_C12_131390_20220113_BATTERY_EQUIPMENT_CAPEX_FALSE_START","symbol":"131390","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"customer_capex_visibility_score":8,"contract_calloff_risk_score":1,"order_to_revenue_score":2,"relative_strength_score":11,"valuation_repricing_score":7,"risk_penalty":7},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"customer_capex_visibility_score":4,"contract_calloff_risk_score":0,"order_to_revenue_score":0,"relative_strength_score":5,"valuation_repricing_score":2,"risk_penalty":14},"weighted_score_after":42,"stage_label_after":"Stage1-Watch","changed_components":["customer_capex_visibility_score","contract_calloff_risk_score","order_to_revenue_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C12 guard demotes battery equipment rows when customer call-off/demand schedule and order-to-revenue bridge are absent.","MFE_90D_pct":2.66,"MAE_90D_pct":-36.68,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c12_requires_customer_capex_order_to_revenue_calloff_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"C12 battery-equipment/customer-contract rows should not promote toward Stage3-Yellow/Green unless customer CAPEX/order-to-revenue evidence survives call-off or demand-schedule risk","137400 survives with strong MFE and contained MAE; 299030 and 131390 show price/theme optionality with high MAE or low MFE","TRG_R3L72_C12_137400_20230519_COATER_CAPEX_ORDER_BRIDGE|TRG_R3L72_C12_299030_20230724_CUSTOMER_CONTRACT_BLOWOFF_CALLOFF_RISK|TRG_R3L72_C12_131390_20220113_BATTERY_EQUIPMENT_CAPEX_FALSE_START",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c12_battery_contract_blowoff_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,1,1,0,"Battery equipment contract/capex rows can peak before demand schedule is confirmed; local 4B/high-MAE watch must stay active","prevents 299030 and 131390 from positive Stage3 routing while preserving 137400 positive","TRG_R3L72_C12_137400_20230519_COATER_CAPEX_ORDER_BRIDGE|TRG_R3L72_C12_299030_20230724_CUSTOMER_CONTRACT_BLOWOFF_CALLOFF_RISK|TRG_R3L72_C12_131390_20220113_BATTERY_EQUIPMENT_CAPEX_FALSE_START",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"72","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["customer_contract_optionality_without_calloff_guard","battery_equipment_false_start_low_MFE_high_MAE","successful_customer_capex_bridge_needs_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

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

## 22. Next Round State

```text
completed_round = R3
completed_loop = 72
next_round = R4
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/137/137400.json
atlas/symbol_profiles/299/299030.json
atlas/symbol_profiles/131/131390.json
atlas/ohlcv_tradable_by_symbol_year/137/137400/2023.csv
atlas/ohlcv_tradable_by_symbol_year/299/299030/2023.csv
atlas/ohlcv_tradable_by_symbol_year/131/131390/2022.csv
```

This loop adds 3 new independent C12 cases, 1 positive, 2 counterexamples, and 1 canonical-archetype residual guard candidate for R3/L3.
