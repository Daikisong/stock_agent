# E2R Stock-Web Historical Calibration / R13 Cross-Archetype 4B/4C Redteam

## 0. Research Metadata

```text
scheduled_round: R13
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R1
computed_next_loop: 77
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: R13_SOURCE_BRIDGE_SURVIVAL_VS_THEME_MFE_NO_BRIDGE_GUARD
loop_objective: cross_archetype_redteam | 4B_local_vs_full_window_split | source_bridge_survival | theme_MFE_no_bridge_demotion | 4C_high_MAE_guardrail
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

R13 is a cross-archetype checkpoint, not a normal sector expansion round. This file therefore uses:

```text
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

Every representative row is marked:

```text
r13_cross_case = true
do_not_count_as_new_case = true
independent_evidence_weight = 0.0
aggregate_group_role = r13_cross_check
```

This run tests the bridge-gate question across three recent source archetypes:

```text
Can the model preserve bridge-backed MFE as guarded Yellow while demoting local/delayed/theme MFE that lacks source bridge?
```

The resulting rule is:

```text
- Source bridge exists: guarded Stage2/Yellow may survive, but Green is blocked by full-window 4B and drawdown/high-MAE.
- Source bridge absent: local, shallow, or delayed MFE is demoted to Watch / 4B / high-MAE.
```

## 3. Cross-Archetype Source Map

| source large sector | source canonical | symbol | company | R13 outcome | local 4B proximity | full-window 4B proximity | 4C/watch label |
|---|---|---:|---|---|---:|---:|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 183190 | 아세아시멘트 | r13_positive_control_source_bridge_survives_as_guarded_yellow | 0.98 | 1.0 | post_peak_drawdown_watch |
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 079550 | LIG넥스원 | r13_positive_control_source_bridge_survives_as_guarded_yellow | 0.77 | 1.0 | post_peak_drawdown_watch |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 035250 | 강원랜드 | r13_positive_control_source_bridge_survives_as_guarded_yellow | 0.99 | 1.0 | post_peak_drawdown_watch |
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 001260 | 남광토건 | r13_no_source_bridge_demoted_to_4b_high_mae_watch | 0.9 | 1.0 | high_MAE_watch |
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 095270 | 웨이브일렉트로 | r13_no_source_bridge_demoted_to_4b_high_mae_watch | 1.0 | 1.0 | severe_high_MAE_watch |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 114090 | GKL | r13_no_source_bridge_demoted_to_4b_high_mae_watch | 1.0 | 1.0 | high_MAE_watch |

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
MFE/MAE/peak/drawdown computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
183190 has a 2022-04-06 corporate-action candidate, outside the selected 2024 representative window.
079550 has no corporate-action candidate dates.
035250 has a 2003-11-04 corporate-action candidate, outside the selected 2024 representative window.
001260 has corporate-action candidates ending 2016-02-05, outside the selected 2024 representative window.
095270 has a 2020-10-15 corporate-action candidate, outside the selected 2024/2025 representative window.
114090 has no corporate-action candidate dates.
All six representative windows are treated as clean for R13 guardrail diagnostics.
```

## 7. Trigger-Level OHLC Backtest Table

| symbol | company | source canonical | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 183190 | 아세아시멘트 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage2-Actionable | 2024-01-29 | 10260 | 13.16 | 13.16 | 15.98 | -2.34 | -4.58 | -4.58 | 2024-07-31 | 11900 | -14.62 |
| 079550 | LIG넥스원 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | Stage2-Actionable | 2024-02-14 | 127000 | 50.63 | 72.83 | 96.06 | -9.13 | -9.13 | -9.13 | 2024-07-17 | 249000 | -32.25 |
| 035250 | 강원랜드 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2024-01-29 | 15110 | 21.38 | 21.38 | 23.16 | -1.06 | -3.31 | -11.78 | 2024-09-05 | 18610 | -11.61 |
| 001260 | 남광토건 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage2-Actionable | 2024-01-29 | 6860 | 11.66 | 11.66 | 24.64 | -3.79 | -12.24 | -13.27 | 2024-07-30 | 8550 | -30.41 |
| 095270 | 웨이브일렉트로 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | Stage2-Actionable | 2024-07-15 | 7320 | 6.69 | 6.69 | 6.69 | -31.42 | -40.3 | -50.07 | 2024-07-16 | 7810 | -53.2 |
| 114090 | GKL | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2024-01-29 | 12990 | 5.62 | 8.47 | 8.47 | -8.01 | -8.01 | -17.55 | 2024-04-05 | 14090 | -23.99 |

## 8. Cross-Case Diagnosis

### 8.1 Bridge-backed guarded-positive rows

`183190`, `079550`, and `035250` survive because the source-archetype bridge is visible.

```text
183190: cement price-cost spread / margin / cashflow bridge
079550: defense export framework / signed order / backlog-to-revenue / margin bridge
035250: domestic casino policy / visitor / revenue / margin / cashflow bridge
```

These rows are not Green. They remain guarded Yellow because post-peak drawdown, full-window 4B, demand sensitivity or regulatory risk is still alive. The bridge is the keel: it lets the boat stay afloat, but the current still prevents full-speed Green.

### 8.2 No-bridge MFE rows

`001260`, `095270`, and `114090` are the opposite side of the gate.

```text
001260: regional contractor delayed MFE without orderbook/PF/balance/cashflow bridge
095270: RF defense component local spike without export framework/backlog bridge
114090: foreign casino visitor-recovery MFE without drop amount/revenue-quality/margin bridge
```

These rows show why MFE cannot be the source of truth. A price spark without economic fuel is smoke, not a furnace.

## 9. Stage2 / Yellow / Green / 4B Comparison

```text
Common R13 rule:
  Stage2-Actionable survives only when a source-archetype bridge exists.
  Stage3-Yellow may survive only as guarded Yellow when the source bridge exists.
  Stage3-Green is blocked when full-window 4B, post-peak drawdown or high-MAE risk remains active.
  Local, shallow or delayed MFE without source bridge routes to Watch / 4B / high-MAE guard.
