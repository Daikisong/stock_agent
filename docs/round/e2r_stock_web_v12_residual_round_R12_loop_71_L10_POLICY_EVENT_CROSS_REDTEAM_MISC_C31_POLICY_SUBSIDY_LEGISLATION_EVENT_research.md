# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R12
scheduled_loop: 71
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R13
computed_next_loop: 71
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: C31_AGRI_POLICY_EXPORT_ORDER_REORDER_BRIDGE_GUARD
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

R12 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or relevant under-covered service/agri residual work. This MD uses C31 and compresses under-covered agri-policy cases into a policy-to-economics bridge test.

| layer | id | definition |
|---|---|---|
| round | R12 | L10 or under-covered service/agri residual |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | policy/event/misc with under-covered agri branch |
| canonical | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | policy/subsidy/legislation event must convert into economics |
| fine | C31_AGRI_POLICY_EXPORT_ORDER_REORDER_BRIDGE_GUARD | agri policy must become export/order/reorder/cashflow |
| deep | FOOD_SECURITY_MECHANIZATION_EXPORT_ORDER_CONVERSION | agri machinery demand/export conversion |
| deep | AGRI_MACHINERY_POLICY_TO_ORDER_BACKLOG_BUT_CYCLICAL_DRAWDOWN | machinery bridge plus 4B/high-MAE guard |
| deep | SEED_AGRI_POLICY_THEME_HIGH_MAE_NO_EXPORT_REORDER_CASHFLOW | seed/food-security theme without conversion |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 is broad and already covered, but the top-covered symbols are `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that top cluster and fills an under-covered agri/service policy branch.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C31 | 002900 | new independent | not top-covered C31 symbol; agri machinery export/order bridge |
| C31 | 000490 | new independent | not top-covered C31 symbol; agri machinery order bridge with 4B/high-MAE watch |
| C31 | 054050 | new independent | not top-covered C31 symbol; seed theme counterexample |

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

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success | 002900 | TYM | Stage2-Actionable | 2022-03-21 | 1855 | agri machinery export/order bridge worked |
| structural_success_with_high_MAE_watch | 000490 | 대동 | Stage2-Actionable | 2022-03-18 | 13550 | machinery order bridge worked, but 4B/high-MAE guard needed |
| failed_rerating | 054050 | 농우바이오 | Stage2-Actionable | 2022-03-15 | 12150 | seed/food-security theme without reorder/cashflow bridge failed |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 2
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 002900 | TYM | Stage2-Actionable | 2022-03-21 | 1855 | 101.08 | 105.66 | 105.66 | -6.2 | -6.2 | -6.2 | 2022-05-16 | 3815 | -49.41 |
| 000490 | 대동 | Stage2-Actionable | 2022-03-18 | 13550 | 42.07 | 42.07 | 42.07 | -7.01 | -21.4 | -21.4 | 2022-05-03 | 19250 | -44.68 |
| 054050 | 농우바이오 | Stage2-Actionable | 2022-03-15 | 12150 | 19.34 | 19.34 | 19.34 | -8.64 | -23.05 | -35.47 | 2022-04-19 | 14500 | -45.93 |

## 9. Case-by-Case Notes

### 9.1 002900 / TYM — agri machinery policy to export/order bridge

The entry row is 2022-03-21 at 1,855. The 90D path reaches 3,815 and MAE remains controlled around the entry window. This is the cleanest R12 agri-policy success: policy acts like irrigation only when it reaches the root, here represented by machinery demand and export/order conversion.

### 9.2 000490 / 대동 — agri machinery order bridge with high-MAE watch

The entry row is 2022-03-18 at 13,550. The path reaches 19,250, but later drawdown reaches the 10,650 area. This validates the machinery/order bridge while warning that C31 agri winners should not bypass 4B/high-MAE watch.

### 9.3 054050 / 농우바이오 — seed theme without reorder/cashflow bridge

The entry row is 2022-03-15 at 12,150. The path reaches 14,500, but then fades into a much deeper drawdown. This is a C31 counterexample: food-security policy language and seed-theme relative strength are not enough without reorder/export/cashflow evidence.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C31 treats agri/food-security theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; agri policy rows need export/order/reorder/cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes for 054050 and as watch discipline after 002900/000490 peaks. |
| Full 4B non-price requirement appropriate? | Yes. 002900/000490 have machinery demand bridge; 054050 does not. |
| 4C timing issue? | High-MAE watch is useful for seed-theme failure; no hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
002900:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after export/order bridge
  Stage3-Green = wait for earnings/cashflow durability and 4B risk check

000490:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed but high-MAE/4B watch must be active
  Stage3-Green = reject unless FCF/earnings durability clears drawdown risk

054050:
  Stage2-Actionable = too generous if based only on food-security/seed theme
  Stage3-Yellow = reject without reorder/export/cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 002900 | 0.98 | 1.00 | good full-window 4B watch after agri export bridge |
| 000490 | 0.98 | 1.00 | good 4B watch but requires drawdown guard |
| 054050 | 1.00 | 1.00 | price-only policy theme 4B rejected as full 4B but valid watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c31_agri_policy_requires_export_order_reorder_cashflow_bridge

rule:
  For C31 under-covered agri/service rows, do not promote food-security/agri policy themes
  from Stage2-Actionable into Stage3-Yellow/Green unless the policy event converts into
  at least one non-price economic bridge:
  export order, machinery demand, backlog/reorder, subsidy cashflow, channel demand,
  or verified margin/FCF repair.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 55.69 | -16.88 | 33.3% | useful but can over-credit seed/food-security theme |
| P0b e2r_2_0_baseline_reference | 3 | 55.69 | -16.88 | 0% | safer but may miss machinery bridge winners |
| P1 sector_specific_candidate_profile | 3 | 55.69 | -16.88 | 33.3% | no broad L10 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 73.86 | -13.8 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 19.34 | -23.05 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 002900 | current_profile_correct | policy-to-machinery/export bridge aligned with strong MFE |
| 000490 | current_profile_partially_correct | bridge worked, but drawdown requires 4B/high-MAE watch |
| 054050 | current_profile_false_positive | seed policy theme produced high MAE without reorder/cashflow bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31_AGRI_POLICY_EXPORT_ORDER_REORDER_BRIDGE_GUARD | 2 | 1 | 2 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | R12 under-covered agri/service branch reduced |

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
- agri policy without reorder/cashflow bridge
- agri machinery policy-to-export/order success
- agri policy winner needs 4B/high-MAE watch
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
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
shadow_weight,c31_agri_policy_requires_export_order_reorder_cashflow_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"R12 under-covered agri/service branch: food-security/agri policy rows should not promote toward Stage3-Yellow/Green unless policy converts into export/order/reorder/cashflow bridge","002900 and 000490 survive because machinery demand/export bridge exists; 054050 fails as seed/food-security theme without reorder/cashflow bridge","TRG_R12L71_C31_002900_20220321_AGRI_MACHINERY_EXPORT_POLICY_BRIDGE|TRG_R12L71_C31_000490_20220318_AGRI_MACHINERY_ORDER_BRIDGE_HIGH_MAE|TRG_R12L71_C31_054050_20220315_SEED_POLICY_THEME_NO_CASHFLOW_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,agri_policy_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Agri policy/machinery winners can peak quickly and still require 4B/high-MAE watch after MFE","preserves 002900/000490 positives while preventing 054050 policy-theme false positive","TRG_R12L71_C31_002900_20220321_AGRI_MACHINERY_EXPORT_POLICY_BRIDGE|TRG_R12L71_C31_000490_20220318_AGRI_MACHINERY_ORDER_BRIDGE_HIGH_MAE|TRG_R12L71_C31_054050_20220315_SEED_POLICY_THEME_NO_CASHFLOW_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch behavior without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R12L71_C31_002900_20220321_AGRI_MACHINERY_EXPORT_POLICY_BRIDGE","symbol":"002900","company_name":"TYM","round":"R12","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_AGRI_MACHINERY_POLICY_TO_EXPORT_DEMAND_BRIDGE","deep_sub_archetype_id":"FOOD_SECURITY_MECHANIZATION_EXPORT_ORDER_CONVERSION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"R12 under-covered agri/service branch: C31 agri policy rows require export/order/reorder/cashflow bridge."}
{"row_type":"case","case_id":"R12L71_C31_000490_20220318_AGRI_MACHINERY_ORDER_BRIDGE_HIGH_MAE","symbol":"000490","company_name":"대동","round":"R12","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_AGRI_MACHINERY_EXPORT_ORDER_BRIDGE_WITH_4B_GUARD","deep_sub_archetype_id":"AGRI_MACHINERY_POLICY_TO_ORDER_BACKLOG_BUT_CYCLICAL_DRAWDOWN","case_type":"structural_success_with_high_MAE_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"R12 under-covered agri/service branch: C31 agri policy rows require export/order/reorder/cashflow bridge."}
{"row_type":"case","case_id":"R12L71_C31_054050_20220315_SEED_POLICY_THEME_NO_CASHFLOW_BRIDGE","symbol":"054050","company_name":"농우바이오","round":"R12","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_SEED_FOOD_SECURITY_POLICY_THEME_WITHOUT_REORDER_BRIDGE","deep_sub_archetype_id":"SEED_AGRI_POLICY_THEME_HIGH_MAE_NO_EXPORT_REORDER_CASHFLOW","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R12 under-covered agri/service branch: C31 agri policy rows require export/order/reorder/cashflow bridge."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R12L71_C31_002900_20220321_AGRI_MACHINERY_EXPORT_POLICY_BRIDGE","case_id":"R12L71_C31_002900_20220321_AGRI_MACHINERY_EXPORT_POLICY_BRIDGE","symbol":"002900","company_name":"TYM","round":"R12","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_AGRI_MACHINERY_POLICY_TO_EXPORT_DEMAND_BRIDGE","deep_sub_archetype_id":"FOOD_SECURITY_MECHANIZATION_EXPORT_ORDER_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-21","entry_date":"2022-03-21","entry_price":1855,"evidence_available_at_that_date":"source_proxy_food_security_agri_mechanization_export_order_bridge; evidence_url_pending","evidence_source":"source_proxy_food_security_agri_mechanization_export_order_bridge; evidence_url_pending","bridge_summary":"food-security policy converted into agri-machinery export/order demand","stage2_evidence_fields":["food_security_policy","agri_mechanization_demand","export_order_bridge","relative_strength"],"stage3_evidence_fields":["machinery_export_conversion","revenue_visibility_proxy","non_price_demand_bridge"],"stage4b_evidence_fields":["post_policy_rerating_peak_watch","crowding_after_MFE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002900/2022.csv","profile_path":"atlas/symbol_profiles/002/002900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":101.08,"MFE_90D_pct":105.66,"MFE_180D_pct":105.66,"MFE_1Y_pct":105.66,"MFE_2Y_pct":105.66,"MAE_30D_pct":-6.2,"MAE_90D_pct":-6.2,"MAE_180D_pct":-6.2,"MAE_1Y_pct":-6.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-05-16","peak_price":3815,"drawdown_after_peak_pct":-49.41,"green_lateness_ratio":"0.30","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_agri_export_bridge","four_b_evidence_type":"non_price_export_order_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L71_C31_002900_20220321_AGRI_MACHINERY_EXPORT_POLICY_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R12L71_C31_000490_20220318_AGRI_MACHINERY_ORDER_BRIDGE_HIGH_MAE","case_id":"R12L71_C31_000490_20220318_AGRI_MACHINERY_ORDER_BRIDGE_HIGH_MAE","symbol":"000490","company_name":"대동","round":"R12","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_AGRI_MACHINERY_EXPORT_ORDER_BRIDGE_WITH_4B_GUARD","deep_sub_archetype_id":"AGRI_MACHINERY_POLICY_TO_ORDER_BACKLOG_BUT_CYCLICAL_DRAWDOWN","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-18","entry_date":"2022-03-18","entry_price":13550,"evidence_available_at_that_date":"source_proxy_agri_machinery_export_order_policy_bridge_with_cyclical_drawdown; evidence_url_pending","evidence_source":"source_proxy_agri_machinery_export_order_policy_bridge_with_cyclical_drawdown; evidence_url_pending","bridge_summary":"agri-machinery policy/order bridge worked, but post-peak drawdown required 4B/high-MAE watch","stage2_evidence_fields":["food_security_policy","agri_machinery_demand","export_or_order_bridge","relative_strength"],"stage3_evidence_fields":["order_or_export_visibility_proxy","non_price_demand_bridge"],"stage4b_evidence_fields":["post_MFE_reversal_watch","cyclical_drawdown_after_policy_rerating"],"stage4c_evidence_fields":["high_MAE_watch_after_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000490/2022.csv","profile_path":"atlas/symbol_profiles/000/000490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":42.07,"MFE_90D_pct":42.07,"MFE_180D_pct":42.07,"MFE_1Y_pct":42.07,"MFE_2Y_pct":42.07,"MAE_30D_pct":-7.01,"MAE_90D_pct":-21.4,"MAE_180D_pct":-21.4,"MAE_1Y_pct":-21.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-05-03","peak_price":19250,"drawdown_after_peak_pct":-44.68,"green_lateness_ratio":"0.43","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_4B_watch_but_requires_drawdown_guard","four_b_evidence_type":"non_price_export_order_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"structural_success_but_needs_4B_high_MAE_guard","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L71_C31_000490_20220318_AGRI_MACHINERY_ORDER_BRIDGE_HIGH_MAE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R12L71_C31_054050_20220315_SEED_POLICY_THEME_NO_CASHFLOW_BRIDGE","case_id":"R12L71_C31_054050_20220315_SEED_POLICY_THEME_NO_CASHFLOW_BRIDGE","symbol":"054050","company_name":"농우바이오","round":"R12","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_SEED_FOOD_SECURITY_POLICY_THEME_WITHOUT_REORDER_BRIDGE","deep_sub_archetype_id":"SEED_AGRI_POLICY_THEME_HIGH_MAE_NO_EXPORT_REORDER_CASHFLOW","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-15","entry_date":"2022-03-15","entry_price":12150,"evidence_available_at_that_date":"source_proxy_food_security_seed_theme_without_reorder_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_food_security_seed_theme_without_reorder_cashflow_bridge; evidence_url_pending","bridge_summary":"seed/food-security theme lacked export/reorder/cashflow conversion bridge","stage2_evidence_fields":["food_security_policy","seed_theme","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","weak_follow_through"],"stage4c_evidence_fields":["high_MAE_without_reorder_or_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/054/054050/2022.csv","profile_path":"atlas/symbol_profiles/054/054050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.34,"MFE_90D_pct":19.34,"MFE_180D_pct":19.34,"MFE_1Y_pct":19.34,"MFE_2Y_pct":19.34,"MAE_30D_pct":-8.64,"MAE_90D_pct":-23.05,"MAE_180D_pct":-35.47,"MAE_1Y_pct":-35.47,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-19","peak_price":14500,"drawdown_after_peak_pct":-45.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_policy_theme_4B_rejected_as_full_4B_but_valid_watch","four_b_evidence_type":"price_only_policy_theme","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L71_C31_054050_20220315_SEED_POLICY_THEME_NO_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L71_C31_002900_20220321_AGRI_MACHINERY_EXPORT_POLICY_BRIDGE","trigger_id":"TRG_R12L71_C31_002900_20220321_AGRI_MACHINERY_EXPORT_POLICY_BRIDGE","symbol":"002900","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_score":10,"export_order_bridge_score":12,"reorder_cashflow_score":8,"relative_strength_score":12,"valuation_repair_score":5,"risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_score":8,"export_order_bridge_score":16,"reorder_cashflow_score":11,"relative_strength_score":9,"valuation_repair_score":5,"risk_penalty":4},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["policy_score","export_order_bridge_score","reorder_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C31 agri policy row is promoted only because policy converted into machinery export/order bridge.","MFE_90D_pct":105.66,"MAE_90D_pct":-6.2,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L71_C31_000490_20220318_AGRI_MACHINERY_ORDER_BRIDGE_HIGH_MAE","trigger_id":"TRG_R12L71_C31_000490_20220318_AGRI_MACHINERY_ORDER_BRIDGE_HIGH_MAE","symbol":"000490","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_score":10,"export_order_bridge_score":10,"reorder_cashflow_score":6,"relative_strength_score":11,"valuation_repair_score":5,"risk_penalty":6},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_score":8,"export_order_bridge_score":13,"reorder_cashflow_score":7,"relative_strength_score":8,"valuation_repair_score":5,"risk_penalty":8},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["policy_score","export_order_bridge_score","reorder_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C31 agri machinery bridge works, but high-MAE/4B risk prevents Green loosening.","MFE_90D_pct":42.07,"MAE_90D_pct":-21.4,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L71_C31_054050_20220315_SEED_POLICY_THEME_NO_CASHFLOW_BRIDGE","trigger_id":"TRG_R12L71_C31_054050_20220315_SEED_POLICY_THEME_NO_CASHFLOW_BRIDGE","symbol":"054050","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_score":9,"export_order_bridge_score":1,"reorder_cashflow_score":1,"relative_strength_score":10,"valuation_repair_score":3,"risk_penalty":7},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_score":4,"export_order_bridge_score":0,"reorder_cashflow_score":0,"relative_strength_score":5,"valuation_repair_score":1,"risk_penalty":13},"weighted_score_after":44,"stage_label_after":"Stage1-Watch","changed_components":["policy_score","export_order_bridge_score","reorder_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C31 guard demotes seed/food-security policy theme without export/reorder/cashflow bridge.","MFE_90D_pct":19.34,"MAE_90D_pct":-23.05,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_agri_policy_requires_export_order_reorder_cashflow_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"R12 under-covered agri/service branch: food-security/agri policy rows should not promote toward Stage3-Yellow/Green unless policy converts into export/order/reorder/cashflow bridge","002900 and 000490 survive because machinery demand/export bridge exists; 054050 fails as seed/food-security theme without reorder/cashflow bridge","TRG_R12L71_C31_002900_20220321_AGRI_MACHINERY_EXPORT_POLICY_BRIDGE|TRG_R12L71_C31_000490_20220318_AGRI_MACHINERY_ORDER_BRIDGE_HIGH_MAE|TRG_R12L71_C31_054050_20220315_SEED_POLICY_THEME_NO_CASHFLOW_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,agri_policy_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Agri policy/machinery winners can peak quickly and still require 4B/high-MAE watch after MFE","preserves 002900/000490 positives while preventing 054050 policy-theme false positive","TRG_R12L71_C31_002900_20220321_AGRI_MACHINERY_EXPORT_POLICY_BRIDGE|TRG_R12L71_C31_000490_20220318_AGRI_MACHINERY_ORDER_BRIDGE_HIGH_MAE|TRG_R12L71_C31_054050_20220315_SEED_POLICY_THEME_NO_CASHFLOW_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch behavior without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R12","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard"],"residual_error_types_found":["agri_policy_without_reorder_cashflow_bridge","agri_machinery_policy_to_export_order_success","agri_policy_winner_needs_4B_high_MAE_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R12
completed_loop = 71
next_round = R13
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
atlas/symbol_profiles/002/002900.json
atlas/symbol_profiles/000/000490.json
atlas/symbol_profiles/054/054050.json
atlas/ohlcv_tradable_by_symbol_year/002/002900/2022.csv
atlas/ohlcv_tradable_by_symbol_year/000/000490/2022.csv
atlas/ohlcv_tradable_by_symbol_year/054/054050/2022.csv
```

This loop adds 3 new independent cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R12/L10/C31 under-covered agri/service policy.
