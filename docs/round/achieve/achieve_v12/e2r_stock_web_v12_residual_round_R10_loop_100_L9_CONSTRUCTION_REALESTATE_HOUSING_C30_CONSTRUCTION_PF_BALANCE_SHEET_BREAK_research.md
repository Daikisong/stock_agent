# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
schema_family = v12_sector_archetype_residual
selected_round = R10
selected_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = PF_BALANCE_SHEET_REPAIR_AND_HOUSING_REBOUND_BRIDGE_VS_CONSTRUCTION_LABEL_WEAK_BRIDGE_HIGH_MAE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

The current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. This loop does not re-propose global Stage2/4B rules. It tests whether C30 construction/PF balance-sheet break needs a canonical-specific bridge: **PF/liquidity vocabulary is not enough; usable Stage2 needs balance-sheet repair, margin/cash conversion, or hard evidence that the risk discount is resolving.**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R10 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK |
| fine_archetype_id | PF_BALANCE_SHEET_REPAIR_AND_HOUSING_REBOUND_BRIDGE_VS_CONSTRUCTION_LABEL_WEAK_BRIDGE_HIGH_MAE |
| scope logic | C30 maps to R10/L9. Scope consistency passes. |

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` marks C30 as Priority 0 with 3 representative rows and top covered symbols `009410`, `034300`, `183190`. This loop avoids those and uses three new symbols: `294870`, `006360`, `047040`.

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected representative row intentionally repeats an existing C30 top-covered symbol or exact trigger group.

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

All representative entries have stock-web tradable rows, 180D forward windows before manifest max date, positive OHLCV, and no 180D corporate-action contamination based on profile candidate dates. HDC had a historical corporate-action candidate in 2020, GS건설 in 2014, and 대우건설 in 2011; none overlaps the 2024 entry-to-180D windows used here.

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | compression logic |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | housing_developer_repair_rebound_bridge | permit Stage2-Actionable only when price strength coincides with repair/rebound and plausible financial bridge |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | large_builder_balance_sheet_discount_reversal | strong MFE is valid but remains Stage2/Yellow until margin/cash repair is visible |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | generic_construction_label_false_positive | construction/PF vocabulary without cash/margin proof should be Watch or failed-rerating counterexample |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | local_4b_after_repair_vertical_move | local 4B watch can be useful after a vertical repair move, but price-only local peaks are not full 4B |

## 7. Case Selection Summary

| case_id | symbol | name | role | trigger | entry | price | MFE90 | MAE90 | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C30_R10L100_294870_20240126 | 294870 | HDC현대산업개발 | structural_success | Stage2-Actionable | 2024-01-26 | 17530 | 18.37 | -8.33 | current_profile_too_late |
| C30_R10L100_006360_20240403 | 006360 | GS건설 | stage2_promote_candidate | Stage2-Actionable | 2024-04-03 | 15630 | 30.52 | -5.31 | current_profile_too_late |
| C30_R10L100_047040_20240403 | 047040 | 대우건설 | failed_rerating | Stage2 | 2024-04-03 | 3805 | 4.07 | -7.49 | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 1 |
| 4C_case_count | 0 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 4 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| new_symbol_count | 3 |
| new_trigger_family_count | 4 |

## 9. Evidence Source Map

| case_id | evidence family | evidence source status |
|---|---|---|
| C30_R10L100_294870_20240126 | housing repair rebound / risk-discount reversal | source_proxy_only |
| C30_R10L100_006360_20240403 | large builder balance-sheet discount repair / margin bridge watch | source_proxy_only |
| C30_R10L100_047040_20240403 | generic construction label without sufficient margin/cash bridge | source_proxy_only |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path |
|---|---|---|
| 294870 | atlas/symbol_profiles/294/294870.json | atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv |
| 006360 | atlas/symbol_profiles/006/006360.json | atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv |
| 047040 | atlas/symbol_profiles/047/047040.json | atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | agg |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C30_R10L100_294870_20240126_Stage2_Actionable | 294870 | Stage2-Actionable | 2024-01-26 | 17530 | 18.37 | -2.11 | 18.37 | -8.33 | 60.87 | -8.33 | representative |
| C30_R10L100_006360_20240403_Stage2_Actionable | 006360 | Stage2-Actionable | 2024-04-03 | 15630 | 5.89 | -4.86 | 30.52 | -5.31 | 39.16 | -5.31 | representative |
| C30_R10L100_047040_20240403_Stage2 | 047040 | Stage2 | 2024-04-03 | 3805 | 1.58 | -2.5 | 4.07 | -7.49 | 6.44 | -14.32 | representative |
| C30_R10L100_294870_20240826_Stage4B | 294870 | Stage4B | 2024-08-26 | 26700 | 5.62 | -15.54 | 5.62 | -24.16 | 8.99 | -24.16 | 4B_overlay_only |


## 12. Trigger-Level OHLC Backtest Tables

The representative trigger rows above use the canonical MFE/MAE field names: `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`.

## 13. Current Calibrated Profile Stress Test

1. Current profile would likely be **too late** on 294870 and 006360 if it waited for full confirmed construction-cycle recovery.
2. Current profile would likely be **false positive** on 047040 if it accepted generic construction/PF vocabulary without a fresh cash/margin bridge.
3. Existing Stage2 bonus is useful only with repair evidence; it is too loose if applied to construction label alone.
4. Yellow threshold 75 should remain strict because C30 has high drawdown risk.
5. Green threshold/revision should not be loosened.
6. Price-only blowoff guard remains correct.
7. Full 4B non-price requirement remains correct; HDC 2024-08-26 is local 4B watch, not necessarily full 4B.
8. Hard 4C routing is not directly tested in this loop.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is created. Green lateness ratio is therefore `not_applicable`. The loop is about Stage2/Actionable filtering and local 4B watch timing rather than Green unlock.

## 15. 4B Local vs Full-window Timing Audit

| case | local 4B trigger | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| 294870 | 2024-08-26 | 0.94 | 0.94 | good local 4B watch; non-price evidence needed for full 4B |

## 16. 4C Protection Audit

No hard Stage4C row is promoted. `four_c_protection_label = thesis_break_watch_only` for the local 4B overlay.

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`

