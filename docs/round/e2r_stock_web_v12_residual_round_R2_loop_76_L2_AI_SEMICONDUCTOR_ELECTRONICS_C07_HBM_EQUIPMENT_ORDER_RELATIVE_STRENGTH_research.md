# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R2
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R3
computed_next_loop: 76
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: C07_CUSTOMER_ORDER_CAPACITY_UTILIZATION_MARGIN_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
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

R2 maps directly to `L2_AI_SEMICONDUCTOR_ELECTRONICS`. The previous R2 loop used C10 memory-recovery equipment-cycle, so this run rotates to C07 HBM/equipment order-relative-strength. The chosen fine branch separates actual customer order / capacity / utilization / margin bridges from equipment-theme MFE that later decays into high-MAE.

| layer | id | definition |
|---|---|---|
| round | R2 | AI / semiconductor / electronics |
| large_sector | L2_AI_SEMICONDUCTOR_ELECTRONICS | semiconductor, AI/HBM, equipment and electronic supply chain |
| canonical | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | HBM/equipment order and relative strength |
| fine | C07_CUSTOMER_ORDER_CAPACITY_UTILIZATION_MARGIN_BRIDGE_GUARD | HBM/equipment signal must become order, capacity, utilization, margin evidence |
| deep | HBM_REFLOW_AND_ADVANCED_PACKAGING_EQUIPMENT_ORDER_TO_MARGIN_AND_RELATIVE_STRENGTH | HBM reflow equipment positive |
| deep | ADVANCED_PROCESS_CONSUMABLE_AND_CUSTOMER_CAPACITY_RECOVERY_TO_MARGIN_OPERATING_LEVERAGE | process consumable positive |
| deep | SUBFAB_CHILLER_EQUIPMENT_HBM_OPTIONALITY_WITHOUT_REPEAT_ORDER_UTILIZATION_MARGIN_CASHFLOW_CONVERSION | subfab/chiller false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C07 top-covered symbols are `UNKNOWN_SYMBOL`, `232140`, `031980`, `042700`, `003160`, and `089030`. This run avoids that cluster and also avoids the immediately previous R2/C10 representatives `114810`, `083310`, and `089970`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C07 | 039440 | new independent | not top-covered C07 symbol; HBM reflow / advanced packaging order-margin bridge |
| C07 | 064760 | new independent | not top-covered C07 symbol; advanced-process consumable/customer capacity margin bridge |
| C07 | 036200 | new independent | not top-covered C07 symbol; subfab/chiller equipment MFE without durable repeat-order/margin bridge |

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

Corporate-action caveat:

