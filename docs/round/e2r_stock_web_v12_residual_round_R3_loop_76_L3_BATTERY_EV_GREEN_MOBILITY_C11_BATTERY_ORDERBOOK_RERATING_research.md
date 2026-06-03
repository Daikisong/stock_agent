# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R3
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R4
computed_next_loop: 76
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: C11_CUSTOMER_ORDER_BACKLOG_MARGIN_CASHFLOW_BRIDGE_GUARD
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

R3 maps directly to `L3_BATTERY_EV_GREEN_MOBILITY`. The previous R3 loop used C12 battery customer-contract/call-off risk, and the recent R9 allowed L3 branch used C29 mobility. This run rotates to C11 battery orderbook rerating and avoids the top-covered battery-cell/material cluster.

| layer | id | definition |
|---|---|---|
| round | R3 | battery / EV / green mobility |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | battery, EV, green mobility, battery equipment and materials |
| canonical | C11_BATTERY_ORDERBOOK_RERATING | battery orderbook, backlog, capacity/order rerating |
| fine | C11_CUSTOMER_ORDER_BACKLOG_MARGIN_CASHFLOW_BRIDGE_GUARD | battery signal must become customer order, backlog, margin and cashflow evidence |
| deep | BATTERY_COATING_AND_ROLL_TO_ROLL_EQUIPMENT_ORDERBOOK_TO_MARGIN_OPERATING_LEVERAGE | battery equipment positive |
| deep | BATTERY_EQUIPMENT_CAPEX_OPTIONALITY_WITHOUT_REPEAT_ORDER_BACKLOG_MARGIN_OR_CASHFLOW_CONVERSION | equipment-order false positive |
| deep | BATTERY_HEAT_TREATMENT_AND_FURNACE_EQUIPMENT_OPTIONALITY_WITHOUT_BACKLOG_MARGIN_CASHFLOW_CONVERSION | furnace equipment false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C11 top-covered symbols are `247540`, `003670`, `393890`, `222080`, `348370`, and `066970`. This run avoids that cluster and also avoids the previous R3/C12 representatives `348370`, `278280`, `093370`, and the recent R9/C29 mobility representatives.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C11 | 137400 | new independent | not top-covered C11 symbol; battery equipment orderbook/margin bridge |
| C11 | 299030 | new independent | not top-covered C11 symbol; battery equipment MFE without durable repeat-order/margin bridge |
| C11 | 382840 | new independent | not top-covered C11 symbol; furnace/heat-treatment equipment low-MFE high-MAE counterexample |

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
137400 has corporate-action candidates ending 2019-05-30, outside the selected 2024 representative window.
299030 has corporate-action candidates ending 2021-04-13, outside the selected 2024 representative window.
382840 has corporate-action candidates ending 2022-07-29, outside the selected 2024 representative window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| battery_equipment_orderbook_success_then_4B_drawdown_watch | 137400 | 피엔티 | Stage2-Actionable | 2024-02-21 | 43500 | roll-to-roll/coating equipment orderbook bridge worked, but 4B drawdown watch required |
| battery_equipment_MFE_then_high_MAE_counterexample | 299030 | 하나기술 | Stage2-Actionable | 2024-02-21 | 62300 | battery equipment CAPEX MFE lacked repeat-order/margin bridge |
| battery_furnace_equipment_low_MFE_high_MAE_counterexample | 382840 | 원준 | Stage2-Actionable | 2024-02-21 | 19110 | furnace/heat-treatment equipment MFE lacked backlog/cashflow bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 137400 | 피엔티 | Stage2-Actionable | 2024-02-21 | 43500 | 10.8 | 105.75 | 105.75 | -10.11 | -10.11 | -10.11 | 2024-06-19 | 89500 | -55.59 |
| 299030 | 하나기술 | Stage2-Actionable | 2024-02-21 | 62300 | 17.34 | 17.34 | 17.34 | -11.56 | -34.03 | -60.91 | 2024-03-08 | 73100 | -66.69 |
| 382840 | 원준 | Stage2-Actionable | 2024-02-21 | 19110 | 8.06 | 8.06 | 8.06 | -16.69 | -27.89 | -55.0 | 2024-03-12 | 20650 | -58.35 |

## 9. Case-by-Case Notes

### 9.1 137400 / 피엔티 — battery equipment orderbook to margin bridge