```

Positive-control check:

```text
183190 / 079550 / 035250:
  Stage2 survives
  Yellow is allowed with 4B/full-window watch
  Green is rejected
```

False-positive check:

```text
001260 / 095270 / 114090:
  Stage2 is demoted to Watch/4B/high-MAE guard
  Yellow is rejected
  Green is rejected
```

## 10. Current Calibrated Profile Stress Test

| question | R13 result |
|---|---|
| Should MFE alone preserve Stage2/Yellow? | No. It survives only when source bridge exists. |
| Should source-bridge rows be deleted because drawdown exists? | No. They survive as guarded Yellow, not Green. |
| Does full-window 4B block Green? | Yes, across all six rows. |
| Should Stage2 bonus be globally reversed? | No. Make it bridge-conditional. |
| Does local/full-window 4B split add information? | Yes. It separates economic-bridge winners from theme-MFE false positives. |
| Are R13 rows new source evidence? | No. They are guardrail diagnostics only. |

## 11. Cross-Archetype Guardrail Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: cross_archetype_guardrail
rule_id: r13_source_bridge_survives_as_guarded_yellow_but_blocks_green

rule:
  Across archetypes, MFE may preserve guarded Stage2/Yellow only when
  the source-archetype bridge exists. Full-window 4B and drawdown still block Green.
  If MFE is local, shallow, or delayed and the source bridge is absent,
  route the row to Watch / 4B / high-MAE guard and block Yellow/Green.

source_bridge_examples:
  C30 construction/PF -> price-cost margin, orderbook, balance repair, PF-risk containment, cashflow
  C03 defense export -> export framework, signed order, backlog-to-revenue, execution margin
  C31 policy/tourism -> policy-to-demand, visitor demand, revenue quality, margin, cashflow
```

## 12. Before / After Backtest Comparison

| profile | eligible R13 cross rows | avg MFE90 | avg MAE90 | false-positive risk | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 6 | 22.36 | -12.93 | high if MFE is over-read | good base, needs source-bridge conditional 4B split |
| P2 source-bridge survival profile | 3 positive controls | 35.79 | -5.67 | low after source bridge gate | preferred shadow |
| P3 no-bridge MFE demotion profile | 3 counterexamples | 8.94 | -20.18 | low after demotion | useful guard |
| P4 over-tight high-MAE profile | 3 positive-control risk | 35.79 | -5.67 | may incorrectly delete bridge-backed winners | rejected |

## 13. Score-Return Alignment Matrix

| case | source canonical | current profile verdict | R13 alignment |
|---|---|---|---|
| 183190 | C30 | current_profile_correct_but_no_green | Source bridge survives; Green blocked |
| 079550 | C03 | current_profile_correct_but_no_green | Export/backlog bridge survives; Green blocked |
| 035250 | C31 | current_profile_correct_but_no_green | Policy/visitor/revenue bridge survives; Green blocked |
| 001260 | C30 | current_profile_false_positive_if_yellow_or_green | Contractor rebound MFE lacks source bridge |
| 095270 | C03 | current_profile_false_positive_if_yellow_or_green | RF component spike lacks export/backlog bridge |
| 114090 | C31 | current_profile_false_positive_if_yellow_or_green | Foreign casino MFE lacks revenue/margin bridge |

## 14. Coverage Matrix

