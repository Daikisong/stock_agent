# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R1
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R2
computed_next_loop: 75
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: C05_CONTRACT_EXECUTION_MARGIN_CASHFLOW_BRIDGE_GUARD
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

R13 / loop 74 has closed, so the scheduler rolls to `R1 / loop 75`. R1 maps to `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`. The previous R1 loop used C02 grid/datacenter CAPEX, and recent R11 used C03 defense. This run therefore uses the under-covered C05 EPC/mega-contract margin-gap branch.

| layer | id | definition |
|---|---|---|
| round | R1 | industrials / infrastructure / defense / grid |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | infrastructure, industrial EPC, order backlog, grid, defense |
| canonical | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | EPC / mega contract / execution margin gap |
| fine | C05_CONTRACT_EXECUTION_MARGIN_CASHFLOW_BRIDGE_GUARD | EPC signal must become contract, margin and cashflow evidence |
| deep | MECHANICAL_ELECTRICAL_PLUMBING_EPC_ORDER_TO_MARGIN_AND_CASHFLOW_BRIDGE | MEP/EPC positive |
| deep | PROJECT_MANAGEMENT_NEOM_OR_OVERSEAS_MEGA_PROJECT_THEME_WITHOUT_CONTRACT_MARGIN_CONVERSION | PM mega-project false positive |
| deep | SHIPYARD_AND_CONSTRUCTION_ORDER_OPTIONALITY_WITHOUT_EXECUTION_MARGIN_BALANCE_CASHFLOW_REPAIR | turnaround false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C05 top-covered symbols are `006360`, `047040`, `000720`, `028050`, `375500`, and `034300`. This run avoids that cluster and also avoids the recent R1/C02 and R11/C03 symbols.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C05 | 011560 | new independent | not top-covered C05 symbol; MEP/EPC order-margin bridge |
| C05 | 053690 | new independent | not top-covered C05 symbol; global PM/mega-project MFE without contract-margin durability |
| C05 | 097230 | new independent | not top-covered C05 symbol; shipyard/construction turnaround low-MFE high-MAE counterexample |
| excluded | 016250 | reviewed | 2025-06-25 corporate-action candidate complicates longer forward windows; also weaker residual value than selected rows |

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
011560 has corporate-action candidates ending 2006, outside the selected 2024 representative window.
053690 has no corporate-action candidate dates.
097230 has corporate-action candidates ending 2019, outside the selected 2024 representative window.
016250/SGC E&C was inspected but excluded because 2025-06-25 corporate-action candidate complicates longer windows and the selected set already has clearer C05 residual coverage.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 011560 | 세보엠이씨 | Stage2-Actionable | 2024-02-21 | 8560 | MEP/EPC order-margin bridge worked |
| theme_MFE_then_high_MAE_counterexample | 053690 | 한미글로벌 | Stage2-Actionable | 2024-07-10 | 16700 | PM/mega-project theme had MFE but lacked margin/cashflow durability |
| failed_turnaround_low_MFE_high_MAE_counterexample | 097230 | HJ중공업 | Stage2-Actionable | 2024-01-29 | 3540 | shipyard/construction turnaround theme lacked execution margin and balance/cashflow bridge |

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
| 011560 | 세보엠이씨 | Stage2-Actionable | 2024-02-21 | 8560 | 14.25 | 74.53 | 74.53 | -0.35 | -0.35 | -0.35 | 2024-05-29 | 14940 | -37.75 |
| 053690 | 한미글로벌 | Stage2-Actionable | 2024-07-10 | 16700 | 15.45 | 15.45 | 15.45 | -17.66 | -17.66 | -17.66 | 2024-07-15 | 19280 | -28.68 |
| 097230 | HJ중공업 | Stage2-Actionable | 2024-01-29 | 3540 | 5.51 | 5.51 | 6.64 | -2.82 | -14.55 | -26.98 | 2024-07-23 | 3775 | -31.52 |

## 9. Case-by-Case Notes

### 9.1 011560 / 세보엠이씨 — MEP/EPC order-margin bridge

The entry row is 2024-02-21 at 8,560. The forward path reached 9,780 in the 30D window and 14,940 in the wider window. This is a valid C05 positive because the signal is not just infrastructure or EPC theme language. It needs order-to-revenue visibility, execution-margin proof and cashflow/working-capital discipline. After the peak, the row still needs 4B watch.

### 9.2 053690 / 한미글로벌 — PM mega-project theme without durable contract-margin bridge

