# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round = R4
scheduled_loop = 71
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = JAPAN_EXPORT_CONTROL_LOCALIZATION_AND_RARE_EARTH_POLICY_SUPPLY_GUARD
output_file = e2r_stock_web_v12_residual_round_R4_loop_71_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
round_schedule_status = valid
round_sector_consistency = pass
research_session = post_calibrated_sector_archetype_residual_research
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
already_applied_axes_tested = stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
```

## 2. Round / Large Sector / Canonical Archetype Scope

This run follows the sequential scheduler after the latest inspected R3 loop-71 registry state.

```text
scheduled_round = R4
scheduled_loop = 71
allowed_large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
computed_next_round = R5
computed_next_loop = 71
```

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot marks C16 as under-covered relative to neighboring R4 archetypes: 7 representative rows, 4 symbols, no 4B/4C cases, and no URL/proxy blockers. Existing visible C16 symbols include 005290, 027580, 047400, and 093370. This loop therefore avoids repeating the exact `canonical_archetype_id + symbol + trigger_type + entry_date` combination and adds two new C16 symbols.

```text
hard_duplicate_check = pass
new_symbol_count = 2
same_archetype_new_symbol_count = 2
reused_case_count = 1
reuse_reason = 005290 reused only as holdout and 4B/full-window audit
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
manifest_path = atlas/manifest.json
manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

## 5. Historical Eligibility Gate

All representative trigger rows use past trigger dates, next/known tradable close entries, 180D forward windows before the manifest max date, and clean 180D corporate-action windows.

## 6. Canonical Archetype Compression Map

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  -> JAPAN_EXPORT_CONTROL_LOCALIZATION_MARGIN_BRIDGE
  -> JAPAN_EXPORT_CONTROL_PHOTORESIST_LOCALIZATION
  -> RARE_EARTH_POLICY_PRICE_ONLY_THEME_TRAP

Compression rule:
  policy/supply shock can earn Stage2/Yellow credit only when it closes into company-level localization, supply contract, off-take, customer quality, margin bridge, or revision evidence.
  policy-only resource beta stays Stage1/Stage2-watch and cannot become Green.
```

## 7. Case Selection Summary

| case_id | symbol | company | role | new? | entry |
|---|---:|---|---|---|---|
| R4L71_C16_036830_LOCALIZATION_SUPPLY_SUCCESS | 036830 | 솔브레인 | structural_success | true | 2019-07-01 |
| R4L71_C16_005290_LOCALIZATION_REUSED_HOLDOUT | 005290 | 동진쎄미켐 | structural_success holdout | false | 2019-07-01 |
| R4L71_C16_000910_RARE_EARTH_POLICY_PRICE_ONLY_COUNTER | 000910 | 유니온 | failed_rerating / counterexample | true | 2023-07-04 |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
new_independent_case_ratio = 0.67
```

## 9. Evidence Source Map

The evidence labels are historical research proxies for calibration only. They are not live discovery, not investment recommendation, and not production scoring evidence.

## 10. Price Data Source Map

| symbol | profile_path | shard |
|---:|---|---|
| 036830 | atlas/symbol_profiles/036/036830.json | atlas/ohlcv_tradable_by_symbol_year/036/036830/2019.csv |
| 005290 | atlas/symbol_profiles/005/005290.json | atlas/ohlcv_tradable_by_symbol_year/005/005290/2019.csv |
| 000910 | atlas/symbol_profiles/000/000910.json | atlas/ohlcv_tradable_by_symbol_year/000/000910/2023.csv |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | entry | MFE90 | MAE90 | verdict |
|---|---|---:|---:|---:|---|
| TR_R4L71_C16_036830_S2A_20190701 | Stage2-Actionable | 49450 | 83.42 | -5.66 | current_profile_missed_structural |
| TR_R4L71_C16_005290_S2A_20190701 | Stage2-Actionable | 11850 | 68.78 | -11.81 | current_profile_correct |
| TR_R4L71_C16_005290_4B_20191025 | Stage4B | 18800 | 6.38 | -51.33 | current_profile_correct |
| TR_R4L71_C16_000910_FALSE_S2_20230704 | Stage2 | 6440 | 21.74 | -26.71 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | peak_date | peak_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | drawdown_after_peak |
|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 036830 | 2019-07-01 | 49450 | 2020-01-17 | 109300 | 68.05 | 83.42 | 121.03 | -5.66 | -5.66 | -5.66 | -53.06 |
| 005290 | 2019-07-01 | 11850 | 2019-10-25 | 20000 | 58.65 | 68.78 | 68.78 | -11.81 | -11.81 | -22.78 | -54.25 |
| 000910 | 2023-07-04 | 6440 | 2023-07-06 | 7840 | 21.74 | 21.74 | 21.74 | -15.99 | -26.71 | -26.71 | -39.80 |

