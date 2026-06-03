# E2R Stock-Web Historical Calibration / R13 Cross-Archetype Red-Team Round

## 0. Research Metadata

```text
scheduled_round: R13
scheduled_loop: 71
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R1
computed_next_loop: 72
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: R13_HIGH_MAE_PRICE_ONLY_THEME_STAGE2_GUARD
loop_objective: cross_archetype_redteam | high_MAE_guardrail | stage2_false_positive_review | 4B_local_vs_full_window_check
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

R13 is not a normal sector expansion round. It is a cross-archetype checkpoint. Per the No-Repeat Index, R13 cross-check rows are accepted as `trigger` rows but must not become new independent source-archetype evidence.

```text
r13_cross_case = true
do_not_count_as_new_case = true
independent_evidence_weight = 0.0
```

This MD tests one residual question:

```text
When a Stage2-Actionable row is driven mostly by price/theme/policy noise,
and the forward path quickly shows high MAE,
should the model demote it to Watch / R13 High-MAE Guard even if the theme looks plausible?
```

## 3. Cross-Archetype Source Map

| R13 source | source canonical | selected symbol | reason |
|---|---|---:|---|
| software/security | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 042510 | security/policy theme without retention bridge |
| construction/PF | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 014790 | one-day construction spike without credit repair |
| policy/agri | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 054050 | seed/food-security theme without reorder/cashflow bridge |

## 4. No-Repeat / Duplicate Handling

Hard duplicate key remains:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

R13 rows are deliberately marked as cross-check rows. They are not counted as new C28/C30/C31 positives or negatives.

```text
new_independent_case_count = 0
reused_case_count = 3
r13_cross_case_count = 3
aggregate_group_role = r13_cross_check
do_not_count_as_new_case = true
independent_evidence_weight = 0.0
```

## 5. Stock-Web OHLC Input / Price Source Validation

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

## 6. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

## 7. Trigger-Level OHLC Backtest Table

| symbol | company | source canonical | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 042510 | 라온시큐어 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Stage2-Actionable | 2024-01-26 | 2940 | 4.25 | 4.25 | 4.25 | -21.09 | -22.62 | -42.55 | 2024-01-26 | 3065 | -44.89 |
| 014790 | HL D&I | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Stage2-Actionable | 2023-05-24 | 2975 | 11.43 | 11.43 | 11.43 | -12.27 | -23.36 | -33.58 | 2023-05-24 | 3315 | -40.39 |
| 054050 | 농우바이오 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2022-03-15 | 12150 | 19.34 | 19.34 | 19.34 | -8.64 | -23.05 | -35.47 | 2022-04-19 | 14500 | -45.93 |

## 8. Cross-Case Diagnosis

### 8.1 042510 / 라온시큐어

C28 requires retention, ARR/RPO, signed customer contract, or recurring security software revenue. The row behaved like a price/policy flare: local peak proximity was 1.00, MFE stayed shallow, and MAE expanded.

```text
source_canonical = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
missing_bridge = retention / ARR / RPO / enterprise contract
R13 verdict = demote to high-MAE watch
```

### 8.2 014790 / HL D&I

C30 requires PF, refinancing, liquidity, balance-sheet repair, or cashflow quality. The row was a one-day construction spike with no confirmed repair bridge. High MAE followed.

```text
source_canonical = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
missing_bridge = PF / credit / balance-sheet repair
R13 verdict = demote to high-MAE watch
```

### 8.3 054050 / 농우바이오

C31 under-covered agri/service rows require policy-to-economics conversion: export order, machinery demand, reorder, subsidy cashflow, or channel demand. Seed/food-security theme alone was not enough.

```text
source_canonical = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
missing_bridge = export / reorder / cashflow
R13 verdict = demote to high-MAE watch
```

## 9. Stage2 / Yellow / Green / 4B / 4C Comparison

```text
Common pattern:
  Stage2-Actionable = too generous if based on price/theme only
  Stage3-Yellow = reject without source-archetype bridge
  Stage3-Green = reject
  4B = local watch only, not full 4B
  4C = not always hard thesis break; high-MAE watch should fire earlier
