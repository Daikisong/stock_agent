# E2R Stock-Web Historical Calibration / R13 Cross-Archetype Stage2 False-Positive Review

## 0. Research Metadata

```text
scheduled_round: R13
scheduled_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R1
computed_next_loop: 74
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: R13_STAGE2_SOURCE_BRIDGE_SURVIVAL_AND_FALSE_POSITIVE_GUARD
loop_objective: cross_archetype_redteam | residual_false_positive_mining | stage2_actionable_bonus_stress_test | high_MAE_guardrail | 4B_non_price_requirement_stress_test
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

R13 is not a normal sector expansion round. It is a cross-archetype checkpoint. This file therefore uses `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` and one of the allowed R13 scopes:

```text
canonical_archetype_id = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```

Every representative row is marked:

```text
r13_cross_case = true
do_not_count_as_new_case = true
independent_evidence_weight = 0.0
aggregate_group_role = r13_cross_check
```

This run tests a different R13 axis from the previous 4B/4C red-team:

```text
Can Stage2-Actionable be kept for real bridge-backed signals while demoting policy/theme/construction rows that only have event heat and later high MAE?
```

The answer from this R13 set is yes. The guardrail should not reverse the global Stage2 bonus. It should make the bonus conditional on a source-archetype bridge.

## 3. Cross-Archetype Source Map

| source large sector | source canonical | symbol | company | outcome | 4B verdict | 4C/watch label |
|---|---|---:|---|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 015760 | 한국전력 | stage2_true_positive_control_with_4B_watch | positive_control_survives_stage2_review_but_routes_to_4B_drawdown_watch | policy_delay_drawdown_watch |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 013990 | 아가방컴퍼니 | stage2_false_positive_policy_theme_high_MAE | policy_theme_local_4B_rejected_as_positive_stage | high_MAE_watch |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 339950 | 아이비김영 | stage2_false_positive_education_policy_high_MAE | education_policy_theme_local_4B_rejected_as_positive_stage | high_MAE_watch |
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 001470 | 삼부토건 | stage2_false_positive_construction_theme_high_MAE | construction_theme_local_4B_rejected_as_positive_stage_and_high_MAE_guard | high_MAE_thesis_break_watch |

## 4. No-Repeat / Duplicate Handling

No-Repeat hard duplicate key remains:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

For R13, these rows are cross-check rows, not new source-archetype rows.

```text
r13_cross_case_count = 4
positive_control_count = 1
counterexample_count = 3
new_independent_case_count = 0
reused_case_count = 4
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
015760 has no corporate-action candidate dates.
013990 has a 2008-05-16 corporate-action candidate date, outside the selected 2024 window.
339950 has a 2020-10-13 corporate-action candidate date, outside the selected 2024 window.
001470 has corporate-action candidate dates ending 2019, outside the selected 2024 representative window.
All four representative windows are treated as clean for R13 guardrail diagnostics.
```

## 7. Trigger-Level OHLC Backtest Table

| symbol | company | source canonical | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 015760 | 한국전력 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2024-01-29 | 19920 | 27.76 | 27.76 | 27.76 | -3.92 | -4.57 | -8.68 | 2024-03-14 | 25450 | -28.53 |
| 013990 | 아가방컴퍼니 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2024-01-03 | 5630 | 27.53 | 27.53 | 27.53 | -9.95 | -17.5 | -39.61 | 2024-01-18 | 7180 | -52.65 |
| 339950 | 아이비김영 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2024-02-20 | 2300 | 28.91 | 28.91 | 28.91 | -18.52 | -26.09 | -35.65 | 2024-02-26 | 2965 | -50.08 |
| 001470 | 삼부토건 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage2-Actionable | 2024-01-29 | 2020 | 37.62 | 41.83 | 41.83 | -7.82 | -25.25 | -78.22 | 2024-03-15 | 2865 | -84.64 |

## 8. Cross-Case Diagnosis

### 8.1 015760 / 한국전력 — positive control: Stage2 survives when policy becomes cashflow

The entry row is 2024-01-29 at 19,920. The path reaches 25,450, but later gives back the move. This is a policy event that should survive Stage2 review because the signal is not just a headline. The bridge is tariff/cost-pass-through and utility cashflow repair. The proper route is Stage3-Yellow with 4B/drawdown watch, not Green.

### 8.2 013990 / 아가방컴퍼니 — policy-theme MFE is not demand

The entry row is 2024-01-03 at 5,630. The move reaches 7,180, but then falls to 3,400. Low-birth policy language can lift childcare-related names, but without demand, margin, inventory, and cashflow conversion, the price spike is a campaign poster, not an earnings bridge.

### 8.3 339950 / 아이비김영 — education policy MFE is not enrollment revenue

The entry row is 2024-02-20 at 2,300. The path reaches 2,965 and then falls to 1,480. This is the education-service version of the same false positive: policy optionality exists, but Stage2 should not climb without enrollment, revenue, margin, or service-demand conversion.

### 8.4 001470 / 삼부토건 — construction/PF theme MFE is not balance repair

The entry row is 2024-01-29 at 2,020. The path reaches 2,865, then falls to 440. Construction/PF theme heat cannot substitute for balance repair, trust quality, liquidity, or cashflow. This row should route to 4B/high-MAE and thesis-break watch.

## 9. Stage2 / Yellow / Green / 4B Comparison

```text
Common R13 Stage2 rule:
  Stage2-Actionable = survives only if the source-archetype bridge exists
  Stage3-Yellow = allowed only after non-price economics bridge
  Stage3-Green = reject if MFE is event/theme-led and bridge is absent
  4B = local/full-window price peak overlay when source bridge is weak
  high-MAE guard = active when post-peak low confirms false positive
