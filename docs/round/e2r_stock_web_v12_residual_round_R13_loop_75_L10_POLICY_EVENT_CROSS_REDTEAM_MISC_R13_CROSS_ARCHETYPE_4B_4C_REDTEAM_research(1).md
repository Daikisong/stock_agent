# E2R Stock-Web Historical Calibration / R13 Cross-Archetype 4B/4C Redteam

## 0. Research Metadata

```text
scheduled_round: R13
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R1
computed_next_loop: 76
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: R13_DELAYED_MFE_SOURCE_BRIDGE_VS_LOCAL_SPIKE_NO_BRIDGE_GUARD
loop_objective: cross_archetype_redteam | 4B_local_vs_full_window_split | delayed_MFE_bridge_survival | local_spike_no_bridge_demotion | 4C_high_MAE_guardrail
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
r13_cross_case_mode: true
new_independent_case_count: 0
do_not_count_as_new_case: true
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

## 2. R13 Scope

R13 is not a normal sector expansion round. It is a cross-archetype checkpoint. This file therefore uses:

```text
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

Every representative row is marked:

```text
r13_cross_case = true
do_not_count_as_new_case = true
independent_evidence_weight = 0.0
aggregate_group_role = r13_cross_check
```

This run tests a different R13 axis from the previous high-MAE guardrail:

```text
Can the system distinguish delayed MFE backed by a real source bridge from a local spike or shallow MFE without source bridge?
```

The answer from this set is yes.

```text
- If source bridge exists: Stage2/Yellow may survive, but Green remains blocked by full-window 4B and drawdown.
- If source bridge is absent: local spike or theme MFE is demoted to Watch/4B/high-MAE guard.
```

## 3. Cross-Archetype Source Map

| source large sector | source canonical | symbol | company | R13 outcome | local 4B proximity | full-window 4B proximity | 4C/watch label |
|---|---|---:|---|---|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 083650 | 비에이치아이 | r13_positive_control_delayed_MFE_bridge_survives_with_4B_watch | 0.61 | 1.0 | post_peak_drawdown_watch |
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 035890 | 서희건설 | r13_positive_control_delayed_MFE_bridge_survives_with_4B_watch | 0.83 | 1.0 | drawdown_watch_after_peak |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 186230 | 그린플러스 | r13_positive_control_delayed_MFE_bridge_survives_with_4B_watch | 0.75 | 1.0 | drawdown_watch_after_peak |
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 011700 | 한신기계 | r13_local_spike_no_source_bridge_demoted_to_4B_high_MAE_watch | 1.0 | 1.0 | severe_high_MAE_watch |
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 007210 | 벽산 | r13_local_spike_no_source_bridge_demoted_to_4B_high_MAE_watch | 1.0 | 1.0 | high_MAE_watch |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 097870 | 효성오앤비 | r13_local_spike_no_source_bridge_demoted_to_4B_high_MAE_watch | 1.0 | 1.0 | high_MAE_watch |

## 4. No-Repeat / Duplicate Handling

No-Repeat hard duplicate key remains:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

For R13, these rows are cross-check rows, not new source-archetype rows.

```text
r13_cross_case_count = 6
positive_control_count = 3
counterexample_count = 3
new_independent_case_count = 0
reused_case_count = 6
source_archetype_coverage_increment = 0
independent_evidence_weight = 0.0
do_not_count_as_new_case = true
```

## 5. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_R13_cross_archetype_4B_4C_diagnostics"}
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