## 13. Current Calibrated Profile Stress Test

```text
036830 = current_profile_missed_structural
005290 = current_profile_correct
000910 = current_profile_false_positive
```

The residual error is asymmetric: the current profile can still under-credit real strategic localization routes while over-crediting price-only resource policy headlines.

## 14. Stage2 / Yellow / Green Comparison

Green should not be globally loosened. C16 needs a bridge, not a lower Green bar. The proposed shadow rule is a canonical-specific Stage2/Yellow bridge: policy shock must convert into company-level localization/offtake/order/margin evidence.

## 15. 4B Local vs Full-window Timing Audit

005290 validates a full-window 4B overlay after the localization rerating peak. 000910 demonstrates that price-only local peaks should not become full 4B or positive Stage credit.

## 16. 4C Protection Audit

No hard 4C is proposed. C16 remains a Stage2/Yellow bridge and 4B-watch guard problem rather than a hard 4C routing problem.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = L4 resource-policy headlines require non-price supply/margin bridge before Stage2-Actionable credit.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
rule = C16 policy/supply theme is positive only when company-level localization/offtake/order/margin/revision bridge exists; otherwise watch-only.
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false_positive_rate | score_return_alignment |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 57.98 | -14.73 | 0.33 | mixed |
| P2 C16 canonical bridge profile | 3 | 76.10 for positives | -8.74 for positives | 0.00 after guard | improved |
| P3 counterexample guard profile | 1 | 21.74 | -26.71 | reduced to watch-only | improved |

## 20. Score-Return Alignment Matrix

The bridge profile aligns high MFE/low initial MAE for localization cases and downgrades the policy-only resource beta.