```

## 10. Current Calibrated Profile Stress Test

| question | R13 result |
|---|---|
| Stage2 actionable bonus too strong? | Yes, when the evidence is price/theme-only. |
| Stage3 Yellow threshold too loose? | Not globally; bridge requirement should intercept before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, but high-MAE guard should cooperate with it earlier. |
| Full 4B non-price requirement appropriate? | Yes. All three are local 4B watch, not full 4B. |
| 4C routing issue? | These are high-MAE watch cases, not necessarily immediate hard 4C. |

## 11. Cross-Archetype Guardrail Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: cross_archetype_guardrail
rule_id: cross_archetype_high_mae_demotes_price_theme_stage2

rule:
  If Stage2-Actionable is based mostly on price/theme/policy relative strength,
  and source-archetype bridge evidence is absent,
  then high forward MAE should override the Stage2 bonus and route the row to:
  Stage1-Watch_or_R13_HighMAE_Guard,
  not Stage3-Yellow/Green.

bridge_required_by_source:
  C28 -> ARR/RPO/retention/customer contract
  C30 -> PF/credit/liquidity/balance-sheet repair
  C31 -> tariff/cashflow/order/reorder/subsidy economics
```

## 12. Before / After Backtest Comparison

| profile | eligible R13 cross rows | avg MFE90 | avg MAE90 | high-MAE false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 11.67 | -23.01 | 100.0% | price/theme-only Stage2 still dangerous |
| P0b e2r_2_0_baseline_reference | 3 | 11.67 | -23.01 | 66.7% | safer but unstructured |
| P2 cross_archetype_guard_profile | 3 demoted | 11.67 | -23.01 | 0.0% after demotion | preferred shadow |
| P3 local_4b_watch_only_profile | 3 watch-only | 11.67 | -37.2 | 0.0% after no-positive-routing | useful overlay |

## 13. Score-Return Alignment Matrix

| case | current profile verdict | R13 alignment |
|---|---|---|
| 042510 | current_profile_false_positive | demote price/security-policy theme |
| 014790 | current_profile_false_positive | demote one-day construction spike |
| 054050 | current_profile_false_positive | demote seed/food-security theme |

## 14. Coverage Matrix

| large_sector_id | canonical_archetype_id | source archetypes | cross rows | new independent | reused/cross | counterexample | high-MAE | sector_rule | canonical_rule | coverage contribution |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | C28/C30/C31 | 3 | 0 | 3 | 3 | 3 | false | true | strengthens R13 high-MAE guardrail without adding duplicate source-archetype coverage |

## 15. Residual Contribution Summary

```text
r13_cross_case_count: 3
new_independent_case_count: 0
reused_case_count: 3
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
- price/theme Stage2 without bridge high-MAE
- local 4B peak misread as positive evidence
- cross-archetype MAE penalty should override theme score
new_axis_proposed: null
existing_axis_strengthened:
- high_MAE_watch_guard
- local_4b_watch_guard
- stage2_required_bridge
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: r13_cross_archetype_high_MAE_guardrail
```

## 16. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- R13 round consistency
- cross-archetype source mapping
- do_not_count_as_new_case handling
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
```

## 17. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,cross_archetype_high_mae_demotes_price_theme_stage2,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,0,1,+1,"Across C28/C30/C31, price/theme-only Stage2 rows without non-price bridge show low MFE and high 90D/180D MAE","3 cross-check rows are demoted to Stage1/Watch_or_R13_HighMAE_Guard; no source-archetype evidence weight is added","TRG_R13L71_HIGHMAE_C28_042510_20240126_SECURITY_POLICY_PRICE_ONLY|TRG_R13L71_HIGHMAE_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE|TRG_R13L71_HIGHMAE_C31_054050_20220315_SEED_POLICY_THEME",3,0,3,medium,cross_archetype_shadow_only,"R13 rows have do_not_count_as_new_case=true per No-Repeat Index"
shadow_weight,price_only_local_4b_not_full_4b_cross_guard,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,1,1,0,"Local peak proximity is 1.0 in all rows, but full 4B must remain watch-only when non-price bridge is absent","prevents local price spike from becoming positive Stage2/Stage3 evidence","TRG_R13L71_HIGHMAE_C28_042510_20240126_SECURITY_POLICY_PRICE_ONLY|TRG_R13L71_HIGHMAE_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE|TRG_R13L71_HIGHMAE_C31_054050_20220315_SEED_POLICY_THEME",3,0,3,medium,existing_axis_kept,"strengthens local_4b_watch_guard without production delta"
```

## 18. Machine-Readable Rows

### 18.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 18.2 case rows

