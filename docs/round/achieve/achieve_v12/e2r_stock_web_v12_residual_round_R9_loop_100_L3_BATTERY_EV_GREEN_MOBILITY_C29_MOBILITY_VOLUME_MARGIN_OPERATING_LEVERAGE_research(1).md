# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R9
selected_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_OEM_AND_AUTO_PARTS_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_VS_MOBILITY_LABEL_SPIKE
output_file = e2r_stock_web_v12_residual_round_R9_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
```

Already-applied global axes are not re-proposed. This loop tests whether C29 needs a sharper bridge: volume/mix/margin/capital-return proof for OEMs, and a high-MAE guard for post-spike auto-parts mobility labels.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R9 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | AUTO_OEM_AND_AUTO_PARTS_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_VS_MOBILITY_LABEL_SPIKE |
| loop_objective | coverage_gap_fill / counterexample_mining / stage2_actionable_bonus_stress_test / canonical_archetype_compression |

C29 is mapped to R9 / L3 because this run treats mobility and transport as the operative sub-sector, not construction/real-estate.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used:

| metric | value |
|---|---:|
| C29 existing rows | 3 |
| need to 30 | 27 |
| need to 50 | 47 |
| top existing symbols to avoid | 005710, 007860, 033530 |

This run avoids the existing C29 top-covered symbols and uses 000270, 005380, 204320.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

| symbol | profile path | shard path | corporate-action window |
|---|---|---|---|
| 000270 | atlas/symbol_profiles/000/000270.json | atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv | clean_180D_window |
| 005380 | atlas/symbol_profiles/005/005380.json | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | clean_180D_window |
| 204320 | atlas/symbol_profiles/204/204320.json | atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv | clean_180D_window |

## 5. Historical Eligibility Gate

| case_id | entry_date | entry_price | forward_window_trading_days | MFE/MAE 30/90/180 complete | calibration_usable |
|---|---:|---:|---:|---|---|
| C29_R9L100_000270_KIA_VALUEUP_MIX_MARGIN | 2024-01-26 | 94400 | 180 | yes | true |
| C29_R9L100_005380_HYUNDAI_VALUEUP_MIX_MARGIN | 2024-01-26 | 187300 | 180 | yes | true |
| C29_R9L100_204320_HLMANDO_POST_SPIKE_WEAK_BRIDGE | 2024-06-07 | 47550 | 180 | yes | true |

## 6. Canonical Archetype Compression Map

| fine / deep sub-archetype | canonical_archetype_id | compression note |
|---|---|---|
| AUTO_OEM_RECORD_MARGIN_SHAREHOLDER_RETURN_VOLUME_MIX_BRIDGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | OEM rerating works when volume/mix/margin and capital return walk together. |
| AUTO_OEM_GLOBAL_MIX_HYBRID_MARGIN_CAPITAL_RETURN_BRIDGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Global OEM mix/ASP/FX/margin and value-up can justify earlier Stage2. |
| AUTO_PARTS_ADAS_MOBILITY_LABEL_POST_SPIKE_WEAK_VOLUME_MARGIN_BRIDGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Parts mobility label without margin bridge is high-MAE false positive. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_type | entry_date | MFE_90D | MAE_90D | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| C29_R9L100_000270_KIA_VALUEUP_MIX_MARGIN | 000270 | 기아 | structural_success | Stage2-Actionable | 2024-01-26 | 39.5 | -1.8 | current_profile_correct |
| C29_R9L100_005380_HYUNDAI_VALUEUP_MIX_MARGIN | 005380 | 현대차 | structural_success | Stage2-Actionable | 2024-01-26 | 48.2 | -0.4 | current_profile_too_late |
| C29_R9L100_204320_HLMANDO_POST_SPIKE_WEAK_BRIDGE | 204320 | HL만도 | failed_rerating | Stage2-Actionable | 2024-06-07 | 2.8 | -35.1 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
calibration_usable_case_count = 3
```

The split is intentionally asymmetric: C29 had only 3 rows in the index, so this run prioritizes two clean OEM positives plus one hard false-positive/high-MAE guard.

## 9. Evidence Source Map

| symbol | evidence source status | evidence summary |
|---:|---|---|
| 000270 | source_proxy_only / URL pending | 2023 result and shareholder-return/mix-margin evidence available at trigger date. |
| 005380 | source_proxy_only / URL pending | 2023 result, global mix, hybrid/US margin, capital-return/value-up bridge. |
| 204320 | source_proxy_only / URL pending | Post-spike mobility/ADAS label had price momentum but weak confirmed margin/volume bridge. |

## 10. Price Data Source Map

