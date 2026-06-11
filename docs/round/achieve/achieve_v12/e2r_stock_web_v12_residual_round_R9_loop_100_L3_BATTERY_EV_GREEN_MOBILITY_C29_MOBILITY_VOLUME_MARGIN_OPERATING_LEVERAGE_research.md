# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
schema_family = v12_sector_archetype_residual
selected_round = R9
selected_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_OEM_VALUEUP_VOLUME_MIX_CAPITAL_RETURN_BRIDGE_VS_SUPPLIER_OPERATING_LEVERAGE_HIGH_MAE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. The already-applied global axes are baseline, not re-proposed globally:

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

This loop tests whether C29 needs a sharper split between **OEM value-up / volume-mix-margin / capital-return rerating** and **supplier operating-leverage vocabulary**. The residual question is whether a mobility label should be Stage2-Actionable only when the company-specific margin, mix, capital policy, or order conversion bridge is present.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R9 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | AUTO_OEM_VALUEUP_VOLUME_MIX_CAPITAL_RETURN_BRIDGE_VS_SUPPLIER_OPERATING_LEVERAGE_HIGH_MAE |
| scope logic | C29 maps to R9 / L3. Scope consistency passes. |

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` marks C29 as Priority 0 with only 3 rows and top-covered symbols `005710`, `007860`, `033530`. This loop avoids those top-covered symbols and adds four new symbols:

| symbol | name | novelty |
|---:|---|---|
| 005380 | 현대차 | new C29 OEM value-up / mix / capital-return route |
| 000270 | 기아 | new C29 OEM margin / capital-return parallel confirmation |
| 011210 | 현대위아 | new supplier operating-leverage false-positive route |
| 204320 | HL만도 | new supplier post-spike 4B overlay route |

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row intentionally repeats the top-covered C29 symbols.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| manifest | atlas/manifest.json |
| schema | atlas/schema.json |
| universe | atlas/universe/all_symbols.csv |
| manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

## 5. Historical Eligibility Gate

All representative entries are historical, have entry rows in stock-web tradable shards, have at least 180 forward trading days before the manifest max date, and are treated as calibration usable. Corporate action candidates for 005380/000270/204320 are outside the 2024~2025 windows used here; 011210 profile has no corporate-action candidate dates.

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | compression logic |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | OEM_valueup_volume_mix_capital_return_bridge | OEM rerating works when volume/mix, margin durability, valuation repricing, and shareholder return line up |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | OEM_parallel_confirmation | parallel OEM confirmation strengthens Stage2-Actionable but still does not unlock Green automatically |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | supplier_operating_leverage_label_false_positive | supplier beta cannot inherit OEM capital-return score without independent order/margin bridge |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | supplier_post_spike_4B_overlay | supplier rerating after local spike needs 4B watch if non-price extension evidence is weak |

## 7. Case Selection Summary

| case_id | symbol | name | role | trigger | entry | price |
|---|---:|---|---|---|---|---:|
| C29_R9L100_005380_20240125 | 005380 | 현대차 | structural_success | Stage2-Actionable | 2024-01-25 | 188700 |
| C29_R9L100_000270_20240125 | 000270 | 기아 | structural_success | Stage2-Actionable | 2024-01-25 | 93000 |
| C29_R9L100_011210_20240125 | 011210 | 현대위아 | failed_rerating | Stage2 | 2024-01-25 | 58000 |
| C29_R9L100_204320_20240605 | 204320 | HL만도 | 4B_overlay_success | Stage4B | 2024-06-05 | 49600 |

## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 4 |
| representative_trigger_count | 3 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| new_symbol_count | 4 |
| new_trigger_family_count | 4 |

## 9. Evidence Source Map

| case_id | evidence family | source status |
|---|---|---|
| C29_R9L100_005380_20240125 | OEM value-up, mix/margin, capital-return route | source_proxy_only / evidence_url_pending |
| C29_R9L100_000270_20240125 | OEM margin durability and shareholder-return parallel route | source_proxy_only / evidence_url_pending |
| C29_R9L100_011210_20240125 | supplier operating-leverage label without independent margin bridge | source_proxy_only / evidence_url_pending |
| C29_R9L100_204320_20240605 | supplier post-spike valuation/positioning 4B overlay | source_proxy_only / evidence_url_pending |

## 10. Price Data Source Map

| symbol | profile_path | shard_path | corporate_action_window_status |
|---:|---|---|---|
| 005380 | atlas/symbol_profiles/005/005380.json | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | clean_180D_window |
| 000270 | atlas/symbol_profiles/000/000270.json | atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv | clean_180D_window |
| 011210 | atlas/symbol_profiles/011/011210.json | atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv | clean_180D_window |
| 204320 | atlas/symbol_profiles/204/204320.json | atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_price | current_profile_verdict | outcome |
|---|---:|---|---:|---|---|
| T_C29_005380_STAGE2A_20240125 | 005380 | Stage2-Actionable | 188700 | current_profile_too_late | OEM bridge positive |
| T_C29_000270_STAGE2A_20240125 | 000270 | Stage2-Actionable | 93000 | current_profile_correct | OEM bridge positive |
| T_C29_011210_STAGE2_20240125 | 011210 | Stage2 | 58000 | current_profile_false_positive | supplier label high-MAE |
| T_C29_204320_STAGE4B_20240605 | 204320 | Stage4B | 49600 | current_profile_4B_too_late | post-spike 4B success |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|
| T_C29_005380_STAGE2A_20240125 | 38.31 | -2.76 | 47.06 | -2.76 | 58.72 | -2.76 | 2024-06-28 | 299500 | -27.71 |
| T_C29_000270_STAGE2A_20240125 | 41.61 | -7.42 | 45.16 | -7.42 | 45.16 | -7.42 | 2024-06-19 | 135000 | -29.63 |
| T_C29_011210_STAGE2_20240125 | 15.52 | -5.17 | 15.52 | -5.17 | 15.52 | -21.64 | 2024-02-05 | 67000 | -32.16 |
| T_C29_204320_STAGE4B_20240605 | 0.81 | -17.04 | 0.81 | -36.19 | 0.81 | -36.19 | 2024-06-05 | 50000 | -36.70 |

## 13. Current Calibrated Profile Stress Test

| case_id | profile verdict | actual path alignment | implication |
|---|---|---|---|
| C29_R9L100_005380_20240125 | current_profile_too_late | high MFE and shallow entry MAE | C29 OEM bridge can be Stage2-Actionable earlier |
| C29_R9L100_000270_20240125 | current_profile_correct | high MFE with tolerable MAE | OEM parallel confirmation supports the bridge |
| C29_R9L100_011210_20240125 | current_profile_false_positive | low MFE versus high 180D MAE | supplier label must not inherit OEM score |
| C29_R9L100_204320_20240605 | current_profile_4B_too_late | post-spike MFE stalled and MAE expanded | supplier spike should route to local 4B watch |

## 14. Stage2 / Yellow / Green Comparison

Stage2-Actionable works in this archetype only when the evidence bridge is company-specific: OEM volume/mix, margin durability, valuation rerating, and capital return. Stage3-Yellow can follow after confirmed revision and financial visibility. Stage3-Green should not be loosened by this loop.

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger in this loop
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| T_C29_204320_STAGE4B_20240605 | 0.98 | 0.98 | good_full_window_4B_timing |

The 204320 row is not a sell signal by price alone. It is an overlay: a supplier rerating after a local spike had weak non-price extension evidence and almost no further MFE, while MAE expanded sharply.

## 16. 4C Protection Audit

No hard 4C row is proposed. The 204320 row is `thesis_break_watch_only`, not a confirmed hard 4C. The loop strengthens 4B watch quality rather than routing to 4C.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
```