```text
039440 has corporate-action candidates ending 2018-04-20, outside the selected 2024 representative window.
064760 has no corporate-action candidate dates.
036200 has corporate-action candidates ending 2017-01-11, outside the selected 2024 representative window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| HBM_reflow_equipment_order_success_then_4B_high_MAE_watch | 039440 | 에스티아이 | Stage2-Actionable | 2024-02-13 | 33650 | HBM reflow/advanced packaging order bridge worked, but full-window high-MAE blocked Green |
| process_consumable_capacity_success_then_4B_drawdown_watch | 064760 | 티씨케이 | Stage2-Actionable | 2024-03-21 | 106000 | customer capacity/process-consumable margin bridge worked, but late drawdown guard required |
| subfab_equipment_MFE_then_high_MAE_counterexample | 036200 | 유니셈 | Stage2-Actionable | 2024-03-12 | 9540 | equipment-theme MFE lacked durable repeat-order/utilization/margin bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 039440 | 에스티아이 | Stage2-Actionable | 2024-02-13 | 33650 | 28.53 | 28.53 | 28.53 | -6.09 | -7.58 | -40.56 | 2024-03-13 | 43250 | -53.76 |
| 064760 | 티씨케이 | Stage2-Actionable | 2024-03-21 | 106000 | 33.11 | 41.42 | 41.42 | -0.94 | -0.94 | -36.32 | 2024-06-14 | 149900 | -54.97 |
| 036200 | 유니셈 | Stage2-Actionable | 2024-03-12 | 9540 | 25.26 | 30.82 | 30.82 | -9.43 | -9.43 | -41.93 | 2024-07-04 | 12480 | -55.61 |

## 9. Case-by-Case Notes

### 9.1 039440 / 에스티아이 — HBM reflow equipment order bridge

The entry row is 2024-02-13 at 33,650. The local path reached 43,250 and later fell to 20,000. This is a valid C07 positive only as guarded Yellow: HBM reflow and advanced packaging equipment optionality had a customer-order/margin bridge, but the path also shows why 4B/high-MAE must block Green.

### 9.2 064760 / 티씨케이 — advanced-process consumable customer capacity bridge

The entry row is 2024-03-21 at 106,000. The early path reached 141,100 and the 90D/180D path reached 149,900. This case is not a pure price burst; it reflects customer-capacity recovery, advanced-process consumable pull-through and margin operating leverage. The later fall to 67,500 still makes it a guarded positive, not a Green loosening case.

### 9.3 036200 / 유니셈 — subfab/chiller equipment MFE without durable bridge

The entry row is 2024-03-12 at 9,540. The stock later reached 12,480, but the 180D low fell to 5,540. This is the C07 trap: HBM/equipment beta and subfab/chiller theme can make MFE, yet without repeat order, utilization, margin and cashflow bridge, the move should be routed to Watch/4B/high-MAE.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C07 treats equipment/HBM MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C07 needs order/capacity/utilization/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 036200 and the post-peak paths of 039440/064760. |
| Full 4B non-price requirement appropriate? | Yes. 039440/064760 have non-price bridges; 036200 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
039440:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after HBM reflow / customer order / margin bridge
  Stage3-Green = reject because full-window high-MAE remains active

064760:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after customer capacity / utilization / margin bridge
  Stage3-Green = reject because post-peak drawdown and cycle risk remain active

036200:
  Stage2-Actionable = acceptable only as equipment-theme watch
  Stage3-Yellow = reject without repeat order, utilization, margin and cashflow bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 039440 | 1.00 | 1.00 | HBM reflow order bridge positive but full-window 4B/high-MAE watch |
| 064760 | 0.94 | 1.00 | process-consumable capacity bridge positive but full-window 4B/high-MAE watch |
| 036200 | 0.96 | 1.00 | subfab equipment MFE but no durable order/margin bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c07_requires_customer_order_capacity_utilization_margin_bridge

rule:
  For C07 HBM/equipment order-relative-strength rows, do not promote HBM,
  equipment, reflow, advanced packaging, subfab, chiller, process consumable,
  or equipment-cycle Stage2 signals into Stage3-Yellow/Green unless at least one
  non-price bridge is visible:
  customer order, repeat order, capacity pull-through, utilization recovery,
  customer qualification, margin conversion, operating leverage, FCF/cash conversion,
  or earnings revision tied to equipment economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 33.59 | -5.98 | 33.3% | useful but can over-credit equipment-theme MFE |
| P0b e2r_2_0_baseline_reference | 3 | 33.59 | -5.98 | 0% | safer but may miss 039440/064760 |
| P1 sector_specific_candidate_profile | 3 | 33.59 | -5.98 | 33.3% | no broad L2 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 34.98 | -4.26 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected/watch | 30.82 | -9.43 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 039440 | current_profile_correct_but_no_green | order/margin bridge aligned with MFE, but high-MAE blocks Green |
| 064760 | current_profile_correct_with_drawdown_guard | capacity/margin bridge aligned with MFE, but drawdown guard remains |
| 036200 | current_profile_false_positive_if_green | subfab/chiller equipment MFE lacked durable repeat-order/margin bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | C07_CUSTOMER_ORDER_CAPACITY_UTILIZATION_MARGIN_BRIDGE_GUARD | 2 | 1 | 3 | 3 | 3 | 0 | 3 | 3 | 1 | false | true | R2/C07 non-top-covered HBM/equipment order residual reduced |

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
- equipment theme without repeat-order/margin bridge
- HBM reflow order winner needs 4B watch
- process-consumable capacity winner needs drawdown guard
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
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
- R2 direct L2 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact customer-order or equipment-supply announcement URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c07_requires_customer_order_capacity_utilization_margin_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"C07 HBM/equipment rows should not promote toward Stage3-Yellow/Green unless HBM/equipment or advanced-process signal converts into customer order, repeat order, capacity pull-through, utilization, margin, operating leverage, or cashflow bridge","039440 and 064760 survive as guarded positives after order/capacity/margin bridge; 036200 is demoted because subfab/chiller equipment MFE lacked durable repeat-order and margin bridge","TRG_R2L76_C07_039440_20240213_HBM_REFLOW_EQUIPMENT_ORDER_MARGIN_BRIDGE|TRG_R2L76_C07_064760_20240321_PROCESS_CONSUMABLE_CUSTOMER_CAPACITY_MARGIN_BRIDGE|TRG_R2L76_C07_036200_20240312_SUBFAB_CHILLER_EQUIPMENT_THEME_NO_DURABLE_ORDER_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c07_equipment_cycle_4b_high_mae_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,1,1,0,"HBM/equipment winners and equipment-theme false starts can peak before order/utilization/margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 039440/064760 guarded positives while preventing 036200 equipment-theme false positive","TRG_R2L76_C07_039440_20240213_HBM_REFLOW_EQUIPMENT_ORDER_MARGIN_BRIDGE|TRG_R2L76_C07_064760_20240321_PROCESS_CONSUMABLE_CUSTOMER_CAPACITY_MARGIN_BRIDGE|TRG_R2L76_C07_036200_20240312_SUBFAB_CHILLER_EQUIPMENT_THEME_NO_DURABLE_ORDER_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R2L76_C07_039440_20240213_HBM_REFLOW_EQUIPMENT_ORDER_MARGIN_BRIDGE","symbol":"039440","company_name":"에스티아이","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_REFLOW_EQUIPMENT_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"HBM_REFLOW_AND_ADVANCED_PACKAGING_EQUIPMENT_ORDER_TO_MARGIN_AND_RELATIVE_STRENGTH","case_type":"HBM_reflow_equipment_order_success_then_4B_high_MAE_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_with_late_guard","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C07 HBM/equipment order rows require customer order, repeat order, capacity pull-through, utilization, margin, operating leverage, or cashflow bridge; HBM/equipment theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R2L76_C07_064760_20240321_PROCESS_CONSUMABLE_CUSTOMER_CAPACITY_MARGIN_BRIDGE","symbol":"064760","company_name":"티씨케이","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_PROCESS_CONSUMABLE_CUSTOMER_CAPACITY_MARGIN_BRIDGE","deep_sub_archetype_id":"ADVANCED_PROCESS_CONSUMABLE_AND_CUSTOMER_CAPACITY_RECOVERY_TO_MARGIN_OPERATING_LEVERAGE","case_type":"process_consumable_capacity_success_then_4B_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard","price_source":"Songdaiki/stock-web","notes":"C07 HBM/equipment order rows require customer order, repeat order, capacity pull-through, utilization, margin, operating leverage, or cashflow bridge; HBM/equipment theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R2L76_C07_036200_20240312_SUBFAB_CHILLER_EQUIPMENT_THEME_NO_DURABLE_ORDER_BRIDGE","symbol":"036200","company_name":"유니셈","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_SUBFAB_CHILLER_EQUIPMENT_THEME_WITHOUT_DURABLE_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"SUBFAB_CHILLER_EQUIPMENT_HBM_OPTIONALITY_WITHOUT_REPEAT_ORDER_UTILIZATION_MARGIN_CASHFLOW_CONVERSION","case_type":"subfab_equipment_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C07 HBM/equipment order rows require customer order, repeat order, capacity pull-through, utilization, margin, operating leverage, or cashflow bridge; HBM/equipment theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R2L76_C07_039440_20240213_HBM_REFLOW_EQUIPMENT_ORDER_MARGIN_BRIDGE","case_id":"R2L76_C07_039440_20240213_HBM_REFLOW_EQUIPMENT_ORDER_MARGIN_BRIDGE","symbol":"039440","company_name":"에스티아이","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_REFLOW_EQUIPMENT_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"HBM_REFLOW_AND_ADVANCED_PACKAGING_EQUIPMENT_ORDER_TO_MARGIN_AND_RELATIVE_STRENGTH","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":33650,"evidence_available_at_that_date":"source_proxy_HBM_reflow_advanced_packaging_equipment_order_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_HBM_reflow_advanced_packaging_equipment_order_margin_bridge; evidence_url_pending","bridge_summary":"HBM reflow/advanced-packaging equipment signal converted into order and margin optionality, but the post-peak path showed valuation and cycle drawdown risk requiring 4B/high-MAE watch","stage2_evidence_fields":["HBM_reflow_equipment","advanced_packaging_order_proxy","relative_strength","margin_bridge_proxy"],"stage3_evidence_fields":["customer_order_to_revenue_visibility","HBM_packaging_equipment_margin_bridge","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","equipment_cycle_crowding","customer_order_timing_risk"],"stage4c_evidence_fields":["post_peak_high_MAE_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv","profile_path":"atlas/symbol_profiles/039/039440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.53,"MFE_90D_pct":28.53,"MFE_180D_pct":28.53,"MFE_1Y_pct":28.53,"MFE_2Y_pct":28.53,"MAE_30D_pct":-6.09,"MAE_90D_pct":-7.58,"MAE_180D_pct":-40.56,"MAE_1Y_pct":-40.56,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":43250,"drawdown_after_peak_pct":-53.76,"green_lateness_ratio":"0.28","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"HBM_reflow_order_bridge_positive_but_full_window_4B_high_MAE_watch","four_b_evidence_type":"non_price_order_capacity_margin_bridge","four_c_protection_label":"post_peak_high_MAE_watch","trigger_outcome_label":"HBM_reflow_equipment_order_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L76_C07_039440_20240213_HBM_REFLOW_EQUIPMENT_ORDER_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L76_C07_064760_20240321_PROCESS_CONSUMABLE_CUSTOMER_CAPACITY_MARGIN_BRIDGE","case_id":"R2L76_C07_064760_20240321_PROCESS_CONSUMABLE_CUSTOMER_CAPACITY_MARGIN_BRIDGE","symbol":"064760","company_name":"티씨케이","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_PROCESS_CONSUMABLE_CUSTOMER_CAPACITY_MARGIN_BRIDGE","deep_sub_archetype_id":"ADVANCED_PROCESS_CONSUMABLE_AND_CUSTOMER_CAPACITY_RECOVERY_TO_MARGIN_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":106000,"evidence_available_at_that_date":"source_proxy_advanced_process_consumable_customer_capacity_recovery_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_advanced_process_consumable_customer_capacity_recovery_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"advanced-process consumable/customer capacity recovery converted into margin and operating-leverage bridge, but the later semi-cycle drawdown required 4B and high-MAE watch","stage2_evidence_fields":["advanced_process_consumable","customer_capacity_recovery_proxy","relative_strength","margin_leverage_proxy"],"stage3_evidence_fields":["customer_capacity_to_revenue_visibility","consumable_margin_bridge","operating_leverage_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","process_consumable_cycle_crowding","customer_utilization_risk"],"stage4c_evidence_fields":["post_peak_high_MAE_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv","profile_path":"atlas/symbol_profiles/064/064760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":33.11,"MFE_90D_pct":41.42,"MFE_180D_pct":41.42,"MFE_1Y_pct":41.42,"MFE_2Y_pct":41.42,"MAE_30D_pct":-0.94,"MAE_90D_pct":-0.94,"MAE_180D_pct":-36.32,"MAE_1Y_pct":-36.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":149900,"drawdown_after_peak_pct":-54.97,"green_lateness_ratio":"0.46","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"process_consumable_capacity_bridge_positive_but_full_window_4B_high_MAE_watch","four_b_evidence_type":"non_price_order_capacity_margin_bridge","four_c_protection_label":"post_peak_high_MAE_watch","trigger_outcome_label":"process_consumable_capacity_success_then_4B_watch","current_profile_verdict":"current_profile_correct_with_drawdown_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L76_C07_064760_20240321_PROCESS_CONSUMABLE_CUSTOMER_CAPACITY_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R2L76_C07_036200_20240312_SUBFAB_CHILLER_EQUIPMENT_THEME_NO_DURABLE_ORDER_BRIDGE","case_id":"R2L76_C07_036200_20240312_SUBFAB_CHILLER_EQUIPMENT_THEME_NO_DURABLE_ORDER_BRIDGE","symbol":"036200","company_name":"유니셈","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_SUBFAB_CHILLER_EQUIPMENT_THEME_WITHOUT_DURABLE_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"SUBFAB_CHILLER_EQUIPMENT_HBM_OPTIONALITY_WITHOUT_REPEAT_ORDER_UTILIZATION_MARGIN_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":9540,"evidence_available_at_that_date":"source_proxy_subfab_chiller_equipment_HBM_optionality_without_repeat_order_utilization_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_subfab_chiller_equipment_HBM_optionality_without_repeat_order_utilization_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"subfab/chiller equipment and HBM optionality produced MFE, but repeat order, utilization, margin and cashflow bridge did not persist through the cycle","stage2_evidence_fields":["subfab_equipment_theme","HBM_equipment_beta","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["MFE_peak_watch","repeat_order_bridge_absent","utilization_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_order_margin_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv","profile_path":"atlas/symbol_profiles/036/036200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.26,"MFE_90D_pct":30.82,"MFE_180D_pct":30.82,"MFE_1Y_pct":30.82,"MFE_2Y_pct":30.82,"MAE_30D_pct":-9.43,"MAE_90D_pct":-9.43,"MAE_180D_pct":-41.93,"MAE_1Y_pct":-41.93,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-04","peak_price":12480,"drawdown_after_peak_pct":-55.61,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"subfab_equipment_MFE_but_no_durable_order_margin_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"HBM_equipment_theme_without_durable_order_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"subfab_equipment_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L76_C07_036200_20240312_SUBFAB_CHILLER_EQUIPMENT_THEME_NO_DURABLE_ORDER_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L76_C07_039440_20240213_HBM_REFLOW_EQUIPMENT_ORDER_MARGIN_BRIDGE","trigger_id":"TRG_R2L76_C07_039440_20240213_HBM_REFLOW_EQUIPMENT_ORDER_MARGIN_BRIDGE","symbol":"039440","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"HBM_equipment_score":12,"customer_order_score":11,"capacity_utilization_score":10,"margin_cashflow_score":10,"relative_strength_score":11,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"HBM_equipment_score":15,"customer_order_score":14,"capacity_utilization_score":13,"margin_cashflow_score":13,"relative_strength_score":8,"theme_risk_penalty":9},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["HBM_equipment_score","customer_order_score","capacity_utilization_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C07 row is promoted only because HBM/equipment or process-consumable signal converts into customer order, capacity, utilization and margin bridge; high-MAE/full-window 4B blocks Green.","MFE_90D_pct":28.53,"MAE_90D_pct":-7.58,"score_return_alignment_label":"score_return_aligned_with_late_guard","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L76_C07_064760_20240321_PROCESS_CONSUMABLE_CUSTOMER_CAPACITY_MARGIN_BRIDGE","trigger_id":"TRG_R2L76_C07_064760_20240321_PROCESS_CONSUMABLE_CUSTOMER_CAPACITY_MARGIN_BRIDGE","symbol":"064760","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"HBM_equipment_score":12,"customer_order_score":11,"capacity_utilization_score":10,"margin_cashflow_score":10,"relative_strength_score":11,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"HBM_equipment_score":15,"customer_order_score":14,"capacity_utilization_score":13,"margin_cashflow_score":13,"relative_strength_score":8,"theme_risk_penalty":9},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["HBM_equipment_score","customer_order_score","capacity_utilization_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C07 row is promoted only because HBM/equipment or process-consumable signal converts into customer order, capacity, utilization and margin bridge; high-MAE/full-window 4B blocks Green.","MFE_90D_pct":41.42,"MAE_90D_pct":-0.94,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_with_drawdown_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L76_C07_036200_20240312_SUBFAB_CHILLER_EQUIPMENT_THEME_NO_DURABLE_ORDER_BRIDGE","trigger_id":"TRG_R2L76_C07_036200_20240312_SUBFAB_CHILLER_EQUIPMENT_THEME_NO_DURABLE_ORDER_BRIDGE","symbol":"036200","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_component_scores_before":{"HBM_equipment_score":10,"customer_order_score":2,"capacity_utilization_score":2,"margin_cashflow_score":0,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"HBM_equipment_score":4,"customer_order_score":0,"capacity_utilization_score":0,"margin_cashflow_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["HBM_equipment_score","customer_order_score","capacity_utilization_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C07 guard demotes HBM/equipment theme rows when repeat order, utilization, margin and cashflow bridge are absent.","MFE_90D_pct":30.82,"MAE_90D_pct":-9.43,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c07_requires_customer_order_capacity_utilization_margin_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"C07 HBM/equipment rows should not promote toward Stage3-Yellow/Green unless HBM/equipment or advanced-process signal converts into customer order, repeat order, capacity pull-through, utilization, margin, operating leverage, or cashflow bridge","039440 and 064760 survive as guarded positives after order/capacity/margin bridge; 036200 is demoted because subfab/chiller equipment MFE lacked durable repeat-order and margin bridge","TRG_R2L76_C07_039440_20240213_HBM_REFLOW_EQUIPMENT_ORDER_MARGIN_BRIDGE|TRG_R2L76_C07_064760_20240321_PROCESS_CONSUMABLE_CUSTOMER_CAPACITY_MARGIN_BRIDGE|TRG_R2L76_C07_036200_20240312_SUBFAB_CHILLER_EQUIPMENT_THEME_NO_DURABLE_ORDER_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c07_equipment_cycle_4b_high_mae_watch_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,1,1,0,"HBM/equipment winners and equipment-theme false starts can peak before order/utilization/margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 039440/064760 guarded positives while preventing 036200 equipment-theme false positive","TRG_R2L76_C07_039440_20240213_HBM_REFLOW_EQUIPMENT_ORDER_MARGIN_BRIDGE|TRG_R2L76_C07_064760_20240321_PROCESS_CONSUMABLE_CUSTOMER_CAPACITY_MARGIN_BRIDGE|TRG_R2L76_C07_036200_20240312_SUBFAB_CHILLER_EQUIPMENT_THEME_NO_DURABLE_ORDER_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"76","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["equipment_theme_without_repeat_order_margin_bridge","HBM_reflow_order_winner_needs_4B_watch","process_consumable_capacity_winner_needs_drawdown_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R2-specific handling

- R2 maps to `L2_AI_SEMICONDUCTOR_ELECTRONICS`.
- This MD uses `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`.
- Validate `round_schedule_status=valid` and `round_sector_consistency=pass` before accepting rows.

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
- price-only/HBM-equipment-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R2 direct L2 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C07 HBM/equipment rows cannot promote without customer order, repeat order, capacity pull-through, utilization recovery, customer qualification, margin conversion, operating leverage, FCF/cash conversion, or earnings revision tied to equipment economics.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R2
completed_loop = 76
next_round = R3
next_loop = 76
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
atlas/symbol_profiles/039/039440.json
atlas/symbol_profiles/064/064760.json
atlas/symbol_profiles/036/036200.json
atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv
atlas/ohlcv_tradable_by_symbol_year/064/064760/2024.csv
atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv
```

This loop continues loop 76 with R2 and adds 3 new independent C07 representative cases, 2 positives, 1 counterexample/watch case, and 1 canonical-archetype residual guard candidate for R2/L2.