## 6. Historical Eligibility Gate

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
035890 has corporate-action candidates ending 2012-07-12, outside the selected 2024 representative window.
186230 has corporate-action candidates ending 2020-11-13, outside the selected 2024 representative window.
011700 has corporate-action candidates ending 2006-05-09, outside the selected 2024 representative window.
007210 has corporate-action candidates ending 2012-05-10, outside the selected 2024 representative window.
097870 has a 2018-05-18 corporate-action candidate, outside the selected 2024 representative window.
All six representative windows are treated as clean for R13 guardrail diagnostics.
```

## 7. Trigger-Level OHLC Backtest Table

| symbol | company | source canonical | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 083650 | 비에이치아이 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | Stage2-Actionable | 2024-02-22 | 8560 | 27.8 | 42.17 | 132.71 | -5.96 | -9.46 | -17.06 | 2024-11-22 | 19920 | -37.25 |
| 035890 | 서희건설 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage2-Actionable | 2024-01-29 | 1259 | 7.15 | 9.77 | 28.75 | -2.3 | -2.3 | -5.48 | 2024-10-10 | 1621 | -14.19 |
| 186230 | 그린플러스 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2024-02-21 | 9200 | 24.89 | 24.89 | 32.61 | -12.83 | -22.07 | -22.07 | 2024-08-20 | 12200 | -31.48 |
| 011700 | 한신기계 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | Stage2-Actionable | 2024-02-22 | 5580 | 6.63 | 6.63 | 6.63 | -15.41 | -23.84 | -45.7 | 2024-02-22 | 5950 | -49.08 |
| 007210 | 벽산 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage2-Actionable | 2024-01-10 | 2770 | 5.05 | 5.05 | 5.05 | -13.18 | -24.91 | -32.85 | 2024-01-11 | 2910 | -36.08 |
| 097870 | 효성오앤비 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2024-06-26 | 7390 | 16.91 | 16.91 | 16.91 | -8.93 | -24.22 | -24.22 | 2024-06-27 | 8640 | -35.19 |

## 8. Cross-Case Diagnosis

### 8.1 Bridge-backed delayed MFE rows

`083650`, `035890`, and `186230` are not Green cases. They all need 4B watch. However, they should not be deleted simply because local timing is imperfect or drawdown appears later. Each has a source-archetype bridge:

```text
083650: nuclear project/orderbook/execution-margin bridge
035890: regional housing orderbook/PF-risk/cashflow bridge
186230: smart-farm policy-to-order/revenue/margin bridge
```

These cases are the positive-control side of this R13 run. The bridge is the keel; the price wave can arrive late, but the boat still has a hull.

### 8.2 Local spike / no-bridge rows

`011700`, `007210`, and `097870` show the opposite. They all produced local MFE or event heat, but no durable source bridge:

```text
011700: nuclear policy/component spike without order/cashflow bridge
007210: building-materials theme without housing order/margin bridge
097870: organic fertilizer policy theme without volume/margin bridge
```

These rows should be demoted to Watch/4B/high-MAE guard. A spark is not a furnace; without fuel from orders, volume, margin or cashflow, the move burns out.

## 9. Stage2 / Yellow / Green / 4B Comparison

```text
Common R13 rule:
  Stage2-Actionable survives only when a source-archetype bridge exists.
  Stage3-Yellow may survive only as guarded Yellow when the source bridge exists.
  Stage3-Green is blocked when full-window 4B, post-peak drawdown or high-MAE risk remains active.
  Local spike or MFE without source bridge routes to Watch / 4B / high-MAE guard.
```

Positive-control check:

```text
083650 / 035890 / 186230:
  Stage2 survives
  Yellow is allowed with 4B/full-window watch
  Green is rejected
```

False-positive check:

```text
011700 / 007210 / 097870:
  Stage2 is demoted to Watch/4B/high-MAE guard
  Yellow is rejected
  Green is rejected
```

## 10. Current Calibrated Profile Stress Test

| question | R13 result |
|---|---|
| Should delayed MFE be treated as failure? | No, when source bridge exists. |
| Should local spike be treated as positive proof? | No, when source bridge is absent. |
| Does full-window 4B block Green? | Yes, across all six rows. |
| Should Stage2 bonus be globally reversed? | No. Make it bridge-conditional. |
| Does local/full-window 4B split add information? | Yes. It separates bridge-backed delayed winners from local-spike false positives. |
| Are R13 rows new source evidence? | No. They are guardrail diagnostics only. |

## 11. Cross-Archetype Guardrail Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: cross_archetype_guardrail
rule_id: r13_delayed_mfe_survives_only_with_source_bridge

rule:
  Across archetypes, delayed MFE may preserve guarded Stage2/Yellow only when
  the source-archetype bridge exists. Full-window 4B and drawdown still block Green.
  If MFE is local, shallow, or event-driven and the source bridge is absent,
  route the row to Watch / 4B / high-MAE guard and block Yellow/Green.

source_bridge_examples:
  C04 nuclear -> signed project/order, regulatory/legal milestone, EPC/orderbook, execution margin
  C30 construction/PF -> orderbook, balance repair, PF-risk containment, cashflow
  C31 policy/agri -> policy-to-order, subsidy-to-demand, volume/spread/margin/cashflow
```

## 12. Before / After Backtest Comparison

| profile | eligible R13 cross rows | avg MFE90 | avg MAE90 | false-positive risk | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 6 | 17.57 | -17.8 | high if local MFE is over-read | good base, needs bridge-conditional 4B split |
| P2 bridge-conditional delayed-MFE profile | 3 positive controls | 25.61 | -11.28 | low after source bridge gate | preferred shadow |
| P3 local-spike demotion profile | 3 counterexamples | 9.53 | -24.32 | low after no-bridge demotion | useful guard |
| P4 over-tight high-MAE profile | 3 positive-control risk | 25.61 | -11.28 | may incorrectly delete delayed winners | rejected |

## 13. Score-Return Alignment Matrix

| case | source canonical | current profile verdict | R13 alignment |
|---|---|---|---|
| 083650 | C04 | current_profile_correct_but_no_green | Bridge-backed delayed MFE survives; Green blocked |
| 035890 | C30 | current_profile_correct_but_no_green | Slow MFE survives because orderbook/cashflow bridge exists |
| 186230 | C31 | current_profile_correct_but_no_green | Smart-farm policy/order bridge survives as guarded Yellow |
| 011700 | C04 | current_profile_false_positive_if_yellow_or_green | Local nuclear-policy spike lacks order/cashflow bridge |
| 007210 | C30 | current_profile_false_positive_if_yellow_or_green | Building-material spike lacks order/margin/cashflow bridge |
| 097870 | C31 | current_profile_false_positive_if_yellow_or_green | Fertilizer policy MFE lacks volume/margin bridge |

