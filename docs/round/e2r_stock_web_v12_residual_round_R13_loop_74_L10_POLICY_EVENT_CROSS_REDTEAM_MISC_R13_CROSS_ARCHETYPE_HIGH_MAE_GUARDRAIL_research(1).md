# E2R Stock-Web Historical Calibration / R13 Cross-Archetype High-MAE Guardrail

## 0. Research Metadata

```text
scheduled_round: R13
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R1
computed_next_loop: 75
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: R13_HIGH_MAE_SOURCE_BRIDGE_SURVIVAL_AND_MFE_OVERRIDE_GUARD
loop_objective: cross_archetype_redteam | high_MAE_guardrail | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | positive_control_bridge_survival
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
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```

Every representative row is marked:

```text
r13_cross_case = true
do_not_count_as_new_case = true
independent_evidence_weight = 0.0
aggregate_group_role = r13_cross_check
```

This run tests a different R13 axis from the previous Stage2 false-positive review:

```text
When MFE exists but the path later prints high MAE, should the system keep the row as Stage2/Yellow if a source bridge exists, and demote it when the source bridge is absent?
```

The answer from this set is yes. High-MAE is a gate, not a blind delete button. It blocks Green, but source-bridge-positive rows may survive as guarded Yellow.

## 3. Cross-Archetype Source Map

| source large sector | source canonical | symbol | company | outcome | 4B verdict | 4C/watch label |
|---|---|---:|---|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 039130 | 하나투어 | bridge_backed_stage2_survives_with_4B_high_MAE_watch | positive_control_survives_because_source_bridge_exists_but_green_blocked_by_MAE | drawdown_watch |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 080160 | 모두투어 | stage2_false_positive_high_MAE | theme_local_peak_and_high_MAE_rejected_as_positive_stage | high_MAE_watch |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 034230 | 파라다이스 | MFE_then_high_MAE_counterexample | MFE_exists_but_source_bridge_absent_keep_4B_high_MAE_watch | high_MAE_watch |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 040300 | YTN | stage2_false_positive_severe_high_MAE | event_local_peak_and_severe_MAE_rejected_as_positive_stage | severe_high_MAE_watch |
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 002780 | 진흥기업 | stage2_false_positive_high_MAE | construction_theme_local_4B_rejected_as_positive_stage | high_MAE_watch |

## 4. No-Repeat / Duplicate Handling

No-Repeat hard duplicate key remains:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

For R13, these rows are cross-check rows, not new source-archetype rows.

```text
r13_cross_case_count = 5
positive_control_count = 1
counterexample_count = 4
new_independent_case_count = 0
reused_case_count = 5
source_archetype_coverage_increment = 0
independent_evidence_weight = 0.0
do_not_count_as_new_case = true
```

## 5. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_R13_cross_guardrail_diagnostics"}
```

Stock-web assumptions used in this MD:

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
039130 has corporate-action candidate dates in 2003/2004, outside the selected 2024 window.
080160 has corporate-action candidates ending 2017, outside the selected 2024 window.
034230 has no corporate-action contamination in the selected 2024 representative window.
040300 has no corporate-action candidate dates.
002780 has corporate-action candidates ending 2015, outside the selected 2024 window.
All five representative windows are treated as clean for R13 guardrail diagnostics.
```

## 7. Trigger-Level OHLC Backtest Table

| symbol | company | source canonical | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 039130 | 하나투어 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2024-01-29 | 60900 | 12.97 | 15.93 | 15.93 | -3.28 | -8.87 | -27.5 | 2024-03-25 | 70600 | -37.46 |
| 080160 | 모두투어 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2024-01-29 | 17070 | 4.04 | 4.04 | 4.04 | -10.84 | -10.84 | -40.25 | 2024-02-14 | 17760 | -42.57 |
| 034230 | 파라다이스 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2024-01-29 | 12750 | 6.12 | 22.9 | 22.9 | -3.76 | -7.45 | -18.98 | 2024-04-09 | 15670 | -34.08 |
| 040300 | YTN | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage2-Actionable | 2024-02-05 | 5840 | 12.67 | 12.67 | 12.67 | -25.77 | -45.72 | -56.76 | 2024-02-07 | 6580 | -61.63 |
| 002780 | 진흥기업 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage2-Actionable | 2024-01-29 | 1046 | 9.85 | 9.85 | 9.85 | -5.64 | -9.27 | -24.0 | 2024-02-26 | 1149 | -30.81 |

## 8. Cross-Case Diagnosis

### 8.1 039130 / 하나투어 — positive control: high MAE blocks Green, not source-bridge Stage2