| symbol | entry row source | 30/90/180 path source |
|---:|---|---|
| 000270 | atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv | 2024 tradable shard |
| 005380 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | 2024 tradable shard |
| 204320 | atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv + 2025.csv | 2024/2025 tradable shard |

## 11. Case-by-Case Trigger Grid

| case_id | trigger_id | trigger_type | trigger_date | entry_date | entry_price | trigger_outcome_label |
|---|---|---|---:|---:|---:|---|
| C29_R9L100_000270_KIA_VALUEUP_MIX_MARGIN | TRG_C29_R9L100_000270_STAGE2A_20240125 | Stage2-Actionable | 2024-01-25 | 2024-01-26 | 94400 | oem_volume_mix_margin_capital_return_positive |
| C29_R9L100_005380_HYUNDAI_VALUEUP_MIX_MARGIN | TRG_C29_R9L100_005380_STAGE2A_20240125 | Stage2-Actionable | 2024-01-25 | 2024-01-26 | 187300 | global_oem_mix_margin_valueup_positive |
| C29_R9L100_204320_HLMANDO_POST_SPIKE_WEAK_BRIDGE | TRG_C29_R9L100_204320_STAGE2_FALSE_20240605 | Stage2-Actionable | 2024-06-05 | 2024-06-07 | 47550 | auto_parts_mobility_label_high_mae_false_positive |
| C29_R9L100_204320_HLMANDO_POST_SPIKE_WEAK_BRIDGE | TRG_C29_R9L100_204320_STAGE4B_OVERLAY_20240607 | Stage4B | 2024-06-07 | 2024-06-07 | 47550 | price_only_local_4b_watch_good_guard |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 000270 | 2024-01-26 | 94400 | 39.5 | -1.8 | 39.5 | -1.8 | 43.0 | -4.7 | 2024-06-19 | 135000 |
| 005380 | 2024-01-26 | 187300 | 39.3 | -0.4 | 48.2 | -0.4 | 59.9 | -0.4 | 2024-06-28 | 299500 |
| 204320 | 2024-06-07 | 47550 | 2.8 | -17.0 | 2.8 | -35.1 | 2.8 | -35.1 | 2024-06-12 | 48900 |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | interpretation |
|---|---|---|
| 000270 | current_profile_correct | Stage2 bridge works when OEM margin/volume and capital return are explicit. |
| 005380 | current_profile_too_late | Strict Green is fine, but Stage2/Yellows should not wait for price to do all the work when margin + value-up bridge is public. |
| 204320 | current_profile_false_positive | Mobility/ADAS label plus short relative strength is insufficient without volume/mix/margin conversion. |

## 14. Stage2 / Yellow / Green Comparison

C29 should not relax Stage3-Green globally. The signal is earlier Stage2/Yellows when OEM mix/margin/capital return is present, while blocking parts-name mobility labels that lack conversion evidence.

## 15. 4B Local vs Full-window Timing Audit

| symbol | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 204320 | 1.0 | 1.0 | Price-only post-spike region should be watch/guard, not positive Stage2 promotion. |

## 16. 4C Protection Audit

No hard 4C is proposed. HL만도 is a Stage2 false positive + 4B watch case, not a hard thesis break.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = only one canonical archetype in one large sector was tested; no global or sector-wide relaxation.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
scope = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

Candidate rule:

```text
For C29, Stage2-Actionable can be retained or strengthened only when at least two of the following exist:
1. volume or mix improvement,
2. margin bridge / ASP or incentive discipline,
3. capital return / ROE or valuation rerating evidence,
4. revision or financial visibility.

If the row is only a mobility/ADAS/auto-parts label plus a price spike, route to Stage1/weak-watch or Stage4B-watch.
```

## 19. Before / After Backtest Comparison

| profile | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | score_return_alignment |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 30.2 | -12.4 | 0.33 | mixed |
| P2 C29 canonical guard profile | 3 | 43.9 for accepted OEMs / 2.8 rejected label | -1.1 for accepted OEMs / -35.1 rejected label | 0.00 after guard | improved |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| C29_R9L100_000270_KIA_VALUEUP_MIX_MARGIN | 78 | Stage3-Yellow | 84 | Stage3-Yellow | 39.5 | -1.8 | aligned_positive |
| C29_R9L100_005380_HYUNDAI_VALUEUP_MIX_MARGIN | 78 | Stage3-Yellow | 84 | Stage3-Yellow | 48.2 | -0.4 | aligned_positive |
| C29_R9L100_204320_HLMANDO_POST_SPIKE_WEAK_BRIDGE | 67 | Stage2-Actionable | 58 | Stage1/weak-watch | 2.8 | -35.1 | false_positive_guard_needed |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_OEM_AND_AUTO_PARTS_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_BRIDGE_VS_MOBILITY_LABEL_SPIKE | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 | 2 | false | true | 24 to 30 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_too_late_for_oem_margin_valueup
  - post_spike_mobility_label_false_positive