## 14. Coverage Matrix

| large_sector_id | canonical_archetype_id | source archetypes | cross rows | positive controls | counterexamples | new independent | reused/cross | 4B watch | high-MAE/watch | sector_rule | canonical_rule | coverage contribution |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | C04/C30/C31 | 6 | 3 | 3 | 0 | 6 | 6 | 6 | false | true | strengthens R13 local/full-window 4B split without source-archetype coverage increment |

## 15. Residual Contribution Summary

```text
r13_cross_case_count: 6
positive_control_count: 3
counterexample_count: 3
new_independent_case_count: 0
reused_case_count: 6
reused_case_policy: R13 cross-check rows only; no source-archetype evidence weight
new_symbol_count_for_source_archetype: 0
new_trigger_family_count_for_source_archetype: 0
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
residual_error_types_found:
- delayed MFE source-bridge survival
- local spike no-bridge Stage2 false positive
- full-window 4B blocks Green
- high-MAE demotes theme MFE
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: r13_cross_archetype_4b_4c_redteam
```

## 16. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- R13 round consistency
- R13 canonical scope
- cross-archetype source mapping
- do_not_count_as_new_case handling
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
- source-archetype coverage increments
```

## 17. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,r13_delayed_mfe_survives_only_with_source_bridge,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"Across C04/C30/C31, delayed MFE can remain Stage2/Yellow only when a source-archetype bridge exists; Green remains blocked by local/full-window 4B and drawdown risk","083650/035890/186230 survive as guarded positives because project/order/cashflow bridge exists; 011700/007210/097870 are demoted because local spike or MFE lacked source bridge","TRG_R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_083650_20240222|TRG_R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_035890_20240129|TRG_R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_186230_20240221|TRG_R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_011700_20240222|TRG_R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_007210_20240110|TRG_R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_097870_20240626",6,0,3,medium,cross_archetype_shadow_only,"R13 rows have do_not_count_as_new_case=true and independent_evidence_weight=0.0"
shadow_weight,r13_local_spike_without_bridge_demotes_to_4b_high_mae,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,1,1,0,"Local spike, price-only MFE, or theme MFE should not promote Stage3 when source bridge is absent; route to Watch/4B/high-MAE","011700/007210/097870 validate local-spike demotion; positives prevent over-tightening by preserving bridge-backed delayed MFE","TRG_R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_011700_20240222|TRG_R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_007210_20240110|TRG_R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_097870_20240626",6,0,3,medium,existing_axis_kept,"strengthens local/full-window 4B split and high-MAE watch without changing source-archetype coverage"
```

## 18. Machine-Readable Rows