| large_sector_id | canonical_archetype_id | source archetypes | cross rows | positive controls | counterexamples | new independent | reused/cross | 4B watch | high-MAE/watch | sector_rule | canonical_rule | coverage contribution |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | C30/C03/C31 | 6 | 3 | 3 | 0 | 6 | 6 | 6 | false | true | strengthens R13 source-bridge 4B/4C gate without source-archetype coverage increment |

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
- source bridge survival as guarded Yellow
- theme MFE without source bridge false positive
- full-window 4B blocks Green
- high-MAE demotes no-bridge MFE
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
shadow_weight,r13_source_bridge_survives_as_guarded_yellow_but_blocks_green,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"Across C30/C03/C31, Stage2/Yellow can survive only when source bridge exists; full-window 4B and drawdown still block Green","183190/079550/035250 survive as guarded positives because price-cost/export-framework/visitor-revenue bridges exist; 001260/095270/114090 are demoted because MFE lacked source bridge","TRG_R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_183190_20240129|TRG_R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_079550_20240214|TRG_R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_035250_20240129|TRG_R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001260_20240129|TRG_R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_095270_20240715|TRG_R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_114090_20240129",6,0,3,medium,cross_archetype_shadow_only,"R13 rows have do_not_count_as_new_case=true and independent_evidence_weight=0.0"
shadow_weight,r13_theme_mfe_without_source_bridge_demotes_to_4b_high_mae,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,1,1,0,"Local spike, shallow MFE, or delayed MFE should not promote Stage3 when source bridge is absent; route to Watch/4B/high-MAE","001260/095270/114090 validate no-bridge demotion; positives prevent over-tightening by preserving bridge-backed MFE rows","TRG_R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001260_20240129|TRG_R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_095270_20240715|TRG_R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_114090_20240129",6,0,3,medium,existing_axis_kept,"strengthens source-bridge gate, local/full-window 4B split and high-MAE watch without source-archetype coverage increment"
```

## 18. Machine-Readable Rows

### 18.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_R13_cross_archetype_4B_4C_diagnostics"}
```

### 18.2 case rows

```jsonl
{"row_type":"case","case_id":"R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_183190_20240129","symbol":"183190","company_name":"아세아시멘트","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_fine_archetype_id":"C30_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE","fine_archetype_id":"R13_SOURCE_BRIDGE_DELAYED_OR_EXTENDED_MFE_SURVIVAL_WITH_GREEN_BLOCK","deep_sub_archetype_id":"SOURCE_ARCHETYPE_BRIDGE_SURVIVES_AS_GUARDED_YELLOW_BUT_FULL_WINDOW_4B_BLOCKS_GREEN","case_type":"r13_positive_control","positive_or_counterexample":"positive_control","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"score_price_alignment":"score_return_aligned_with_guarded_stage","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-case only: validates source-bridge survival versus no-bridge MFE demotion; does not increase source canonical coverage."}
{"row_type":"case","case_id":"R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_079550_20240214","symbol":"079550","company_name":"LIG넥스원","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","source_fine_archetype_id":"C03_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"R13_SOURCE_BRIDGE_DELAYED_OR_EXTENDED_MFE_SURVIVAL_WITH_GREEN_BLOCK","deep_sub_archetype_id":"SOURCE_ARCHETYPE_BRIDGE_SURVIVES_AS_GUARDED_YELLOW_BUT_FULL_WINDOW_4B_BLOCKS_GREEN","case_type":"r13_positive_control","positive_or_counterexample":"positive_control","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"score_price_alignment":"score_return_aligned_with_guarded_stage","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-case only: validates source-bridge survival versus no-bridge MFE demotion; does not increase source canonical coverage."}
{"row_type":"case","case_id":"R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_035250_20240129","symbol":"035250","company_name":"강원랜드","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE","fine_archetype_id":"R13_SOURCE_BRIDGE_DELAYED_OR_EXTENDED_MFE_SURVIVAL_WITH_GREEN_BLOCK","deep_sub_archetype_id":"SOURCE_ARCHETYPE_BRIDGE_SURVIVES_AS_GUARDED_YELLOW_BUT_FULL_WINDOW_4B_BLOCKS_GREEN","case_type":"r13_positive_control","positive_or_counterexample":"positive_control","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"score_price_alignment":"score_return_aligned_with_guarded_stage","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-case only: validates source-bridge survival versus no-bridge MFE demotion; does not increase source canonical coverage."}
{"row_type":"case","case_id":"R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001260_20240129","symbol":"001260","company_name":"남광토건","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_fine_archetype_id":"C30_REGIONAL_CONTRACTOR_REBOUND_WITHOUT_ORDER_CASHFLOW_BRIDGE","fine_archetype_id":"R13_THEME_MFE_NO_SOURCE_BRIDGE_4B_HIGHMAE_DEMOTION","deep_sub_archetype_id":"LOCAL_OR_DELAYED_MFE_WITHOUT_SOURCE_BRIDGE_DEMOTED_TO_WATCH_4B_HIGHMAE","case_type":"r13_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"score_price_alignment":"score_return_misaligned_without_guard","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-case only: validates source-bridge survival versus no-bridge MFE demotion; does not increase source canonical coverage."}
{"row_type":"case","case_id":"R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_095270_20240715","symbol":"095270","company_name":"웨이브일렉트로","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","source_fine_archetype_id":"C03_RF_DEFENSE_COMPONENT_SPIKE_WITHOUT_EXPORT_BACKLOG_BRIDGE","fine_archetype_id":"R13_THEME_MFE_NO_SOURCE_BRIDGE_4B_HIGHMAE_DEMOTION","deep_sub_archetype_id":"LOCAL_OR_DELAYED_MFE_WITHOUT_SOURCE_BRIDGE_DEMOTED_TO_WATCH_4B_HIGHMAE","case_type":"r13_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"score_price_alignment":"score_return_misaligned_without_guard","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-case only: validates source-bridge survival versus no-bridge MFE demotion; does not increase source canonical coverage."}
{"row_type":"case","case_id":"R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_114090_20240129","symbol":"114090","company_name":"GKL","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_FOREIGN_CASINO_VISITOR_THEME_WITHOUT_DURABLE_MARGIN_BRIDGE","fine_archetype_id":"R13_THEME_MFE_NO_SOURCE_BRIDGE_4B_HIGHMAE_DEMOTION","deep_sub_archetype_id":"LOCAL_OR_DELAYED_MFE_WITHOUT_SOURCE_BRIDGE_DEMOTED_TO_WATCH_4B_HIGHMAE","case_type":"r13_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"score_price_alignment":"score_return_misaligned_without_guard","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-case only: validates source-bridge survival versus no-bridge MFE demotion; does not increase source canonical coverage."}
```