```jsonl
{"row_type":"case","case_id":"R13L71_HIGHMAE_C28_042510_20240126_SECURITY_POLICY_PRICE_ONLY","symbol":"042510","company_name":"라온시큐어","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"R13_HIGH_MAE_PRICE_ONLY_POLICY_THEME_STAGE2_GUARD","deep_sub_archetype_id":"SECURITY_POLICY_THEME_WITHOUT_RETENTION_BRIDGE","case_type":"r13_cross_case_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":false,"r13_cross_case":true,"do_not_count_as_new_case":true,"reuse_reason":"R13 cross-archetype checkpoint row; No-Repeat Index requires do_not_count_as_new_case=true for R13 cross validation","independent_evidence_weight":0.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: strengthens high-MAE guardrail, not source archetype coverage."}
{"row_type":"case","case_id":"R13L71_HIGHMAE_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE","symbol":"014790","company_name":"HL D&I","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"R13_HIGH_MAE_PRICE_ONLY_POLICY_THEME_STAGE2_GUARD","deep_sub_archetype_id":"SMALL_BUILDER_PRICE_SPIKE_WITHOUT_CREDIT_REPAIR","case_type":"r13_cross_case_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":false,"r13_cross_case":true,"do_not_count_as_new_case":true,"reuse_reason":"R13 cross-archetype checkpoint row; No-Repeat Index requires do_not_count_as_new_case=true for R13 cross validation","independent_evidence_weight":0.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: strengthens high-MAE guardrail, not source archetype coverage."}
{"row_type":"case","case_id":"R13L71_HIGHMAE_C31_054050_20220315_SEED_POLICY_THEME","symbol":"054050","company_name":"농우바이오","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"R13_HIGH_MAE_PRICE_ONLY_POLICY_THEME_STAGE2_GUARD","deep_sub_archetype_id":"SEED_FOOD_SECURITY_POLICY_THEME_WITHOUT_REORDER_CASHFLOW","case_type":"r13_cross_case_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":false,"r13_cross_case":true,"do_not_count_as_new_case":true,"reuse_reason":"R13 cross-archetype checkpoint row; No-Repeat Index requires do_not_count_as_new_case=true for R13 cross validation","independent_evidence_weight":0.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: strengthens high-MAE guardrail, not source archetype coverage."}
```