The entry row is 2024-02-21 at 43,500. The 30D path reached 48,200, and the 90D/180D path reached 89,500. This is a valid C11 positive because the bridge is not just battery equipment theme heat. It requires customer orderbook, roll-to-roll/coating equipment demand, backlog-to-revenue and margin operating leverage. The post-peak low still forces full-window 4B/drawdown watch and blocks Green.

### 9.2 299030 / 하나기술 — equipment order theme without durable bridge

The entry row is 2024-02-21 at 62,300. The stock reached 73,100, but the 180D low fell to 24,350. This is a C11 counterexample: battery equipment CAPEX optionality can create MFE, but without repeat order, backlog-to-revenue, execution margin, working-capital control and cashflow bridge, the row should be Watch/4B/high-MAE rather than Stage3 evidence.

### 9.3 382840 / 원준 — furnace equipment low-MFE high-MAE

The entry row is 2024-02-21 at 19,110. The best forward high was only 20,650, while the 180D low reached 8,600. This is the cleanest false-positive row in the set. Furnace and heat-treatment equipment optionality sounded like orderbook beta, but the path shows that without backlog, utilization, margin and cashflow, it behaves like a local spark, not an orderbook rerating.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C11 treats battery-equipment MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C11 needs customer order/backlog/margin/cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 299030/382840 and post-peak 137400. |
| Full 4B non-price requirement appropriate? | Yes. 137400 has a better non-price bridge; 299030/382840 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
137400:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after customer orderbook / backlog-to-revenue / margin bridge
  Stage3-Green = reject unless post-peak drawdown and customer capex timing risk clear

299030:
  Stage2-Actionable = acceptable only as battery equipment CAPEX watch
  Stage3-Yellow = reject without repeat order, backlog, margin and cashflow bridge
  Stage3-Green = reject despite MFE

382840:
  Stage2-Actionable = too generous if based only on furnace/heat-treatment equipment optionality
  Stage3-Yellow = reject without backlog-to-revenue, utilization, margin and cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 137400 | 0.54 | 1.00 | battery equipment orderbook positive but full-window 4B/drawdown watch |
| 299030 | 1.00 | 1.00 | battery equipment MFE but no durable margin bridge; keep 4B/high-MAE watch |
| 382840 | 1.00 | 1.00 | furnace equipment local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c11_requires_customer_order_backlog_margin_cashflow_bridge

rule:
  For C11 battery orderbook/rerating rows, do not promote battery equipment,
  battery material, CAPEX, roll-to-roll, coating, furnace, heat-treatment, formation,
  or order-cycle Stage2 signals into Stage3-Yellow/Green unless at least one non-price
  bridge is visible:
  customer order, repeat order, backlog-to-revenue conversion, execution-margin proof,
  utilization recovery, working-capital control, FCF/cash conversion, or earnings revision
  tied to battery-order economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 43.72 | -24.01 | 66.7% | too generous to battery-equipment theme MFE |
