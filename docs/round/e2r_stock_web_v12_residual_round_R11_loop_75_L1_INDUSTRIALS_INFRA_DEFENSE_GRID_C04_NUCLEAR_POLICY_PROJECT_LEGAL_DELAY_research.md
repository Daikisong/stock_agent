# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R11
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R12
computed_next_loop: 75
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: C04_PROJECT_ORDER_REGULATORY_MARGIN_CASHFLOW_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
r11_branch: L1_policy_linked_infra_nuclear_branch
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

R11 allows either `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or a policy/defense-linked `L1_INDUSTRIALS_INFRA_DEFENSE_GRID` branch. The previous R11 loop used C32 governance/control-premium, so this run rotates to the L1 nuclear-policy/project branch. The selected set avoids the top-covered C04 nuclear names and tests a classic fault line: project/order evidence can survive, but nuclear-policy component spikes without order, legal, margin or cashflow bridge should be demoted.

| layer | id | definition |
|---|---|---|
| round | R11 | policy/event or policy-linked infra/defense cross round |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | industrial infra, policy-linked project, nuclear, defense/grid |
| canonical | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | nuclear policy/project, legal/permitting delay, execution bridge |
| fine | C04_PROJECT_ORDER_REGULATORY_MARGIN_CASHFLOW_BRIDGE_GUARD | nuclear signal must become project/order/regulatory/margin/cashflow evidence |
| deep | NUCLEAR_HRSG_POWER_EQUIPMENT_ORDERBOOK_TO_EXECUTION_MARGIN_AND_POLICY_PROJECT_VALUE | nuclear power-equipment positive |
| deep | NUCLEAR_POWER_COMPONENT_POLICY_THEME_WITHOUT_SIGNED_PROJECT_BACKLOG_MARGIN_OR_CASHFLOW_CONVERSION | nuclear component theme false positive |
| deep | NUCLEAR_AIR_COMPRESSOR_POLICY_THEME_WITHOUT_PROJECT_ORDER_MARGIN_OR_CASHFLOW_CONVERSION | nuclear compressor theme false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C04 top-covered symbols are `032820`, `094820`, `105840`, `006910`, `034020`, and `052690`. This run avoids that cluster and also avoids the prior R11/C32 governance-control representatives `036560`, `040300`, and `000990`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C04 | 083650 | new independent | not top-covered C04 symbol; nuclear/power-equipment orderbook and execution-margin bridge |
| C04 | 042370 | new independent | not top-covered C04 symbol; nuclear component policy spike without signed project/margin bridge |
| C04 | 011700 | new independent | not top-covered C04 symbol; nuclear air-compressor policy theme without order/cashflow bridge |

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
083650 has corporate-action candidates ending 2015-05-12, outside the selected 2024 representative window.
042370 has corporate-action candidates ending 2016-09-13, outside the selected 2024 representative window.
011700 has corporate-action candidates ending 2006-05-09, outside the selected 2024 representative window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| nuclear_project_order_success_then_4B_execution_watch | 083650 | 비에이치아이 | Stage2-Actionable | 2024-02-22 | 8560 | nuclear/power-equipment orderbook and execution-margin bridge worked |
| nuclear_component_theme_MFE_then_high_MAE_counterexample | 042370 | 비츠로테크 | Stage2-Actionable | 2024-02-14 | 8250 | nuclear component policy theme lacked signed project/margin bridge |
| nuclear_theme_local_spike_then_high_MAE_counterexample | 011700 | 한신기계 | Stage2-Actionable | 2024-02-22 | 5580 | nuclear policy/component spike lacked order/cashflow bridge |

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
| 083650 | 비에이치아이 | Stage2-Actionable | 2024-02-22 | 8560 | 27.8 | 42.17 | 132.71 | -5.96 | -9.46 | -17.06 | 2024-11-22 | 19920 | -37.25 |
| 042370 | 비츠로테크 | Stage2-Actionable | 2024-02-14 | 8250 | 19.27 | 19.27 | 19.27 | -9.09 | -9.09 | -22.3 | 2024-02-15 | 9840 | -34.86 |
| 011700 | 한신기계 | Stage2-Actionable | 2024-02-22 | 5580 | 6.63 | 6.63 | 6.63 | -15.41 | -23.84 | -45.7 | 2024-02-22 | 5950 | -49.08 |

## 9. Case-by-Case Notes

### 9.1 083650 / 비에이치아이 — nuclear/power-equipment orderbook bridge

The entry row is 2024-02-22 at 8,560. The early path reached 10,940, then 12,170 in the broader 90D area, and later 19,920. This is a valid C04 positive only as guarded Yellow. The key is not nuclear theme heat but project/orderbook visibility, policy-linked plant cycle, and execution-margin bridge. The later crowding and drawdown make 4B watch mandatory.

### 9.2 042370 / 비츠로테크 — nuclear component policy theme without durable source bridge

The entry row is 2024-02-14 at 8,250. It reached 9,840 almost immediately, but the path later fell to 6,410. This is the C04 false-positive shape: nuclear component or policy language can move price, but without signed project, regulatory/legal milestone, backlog-to-revenue, margin and cashflow, MFE is only 4B evidence.

### 9.3 011700 / 한신기계 — nuclear policy spike without order/cashflow bridge

The entry row is 2024-02-22 at 5,580. The local high was 5,950, and the wider low reached 3,030. This row is a cleaner severe high-MAE guard case. Air-compressor or component optionality without order, execution-margin and cashflow bridge should be Watch/4B, not Stage3.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C04 treats nuclear-policy/component theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C04 needs project/order/regulatory/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 042370 and 011700 local event peaks. |
| Full 4B non-price requirement appropriate? | Yes. 083650 has a better bridge; 042370/011700 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
083650:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after project/orderbook/execution-margin bridge
  Stage3-Green = reject unless project timing, legal/permitting and margin durability clear

042370:
  Stage2-Actionable = acceptable only as nuclear component policy watch
  Stage3-Yellow = reject without signed project, backlog, margin and cashflow bridge
  Stage3-Green = reject despite MFE

011700:
  Stage2-Actionable = too generous if based only on nuclear policy/component spike
  Stage3-Yellow = reject without project order, execution margin and cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 083650 | 0.61 | 1.00 | nuclear project/order bridge positive but full-window 4B execution watch |
| 042370 | 1.00 | 1.00 | nuclear component policy theme local 4B watch, not positive stage |
| 011700 | 1.00 | 1.00 | nuclear policy theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c04_requires_project_order_regulatory_margin_cashflow_bridge

rule:
  For C04 nuclear policy/project rows, do not promote nuclear,
  SMR, power equipment, component, compressor, reactor supply-chain, or policy-project
  Stage2 signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  signed project/order, regulatory or legal milestone, EPC/orderbook,
  backlog-to-revenue conversion, execution-margin proof, permitting progress,
  cost-overrun/legal-delay containment, FCF/cash conversion, or earnings revision
  tied to project economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 22.69 | -14.13 | 66.7% | too generous to nuclear-policy/component theme MFE |
| P0b e2r_2_0_baseline_reference | 3 | 22.69 | -14.13 | 33.3% | safer but may miss 083650 |
| P1 sector_specific_candidate_profile | 3 | 22.69 | -14.13 | 66.7% | no broad L1 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 42.17 | -9.46 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 12.95 | -16.46 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 083650 | current_profile_correct_but_no_green | project/order/execution bridge aligned with strong MFE, but 4B execution watch blocks Green |
| 042370 | current_profile_false_positive | nuclear component MFE lacked signed project/margin/cashflow bridge |
| 011700 | current_profile_false_positive | nuclear policy spike produced severe high MAE without order/cashflow bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | C04_PROJECT_ORDER_REGULATORY_MARGIN_CASHFLOW_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R11 allowed L1/C04 non-top-covered nuclear residual reduced |

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
- nuclear policy theme without project/order bridge
- nuclear project/order winner needs 4B watch
- component theme local spike high-MAE
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
- R11 allowed L1 policy-linked infra branch consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact project/order/regulatory milestone announcement URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c04_requires_project_order_regulatory_margin_cashflow_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,"C04 nuclear policy/project rows should not promote toward Stage3-Yellow/Green unless nuclear-policy signal converts into signed project, regulatory/legal milestone, EPC/orderbook, backlog-to-revenue, execution-margin, permitting progress, or cashflow bridge","083650 survives as guarded positive after nuclear/power-equipment project-order bridge; 042370 and 011700 are demoted because nuclear-component/policy themes lacked signed project, margin and cashflow bridge","TRG_R11L75_C04_083650_20240222_NUCLEAR_HRSG_PROJECT_ORDER_MARGIN_BRIDGE|TRG_R11L75_C04_042370_20240214_NUCLEAR_POWER_COMPONENT_THEME_NO_PROJECT_MARGIN_BRIDGE|TRG_R11L75_C04_011700_20240222_NUCLEAR_AIR_COMPRESSOR_THEME_NO_ORDER_CASHFLOW_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R11 allowed L1 policy-linked infra branch"
shadow_weight,c04_nuclear_policy_4b_high_mae_legal_delay_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,1,1,0,"Nuclear project winners and policy-theme false starts can peak before regulatory/legal/project execution durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 083650 guarded positive while preventing 042370/011700 nuclear-policy theme false positives","TRG_R11L75_C04_083650_20240222_NUCLEAR_HRSG_PROJECT_ORDER_MARGIN_BRIDGE|TRG_R11L75_C04_042370_20240214_NUCLEAR_POWER_COMPONENT_THEME_NO_PROJECT_MARGIN_BRIDGE|TRG_R11L75_C04_011700_20240222_NUCLEAR_AIR_COMPRESSOR_THEME_NO_ORDER_CASHFLOW_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R11L75_C04_083650_20240222_NUCLEAR_HRSG_PROJECT_ORDER_MARGIN_BRIDGE","symbol":"083650","company_name":"비에이치아이","round":"R11","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_NUCLEAR_PROJECT_ORDER_EXECUTION_MARGIN_BRIDGE","deep_sub_archetype_id":"NUCLEAR_HRSG_POWER_EQUIPMENT_ORDERBOOK_TO_EXECUTION_MARGIN_AND_POLICY_PROJECT_VALUE","case_type":"nuclear_project_order_success_then_4B_execution_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R11 uses the allowed L1 policy-linked infra branch. C04 nuclear policy/project rows require signed project, regulatory milestone, EPC/orderbook, backlog-to-revenue, execution margin, legal/permitting progress or cashflow bridge; nuclear-policy theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R11L75_C04_042370_20240214_NUCLEAR_POWER_COMPONENT_THEME_NO_PROJECT_MARGIN_BRIDGE","symbol":"042370","company_name":"비츠로테크","round":"R11","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_NUCLEAR_COMPONENT_THEME_WITHOUT_PROJECT_MARGIN_BRIDGE","deep_sub_archetype_id":"NUCLEAR_POWER_COMPONENT_POLICY_THEME_WITHOUT_SIGNED_PROJECT_BACKLOG_MARGIN_OR_CASHFLOW_CONVERSION","case_type":"nuclear_component_theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R11 uses the allowed L1 policy-linked infra branch. C04 nuclear policy/project rows require signed project, regulatory milestone, EPC/orderbook, backlog-to-revenue, execution margin, legal/permitting progress or cashflow bridge; nuclear-policy theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R11L75_C04_011700_20240222_NUCLEAR_AIR_COMPRESSOR_THEME_NO_ORDER_CASHFLOW_BRIDGE","symbol":"011700","company_name":"한신기계","round":"R11","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_NUCLEAR_AIR_COMPRESSOR_THEME_WITHOUT_ORDER_CASHFLOW_BRIDGE","deep_sub_archetype_id":"NUCLEAR_AIR_COMPRESSOR_POLICY_THEME_WITHOUT_PROJECT_ORDER_MARGIN_OR_CASHFLOW_CONVERSION","case_type":"nuclear_theme_local_spike_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R11 uses the allowed L1 policy-linked infra branch. C04 nuclear policy/project rows require signed project, regulatory milestone, EPC/orderbook, backlog-to-revenue, execution margin, legal/permitting progress or cashflow bridge; nuclear-policy theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R11L75_C04_083650_20240222_NUCLEAR_HRSG_PROJECT_ORDER_MARGIN_BRIDGE","case_id":"R11L75_C04_083650_20240222_NUCLEAR_HRSG_PROJECT_ORDER_MARGIN_BRIDGE","symbol":"083650","company_name":"비에이치아이","round":"R11","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_NUCLEAR_PROJECT_ORDER_EXECUTION_MARGIN_BRIDGE","deep_sub_archetype_id":"NUCLEAR_HRSG_POWER_EQUIPMENT_ORDERBOOK_TO_EXECUTION_MARGIN_AND_POLICY_PROJECT_VALUE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":8560,"evidence_available_at_that_date":"source_proxy_nuclear_power_equipment_HRSG_project_orderbook_execution_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_nuclear_power_equipment_HRSG_project_orderbook_execution_margin_bridge; evidence_url_pending","bridge_summary":"nuclear/power-equipment project orderbook and policy-linked plant cycle converted into execution-margin and backlog-to-revenue bridge, but project timing, cost and post-peak crowding require 4B watch","stage2_evidence_fields":["nuclear_power_equipment_order","policy_project_cycle","relative_strength","backlog_visibility_proxy"],"stage3_evidence_fields":["orderbook_to_revenue_visibility","execution_margin_bridge","policy_project_value_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","project_execution_timing_risk","nuclear_policy_crowding"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv","profile_path":"atlas/symbol_profiles/083/083650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.8,"MFE_90D_pct":42.17,"MFE_180D_pct":132.71,"MFE_1Y_pct":132.71,"MFE_2Y_pct":132.71,"MAE_30D_pct":-5.96,"MAE_90D_pct":-9.46,"MAE_180D_pct":-17.06,"MAE_1Y_pct":-17.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-22","peak_price":19920,"drawdown_after_peak_pct":-37.25,"green_lateness_ratio":"0.49","four_b_local_peak_proximity":0.61,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"nuclear_project_order_bridge_positive_but_full_window_4B_execution_watch","four_b_evidence_type":"non_price_nuclear_project_order_margin_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"nuclear_project_order_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L75_C04_083650_20240222_NUCLEAR_HRSG_PROJECT_ORDER_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R11L75_C04_042370_20240214_NUCLEAR_POWER_COMPONENT_THEME_NO_PROJECT_MARGIN_BRIDGE","case_id":"R11L75_C04_042370_20240214_NUCLEAR_POWER_COMPONENT_THEME_NO_PROJECT_MARGIN_BRIDGE","symbol":"042370","company_name":"비츠로테크","round":"R11","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_NUCLEAR_COMPONENT_THEME_WITHOUT_PROJECT_MARGIN_BRIDGE","deep_sub_archetype_id":"NUCLEAR_POWER_COMPONENT_POLICY_THEME_WITHOUT_SIGNED_PROJECT_BACKLOG_MARGIN_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":8250,"evidence_available_at_that_date":"source_proxy_nuclear_power_component_policy_theme_without_signed_project_backlog_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_nuclear_power_component_policy_theme_without_signed_project_backlog_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"nuclear/power-component policy theme produced a local MFE spike, but signed project, backlog-to-revenue, execution-margin and cashflow bridge were absent; later MAE dominated","stage2_evidence_fields":["nuclear_component_theme","policy_project_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_policy_theme_peak","signed_project_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_project_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042370/2024.csv","profile_path":"atlas/symbol_profiles/042/042370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.27,"MFE_90D_pct":19.27,"MFE_180D_pct":19.27,"MFE_1Y_pct":19.27,"MFE_2Y_pct":19.27,"MAE_30D_pct":-9.09,"MAE_90D_pct":-9.09,"MAE_180D_pct":-22.3,"MAE_1Y_pct":-22.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-15","peak_price":9840,"drawdown_after_peak_pct":-34.86,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"nuclear_component_policy_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"nuclear_policy_theme_without_order_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"nuclear_component_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L75_C04_042370_20240214_NUCLEAR_POWER_COMPONENT_THEME_NO_PROJECT_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R11L75_C04_011700_20240222_NUCLEAR_AIR_COMPRESSOR_THEME_NO_ORDER_CASHFLOW_BRIDGE","case_id":"R11L75_C04_011700_20240222_NUCLEAR_AIR_COMPRESSOR_THEME_NO_ORDER_CASHFLOW_BRIDGE","symbol":"011700","company_name":"한신기계","round":"R11","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_NUCLEAR_AIR_COMPRESSOR_THEME_WITHOUT_ORDER_CASHFLOW_BRIDGE","deep_sub_archetype_id":"NUCLEAR_AIR_COMPRESSOR_POLICY_THEME_WITHOUT_PROJECT_ORDER_MARGIN_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":5580,"evidence_available_at_that_date":"source_proxy_nuclear_air_compressor_policy_theme_without_project_order_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_nuclear_air_compressor_policy_theme_without_project_order_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"nuclear air-compressor/policy theme produced an event spike, but project order, backlog-to-revenue, execution-margin and cashflow bridge were not visible; high-MAE path followed","stage2_evidence_fields":["nuclear_policy_theme","air_compressor_component_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["event_local_peak","order_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["severe_high_MAE_without_order_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011700/2024.csv","profile_path":"atlas/symbol_profiles/011/011700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.63,"MFE_90D_pct":6.63,"MFE_180D_pct":6.63,"MFE_1Y_pct":6.63,"MFE_2Y_pct":6.63,"MAE_30D_pct":-15.41,"MAE_90D_pct":-23.84,"MAE_180D_pct":-45.7,"MAE_1Y_pct":-45.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-22","peak_price":5950,"drawdown_after_peak_pct":-49.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"nuclear_policy_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"nuclear_policy_theme_without_order_margin_bridge","four_c_protection_label":"severe_high_MAE_watch","trigger_outcome_label":"nuclear_theme_local_spike_then_severe_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L75_C04_011700_20240222_NUCLEAR_AIR_COMPRESSOR_THEME_NO_ORDER_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L75_C04_083650_20240222_NUCLEAR_HRSG_PROJECT_ORDER_MARGIN_BRIDGE","trigger_id":"TRG_R11L75_C04_083650_20240222_NUCLEAR_HRSG_PROJECT_ORDER_MARGIN_BRIDGE","symbol":"083650","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"policy_project_score":12,"signed_order_score":12,"regulatory_legal_score":8,"execution_margin_score":10,"relative_strength_score":12,"risk_penalty":7},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_project_score":15,"signed_order_score":15,"regulatory_legal_score":9,"execution_margin_score":13,"relative_strength_score":9,"risk_penalty":10},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["policy_project_score","signed_order_score","regulatory_legal_score","execution_margin_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C04 row is promoted only because nuclear policy/project signal converts into orderbook, project value and execution-margin bridge; legal/permitting/project timing and post-peak drawdown block Green.","MFE_90D_pct":42.17,"MAE_90D_pct":-9.46,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L75_C04_042370_20240214_NUCLEAR_POWER_COMPONENT_THEME_NO_PROJECT_MARGIN_BRIDGE","trigger_id":"TRG_R11L75_C04_042370_20240214_NUCLEAR_POWER_COMPONENT_THEME_NO_PROJECT_MARGIN_BRIDGE","symbol":"042370","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"policy_project_score":10,"signed_order_score":1,"regulatory_legal_score":2,"execution_margin_score":0,"relative_strength_score":10,"risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_project_score":4,"signed_order_score":0,"regulatory_legal_score":0,"execution_margin_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["policy_project_score","signed_order_score","regulatory_legal_score","execution_margin_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C04 guard demotes nuclear-policy/component theme rows when signed project, regulatory milestone, orderbook, execution-margin and cashflow bridge are absent.","MFE_90D_pct":19.27,"MAE_90D_pct":-9.09,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L75_C04_011700_20240222_NUCLEAR_AIR_COMPRESSOR_THEME_NO_ORDER_CASHFLOW_BRIDGE","trigger_id":"TRG_R11L75_C04_011700_20240222_NUCLEAR_AIR_COMPRESSOR_THEME_NO_ORDER_CASHFLOW_BRIDGE","symbol":"011700","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"policy_project_score":10,"signed_order_score":1,"regulatory_legal_score":2,"execution_margin_score":0,"relative_strength_score":10,"risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_project_score":4,"signed_order_score":0,"regulatory_legal_score":0,"execution_margin_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["policy_project_score","signed_order_score","regulatory_legal_score","execution_margin_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C04 guard demotes nuclear-policy/component theme rows when signed project, regulatory milestone, orderbook, execution-margin and cashflow bridge are absent.","MFE_90D_pct":6.63,"MAE_90D_pct":-23.84,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c04_requires_project_order_regulatory_margin_cashflow_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,"C04 nuclear policy/project rows should not promote toward Stage3-Yellow/Green unless nuclear-policy signal converts into signed project, regulatory/legal milestone, EPC/orderbook, backlog-to-revenue, execution-margin, permitting progress, or cashflow bridge","083650 survives as guarded positive after nuclear/power-equipment project-order bridge; 042370 and 011700 are demoted because nuclear-component/policy themes lacked signed project, margin and cashflow bridge","TRG_R11L75_C04_083650_20240222_NUCLEAR_HRSG_PROJECT_ORDER_MARGIN_BRIDGE|TRG_R11L75_C04_042370_20240214_NUCLEAR_POWER_COMPONENT_THEME_NO_PROJECT_MARGIN_BRIDGE|TRG_R11L75_C04_011700_20240222_NUCLEAR_AIR_COMPRESSOR_THEME_NO_ORDER_CASHFLOW_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R11 allowed L1 policy-linked infra branch"
shadow_weight,c04_nuclear_policy_4b_high_mae_legal_delay_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,1,1,0,"Nuclear project winners and policy-theme false starts can peak before regulatory/legal/project execution durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 083650 guarded positive while preventing 042370/011700 nuclear-policy theme false positives","TRG_R11L75_C04_083650_20240222_NUCLEAR_HRSG_PROJECT_ORDER_MARGIN_BRIDGE|TRG_R11L75_C04_042370_20240214_NUCLEAR_POWER_COMPONENT_THEME_NO_PROJECT_MARGIN_BRIDGE|TRG_R11L75_C04_011700_20240222_NUCLEAR_AIR_COMPRESSOR_THEME_NO_ORDER_CASHFLOW_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["nuclear_policy_theme_without_project_order_bridge","nuclear_project_order_winner_needs_4B_watch","component_theme_local_spike_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R11-specific handling

- R11 may use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or an L1 policy/defense-linked branch.
- This MD uses the allowed `L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` branch.
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
- price-only/nuclear-policy-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R11 allowed L1 branch.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C04 nuclear-policy/project rows cannot promote without signed project/order, regulatory or legal milestone, EPC/orderbook, backlog-to-revenue conversion, execution-margin proof, permitting progress, cost-overrun/legal-delay containment, FCF/cash conversion, or earnings revision tied to project economics.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R11
completed_loop = 75
next_round = R12
next_loop = 75
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
atlas/symbol_profiles/083/083650.json
atlas/symbol_profiles/042/042370.json
atlas/symbol_profiles/011/011700.json
atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv
atlas/ohlcv_tradable_by_symbol_year/042/042370/2024.csv
atlas/ohlcv_tradable_by_symbol_year/011/011700/2024.csv
```

This loop continues loop 75 with R11 and adds 3 new independent C04 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R11/L1.