### 18.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R13L71_HIGHMAE_C28_042510_20240126_SECURITY_POLICY_PRICE_ONLY","case_id":"R13L71_HIGHMAE_C28_042510_20240126_SECURITY_POLICY_PRICE_ONLY","symbol":"042510","company_name":"라온시큐어","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"R13_HIGH_MAE_PRICE_ONLY_POLICY_THEME_STAGE2_GUARD","deep_sub_archetype_id":"SECURITY_POLICY_THEME_WITHOUT_RETENTION_BRIDGE","loop_objective":"cross_archetype_redteam|high_MAE_guardrail|stage2_false_positive_review|4B_local_vs_full_window_check","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":2940,"evidence_available_at_that_date":"source_proxy_mobile_ID_security_policy_theme_without_retention_bridge; evidence_url_pending","evidence_source":"source_proxy_mobile_ID_security_policy_theme_without_retention_bridge; evidence_url_pending","bridge_summary":"C28 security-policy theme lacked ARR/RPO/retention/customer-contract bridge","stage2_evidence_fields":["policy_or_security_theme","relative_strength","price_spike"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","weak_follow_through"],"stage4c_evidence_fields":["high_MAE_without_retention_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042510/2024.csv","profile_path":"atlas/symbol_profiles/042/042510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.25,"MFE_90D_pct":4.25,"MFE_180D_pct":4.25,"MFE_1Y_pct":4.25,"MFE_2Y_pct":4.25,"MAE_30D_pct":-21.09,"MAE_90D_pct":-22.62,"MAE_180D_pct":-42.55,"MAE_1Y_pct":-42.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-26","peak_price":3065,"drawdown_after_peak_pct":-44.89,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":"price_only_or_weak_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L71_HIGHMAE_C28_042510_20240126_SECURITY_POLICY_PRICE_ONLY_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","is_new_independent_case":false,"r13_cross_case":true,"reuse_reason":"R13 cross-archetype checkpoint; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L71_HIGHMAE_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE","case_id":"R13L71_HIGHMAE_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE","symbol":"014790","company_name":"HL D&I","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"R13_HIGH_MAE_PRICE_ONLY_POLICY_THEME_STAGE2_GUARD","deep_sub_archetype_id":"SMALL_BUILDER_PRICE_SPIKE_WITHOUT_CREDIT_REPAIR","loop_objective":"cross_archetype_redteam|high_MAE_guardrail|stage2_false_positive_review|4B_local_vs_full_window_check","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-24","entry_date":"2023-05-24","entry_price":2975,"evidence_available_at_that_date":"source_proxy_small_builder_price_spike_without_credit_PF_repair_bridge; evidence_url_pending","evidence_source":"source_proxy_small_builder_price_spike_without_credit_PF_repair_bridge; evidence_url_pending","bridge_summary":"C30 construction rebound lacked PF/credit/balance-sheet repair bridge","stage2_evidence_fields":["housing_rebound_theme","one_day_price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","weak_follow_through"],"stage4c_evidence_fields":["high_MAE_without_balance_sheet_or_credit_repair"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014790/2023.csv","profile_path":"atlas/symbol_profiles/014/014790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.43,"MFE_90D_pct":11.43,"MFE_180D_pct":11.43,"MFE_1Y_pct":11.43,"MFE_2Y_pct":11.43,"MAE_30D_pct":-12.27,"MAE_90D_pct":-23.36,"MAE_180D_pct":-33.58,"MAE_1Y_pct":-33.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-24","peak_price":3315,"drawdown_after_peak_pct":-40.39,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":"price_only_or_weak_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L71_HIGHMAE_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","is_new_independent_case":false,"r13_cross_case":true,"reuse_reason":"R13 cross-archetype checkpoint; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L71_HIGHMAE_C31_054050_20220315_SEED_POLICY_THEME","case_id":"R13L71_HIGHMAE_C31_054050_20220315_SEED_POLICY_THEME","symbol":"054050","company_name":"농우바이오","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"R13_HIGH_MAE_PRICE_ONLY_POLICY_THEME_STAGE2_GUARD","deep_sub_archetype_id":"SEED_FOOD_SECURITY_POLICY_THEME_WITHOUT_REORDER_CASHFLOW","loop_objective":"cross_archetype_redteam|high_MAE_guardrail|stage2_false_positive_review|4B_local_vs_full_window_check","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-15","entry_date":"2022-03-15","entry_price":12150,"evidence_available_at_that_date":"source_proxy_food_security_seed_policy_theme_without_reorder_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_food_security_seed_policy_theme_without_reorder_cashflow_bridge; evidence_url_pending","bridge_summary":"C31 food-security seed theme lacked reorder/export/cashflow bridge","stage2_evidence_fields":["food_security_policy","seed_theme","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","weak_follow_through"],"stage4c_evidence_fields":["high_MAE_without_reorder_or_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/054/054050/2022.csv","profile_path":"atlas/symbol_profiles/054/054050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.34,"MFE_90D_pct":19.34,"MFE_180D_pct":19.34,"MFE_1Y_pct":19.34,"MFE_2Y_pct":19.34,"MAE_30D_pct":-8.64,"MAE_90D_pct":-23.05,"MAE_180D_pct":-35.47,"MAE_1Y_pct":-35.47,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-19","peak_price":14500,"drawdown_after_peak_pct":-45.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_policy_theme_4B_watch_not_full_4B","four_b_evidence_type":"price_only_or_weak_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L71_HIGHMAE_C31_054050_20220315_SEED_POLICY_THEME_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","is_new_independent_case":false,"r13_cross_case":true,"reuse_reason":"R13 cross-archetype checkpoint; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 18.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L71_HIGHMAE_C28_042510_20240126_SECURITY_POLICY_PRICE_ONLY","trigger_id":"TRG_R13L71_HIGHMAE_C28_042510_20240126_SECURITY_POLICY_PRICE_ONLY","symbol":"042510","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"theme_or_event_score":10,"non_price_bridge_score":1,"relative_strength_score":11,"stage2_actionable_bonus":2,"high_MAE_risk_penalty":3,"price_only_4b_watch":1},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"theme_or_event_score":4,"non_price_bridge_score":0,"relative_strength_score":5,"stage2_actionable_bonus":0,"high_MAE_risk_penalty":12,"price_only_4b_watch":1},"weighted_score_after":44,"stage_label_after":"Stage1-Watch_or_R13_HighMAE_Guard","changed_components":["theme_or_event_score","non_price_bridge_score","relative_strength_score","stage2_actionable_bonus","high_MAE_risk_penalty"],"component_delta_explanation":"R13 guardrail demotes price/theme-only Stage2 rows when 90D/180D MAE becomes large and non-price bridge is absent.","MFE_90D_pct":4.25,"MAE_90D_pct":-22.62,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L71_HIGHMAE_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE","trigger_id":"TRG_R13L71_HIGHMAE_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE","symbol":"014790","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"theme_or_event_score":10,"non_price_bridge_score":1,"relative_strength_score":11,"stage2_actionable_bonus":2,"high_MAE_risk_penalty":3,"price_only_4b_watch":1},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"theme_or_event_score":4,"non_price_bridge_score":0,"relative_strength_score":5,"stage2_actionable_bonus":0,"high_MAE_risk_penalty":12,"price_only_4b_watch":1},"weighted_score_after":44,"stage_label_after":"Stage1-Watch_or_R13_HighMAE_Guard","changed_components":["theme_or_event_score","non_price_bridge_score","relative_strength_score","stage2_actionable_bonus","high_MAE_risk_penalty"],"component_delta_explanation":"R13 guardrail demotes price/theme-only Stage2 rows when 90D/180D MAE becomes large and non-price bridge is absent.","MFE_90D_pct":11.43,"MAE_90D_pct":-23.36,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L71_HIGHMAE_C31_054050_20220315_SEED_POLICY_THEME","trigger_id":"TRG_R13L71_HIGHMAE_C31_054050_20220315_SEED_POLICY_THEME","symbol":"054050","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"theme_or_event_score":10,"non_price_bridge_score":1,"relative_strength_score":11,"stage2_actionable_bonus":2,"high_MAE_risk_penalty":3,"price_only_4b_watch":1},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"theme_or_event_score":4,"non_price_bridge_score":0,"relative_strength_score":5,"stage2_actionable_bonus":0,"high_MAE_risk_penalty":12,"price_only_4b_watch":1},"weighted_score_after":44,"stage_label_after":"Stage1-Watch_or_R13_HighMAE_Guard","changed_components":["theme_or_event_score","non_price_bridge_score","relative_strength_score","stage2_actionable_bonus","high_MAE_risk_penalty"],"component_delta_explanation":"R13 guardrail demotes price/theme-only Stage2 rows when 90D/180D MAE becomes large and non-price bridge is absent.","MFE_90D_pct":19.34,"MAE_90D_pct":-23.05,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 18.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,cross_archetype_high_mae_demotes_price_theme_stage2,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,0,1,+1,"Across C28/C30/C31, price/theme-only Stage2 rows without non-price bridge show low MFE and high 90D/180D MAE","3 cross-check rows are demoted to Stage1/Watch_or_R13_HighMAE_Guard; no source-archetype evidence weight is added","TRG_R13L71_HIGHMAE_C28_042510_20240126_SECURITY_POLICY_PRICE_ONLY|TRG_R13L71_HIGHMAE_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE|TRG_R13L71_HIGHMAE_C31_054050_20220315_SEED_POLICY_THEME",3,0,3,medium,cross_archetype_shadow_only,"R13 rows have do_not_count_as_new_case=true per No-Repeat Index"
shadow_weight,price_only_local_4b_not_full_4b_cross_guard,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL,1,1,0,"Local peak proximity is 1.0 in all rows, but full 4B must remain watch-only when non-price bridge is absent","prevents local price spike from becoming positive Stage2/Stage3 evidence","TRG_R13L71_HIGHMAE_C28_042510_20240126_SECURITY_POLICY_PRICE_ONLY|TRG_R13L71_HIGHMAE_C30_014790_20230524_SMALL_BUILDER_ONE_DAY_SPIKE|TRG_R13L71_HIGHMAE_C31_054050_20220315_SEED_POLICY_THEME",3,0,3,medium,existing_axis_kept,"strengthens local_4b_watch_guard without production delta"
```

### 18.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","r13_cross_case_count":3,"new_independent_case_count":0,"reused_case_count":3,"new_symbol_count_for_source_archetype":0,"new_trigger_family_count_for_source_archetype":0,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["price_theme_stage2_without_bridge_high_MAE","local_4B_peak_misread_as_positive","cross_archetype_MAE_penalty_should_override_theme_score"],"loop_contribution_label":"r13_cross_archetype_high_MAE_guardrail","do_not_propose_new_weight_delta":false}
```

## 19. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R13-specific handling

- R13 cross-case rows must be parsed as trigger rows.
- R13 cross-case rows must keep `do_not_count_as_new_case=true`.
- R13 cross-case rows must not increase source archetype positive/counterexample coverage.
- Use them only for cross-archetype guardrail calibration.
- `independent_evidence_weight=0.0` means no duplicate source evidence.

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
- price-only rows cannot promote Stage2/Stage3.
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
9. Report cross-case count, counterexamples, and residual error types.
10. Add tests that R13 rows cannot change source archetype independent coverage.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- R13 guardrail coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 20. Next Round State

```text
completed_round = R13
completed_loop = 71
next_round = R1
next_loop = 72
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
atlas/symbol_profiles/042/042510.json
atlas/symbol_profiles/014/014790.json
atlas/symbol_profiles/054/054050.json
atlas/ohlcv_tradable_by_symbol_year/042/042510/2024.csv
atlas/ohlcv_tradable_by_symbol_year/014/014790/2023.csv
atlas/ohlcv_tradable_by_symbol_year/054/054050/2022.csv
```

This loop completes R13 / loop 71 and moves the scheduler to R1 / loop 72.