The entry row is 2024-01-29 at 60,900. The price reached 70,600 and later fell to 44,150. This row has a source bridge: demand-to-revenue, package margin and operating leverage. So high MAE should not erase the evidence, but it must cap the stage at guarded Yellow / 4B watch.

### 8.2 080160 / 모두투어 — travel theme high-MAE false positive

The entry row is 2024-01-29 at 17,070. The best forward high is only 17,760 and the 180D low is 10,200. There is no durable service-economics bridge. High MAE should override the reopening theme.

### 8.3 034230 / 파라다이스 — casino MFE without durable economics

The entry row is 2024-01-29 at 12,750. The MFE is real, but the 180D low later reaches 10,330. Without a durable VIP drop, hold-rate, margin or cashflow bridge, MFE remains 4B evidence only.

### 8.4 040300 / YTN — governance/event severe high-MAE false positive

The entry row is 2024-02-05 at 5,840. The event spike reaches 6,580, then falls to 2,525. This is a severe high-MAE case. Without incremental tender cash, cash-price floor or control-premium bridge, the event route must be demoted.

### 8.5 002780 / 진흥기업 — construction/PF high-MAE false positive

The entry row is 2024-01-29 at 1,046. The local high reaches only 1,149 and the 180D low reaches 795. Without orderbook, liquidity, balance repair or cashflow bridge, C30 should not survive Stage2/Yellow.

## 9. Stage2 / Yellow / Green / 4B Comparison

```text
Common R13 high-MAE rule:
  Stage2-Actionable = survives only when the source bridge exists
  Stage3-Yellow = allowed only as guarded Yellow when source bridge exists and MAE risk is explicit
  Stage3-Green = blocked whenever high-MAE/post-peak drawdown dominates
  4B = required when MFE precedes source-bridge confirmation or post-peak decay
  high-MAE guard = overrides MFE when source bridge is absent
```

Positive-control check:

```text
039130:
  Stage2 survives
  Yellow is allowed with 4B/high-MAE watch
  Green is rejected
```

False-positive check:

```text
080160 / 034230 / 040300 / 002780:
  Stage2 is demoted to Watch/4B/high-MAE guard
  Yellow is rejected
  Green is rejected
```

## 10. Current Calibrated Profile Stress Test

| question | R13 result |
|---|---|
| Is high-MAE always a hard delete? | No. 039130 survives because source bridge exists. |
| Does high-MAE block Green? | Yes, across all five rows. |
| Should MFE alone protect a row? | No. 034230 and 040300 show MFE can be a trap. |
| Should Stage2 bonus be globally reversed? | No. Make it conditional on source bridge. |
| Is local/full-window 4B still useful? | Yes. Every row routes through 4B/high-MAE watch. |
| Are cross-archetype rows new source evidence? | No. They are guardrail diagnostics only. |

## 11. Cross-Archetype Guardrail Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: cross_archetype_guardrail
rule_id: r13_high_mae_overrides_mfe_when_source_bridge_absent

rule:
  Across archetypes, if high-MAE or post-peak drawdown appears after MFE,
  the row cannot become Green. If the source bridge exists, keep it only as guarded
  Stage2/Yellow with 4B watch. If the source bridge is absent, demote it to
  Watch/4B/high-MAE guard and block Yellow/Green.

source_bridge_examples:
  C31 service/tourism -> demand-to-revenue, margin, cashflow, operating leverage
  C32 governance -> tender/cash price, control premium, capital-return or ownership resolution
  C30 construction/PF -> orderbook, balance repair, liquidity, PF-risk containment, cashflow