```

Positive-control check:

```text
015760:
  Stage2 survives
  Yellow is allowed with 4B/drawdown watch
  Green is rejected
```

False-positive check:

```text
013990 / 339950 / 001470:
  Stage2 is demoted to Watch/4B guard
  Yellow is rejected
  Green is rejected
```

## 10. Current Calibrated Profile Stress Test

| question | R13 result |
|---|---|
| Stage2 actionable bonus too strong? | Too strong only when event/theme evidence lacks source bridge. |
| Should Stage2 bonus be globally reversed? | No. 015760 shows bridge-backed Stage2 should survive. |
| Stage3 Yellow threshold too loose? | Not globally; source-bridge gate should intercept before Yellow. |
| Stage3 Green too strict? | Correct. This run reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, but it needs source-bridge context. |
| Full 4B non-price requirement appropriate? | Yes. MFE alone is not positive evidence. |
| High-MAE guard appropriate? | Yes. 013990, 339950, and 001470 all require high-MAE guard. |

## 11. Cross-Archetype Guardrail Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: cross_archetype_guardrail
rule_id: r13_stage2_requires_source_bridge_not_theme_only

rule:
  Stage2-Actionable may remain valid when the source-archetype bridge exists.
  If the evidence is mostly policy/theme/event/price strength and the source bridge is absent,
  demote to Watch/4B/high-MAE guard and block Yellow/Green promotion.

source_bridge_examples:
  C31 -> policy-to-economics: cashflow, cost recovery, demand, enrollment, margin, revenue
  C30 -> construction/PF economics: balance repair, trust quality, liquidity, cashflow, PF-credit containment
```

## 12. Before / After Backtest Comparison

| profile | eligible R13 cross rows | avg MFE90 | avg MAE90 | Stage2 false-positive risk | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 31.51 | -18.35 | high if theme MFE is over-read | good base, needs source-bridge gate |
| P0b e2r_2_0_baseline_reference | 4 | 31.51 | -18.35 | medium | safer but can miss 015760 |
| P2 R13 source_bridge_gate_profile | 4 routed | 31.51 | -18.35 | 0% false positives after bridge gate | preferred shadow |
| P3 over_tight_guard_profile | 1 positive-control risk | 27.76 | -4.57 | may incorrectly delete 015760 | rejected |

## 13. Score-Return Alignment Matrix

| case | source canonical | current profile verdict | R13 alignment |
|---|---|---|---|
| 015760 | C31 | current_profile_correct_but_no_green | Stage2 survives because policy-to-cashflow bridge exists |
| 013990 | C31 | current_profile_false_positive_if_green | MFE does not survive without demand/margin bridge |
| 339950 | C31 | current_profile_false_positive_if_green | MFE does not survive without enrollment/revenue bridge |
| 001470 | C30 | current_profile_false_positive_without_balance_trust_guard | construction/PF theme routes to high-MAE guard |

## 14. Coverage Matrix