The entry row is 2024-07-10 at 16,700. It reached 19,280 quickly, but then fell to 13,750. The MFE is real, but the residual lesson is that global PM / overseas mega-project optionality should not be promoted unless contract conversion, margin durability and cashflow visibility are present.

### 9.3 097230 / HJ중공업 — shipyard/construction turnaround false start

The entry row is 2024-01-29 at 3,540. The forward high reached only 3,775, while the 180D low fell to 2,585. This is a clean C05 false-positive shape: order or turnaround language without execution-margin repair, balance repair and cashflow bridge is not Stage3 evidence.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C05 treats EPC/mega-project/turnaround theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C05 needs contract conversion, execution margin and cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 053690. |
| Full 4B non-price requirement appropriate? | Yes. 011560 has a bridge; 053690/097230 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
011560:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after order-to-revenue / execution-margin / cashflow bridge
  Stage3-Green = wait for post-MFE 4B review and margin durability

053690:
  Stage2-Actionable = acceptable only as mega-project watch
  Stage3-Yellow = reject without contract conversion, execution margin and cashflow bridge
  Stage3-Green = reject despite MFE

097230:
  Stage2-Actionable = too generous if based only on shipyard/construction turnaround theme
  Stage3-Yellow = reject without execution-margin, balance repair or cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 011560 | 0.91 | 1.00 | good full-window 4B watch after MEP/EPC order-margin bridge |
| 053690 | 1.00 | 1.00 | mega-project theme MFE but no contract-margin bridge; keep 4B/high-MAE watch |
| 097230 | 0.99 | 1.00 | turnaround theme weak MFE; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c05_requires_contract_execution_margin_cashflow_bridge

rule:
  For C05 EPC/mega-contract rows, do not promote EPC, plant,
  infrastructure, shipyard-construction, project management, overseas mega-project,
  or turnaround Stage2 signals into Stage3-Yellow/Green unless at least one
  non-price bridge is visible:
  signed contract conversion, backlog-to-revenue conversion, execution-margin proof,
  claim/cost-overrun containment, working-capital control, balance repair,
  FCF/cash conversion, or earnings revision tied to contract economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 31.83 | -10.85 | 66.7% | too generous to EPC/mega-project theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 31.83 | -10.85 | 33.3% | safer but may miss 011560 |