```

## 12. Before / After Backtest Comparison

| profile | eligible R13 cross rows | avg MFE90 | avg MAE90 | high-MAE false-positive risk | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 5 | 13.08 | -16.43 | high if MFE is over-read | good base, needs source-bridge high-MAE gate |
| P0b e2r_2_0_baseline_reference | 5 | 13.08 | -16.43 | medium | safer but can miss 039130 |
| P2 R13 high_MAE_source_bridge_gate_profile | 5 routed | 13.08 | -16.43 | 0% false positives after bridge gate | preferred shadow |
| P3 over_tight_high_MAE_profile | 1 positive-control risk | 15.93 | -8.87 | may incorrectly delete 039130 | rejected |

## 13. Score-Return Alignment Matrix

| case | source canonical | current profile verdict | R13 alignment |
|---|---|---|---|
| 039130 | C31 | current_profile_correct_but_no_green | Bridge-backed Stage2 survives; Green blocked |
| 080160 | C31 | current_profile_false_positive | High MAE overrides travel theme |
| 034230 | C31 | current_profile_false_positive_if_green | MFE exists but no margin/cashflow bridge |
| 040300 | C32 | current_profile_false_positive | Severe high MAE overrides privatization theme |
| 002780 | C30 | current_profile_false_positive | Construction/PF theme lacks liquidity/cashflow bridge |

## 14. Coverage Matrix

| large_sector_id | canonical_archetype_id | source archetypes | cross rows | positive controls | counterexamples | new independent | reused/cross | 4B watch | high-MAE | sector_rule | canonical_rule | coverage contribution |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | C31/C32/C30 | 5 | 1 | 4 | 0 | 5 | 5 | 5 | false | true | strengthens R13 high-MAE routing without adding source-archetype coverage |

## 15. Residual Contribution Summary

```text
r13_cross_case_count: 5
positive_control_count: 1
counterexample_count: 4
new_independent_case_count: 0
reused_case_count: 5
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
- high-MAE overrides MFE when source bridge is absent
- positive-control bridge survival with 4B watch
- tourism-theme high MAE
- governance-event high MAE
- construction/PF high MAE
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: r13_cross_archetype_high_mae_guardrail
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
shadow_weight,r13_high_mae_overrides_mfe_when_source_bridge_absent,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,0,1,+1,"Across C30/C31/C32 rows, high-MAE and post-peak drawdown should override MFE/theme evidence when the source-archetype bridge is absent","039130 survives only because source bridge exists; 080160, 034230, 040300, and 002780 are demoted because high-MAE arrived without margin/cashflow/tender/liquidity bridge","TRG_R13L74_HIGHMAE_C31_039130_20240129_SERVICE_DEMAND_BRIDGE_POSITIVE_CONTROL|TRG_R13L74_HIGHMAE_C31_080160_20240129_TOURISM_THEME_HIGH_MAE_FALSE_POSITIVE|TRG_R13L74_HIGHMAE_C31_034230_20240129_CASINO_TOURISM_MFE_WITHOUT_MARGIN_BRIDGE|TRG_R13L74_HIGHMAE_C32_040300_20240205_PRIVATIZATION_EVENT_HIGH_MAE_FALSE_POSITIVE|TRG_R13L74_HIGHMAE_C30_002780_20240129_SMALL_BUILDER_PF_HIGH_MAE_FALSE_POSITIVE",5,0,4,medium,cross_archetype_shadow_only,"R13 rows have do_not_count_as_new_case=true and independent_evidence_weight=0.0"
shadow_weight,r13_positive_control_high_mae_bridge_survival_guard,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,1,1,0,"High-MAE guard should block Green but not delete source-bridge-positive Stage2/Yellow rows","039130 prevents over-tightening: bridge-backed service demand row survives with 4B/high-MAE watch","TRG_R13L74_HIGHMAE_C31_039130_20240129_SERVICE_DEMAND_BRIDGE_POSITIVE_CONTROL",1,0,0,medium,existing_axis_kept,"keeps Stage2 bridge conditional rather than globally reversed"
```

## 18. Machine-Readable Rows

### 18.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_R13_cross_guardrail_diagnostics"}
```

### 18.2 case rows