Rule candidate:

```text
For C29, Stage2-Actionable should require at least one OEM-quality bridge:
- volume/mix margin durability
- confirmed capital-return or value-up execution
- company-specific operating leverage evidence
- financial visibility or revision support

Supplier beta without independent order/margin bridge should remain Stage2-watch or 4B-watch.
```

## 18. Canonical-Archetype Rule Candidate

```text
new_axis_proposed = C29_oem_mix_margin_capital_return_bridge_required
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened = null
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive read |
|---|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 27.14 | -12.88 | supplier labels still too easy |
| P2 C29 canonical candidate | 4 | 27.14 | -12.88 | separates OEM bridge from supplier beta |
| P3 counterexample guard | 2 supplier rows | 8.17 | -20.68 | supplier weak-bridge rows need demotion/4B watch |

## 20. Score-Return Alignment Matrix

| case_id | score-return alignment | verdict |
|---|---|---|
| C29_R9L100_005380_20240125 | high score aligned with high MFE / shallow MAE | aligned_positive |
| C29_R9L100_000270_20240125 | high score aligned with high MFE | aligned_positive |
| C29_R9L100_011210_20240125 | demotion aligned with high 180D MAE | demotion_aligned |
| C29_R9L100_204320_20240605 | 4B guard aligned with post-spike MAE | 4B_guard_aligned |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counter | 4B | 4C | new_independent | reused | usable_triggers | representative_triggers | current_profile_error | sector_rule | canonical_rule | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_OEM_VALUEUP_VOLUME_MIX_CAPITAL_RETURN_BRIDGE_VS_SUPPLIER_OPERATING_LEVERAGE_HIGH_MAE | 2 | 2 | 1 | 0 | 4 | 0 | 4 | 3 | 3 | true | true | C29 3 → 6 representative rows if accepted; still Priority 0 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_too_late, current_profile_false_positive, current_profile_4B_too_late, supplier_high_MAE_guardrail
new_axis_proposed: C29_oem_mix_margin_capital_return_bridge_required
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min | stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical OHLC path, entry date/price, MFE/MAE, canonical scope, novelty, and 4B overlay timing.  
Non-validation scope: live investment recommendation, production scoring change, and external evidence URL repair.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_oem_mix_margin_capital_return_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"OEM bridge separates winners from supplier beta","better supplier false-positive control","T_C29_005380_STAGE2A_20240125|T_C29_000270_STAGE2A_20240125|T_C29_011210_STAGE2_20240125|T_C29_204320_STAGE4B_20240605",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C29_R9L100_005380_20240125","symbol":"005380","company_name":"현대차","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_VALUEUP_VOLUME_MIX_CAPITAL_RETURN_BRIDGE_VS_SUPPLIER_OPERATING_LEVERAGE_HIGH_MAE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"large OEM value-up, mix/margin and capital-return bridge aligned with high MFE and shallow entry MAE","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"OEM-level capital return and mix/margin route should not be compressed with generic mobility beta"}
{"row_type":"case","case_id":"C29_R9L100_000270_20240125","symbol":"000270","company_name":"기아","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_VALUEUP_VOLUME_MIX_CAPITAL_RETURN_BRIDGE_VS_SUPPLIER_OPERATING_LEVERAGE_HIGH_MAE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"OEM mix/capital-return bridge produced strong MFE with manageable entry MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"same sector as Hyundai but independent symbol and trigger family: capital-return plus margin durability"}
{"row_type":"case","case_id":"C29_R9L100_011210_20240125","symbol":"011210","company_name":"현대위아","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_VALUEUP_VOLUME_MIX_CAPITAL_RETURN_BRIDGE_VS_SUPPLIER_OPERATING_LEVERAGE_HIGH_MAE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"supplier label had limited MFE and later high MAE; operating leverage did not mirror OEM rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"supplier operating leverage must be proven separately, not inherited from OEM value-up"}
{"row_type":"case","case_id":"C29_R9L100_204320_20240605","symbol":"204320","company_name":"HL만도","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_VALUEUP_VOLUME_MIX_CAPITAL_RETURN_BRIDGE_VS_SUPPLIER_OPERATING_LEVERAGE_HIGH_MAE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"score_price_alignment":"post-spike supplier 4B overlay had almost no further MFE and large MAE","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"local supplier spike needs 4B watch unless non-price margin/order bridge extends"}
{"row_type":"trigger","trigger_id":"T_C29_005380_STAGE2A_20240125","case_id":"C29_R9L100_005380_20240125","symbol":"005380","company_name":"현대차","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_VALUEUP_VOLUME_MIX_CAPITAL_RETURN_BRIDGE_VS_SUPPLIER_OPERATING_LEVERAGE_HIGH_MAE","sector":"mobility / OEM / value-up / volume mix / capital return","primary_archetype":"OEM volume-mix and capital-return rerating","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":188700,"evidence_available_at_that_date":"source_proxy_only historical evidence family; non-price bridge noted but URL repair pending","evidence_source":"source_proxy_only:evidence_url_pending:C29_volume_mix_margin_capital_return_or_supplier_operating_leverage","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.31,"MFE_90D_pct":47.06,"MFE_180D_pct":58.72,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.76,"MAE_90D_pct":-2.76,"MAE_180D_pct":-2.76,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-27.71,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"oem_valueup_volume_mix_capital_return_stage2_actionable_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_005380_2024-01-25_188700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C29_000270_STAGE2A_20240125","case_id":"C29_R9L100_000270_20240125","symbol":"000270","company_name":"기아","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_VALUEUP_VOLUME_MIX_CAPITAL_RETURN_BRIDGE_VS_SUPPLIER_OPERATING_LEVERAGE_HIGH_MAE","sector":"mobility / OEM / mix margin / capital return","primary_archetype":"OEM mix margin and shareholder return","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":93000,"evidence_available_at_that_date":"source_proxy_only historical evidence family; non-price bridge noted but URL repair pending","evidence_source":"source_proxy_only:evidence_url_pending:C29_volume_mix_margin_capital_return_or_supplier_operating_leverage","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":41.61,"MFE_90D_pct":45.16,"MFE_180D_pct":45.16,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.42,"MAE_90D_pct":-7.42,"MAE_180D_pct":-7.42,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":135000,"drawdown_after_peak_pct":-29.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"kia_oem_mix_margin_capital_return_stage2_actionable_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_000270_2024-01-25_93000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C29_011210_STAGE2_20240125","case_id":"C29_R9L100_011210_20240125","symbol":"011210","company_name":"현대위아","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_VALUEUP_VOLUME_MIX_CAPITAL_RETURN_BRIDGE_VS_SUPPLIER_OPERATING_LEVERAGE_HIGH_MAE","sector":"mobility / supplier / operating leverage / high MAE","primary_archetype":"supplier label without independent operating leverage bridge","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":58000,"evidence_available_at_that_date":"source_proxy_only historical evidence family; non-price bridge noted but URL repair pending","evidence_source":"source_proxy_only:evidence_url_pending:C29_volume_mix_margin_capital_return_or_supplier_operating_leverage","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011210/2024.csv","profile_path":"atlas/symbol_profiles/011/011210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.52,"MFE_90D_pct":15.52,"MFE_180D_pct":15.52,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.17,"MAE_90D_pct":-5.17,"MAE_180D_pct":-21.64,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":67000,"drawdown_after_peak_pct":-32.16,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"supplier_operating_leverage_label_false_positive_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_011210_2024-01-25_58000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C29_204320_STAGE4B_20240605","case_id":"C29_R9L100_204320_20240605","symbol":"204320","company_name":"HL만도","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_VALUEUP_VOLUME_MIX_CAPITAL_RETURN_BRIDGE_VS_SUPPLIER_OPERATING_LEVERAGE_HIGH_MAE","sector":"mobility / supplier / post-spike 4B overlay","primary_archetype":"supplier event spike 4B watch","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-06-05","entry_date":"2024-06-05","entry_price":49600,"evidence_available_at_that_date":"source_proxy_only historical evidence family; non-price bridge noted but URL repair pending","evidence_source":"source_proxy_only:evidence_url_pending:C29_volume_mix_margin_capital_return_or_supplier_operating_leverage","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.81,"MFE_90D_pct":0.81,"MFE_180D_pct":0.81,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.04,"MAE_90D_pct":-36.19,"MAE_180D_pct":-36.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-05","peak_price":50000,"drawdown_after_peak_pct":-36.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"supplier_post_spike_4b_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_204320_2024-06-05_49600","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L100_005380_20240125","trigger_id":"T_C29_005380_STAGE2A_20240125","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","customer_quality_score","valuation_repricing_score"],"component_delta_explanation":"C29 OEM value-up requires capital return plus mix/margin bridge; the path aligned with high MFE and shallow MAE","MFE_90D_pct":47.06,"MAE_90D_pct":-2.76,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L100_000270_20240125","trigger_id":"T_C29_000270_STAGE2A_20240125","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":5,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":6,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":75,"stage_label_after":"Stage3-Yellow watch","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score"],"component_delta_explanation":"OEM mix/capital return bridge deserved early Stage2-Actionable but Green still waits for confirmed revision and durability","MFE_90D_pct":45.16,"MAE_90D_pct":-7.42,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L100_011210_20240125","trigger_id":"T_C29_011210_STAGE2_20240125","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":64,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":55,"stage_label_after":"Stage1/Stage2-watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"supplier operating leverage cannot be inherited from OEM value-up; high MAE shows false-positive risk","MFE_90D_pct":15.52,"MAE_90D_pct":-5.17,"score_return_alignment_label":"demotion_aligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L100_204320_20240605","trigger_id":"T_C29_204320_STAGE4B_20240605","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":67,"stage_label_before":"Stage2 / local 4B watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":52,"stage_label_after":"Stage4B overlay / no new Stage2 promotion","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"post-spike supplier rerating had no further MFE and large MAE; price extension should be 4B overlay, not Stage2 reinforcement","MFE_90D_pct":0.81,"MAE_90D_pct":-36.19,"score_return_alignment_label":"4B_guard_aligned","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","current_profile_4B_too_late","supplier_high_MAE_guardrail"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"Priority 0 C29 shortage fill; 4 new symbols; 4 trigger families; 2 positives; 2 counterexamples; 1 4B overlay"}
```

## 26. Deferred Coding Agent Handoff Prompt

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

## 27. Next Round State

```text
completed_round = R9
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` was used as the execution procedure.
- `docs/core/V12_Research_No_Repeat_Index.md` was used only as the duplicate/coverage ledger.
- `Songdaiki/stock-web` manifest/schema/profile/shard paths were used for price-source validation and OHLC path calculations.
- Evidence URLs are deliberately marked `source_proxy_only / evidence_url_pending`; a later repair loop can add company IR, DART, or dated market source URLs.
- This is historical calibration research only and contains no investment recommendation language.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 3
new_weight_evidence_candidate_count: 3
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
