# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R11
scheduled_loop: 71
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R12
computed_next_loop: 71
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: C31_UTILITY_TARIFF_POLICY_TO_CASHFLOW_BRIDGE_GUARD
loop_objective: counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Current Calibrated Profile Assumption

Current proxy remains `e2r_2_1_stock_web_calibrated`.

```text
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

R11 is the policy/event bridge round. This execution uses the L10 branch and compresses the case set into C31. The working distinction is simple: policy is not fuel by itself; it must become cashflow, contract, tariff pass-through, or a legal economic right.

| layer | id | definition |
|---|---|---|
| round | R11 | policy/event/government bridge |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | policy, subsidy, legislation, event, governance-adjacent checks |
| canonical | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | policy/subsidy/legislation event must convert into economics |
| fine | C31_UTILITY_TARIFF_POLICY_TO_CASHFLOW_BRIDGE_GUARD | utility tariff and cost-pass-through bridge |
| deep | ELECTRICITY_TARIFF_COST_PASS_THROUGH_REPAIR | electricity tariff/cashflow repair |
| deep | DISTRICT_HEATING_TARIFF_COST_PASS_THROUGH_RERATING | heat tariff/operating leverage |
| deep | GEOPOLITICAL_GAS_PRICE_THEME_PRICE_ONLY_FALSE_POSITIVE | gas policy/geopolitical theme without bridge |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 is broad and already covered, but the top-covered symbols are `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that top cluster and fills regulated-utility policy-to-cashflow bridge coverage.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C31 | 015760 | new independent | not top-covered C31 symbol; electricity tariff/cashflow repair |
| C31 | 071320 | new independent | not top-covered C31 symbol; heat tariff operating leverage |
| C31 | 117580 | new independent | not top-covered C31 symbol; gas/geopolitical theme counterexample |

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
```

Schema assumptions:

```text
tradable columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
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
| structural_success | 015760 | 한국전력 | Stage2-Actionable | 2024-01-25 | 19160 | tariff/cost pass-through policy bridge worked |
| structural_success | 071320 | 지역난방공사 | Stage2-Actionable | 2024-01-26 | 29000 | heat tariff/operating leverage bridge worked |
| failed_rerating | 117580 | 대성에너지 | Stage2-Actionable | 2024-01-15 | 12500 | gas/geopolitical policy theme without cashflow bridge failed |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 1
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 015760 | 한국전력 | Stage2-Actionable | 2024-01-25 | 19160 | 31.0 | 32.83 | 32.83 | -4.59 | -4.59 | -4.59 | 2024-03-14 | 25450 | -25.3 |
| 071320 | 지역난방공사 | Stage2-Actionable | 2024-01-26 | 29000 | 76.9 | 85.86 | 85.86 | -5.17 | -5.17 | -5.17 | 2024-06-18 | 53900 | -33.21 |
| 117580 | 대성에너지 | Stage2-Actionable | 2024-01-15 | 12500 | 6.64 | 6.64 | 6.64 | -30.4 | -36.32 | -36.32 | 2024-01-16 | 13330 | -40.29 |

## 9. Case-by-Case Notes

### 9.1 015760 / 한국전력 — electricity tariff policy to cashflow repair

The entry row is 2024-01-25 at 19,160. The 90D path reaches 25,450, while drawdown from the local policy peak later matters. This is not a price-only policy theme; it has a cost pass-through / cashflow repair bridge.

```text
MFE_90D_pct = 32.83
MAE_90D_pct = -4.59
four_b_timing_verdict = local_4B_watch_after_policy_cashflow_bridge
```

### 9.2 071320 / 지역난방공사 — heat tariff policy to operating leverage

The entry row is 2024-01-26 at 29,000. The price path reaches 51,300 quickly and 53,900 later. This is a strong C31 positive because tariff policy acted like a valve that finally let economics move into the income statement.

```text
MFE_30D_pct = 76.9
MFE_180D_pct = 85.86
MAE_180D_pct = -5.17
```

### 9.3 117580 / 대성에너지 — gas policy/geopolitical theme without cashflow bridge

The entry row is 2024-01-15 at 12,500. The local high was almost immediate, while the 90D low reached 7,960. This is the policy-theme trap: there was heat and noise, but no regulated cashflow bridge.

```text
MFE_90D_pct = 6.64
MAE_90D_pct = -36.32
current_profile_verdict = current_profile_false_positive
```

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C31 treats policy/geopolitical theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C31 should require cashflow/contract/tariff bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes for 117580. |
| Full 4B non-price requirement appropriate? | Yes. 015760/071320 have policy-to-cashflow bridge; 117580 does not. |
| 4C timing issue? | 117580 supports high-MAE watch rather than immediate hard 4C. |

## 11. Stage2 / Yellow / Green Comparison