```jsonl
{"row_type":"case","case_id":"R13L74_HIGHMAE_C31_039130_20240129_SERVICE_DEMAND_BRIDGE_POSITIVE_CONTROL","symbol":"039130","company_name":"하나투어","round":"R13","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_SERVICE_TOURISM_DEMAND_MARGIN_CASHFLOW_BRIDGE_GUARD","fine_archetype_id":"R13_HIGH_MAE_POSITIVE_CONTROL_BRIDGE_SURVIVES_WITH_4B_WATCH","deep_sub_archetype_id":"SERVICE_DEMAND_MARGIN_BRIDGE_WITH_POST_PEAK_HIGH_MAE","case_type":"r13_positive_control_bridge_survives_but_green_blocked","positive_or_counterexample":"positive_control","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 high-MAE cross-archetype guardrail; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates high-MAE routing and positive-control bridge survival; does not increase source archetype coverage."}
{"row_type":"case","case_id":"R13L74_HIGHMAE_C31_080160_20240129_TOURISM_THEME_HIGH_MAE_FALSE_POSITIVE","symbol":"080160","company_name":"모두투어","round":"R13","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_TRAVEL_AGENT_THEME_WITHOUT_MARGIN_CASHFLOW_BRIDGE","fine_archetype_id":"R13_HIGH_MAE_SERVICE_THEME_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"TRAVEL_REOPENING_THEME_LOW_MFE_HIGH_MAE_WITHOUT_SERVICE_ECONOMICS","case_type":"r13_high_mae_theme_false_positive","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 high-MAE cross-archetype guardrail; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates high-MAE routing and positive-control bridge survival; does not increase source archetype coverage."}
{"row_type":"case","case_id":"R13L74_HIGHMAE_C31_034230_20240129_CASINO_TOURISM_MFE_WITHOUT_MARGIN_BRIDGE","symbol":"034230","company_name":"파라다이스","round":"R13","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_CASINO_INBOUND_TOURISM_THEME_WITHOUT_DROP_MARGIN_BRIDGE","fine_archetype_id":"R13_HIGH_MAE_CASINO_THEME_WITHOUT_DROP_MARGIN_BRIDGE","deep_sub_archetype_id":"CASINO_INBOUND_MFE_WITHOUT_VIP_DROP_HOLD_RATE_MARGIN_CONVERSION","case_type":"r13_MFE_then_high_MAE_false_positive","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 high-MAE cross-archetype guardrail; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates high-MAE routing and positive-control bridge survival; does not increase source archetype coverage."}
{"row_type":"case","case_id":"R13L74_HIGHMAE_C32_040300_20240205_PRIVATIZATION_EVENT_HIGH_MAE_FALSE_POSITIVE","symbol":"040300","company_name":"YTN","round":"R13","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","source_fine_archetype_id":"C32_PRIVATIZATION_CONTROL_THEME_WITHOUT_INCREMENTAL_CASH_BRIDGE","fine_archetype_id":"R13_HIGH_MAE_GOVERNANCE_EVENT_WITHOUT_TENDER_CASH_BRIDGE","deep_sub_archetype_id":"PRIVATIZATION_EVENT_MFE_WITHOUT_CONTROL_PREMIUM_CASH_FLOOR","case_type":"r13_event_theme_high_MAE_false_positive","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 high-MAE cross-archetype guardrail; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates high-MAE routing and positive-control bridge survival; does not increase source archetype coverage."}
{"row_type":"case","case_id":"R13L74_HIGHMAE_C30_002780_20240129_SMALL_BUILDER_PF_HIGH_MAE_FALSE_POSITIVE","symbol":"002780","company_name":"진흥기업","round":"R13","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_fine_archetype_id":"C30_SMALL_BUILDER_PF_VALUE_REBOUND_WITHOUT_LIQUIDITY_BRIDGE","fine_archetype_id":"R13_HIGH_MAE_CONSTRUCTION_PF_THEME_WITHOUT_LIQUIDITY_BRIDGE","deep_sub_archetype_id":"SMALL_BUILDER_VALUE_REBOUND_WITHOUT_ORDER_BALANCE_LIQUIDITY_CASHFLOW_REPAIR","case_type":"r13_construction_theme_high_MAE_false_positive","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 high-MAE cross-archetype guardrail; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates high-MAE routing and positive-control bridge survival; does not increase source archetype coverage."}
```