## 21. Coverage Matrix

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = JAPAN_EXPORT_CONTROL_LOCALIZATION_AND_RARE_EARTH_POLICY_SUPPLY_GUARD
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
new_independent_case_count = 2
reused_case_count = 1
calibration_usable_trigger_count = 4
representative_trigger_count = 3
current_profile_error_count = 2
sector_rule_candidate = true
canonical_rule_candidate = true
coverage_gap_after_this_loop = C16 still needs more non-overlapping 4C and non-Japan strategic-resource cases
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 2
reused_case_count: 1
reused_case_ids: R4L71_C16_005290_LOCALIZATION_REUSED_HOLDOUT
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 2
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage | stage2_actionable_evidence_bonus | stage3_green_total_min
residual_error_types_found: current_profile_false_positive | current_profile_missed_structural
new_axis_proposed: C16_non_price_supply_bridge_guard
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage inside C16 resource-policy themes
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope is historical trigger-level calibration only. This is not a live scan, not a recommendation, and not a code patch.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C16_non_price_supply_bridge_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"Require company-level localization/offtake/order/margin evidence before Stage2-Actionable/Yellow credit in strategic-resource policy themes.","Positive localization cases show high 90D/180D MFE while policy-only resource beta shows weak durability and high MAE.","TR_R4L71_C16_036830_S2A_20190701|TR_R4L71_C16_005290_S2A_20190701|TR_R4L71_C16_000910_FALSE_S2_20230704",3,2,1,low,canonical_shadow_only,"Not production; post-calibrated residual."
shadow_weight,C16_price_only_resource_theme_guard,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,0,1,+1,"Resource-policy headline without contract/offtake/margin bridge should remain watch-only even when short MFE is positive.","000910 showed MFE but heavy MAE and no durable bridge.","TR_R4L71_C16_000910_FALSE_S2_20230704",1,1,1,low,sector_shadow_only,"Strengthens price-only blowoff guard inside R4 strategic-resource policy cases."
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R4L71_C16_036830_LOCALIZATION_SUPPLY_SUCCESS","symbol":"036830","company_name":"솔브레인","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable / 2019-07-01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 evidence aligned with very strong 90D/180D MFE and limited initial MAE.","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"New symbol for C16 coverage. Treated as localization/specialty-material supply-chain rerating case, not live candidate research."}
{"row_type":"case","case_id":"R4L71_C16_005290_LOCALIZATION_REUSED_HOLDOUT","symbol":"005290","company_name":"동진쎄미켐","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_PHOTORESIST_LOCALIZATION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable / 2019-07-01","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"Existing C16 symbol reused as holdout validation with explicit 4B/full-window drawdown audit.","independent_evidence_weight":0.25,"score_price_alignment":"Positive but reused symbol; still validates supply-localization bridge and later 4B/drawdown path.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Not counted as a fully new case because C16 coverage already includes 005290."}
{"row_type":"case","case_id":"R4L71_C16_000910_RARE_EARTH_POLICY_PRICE_ONLY_COUNTER","symbol":"000910","company_name":"유니온","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_EARTH_POLICY_PRICE_ONLY_THEME_TRAP","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2 false-positive stress / 2023-07-04","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Policy/resource headline created short MFE but weak 90D/180D path and large MAE; current profile should avoid positive Stage promotion.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"New C16 counterexample: policy/resource theme without order/offtake/margin/revision bridge."}
{"row_type":"trigger","trigger_id":"TR_R4L71_C16_036830_S2A_20190701","case_id":"R4L71_C16_036830_LOCALIZATION_SUPPLY_SUCCESS","symbol":"036830","company_name":"솔브레인","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_LOCALIZATION_MARGIN_BRIDGE","sector":"materials / strategic resource / controlled supply chain","primary_archetype":"strategic resource policy supply","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2019-07-01","evidence_available_at_that_date":"Japan export-control localization shock and Korean specialty-material localization route visible by July 2019.","evidence_source":"historical_public_policy_event + company localization supply-chain evidence class","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036830/2019.csv","profile_path":"atlas/symbol_profiles/036/036830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-07-01","entry_price":49450.0,"MFE_30D_pct":68.05,"MFE_90D_pct":83.42,"MFE_180D_pct":121.03,"MFE_1Y_pct":"contaminated_or_unavailable","MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-5.66,"MAE_90D_pct":-5.66,"MAE_180D_pct":-5.66,"MAE_1Y_pct":"contaminated_or_unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-01-17","peak_price":109300.0,"drawdown_after_peak_pct":-53.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":null,"trigger_outcome_label":"structural_success_high_mfe_low_initial_mae","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L71_C16_036830_20190701","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R4L71_C16_005290_S2A_20190701","case_id":"R4L71_C16_005290_LOCALIZATION_REUSED_HOLDOUT","symbol":"005290","company_name":"동진쎄미켐","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_PHOTORESIST_LOCALIZATION","sector":"materials / strategic resource / controlled supply chain","primary_archetype":"strategic resource policy supply","loop_objective":"holdout_validation|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2019-07-01","evidence_available_at_that_date":"Japan export-control localization shock and photoresist/localization route visible by July 2019.","evidence_source":"historical_public_policy_event + localization-supply evidence class","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005290/2019.csv","profile_path":"atlas/symbol_profiles/005/005290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-07-01","entry_price":11850.0,"MFE_30D_pct":58.65,"MFE_90D_pct":68.78,"MFE_180D_pct":68.78,"MFE_1Y_pct":"not_used","MFE_2Y_pct":"not_used","MAE_30D_pct":-11.81,"MAE_90D_pct":-11.81,"MAE_180D_pct":-22.78,"MAE_1Y_pct":"not_used","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2019-10-25","peak_price":20000.0,"drawdown_after_peak_pct":-54.25,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":null,"trigger_outcome_label":"holdout_structural_success_but_reused_symbol","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L71_C16_005290_20190701","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same C16 symbol reused for holdout and 4B/full-window audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R4L71_C16_005290_4B_20191025","case_id":"R4L71_C16_005290_LOCALIZATION_REUSED_HOLDOUT","symbol":"005290","company_name":"동진쎄미켐","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"JAPAN_EXPORT_CONTROL_PHOTORESIST_LOCALIZATION","sector":"materials / strategic resource / controlled supply chain","primary_archetype":"strategic resource policy supply","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2019-10-25","evidence_available_at_that_date":"Price and positioning blowoff after policy-localization rerating; full-window drawdown validates 4B overlay as risk audit only.","evidence_source":"stock-web price path plus non-price policy/localization context","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005290/2019.csv","profile_path":"atlas/symbol_profiles/005/005290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2019-10-25","entry_price":18800.0,"MFE_30D_pct":6.38,"MFE_90D_pct":6.38,"MFE_180D_pct":6.38,"MFE_1Y_pct":"not_used","MFE_2Y_pct":"not_used","MAE_30D_pct":-22.87,"MAE_90D_pct":-51.33,"MAE_180D_pct":-51.33,"MAE_1Y_pct":"not_used","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2019-10-25","peak_price":20000.0,"drawdown_after_peak_pct":-54.25,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":"positioning_overheat|valuation_blowoff","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L71_C16_005290_20191025_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same symbol, different 4B timing family","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR_R4L71_C16_000910_FALSE_S2_20230704","case_id":"R4L71_C16_000910_RARE_EARTH_POLICY_PRICE_ONLY_COUNTER","symbol":"000910","company_name":"유니온","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_EARTH_POLICY_PRICE_ONLY_THEME_TRAP","sector":"materials / strategic resource / controlled supply chain","primary_archetype":"strategic resource policy supply","loop_objective":"counterexample_mining|residual_false_positive_mining|green_strictness_stress_test","trigger_type":"Stage2","trigger_date":"2023-07-04","evidence_available_at_that_date":"China rare-earth/gallium/germanium policy headline created resource-theme attention, but company-level order/offtake/margin bridge was missing.","evidence_source":"historical_public_policy_event + stock-web price path; no company-level supply contract evidence used for promotion","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000910/2023.csv","profile_path":"atlas/symbol_profiles/000/000910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-04","entry_price":6440.0,"MFE_30D_pct":21.74,"MFE_90D_pct":21.74,"MFE_180D_pct":21.74,"MFE_1Y_pct":"not_used","MFE_2Y_pct":"not_used","MAE_30D_pct":-15.99,"MAE_90D_pct":-26.71,"MAE_180D_pct":-26.71,"MAE_1Y_pct":"not_used","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-06","peak_price":7840.0,"drawdown_after_peak_pct":-39.8,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":"price_only","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_price_only_policy_theme","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L71_C16_000910_20230704","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L71_C16_036830_LOCALIZATION_SUPPLY_SUCCESS","trigger_id":"TR_R4L71_C16_036830_S2A_20190701","symbol":"036830","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":30,"margin_bridge_score":55,"revision_score":45,"relative_strength_score":80,"customer_quality_score":35,"policy_or_regulatory_score":80,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":35,"margin_bridge_score":65,"revision_score":55,"relative_strength_score":80,"customer_quality_score":45,"policy_or_regulatory_score":80,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow candidate","changed_components":["margin_bridge_score","backlog_visibility_score","execution_risk_score"],"component_delta_explanation":"C16-specific rule raises weight only when policy supply shock closes through company-level localization/order/margin evidence; policy-only resource beta is downgraded.","MFE_90D_pct":83.42,"MAE_90D_pct":-5.66,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L71_C16_005290_LOCALIZATION_REUSED_HOLDOUT","trigger_id":"TR_R4L71_C16_005290_S2A_20190701","symbol":"005290","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":30,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":80,"customer_quality_score":35,"policy_or_regulatory_score":80,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":35,"margin_bridge_score":55,"revision_score":50,"relative_strength_score":80,"customer_quality_score":45,"policy_or_regulatory_score":80,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable holdout","changed_components":["margin_bridge_score","backlog_visibility_score","execution_risk_score"],"component_delta_explanation":"C16-specific rule raises weight only when policy supply shock closes through company-level localization/order/margin evidence; policy-only resource beta is downgraded.","MFE_90D_pct":68.78,"MAE_90D_pct":-11.81,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L71_C16_005290_LOCALIZATION_REUSED_HOLDOUT","trigger_id":"TR_R4L71_C16_005290_4B_20191025","symbol":"005290","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":30,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":80,"customer_quality_score":35,"policy_or_regulatory_score":80,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage4B-watch","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":35,"margin_bridge_score":55,"revision_score":50,"relative_strength_score":80,"customer_quality_score":45,"policy_or_regulatory_score":80,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage4B overlay","changed_components":["margin_bridge_score","backlog_visibility_score","execution_risk_score"],"component_delta_explanation":"C16-specific rule raises weight only when policy supply shock closes through company-level localization/order/margin evidence; policy-only resource beta is downgraded.","MFE_90D_pct":6.38,"MAE_90D_pct":-51.33,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L71_C16_000910_RARE_EARTH_POLICY_PRICE_ONLY_COUNTER","trigger_id":"TR_R4L71_C16_000910_FALSE_S2_20230704","symbol":"000910","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":80,"customer_quality_score":0,"policy_or_regulatory_score":80,"valuation_repricing_score":35,"execution_risk_score":60,"legal_or_contract_risk_score":40,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":80,"customer_quality_score":0,"policy_or_regulatory_score":80,"valuation_repricing_score":25,"execution_risk_score":70,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52,"stage_label_after":"Stage1/Stage2-watch only","changed_components":["margin_bridge_score","backlog_visibility_score","execution_risk_score"],"component_delta_explanation":"C16-specific rule raises weight only when policy supply shock closes through company-level localization/order/margin evidence; policy-only resource beta is downgraded.","MFE_90D_pct":21.74,"MAE_90D_pct":-26.71,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","new_independent_case_count":2,"reused_case_count":1,"new_symbol_count":2,"new_trigger_family_count":2,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","stage2_actionable_evidence_bonus","stage3_green_total_min"],"residual_error_types_found":["current_profile_false_positive","current_profile_missed_structural"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

```jsonl
{"row_type":"narrative_only","case_id":"R4L71_C16_SOURCE_URL_RECHECK","symbol":"MIXED","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reason":"Exact primary evidence URLs should be attached in later ingestion; this MD uses historical public evidence class and Stock-Web OHLC validation.","price_source":"Songdaiki/stock-web","usage":"source_url_repair_not_weight_calibration"}
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
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
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
completed_round = R4
completed_loop = 71
next_round = R5
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
Raw prompt source: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
Stock-Web manifest: atlas/manifest.json
Stock-Web profiles:
- atlas/symbol_profiles/036/036830.json
- atlas/symbol_profiles/005/005290.json
- atlas/symbol_profiles/000/000910.json
Stock-Web tradable shards:
- atlas/ohlcv_tradable_by_symbol_year/036/036830/2019.csv
- atlas/ohlcv_tradable_by_symbol_year/036/036830/2020.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005290/2019.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005290/2020.csv
- atlas/ohlcv_tradable_by_symbol_year/000/000910/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/000/000910/2024.csv
```