```text
015760:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after tariff/cashflow bridge
  Stage3-Green = wait for stronger balance-sheet/cashflow confirmation

071320:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after tariff/operating-leverage bridge
  Stage3-Green = wait for revision durability and 4B risk check

117580:
  Stage2-Actionable = too generous if based only on gas/geopolitical theme
  Stage3-Yellow = reject without regulated tariff/cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 015760 | 0.97 | 1.00 | local 4B watch after tariff/cashflow bridge |
| 071320 | 0.95 | 1.00 | good full-window 4B watch after tariff/cashflow bridge |
| 117580 | 1.00 | 1.00 | price-only policy theme 4B rejected as full 4B but valid watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c31_requires_policy_to_cashflow_or_contract_bridge

rule:
  For C31, do not promote policy/subsidy/legislation rows from Stage2-Actionable into Stage3-Yellow/Green
  unless the policy event converts into at least one non-price economic bridge:
  tariff/cost pass-through, signed government contract, budget allocation,
  subsidy cashflow, legal entitlement, or direct margin/FCF repair.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 41.78 | -15.36 | 33.3% | mostly good but can over-credit gas/geopolitical theme |
| P0b e2r_2_0_baseline_reference | 3 | 41.78 | -15.36 | 0% | safer but may miss tariff bridge winners |
| P1 sector_specific_candidate_profile | 3 | 41.78 | -15.36 | 33.3% | no broad L10 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 59.34 | -4.88 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 6.64 | -36.32 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 015760 | current_profile_correct | policy-to-cashflow bridge aligned with positive MFE |
| 071320 | current_profile_correct | tariff/operating-leverage bridge aligned with strong MFE |
| 117580 | current_profile_false_positive | price-only gas/geopolitical theme produced high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31_UTILITY_TARIFF_POLICY_TO_CASHFLOW_BRIDGE_GUARD | 2 | 1 | 3 | 1 | 3 | 0 | 3 | 3 | 1 | false | true | C31 utility policy-to-cashflow bridge residual reduced |

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
residual_error_types_found:
- policy theme without cashflow bridge
- utility tariff policy to cashflow success
- gas/geopolitical policy price-only high MAE
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- local_4b_watch_guard
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
shadow_weight,c31_requires_policy_to_cashflow_or_contract_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"C31 policy/subsidy rows should not promote toward Stage3-Yellow/Green unless policy converts into tariff/cashflow/contract/economic bridge","015760 and 071320 survive with strong MFE after tariff/cashflow bridge; 117580 fails as gas/geopolitical policy theme without bridge","TRG_R11L71_C31_015760_20240125_TARIFF_POLICY_CASHFLOW_BRIDGE|TRG_R11L71_C31_071320_20240126_HEAT_TARIFF_POLICY_CASHFLOW_BRIDGE|TRG_R11L71_C31_117580_20240115_GAS_THEME_NO_CASHFLOW_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,price_policy_theme_local_4b_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Policy-theme price spikes should remain local 4B/watch unless non-price economic conversion appears","keeps 117580 as watch-only while preserving utility tariff positives","TRG_R11L71_C31_117580_20240115_GAS_THEME_NO_CASHFLOW_BRIDGE",1,1,1,medium,existing_axis_kept,"strengthens local 4B watch behavior without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R11L71_C31_015760_20240125_TARIFF_POLICY_CASHFLOW_BRIDGE","symbol":"015760","company_name":"한국전력","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_REGULATED_UTILITY_TARIFF_POLICY_TO_CASHFLOW","deep_sub_archetype_id":"ELECTRICITY_TARIFF_COST_PASS_THROUGH_REPAIR","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C31 regulated-utility policy rows require tariff/cost-pass-through/cashflow bridge before Stage2 travels toward Yellow/Green."}
{"row_type":"case","case_id":"R11L71_C31_071320_20240126_HEAT_TARIFF_POLICY_CASHFLOW_BRIDGE","symbol":"071320","company_name":"지역난방공사","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_HEAT_TARIFF_POLICY_TO_OPERATING_LEVERAGE","deep_sub_archetype_id":"DISTRICT_HEATING_TARIFF_COST_PASS_THROUGH_RERATING","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C31 regulated-utility policy rows require tariff/cost-pass-through/cashflow bridge before Stage2 travels toward Yellow/Green."}
{"row_type":"case","case_id":"R11L71_C31_117580_20240115_GAS_THEME_NO_CASHFLOW_BRIDGE","symbol":"117580","company_name":"대성에너지","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_GAS_POLICY_THEME_WITHOUT_CASHFLOW_BRIDGE","deep_sub_archetype_id":"GEOPOLITICAL_GAS_PRICE_THEME_PRICE_ONLY_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C31 regulated-utility policy rows require tariff/cost-pass-through/cashflow bridge before Stage2 travels toward Yellow/Green."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R11L71_C31_015760_20240125_TARIFF_POLICY_CASHFLOW_BRIDGE","case_id":"R11L71_C31_015760_20240125_TARIFF_POLICY_CASHFLOW_BRIDGE","symbol":"015760","company_name":"한국전력","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_REGULATED_UTILITY_TARIFF_POLICY_TO_CASHFLOW","deep_sub_archetype_id":"ELECTRICITY_TARIFF_COST_PASS_THROUGH_REPAIR","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":19160,"evidence_available_at_that_date":"source_proxy_electricity_tariff_cost_pass_through_and_cashflow_repair; evidence_url_pending","evidence_source":"source_proxy_electricity_tariff_cost_pass_through_and_cashflow_repair; evidence_url_pending","bridge_summary":"tariff/cost pass-through policy had non-price cashflow repair route","stage2_evidence_fields":["tariff_policy","regulated_utility_cashflow_repair","non_price_policy_to_earnings_bridge"],"stage3_evidence_fields":["cost_pass_through_visibility","earnings_revision_proxy","balance_sheet_repair_optionality"],"stage4b_evidence_fields":["policy_rerating_peak_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv","profile_path":"atlas/symbol_profiles/015/015760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.0,"MFE_90D_pct":32.83,"MFE_180D_pct":32.83,"MFE_1Y_pct":32.83,"MFE_2Y_pct":32.83,"MAE_30D_pct":-4.59,"MAE_90D_pct":-4.59,"MAE_180D_pct":-4.59,"MAE_1Y_pct":-4.59,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-14","peak_price":25450,"drawdown_after_peak_pct":-25.3,"green_lateness_ratio":"0.42","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_watch_after_policy_cashflow_bridge","four_b_evidence_type":"non_price_tariff_cashflow_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L71_C31_015760_20240125_TARIFF_POLICY_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R11L71_C31_071320_20240126_HEAT_TARIFF_POLICY_CASHFLOW_BRIDGE","case_id":"R11L71_C31_071320_20240126_HEAT_TARIFF_POLICY_CASHFLOW_BRIDGE","symbol":"071320","company_name":"지역난방공사","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_HEAT_TARIFF_POLICY_TO_OPERATING_LEVERAGE","deep_sub_archetype_id":"DISTRICT_HEATING_TARIFF_COST_PASS_THROUGH_RERATING","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":29000,"evidence_available_at_that_date":"source_proxy_heat_tariff_cost_pass_through_and_operating_leverage_repair; evidence_url_pending","evidence_source":"source_proxy_heat_tariff_cost_pass_through_and_operating_leverage_repair; evidence_url_pending","bridge_summary":"heat tariff policy converted into operating leverage/cashflow repair route","stage2_evidence_fields":["tariff_policy","regulated_heat_utility","cost_pass_through_bridge","relative_strength"],"stage3_evidence_fields":["operating_leverage_after_tariff","earnings_visibility_proxy","non_price_policy_cashflow_bridge"],"stage4b_evidence_fields":["policy_rerating_peak_watch","crowding_after_MFE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/071/071320/2024.csv","profile_path":"atlas/symbol_profiles/071/071320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":76.9,"MFE_90D_pct":85.86,"MFE_180D_pct":85.86,"MFE_1Y_pct":85.86,"MFE_2Y_pct":85.86,"MAE_30D_pct":-5.17,"MAE_90D_pct":-5.17,"MAE_180D_pct":-5.17,"MAE_1Y_pct":-5.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":53900,"drawdown_after_peak_pct":-33.21,"green_lateness_ratio":"0.35","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_policy_cashflow_bridge","four_b_evidence_type":"non_price_tariff_cashflow_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L71_C31_071320_20240126_HEAT_TARIFF_POLICY_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R11L71_C31_117580_20240115_GAS_THEME_NO_CASHFLOW_BRIDGE","case_id":"R11L71_C31_117580_20240115_GAS_THEME_NO_CASHFLOW_BRIDGE","symbol":"117580","company_name":"대성에너지","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_GAS_POLICY_THEME_WITHOUT_CASHFLOW_BRIDGE","deep_sub_archetype_id":"GEOPOLITICAL_GAS_PRICE_THEME_PRICE_ONLY_FALSE_POSITIVE","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-15","entry_date":"2024-01-15","entry_price":12500,"evidence_available_at_that_date":"source_proxy_gas_geopolitical_policy_theme_without_regulated_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_gas_geopolitical_policy_theme_without_regulated_cashflow_bridge; evidence_url_pending","bridge_summary":"gas/geopolitical theme lacked regulated tariff or cashflow conversion bridge","stage2_evidence_fields":["gas_policy_or_geopolitical_theme","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","weak_follow_through"],"stage4c_evidence_fields":["high_MAE_without_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/117/117580/2024.csv","profile_path":"atlas/symbol_profiles/117/117580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.64,"MFE_90D_pct":6.64,"MFE_180D_pct":6.64,"MFE_1Y_pct":6.64,"MFE_2Y_pct":6.64,"MAE_30D_pct":-30.4,"MAE_90D_pct":-36.32,"MAE_180D_pct":-36.32,"MAE_1Y_pct":-36.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-16","peak_price":13330,"drawdown_after_peak_pct":-40.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_policy_theme_4B_rejected_as_full_4B_but_valid_watch","four_b_evidence_type":"price_only_policy_theme","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L71_C31_117580_20240115_GAS_THEME_NO_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L71_C31_015760_20240125_TARIFF_POLICY_CASHFLOW_BRIDGE","trigger_id":"TRG_R11L71_C31_015760_20240125_TARIFF_POLICY_CASHFLOW_BRIDGE","symbol":"015760","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_score":12,"cashflow_bridge_score":10,"tariff_visibility_score":12,"relative_strength_score":9,"valuation_repair_score":7,"risk_penalty":4},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_score":12,"cashflow_bridge_score":15,"tariff_visibility_score":15,"relative_strength_score":8,"valuation_repair_score":7,"risk_penalty":4},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["cashflow_bridge_score","tariff_visibility_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C31 utility policy rows are rewarded only when tariff/cost pass-through converts into cashflow repair.","MFE_90D_pct":32.83,"MAE_90D_pct":-4.59,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L71_C31_071320_20240126_HEAT_TARIFF_POLICY_CASHFLOW_BRIDGE","trigger_id":"TRG_R11L71_C31_071320_20240126_HEAT_TARIFF_POLICY_CASHFLOW_BRIDGE","symbol":"071320","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_score":12,"cashflow_bridge_score":10,"tariff_visibility_score":12,"relative_strength_score":9,"valuation_repair_score":7,"risk_penalty":4},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_score":12,"cashflow_bridge_score":15,"tariff_visibility_score":15,"relative_strength_score":8,"valuation_repair_score":7,"risk_penalty":4},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["cashflow_bridge_score","tariff_visibility_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C31 utility policy rows are rewarded only when tariff/cost pass-through converts into cashflow repair.","MFE_90D_pct":85.86,"MAE_90D_pct":-5.17,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L71_C31_117580_20240115_GAS_THEME_NO_CASHFLOW_BRIDGE","trigger_id":"TRG_R11L71_C31_117580_20240115_GAS_THEME_NO_CASHFLOW_BRIDGE","symbol":"117580","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_score":10,"cashflow_bridge_score":1,"tariff_visibility_score":2,"relative_strength_score":12,"valuation_repair_score":3,"risk_penalty":7},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_score":5,"cashflow_bridge_score":0,"tariff_visibility_score":0,"relative_strength_score":5,"valuation_repair_score":1,"risk_penalty":13},"weighted_score_after":45,"stage_label_after":"Stage1-Watch","changed_components":["cashflow_bridge_score","tariff_visibility_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C31 guard demotes gas/geopolitical policy theme without regulated tariff or cashflow bridge.","MFE_90D_pct":6.64,"MAE_90D_pct":-36.32,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_requires_policy_to_cashflow_or_contract_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"C31 policy/subsidy rows should not promote toward Stage3-Yellow/Green unless policy converts into tariff/cashflow/contract/economic bridge","015760 and 071320 survive with strong MFE after tariff/cashflow bridge; 117580 fails as gas/geopolitical policy theme without bridge","TRG_R11L71_C31_015760_20240125_TARIFF_POLICY_CASHFLOW_BRIDGE|TRG_R11L71_C31_071320_20240126_HEAT_TARIFF_POLICY_CASHFLOW_BRIDGE|TRG_R11L71_C31_117580_20240115_GAS_THEME_NO_CASHFLOW_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,price_policy_theme_local_4b_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Policy-theme price spikes should remain local 4B/watch unless non-price economic conversion appears","keeps 117580 as watch-only while preserving utility tariff positives","TRG_R11L71_C31_117580_20240115_GAS_THEME_NO_CASHFLOW_BRIDGE",1,1,1,medium,existing_axis_kept,"strengthens local 4B watch behavior without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard"],"residual_error_types_found":["policy_theme_without_cashflow_bridge","utility_tariff_policy_to_cashflow_success","gas_geopolitical_policy_price_only_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R11
completed_loop = 71
next_round = R12
next_loop = 71
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
atlas/symbol_profiles/071/071320.json
atlas/symbol_profiles/117/117580.json
atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv
atlas/ohlcv_tradable_by_symbol_year/071/071320/2024.csv
atlas/ohlcv_tradable_by_symbol_year/117/117580/2024.csv
```

This loop adds 3 new independent cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R11/L10/C31.