| large_sector_id | canonical_archetype_id | source archetypes | cross rows | positive controls | counterexamples | new independent | reused/cross | 4B watch | high-MAE | sector_rule | canonical_rule | coverage contribution |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | C31/C30 | 4 | 1 | 3 | 0 | 4 | 4 | 3 | false | true | strengthens R13 Stage2 false-positive routing without adding source-archetype coverage |

## 15. Residual Contribution Summary

```text
r13_cross_case_count: 4
positive_control_count: 1
counterexample_count: 3
new_independent_case_count: 0
reused_case_count: 4
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
- Stage2 theme false positive without source bridge
- positive-control bridge survival
- policy-theme high-MAE
- construction-theme high-MAE
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: r13_cross_archetype_stage2_false_positive_review
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
shadow_weight,r13_stage2_requires_source_bridge_not_theme_only,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW,0,1,+1,"Across C31 and C30 rows, Stage2 should survive only when the source-archetype economic bridge exists; theme/event/price evidence alone should remain Watch/4B/high-MAE guard","015760 survives as positive control because policy-to-cashflow bridge exists; 013990, 339950, and 001470 are demoted because policy/construction themes lacked demand, revenue, balance, or cashflow bridge","TRG_R13L73_STAGE2FP_C31_015760_20240129_POLICY_TO_CASHFLOW_POSITIVE_CONTROL|TRG_R13L73_STAGE2FP_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_FALSE_POSITIVE|TRG_R13L73_STAGE2FP_C31_339950_20240220_EDUCATION_POLICY_THEME_FALSE_POSITIVE|TRG_R13L73_STAGE2FP_C30_001470_20240129_CONSTRUCTION_THEME_FALSE_POSITIVE",4,0,3,medium,cross_archetype_shadow_only,"R13 rows have do_not_count_as_new_case=true and independent_evidence_weight=0.0"
shadow_weight,r13_positive_control_bridge_survival_guard,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW,1,1,0,"The false-positive guard must not erase real Stage2 rows when non-price economics bridge exists","015760 prevents over-tightening: the policy row survives, but Green is blocked by local 4B/drawdown watch","TRG_R13L73_STAGE2FP_C31_015760_20240129_POLICY_TO_CASHFLOW_POSITIVE_CONTROL",1,0,0,medium,existing_axis_kept,"keeps stage2_actionable_evidence_bonus conditional rather than globally reversed"
```

## 18. Machine-Readable Rows