### 18.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_183190_20240129","case_id":"R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_183190_20240129","symbol":"183190","company_name":"아세아시멘트","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_fine_archetype_id":"C30_CEMENT_PRICE_COST_MARGIN_CASHFLOW_BRIDGE","fine_archetype_id":"R13_SOURCE_BRIDGE_DELAYED_OR_EXTENDED_MFE_SURVIVAL_WITH_GREEN_BLOCK","deep_sub_archetype_id":"SOURCE_ARCHETYPE_BRIDGE_SURVIVES_AS_GUARDED_YELLOW_BUT_FULL_WINDOW_4B_BLOCKS_GREEN","loop_objective":"cross_archetype_redteam|4B_local_vs_full_window_split|source_bridge_survival|theme_MFE_no_bridge_demotion|4C_high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":10260,"evidence_available_at_that_date":"source_proxy_cement_price_cost_spread_volume_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_cement_price_cost_spread_volume_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"source-archetype bridge exists, so Stage2/Yellow may survive even when full-window 4B or drawdown appears; Green remains blocked by 4B/high-MAE guard","stage2_evidence_fields":["cement_price_cost_spread","fuel_cost_relief_proxy","relative_strength","cashflow_stability_proxy"],"stage3_evidence_fields":["price_cost_spread_to_margin_visibility","volume_mix_stability","cashflow_conversion_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","cement_cycle_crowding","spread_reversal_risk","R13_source_bridge_vs_no_bridge_4B_review"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/183/183190/2024.csv","profile_path":"atlas/symbol_profiles/183/183190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.16,"MFE_90D_pct":13.16,"MFE_180D_pct":15.98,"MFE_1Y_pct":15.98,"MFE_2Y_pct":15.98,"MAE_30D_pct":-2.34,"MAE_90D_pct":-4.58,"MAE_180D_pct":-4.58,"MAE_1Y_pct":-4.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":11900,"drawdown_after_peak_pct":-14.62,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"cement_price_cost_margin_bridge_positive_but_full_window_4B_watch","four_b_evidence_type":"source_bridge_survives_as_guarded_yellow","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"r13_positive_control_source_bridge_survives_as_guarded_yellow","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_183190_20240129_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_079550_20240214","case_id":"R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_079550_20240214","symbol":"079550","company_name":"LIG넥스원","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","source_fine_archetype_id":"C03_GUIDED_WEAPON_EXPORT_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"R13_SOURCE_BRIDGE_DELAYED_OR_EXTENDED_MFE_SURVIVAL_WITH_GREEN_BLOCK","deep_sub_archetype_id":"SOURCE_ARCHETYPE_BRIDGE_SURVIVES_AS_GUARDED_YELLOW_BUT_FULL_WINDOW_4B_BLOCKS_GREEN","loop_objective":"cross_archetype_redteam|4B_local_vs_full_window_split|source_bridge_survival|theme_MFE_no_bridge_demotion|4C_high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":127000,"evidence_available_at_that_date":"source_proxy_guided_weapon_export_framework_orderbook_backlog_margin_revenue_visibility_bridge; evidence_url_pending","evidence_source":"source_proxy_guided_weapon_export_framework_orderbook_backlog_margin_revenue_visibility_bridge; evidence_url_pending","bridge_summary":"source-archetype bridge exists, so Stage2/Yellow may survive even when full-window 4B or drawdown appears; Green remains blocked by 4B/high-MAE guard","stage2_evidence_fields":["guided_weapon_export_framework","defense_orderbook_proxy","relative_strength","margin_bridge_proxy"],"stage3_evidence_fields":["export_framework_to_backlog_visibility","backlog_to_revenue_bridge","margin_earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","defense_export_crowding","order_execution_timing_risk","R13_source_bridge_vs_no_bridge_4B_review"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv","profile_path":"atlas/symbol_profiles/079/079550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":50.63,"MFE_90D_pct":72.83,"MFE_180D_pct":96.06,"MFE_1Y_pct":96.06,"MFE_2Y_pct":96.06,"MAE_30D_pct":-9.13,"MAE_90D_pct":-9.13,"MAE_180D_pct":-9.13,"MAE_1Y_pct":-9.13,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":249000,"drawdown_after_peak_pct":-32.25,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"guided_weapon_export_backlog_bridge_positive_but_full_window_4B_drawdown_watch","four_b_evidence_type":"source_bridge_survives_as_guarded_yellow","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"r13_positive_control_source_bridge_survives_as_guarded_yellow","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_079550_20240214_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_035250_20240129","case_id":"R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_035250_20240129","symbol":"035250","company_name":"강원랜드","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE","fine_archetype_id":"R13_SOURCE_BRIDGE_DELAYED_OR_EXTENDED_MFE_SURVIVAL_WITH_GREEN_BLOCK","deep_sub_archetype_id":"SOURCE_ARCHETYPE_BRIDGE_SURVIVES_AS_GUARDED_YELLOW_BUT_FULL_WINDOW_4B_BLOCKS_GREEN","loop_objective":"cross_archetype_redteam|4B_local_vs_full_window_split|source_bridge_survival|theme_MFE_no_bridge_demotion|4C_high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":15110,"evidence_available_at_that_date":"source_proxy_domestic_casino_policy_capacity_visitor_recovery_revenue_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_domestic_casino_policy_capacity_visitor_recovery_revenue_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"source-archetype bridge exists, so Stage2/Yellow may survive even when full-window 4B or drawdown appears; Green remains blocked by 4B/high-MAE guard","stage2_evidence_fields":["casino_policy_capacity","visitor_recovery_proxy","relative_strength","margin_cashflow_proxy"],"stage3_evidence_fields":["visitor_to_revenue_visibility","margin_cashflow_bridge","policy_capacity_normalization_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","casino_policy_crowding","regulatory_reversal_risk","R13_source_bridge_vs_no_bridge_4B_review"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035250/2024.csv","profile_path":"atlas/symbol_profiles/035/035250.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.38,"MFE_90D_pct":21.38,"MFE_180D_pct":23.16,"MFE_1Y_pct":23.16,"MFE_2Y_pct":23.16,"MAE_30D_pct":-1.06,"MAE_90D_pct":-3.31,"MAE_180D_pct":-11.78,"MAE_1Y_pct":-11.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-05","peak_price":18610,"drawdown_after_peak_pct":-11.61,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"casino_policy_visitor_margin_bridge_positive_but_full_window_4B_watch","four_b_evidence_type":"source_bridge_survives_as_guarded_yellow","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"r13_positive_control_source_bridge_survives_as_guarded_yellow","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_035250_20240129_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001260_20240129","case_id":"R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001260_20240129","symbol":"001260","company_name":"남광토건","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_fine_archetype_id":"C30_REGIONAL_CONTRACTOR_REBOUND_WITHOUT_ORDER_CASHFLOW_BRIDGE","fine_archetype_id":"R13_THEME_MFE_NO_SOURCE_BRIDGE_4B_HIGHMAE_DEMOTION","deep_sub_archetype_id":"LOCAL_OR_DELAYED_MFE_WITHOUT_SOURCE_BRIDGE_DEMOTED_TO_WATCH_4B_HIGHMAE","loop_objective":"cross_archetype_redteam|4B_local_vs_full_window_split|source_bridge_survival|theme_MFE_no_bridge_demotion|4C_high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":6860,"evidence_available_at_that_date":"source_proxy_regional_contractor_policy_rebound_without_orderbook_PF_balance_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_regional_contractor_policy_rebound_without_orderbook_PF_balance_cashflow_bridge; evidence_url_pending","bridge_summary":"source-archetype bridge is absent; local or delayed MFE should be treated as theme/rebound heat and demoted to Watch/4B/high-MAE guard","stage2_evidence_fields":["regional_contractor_rebound","construction_policy_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["delayed_MFE_peak","orderbook_bridge_absent","balance_cashflow_bridge_absent","R13_source_bridge_vs_no_bridge_4B_review"],"stage4c_evidence_fields":["high_MAE_without_orderbook_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv","profile_path":"atlas/symbol_profiles/001/001260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.66,"MFE_90D_pct":11.66,"MFE_180D_pct":24.64,"MFE_1Y_pct":24.64,"MFE_2Y_pct":24.64,"MAE_30D_pct":-3.79,"MAE_90D_pct":-12.24,"MAE_180D_pct":-13.27,"MAE_1Y_pct":-13.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":8550,"drawdown_after_peak_pct":-30.41,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"regional_contractor_rebound_MFE_but_no_order_cashflow_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"theme_or_rebound_MFE_without_source_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"r13_no_source_bridge_demoted_to_4b_high_mae_watch","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001260_20240129_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_095270_20240715","case_id":"R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_095270_20240715","symbol":"095270","company_name":"웨이브일렉트로","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","source_fine_archetype_id":"C03_RF_DEFENSE_COMPONENT_SPIKE_WITHOUT_EXPORT_BACKLOG_BRIDGE","fine_archetype_id":"R13_THEME_MFE_NO_SOURCE_BRIDGE_4B_HIGHMAE_DEMOTION","deep_sub_archetype_id":"LOCAL_OR_DELAYED_MFE_WITHOUT_SOURCE_BRIDGE_DEMOTED_TO_WATCH_4B_HIGHMAE","loop_objective":"cross_archetype_redteam|4B_local_vs_full_window_split|source_bridge_survival|theme_MFE_no_bridge_demotion|4C_high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-15","entry_date":"2024-07-15","entry_price":7320,"evidence_available_at_that_date":"source_proxy_RF_defense_component_missile_electronics_theme_without_export_framework_backlog_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_RF_defense_component_missile_electronics_theme_without_export_framework_backlog_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"source-archetype bridge is absent; local or delayed MFE should be treated as theme/rebound heat and demoted to Watch/4B/high-MAE guard","stage2_evidence_fields":["RF_defense_component_theme","missile_electronics_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_spike_peak","export_framework_bridge_absent","backlog_cashflow_bridge_absent","R13_source_bridge_vs_no_bridge_4B_review"],"stage4c_evidence_fields":["severe_high_MAE_without_export_backlog_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095270/2024.csv|atlas/ohlcv_tradable_by_symbol_year/095/095270/2025.csv","profile_path":"atlas/symbol_profiles/095/095270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.69,"MFE_90D_pct":6.69,"MFE_180D_pct":6.69,"MFE_1Y_pct":6.69,"MFE_2Y_pct":6.69,"MAE_30D_pct":-31.42,"MAE_90D_pct":-40.3,"MAE_180D_pct":-50.07,"MAE_1Y_pct":-50.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-16","peak_price":7810,"drawdown_after_peak_pct":-53.2,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"RF_defense_component_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"theme_or_rebound_MFE_without_source_bridge","four_c_protection_label":"severe_high_MAE_watch","trigger_outcome_label":"r13_no_source_bridge_demoted_to_4b_high_mae_watch","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_095270_20240715_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_114090_20240129","case_id":"R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_114090_20240129","symbol":"114090","company_name":"GKL","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_FOREIGN_CASINO_VISITOR_THEME_WITHOUT_DURABLE_MARGIN_BRIDGE","fine_archetype_id":"R13_THEME_MFE_NO_SOURCE_BRIDGE_4B_HIGHMAE_DEMOTION","deep_sub_archetype_id":"LOCAL_OR_DELAYED_MFE_WITHOUT_SOURCE_BRIDGE_DEMOTED_TO_WATCH_4B_HIGHMAE","loop_objective":"cross_archetype_redteam|4B_local_vs_full_window_split|source_bridge_survival|theme_MFE_no_bridge_demotion|4C_high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":12990,"evidence_available_at_that_date":"source_proxy_foreigner_casino_visitor_recovery_theme_without_drop_amount_revenue_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_foreigner_casino_visitor_recovery_theme_without_drop_amount_revenue_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"source-archetype bridge is absent; local or delayed MFE should be treated as theme/rebound heat and demoted to Watch/4B/high-MAE guard","stage2_evidence_fields":["foreign_casino_recovery_theme","visitor_rebound_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","drop_amount_bridge_absent","margin_cashflow_bridge_absent","R13_source_bridge_vs_no_bridge_4B_review"],"stage4c_evidence_fields":["high_MAE_without_visitor_revenue_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/114/114090/2024.csv","profile_path":"atlas/symbol_profiles/114/114090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.62,"MFE_90D_pct":8.47,"MFE_180D_pct":8.47,"MFE_1Y_pct":8.47,"MFE_2Y_pct":8.47,"MAE_30D_pct":-8.01,"MAE_90D_pct":-8.01,"MAE_180D_pct":-17.55,"MAE_1Y_pct":-17.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-05","peak_price":14090,"drawdown_after_peak_pct":-23.99,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"foreign_casino_visitor_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"theme_or_rebound_MFE_without_source_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"r13_no_source_bridge_demoted_to_4b_high_mae_watch","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_114090_20240129_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype 4B/4C diagnostic; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 18.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_183190_20240129","trigger_id":"TRG_R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_183190_20240129","symbol":"183190","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"source_bridge_score":14,"local_peak_risk_score":7,"full_window_MFE_score":11,"MAE_drawdown_penalty":8,"theme_only_penalty":2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":16,"local_peak_risk_score":10,"full_window_MFE_score":12,"MAE_drawdown_penalty":12,"theme_only_penalty":3},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_with_4B_Watch","changed_components":["source_bridge_score","local_peak_risk_score","full_window_MFE_score","MAE_drawdown_penalty","theme_only_penalty"],"component_delta_explanation":"R13 source-bridge positive control: bridge-backed rows survive as guarded Yellow, but full-window 4B/drawdown blocks Green.","MFE_90D_pct":13.16,"MAE_90D_pct":-4.58,"score_return_alignment_label":"score_return_aligned_with_guarded_stage","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_079550_20240214","trigger_id":"TRG_R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_079550_20240214","symbol":"079550","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"source_bridge_score":14,"local_peak_risk_score":7,"full_window_MFE_score":11,"MAE_drawdown_penalty":8,"theme_only_penalty":2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":16,"local_peak_risk_score":10,"full_window_MFE_score":12,"MAE_drawdown_penalty":12,"theme_only_penalty":3},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_with_4B_Watch","changed_components":["source_bridge_score","local_peak_risk_score","full_window_MFE_score","MAE_drawdown_penalty","theme_only_penalty"],"component_delta_explanation":"R13 source-bridge positive control: bridge-backed rows survive as guarded Yellow, but full-window 4B/drawdown blocks Green.","MFE_90D_pct":72.83,"MAE_90D_pct":-9.13,"score_return_alignment_label":"score_return_aligned_with_guarded_stage","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_035250_20240129","trigger_id":"TRG_R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_035250_20240129","symbol":"035250","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"source_bridge_score":14,"local_peak_risk_score":7,"full_window_MFE_score":11,"MAE_drawdown_penalty":8,"theme_only_penalty":2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":16,"local_peak_risk_score":10,"full_window_MFE_score":12,"MAE_drawdown_penalty":12,"theme_only_penalty":3},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_with_4B_Watch","changed_components":["source_bridge_score","local_peak_risk_score","full_window_MFE_score","MAE_drawdown_penalty","theme_only_penalty"],"component_delta_explanation":"R13 source-bridge positive control: bridge-backed rows survive as guarded Yellow, but full-window 4B/drawdown blocks Green.","MFE_90D_pct":21.38,"MAE_90D_pct":-3.31,"score_return_alignment_label":"score_return_aligned_with_guarded_stage","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001260_20240129","trigger_id":"TRG_R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001260_20240129","symbol":"001260","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"source_bridge_score":2,"local_peak_risk_score":8,"full_window_MFE_score":6,"MAE_drawdown_penalty":8,"theme_only_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":0,"local_peak_risk_score":14,"full_window_MFE_score":2,"MAE_drawdown_penalty":16,"theme_only_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["source_bridge_score","local_peak_risk_score","full_window_MFE_score","MAE_drawdown_penalty","theme_only_penalty"],"component_delta_explanation":"R13 no-bridge guard: local or delayed MFE is demoted when source bridge is absent and high-MAE/full-window decay appears.","MFE_90D_pct":11.66,"MAE_90D_pct":-12.24,"score_return_alignment_label":"score_return_misaligned_without_guard","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_095270_20240715","trigger_id":"TRG_R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_095270_20240715","symbol":"095270","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","raw_component_scores_before":{"source_bridge_score":2,"local_peak_risk_score":8,"full_window_MFE_score":6,"MAE_drawdown_penalty":8,"theme_only_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":0,"local_peak_risk_score":14,"full_window_MFE_score":2,"MAE_drawdown_penalty":16,"theme_only_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["source_bridge_score","local_peak_risk_score","full_window_MFE_score","MAE_drawdown_penalty","theme_only_penalty"],"component_delta_explanation":"R13 no-bridge guard: local or delayed MFE is demoted when source bridge is absent and high-MAE/full-window decay appears.","MFE_90D_pct":6.69,"MAE_90D_pct":-40.3,"score_return_alignment_label":"score_return_misaligned_without_guard","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_114090_20240129","trigger_id":"TRG_R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_114090_20240129","symbol":"114090","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"source_bridge_score":2,"local_peak_risk_score":8,"full_window_MFE_score":6,"MAE_drawdown_penalty":8,"theme_only_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":0,"local_peak_risk_score":14,"full_window_MFE_score":2,"MAE_drawdown_penalty":16,"theme_only_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["source_bridge_score","local_peak_risk_score","full_window_MFE_score","MAE_drawdown_penalty","theme_only_penalty"],"component_delta_explanation":"R13 no-bridge guard: local or delayed MFE is demoted when source bridge is absent and high-MAE/full-window decay appears.","MFE_90D_pct":8.47,"MAE_90D_pct":-8.01,"score_return_alignment_label":"score_return_misaligned_without_guard","current_profile_verdict":"current_profile_false_positive_if_yellow_or_green"}
```

### 18.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,r13_source_bridge_survives_as_guarded_yellow_but_blocks_green,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"Across C30/C03/C31, Stage2/Yellow can survive only when source bridge exists; full-window 4B and drawdown still block Green","183190/079550/035250 survive as guarded positives because price-cost/export-framework/visitor-revenue bridges exist; 001260/095270/114090 are demoted because MFE lacked source bridge","TRG_R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_183190_20240129|TRG_R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_079550_20240214|TRG_R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_035250_20240129|TRG_R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001260_20240129|TRG_R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_095270_20240715|TRG_R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_114090_20240129",6,0,3,medium,cross_archetype_shadow_only,"R13 rows have do_not_count_as_new_case=true and independent_evidence_weight=0.0"
shadow_weight,r13_theme_mfe_without_source_bridge_demotes_to_4b_high_mae,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,1,1,0,"Local spike, shallow MFE, or delayed MFE should not promote Stage3 when source bridge is absent; route to Watch/4B/high-MAE","001260/095270/114090 validate no-bridge demotion; positives prevent over-tightening by preserving bridge-backed MFE rows","TRG_R13L76_4B4C_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_001260_20240129|TRG_R13L76_4B4C_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_095270_20240715|TRG_R13L76_4B4C_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_114090_20240129",6,0,3,medium,existing_axis_kept,"strengthens source-bridge gate, local/full-window 4B split and high-MAE watch without source-archetype coverage increment"
```