### 18.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R13L74_HIGHMAE_C31_039130_20240129_SERVICE_DEMAND_BRIDGE_POSITIVE_CONTROL","case_id":"R13L74_HIGHMAE_C31_039130_20240129_SERVICE_DEMAND_BRIDGE_POSITIVE_CONTROL","symbol":"039130","company_name":"하나투어","round":"R13","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_SERVICE_TOURISM_DEMAND_MARGIN_CASHFLOW_BRIDGE_GUARD","fine_archetype_id":"R13_HIGH_MAE_POSITIVE_CONTROL_BRIDGE_SURVIVES_WITH_4B_WATCH","deep_sub_archetype_id":"SERVICE_DEMAND_MARGIN_BRIDGE_WITH_POST_PEAK_HIGH_MAE","loop_objective":"cross_archetype_redteam|high_MAE_guardrail|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|positive_control_bridge_survival","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":60900,"evidence_available_at_that_date":"source_proxy_outbound_travel_recovery_package_demand_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_outbound_travel_recovery_package_demand_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"source bridge exists: outbound package demand, revenue, margin and operating leverage; high-MAE/post-peak drawdown blocks Green but should not erase Stage2/Yellow evidence","stage2_evidence_fields":["service_demand_recovery","package_demand_proxy","relative_strength"],"stage3_evidence_fields":["demand_to_revenue_visibility","package_mix_margin_bridge","operating_leverage_proxy"],"stage4b_evidence_fields":["post_peak_high_MAE_watch","drawdown_after_recovery_peak"],"stage4c_evidence_fields":["drawdown_watch_after_recovery_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039130/2024.csv","profile_path":"atlas/symbol_profiles/039/039130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.97,"MFE_90D_pct":15.93,"MFE_180D_pct":15.93,"MFE_1Y_pct":15.93,"MFE_2Y_pct":15.93,"MAE_30D_pct":-3.28,"MAE_90D_pct":-8.87,"MAE_180D_pct":-27.5,"MAE_1Y_pct":-27.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":70600,"drawdown_after_peak_pct":-37.46,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_control_survives_because_source_bridge_exists_but_green_blocked_by_MAE","four_b_evidence_type":"source_bridge_positive_control_with_high_MAE","four_c_protection_label":"drawdown_watch","trigger_outcome_label":"bridge_backed_stage2_survives_with_4B_high_MAE_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L74_HIGHMAE_C31_039130_20240129_SERVICE_DEMAND_BRIDGE_POSITIVE_CONTROL_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 high-MAE cross-archetype guardrail; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L74_HIGHMAE_C31_080160_20240129_TOURISM_THEME_HIGH_MAE_FALSE_POSITIVE","case_id":"R13L74_HIGHMAE_C31_080160_20240129_TOURISM_THEME_HIGH_MAE_FALSE_POSITIVE","symbol":"080160","company_name":"모두투어","round":"R13","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_TRAVEL_AGENT_THEME_WITHOUT_MARGIN_CASHFLOW_BRIDGE","fine_archetype_id":"R13_HIGH_MAE_SERVICE_THEME_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"TRAVEL_REOPENING_THEME_LOW_MFE_HIGH_MAE_WITHOUT_SERVICE_ECONOMICS","loop_objective":"cross_archetype_redteam|high_MAE_guardrail|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|positive_control_bridge_survival","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":17070,"evidence_available_at_that_date":"source_proxy_outbound_travel_agent_theme_without_package_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_outbound_travel_agent_theme_without_package_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"travel reopening theme lacked package-margin, cashflow and operating-leverage bridge; high-MAE confirms Stage2 false positive","stage2_evidence_fields":["tourism_reopening_theme","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_service_economics_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/080/080160/2024.csv","profile_path":"atlas/symbol_profiles/080/080160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.04,"MFE_90D_pct":4.04,"MFE_180D_pct":4.04,"MFE_1Y_pct":4.04,"MFE_2Y_pct":4.04,"MAE_30D_pct":-10.84,"MAE_90D_pct":-10.84,"MAE_180D_pct":-40.25,"MAE_1Y_pct":-40.25,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-14","peak_price":17760,"drawdown_after_peak_pct":-42.57,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"theme_local_peak_and_high_MAE_rejected_as_positive_stage","four_b_evidence_type":"theme_or_event_without_bridge_high_MAE","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"stage2_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L74_HIGHMAE_C31_080160_20240129_TOURISM_THEME_HIGH_MAE_FALSE_POSITIVE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 high-MAE cross-archetype guardrail; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L74_HIGHMAE_C31_034230_20240129_CASINO_TOURISM_MFE_WITHOUT_MARGIN_BRIDGE","case_id":"R13L74_HIGHMAE_C31_034230_20240129_CASINO_TOURISM_MFE_WITHOUT_MARGIN_BRIDGE","symbol":"034230","company_name":"파라다이스","round":"R13","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_CASINO_INBOUND_TOURISM_THEME_WITHOUT_DROP_MARGIN_BRIDGE","fine_archetype_id":"R13_HIGH_MAE_CASINO_THEME_WITHOUT_DROP_MARGIN_BRIDGE","deep_sub_archetype_id":"CASINO_INBOUND_MFE_WITHOUT_VIP_DROP_HOLD_RATE_MARGIN_CONVERSION","loop_objective":"cross_archetype_redteam|high_MAE_guardrail|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|positive_control_bridge_survival","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":12750,"evidence_available_at_that_date":"source_proxy_casino_inbound_tourism_theme_without_VIP_drop_hold_rate_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_casino_inbound_tourism_theme_without_VIP_drop_hold_rate_margin_bridge; evidence_url_pending","bridge_summary":"casino/inbound MFE lacked durable VIP drop, hold-rate, margin and cashflow bridge; high-MAE watch blocks Green","stage2_evidence_fields":["casino_inbound_tourism_theme","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_MFE_peak","drop_hold_rate_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_drop_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034230/2024.csv","profile_path":"atlas/symbol_profiles/034/034230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.12,"MFE_90D_pct":22.9,"MFE_180D_pct":22.9,"MFE_1Y_pct":22.9,"MFE_2Y_pct":22.9,"MAE_30D_pct":-3.76,"MAE_90D_pct":-7.45,"MAE_180D_pct":-18.98,"MAE_1Y_pct":-18.98,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-09","peak_price":15670,"drawdown_after_peak_pct":-34.08,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"MFE_exists_but_source_bridge_absent_keep_4B_high_MAE_watch","four_b_evidence_type":"theme_or_event_without_bridge_high_MAE","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L74_HIGHMAE_C31_034230_20240129_CASINO_TOURISM_MFE_WITHOUT_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 high-MAE cross-archetype guardrail; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L74_HIGHMAE_C32_040300_20240205_PRIVATIZATION_EVENT_HIGH_MAE_FALSE_POSITIVE","case_id":"R13L74_HIGHMAE_C32_040300_20240205_PRIVATIZATION_EVENT_HIGH_MAE_FALSE_POSITIVE","symbol":"040300","company_name":"YTN","round":"R13","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","source_fine_archetype_id":"C32_PRIVATIZATION_CONTROL_THEME_WITHOUT_INCREMENTAL_CASH_BRIDGE","fine_archetype_id":"R13_HIGH_MAE_GOVERNANCE_EVENT_WITHOUT_TENDER_CASH_BRIDGE","deep_sub_archetype_id":"PRIVATIZATION_EVENT_MFE_WITHOUT_CONTROL_PREMIUM_CASH_FLOOR","loop_objective":"cross_archetype_redteam|high_MAE_guardrail|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|positive_control_bridge_survival","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":5840,"evidence_available_at_that_date":"source_proxy_media_privatization_control_theme_without_incremental_tender_cash_price_or_earnings_bridge; evidence_url_pending","evidence_source":"source_proxy_media_privatization_control_theme_without_incremental_tender_cash_price_or_earnings_bridge; evidence_url_pending","bridge_summary":"privatization event lacked incremental tender/cash-price, control-premium floor or earnings bridge; severe high-MAE confirms guard","stage2_evidence_fields":["privatization_control_theme","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["event_local_peak","tender_cash_bridge_absent"],"stage4c_evidence_fields":["severe_high_MAE_without_cash_floor"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/040/040300/2024.csv","profile_path":"atlas/symbol_profiles/040/040300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.67,"MFE_90D_pct":12.67,"MFE_180D_pct":12.67,"MFE_1Y_pct":12.67,"MFE_2Y_pct":12.67,"MAE_30D_pct":-25.77,"MAE_90D_pct":-45.72,"MAE_180D_pct":-56.76,"MAE_1Y_pct":-56.76,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-07","peak_price":6580,"drawdown_after_peak_pct":-61.63,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"event_local_peak_and_severe_MAE_rejected_as_positive_stage","four_b_evidence_type":"theme_or_event_without_bridge_high_MAE","four_c_protection_label":"severe_high_MAE_watch","trigger_outcome_label":"stage2_false_positive_severe_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L74_HIGHMAE_C32_040300_20240205_PRIVATIZATION_EVENT_HIGH_MAE_FALSE_POSITIVE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 high-MAE cross-archetype guardrail; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L74_HIGHMAE_C30_002780_20240129_SMALL_BUILDER_PF_HIGH_MAE_FALSE_POSITIVE","case_id":"R13L74_HIGHMAE_C30_002780_20240129_SMALL_BUILDER_PF_HIGH_MAE_FALSE_POSITIVE","symbol":"002780","company_name":"진흥기업","round":"R13","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_fine_archetype_id":"C30_SMALL_BUILDER_PF_VALUE_REBOUND_WITHOUT_LIQUIDITY_BRIDGE","fine_archetype_id":"R13_HIGH_MAE_CONSTRUCTION_PF_THEME_WITHOUT_LIQUIDITY_BRIDGE","deep_sub_archetype_id":"SMALL_BUILDER_VALUE_REBOUND_WITHOUT_ORDER_BALANCE_LIQUIDITY_CASHFLOW_REPAIR","loop_objective":"cross_archetype_redteam|high_MAE_guardrail|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|positive_control_bridge_survival","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":1046,"evidence_available_at_that_date":"source_proxy_small_builder_PF_value_rebound_without_order_balance_liquidity_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_small_builder_PF_value_rebound_without_order_balance_liquidity_cashflow_bridge; evidence_url_pending","bridge_summary":"small-builder value rebound lacked orderbook, balance repair, PF-risk containment, liquidity and cashflow bridge; high-MAE validates demotion","stage2_evidence_fields":["small_builder_value_rebound","PF_relief_expectation"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","liquidity_bridge_absent","cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_order_balance_or_liquidity_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv","profile_path":"atlas/symbol_profiles/002/002780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.85,"MFE_90D_pct":9.85,"MFE_180D_pct":9.85,"MFE_1Y_pct":9.85,"MFE_2Y_pct":9.85,"MAE_30D_pct":-5.64,"MAE_90D_pct":-9.27,"MAE_180D_pct":-24.0,"MAE_1Y_pct":-24.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-26","peak_price":1149,"drawdown_after_peak_pct":-30.81,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"construction_theme_local_4B_rejected_as_positive_stage","four_b_evidence_type":"theme_or_event_without_bridge_high_MAE","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"stage2_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L74_HIGHMAE_C30_002780_20240129_SMALL_BUILDER_PF_HIGH_MAE_FALSE_POSITIVE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 high-MAE cross-archetype guardrail; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 18.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L74_HIGHMAE_C31_039130_20240129_SERVICE_DEMAND_BRIDGE_POSITIVE_CONTROL","trigger_id":"TRG_R13L74_HIGHMAE_C31_039130_20240129_SERVICE_DEMAND_BRIDGE_POSITIVE_CONTROL","symbol":"039130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"source_bridge_score":14,"theme_event_score":8,"MFE_score":10,"MAE_penalty":7,"local_4b_score":7},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":15,"theme_event_score":6,"MFE_score":7,"MAE_penalty":12,"local_4b_score":12},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow_with_4B_HighMAE_Watch","changed_components":["source_bridge_score","theme_event_score","MFE_score","MAE_penalty","local_4b_score"],"component_delta_explanation":"R13 positive-control: bridge-backed Stage2 survives, but high-MAE/post-peak drawdown blocks Green and forces 4B watch.","MFE_90D_pct":15.93,"MAE_90D_pct":-8.87,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L74_HIGHMAE_C31_080160_20240129_TOURISM_THEME_HIGH_MAE_FALSE_POSITIVE","trigger_id":"TRG_R13L74_HIGHMAE_C31_080160_20240129_TOURISM_THEME_HIGH_MAE_FALSE_POSITIVE","symbol":"080160","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"source_bridge_score":1,"theme_event_score":12,"MFE_score":8,"MAE_penalty":7,"local_4b_score":5},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":0,"theme_event_score":4,"MFE_score":3,"MAE_penalty":16,"local_4b_score":12},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["source_bridge_score","theme_event_score","MFE_score","MAE_penalty","local_4b_score"],"component_delta_explanation":"R13 guard: when source bridge is absent, MFE/theme evidence is overridden by high-MAE and 4B protection.","MFE_90D_pct":4.04,"MAE_90D_pct":-10.84,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L74_HIGHMAE_C31_034230_20240129_CASINO_TOURISM_MFE_WITHOUT_MARGIN_BRIDGE","trigger_id":"TRG_R13L74_HIGHMAE_C31_034230_20240129_CASINO_TOURISM_MFE_WITHOUT_MARGIN_BRIDGE","symbol":"034230","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"source_bridge_score":1,"theme_event_score":12,"MFE_score":8,"MAE_penalty":7,"local_4b_score":5},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":0,"theme_event_score":4,"MFE_score":3,"MAE_penalty":16,"local_4b_score":12},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["source_bridge_score","theme_event_score","MFE_score","MAE_penalty","local_4b_score"],"component_delta_explanation":"R13 guard: when source bridge is absent, MFE/theme evidence is overridden by high-MAE and 4B protection.","MFE_90D_pct":22.9,"MAE_90D_pct":-7.45,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L74_HIGHMAE_C32_040300_20240205_PRIVATIZATION_EVENT_HIGH_MAE_FALSE_POSITIVE","trigger_id":"TRG_R13L74_HIGHMAE_C32_040300_20240205_PRIVATIZATION_EVENT_HIGH_MAE_FALSE_POSITIVE","symbol":"040300","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"source_bridge_score":1,"theme_event_score":12,"MFE_score":8,"MAE_penalty":7,"local_4b_score":5},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":0,"theme_event_score":4,"MFE_score":3,"MAE_penalty":16,"local_4b_score":12},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["source_bridge_score","theme_event_score","MFE_score","MAE_penalty","local_4b_score"],"component_delta_explanation":"R13 guard: when source bridge is absent, MFE/theme evidence is overridden by high-MAE and 4B protection.","MFE_90D_pct":12.67,"MAE_90D_pct":-45.72,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L74_HIGHMAE_C30_002780_20240129_SMALL_BUILDER_PF_HIGH_MAE_FALSE_POSITIVE","trigger_id":"TRG_R13L74_HIGHMAE_C30_002780_20240129_SMALL_BUILDER_PF_HIGH_MAE_FALSE_POSITIVE","symbol":"002780","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"source_bridge_score":1,"theme_event_score":12,"MFE_score":8,"MAE_penalty":7,"local_4b_score":5},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"source_bridge_score":0,"theme_event_score":4,"MFE_score":3,"MAE_penalty":16,"local_4b_score":12},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["source_bridge_score","theme_event_score","MFE_score","MAE_penalty","local_4b_score"],"component_delta_explanation":"R13 guard: when source bridge is absent, MFE/theme evidence is overridden by high-MAE and 4B protection.","MFE_90D_pct":9.85,"MAE_90D_pct":-9.27,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 18.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,r13_high_mae_overrides_mfe_when_source_bridge_absent,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,0,1,+1,"Across C30/C31/C32 rows, high-MAE and post-peak drawdown should override MFE/theme evidence when the source-archetype bridge is absent","039130 survives only because source bridge exists; 080160, 034230, 040300, and 002780 are demoted because high-MAE arrived without margin/cashflow/tender/liquidity bridge","TRG_R13L74_HIGHMAE_C31_039130_20240129_SERVICE_DEMAND_BRIDGE_POSITIVE_CONTROL|TRG_R13L74_HIGHMAE_C31_080160_20240129_TOURISM_THEME_HIGH_MAE_FALSE_POSITIVE|TRG_R13L74_HIGHMAE_C31_034230_20240129_CASINO_TOURISM_MFE_WITHOUT_MARGIN_BRIDGE|TRG_R13L74_HIGHMAE_C32_040300_20240205_PRIVATIZATION_EVENT_HIGH_MAE_FALSE_POSITIVE|TRG_R13L74_HIGHMAE_C30_002780_20240129_SMALL_BUILDER_PF_HIGH_MAE_FALSE_POSITIVE",5,0,4,medium,cross_archetype_shadow_only,"R13 rows have do_not_count_as_new_case=true and independent_evidence_weight=0.0"
shadow_weight,r13_positive_control_high_mae_bridge_survival_guard,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,1,1,0,"High-MAE guard should block Green but not delete source-bridge-positive Stage2/Yellow rows","039130 prevents over-tightening: bridge-backed service demand row survives with 4B/high-MAE watch","TRG_R13L74_HIGHMAE_C31_039130_20240129_SERVICE_DEMAND_BRIDGE_POSITIVE_CONTROL",1,0,0,medium,existing_axis_kept,"keeps Stage2 bridge conditional rather than globally reversed"
```

### 18.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","r13_cross_case_count":5,"new_independent_case_count":0,"reused_case_count":5,"positive_control_count":1,"counterexample_count":4,"new_symbol_count_for_source_archetype":0,"new_trigger_family_count_for_source_archetype":0,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["high_MAE_overrides_MFE_when_source_bridge_absent","positive_control_bridge_survival_with_4B_watch","tourism_theme_high_MAE","governance_event_high_MAE","construction_PF_high_MAE"],"loop_contribution_label":"r13_cross_archetype_high_mae_guardrail","do_not_propose_new_weight_delta":false}
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
- `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` rows should update cross_archetype_shadow_profile only.

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
- Stage2 bonus should be conditional on a source-archetype bridge rather than globally removed.
- High-MAE should block Green across all source archetypes.
- High-MAE should demote MFE/theme rows when source bridge is absent.
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
11. Add tests that high-MAE blocks Green but does not delete bridge-backed Stage2/Yellow rows.
12. Add tests that MFE/theme rows are demoted when source bridge is absent and MAE is high.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- R13 high-MAE guardrail coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 20. Next Round State

```text
completed_round = R13
completed_loop = 74
next_round = R1
next_loop = 75
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
atlas/symbol_profiles/039/039130.json
atlas/symbol_profiles/080/080160.json
atlas/symbol_profiles/034/034230.json
atlas/symbol_profiles/040/040300.json
atlas/symbol_profiles/002/002780.json
atlas/ohlcv_tradable_by_symbol_year/039/039130/2024.csv
atlas/ohlcv_tradable_by_symbol_year/080/080160/2024.csv
atlas/ohlcv_tradable_by_symbol_year/034/034230/2024.csv
atlas/ohlcv_tradable_by_symbol_year/040/040300/2024.csv
atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv
```

This loop completes R13 / loop 74 and moves the scheduler to R1 / loop 75.
