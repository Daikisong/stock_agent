# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R9
scheduled_loop: 71
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R10
computed_next_loop: 71
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: C29_AUTO_PARTS_VOLUME_MIX_MARGIN_BRIDGE_GUARD
loop_objective: counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_rule_candidate
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Current Calibrated Profile Assumption

Current proxy remains `e2r_2_1_stock_web_calibrated`. This run does not re-prove the already-applied global rules. It stress-tests them inside C29 mobility/auto-parts.

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

R9 allows mobility/transport cases under `L3_BATTERY_EV_GREEN_MOBILITY` or construction/PF cases under L9. This execution uses the mobility branch.

| layer | id | definition |
|---|---|---|
| round | R9 | mobility/transport bridge round |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | battery/EV/green mobility and mobility volume/margin |
| canonical | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | auto/OEM/auto-parts/transport volume, mix, and operating leverage |
| fine | C29_AUTO_PARTS_VOLUME_MIX_MARGIN_BRIDGE_GUARD | supplier-specific volume/mix/margin bridge before Yellow/Green |
| deep | BODY_CHASSIS_EXPORT_OPERATING_LEVERAGE | export-volume and margin conversion in body/chassis parts |
| deep | INTERIOR_MODULE_EXPORT_CUSTOMER_MIX_RERATING | customer/mix rerating in interior modules |
| deep | OEM_AFFILIATE_OPTIONALITY_WITHOUT_SUPPLIER_MARGIN_CONVERSION | weak bridge counterexample |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

The No-Repeat snapshot shows C29 has many rows, but the top-covered symbols are `UNKNOWN_SYMBOL`, `000270`, `161390`, `012330`, `005380`, and `018880`. This run avoids those top-covered clusters and fills non-top-covered supplier bridge coverage.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C29 | 010690 | new independent | not top-covered C29 symbol; auto-parts export/mix bridge |
| C29 | 200880 | new independent | not top-covered C29 symbol; interior parts customer/mix bridge |
| C29 | 011210 | new independent | not top-covered C29 symbol; weak subsystem/OEM-affiliate bridge counterexample |

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
| structural_success | 010690 | 화신 | Stage2-Actionable | 2023-03-09 | 11540 | export volume/mix margin bridge worked |
| structural_success | 200880 | 서연이화 | Stage2-Actionable | 2023-02-23 | 11200 | customer/mix rerating worked |
| failed_rerating | 011210 | 현대위아 | Stage2-Actionable | 2023-04-11 | 64400 | OEM-affiliate optionality without supplier margin bridge underperformed |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 2
4C_case_count: 0
calibration_usable_case_count: 3
current_profile_error_count: 1
```

This is not a raw coverage-count exercise. C29 is already well covered. The residual here is subtler: C29 winners need supplier-specific volume/mix/margin conversion. If the evidence is only OEM-affiliate optionality or mobility theme, the score should stay lower.

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 010690 | 화신 | Stage2-Actionable | 2023-03-09 | 11540 | 40.73 | 96.71 | 96.71 | -9.53 | -9.53 | -13.86 | 2023-07-06 | 22700 | -56.21 |
| 200880 | 서연이화 | Stage2-Actionable | 2023-02-23 | 11200 | 29.64 | 127.68 | 166.07 | -7.23 | -7.23 | -7.23 | 2023-07-17 | 29800 | -54.16 |
| 011210 | 현대위아 | Stage2-Actionable | 2023-04-11 | 64400 | 4.04 | 9.47 | 9.47 | -13.82 | -13.82 | -20.03 | 2023-07-06 | 70500 | -26.95 |

## 9. Case-by-Case Notes

### 9.1 010690 / 화신 — successful auto-parts export/mix bridge

The entry row is 2023-03-09 at 11,540. The 180D path reaches a high of 22,700 and later retraces sharply. That makes this a valid C29 success plus 4B watch case, not a simple “buy and forget” rerating.

```text
MFE_90D_pct = 96.71
MAE_90D_pct = -9.53
peak_date = 2023-07-06
four_b_timing_verdict = good_full_window_4B_timing_with_volume_margin_bridge
```

Interpretation:

```text
Stage2-Actionable was valid because the bridge was not just auto-theme price strength.
Required evidence family = auto parts export volume + customer/mix + margin leverage.
Stage3-Green should still require stronger revision/FCF confirmation.
```

### 9.2 200880 / 서연이화 — successful customer/mix rerating

The entry row is 2023-02-23 at 11,200. The 180D path reaches 29,800, but drawdown after the peak is deep. This supports C29 Stage2/Yellow recognition when customer/mix evidence exists, while still reinforcing 4B watch discipline.

```text
MFE_90D_pct = 127.68
MFE_180D_pct = 166.07
MAE_180D_pct = -7.23
four_b_timing_verdict = good_full_window_4B_timing_after_confirmed_customer_mix_bridge
```

### 9.3 011210 / 현대위아 — weak subsystem/OEM-affiliate bridge counterexample

The entry row is 2023-04-11 at 64,400. The 90D high reaches only 70,500, while 180D low reaches 51,500. This is a C29 false-positive pattern if the model gives too much credit to OEM-affiliate optionality without supplier-specific conversion.

```text
MFE_90D_pct = 9.47
MAE_180D_pct = -20.03
current_profile_verdict = current_profile_false_positive
```

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Only if C29 treats OEM-affiliate optionality as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C29 needs a supplier-specific bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes. Local peaks after auto-parts runs need watch overlay. |
| Full 4B non-price requirement appropriate? | Yes. 010690/200880 have better non-price bridge than 011210. |
| 4C routing issue? | No hard 4C proposed; this is high-MAE/watch, not thesis-break evidence. |

## 11. Stage2 / Yellow / Green Comparison

```text
010690:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after volume/mix/margin bridge
  Stage3-Green = wait for revision/FCF quality