### 18.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","r13_cross_case_count":6,"new_independent_case_count":0,"reused_case_count":6,"positive_control_count":3,"counterexample_count":3,"new_symbol_count_for_source_archetype":0,"new_trigger_family_count_for_source_archetype":0,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["source_bridge_survival_as_guarded_yellow","theme_MFE_without_source_bridge_false_positive","full_window_4B_blocks_green","high_MAE_demotes_no_bridge_MFE"],"loop_contribution_label":"r13_cross_archetype_4b_4c_redteam","do_not_propose_new_weight_delta":false}
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
- Positive score promotion requires non-price evidence and clean MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only/theme-only rows cannot promote Stage2/Stage3.
- MFE can survive only when source bridge exists.
- Full-window 4B and post-peak drawdown block Green.
- Local, shallow or delayed MFE without source bridge demotes to Watch/4B/high-MAE.
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
11. Add tests that MFE survives only when source bridge exists.
12. Add tests that local/shallow/delayed MFE without source bridge is demoted to Watch/4B/high-MAE.
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
completed_loop = 76
next_round = R1
next_loop = 77
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
atlas/symbol_profiles/183/183190.json
atlas/symbol_profiles/079/079550.json
atlas/symbol_profiles/035/035250.json
atlas/symbol_profiles/001/001260.json
atlas/symbol_profiles/095/095270.json
atlas/symbol_profiles/114/114090.json
atlas/ohlcv_tradable_by_symbol_year/183/183190/2024.csv
atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv
atlas/ohlcv_tradable_by_symbol_year/035/035250/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv
atlas/ohlcv_tradable_by_symbol_year/095/095270/2024.csv
atlas/ohlcv_tradable_by_symbol_year/095/095270/2025.csv
atlas/ohlcv_tradable_by_symbol_year/114/114090/2024.csv
```

This loop completes R13 / loop 76 and moves the scheduler to R1 / loop 77.
