# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R12
scheduled_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R13
computed_next_loop: 73
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: C31_POLICY_TO_ECONOMICS_CASHFLOW_DEMAND_BRIDGE_GUARD
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

R12 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or an under-covered service/agri branch. This run stays in L10/C31, but avoids the prior R12 tourism/면세 branch and the older agri-policy set. The residual target is the policy-to-economics bridge: tariff policy can work when it turns into cost recovery and cashflow, while low-birth and education-policy themes can spike without durable demand or revenue.

| layer | id | definition |
|---|---|---|
| round | R12 | policy/event or under-covered service residual |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | policy, subsidy, legislation, utility/social service event |
| canonical | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | policy/subsidy/legislation event must convert into economics |
| fine | C31_POLICY_TO_ECONOMICS_CASHFLOW_DEMAND_BRIDGE_GUARD | policy signal must become cashflow, demand, margin, revenue, or cost recovery |
| deep | ELECTRICITY_TARIFF_POLICY_TO_COST_RECOVERY_CASHFLOW_REPAIR | utility tariff/cashflow positive |
| deep | LOW_BIRTH_POLICY_CHILDCARE_THEME_WITHOUT_REAL_DEMAND_MARGIN_CASHFLOW_CONVERSION | low-birth policy theme false positive |
| deep | MEDICAL_SCHOOL_EDUCATION_POLICY_OPTIONALITY_WITHOUT_ENROLLMENT_REVENUE_MARGIN_CONVERSION | education policy theme false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 top-covered symbols are `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that cluster and also avoids the prior R12 service/tourism symbols `114090`, `032350`, `008770`, and the older agri branch symbols `002900`, `000490`, and `054050`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C31 | 015760 | new independent | not top-covered C31 symbol; utility tariff/cost-pass-through cashflow bridge |
| C31 | 013990 | new independent | not top-covered C31 symbol; low-birth policy theme high-MAE counterexample |
| C31 | 339950 | new independent | not top-covered C31 symbol; education policy theme high-MAE counterexample |

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
015760 has no corporate-action candidate dates.
013990 has a 2008-05-16 corporate-action candidate date, outside the selected 2024 representative window.
339950 has a 2020-10-13 corporate-action candidate date, outside the selected 2024 representative window.
All three representative windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_drawdown_watch | 015760 | 한국전력 | Stage2-Actionable | 2024-01-29 | 19920 | tariff/cost-pass-through policy bridge worked but needed 4B/drawdown watch |
| theme_MFE_then_high_MAE_counterexample | 013990 | 아가방컴퍼니 | Stage2-Actionable | 2024-01-03 | 5630 | low-birth policy theme lacked demand/margin bridge |
| education_policy_theme_MFE_then_high_MAE_counterexample | 339950 | 아이비김영 | Stage2-Actionable | 2024-02-20 | 2300 | education policy theme lacked enrollment/revenue bridge |

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
| 015760 | 한국전력 | Stage2-Actionable | 2024-01-29 | 19920 | 27.76 | 27.76 | 27.76 | -3.92 | -4.57 | -8.68 | 2024-03-14 | 25450 | -28.53 |
| 013990 | 아가방컴퍼니 | Stage2-Actionable | 2024-01-03 | 5630 | 27.53 | 27.53 | 27.53 | -9.95 | -17.5 | -39.61 | 2024-01-18 | 7180 | -52.65 |
| 339950 | 아이비김영 | Stage2-Actionable | 2024-02-20 | 2300 | 28.91 | 28.91 | 28.91 | -18.52 | -26.09 | -35.65 | 2024-02-26 | 2965 | -50.08 |

## 9. Case-by-Case Notes

### 9.1 015760 / 한국전력 — tariff policy to cashflow bridge

The entry row is 2024-01-29 at 19,920. The 30D and 90D path reaches 25,450, then the later path gives back much of the move. This is the valid C31 policy case: the signal was not just policy language. Tariff/cost-pass-through and cashflow repair were the economic bridge. Still, because the peak comes early and the policy path is reversible, it should be Yellow plus 4B/drawdown watch, not Green.

### 9.2 013990 / 아가방컴퍼니 — low-birth policy theme without demand bridge

The entry row is 2024-01-03 at 5,630. The path reaches 7,180, but later falls to 3,400. This is the C31 social-policy trap: low-birth policy headlines can ignite childcare-related equities, but unless they convert into durable demand, margin, inventory, or cashflow, the policy headline is only a loud doorbell with nobody entering the store.

### 9.3 339950 / 아이비김영 — education policy theme without enrollment/revenue bridge

The entry row is 2024-02-20 at 2,300. The forward path reaches 2,965, then later falls to 1,480. This is the education-service version of the same residual: medical-school or education-policy optionality can create MFE, but without enrollment, revenue, margin, or operating leverage, it should remain 4B/high-MAE watch rather than Stage3 evidence.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C31 treats policy theme price strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C31 needs policy-to-economics bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for low-birth/education theme rows. |
| Full 4B non-price requirement appropriate? | Yes. 015760 has a cashflow bridge; 013990/339950 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
015760:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after tariff/cost recovery and cashflow bridge
  Stage3-Green = reject unless policy durability and drawdown risk clear

013990:
  Stage2-Actionable = acceptable only as policy-theme watch
  Stage3-Yellow = reject without demand, margin, inventory, or cashflow bridge
  Stage3-Green = reject despite MFE

339950:
  Stage2-Actionable = acceptable only as policy-theme watch
  Stage3-Yellow = reject without enrollment, revenue, margin, or service-demand bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 015760 | 1.00 | 1.00 | policy-to-cashflow bridge positive but local 4B/drawdown watch |
| 013990 | 1.00 | 1.00 | low-birth policy theme local 4B watch, not positive stage |
| 339950 | 1.00 | 1.00 | education policy theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c31_requires_policy_to_economics_cashflow_demand_bridge

rule:
  For C31 policy/subsidy/legislation rows, do not promote tariff, utility,
  low-birth, education, childcare, quota, subsidy, or social-policy Stage2 signals
  into Stage3-Yellow/Green unless at least one non-price economic bridge is visible:
  cost pass-through, cashflow repair, balance-sheet repair, durable demand,
  enrollment/revenue conversion, margin recovery, inventory normalization,
  operating leverage, or earnings revision tied to policy economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 28.07 | -16.05 | 66.7% | too generous to social-policy theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 28.07 | -16.05 | 33.3% | safer but may miss 015760 |
| P1 sector_specific_candidate_profile | 3 | 28.07 | -16.05 | 66.7% | no broad L10 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 27.76 | -4.57 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected | 28.22 | -21.8 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 015760 | current_profile_correct_but_no_green | tariff/cashflow bridge aligned with MFE, but drawdown requires 4B watch |
| 013990 | current_profile_false_positive_if_green | low-birth policy MFE lacked demand/margin bridge |
| 339950 | current_profile_false_positive_if_green | education policy MFE lacked enrollment/revenue bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31_POLICY_TO_ECONOMICS_CASHFLOW_DEMAND_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R12 non-tourism/non-agri C31 policy-to-economics residual reduced |

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
- social policy theme without economic bridge
- utility tariff winner needs 4B drawdown watch
- education policy MFE without enrollment/revenue bridge
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
- round/sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean forward windows
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
shadow_weight,c31_requires_policy_to_economics_cashflow_demand_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"C31 policy/subsidy/event rows should not promote toward Stage3-Yellow/Green unless policy signal converts into cashflow, cost pass-through, demand, enrollment, margin, revenue, inventory, or economic bridge","015760 survives as utility tariff/cashflow repair case; 013990 and 339950 fail when low-birth or education policy theme lacks demand/revenue/margin bridge","TRG_R12L73_C31_015760_20240129_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE|TRG_R12L73_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_NO_DEMAND_MARGIN_BRIDGE|TRG_R12L73_C31_339950_20240220_EDUCATION_POLICY_THEME_NO_ENROLLMENT_REVENUE_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_policy_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Policy-event winners and social-policy theme failures can peak quickly before economics is proven; local/full-window 4B and high-MAE watch should remain active after MFE","preserves 015760 guarded positive while preventing 013990/339950 policy-theme false positives","TRG_R12L73_C31_015760_20240129_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE|TRG_R12L73_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_NO_DEMAND_MARGIN_BRIDGE|TRG_R12L73_C31_339950_20240220_EDUCATION_POLICY_THEME_NO_ENROLLMENT_REVENUE_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R12L73_C31_015760_20240129_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE","symbol":"015760","company_name":"한국전력","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_UTILITY_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE","deep_sub_archetype_id":"ELECTRICITY_TARIFF_POLICY_TO_COST_RECOVERY_CASHFLOW_REPAIR","case_type":"structural_success_then_4B_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R12 C31 policy/event rows require policy-to-economics bridge: cashflow, cost pass-through, demand, enrollment, margin, inventory, or revenue conversion; policy theme alone is insufficient."}
{"row_type":"case","case_id":"R12L73_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_NO_DEMAND_MARGIN_BRIDGE","symbol":"013990","company_name":"아가방컴퍼니","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_LOW_BIRTH_POLICY_CONSUMER_THEME_WITHOUT_DEMAND_MARGIN_BRIDGE","deep_sub_archetype_id":"LOW_BIRTH_POLICY_CHILDCARE_THEME_WITHOUT_REAL_DEMAND_MARGIN_CASHFLOW_CONVERSION","case_type":"theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"R12 C31 policy/event rows require policy-to-economics bridge: cashflow, cost pass-through, demand, enrollment, margin, inventory, or revenue conversion; policy theme alone is insufficient."}
{"row_type":"case","case_id":"R12L73_C31_339950_20240220_EDUCATION_POLICY_THEME_NO_ENROLLMENT_REVENUE_BRIDGE","symbol":"339950","company_name":"아이비김영","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_EDUCATION_POLICY_THEME_WITHOUT_ENROLLMENT_REVENUE_BRIDGE","deep_sub_archetype_id":"MEDICAL_SCHOOL_EDUCATION_POLICY_OPTIONALITY_WITHOUT_ENROLLMENT_REVENUE_MARGIN_CONVERSION","case_type":"education_policy_theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"R12 C31 policy/event rows require policy-to-economics bridge: cashflow, cost pass-through, demand, enrollment, margin, inventory, or revenue conversion; policy theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R12L73_C31_015760_20240129_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE","case_id":"R12L73_C31_015760_20240129_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE","symbol":"015760","company_name":"한국전력","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_UTILITY_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE","deep_sub_archetype_id":"ELECTRICITY_TARIFF_POLICY_TO_COST_RECOVERY_CASHFLOW_REPAIR","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":19920,"evidence_available_at_that_date":"source_proxy_utility_tariff_cost_pass_through_cashflow_repair_policy_bridge; evidence_url_pending","evidence_source":"source_proxy_utility_tariff_cost_pass_through_cashflow_repair_policy_bridge; evidence_url_pending","bridge_summary":"tariff/cost-pass-through and utility cashflow repair converted policy event into economics; later policy reversal/drawdown risk required 4B watch","stage2_evidence_fields":["utility_tariff_policy","cost_pass_through_proxy","relative_strength","cashflow_repair_proxy"],"stage3_evidence_fields":["policy_to_cashflow_visibility","cost_recovery_bridge","balance_sheet_repair_proxy"],"stage4b_evidence_fields":["post_tariff_peak_watch","policy_reversal_or_delay_watch","utility_valueup_crowding"],"stage4c_evidence_fields":["drawdown_watch_after_policy_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv","profile_path":"atlas/symbol_profiles/015/015760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.76,"MFE_90D_pct":27.76,"MFE_180D_pct":27.76,"MFE_1Y_pct":27.76,"MFE_2Y_pct":27.76,"MAE_30D_pct":-3.92,"MAE_90D_pct":-4.57,"MAE_180D_pct":-8.68,"MAE_1Y_pct":-8.68,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-14","peak_price":25450,"drawdown_after_peak_pct":-28.53,"green_lateness_ratio":"0.44","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"policy_to_cashflow_bridge_positive_but_local_4B_drawdown_watch","four_b_evidence_type":"non_price_policy_to_cashflow_bridge","four_c_protection_label":"policy_delay_drawdown_watch","trigger_outcome_label":"structural_success_then_4B_drawdown_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L73_C31_015760_20240129_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R12L73_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_NO_DEMAND_MARGIN_BRIDGE","case_id":"R12L73_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_NO_DEMAND_MARGIN_BRIDGE","symbol":"013990","company_name":"아가방컴퍼니","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_LOW_BIRTH_POLICY_CONSUMER_THEME_WITHOUT_DEMAND_MARGIN_BRIDGE","deep_sub_archetype_id":"LOW_BIRTH_POLICY_CHILDCARE_THEME_WITHOUT_REAL_DEMAND_MARGIN_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-03","entry_date":"2024-01-03","entry_price":5630,"evidence_available_at_that_date":"source_proxy_low_birth_policy_childcare_theme_without_demand_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_low_birth_policy_childcare_theme_without_demand_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"low-birth/childcare policy theme created MFE, but no durable demand, margin, inventory, or cashflow bridge followed; high MAE should block Stage3","stage2_evidence_fields":["low_birth_policy_theme","childcare_consumption_theme","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["policy_theme_local_peak","demand_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_policy_to_demand_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv","profile_path":"atlas/symbol_profiles/013/013990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.53,"MFE_90D_pct":27.53,"MFE_180D_pct":27.53,"MFE_1Y_pct":27.53,"MFE_2Y_pct":27.53,"MAE_30D_pct":-9.95,"MAE_90D_pct":-17.5,"MAE_180D_pct":-39.61,"MAE_1Y_pct":-39.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-18","peak_price":7180,"drawdown_after_peak_pct":-52.65,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_birth_policy_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"policy_theme_without_economic_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L73_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_NO_DEMAND_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R12L73_C31_339950_20240220_EDUCATION_POLICY_THEME_NO_ENROLLMENT_REVENUE_BRIDGE","case_id":"R12L73_C31_339950_20240220_EDUCATION_POLICY_THEME_NO_ENROLLMENT_REVENUE_BRIDGE","symbol":"339950","company_name":"아이비김영","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_EDUCATION_POLICY_THEME_WITHOUT_ENROLLMENT_REVENUE_BRIDGE","deep_sub_archetype_id":"MEDICAL_SCHOOL_EDUCATION_POLICY_OPTIONALITY_WITHOUT_ENROLLMENT_REVENUE_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":2300,"evidence_available_at_that_date":"source_proxy_education_medical_school_policy_theme_without_enrollment_revenue_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_education_medical_school_policy_theme_without_enrollment_revenue_margin_bridge; evidence_url_pending","bridge_summary":"education/medical-school policy optionality produced a short MFE spike, but enrollment, revenue, margin, or durable service-demand bridge did not follow","stage2_evidence_fields":["education_policy_theme","medical_school_quota_or_exam_service_optionality","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["policy_theme_local_peak","enrollment_revenue_bridge_absent","margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_enrollment_or_revenue_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/339/339950/2024.csv","profile_path":"atlas/symbol_profiles/339/339950.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.91,"MFE_90D_pct":28.91,"MFE_180D_pct":28.91,"MFE_1Y_pct":28.91,"MFE_2Y_pct":28.91,"MAE_30D_pct":-18.52,"MAE_90D_pct":-26.09,"MAE_180D_pct":-35.65,"MAE_1Y_pct":-35.65,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-26","peak_price":2965,"drawdown_after_peak_pct":-50.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"education_policy_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"policy_theme_without_economic_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"policy_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L73_C31_339950_20240220_EDUCATION_POLICY_THEME_NO_ENROLLMENT_REVENUE_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L73_C31_015760_20240129_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE","trigger_id":"TRG_R12L73_C31_015760_20240129_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE","symbol":"015760","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_score":11,"economic_bridge_score":12,"cashflow_or_demand_score":12,"margin_or_cost_recovery_score":10,"relative_strength_score":10,"policy_reversal_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_score":9,"economic_bridge_score":16,"cashflow_or_demand_score":15,"margin_or_cost_recovery_score":13,"relative_strength_score":8,"policy_reversal_risk_penalty":8},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["policy_event_score","economic_bridge_score","cashflow_or_demand_score","margin_or_cost_recovery_score","relative_strength_score","policy_reversal_risk_penalty"],"component_delta_explanation":"C31 utility policy row is promoted only when policy converts into cost recovery and cashflow repair; later drawdown keeps 4B watch active.","MFE_90D_pct":27.76,"MAE_90D_pct":-4.57,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L73_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_NO_DEMAND_MARGIN_BRIDGE","trigger_id":"TRG_R12L73_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_NO_DEMAND_MARGIN_BRIDGE","symbol":"013990","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_score":12,"economic_bridge_score":1,"cashflow_or_demand_score":1,"margin_or_cost_recovery_score":0,"relative_strength_score":12,"policy_reversal_risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_score":5,"economic_bridge_score":0,"cashflow_or_demand_score":0,"margin_or_cost_recovery_score":0,"relative_strength_score":5,"policy_reversal_risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["policy_event_score","economic_bridge_score","cashflow_or_demand_score","margin_or_cost_recovery_score","relative_strength_score","policy_reversal_risk_penalty"],"component_delta_explanation":"C31 guard demotes social-policy theme rows when demand, enrollment, margin, revenue, or cashflow bridge is absent.","MFE_90D_pct":27.53,"MAE_90D_pct":-17.5,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L73_C31_339950_20240220_EDUCATION_POLICY_THEME_NO_ENROLLMENT_REVENUE_BRIDGE","trigger_id":"TRG_R12L73_C31_339950_20240220_EDUCATION_POLICY_THEME_NO_ENROLLMENT_REVENUE_BRIDGE","symbol":"339950","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_score":12,"economic_bridge_score":1,"cashflow_or_demand_score":1,"margin_or_cost_recovery_score":0,"relative_strength_score":12,"policy_reversal_risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_score":5,"economic_bridge_score":0,"cashflow_or_demand_score":0,"margin_or_cost_recovery_score":0,"relative_strength_score":5,"policy_reversal_risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["policy_event_score","economic_bridge_score","cashflow_or_demand_score","margin_or_cost_recovery_score","relative_strength_score","policy_reversal_risk_penalty"],"component_delta_explanation":"C31 guard demotes social-policy theme rows when demand, enrollment, margin, revenue, or cashflow bridge is absent.","MFE_90D_pct":28.91,"MAE_90D_pct":-26.09,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_requires_policy_to_economics_cashflow_demand_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"C31 policy/subsidy/event rows should not promote toward Stage3-Yellow/Green unless policy signal converts into cashflow, cost pass-through, demand, enrollment, margin, revenue, inventory, or economic bridge","015760 survives as utility tariff/cashflow repair case; 013990 and 339950 fail when low-birth or education policy theme lacks demand/revenue/margin bridge","TRG_R12L73_C31_015760_20240129_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE|TRG_R12L73_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_NO_DEMAND_MARGIN_BRIDGE|TRG_R12L73_C31_339950_20240220_EDUCATION_POLICY_THEME_NO_ENROLLMENT_REVENUE_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_policy_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Policy-event winners and social-policy theme failures can peak quickly before economics is proven; local/full-window 4B and high-MAE watch should remain active after MFE","preserves 015760 guarded positive while preventing 013990/339950 policy-theme false positives","TRG_R12L73_C31_015760_20240129_TARIFF_POLICY_COST_PASS_THROUGH_CASHFLOW_BRIDGE|TRG_R12L73_C31_013990_20240103_LOW_BIRTH_POLICY_THEME_NO_DEMAND_MARGIN_BRIDGE|TRG_R12L73_C31_339950_20240220_EDUCATION_POLICY_THEME_NO_ENROLLMENT_REVENUE_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R12","loop":"73","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["social_policy_theme_without_economic_bridge","utility_tariff_winner_needs_4B_drawdown_watch","education_policy_MFE_without_enrollment_revenue_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R12-specific handling

- R12 may use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or under-covered service/agri branches.
- This MD uses `L10_POLICY_EVENT_CROSS_REDTEAM_MISC / C31_POLICY_SUBSIDY_LEGISLATION_EVENT`.
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
- price-only/policy-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R12 allowed branch and large_sector_id.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C31 policy/subsidy/legislation rows cannot promote without policy-to-economics bridge: cost pass-through, cashflow repair, demand, enrollment/revenue conversion, margin, inventory, or operating leverage.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R12
completed_loop = 73
next_round = R13
next_loop = 73
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
atlas/symbol_profiles/015/015760.json
atlas/symbol_profiles/013/013990.json
atlas/symbol_profiles/339/339950.json
atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv
atlas/ohlcv_tradable_by_symbol_year/013/013990/2024.csv
atlas/ohlcv_tradable_by_symbol_year/339/339950/2024.csv
```

This loop continues loop 73 with R12 and adds 3 new independent C31 representative cases, 1 positive, 2 counterexamples, and 1 canonical-archetype residual guard candidate for R12/L10.