new_axis_proposed: null
existing_axis_strengthened:
  - C29_stage2_required_volume_mix_margin_bridge
  - C29_local_4b_watch_guard_for_price_only_mobility_label
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical trigger-level calibration only
- Stock-Web tradable_raw OHLC only
- 30/90/180D MFE/MAE fields complete
- C29 canonical guard candidate only
```

Non-validation scope:

```text
- No live candidate scan
- No current stock recommendation
- No production code patch
- No brokerage/API usage
- No global Green relaxation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Require volume/mix/margin or capital-return bridge for C29 Stage2","rejects 204320 false positive while retaining 000270/005380 OEM positives","TRG_C29_R9L100_000270_STAGE2A_20240125|TRG_C29_R9L100_005380_STAGE2A_20240125|TRG_C29_R9L100_204320_STAGE2_FALSE_20240605",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Price-only mobility/ADAS label after spike should be 4B watch not Stage2 promotion","204320 avoids high-MAE false positive","TRG_C29_R9L100_204320_STAGE4B_OVERLAY_20240607",1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C29_R9L100_000270_KIA_VALUEUP_MIX_MARGIN","symbol":"000270","company_name":"기아","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_RECORD_MARGIN_SHAREHOLDER_RETURN_VOLUME_MIX_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_C29_R9L100_000270_STAGE2A_20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2023 실적/IR 및 주주환원 발표 source-proxy: record profitability, ASP/mix, shareholder return, no pure price-only event."}
{"row_type":"case","case_id":"C29_R9L100_005380_HYUNDAI_VALUEUP_MIX_MARGIN","symbol":"005380","company_name":"현대차","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_GLOBAL_MIX_HYBRID_MARGIN_CAPITAL_RETURN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_C29_R9L100_005380_STAGE2A_20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"2023/4Q result and capital-return/value-up source-proxy: mix, hybrid/US margin, shareholder return, global volume durability."}
{"row_type":"case","case_id":"C29_R9L100_204320_HLMANDO_POST_SPIKE_WEAK_BRIDGE","symbol":"204320","company_name":"HL만도","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_ADAS_MOBILITY_LABEL_POST_SPIKE_WEAK_VOLUME_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C29_R9L100_204320_STAGE2_FALSE_20240605","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_without_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2024 mobility/ADAS parts label and short price spike source-proxy, but no confirmed volume/mix/margin operating leverage bridge at entry."}
{"row_type":"trigger","trigger_id":"TRG_C29_R9L100_000270_STAGE2A_20240125","case_id":"C29_R9L100_000270_KIA_VALUEUP_MIX_MARGIN","symbol":"000270","company_name":"기아","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_RECORD_MARGIN_SHAREHOLDER_RETURN_VOLUME_MIX_BRIDGE","sector":"mobility / auto OEM / auto parts / volume / mix / margin / operating leverage / capital return","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-26","entry_price":94400,"evidence_available_at_that_date":"2023 실적/IR 및 주주환원 발표 source-proxy: record profitability, ASP/mix, shareholder return, no pure price-only event.","evidence_source":"source_proxy: company IR/earnings disclosure and contemporaneous market evidence; URL verification pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":39.5,"MFE_90D_pct":39.5,"MFE_180D_pct":43.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.8,"MAE_90D_pct":-1.8,"MAE_180D_pct":-4.7,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":135000,"drawdown_after_peak_pct":-33.3,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"oem_volume_mix_margin_capital_return_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_R9L100_000270_KIA_VALUEUP_MIX_MARGIN|2024-01-26|94400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C29_R9L100_005380_STAGE2A_20240125","case_id":"C29_R9L100_005380_HYUNDAI_VALUEUP_MIX_MARGIN","symbol":"005380","company_name":"현대차","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_OEM_GLOBAL_MIX_HYBRID_MARGIN_CAPITAL_RETURN_BRIDGE","sector":"mobility / auto OEM / auto parts / volume / mix / margin / operating leverage / capital return","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-26","entry_price":187300,"evidence_available_at_that_date":"2023/4Q result and capital-return/value-up source-proxy: mix, hybrid/US margin, shareholder return, global volume durability.","evidence_source":"source_proxy: company IR/earnings disclosure and contemporaneous market evidence; URL verification pending","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":39.3,"MFE_90D_pct":48.2,"MFE_180D_pct":59.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.4,"MAE_90D_pct":-0.4,"MAE_180D_pct":-0.4,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-21.4,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"global_oem_mix_margin_valueup_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_R9L100_005380_HYUNDAI_VALUEUP_MIX_MARGIN|2024-01-26|187300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C29_R9L100_204320_STAGE2_FALSE_20240605","case_id":"C29_R9L100_204320_HLMANDO_POST_SPIKE_WEAK_BRIDGE","symbol":"204320","company_name":"HL만도","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_ADAS_MOBILITY_LABEL_POST_SPIKE_WEAK_VOLUME_MARGIN_BRIDGE","sector":"mobility / auto OEM / auto parts / volume / mix / margin / operating leverage / capital return","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-05","entry_date":"2024-06-07","entry_price":47550,"evidence_available_at_that_date":"2024 mobility/ADAS parts label and short price spike source-proxy, but no confirmed volume/mix/margin operating leverage bridge at entry.","evidence_source":"source_proxy: company IR/earnings disclosure and contemporaneous market evidence; URL verification pending","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.8,"MFE_90D_pct":2.8,"MFE_180D_pct":2.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.0,"MAE_90D_pct":-35.1,"MAE_180D_pct":-35.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-12","peak_price":48900,"drawdown_after_peak_pct":-36.9,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_should_be_watch_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"auto_parts_mobility_label_high_mae_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_R9L100_204320_HLMANDO_POST_SPIKE_WEAK_BRIDGE|2024-06-07|47550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C29_R9L100_204320_STAGE4B_OVERLAY_20240607","case_id":"C29_R9L100_204320_HLMANDO_POST_SPIKE_WEAK_BRIDGE","symbol":"204320","company_name":"HL만도","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_ADAS_MOBILITY_LABEL_POST_SPIKE_WEAK_VOLUME_MARGIN_BRIDGE","sector":"mobility / auto OEM / auto parts / volume / mix / margin / operating leverage / capital return","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-06-05","entry_date":"2024-06-07","entry_price":47550,"evidence_available_at_that_date":"2024 mobility/ADAS parts label and short price spike source-proxy, but no confirmed volume/mix/margin operating leverage bridge at entry.","evidence_source":"source_proxy: company IR/earnings disclosure and contemporaneous market evidence; URL verification pending","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.8,"MFE_90D_pct":2.8,"MFE_180D_pct":2.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.0,"MAE_90D_pct":-35.1,"MAE_180D_pct":-35.1,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-12","peak_price":48900,"drawdown_after_peak_pct":-36.9,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_watch_guard_after_local_spike","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_only_local_4b_watch_good_guard","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_R9L100_204320_HLMANDO_POST_SPIKE_WEAK_BRIDGE|2024-06-07|47550","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L100_000270_KIA_VALUEUP_MIX_MARGIN","trigger_id":"TRG_C29_R9L100_000270_STAGE2A_20240125","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":12,"revision_score":13,"relative_strength_score":12,"customer_quality_score":10,"policy_or_regulatory_score":4,"valuation_repricing_score":12,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":15,"relative_strength_score":10,"customer_quality_score":12,"policy_or_regulatory_score":5,"valuation_repricing_score":13,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C29 should reward volume/mix/margin/capital-return bridge, but penalize post-spike mobility label without margin or order conversion.","MFE_90D_pct":39.5,"MAE_90D_pct":-1.8,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L100_005380_HYUNDAI_VALUEUP_MIX_MARGIN","trigger_id":"TRG_C29_R9L100_005380_STAGE2A_20240125","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":12,"revision_score":13,"relative_strength_score":12,"customer_quality_score":10,"policy_or_regulatory_score":4,"valuation_repricing_score":12,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":14,"revision_score":15,"relative_strength_score":10,"customer_quality_score":12,"policy_or_regulatory_score":5,"valuation_repricing_score":13,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C29 should reward volume/mix/margin/capital-return bridge, but penalize post-spike mobility label without margin or order conversion.","MFE_90D_pct":48.2,"MAE_90D_pct":-0.4,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L100_204320_HLMANDO_POST_SPIKE_WEAK_BRIDGE","trigger_id":"TRG_C29_R9L100_204320_STAGE2_FALSE_20240605","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":12,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":16,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage1/weak-watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"C29 should reward volume/mix/margin/capital-return bridge, but penalize post-spike mobility label without margin or order conversion.","MFE_90D_pct":2.8,"MAE_90D_pct":-35.1,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R9","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["post_spike_mobility_label_false_positive","current_profile_too_late_for_oem_margin_valueup"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
next_recommended_archetypes = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Batch Ingest Self-Audit

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