L9 construction/PF cases should require one of the following before Stage2-Actionable:

```text
balance_sheet_repair_evidence
cash_conversion_or_working_capital_improvement
margin_bridge_or_loss_normalization
credible risk-discount reversal with clean 30/90/180D path
```

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

Proposed C30 rule:

```text
C30_PF_BALANCE_SHEET_REPAIR_BRIDGE_REQUIRED:
  - Generic PF/construction label alone cannot promote Stage2.
  - Stage2-Actionable requires balance-sheet repair, margin/cash bridge, or clear working-capital risk reduction.
  - Local price overheat after rebound can become 4B watch, but full 4B needs non-price evidence.
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | missed structural count | verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 current proxy | 3 | 17.65 | -7.04 | 0.33 | 2 | too blunt for C30 |
| P2 canonical C30 bridge | 3 | 17.65 | -7.04 | 0.00 | 0 | better alignment by promoting only repair-bridge cases |
| P3 counterexample guard | 3 | 17.65 | -7.04 | 0.00 | 1 | safest but may miss early rebound |

## 20. Score-Return Alignment Matrix

| case | current verdict | after-profile adjustment | alignment |
|---|---|---|---|
| 294870 | current_profile_too_late | promote to Stage2-Actionable with repair bridge | improves |
| 006360 | current_profile_too_late | promote to Stage2-Actionable with margin/cash watch | improves |
| 047040 | current_profile_false_positive | downgrade to Watch until margin/cash evidence | improves |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_BALANCE_SHEET_REPAIR_AND_HOUSING_REBOUND_BRIDGE_VS_CONSTRUCTION_LABEL_WEAK_BRIDGE_HIGH_MAE | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 | 3 | true | true | C30 3 -> 6 if accepted; need 24 to 30 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_too_late | current_profile_false_positive | current_profile_4B_too_late
new_axis_proposed: C30_PF_BALANCE_SHEET_REPAIR_BRIDGE_REQUIRED
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min | stage3_green_revision_min | hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 3 new independent cases, 1 counterexample, and 3 residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

## 23. Validation Scope / Non-Validation Scope

Validation scope:
- Stock-web historical OHLC path.
- C30 canonical-specific Stage2 bridge.
- C30 local 4B watch timing.

Non-validation scope:
- Production scoring patch execution.
- Live candidate recommendation.
- Current market scan.
- Final investment conclusion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_PF_BALANCE_SHEET_REPAIR_BRIDGE_REQUIRED,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 needs repair/cash/margin bridge before Stage2-Actionable","reduces 047040 false positive while preserving 294870/006360 early rebound","C30_R10L100_294870_20240126_Stage2_Actionable|C30_R10L100_006360_20240403_Stage2_Actionable|C30_R10L100_047040_20240403_Stage2",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,price_only_local_4b_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"HDC local 4B watch useful after vertical move but non-price evidence needed for full 4B","keeps full_4b_requires_non_price_evidence intact","C30_R10L100_294870_20240826_Stage4B",1,0,0,low,guardrail_shadow_only,"overlay row only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C30_R10L100_294870_20240126","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_REPAIR_AND_HOUSING_REBOUND_BRIDGE_VS_CONSTRUCTION_LABEL_WEAK_BRIDGE_HIGH_MAE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"housing_developer_repair_rebound_positive"}
{"row_type":"case","case_id":"C30_R10L100_006360_20240403","symbol":"006360","company_name":"GS건설","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_REPAIR_AND_HOUSING_REBOUND_BRIDGE_VS_CONSTRUCTION_LABEL_WEAK_BRIDGE_HIGH_MAE","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"large_builder_repair_bounce_needs_nonprice_bridge"}
{"row_type":"case","case_id":"C30_R10L100_047040_20240403","symbol":"047040","company_name":"대우건설","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_REPAIR_AND_HOUSING_REBOUND_BRIDGE_VS_CONSTRUCTION_LABEL_WEAK_BRIDGE_HIGH_MAE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_risk_confirmed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"construction_label_without_clear_margin_cash_bridge_failed_rerating"}
{"row_type":"trigger","trigger_id":"C30_R10L100_294870_20240126_Stage2_Actionable","case_id":"C30_R10L100_294870_20240126","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_REPAIR_AND_HOUSING_REBOUND_BRIDGE_VS_CONSTRUCTION_LABEL_WEAK_BRIDGE_HIGH_MAE","sector":"construction / real estate / housing / PF liquidity / balance-sheet repair","primary_archetype":"PF balance-sheet repair vs construction label false positive","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-26","evidence_available_at_that_date":"source_proxy_only: housing developer repair/rebound; stock-web OHLC confirms early strength before broader C30 rerating","evidence_source":"source_proxy_only: housing developer repair/rebound; stock-web OHLC confirms early strength before broader C30 rerating","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-26","entry_price":17530,"MFE_30D_pct":18.37,"MFE_90D_pct":18.37,"MFE_180D_pct":60.87,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.11,"MAE_90D_pct":-8.33,"MAE_180D_pct":-8.33,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":28200,"drawdown_after_peak_pct":-28.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":"not_applicable","trigger_outcome_label":"housing_developer_repair_rebound_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_R10L100_294870_20240126","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C30_R10L100_006360_20240403_Stage2_Actionable","case_id":"C30_R10L100_006360_20240403","symbol":"006360","company_name":"GS건설","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_REPAIR_AND_HOUSING_REBOUND_BRIDGE_VS_CONSTRUCTION_LABEL_WEAK_BRIDGE_HIGH_MAE","sector":"construction / real estate / housing / PF liquidity / balance-sheet repair","primary_archetype":"PF balance-sheet repair vs construction label false positive","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-03","evidence_available_at_that_date":"source_proxy_only: construction repair/balance-sheet risk discount rebound; price path validates but needs margin/cash proof","evidence_source":"source_proxy_only: construction repair/balance-sheet risk discount rebound; price path validates but needs margin/cash proof","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-03","entry_price":15630,"MFE_30D_pct":5.89,"MFE_90D_pct":30.52,"MFE_180D_pct":39.16,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.86,"MAE_90D_pct":-5.31,"MAE_180D_pct":-5.31,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":21750,"drawdown_after_peak_pct":-19.4,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":"not_applicable","trigger_outcome_label":"large_builder_repair_bounce_needs_nonprice_bridge","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_R10L100_006360_20240403","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C30_R10L100_047040_20240403_Stage2","case_id":"C30_R10L100_047040_20240403","symbol":"047040","company_name":"대우건설","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_REPAIR_AND_HOUSING_REBOUND_BRIDGE_VS_CONSTRUCTION_LABEL_WEAK_BRIDGE_HIGH_MAE","sector":"construction / real estate / housing / PF liquidity / balance-sheet repair","primary_archetype":"PF balance-sheet repair vs construction label false positive","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-04-03","evidence_available_at_that_date":"source_proxy_only: generic construction/PF recovery label without enough new margin/cash conversion evidence","evidence_source":"source_proxy_only: generic construction/PF recovery label without enough new margin/cash conversion evidence","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-03","entry_price":3805,"MFE_30D_pct":1.58,"MFE_90D_pct":4.07,"MFE_180D_pct":6.44,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.5,"MAE_90D_pct":-7.49,"MAE_180D_pct":-14.32,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-12","peak_price":4050,"drawdown_after_peak_pct":-18.1,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":"not_applicable","trigger_outcome_label":"construction_label_without_clear_margin_cash_bridge_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_R10L100_047040_20240403","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C30_R10L100_294870_20240826_Stage4B","case_id":"C30_R10L100_294870_20240126","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_REPAIR_AND_HOUSING_REBOUND_BRIDGE_VS_CONSTRUCTION_LABEL_WEAK_BRIDGE_HIGH_MAE","sector":"construction / real estate / housing / PF liquidity / balance-sheet repair","primary_archetype":"local 4B after housing rebound","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-08-26","evidence_available_at_that_date":"price strength had moved far ahead of confirmed multi-quarter cash/working-capital proof; non-price 4B evidence incomplete","evidence_source":"source_proxy_only: stock-web price path and local overheat overlay; not a full thesis break","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-26","entry_price":26700,"MFE_30D_pct":5.62,"MFE_90D_pct":5.62,"MFE_180D_pct":8.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.54,"MAE_90D_pct":-24.16,"MAE_180D_pct":-24.16,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":28200,"drawdown_after_peak_pct":-28.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_local_4B_watch_but_nonprice_evidence_needed_for_full_4B","four_b_evidence_type":["positioning_overheat","price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"housing_rebound_local_4b_watch_after_vertical_move","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C30_R10L100_294870_20240826_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same symbol as representative HDC case but different trigger family and 4B timing audit","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L100_294870_20240126","trigger_id":"C30_R10L100_294870_20240126_Stage2_Actionable","symbol":"294870","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":64,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":71,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C30 needs proof of cash/margin/working-capital repair; generic construction label is downgraded if the bridge is missing.","MFE_90D_pct":18.37,"MAE_90D_pct":-8.33,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L100_006360_20240403","trigger_id":"C30_R10L100_006360_20240403_Stage2_Actionable","symbol":"006360","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":64,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":3,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":71,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C30 needs proof of cash/margin/working-capital repair; generic construction label is downgraded if the bridge is missing.","MFE_90D_pct":30.52,"MAE_90D_pct":-5.31,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L100_047040_20240403","trigger_id":"C30_R10L100_047040_20240403_Stage2","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":6,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":66,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":7,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":7},"weighted_score_after":58,"stage_label_after":"Stage1/Watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"C30 needs proof of cash/margin/working-capital repair; generic construction label is downgraded if the bridge is missing.","MFE_90D_pct":4.07,"MAE_90D_pct":-7.49,"score_return_alignment_label":"false_positive_block_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R10","loop":"100","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 3
new_weight_evidence_candidate_count: 3
guardrail_candidate_count: 1
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
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
completed_round = R10
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: docs/core/V12_Research_No_Repeat_Index.md
- price atlas: Songdaiki/stock-web
- manifest max date: 2026-02-20
- This output is historical calibration research, not investment advice and not a live scan.