### 18.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_R13_cross_guardrail_diagnostics"}
```

### 18.2 case rows

```jsonl
{"row_type":"case","case_id":"R13L73_STAGE2FP_C31_015760_20240129_POLICY_TO_CASHFLOW_POSITIVE_CONTROL","symbol":"015760","company_name":"한국전력","round":"R13","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_UTILITY_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE","fine_archetype_id":"R13_STAGE2_POSITIVE_CONTROL_POLICY_TO_ECONOMICS_BRIDGE","deep_sub_archetype_id":"UTILITY_TARIFF_POLICY_WITH_COST_RECOVERY_CASHFLOW_BRIDGE","case_type":"r13_positive_control_stage2_survives_when_bridge_exists","positive_or_counterexample":"positive_control","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 cross-archetype Stage2 false-positive review; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates Stage2 false-positive routing and positive-control survival; does not increase source archetype coverage."}
{"row_type":"case","case_id":"R13L73_STAGE2FP_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_FALSE_POSITIVE","symbol":"013990","company_name":"아가방컴퍼니","round":"R13","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_LOW_BIRTH_POLICY_CONSUMER_THEME_WITHOUT_DEMAND_MARGIN_BRIDGE","fine_archetype_id":"R13_STAGE2_POLICY_THEME_WITHOUT_ECONOMIC_BRIDGE","deep_sub_archetype_id":"LOW_BIRTH_POLICY_THEME_MFE_WITHOUT_DEMAND_MARGIN_CASHFLOW","case_type":"r13_policy_theme_false_positive_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 cross-archetype Stage2 false-positive review; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates Stage2 false-positive routing and positive-control survival; does not increase source archetype coverage."}
{"row_type":"case","case_id":"R13L73_STAGE2FP_C31_339950_20240220_EDUCATION_POLICY_THEME_FALSE_POSITIVE","symbol":"339950","company_name":"아이비김영","round":"R13","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_EDUCATION_POLICY_THEME_WITHOUT_ENROLLMENT_REVENUE_BRIDGE","fine_archetype_id":"R13_STAGE2_EDUCATION_POLICY_THEME_WITHOUT_REVENUE_BRIDGE","deep_sub_archetype_id":"EDUCATION_POLICY_MFE_WITHOUT_ENROLLMENT_REVENUE_MARGIN_CONVERSION","case_type":"r13_policy_theme_false_positive_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 cross-archetype Stage2 false-positive review; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates Stage2 false-positive routing and positive-control survival; does not increase source archetype coverage."}
{"row_type":"case","case_id":"R13L73_STAGE2FP_C30_001470_20240129_CONSTRUCTION_THEME_FALSE_POSITIVE","symbol":"001470","company_name":"삼부토건","round":"R13","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_fine_archetype_id":"C30_CONSTRUCTION_THEME_WITHOUT_BALANCE_TRUST_CASHFLOW_BRIDGE","fine_archetype_id":"R13_STAGE2_CONSTRUCTION_PF_THEME_WITHOUT_BALANCE_TRUST_BRIDGE","deep_sub_archetype_id":"CONSTRUCTION_PF_THEME_MFE_WITHOUT_BALANCE_LIQUIDITY_CASHFLOW_TRUST_REPAIR","case_type":"r13_construction_theme_false_positive_high_MAE_thesis_break_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 cross-archetype Stage2 false-positive review; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive_without_balance_trust_guard","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates Stage2 false-positive routing and positive-control survival; does not increase source archetype coverage."}
```

### 18.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R13L73_STAGE2FP_C31_015760_20240129_POLICY_TO_CASHFLOW_POSITIVE_CONTROL","case_id":"R13L73_STAGE2FP_C31_015760_20240129_POLICY_TO_CASHFLOW_POSITIVE_CONTROL","symbol":"015760","company_name":"한국전력","round":"R13","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_UTILITY_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE","fine_archetype_id":"R13_STAGE2_POSITIVE_CONTROL_POLICY_TO_ECONOMICS_BRIDGE","deep_sub_archetype_id":"UTILITY_TARIFF_POLICY_WITH_COST_RECOVERY_CASHFLOW_BRIDGE","loop_objective":"cross_archetype_redteam|residual_false_positive_mining|stage2_actionable_bonus_stress_test|high_MAE_guardrail|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":19920,"evidence_available_at_that_date":"source_proxy_utility_tariff_cost_pass_through_cashflow_repair_policy_bridge; evidence_url_pending","evidence_source":"source_proxy_utility_tariff_cost_pass_through_cashflow_repair_policy_bridge; evidence_url_pending","bridge_summary":"policy event survives Stage2 false-positive review because tariff/cost recovery translated into a cashflow repair bridge","stage2_evidence_fields":["policy_event","cost_pass_through","cashflow_repair_proxy","relative_strength"],"stage3_evidence_fields":["policy_to_cashflow_bridge","cost_recovery_visibility","balance_sheet_repair_proxy"],"stage4b_evidence_fields":["policy_peak_drawdown_watch","policy_delay_risk"],"stage4c_evidence_fields":["drawdown_watch_after_policy_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv","profile_path":"atlas/symbol_profiles/015/015760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.76,"MFE_90D_pct":27.76,"MFE_180D_pct":27.76,"MFE_1Y_pct":27.76,"MFE_2Y_pct":27.76,"MAE_30D_pct":-3.92,"MAE_90D_pct":-4.57,"MAE_180D_pct":-8.68,"MAE_1Y_pct":-8.68,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-14","peak_price":25450,"drawdown_after_peak_pct":-28.53,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_control_survives_stage2_review_but_routes_to_4B_drawdown_watch","four_b_evidence_type":"positive_control_non_price_bridge","four_c_protection_label":"policy_delay_drawdown_watch","trigger_outcome_label":"stage2_true_positive_control_with_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L73_STAGE2FP_C31_015760_20240129_POLICY_TO_CASHFLOW_POSITIVE_CONTROL_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype Stage2 false-positive review; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L73_STAGE2FP_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_FALSE_POSITIVE","case_id":"R13L73_STAGE2FP_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_FALSE_POSITIVE","symbol":"013990","company_name":"아가방컴퍼니","round":"R13","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_LOW_BIRTH_POLICY_CONSUMER_THEME_WITHOUT_DEMAND_MARGIN_BRIDGE","fine_archetype_id":"R13_STAGE2_POLICY_THEME_WITHOUT_ECONOMIC_BRIDGE","deep_sub_archetype_id":"LOW_BIRTH_POLICY_THEME_MFE_WITHOUT_DEMAND_MARGIN_CASHFLOW","loop_objective":"cross_archetype_redteam|residual_false_positive_mining|stage2_actionable_bonus_stress_test|high_MAE_guardrail|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-03","entry_date":"2024-01-03","entry_price":5630,"evidence_available_at_that_date":"source_proxy_low_birth_policy_childcare_theme_without_demand_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_low_birth_policy_childcare_theme_without_demand_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"low-birth policy theme created MFE but had no durable demand, margin, inventory, or cashflow bridge","stage2_evidence_fields":["policy_theme","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["policy_theme_local_peak","demand_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_policy_to_demand_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv","profile_path":"atlas/symbol_profiles/013/013990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.53,"MFE_90D_pct":27.53,"MFE_180D_pct":27.53,"MFE_1Y_pct":27.53,"MFE_2Y_pct":27.53,"MAE_30D_pct":-9.95,"MAE_90D_pct":-17.5,"MAE_180D_pct":-39.61,"MAE_1Y_pct":-39.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-18","peak_price":7180,"drawdown_after_peak_pct":-52.65,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"policy_theme_local_4B_rejected_as_positive_stage","four_b_evidence_type":"theme_or_price_without_source_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"stage2_false_positive_policy_theme_high_MAE","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L73_STAGE2FP_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_FALSE_POSITIVE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype Stage2 false-positive review; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L73_STAGE2FP_C31_339950_20240220_EDUCATION_POLICY_THEME_FALSE_POSITIVE","case_id":"R13L73_STAGE2FP_C31_339950_20240220_EDUCATION_POLICY_THEME_FALSE_POSITIVE","symbol":"339950","company_name":"아이비김영","round":"R13","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_EDUCATION_POLICY_THEME_WITHOUT_ENROLLMENT_REVENUE_BRIDGE","fine_archetype_id":"R13_STAGE2_EDUCATION_POLICY_THEME_WITHOUT_REVENUE_BRIDGE","deep_sub_archetype_id":"EDUCATION_POLICY_MFE_WITHOUT_ENROLLMENT_REVENUE_MARGIN_CONVERSION","loop_objective":"cross_archetype_redteam|residual_false_positive_mining|stage2_actionable_bonus_stress_test|high_MAE_guardrail|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":2300,"evidence_available_at_that_date":"source_proxy_education_medical_school_policy_theme_without_enrollment_revenue_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_education_medical_school_policy_theme_without_enrollment_revenue_margin_bridge; evidence_url_pending","bridge_summary":"education policy optionality produced short MFE but no enrollment, revenue, margin, or service-demand bridge","stage2_evidence_fields":["education_policy_theme","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["policy_theme_local_peak","enrollment_revenue_bridge_absent","margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_enrollment_or_revenue_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/339/339950/2024.csv","profile_path":"atlas/symbol_profiles/339/339950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.91,"MFE_90D_pct":28.91,"MFE_180D_pct":28.91,"MFE_1Y_pct":28.91,"MFE_2Y_pct":28.91,"MAE_30D_pct":-18.52,"MAE_90D_pct":-26.09,"MAE_180D_pct":-35.65,"MAE_1Y_pct":-35.65,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-26","peak_price":2965,"drawdown_after_peak_pct":-50.08,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"education_policy_theme_local_4B_rejected_as_positive_stage","four_b_evidence_type":"theme_or_price_without_source_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"stage2_false_positive_education_policy_high_MAE","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L73_STAGE2FP_C31_339950_20240220_EDUCATION_POLICY_THEME_FALSE_POSITIVE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype Stage2 false-positive review; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L73_STAGE2FP_C30_001470_20240129_CONSTRUCTION_THEME_FALSE_POSITIVE","case_id":"R13L73_STAGE2FP_C30_001470_20240129_CONSTRUCTION_THEME_FALSE_POSITIVE","symbol":"001470","company_name":"삼부토건","round":"R13","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","source_fine_archetype_id":"C30_CONSTRUCTION_THEME_WITHOUT_BALANCE_TRUST_CASHFLOW_BRIDGE","fine_archetype_id":"R13_STAGE2_CONSTRUCTION_PF_THEME_WITHOUT_BALANCE_TRUST_BRIDGE","deep_sub_archetype_id":"CONSTRUCTION_PF_THEME_MFE_WITHOUT_BALANCE_LIQUIDITY_CASHFLOW_TRUST_REPAIR","loop_objective":"cross_archetype_redteam|residual_false_positive_mining|stage2_actionable_bonus_stress_test|high_MAE_guardrail|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":2020,"evidence_available_at_that_date":"source_proxy_construction_theme_price_spike_without_PF_trust_balance_cashflow_repair; evidence_url_pending","evidence_source":"source_proxy_construction_theme_price_spike_without_PF_trust_balance_cashflow_repair; evidence_url_pending","bridge_summary":"construction/PF theme price strength lacked balance repair, trust quality, liquidity, and cashflow bridge","stage2_evidence_fields":["construction_theme","PF_relief_expectation","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","trust_balance_bridge_absent","liquidity_cashflow_risk"],"stage4c_evidence_fields":["high_MAE_after_balance_trust_break_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv","profile_path":"atlas/symbol_profiles/001/001470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":37.62,"MFE_90D_pct":41.83,"MFE_180D_pct":41.83,"MFE_1Y_pct":41.83,"MFE_2Y_pct":41.83,"MAE_30D_pct":-7.82,"MAE_90D_pct":-25.25,"MAE_180D_pct":-78.22,"MAE_1Y_pct":-78.22,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-15","peak_price":2865,"drawdown_after_peak_pct":-84.64,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"construction_theme_local_4B_rejected_as_positive_stage_and_high_MAE_guard","four_b_evidence_type":"theme_or_price_without_source_bridge","four_c_protection_label":"high_MAE_thesis_break_watch","trigger_outcome_label":"stage2_false_positive_construction_theme_high_MAE","current_profile_verdict":"current_profile_false_positive_without_balance_trust_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L73_STAGE2FP_C30_001470_20240129_CONSTRUCTION_THEME_FALSE_POSITIVE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype Stage2 false-positive review; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 18.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L73_STAGE2FP_C31_015760_20240129_POLICY_TO_CASHFLOW_POSITIVE_CONTROL","trigger_id":"TRG_R13L73_STAGE2FP_C31_015760_20240129_POLICY_TO_CASHFLOW_POSITIVE_CONTROL","symbol":"015760","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"event_or_theme_score":9,"source_bridge_score":14,"relative_strength_score":9,"stage2_actionable_bonus":2,"local_4b_watch_score":6,"high_MAE_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"event_or_theme_score":7,"source_bridge_score":16,"relative_strength_score":8,"stage2_actionable_bonus":2,"local_4b_watch_score":9,"high_MAE_penalty":7},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow_with_4B_watch","changed_components":["event_or_theme_score","source_bridge_score","relative_strength_score","stage2_actionable_bonus","local_4b_watch_score","high_MAE_penalty"],"component_delta_explanation":"R13 positive-control: Stage2 survives because non-price policy-to-cashflow bridge exists, but 4B/drawdown watch blocks Green.","MFE_90D_pct":27.76,"MAE_90D_pct":-4.57,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L73_STAGE2FP_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_FALSE_POSITIVE","trigger_id":"TRG_R13L73_STAGE2FP_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_FALSE_POSITIVE","symbol":"013990","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"event_or_theme_score":12,"source_bridge_score":1,"relative_strength_score":12,"stage2_actionable_bonus":2,"local_4b_watch_score":4,"high_MAE_penalty":5},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"event_or_theme_score":4,"source_bridge_score":0,"relative_strength_score":5,"stage2_actionable_bonus":0,"local_4b_watch_score":10,"high_MAE_penalty":15},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["event_or_theme_score","source_bridge_score","relative_strength_score","stage2_actionable_bonus","local_4b_watch_score","high_MAE_penalty"],"component_delta_explanation":"R13 false-positive guard: event/theme score is demoted when source bridge is absent and high-MAE path confirms failure.","MFE_90D_pct":27.53,"MAE_90D_pct":-17.5,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L73_STAGE2FP_C31_339950_20240220_EDUCATION_POLICY_THEME_FALSE_POSITIVE","trigger_id":"TRG_R13L73_STAGE2FP_C31_339950_20240220_EDUCATION_POLICY_THEME_FALSE_POSITIVE","symbol":"339950","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"event_or_theme_score":12,"source_bridge_score":1,"relative_strength_score":12,"stage2_actionable_bonus":2,"local_4b_watch_score":4,"high_MAE_penalty":5},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"event_or_theme_score":4,"source_bridge_score":0,"relative_strength_score":5,"stage2_actionable_bonus":0,"local_4b_watch_score":10,"high_MAE_penalty":15},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["event_or_theme_score","source_bridge_score","relative_strength_score","stage2_actionable_bonus","local_4b_watch_score","high_MAE_penalty"],"component_delta_explanation":"R13 false-positive guard: event/theme score is demoted when source bridge is absent and high-MAE path confirms failure.","MFE_90D_pct":28.91,"MAE_90D_pct":-26.09,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L73_STAGE2FP_C30_001470_20240129_CONSTRUCTION_THEME_FALSE_POSITIVE","trigger_id":"TRG_R13L73_STAGE2FP_C30_001470_20240129_CONSTRUCTION_THEME_FALSE_POSITIVE","symbol":"001470","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"event_or_theme_score":12,"source_bridge_score":1,"relative_strength_score":12,"stage2_actionable_bonus":2,"local_4b_watch_score":4,"high_MAE_penalty":5},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"event_or_theme_score":4,"source_bridge_score":0,"relative_strength_score":5,"stage2_actionable_bonus":0,"local_4b_watch_score":10,"high_MAE_penalty":15},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["event_or_theme_score","source_bridge_score","relative_strength_score","stage2_actionable_bonus","local_4b_watch_score","high_MAE_penalty"],"component_delta_explanation":"R13 false-positive guard: event/theme score is demoted when source bridge is absent and high-MAE path confirms failure.","MFE_90D_pct":41.83,"MAE_90D_pct":-25.25,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive_without_balance_trust_guard"}
```