| P0b e2r_2_0_baseline_reference | 3 | 43.72 | -24.01 | 33.3% | safer but may miss 137400 |
| P1 sector_specific_candidate_profile | 3 | 43.72 | -24.01 | 66.7% | no broad L3 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 105.75 | -10.11 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 12.7 | -30.96 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 137400 | current_profile_correct_but_no_green | orderbook/margin bridge aligned with strong MFE, but post-peak drawdown blocks Green |
| 299030 | current_profile_false_positive_if_green | equipment CAPEX MFE lacked durable repeat-order/margin bridge |
| 382840 | current_profile_false_positive | furnace equipment row produced low MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | C11_CUSTOMER_ORDER_BACKLOG_MARGIN_CASHFLOW_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R3/C11 non-top-covered battery orderbook residual reduced |

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
- battery equipment theme without repeat-order/margin bridge
- battery orderbook winner needs 4B watch
- battery furnace equipment low-MFE high-MAE
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
- R3 direct L3 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact customer-order or backlog announcement URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c11_requires_customer_order_backlog_margin_cashflow_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"C11 battery orderbook rows should not promote toward Stage3-Yellow/Green unless battery-equipment or material signal converts into customer order, repeat order, backlog-to-revenue, execution margin, utilization, working-capital control, or cashflow bridge","137400 survives as guarded positive after battery equipment orderbook/margin bridge; 299030 and 382840 are demoted because battery-equipment MFE lacked durable repeat-order, backlog and margin bridge","TRG_R3L76_C11_137400_20240221_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE|TRG_R3L76_C11_299030_20240221_BATTERY_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE|TRG_R3L76_C11_382840_20240221_BATTERY_FURNACE_EQUIPMENT_NO_BACKLOG_CASHFLOW_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c11_battery_equipment_4b_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,1,1,0,"Battery equipment winners and order-theme false starts can peak before repeat-order and margin durability are confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 137400 guarded positive while preventing 299030/382840 battery-equipment theme false positives","TRG_R3L76_C11_137400_20240221_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE|TRG_R3L76_C11_299030_20240221_BATTERY_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE|TRG_R3L76_C11_382840_20240221_BATTERY_FURNACE_EQUIPMENT_NO_BACKLOG_CASHFLOW_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R3L76_C11_137400_20240221_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE","symbol":"137400","company_name":"피엔티","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE","deep_sub_archetype_id":"BATTERY_COATING_AND_ROLL_TO_ROLL_EQUIPMENT_ORDERBOOK_TO_MARGIN_OPERATING_LEVERAGE","case_type":"battery_equipment_orderbook_success_then_4B_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C11 battery orderbook rerating rows require customer order, repeat order, backlog-to-revenue, execution margin, utilization, working-capital control or cashflow bridge; battery-equipment theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R3L76_C11_299030_20240221_BATTERY_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE","symbol":"299030","company_name":"하나기술","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_ORDER_THEME_WITHOUT_DURABLE_MARGIN_BRIDGE","deep_sub_archetype_id":"BATTERY_EQUIPMENT_CAPEX_OPTIONALITY_WITHOUT_REPEAT_ORDER_BACKLOG_MARGIN_OR_CASHFLOW_CONVERSION","case_type":"battery_equipment_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C11 battery orderbook rerating rows require customer order, repeat order, backlog-to-revenue, execution margin, utilization, working-capital control or cashflow bridge; battery-equipment theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R3L76_C11_382840_20240221_BATTERY_FURNACE_EQUIPMENT_NO_BACKLOG_CASHFLOW_BRIDGE","symbol":"382840","company_name":"원준","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_FURNACE_EQUIPMENT_THEME_WITHOUT_BACKLOG_CASHFLOW_BRIDGE","deep_sub_archetype_id":"BATTERY_HEAT_TREATMENT_AND_FURNACE_EQUIPMENT_OPTIONALITY_WITHOUT_BACKLOG_MARGIN_CASHFLOW_CONVERSION","case_type":"battery_furnace_equipment_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C11 battery orderbook rerating rows require customer order, repeat order, backlog-to-revenue, execution margin, utilization, working-capital control or cashflow bridge; battery-equipment theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R3L76_C11_137400_20240221_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE","case_id":"R3L76_C11_137400_20240221_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE","symbol":"137400","company_name":"피엔티","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE","deep_sub_archetype_id":"BATTERY_COATING_AND_ROLL_TO_ROLL_EQUIPMENT_ORDERBOOK_TO_MARGIN_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":43500,"evidence_available_at_that_date":"source_proxy_battery_coating_roll_to_roll_equipment_orderbook_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_battery_coating_roll_to_roll_equipment_orderbook_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"battery equipment orderbook and roll-to-roll/coating equipment customer demand converted into backlog-to-revenue and margin operating-leverage bridge, but post-peak sector drawdown required 4B watch","stage2_evidence_fields":["battery_equipment_orderbook","roll_to_roll_coating_equipment","relative_strength","customer_order_proxy"],"stage3_evidence_fields":["orderbook_to_revenue_visibility","equipment_margin_bridge","operating_leverage_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","battery_equipment_cycle_crowding","customer_capex_timing_risk"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv","profile_path":"atlas/symbol_profiles/137/137400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.8,"MFE_90D_pct":105.75,"MFE_180D_pct":105.75,"MFE_1Y_pct":105.75,"MFE_2Y_pct":105.75,"MAE_30D_pct":-10.11,"MAE_90D_pct":-10.11,"MAE_180D_pct":-10.11,"MAE_1Y_pct":-10.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":89500,"drawdown_after_peak_pct":-55.59,"green_lateness_ratio":"0.45","four_b_local_peak_proximity":0.54,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"battery_equipment_orderbook_positive_but_full_window_4B_drawdown_watch","four_b_evidence_type":"non_price_battery_orderbook_margin_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"battery_equipment_orderbook_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L76_C11_137400_20240221_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R3L76_C11_299030_20240221_BATTERY_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE","case_id":"R3L76_C11_299030_20240221_BATTERY_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE","symbol":"299030","company_name":"하나기술","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_ORDER_THEME_WITHOUT_DURABLE_MARGIN_BRIDGE","deep_sub_archetype_id":"BATTERY_EQUIPMENT_CAPEX_OPTIONALITY_WITHOUT_REPEAT_ORDER_BACKLOG_MARGIN_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":62300,"evidence_available_at_that_date":"source_proxy_battery_equipment_capex_theme_without_repeat_order_backlog_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_battery_equipment_capex_theme_without_repeat_order_backlog_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"battery equipment CAPEX/order theme produced MFE, but repeat order, backlog-to-revenue, execution margin, working-capital and cashflow bridge did not remain durable; high MAE dominated the forward path","stage2_evidence_fields":["battery_equipment_theme","customer_capex_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_MFE_peak","repeat_order_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["severe_high_MAE_without_order_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/299/299030/2024.csv","profile_path":"atlas/symbol_profiles/299/299030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.34,"MFE_90D_pct":17.34,"MFE_180D_pct":17.34,"MFE_1Y_pct":17.34,"MFE_2Y_pct":17.34,"MAE_30D_pct":-11.56,"MAE_90D_pct":-34.03,"MAE_180D_pct":-60.91,"MAE_1Y_pct":-60.91,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":73100,"drawdown_after_peak_pct":-66.69,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"battery_equipment_theme_MFE_but_no_durable_margin_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"battery_equipment_theme_without_durable_order_margin_bridge","four_c_protection_label":"severe_high_MAE_watch","trigger_outcome_label":"battery_equipment_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L76_C11_299030_20240221_BATTERY_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R3L76_C11_382840_20240221_BATTERY_FURNACE_EQUIPMENT_NO_BACKLOG_CASHFLOW_BRIDGE","case_id":"R3L76_C11_382840_20240221_BATTERY_FURNACE_EQUIPMENT_NO_BACKLOG_CASHFLOW_BRIDGE","symbol":"382840","company_name":"원준","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_FURNACE_EQUIPMENT_THEME_WITHOUT_BACKLOG_CASHFLOW_BRIDGE","deep_sub_archetype_id":"BATTERY_HEAT_TREATMENT_AND_FURNACE_EQUIPMENT_OPTIONALITY_WITHOUT_BACKLOG_MARGIN_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":19110,"evidence_available_at_that_date":"source_proxy_battery_furnace_heat_treatment_equipment_optionality_without_backlog_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_battery_furnace_heat_treatment_equipment_optionality_without_backlog_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"battery furnace/heat-treatment equipment optionality generated only shallow MFE; backlog-to-revenue, margin, utilization and cashflow bridge were too weak, so the path degraded into high MAE","stage2_evidence_fields":["battery_furnace_equipment_theme","equipment_order_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_MFE_peak","backlog_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_backlog_or_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/382/382840/2024.csv","profile_path":"atlas/symbol_profiles/382/382840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.06,"MFE_90D_pct":8.06,"MFE_180D_pct":8.06,"MFE_1Y_pct":8.06,"MFE_2Y_pct":8.06,"MAE_30D_pct":-16.69,"MAE_90D_pct":-27.89,"MAE_180D_pct":-55.0,"MAE_1Y_pct":-55.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-12","peak_price":20650,"drawdown_after_peak_pct":-58.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"battery_furnace_equipment_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"battery_equipment_theme_without_durable_order_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"battery_furnace_equipment_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L76_C11_382840_20240221_BATTERY_FURNACE_EQUIPMENT_NO_BACKLOG_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L76_C11_137400_20240221_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE","trigger_id":"TRG_R3L76_C11_137400_20240221_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE","symbol":"137400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"battery_orderbook_score":12,"customer_order_score":12,"backlog_revenue_score":11,"margin_cashflow_score":10,"relative_strength_score":11,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"battery_orderbook_score":15,"customer_order_score":15,"backlog_revenue_score":14,"margin_cashflow_score":12,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["battery_orderbook_score","customer_order_score","backlog_revenue_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C11 row is promoted only because battery-equipment signal converts into customer order, backlog-to-revenue and margin bridge; 4B drawdown/capex timing watch blocks Green.","MFE_90D_pct":105.75,"MAE_90D_pct":-10.11,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L76_C11_299030_20240221_BATTERY_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE","trigger_id":"TRG_R3L76_C11_299030_20240221_BATTERY_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE","symbol":"299030","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"battery_orderbook_score":6,"customer_order_score":2,"backlog_revenue_score":1,"margin_cashflow_score":0,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"battery_orderbook_score":2,"customer_order_score":0,"backlog_revenue_score":0,"margin_cashflow_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["battery_orderbook_score","customer_order_score","backlog_revenue_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C11 guard demotes battery-equipment order-theme rows when repeat order, backlog-to-revenue, margin and cashflow bridge are absent.","MFE_90D_pct":17.34,"MAE_90D_pct":-34.03,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L76_C11_382840_20240221_BATTERY_FURNACE_EQUIPMENT_NO_BACKLOG_CASHFLOW_BRIDGE","trigger_id":"TRG_R3L76_C11_382840_20240221_BATTERY_FURNACE_EQUIPMENT_NO_BACKLOG_CASHFLOW_BRIDGE","symbol":"382840","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"battery_orderbook_score":6,"customer_order_score":2,"backlog_revenue_score":1,"margin_cashflow_score":0,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"battery_orderbook_score":2,"customer_order_score":0,"backlog_revenue_score":0,"margin_cashflow_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["battery_orderbook_score","customer_order_score","backlog_revenue_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C11 guard demotes battery-equipment order-theme rows when repeat order, backlog-to-revenue, margin and cashflow bridge are absent.","MFE_90D_pct":8.06,"MAE_90D_pct":-27.89,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c11_requires_customer_order_backlog_margin_cashflow_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"C11 battery orderbook rows should not promote toward Stage3-Yellow/Green unless battery-equipment or material signal converts into customer order, repeat order, backlog-to-revenue, execution margin, utilization, working-capital control, or cashflow bridge","137400 survives as guarded positive after battery equipment orderbook/margin bridge; 299030 and 382840 are demoted because battery-equipment MFE lacked durable repeat-order, backlog and margin bridge","TRG_R3L76_C11_137400_20240221_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE|TRG_R3L76_C11_299030_20240221_BATTERY_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE|TRG_R3L76_C11_382840_20240221_BATTERY_FURNACE_EQUIPMENT_NO_BACKLOG_CASHFLOW_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c11_battery_equipment_4b_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,1,1,0,"Battery equipment winners and order-theme false starts can peak before repeat-order and margin durability are confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 137400 guarded positive while preventing 299030/382840 battery-equipment theme false positives","TRG_R3L76_C11_137400_20240221_BATTERY_EQUIPMENT_ORDERBOOK_MARGIN_BRIDGE|TRG_R3L76_C11_299030_20240221_BATTERY_EQUIPMENT_ORDER_THEME_NO_DURABLE_MARGIN_BRIDGE|TRG_R3L76_C11_382840_20240221_BATTERY_FURNACE_EQUIPMENT_NO_BACKLOG_CASHFLOW_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"76","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["battery_equipment_theme_without_repeat_order_margin_bridge","battery_orderbook_winner_needs_4B_watch","battery_furnace_equipment_low_MFE_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R3-specific handling

- R3 maps to `L3_BATTERY_EV_GREEN_MOBILITY`.
- This MD uses `C11_BATTERY_ORDERBOOK_RERATING`.
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
- price-only/battery-equipment-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R3 direct L3 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C11 battery-orderbook rows cannot promote without customer order, repeat order, backlog-to-revenue conversion, execution-margin proof, utilization recovery, working-capital control, FCF/cash conversion, or earnings revision tied to battery-order economics.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R3
completed_loop = 76
next_round = R4
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
atlas/symbol_profiles/137/137400.json
atlas/symbol_profiles/299/299030.json
atlas/symbol_profiles/382/382840.json
atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv
atlas/ohlcv_tradable_by_symbol_year/299/299030/2024.csv
atlas/ohlcv_tradable_by_symbol_year/382/382840/2024.csv
```

This loop continues loop 76 with R3 and adds 3 new independent C11 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R3/L3.