### 18.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_R13_cross_archetype_4B_4C_diagnostics"}
```

### 18.2 case rows

```jsonl
{"row_type":"case","case_id":"R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_083650_20240222","symbol":"083650","company_name":"비에이치아이","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","source_fine_archetype_id":"C04_NUCLEAR_PROJECT_ORDER_EXECUTION_MARGIN_BRIDGE","fine_archetype_id":"R13_DELAYED_MFE_SOURCE_BRIDGE_SURVIVAL_WITH_GREEN_BLOCK","deep_sub_archetype_id":"SOURCE_BRIDGE_DELAYED_MFE_SURVIVES_AS_GUARDED_YELLOW","case_type":"r13_positive_control","positive_or_counterexample":"positive_control","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"score_price_alignment":"score_return_aligned_with_guarded_stage","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-case only: validates delayed-MFE bridge survival versus local-spike no-bridge demotion; does not increase source canonical coverage."}
{"row_type":"case","case_id":"R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_035890_20240129","symbol":"035890","company_name":"서희건설","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_fine_archetype_id":"C30_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE","fine_archetype_id":"R13_DELAYED_MFE_SOURCE_BRIDGE_SURVIVAL_WITH_GREEN_BLOCK","deep_sub_archetype_id":"SOURCE_BRIDGE_DELAYED_MFE_SURVIVES_AS_GUARDED_YELLOW","case_type":"r13_positive_control","positive_or_counterexample":"positive_control","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"score_price_alignment":"score_return_aligned_with_guarded_stage","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-case only: validates delayed-MFE bridge survival versus local-spike no-bridge demotion; does not increase source canonical coverage."}
{"row_type":"case","case_id":"R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_186230_20240221","symbol":"186230","company_name":"그린플러스","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_SMART_FARM_POLICY_ORDER_EXPORT_MARGIN_BRIDGE","fine_archetype_id":"R13_DELAYED_MFE_SOURCE_BRIDGE_SURVIVAL_WITH_GREEN_BLOCK","deep_sub_archetype_id":"SOURCE_BRIDGE_DELAYED_MFE_SURVIVES_AS_GUARDED_YELLOW","case_type":"r13_positive_control","positive_or_counterexample":"positive_control","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"score_price_alignment":"score_return_aligned_with_guarded_stage","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-case only: validates delayed-MFE bridge survival versus local-spike no-bridge demotion; does not increase source canonical coverage."}
{"row_type":"case","case_id":"R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_011700_20240222","symbol":"011700","company_name":"한신기계","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","source_fine_archetype_id":"C04_NUCLEAR_AIR_COMPRESSOR_THEME_WITHOUT_ORDER_CASHFLOW_BRIDGE","fine_archetype_id":"R13_LOCAL_SPIKE_NO_SOURCE_BRIDGE_4B_HIGHMAE_DEMOTION","deep_sub_archetype_id":"LOCAL_SPIKE_OR_THEME_MFE_WITHOUT_SOURCE_BRIDGE_DEMOTED_TO_WATCH","case_type":"r13_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"score_price_alignment":"score_return_misaligned_without_guard","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-case only: validates delayed-MFE bridge survival versus local-spike no-bridge demotion; does not increase source canonical coverage."}
{"row_type":"case","case_id":"R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_007210_20240110","symbol":"007210","company_name":"벽산","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_fine_archetype_id":"C30_BUILDING_MATERIALS_THEME_WITHOUT_ORDER_MARGIN_BRIDGE","fine_archetype_id":"R13_LOCAL_SPIKE_NO_SOURCE_BRIDGE_4B_HIGHMAE_DEMOTION","deep_sub_archetype_id":"LOCAL_SPIKE_OR_THEME_MFE_WITHOUT_SOURCE_BRIDGE_DEMOTED_TO_WATCH","case_type":"r13_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"score_price_alignment":"score_return_misaligned_without_guard","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-case only: validates delayed-MFE bridge survival versus local-spike no-bridge demotion; does not increase source canonical coverage."}
{"row_type":"case","case_id":"R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_097870_20240626","symbol":"097870","company_name":"효성오앤비","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_ORGANIC_FERTILIZER_POLICY_THEME_WITHOUT_VOLUME_MARGIN_BRIDGE","fine_archetype_id":"R13_LOCAL_SPIKE_NO_SOURCE_BRIDGE_4B_HIGHMAE_DEMOTION","deep_sub_archetype_id":"LOCAL_SPIKE_OR_THEME_MFE_WITHOUT_SOURCE_BRIDGE_DEMOTED_TO_WATCH","case_type":"r13_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"score_price_alignment":"score_return_misaligned_without_guard","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-case only: validates delayed-MFE bridge survival versus local-spike no-bridge demotion; does not increase source canonical coverage."}
```

### 18.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_083650_20240222","case_id":"R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_083650_20240222","symbol":"083650","company_name":"비에이치아이","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","source_fine_archetype_id":"C04_NUCLEAR_PROJECT_ORDER_EXECUTION_MARGIN_BRIDGE","fine_archetype_id":"R13_DELAYED_MFE_SOURCE_BRIDGE_SURVIVAL_WITH_GREEN_BLOCK","deep_sub_archetype_id":"SOURCE_BRIDGE_DELAYED_MFE_SURVIVES_AS_GUARDED_YELLOW","loop_objective":"cross_archetype_redteam|4B_local_vs_full_window_split|delayed_MFE_bridge_survival|local_spike_no_bridge_demotion|4C_high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":8560,"evidence_available_at_that_date":"source_proxy_nuclear_power_equipment_HRSG_project_orderbook_execution_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_nuclear_power_equipment_HRSG_project_orderbook_execution_margin_bridge; evidence_url_pending","bridge_summary":"source bridge exists and MFE arrives later or extends beyond the local window; Stage2/Yellow can survive, but Green remains blocked by 4B/full-window drawdown risk","stage2_evidence_fields":["nuclear_power_equipment_order","policy_project_cycle","relative_strength","backlog_visibility_proxy"],"stage3_evidence_fields":["orderbook_to_revenue_visibility","execution_margin_bridge","policy_project_value_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","project_execution_timing_risk","nuclear_policy_crowding","R13_local_vs_full_window_4B_review"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv","profile_path":"atlas/symbol_profiles/083/083650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.8,"MFE_90D_pct":42.17,"MFE_180D_pct":132.71,"MFE_1Y_pct":132.71,"MFE_2Y_pct":132.71,"MAE_30D_pct":-5.96,"MAE_90D_pct":-9.46,"MAE_180D_pct":-17.06,"MAE_1Y_pct":-17.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-22","peak_price":19920,"drawdown_after_peak_pct":-37.25,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":0.61,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"nuclear_project_order_bridge_positive_but_full_window_4B_execution_watch","four_b_evidence_type":"source_bridge_delayed_MFE_positive_control","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"r13_positive_control_delayed_MFE_bridge_survives_with_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_083650_20240222_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_035890_20240129","case_id":"R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_035890_20240129","symbol":"035890","company_name":"서희건설","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_fine_archetype_id":"C30_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE","fine_archetype_id":"R13_DELAYED_MFE_SOURCE_BRIDGE_SURVIVAL_WITH_GREEN_BLOCK","deep_sub_archetype_id":"SOURCE_BRIDGE_DELAYED_MFE_SURVIVES_AS_GUARDED_YELLOW","loop_objective":"cross_archetype_redteam|4B_local_vs_full_window_split|delayed_MFE_bridge_survival|local_spike_no_bridge_demotion|4C_high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":1259,"evidence_available_at_that_date":"source_proxy_regional_housing_orderbook_PF_risk_containment_cashflow_stability_bridge; evidence_url_pending","evidence_source":"source_proxy_regional_housing_orderbook_PF_risk_containment_cashflow_stability_bridge; evidence_url_pending","bridge_summary":"source bridge exists and MFE arrives later or extends beyond the local window; Stage2/Yellow can survive, but Green remains blocked by 4B/full-window drawdown risk","stage2_evidence_fields":["regional_housing_orderbook","PF_risk_containment_proxy","cashflow_stability_proxy","relative_strength"],"stage3_evidence_fields":["orderbook_to_cashflow_visibility","balance_sheet_stability","PF_liquidity_risk_containment"],"stage4b_evidence_fields":["slow_MFE_peak_watch","regional_housing_cycle_crowding","R13_local_vs_full_window_4B_review"],"stage4c_evidence_fields":["housing_cycle_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv","profile_path":"atlas/symbol_profiles/035/035890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.15,"MFE_90D_pct":9.77,"MFE_180D_pct":28.75,"MFE_1Y_pct":28.75,"MFE_2Y_pct":28.75,"MAE_30D_pct":-2.3,"MAE_90D_pct":-2.3,"MAE_180D_pct":-5.48,"MAE_1Y_pct":-5.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-10","peak_price":1621,"drawdown_after_peak_pct":-14.19,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":0.83,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"slow_regional_housing_orderbook_positive_but_4B_housing_cycle_watch","four_b_evidence_type":"source_bridge_delayed_MFE_positive_control","four_c_protection_label":"drawdown_watch_after_peak","trigger_outcome_label":"r13_positive_control_delayed_MFE_bridge_survives_with_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_035890_20240129_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_186230_20240221","case_id":"R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_186230_20240221","symbol":"186230","company_name":"그린플러스","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_SMART_FARM_POLICY_ORDER_EXPORT_MARGIN_BRIDGE","fine_archetype_id":"R13_DELAYED_MFE_SOURCE_BRIDGE_SURVIVAL_WITH_GREEN_BLOCK","deep_sub_archetype_id":"SOURCE_BRIDGE_DELAYED_MFE_SURVIVES_AS_GUARDED_YELLOW","loop_objective":"cross_archetype_redteam|4B_local_vs_full_window_split|delayed_MFE_bridge_survival|local_spike_no_bridge_demotion|4C_high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":9200,"evidence_available_at_that_date":"source_proxy_smart_farm_policy_order_export_revenue_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_smart_farm_policy_order_export_revenue_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"source bridge exists and MFE arrives later or extends beyond the local window; Stage2/Yellow can survive, but Green remains blocked by 4B/full-window drawdown risk","stage2_evidence_fields":["smart_farm_policy","facility_order_proxy","export_optionality","relative_strength"],"stage3_evidence_fields":["policy_to_order_visibility","order_to_revenue_bridge","margin_cashflow_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","project_timing_risk","working_capital_cashflow_watch","R13_local_vs_full_window_4B_review"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/186/186230/2024.csv","profile_path":"atlas/symbol_profiles/186/186230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.89,"MFE_90D_pct":24.89,"MFE_180D_pct":32.61,"MFE_1Y_pct":32.61,"MFE_2Y_pct":32.61,"MAE_30D_pct":-12.83,"MAE_90D_pct":-22.07,"MAE_180D_pct":-22.07,"MAE_1Y_pct":-22.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-20","peak_price":12200,"drawdown_after_peak_pct":-31.48,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":0.75,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smart_farm_policy_order_bridge_positive_but_full_window_4B_cashflow_watch","four_b_evidence_type":"source_bridge_delayed_MFE_positive_control","four_c_protection_label":"drawdown_watch_after_peak","trigger_outcome_label":"r13_positive_control_delayed_MFE_bridge_survives_with_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_186230_20240221_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_011700_20240222","case_id":"R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_011700_20240222","symbol":"011700","company_name":"한신기계","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","source_fine_archetype_id":"C04_NUCLEAR_AIR_COMPRESSOR_THEME_WITHOUT_ORDER_CASHFLOW_BRIDGE","fine_archetype_id":"R13_LOCAL_SPIKE_NO_SOURCE_BRIDGE_4B_HIGHMAE_DEMOTION","deep_sub_archetype_id":"LOCAL_SPIKE_OR_THEME_MFE_WITHOUT_SOURCE_BRIDGE_DEMOTED_TO_WATCH","loop_objective":"cross_archetype_redteam|4B_local_vs_full_window_split|delayed_MFE_bridge_survival|local_spike_no_bridge_demotion|4C_high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":5580,"evidence_available_at_that_date":"source_proxy_nuclear_air_compressor_policy_theme_without_project_order_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_nuclear_air_compressor_policy_theme_without_project_order_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"source bridge is absent; local spike or shallow MFE should be overridden by 4B/high-MAE guard and rejected as positive Stage3 evidence","stage2_evidence_fields":["nuclear_policy_theme","air_compressor_component_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["event_local_peak","order_bridge_absent","margin_cashflow_bridge_absent","R13_local_vs_full_window_4B_review"],"stage4c_evidence_fields":["severe_high_MAE_without_order_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011700/2024.csv","profile_path":"atlas/symbol_profiles/011/011700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.63,"MFE_90D_pct":6.63,"MFE_180D_pct":6.63,"MFE_1Y_pct":6.63,"MFE_2Y_pct":6.63,"MAE_30D_pct":-15.41,"MAE_90D_pct":-23.84,"MAE_180D_pct":-45.7,"MAE_1Y_pct":-45.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-22","peak_price":5950,"drawdown_after_peak_pct":-49.08,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"nuclear_policy_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"local_spike_or_theme_MFE_without_source_bridge","four_c_protection_label":"severe_high_MAE_watch","trigger_outcome_label":"r13_local_spike_no_source_bridge_demoted_to_4B_high_MAE_watch","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_011700_20240222_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_007210_20240110","case_id":"R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_007210_20240110","symbol":"007210","company_name":"벽산","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_fine_archetype_id":"C30_BUILDING_MATERIALS_THEME_WITHOUT_ORDER_MARGIN_BRIDGE","fine_archetype_id":"R13_LOCAL_SPIKE_NO_SOURCE_BRIDGE_4B_HIGHMAE_DEMOTION","deep_sub_archetype_id":"LOCAL_SPIKE_OR_THEME_MFE_WITHOUT_SOURCE_BRIDGE_DEMOTED_TO_WATCH","loop_objective":"cross_archetype_redteam|4B_local_vs_full_window_split|delayed_MFE_bridge_survival|local_spike_no_bridge_demotion|4C_high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":2770,"evidence_available_at_that_date":"source_proxy_building_materials_remodeling_theme_without_housing_order_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_building_materials_remodeling_theme_without_housing_order_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"source bridge is absent; local spike or shallow MFE should be overridden by 4B/high-MAE guard and rejected as positive Stage3 evidence","stage2_evidence_fields":["building_materials_theme","housing_repair_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_theme_peak","housing_order_bridge_absent","margin_cashflow_bridge_absent","R13_local_vs_full_window_4B_review"],"stage4c_evidence_fields":["high_MAE_without_order_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007210/2024.csv","profile_path":"atlas/symbol_profiles/007/007210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.05,"MFE_90D_pct":5.05,"MFE_180D_pct":5.05,"MFE_1Y_pct":5.05,"MFE_2Y_pct":5.05,"MAE_30D_pct":-13.18,"MAE_90D_pct":-24.91,"MAE_180D_pct":-32.85,"MAE_1Y_pct":-32.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-11","peak_price":2910,"drawdown_after_peak_pct":-36.08,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"building_materials_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"local_spike_or_theme_MFE_without_source_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"r13_local_spike_no_source_bridge_demoted_to_4B_high_MAE_watch","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_007210_20240110_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_097870_20240626","case_id":"R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_097870_20240626","symbol":"097870","company_name":"효성오앤비","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_ORGANIC_FERTILIZER_POLICY_THEME_WITHOUT_VOLUME_MARGIN_BRIDGE","fine_archetype_id":"R13_LOCAL_SPIKE_NO_SOURCE_BRIDGE_4B_HIGHMAE_DEMOTION","deep_sub_archetype_id":"LOCAL_SPIKE_OR_THEME_MFE_WITHOUT_SOURCE_BRIDGE_DEMOTED_TO_WATCH","loop_objective":"cross_archetype_redteam|4B_local_vs_full_window_split|delayed_MFE_bridge_survival|local_spike_no_bridge_demotion|4C_high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-26","entry_date":"2024-06-26","entry_price":7390,"evidence_available_at_that_date":"source_proxy_organic_fertilizer_food_security_policy_theme_without_volume_price_cost_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_organic_fertilizer_food_security_policy_theme_without_volume_price_cost_margin_bridge; evidence_url_pending","bridge_summary":"source bridge is absent; local spike or shallow MFE should be overridden by 4B/high-MAE guard and rejected as positive Stage3 evidence","stage2_evidence_fields":["organic_fertilizer_theme","food_security_policy","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_policy_theme_peak","volume_margin_bridge_absent","cashflow_bridge_absent","R13_local_vs_full_window_4B_review"],"stage4c_evidence_fields":["high_MAE_without_volume_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/097/097870/2024.csv","profile_path":"atlas/symbol_profiles/097/097870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.91,"MFE_90D_pct":16.91,"MFE_180D_pct":16.91,"MFE_1Y_pct":16.91,"MFE_2Y_pct":16.91,"MAE_30D_pct":-8.93,"MAE_90D_pct":-24.22,"MAE_180D_pct":-24.22,"MAE_1Y_pct":-24.22,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-27","peak_price":8640,"drawdown_after_peak_pct":-35.19,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"fertilizer_policy_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"local_spike_or_theme_MFE_without_source_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"r13_local_spike_no_source_bridge_demoted_to_4B_high_MAE_watch","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_097870_20240626_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 18.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_083650_20240222","trigger_id":"TRG_R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_083650_20240222","symbol":"083650","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"source_bridge_score":14,"local_peak_risk_score":7,"full_window_MFE_score":11,"MAE_drawdown_penalty":8,"theme_only_penalty":2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":16,"local_peak_risk_score":10,"full_window_MFE_score":12,"MAE_drawdown_penalty":12,"theme_only_penalty":3},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_with_4B_Watch","changed_components":["source_bridge_score","local_peak_risk_score","full_window_MFE_score","MAE_drawdown_penalty","theme_only_penalty"],"component_delta_explanation":"R13 delayed-MFE positive control: source bridge lets Stage2/Yellow survive even when local proximity is not perfect, but full-window 4B/drawdown blocks Green.","MFE_90D_pct":42.17,"MAE_90D_pct":-9.46,"score_return_alignment_label":"score_return_aligned_with_guarded_stage","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_035890_20240129","trigger_id":"TRG_R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_035890_20240129","symbol":"035890","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"source_bridge_score":14,"local_peak_risk_score":7,"full_window_MFE_score":11,"MAE_drawdown_penalty":8,"theme_only_penalty":2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":16,"local_peak_risk_score":10,"full_window_MFE_score":12,"MAE_drawdown_penalty":12,"theme_only_penalty":3},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_with_4B_Watch","changed_components":["source_bridge_score","local_peak_risk_score","full_window_MFE_score","MAE_drawdown_penalty","theme_only_penalty"],"component_delta_explanation":"R13 delayed-MFE positive control: source bridge lets Stage2/Yellow survive even when local proximity is not perfect, but full-window 4B/drawdown blocks Green.","MFE_90D_pct":9.77,"MAE_90D_pct":-2.3,"score_return_alignment_label":"score_return_aligned_with_guarded_stage","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_186230_20240221","trigger_id":"TRG_R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_186230_20240221","symbol":"186230","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"source_bridge_score":14,"local_peak_risk_score":7,"full_window_MFE_score":11,"MAE_drawdown_penalty":8,"theme_only_penalty":2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":16,"local_peak_risk_score":10,"full_window_MFE_score":12,"MAE_drawdown_penalty":12,"theme_only_penalty":3},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_with_4B_Watch","changed_components":["source_bridge_score","local_peak_risk_score","full_window_MFE_score","MAE_drawdown_penalty","theme_only_penalty"],"component_delta_explanation":"R13 delayed-MFE positive control: source bridge lets Stage2/Yellow survive even when local proximity is not perfect, but full-window 4B/drawdown blocks Green.","MFE_90D_pct":24.89,"MAE_90D_pct":-22.07,"score_return_alignment_label":"score_return_aligned_with_guarded_stage","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_011700_20240222","trigger_id":"TRG_R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_011700_20240222","symbol":"011700","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"source_bridge_score":2,"local_peak_risk_score":8,"full_window_MFE_score":6,"MAE_drawdown_penalty":8,"theme_only_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":0,"local_peak_risk_score":14,"full_window_MFE_score":2,"MAE_drawdown_penalty":16,"theme_only_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["source_bridge_score","local_peak_risk_score","full_window_MFE_score","MAE_drawdown_penalty","theme_only_penalty"],"component_delta_explanation":"R13 no-bridge guard: local spike or shallow MFE is demoted when source bridge is absent and high-MAE/full-window decay appears.","MFE_90D_pct":6.63,"MAE_90D_pct":-23.84,"score_return_alignment_label":"score_return_misaligned_without_guard","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_007210_20240110","trigger_id":"TRG_R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_007210_20240110","symbol":"007210","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"source_bridge_score":2,"local_peak_risk_score":8,"full_window_MFE_score":6,"MAE_drawdown_penalty":8,"theme_only_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":0,"local_peak_risk_score":14,"full_window_MFE_score":2,"MAE_drawdown_penalty":16,"theme_only_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["source_bridge_score","local_peak_risk_score","full_window_MFE_score","MAE_drawdown_penalty","theme_only_penalty"],"component_delta_explanation":"R13 no-bridge guard: local spike or shallow MFE is demoted when source bridge is absent and high-MAE/full-window decay appears.","MFE_90D_pct":5.05,"MAE_90D_pct":-24.91,"score_return_alignment_label":"score_return_misaligned_without_guard","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_097870_20240626","trigger_id":"TRG_R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_097870_20240626","symbol":"097870","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"source_bridge_score":2,"local_peak_risk_score":8,"full_window_MFE_score":6,"MAE_drawdown_penalty":8,"theme_only_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":0,"local_peak_risk_score":14,"full_window_MFE_score":2,"MAE_drawdown_penalty":16,"theme_only_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["source_bridge_score","local_peak_risk_score","full_window_MFE_score","MAE_drawdown_penalty","theme_only_penalty"],"component_delta_explanation":"R13 no-bridge guard: local spike or shallow MFE is demoted when source bridge is absent and high-MAE/full-window decay appears.","MFE_90D_pct":16.91,"MAE_90D_pct":-24.22,"score_return_alignment_label":"score_return_misaligned_without_guard","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green"}
```

### 18.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,r13_delayed_mfe_survives_only_with_source_bridge,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"Across C04/C30/C31, delayed MFE can remain Stage2/Yellow only when a source-archetype bridge exists; Green remains blocked by local/full-window 4B and drawdown risk","083650/035890/186230 survive as guarded positives because project/order/cashflow bridge exists; 011700/007210/097870 are demoted because local spike or MFE lacked source bridge","TRG_R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_083650_20240222|TRG_R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_035890_20240129|TRG_R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_186230_20240221|TRG_R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_011700_20240222|TRG_R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_007210_20240110|TRG_R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_097870_20240626",6,0,3,medium,cross_archetype_shadow_only,"R13 rows have do_not_count_as_new_case=true and independent_evidence_weight=0.0"
shadow_weight,r13_local_spike_without_bridge_demotes_to_4b_high_mae,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,1,1,0,"Local spike, price-only MFE, or theme MFE should not promote Stage3 when source bridge is absent; route to Watch/4B/high-MAE","011700/007210/097870 validate local-spike demotion; positives prevent over-tightening by preserving bridge-backed delayed MFE","TRG_R13L75_4B4C_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_011700_20240222|TRG_R13L75_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_007210_20240110|TRG_R13L75_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_097870_20240626",6,0,3,medium,existing_axis_kept,"strengthens local/full-window 4B split and high-MAE watch without changing source-archetype coverage"
```

### 18.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","r13_cross_case_count":6,"new_independent_case_count":0,"reused_case_count":6,"positive_control_count":3,"counterexample_count":3,"new_symbol_count_for_source_archetype":0,"new_trigger_family_count_for_source_archetype":0,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["delayed_MFE_source_bridge_survival","local_spike_no_bridge_stage2_false_positive","full_window_4B_blocks_green","high_MAE_demotes_theme_MFE"],"loop_contribution_label":"r13_cross_archetype_4b_4c_redteam","do_not_propose_new_weight_delta":false}
```

## 19. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update cross-archetype guardrail ledgers.

### R13-specific handling

- R13 cross-case rows must be parsed as trigger rows.
- R13 cross-case rows must keep `do_not_count_as_new_case=true`.
- R13 cross-case rows must not increase source archetype positive/counterexample coverage.
- Use them only for cross-archetype guardrail calibration.
- `independent_evidence_weight=0.0` means no duplicate source evidence.
- `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` rows should update cross_archetype_shadow_profile only.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for guardrail diagnostics.
- Do not count R13 cross rows as new source-archetype evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only/theme-only rows cannot promote Stage2/Stage3.
- Delayed MFE can survive only when source bridge exists.
- Full-window 4B and post-peak drawdown block Green.
- Local spike or shallow MFE without source bridge demotes to Watch/4B/high-MAE.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R13 canonical_archetype_id.
4. Confirm `do_not_count_as_new_case=true` for every R13 cross row.
5. Deduplicate same_entry_group_id.
6. Aggregate only under R13 guardrail, not source archetype coverage.
7. Update cross_archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report cross-case count, positive-control count, counterexamples, 4B watch rows, high-MAE rows, and residual error types.
10. Add tests that R13 rows cannot change source archetype independent coverage.
11. Add tests that delayed MFE survives only when source bridge exists.
12. Add tests that local spike or shallow MFE without source bridge is demoted to Watch/4B/high-MAE.
13. Add tests that full-window 4B and post-peak drawdown block Green.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- R13 4B/4C redteam coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 20. Next Round State

```text
completed_round = R13
completed_loop = 75
next_round = R1
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

## 21. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/083/083650.json
atlas/symbol_profiles/035/035890.json
atlas/symbol_profiles/186/186230.json
atlas/symbol_profiles/011/011700.json
atlas/symbol_profiles/007/007210.json
atlas/symbol_profiles/097/097870.json
atlas/ohlcv_tradable_by_symbol_year/083/083650/2024.csv
atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv
atlas/ohlcv_tradable_by_symbol_year/186/186230/2024.csv
atlas/ohlcv_tradable_by_symbol_year/011/011700/2024.csv
atlas/ohlcv_tradable_by_symbol_year/007/007210/2024.csv
atlas/ohlcv_tradable_by_symbol_year/097/097870/2024.csv
```

This loop completes R13 / loop 75 and moves the scheduler to R1 / loop 76.