| P1 sector_specific_candidate_profile | 3 | 31.83 | -10.85 | 66.7% | no broad L1 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 74.53 | -0.35 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 10.48 | -16.11 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 011560 | current_profile_correct | MEP/EPC order-margin bridge aligned with strong MFE |
| 053690 | current_profile_false_positive_if_green | mega-project MFE lacked durable margin/cashflow bridge |
| 097230 | current_profile_false_positive | turnaround theme produced low MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | C05_CONTRACT_EXECUTION_MARGIN_CASHFLOW_BRIDGE_GUARD | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 2 | false | true | R1/C05 non-top-covered EPC/mega-contract residual reduced |

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
- mega-project theme without contract-margin bridge
- EPC order-margin winner needs 4B watch
- turnaround theme low-MFE high-MAE
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
- R1 direct L1 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact contract announcement URLs
- production scoring behavior
- live candidate status
- 016250/SGC E&C as representative row because cleaner C05 residual alternatives were selected
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c05_requires_contract_execution_margin_cashflow_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"C05 EPC/mega-contract rows should not promote toward Stage3-Yellow/Green unless EPC or mega-project signal converts into contract conversion, backlog-to-revenue, execution-margin, claim/working-capital control, balance repair, or cashflow bridge","011560 survives after MEP/EPC order-margin bridge; 053690 and 097230 are demoted because mega-project/turnaround theme lacked durable contract-margin and cashflow bridge","TRG_R1L75_C05_011560_20240221_MEP_EPC_ORDER_MARGIN_BRIDGE|TRG_R1L75_C05_053690_20240710_GLOBAL_PM_NEOM_THEME_WITHOUT_MARGIN_DURABILITY|TRG_R1L75_C05_097230_20240129_SHIPYARD_CONSTRUCTION_TURNAROUND_MARGIN_GAP_FALSE_START",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c05_epc_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,1,1,0,"EPC/order winners and mega-project theme false starts can peak before execution-margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 011560 positive while preventing 053690/097230 EPC-theme false positives","TRG_R1L75_C05_011560_20240221_MEP_EPC_ORDER_MARGIN_BRIDGE|TRG_R1L75_C05_053690_20240710_GLOBAL_PM_NEOM_THEME_WITHOUT_MARGIN_DURABILITY|TRG_R1L75_C05_097230_20240129_SHIPYARD_CONSTRUCTION_TURNAROUND_MARGIN_GAP_FALSE_START",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R1L75_C05_011560_20240221_MEP_EPC_ORDER_MARGIN_BRIDGE","symbol":"011560","company_name":"세보엠이씨","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_MEP_EPC_ORDER_MARGIN_OPERATING_LEVERAGE_BRIDGE","deep_sub_archetype_id":"MECHANICAL_ELECTRICAL_PLUMBING_EPC_ORDER_TO_MARGIN_AND_CASHFLOW_BRIDGE","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C05 EPC/mega-contract rows require contract conversion, backlog-to-revenue, execution-margin, claim/working-capital control, balance repair, or cashflow bridge; EPC/mega-project theme alone is insufficient."}
{"row_type":"case","case_id":"R1L75_C05_053690_20240710_GLOBAL_PM_NEOM_THEME_WITHOUT_MARGIN_DURABILITY","symbol":"053690","company_name":"한미글로벌","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_GLOBAL_PM_MEGA_PROJECT_THEME_WITHOUT_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"PROJECT_MANAGEMENT_NEOM_OR_OVERSEAS_MEGA_PROJECT_THEME_WITHOUT_CONTRACT_MARGIN_CONVERSION","case_type":"theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C05 EPC/mega-contract rows require contract conversion, backlog-to-revenue, execution-margin, claim/working-capital control, balance repair, or cashflow bridge; EPC/mega-project theme alone is insufficient."}
{"row_type":"case","case_id":"R1L75_C05_097230_20240129_SHIPYARD_CONSTRUCTION_TURNAROUND_MARGIN_GAP_FALSE_START","symbol":"097230","company_name":"HJ중공업","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPYARD_CONSTRUCTION_TURNAROUND_WITHOUT_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"SHIPYARD_AND_CONSTRUCTION_ORDER_OPTIONALITY_WITHOUT_EXECUTION_MARGIN_BALANCE_CASHFLOW_REPAIR","case_type":"failed_turnaround_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C05 EPC/mega-contract rows require contract conversion, backlog-to-revenue, execution-margin, claim/working-capital control, balance repair, or cashflow bridge; EPC/mega-project theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R1L75_C05_011560_20240221_MEP_EPC_ORDER_MARGIN_BRIDGE","case_id":"R1L75_C05_011560_20240221_MEP_EPC_ORDER_MARGIN_BRIDGE","symbol":"011560","company_name":"세보엠이씨","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_MEP_EPC_ORDER_MARGIN_OPERATING_LEVERAGE_BRIDGE","deep_sub_archetype_id":"MECHANICAL_ELECTRICAL_PLUMBING_EPC_ORDER_TO_MARGIN_AND_CASHFLOW_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":8560,"evidence_available_at_that_date":"source_proxy_MEP_EPC_cleanroom_or_infra_order_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_MEP_EPC_cleanroom_or_infra_order_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"MEP/EPC order visibility converted into margin, execution, and cashflow bridge rather than construction/EPC theme heat","stage2_evidence_fields":["MEP_EPC_order_visibility","infra_or_cleanroom_execution_proxy","relative_strength","margin_bridge_proxy"],"stage3_evidence_fields":["order_to_revenue_visibility","execution_margin_bridge","cashflow_or_working_capital_watch"],"stage4b_evidence_fields":["post_MFE_peak_watch","EPC_margin_cycle_crowding"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011560/2024.csv","profile_path":"atlas/symbol_profiles/011/011560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.25,"MFE_90D_pct":74.53,"MFE_180D_pct":74.53,"MFE_1Y_pct":74.53,"MFE_2Y_pct":74.53,"MAE_30D_pct":-0.35,"MAE_90D_pct":-0.35,"MAE_180D_pct":-0.35,"MAE_1Y_pct":-0.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-29","peak_price":14940,"drawdown_after_peak_pct":-37.75,"green_lateness_ratio":"0.37","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_MEP_EPC_order_margin_bridge","four_b_evidence_type":"non_price_EPC_order_margin_cashflow_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L75_C05_011560_20240221_MEP_EPC_ORDER_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L75_C05_053690_20240710_GLOBAL_PM_NEOM_THEME_WITHOUT_MARGIN_DURABILITY","case_id":"R1L75_C05_053690_20240710_GLOBAL_PM_NEOM_THEME_WITHOUT_MARGIN_DURABILITY","symbol":"053690","company_name":"한미글로벌","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_GLOBAL_PM_MEGA_PROJECT_THEME_WITHOUT_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"PROJECT_MANAGEMENT_NEOM_OR_OVERSEAS_MEGA_PROJECT_THEME_WITHOUT_CONTRACT_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-10","entry_date":"2024-07-10","entry_price":16700,"evidence_available_at_that_date":"source_proxy_global_PM_mega_project_theme_without_contract_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_global_PM_mega_project_theme_without_contract_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"global PM / mega-project theme produced MFE, but contract conversion, margin durability, backlog-to-revenue, and cashflow bridge were weak","stage2_evidence_fields":["global_PM_mega_project_theme","overseas_project_optionality","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_local_peak","contract_margin_bridge_absent","cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_contract_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053690/2024.csv","profile_path":"atlas/symbol_profiles/053/053690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.45,"MFE_90D_pct":15.45,"MFE_180D_pct":15.45,"MFE_1Y_pct":15.45,"MFE_2Y_pct":15.45,"MAE_30D_pct":-17.66,"MAE_90D_pct":-17.66,"MAE_180D_pct":-17.66,"MAE_1Y_pct":-17.66,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-15","peak_price":19280,"drawdown_after_peak_pct":-28.68,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"mega_project_theme_MFE_but_no_contract_margin_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"EPC_or_mega_project_theme_without_margin_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L75_C05_053690_20240710_GLOBAL_PM_NEOM_THEME_WITHOUT_MARGIN_DURABILITY_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L75_C05_097230_20240129_SHIPYARD_CONSTRUCTION_TURNAROUND_MARGIN_GAP_FALSE_START","case_id":"R1L75_C05_097230_20240129_SHIPYARD_CONSTRUCTION_TURNAROUND_MARGIN_GAP_FALSE_START","symbol":"097230","company_name":"HJ중공업","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_SHIPYARD_CONSTRUCTION_TURNAROUND_WITHOUT_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"SHIPYARD_AND_CONSTRUCTION_ORDER_OPTIONALITY_WITHOUT_EXECUTION_MARGIN_BALANCE_CASHFLOW_REPAIR","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":3540,"evidence_available_at_that_date":"source_proxy_shipyard_construction_turnaround_without_execution_margin_balance_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_shipyard_construction_turnaround_without_execution_margin_balance_cashflow_bridge; evidence_url_pending","bridge_summary":"shipyard/construction turnaround and order optionality lacked execution-margin, balance repair, and cashflow bridge; upside stayed shallow while MAE expanded","stage2_evidence_fields":["shipyard_construction_turnaround_theme","order_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","execution_margin_gap","balance_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_margin_or_cashflow_repair"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv","profile_path":"atlas/symbol_profiles/097/097230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.51,"MFE_90D_pct":5.51,"MFE_180D_pct":6.64,"MFE_1Y_pct":6.64,"MFE_2Y_pct":6.64,"MAE_30D_pct":-2.82,"MAE_90D_pct":-14.55,"MAE_180D_pct":-26.98,"MAE_1Y_pct":-26.98,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-23","peak_price":3775,"drawdown_after_peak_pct":-31.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"turnaround_theme_weak_MFE_keep_4B_high_MAE_watch","four_b_evidence_type":"EPC_or_mega_project_theme_without_margin_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_turnaround_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L75_C05_097230_20240129_SHIPYARD_CONSTRUCTION_TURNAROUND_MARGIN_GAP_FALSE_START_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L75_C05_011560_20240221_MEP_EPC_ORDER_MARGIN_BRIDGE","trigger_id":"TRG_R1L75_C05_011560_20240221_MEP_EPC_ORDER_MARGIN_BRIDGE","symbol":"011560","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_conversion_score":11,"backlog_revenue_score":12,"execution_margin_score":11,"working_capital_cashflow_score":10,"relative_strength_score":10,"risk_penalty":6},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_conversion_score":14,"backlog_revenue_score":15,"execution_margin_score":14,"working_capital_cashflow_score":13,"relative_strength_score":8,"risk_penalty":7},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["contract_conversion_score","backlog_revenue_score","execution_margin_score","working_capital_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C05 row is promoted only because EPC order visibility converts into execution-margin, backlog-to-revenue, and cashflow bridge; post-MFE 4B watch remains.","MFE_90D_pct":74.53,"MAE_90D_pct":-0.35,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L75_C05_053690_20240710_GLOBAL_PM_NEOM_THEME_WITHOUT_MARGIN_DURABILITY","trigger_id":"TRG_R1L75_C05_053690_20240710_GLOBAL_PM_NEOM_THEME_WITHOUT_MARGIN_DURABILITY","symbol":"053690","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_conversion_score":5,"backlog_revenue_score":3,"execution_margin_score":1,"working_capital_cashflow_score":0,"relative_strength_score":10,"risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_conversion_score":2,"backlog_revenue_score":1,"execution_margin_score":0,"working_capital_cashflow_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["contract_conversion_score","backlog_revenue_score","execution_margin_score","working_capital_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C05 guard demotes EPC/mega-project/turnaround theme rows when contract conversion, execution margin, working-capital and cashflow bridge are absent.","MFE_90D_pct":15.45,"MAE_90D_pct":-17.66,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L75_C05_097230_20240129_SHIPYARD_CONSTRUCTION_TURNAROUND_MARGIN_GAP_FALSE_START","trigger_id":"TRG_R1L75_C05_097230_20240129_SHIPYARD_CONSTRUCTION_TURNAROUND_MARGIN_GAP_FALSE_START","symbol":"097230","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_conversion_score":5,"backlog_revenue_score":3,"execution_margin_score":1,"working_capital_cashflow_score":0,"relative_strength_score":10,"risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_conversion_score":2,"backlog_revenue_score":1,"execution_margin_score":0,"working_capital_cashflow_score":0,"relative_strength_score":4,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["contract_conversion_score","backlog_revenue_score","execution_margin_score","working_capital_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C05 guard demotes EPC/mega-project/turnaround theme rows when contract conversion, execution margin, working-capital and cashflow bridge are absent.","MFE_90D_pct":5.51,"MAE_90D_pct":-14.55,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c05_requires_contract_execution_margin_cashflow_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"C05 EPC/mega-contract rows should not promote toward Stage3-Yellow/Green unless EPC or mega-project signal converts into contract conversion, backlog-to-revenue, execution-margin, claim/working-capital control, balance repair, or cashflow bridge","011560 survives after MEP/EPC order-margin bridge; 053690 and 097230 are demoted because mega-project/turnaround theme lacked durable contract-margin and cashflow bridge","TRG_R1L75_C05_011560_20240221_MEP_EPC_ORDER_MARGIN_BRIDGE|TRG_R1L75_C05_053690_20240710_GLOBAL_PM_NEOM_THEME_WITHOUT_MARGIN_DURABILITY|TRG_R1L75_C05_097230_20240129_SHIPYARD_CONSTRUCTION_TURNAROUND_MARGIN_GAP_FALSE_START",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c05_epc_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,1,1,0,"EPC/order winners and mega-project theme false starts can peak before execution-margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 011560 positive while preventing 053690/097230 EPC-theme false positives","TRG_R1L75_C05_011560_20240221_MEP_EPC_ORDER_MARGIN_BRIDGE|TRG_R1L75_C05_053690_20240710_GLOBAL_PM_NEOM_THEME_WITHOUT_MARGIN_DURABILITY|TRG_R1L75_C05_097230_20240129_SHIPYARD_CONSTRUCTION_TURNAROUND_MARGIN_GAP_FALSE_START",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"75","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["mega_project_theme_without_contract_margin_bridge","EPC_order_margin_winner_needs_4B_watch","turnaround_theme_low_MFE_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R1-specific handling

- R1 maps to `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`.
- This MD uses `C05_EPC_MEGA_CONTRACT_MARGIN_GAP`.
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
- price-only/EPC-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R1 direct L1 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C05 EPC/mega-contract rows cannot promote without signed contract conversion, backlog-to-revenue conversion, execution-margin proof, claim/cost-overrun containment, working-capital control, balance repair, FCF/cash conversion, or earnings revision tied to contract economics.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R1
completed_loop = 75
next_round = R2
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
atlas/symbol_profiles/011/011560.json
atlas/symbol_profiles/053/053690.json
atlas/symbol_profiles/097/097230.json
atlas/symbol_profiles/016/016250.json
atlas/ohlcv_tradable_by_symbol_year/011/011560/2024.csv
atlas/ohlcv_tradable_by_symbol_year/053/053690/2024.csv
atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv
atlas/ohlcv_tradable_by_symbol_year/016/016250/2024.csv
```

This loop starts loop 75 with R1 and adds 3 new independent C05 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R1/L1.