200880:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after customer/mix bridge
  Stage3-Green = wait for earnings visibility and peak-risk review

011210:
  Stage2-Actionable = too generous if only theme/OEM-affiliate optionality exists
  Stage3-Yellow = reject without supplier-specific volume/margin conversion
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 010690 | 0.96 | 1.00 | good full-window 4B watch after confirmed bridge |
| 200880 | 0.91 | 1.00 | good full-window 4B watch after confirmed bridge |
| 011210 | 0.97 | 0.86 | weak local 4B watch only, not successful full-window rerating |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c29_requires_supplier_specific_volume_mix_margin_bridge

rule:
  For C29, do not promote mobility/auto rows from Stage2-Actionable into Stage3-Yellow/Green
  unless supplier-specific volume/mix/margin conversion is visible.
  OEM-affiliate optionality, robot/EV theme, or sector price strength alone should remain Stage1/Stage2 watch.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 77.95 | -10.19 | 33.3% | broadly good but can over-credit weak bridge |
| P0b e2r_2_0_baseline_reference | 3 | 77.95 | -10.19 | 0% | safer but risks missing 010690/200880 |
| P1 sector_specific_candidate_profile | 3 | 77.95 | -10.19 | 33.3% | no sector-wide L3 patch |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 112.19 | -8.38 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 9.47 | -13.82 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 010690 | current_profile_correct | volume/mix margin bridge aligned with strong MFE |
| 200880 | current_profile_correct | customer/mix bridge aligned with strong MFE |
| 011210 | current_profile_false_positive | weak bridge produced low MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | C29_AUTO_PARTS_VOLUME_MIX_MARGIN_BRIDGE_GUARD | 2 | 1 | 2 | 0 | 3 | 0 | 3 | 3 | 1 | false | true | C29 non-top-covered supplier bridge residual reduced |

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
- OEM-affiliate optionality without supplier margin bridge
- auto-parts success needs 4B watch after high MFE
- C29 high-MAE false positive when volume bridge is weak
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
shadow_weight,c29_requires_supplier_specific_volume_mix_margin_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 rows should require supplier-specific volume/mix/margin evidence before Stage3-Yellow/Green; OEM-affiliate optionality alone can produce weak MFE/high MAE","2 positive supplier bridge cases show strong MFE; 1 weak bridge case shows low MFE/high MAE","TRG_R9L71_C29_010690_20230309_AUTO_PARTS_EXPORT_MARGIN_BRIDGE|TRG_R9L71_C29_200880_20230223_INTERIOR_PARTS_CUSTOMER_MIX_RERATING|TRG_R9L71_C29_011210_20230411_SUBSYSTEM_VOLUME_BRIDGE_WEAK_FALSE_POSITIVE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,1,1,0,"Auto-parts rerating winners can peak quickly after volume/mix evidence; price-only local peaks should remain watch-only","preserves 4B watch for successful 010690/200880 while preventing full-4B treatment for weak 011210","TRG_R9L71_C29_010690_20230309_AUTO_PARTS_EXPORT_MARGIN_BRIDGE|TRG_R9L71_C29_200880_20230223_INTERIOR_PARTS_CUSTOMER_MIX_RERATING|TRG_R9L71_C29_011210_20230411_SUBSYSTEM_VOLUME_BRIDGE_WEAK_FALSE_POSITIVE",3,3,1,medium,existing_axis_kept,"strengthens existing watch behavior without new global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R9L71_C29_010690_20230309_AUTO_PARTS_EXPORT_MARGIN_BRIDGE","symbol":"010690","company_name":"화신","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_PARTS_EXPORT_VOLUME_MIX_MARGIN_BRIDGE","deep_sub_archetype_id":"BODY_CHASSIS_EXPORT_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C29 mobility/auto-parts rows require supplier-specific volume/mix/margin bridge; OEM-affiliate optionality alone is not enough."}
{"row_type":"case","case_id":"R9L71_C29_200880_20230223_INTERIOR_PARTS_CUSTOMER_MIX_RERATING","symbol":"200880","company_name":"서연이화","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_INTERIOR_PARTS_CUSTOMER_MIX_OPERATING_LEVERAGE","deep_sub_archetype_id":"INTERIOR_MODULE_EXPORT_CUSTOMER_MIX_RERATING","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C29 mobility/auto-parts rows require supplier-specific volume/mix/margin bridge; OEM-affiliate optionality alone is not enough."}
{"row_type":"case","case_id":"R9L71_C29_011210_20230411_SUBSYSTEM_VOLUME_BRIDGE_WEAK_FALSE_POSITIVE","symbol":"011210","company_name":"현대위아","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_SUBSYSTEM_VOLUME_BRIDGE_WEAK_HIGH_MAE_GUARD","deep_sub_archetype_id":"OEM_AFFILIATE_OPTIONALITY_WITHOUT_SUPPLIER_MARGIN_CONVERSION","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C29 mobility/auto-parts rows require supplier-specific volume/mix/margin bridge; OEM-affiliate optionality alone is not enough."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R9L71_C29_010690_20230309_AUTO_PARTS_EXPORT_MARGIN_BRIDGE","case_id":"R9L71_C29_010690_20230309_AUTO_PARTS_EXPORT_MARGIN_BRIDGE","symbol":"010690","company_name":"화신","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_PARTS_EXPORT_VOLUME_MIX_MARGIN_BRIDGE","deep_sub_archetype_id":"BODY_CHASSIS_EXPORT_OPERATING_LEVERAGE","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_rule_candidate","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-09","entry_date":"2023-03-09","entry_price":11540,"evidence_available_at_that_date":"source_proxy_auto_parts_export_volume_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_auto_parts_export_volume_margin_bridge; evidence_url_pending","bridge_summary":"export volume + mix/margin route survived price-path validation","stage2_evidence_fields":["auto_parts_export_volume","customer_mix_improvement","relative_strength","margin_leverage_proxy"],"stage3_evidence_fields":["operating_leverage_confirmed","mix_margin_bridge","non_price_evidence_confirmed"],"stage4b_evidence_fields":["valuation_repricing_after_mfe","positioning_overheat_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010690/2023.csv","profile_path":"atlas/symbol_profiles/010/010690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":40.73,"MFE_90D_pct":96.71,"MFE_180D_pct":96.71,"MFE_1Y_pct":96.71,"MFE_2Y_pct":96.71,"MAE_30D_pct":-9.53,"MAE_90D_pct":-9.53,"MAE_180D_pct":-13.86,"MAE_1Y_pct":-13.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-06","peak_price":22700,"drawdown_after_peak_pct":-56.21,"green_lateness_ratio":"0.31","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_with_volume_margin_bridge","four_b_evidence_type":"non_price_volume_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L71_C29_010690_20230309_AUTO_PARTS_EXPORT_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R9L71_C29_200880_20230223_INTERIOR_PARTS_CUSTOMER_MIX_RERATING","case_id":"R9L71_C29_200880_20230223_INTERIOR_PARTS_CUSTOMER_MIX_RERATING","symbol":"200880","company_name":"서연이화","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_INTERIOR_PARTS_CUSTOMER_MIX_OPERATING_LEVERAGE","deep_sub_archetype_id":"INTERIOR_MODULE_EXPORT_CUSTOMER_MIX_RERATING","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_rule_candidate","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-23","entry_date":"2023-02-23","entry_price":11200,"evidence_available_at_that_date":"source_proxy_auto_interior_parts_customer_mix_export_rerating; evidence_url_pending","evidence_source":"source_proxy_auto_interior_parts_customer_mix_export_rerating; evidence_url_pending","bridge_summary":"interior parts customer/mix bridge became price-validated","stage2_evidence_fields":["customer_mix_improvement","auto_parts_export_volume","relative_strength","margin_leverage_proxy"],"stage3_evidence_fields":["operating_leverage_confirmed","customer_mix_margin_bridge","earnings_revision_proxy"],"stage4b_evidence_fields":["valuation_repricing_after_mfe","local_blowoff_after_success"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/200/200880/2023.csv","profile_path":"atlas/symbol_profiles/200/200880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.64,"MFE_90D_pct":127.68,"MFE_180D_pct":166.07,"MFE_1Y_pct":166.07,"MFE_2Y_pct":166.07,"MAE_30D_pct":-7.23,"MAE_90D_pct":-7.23,"MAE_180D_pct":-7.23,"MAE_1Y_pct":-7.23,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-17","peak_price":29800,"drawdown_after_peak_pct":-54.16,"green_lateness_ratio":"0.28","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_after_confirmed_customer_mix_bridge","four_b_evidence_type":"non_price_volume_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L71_C29_200880_20230223_INTERIOR_PARTS_CUSTOMER_MIX_RERATING_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R9L71_C29_011210_20230411_SUBSYSTEM_VOLUME_BRIDGE_WEAK_FALSE_POSITIVE","case_id":"R9L71_C29_011210_20230411_SUBSYSTEM_VOLUME_BRIDGE_WEAK_FALSE_POSITIVE","symbol":"011210","company_name":"현대위아","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_SUBSYSTEM_VOLUME_BRIDGE_WEAK_HIGH_MAE_GUARD","deep_sub_archetype_id":"OEM_AFFILIATE_OPTIONALITY_WITHOUT_SUPPLIER_MARGIN_CONVERSION","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_rule_candidate","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-11","entry_date":"2023-04-11","entry_price":64400,"evidence_available_at_that_date":"source_proxy_auto_subsystem_robot_mobility_optionality_without_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_auto_subsystem_robot_mobility_optionality_without_margin_bridge; evidence_url_pending","bridge_summary":"theme/affiliate optionality lacked supplier-specific volume/margin conversion","stage2_evidence_fields":["auto_subsystem_optionality","relative_strength","OEM_affiliate_theme"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","weak_follow_through"],"stage4c_evidence_fields":["high_MAE_without_margin_conversion"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv","profile_path":"atlas/symbol_profiles/011/011210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.04,"MFE_90D_pct":9.47,"MFE_180D_pct":9.47,"MFE_1Y_pct":9.47,"MFE_2Y_pct":9.47,"MAE_30D_pct":-13.82,"MAE_90D_pct":-13.82,"MAE_180D_pct":-20.03,"MAE_1Y_pct":-20.03,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-06","peak_price":70500,"drawdown_after_peak_pct":-26.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.86,"four_b_timing_verdict":"weak_local_4B_watch_only_not_full_window_success","four_b_evidence_type":"weak_local_price_watch","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L71_C29_011210_20230411_SUBSYSTEM_VOLUME_BRIDGE_WEAK_FALSE_POSITIVE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L71_C29_010690_20230309_AUTO_PARTS_EXPORT_MARGIN_BRIDGE","trigger_id":"TRG_R9L71_C29_010690_20230309_AUTO_PARTS_EXPORT_MARGIN_BRIDGE","symbol":"010690","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"volume_score":12,"mix_margin_bridge_score":12,"customer_quality_score":10,"revision_score":8,"relative_strength_score":12,"valuation_score":7,"capital_allocation_score":1,"risk_penalty":3},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_score":13,"mix_margin_bridge_score":15,"customer_quality_score":11,"revision_score":9,"relative_strength_score":10,"valuation_score":7,"capital_allocation_score":1,"risk_penalty":3},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["mix_margin_bridge_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C29 bridge rewards supplier-specific volume/mix/margin conversion, but Green still waits for revision/FCF quality.","MFE_90D_pct":96.71,"MAE_90D_pct":-9.53,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L71_C29_200880_20230223_INTERIOR_PARTS_CUSTOMER_MIX_RERATING","trigger_id":"TRG_R9L71_C29_200880_20230223_INTERIOR_PARTS_CUSTOMER_MIX_RERATING","symbol":"200880","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"volume_score":12,"mix_margin_bridge_score":12,"customer_quality_score":10,"revision_score":8,"relative_strength_score":12,"valuation_score":7,"capital_allocation_score":1,"risk_penalty":3},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_score":13,"mix_margin_bridge_score":15,"customer_quality_score":11,"revision_score":9,"relative_strength_score":10,"valuation_score":7,"capital_allocation_score":1,"risk_penalty":3},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["mix_margin_bridge_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C29 bridge rewards supplier-specific volume/mix/margin conversion, but Green still waits for revision/FCF quality.","MFE_90D_pct":127.68,"MAE_90D_pct":-7.23,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L71_C29_011210_20230411_SUBSYSTEM_VOLUME_BRIDGE_WEAK_FALSE_POSITIVE","trigger_id":"TRG_R9L71_C29_011210_20230411_SUBSYSTEM_VOLUME_BRIDGE_WEAK_FALSE_POSITIVE","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"volume_score":6,"mix_margin_bridge_score":2,"customer_quality_score":6,"revision_score":3,"relative_strength_score":11,"valuation_score":5,"capital_allocation_score":1,"risk_penalty":6},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_score":5,"mix_margin_bridge_score":0,"customer_quality_score":4,"revision_score":2,"relative_strength_score":6,"valuation_score":4,"capital_allocation_score":1,"risk_penalty":10},"weighted_score_after":51,"stage_label_after":"Stage1-Watch","changed_components":["mix_margin_bridge_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C29 guard demotes OEM-affiliate/theme optionality when supplier-specific volume/margin bridge is missing.","MFE_90D_pct":9.47,"MAE_90D_pct":-13.82,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_requires_supplier_specific_volume_mix_margin_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"C29 rows should require supplier-specific volume/mix/margin evidence before Stage3-Yellow/Green; OEM-affiliate optionality alone can produce weak MFE/high MAE","2 positive supplier bridge cases show strong MFE; 1 weak bridge case shows low MFE/high MAE","TRG_R9L71_C29_010690_20230309_AUTO_PARTS_EXPORT_MARGIN_BRIDGE|TRG_R9L71_C29_200880_20230223_INTERIOR_PARTS_CUSTOMER_MIX_RERATING|TRG_R9L71_C29_011210_20230411_SUBSYSTEM_VOLUME_BRIDGE_WEAK_FALSE_POSITIVE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,1,1,0,"Auto-parts rerating winners can peak quickly after volume/mix evidence; price-only local peaks should remain watch-only","preserves 4B watch for successful 010690/200880 while preventing full-4B treatment for weak 011210","TRG_R9L71_C29_010690_20230309_AUTO_PARTS_EXPORT_MARGIN_BRIDGE|TRG_R9L71_C29_200880_20230223_INTERIOR_PARTS_CUSTOMER_MIX_RERATING|TRG_R9L71_C29_011210_20230411_SUBSYSTEM_VOLUME_BRIDGE_WEAK_FALSE_POSITIVE",3,3,1,medium,existing_axis_kept,"strengthens existing watch behavior without new global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"71","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard"],"residual_error_types_found":["OEM_affiliate_optionality_without_supplier_margin_bridge","auto_parts_success_needs_4B_watch_after_MFE","C29_high_MAE_false_positive_when_volume_bridge_weak"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R9
completed_loop = 71
next_round = R10
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
atlas/symbol_profiles/010/010690.json
atlas/symbol_profiles/200/200880.json
atlas/symbol_profiles/011/011210.json
atlas/ohlcv_tradable_by_symbol_year/010/010690/2023.csv
atlas/ohlcv_tradable_by_symbol_year/200/200880/2023.csv
atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv
```

This loop adds 3 new independent cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R9/L3/C29.