### 18.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,r13_stage2_requires_source_bridge_not_theme_only,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW,0,1,+1,"Across C31 and C30 rows, Stage2 should survive only when the source-archetype economic bridge exists; theme/event/price evidence alone should remain Watch/4B/high-MAE guard","015760 survives as positive control because policy-to-cashflow bridge exists; 013990, 339950, and 001470 are demoted because policy/construction themes lacked demand, revenue, balance, or cashflow bridge","TRG_R13L73_STAGE2FP_C31_015760_20240129_POLICY_TO_CASHFLOW_POSITIVE_CONTROL|TRG_R13L73_STAGE2FP_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_FALSE_POSITIVE|TRG_R13L73_STAGE2FP_C31_339950_20240220_EDUCATION_POLICY_THEME_FALSE_POSITIVE|TRG_R13L73_STAGE2FP_C30_001470_20240129_CONSTRUCTION_THEME_FALSE_POSITIVE",4,0,3,medium,cross_archetype_shadow_only,"R13 rows have do_not_count_as_new_case=true and independent_evidence_weight=0.0"
shadow_weight,r13_positive_control_bridge_survival_guard,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW,1,1,0,"The false-positive guard must not erase real Stage2 rows when non-price economics bridge exists","015760 prevents over-tightening: the policy row survives, but Green is blocked by local 4B/drawdown watch","TRG_R13L73_STAGE2FP_C31_015760_20240129_POLICY_TO_CASHFLOW_POSITIVE_CONTROL",1,0,0,medium,existing_axis_kept,"keeps stage2_actionable_evidence_bonus conditional rather than globally reversed"
```

### 18.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","r13_cross_case_count":4,"new_independent_case_count":0,"reused_case_count":4,"positive_control_count":1,"counterexample_count":3,"new_symbol_count_for_source_archetype":0,"new_trigger_family_count_for_source_archetype":0,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["stage2_theme_false_positive_without_source_bridge","positive_control_bridge_survival","policy_theme_high_MAE","construction_theme_high_MAE"],"loop_contribution_label":"r13_cross_archetype_stage2_false_positive_review","do_not_propose_new_weight_delta":false}
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
- R13 `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW` rows should update cross_archetype_shadow_profile only.

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
11. Add tests that source-bridge-positive Stage2 rows survive while theme-only Stage2 rows are demoted.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- R13 Stage2 false-positive guardrail coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 20. Next Round State

```text
completed_round = R13
completed_loop = 73
next_round = R1
next_loop = 74
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
atlas/symbol_profiles/015/015760.json
atlas/symbol_profiles/013/013990.json
atlas/symbol_profiles/339/339950.json
atlas/symbol_profiles/001/001470.json
atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv
atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv
atlas/ohlcv_tradable_by_symbol_year/339/339950/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv
```

This loop completes R13 / loop 73 and moves the scheduler to R1 / loop 74.
