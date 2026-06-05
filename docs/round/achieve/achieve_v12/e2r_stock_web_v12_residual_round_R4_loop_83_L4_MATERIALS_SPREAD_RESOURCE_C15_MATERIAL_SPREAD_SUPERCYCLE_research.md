# E2R Stock-Web v12 Residual Research — R4 Loop 83 / L4 / C15

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R4
loop: 83
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: ALUMINUM_COPPER_SPREAD_SUPERCYCLE_BRIDGE_VS_PRICE_SPIKE_ROUNDTRIP
sector: 소재·spread·비철금속
output_file: e2r_stock_web_v12_residual_round_R4_loop_83_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 0. Research Metadata

This loop adds 2 new independent cases, 2 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.

```text
scheduled_round = R4
scheduled_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
selection_mode = sequential_round_cycle_then_coverage_gap
auto_selected_coverage_gap = C15 has many positive rows but no bad Stage2 counterexample row in the current no-repeat snapshot
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
```

The already-applied global axes are treated as baseline assumptions, not re-proposed globally:

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

```text
round = R4
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = ALUMINUM_COPPER_SPREAD_SUPERCYCLE_BRIDGE_VS_PRICE_SPIKE_ROUNDTRIP
```

R4 allows the materials/spread/resource family. The chosen C15 scope is deliberately not C16 strategic-resource policy and not C17 chemical commodity spread. The cases below focus on metals/material spread narratives where the core issue is whether price spike, copper/aluminum spread, or inventory-cycle enthusiasm turned into durable earnings/FCF conversion.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index is used only as a duplicate-avoidance ledger.

The ledger snapshot shows `C15_MATERIAL_SPREAD_SUPERCYCLE` with heavy positive coverage and no bad Stage2 rows. Top repeated symbols include `103140`, `012800`, `025820`, `004560`, `021050`, and `001780`. This run therefore uses `103140` only as a reused positive control and adds two new/newer counterexample lanes using `006110` and `001780`.

Hard duplicate key rule:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"103140","trigger_type":"Stage2-Actionable-CopperDefenseSpread-PositiveControl","entry_date":"2024-02-22","duplicate_status":"soft_reuse_positive_control; top-covered symbol, independent_evidence_weight=0.25"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"006110","trigger_type":"Stage2-FalsePositive-AluminumFoilSpread-HighMAE","entry_date":"2024-02-14","duplicate_status":"new symbol/failure-mode expansion inside C15; not in C15 top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"001780","trigger_type":"Stage2-FalsePositive-AluminumPriceSpike-RoundTrip","entry_date":"2024-03-14","duplicate_status":"low-covered symbol in C15; new trigger family and counterexample usage"}
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"price_source_validation","symbol":"103140","company_name":"풍산","profile_path":"atlas/symbol_profiles/103/103140.json","first_date":"2008-07-30","last_date":"2026-02-20","trading_day_count":4331,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"006110","company_name":"삼아알미늄","profile_path":"atlas/symbol_profiles/006/006110.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7041,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["2000-10-16","2000-11-14","2007-05-04","2011-04-26","2023-02-09"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates do not overlap selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"001780","company_name":"알루코","profile_path":"atlas/symbol_profiles/001/001780.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":6459,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1996-01-16","1997-01-10","1999-10-15","2002-04-08","2007-06-07","2008-05-08"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates do not overlap selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window_for_selected_entry"}
```

## 5. Historical Eligibility Gate

All representative triggers below have:

```text
entry_date in Stock-Web tradable shard = true
forward 180D available by manifest max_date = true
corporate-action-contaminated 180D window = false
calibration_usable = true
```

## 6. Canonical Archetype Compression Map

```text
C15_MATERIAL_SPREAD_SUPERCYCLE
  ├─ COPPER_DEFENSE_SPREAD_POSITIVE_CONTROL
  ├─ ALUMINUM_FOIL_SPREAD_HIGH_MAE_FALSE_POSITIVE
  └─ ALUMINUM_PRICE_SPIKE_ROUNDTRIP_FALSE_POSITIVE
```

Compression rule: the fine archetypes remain local explanation tags. Scoring and aggregation stay under `C15_MATERIAL_SPREAD_SUPERCYCLE`.

## 7. Case Selection Summary

```jsonl
{"row_type":"case","case_id":"C15_R4L83_103140_POONGSAN_COPPER_DEFENSE_POSITIVE_CONTROL","symbol":"103140","company_name":"풍산","round":"R4","loop":"83","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_DEFENSE_SPREAD_POSITIVE_CONTROL","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L83_C15_103140_20240222_STAGE2_COPPER_DEFENSE_POSITIVE_CONTROL","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"soft_reuse_positive_control_for_C15_counterexample_balance","independent_evidence_weight":0.25,"score_price_alignment":"positive MFE90/180 and manageable MAE; confirms that C15 should not be over-tightened globally","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Used as bridge control, not as fresh C15 positive evidence."}
{"row_type":"case","case_id":"C15_R4L83_006110_SAMA_ALUMINUM_FOIL_HIGH_MAE","symbol":"006110","company_name":"삼아알미늄","round":"R4","loop":"83","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINUM_FOIL_SPREAD_HIGH_MAE_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R4L83_C15_006110_20240214_STAGE2_FALSE_POSITIVE_ALUMINUM_FOIL_HIGH_MAE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early MFE looked valid but 90/180D MAE overwhelmed the spread thesis","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"New C15 counterexample for high-MAE spread-cycle fade."}
{"row_type":"case","case_id":"C15_R4L83_001780_ALUKO_PRICE_SPIKE_ROUNDTRIP","symbol":"001780","company_name":"알루코","round":"R4","loop":"83","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINUM_PRICE_SPIKE_ROUNDTRIP_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R4L83_C15_001780_20240314_STAGE2_FALSE_POSITIVE_ALUMINUM_PRICE_SPIKE_ROUNDTRIP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"short-lived aluminum/copper price spike gave MFE, then large 90/180D drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"New trigger/failure-mode use for a low-covered C15 symbol."}
```

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
calibration_usable_case_count = 3
new_independent_case_count = 2
reused_case_count = 1
```

This loop intentionally does not add more C15 positives. It uses one positive bridge control and two counterexamples to reduce the current C15 success-only skew.

## 9. Evidence Source Map

```jsonl
{"row_type":"narrative_only","case_id":"C15_R4L83_103140_POONGSAN_COPPER_DEFENSE_POSITIVE_CONTROL","symbol":"103140","evidence_source_type":"historical_public_report_consensus_proxy","evidence_available_at_that_date":"copper/defense spread and earnings-revision proxy existed around trigger window; exact URL pending","stage2_evidence_fields":["relative_strength","early_revision_signal","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"narrative_only","case_id":"C15_R4L83_006110_SAMA_ALUMINUM_FOIL_HIGH_MAE","symbol":"006110","evidence_source_type":"historical_public_report_consensus_proxy","evidence_available_at_that_date":"aluminum foil / battery-material spread enthusiasm existed, but customer/order/margin bridge was not confirmed to support Green","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"narrative_only","case_id":"C15_R4L83_001780_ALUKO_PRICE_SPIKE_ROUNDTRIP","symbol":"001780","evidence_source_type":"historical_public_report_consensus_proxy","evidence_available_at_that_date":"aluminum/copper price spike and material-stock relative strength existed, but evidence bridge was mostly price/spread narrative","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"source_proxy_only":true,"evidence_url_pending":true}
```

## 10. Price Data Source Map

```text
103140 tradable shard = atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv
006110 tradable shard = atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv
001780 tradable shard = atlas/ohlcv_tradable_by_symbol_year/001/001780/2024.csv
```

## 11. Case-by-Case Trigger Grid

| case_id | symbol | trigger_type | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| C15_R4L83_103140 | 103140 | Stage2-Actionable-CopperDefenseSpread-PositiveControl | 2024-02-22 | 42200 | 86.97 | -7.70 | 86.97 | -7.70 | positive control |
| C15_R4L83_006110 | 006110 | Stage2-FalsePositive-AluminumFoilSpread-HighMAE | 2024-02-14 | 91300 | 27.49 | -21.03 | 27.49 | -56.63 | high-MAE counterexample |
| C15_R4L83_001780 | 001780 | Stage2-FalsePositive-AluminumPriceSpike-RoundTrip | 2024-03-14 | 3660 | 23.50 | -26.09 | 23.50 | -52.05 | roundtrip counterexample |

## 12. Trigger-Level OHLC Backtest Tables

```jsonl
{"row_type":"trigger","trigger_id":"R4L83_C15_103140_20240222_STAGE2_COPPER_DEFENSE_POSITIVE_CONTROL","case_id":"C15_R4L83_103140_POONGSAN_COPPER_DEFENSE_POSITIVE_CONTROL","symbol":"103140","company_name":"풍산","round":"R4","loop":"83","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_DEFENSE_SPREAD_POSITIVE_CONTROL","sector":"소재·비철·방산금속","primary_archetype":"C15_MATERIAL_SPREAD_SUPERCYCLE","loop_objective":"holdout_validation;positive_control;canonical_archetype_compression","trigger_type":"Stage2-Actionable-CopperDefenseSpread-PositiveControl","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":42200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical copper/defense spread and revision proxy; exact URL pending","evidence_source":"source-name-level proxy; exact URL pending","stage2_evidence_fields":["relative_strength","early_revision_signal","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv","profile_path":"atlas/symbol_profiles/103/103140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.07,"MFE_90D_pct":86.97,"MFE_180D_pct":86.97,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.70,"MAE_90D_pct":-7.70,"MAE_180D_pct":-7.70,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-14","peak_price":78900.0,"drawdown_after_peak_pct":-26.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_positive_control","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_manageable_MAE","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C15_103140_20240222_42200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"soft_reuse_positive_control_for_C15_counterexample_balance","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L83_C15_006110_20240214_STAGE2_FALSE_POSITIVE_ALUMINUM_FOIL_HIGH_MAE","case_id":"C15_R4L83_006110_SAMA_ALUMINUM_FOIL_HIGH_MAE","symbol":"006110","company_name":"삼아알미늄","round":"R4","loop":"83","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINUM_FOIL_SPREAD_HIGH_MAE_FALSE_POSITIVE","sector":"소재·알루미늄·2차전지소재","primary_archetype":"C15_MATERIAL_SPREAD_SUPERCYCLE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-AluminumFoilSpread-HighMAE","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":91300.0,"entry_price_basis":"close","evidence_available_at_that_date":"aluminum foil / battery material spread narrative; no confirmed durable order/margin bridge at trigger grade","evidence_source":"source-name-level proxy; exact URL pending","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv","profile_path":"atlas/symbol_profiles/006/006110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.49,"MFE_90D_pct":27.49,"MFE_180D_pct":27.49,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.34,"MAE_90D_pct":-21.03,"MAE_180D_pct":-56.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":116400.0,"drawdown_after_peak_pct":-65.98,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.97,"four_b_timing_verdict":"price_only_local_4B_with_later_deep_MAE","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_after_early_MFE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C15_006110_20240214_91300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L83_C15_001780_20240314_STAGE2_FALSE_POSITIVE_ALUMINUM_PRICE_SPIKE_ROUNDTRIP","case_id":"C15_R4L83_001780_ALUKO_PRICE_SPIKE_ROUNDTRIP","symbol":"001780","company_name":"알루코","round":"R4","loop":"83","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINUM_PRICE_SPIKE_ROUNDTRIP_FALSE_POSITIVE","sector":"소재·알루미늄·비철","primary_archetype":"C15_MATERIAL_SPREAD_SUPERCYCLE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-AluminumPriceSpike-RoundTrip","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":3660.0,"entry_price_basis":"close","evidence_available_at_that_date":"short-lived aluminum/material price spike and relative-strength narrative; no durable spread/FCF conversion at trigger grade","evidence_source":"source-name-level proxy; exact URL pending","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001780/2024.csv","profile_path":"atlas/symbol_profiles/001/001780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.50,"MFE_90D_pct":23.50,"MFE_180D_pct":23.50,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.70,"MAE_90D_pct":-26.09,"MAE_180D_pct":-52.05,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":4520.0,"drawdown_after_peak_pct":-61.17,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_peak_without_non_price_bridge","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_roundtrip_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C15_001780_20240314_3660","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

## 13. Current Calibrated Profile Stress Test

```text
1. current calibrated profile would likely allow 103140 as Stage2/Yellow because non-price bridge proxy and price confirmation align.
2. current calibrated profile could over-allow 006110 and 001780 if relative strength plus material-spread narrative is treated as enough evidence.
3. stage2_actionable_evidence_bonus is not globally too high, but C15 needs stronger bridge check for price-only spread spikes.
4. Yellow threshold 75 is not the main problem; evidence quality is.
5. Green threshold 87 / revision 55 should remain strict.
6. price-only blowoff guard is directionally correct and should be strengthened locally for C15.
7. full 4B non-price requirement is correct; local price peak alone was not durable signal.
8. hard 4C routing is not directly tested; these are watch/4B-risk counterexamples rather than hard thesis-break cases.
```

## 14. Stage2 / Yellow / Green Comparison

```text
103140:
  Stage2 entry preserved useful upside.
  Green should not be loosened by this MD because evidence URL remains pending.

006110:
  Stage2-like entry captured a local peak but led into -56.63% 180D MAE.
  Yellow/Green should require confirmed customer/order/margin bridge.

001780:
  Stage2-like price spike produced +23.50% MFE but then collapsed into -52.05% 180D MAE.
  This is a classic C15 price-spike roundtrip.
```

## 15. 4B Local vs Full-window Timing Audit

```text
103140:
  four_b_timing_verdict = not_applicable_positive_control

006110:
  local peak: 2024-02-21 high 116400
  full observed 180D peak: 2024-02-21 high 116400
  full-window drawdown after peak: -65.98%
  4B type: price_only / valuation_blowoff
  verdict: local 4B watch would have been useful, but full 4B requires non-price slowdown evidence.

001780:
  local peak: 2024-03-26 high 4520
  full observed 180D peak: 2024-03-26 high 4520
  full-window drawdown after peak: -61.17%
  4B type: price_only / valuation_blowoff
  verdict: price-only spike should not promote Stage2/Green; it is a 4B-watch guardrail case.
```

## 16. 4C Protection Audit

```text
four_c_protection_label = thesis_break_watch_only
```

No hard 4C is asserted in this MD. The two counterexamples are high-MAE / 4B-watch cases, not confirmed hard thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

The candidate is not proposed across all L4. C16 strategic-resource policy and C17 chemical commodity spreads have different evidence structures.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
target = C15_MATERIAL_SPREAD_SUPERCYCLE
```

Candidate:

```text
For C15, Stage2/Yellow may use material-spread and relative-strength evidence only when one of the following non-price bridges exists:
- confirmed spread-to-margin conversion,
- inventory/cost curve support,
- customer/order/shipment bridge,
- FCF/cash conversion,
- public report or disclosure-grade revision confirmation.

If C15 trigger has MFE30/MFE90 from price spike but no non-price bridge and MAE90 <= -20, classify as 4B-watch / high-MAE guard rather than positive Stage2 evidence.
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false_positive_rate | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_0_baseline_reference | 3 | 45.99 | -18.27 | 0.67 | too much price/spread enthusiasm |
| P0b e2r_2_1_stock_web_calibrated_proxy | 3 | 45.99 | -18.27 | 0.67 | global guard helps but C15 false positives remain |
| P1 sector_specific_candidate_profile | 3 | 45.99 | -18.27 | 0.67 | too broad for L4 |
| P2 canonical_archetype_candidate_profile | 3 | 45.99 | -18.27 | 0.33 | bridge requirement separates 103140 from 006110/001780 |
| P3 counterexample_guard_profile | 3 | 45.99 | -18.27 | 0.33 | best shadow-only candidate |

## 20. Score-Return Alignment Matrix

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C15_R4L83_103140_POONGSAN_COPPER_DEFENSE_POSITIVE_CONTROL","trigger_id":"R4L83_C15_103140_20240222_STAGE2_COPPER_DEFENSE_POSITIVE_CONTROL","symbol":"103140","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":8,"margin_bridge_score":14,"revision_score":13,"relative_strength_score":15,"customer_quality_score":8,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":8,"margin_bridge_score":16,"revision_score":14,"relative_strength_score":15,"customer_quality_score":8,"policy_or_regulatory_score":4,"valuation_repricing_score":10,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable/Stage3-Yellow-Watch","changed_components":["margin_bridge_score","revision_score"],"component_delta_explanation":"Positive control keeps C15 bridge allowance when spread-to-margin proxy exists.","MFE_90D_pct":86.97,"MAE_90D_pct":-7.70,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C15_R4L83_006110_SAMA_ALUMINUM_FOIL_HIGH_MAE","trigger_id":"R4L83_C15_006110_20240214_STAGE2_FALSE_POSITIVE_ALUMINUM_FOIL_HIGH_MAE","symbol":"006110","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":4,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":16,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":12,"execution_risk_score":13,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Watch/FalsePositiveRisk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":12,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":9,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":59,"stage_label_after":"Stage2-FalsePositive-Watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"High MAE and no non-price bridge convert spread enthusiasm into C15 guardrail case.","MFE_90D_pct":27.49,"MAE_90D_pct":-21.03,"score_return_alignment_label":"false_positive_corrected_by_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C15_R4L83_001780_ALUKO_PRICE_SPIKE_ROUNDTRIP","trigger_id":"R4L83_C15_001780_20240314_STAGE2_FALSE_POSITIVE_ALUMINUM_PRICE_SPIKE_ROUNDTRIP","symbol":"001780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":17,"customer_quality_score":2,"policy_or_regulatory_score":5,"valuation_repricing_score":13,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Watch/FalsePositiveRisk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":11,"customer_quality_score":1,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":54,"stage_label_after":"Stage2-FalsePositive-Watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Price spike without bridge round-tripped into -52% 180D MAE; C15 should not treat price-spread spike alone as actionable.","MFE_90D_pct":23.50,"MAE_90D_pct":-26.09,"score_return_alignment_label":"false_positive_corrected_by_guard","current_profile_verdict":"current_profile_false_positive"}
```

## 21. Coverage Matrix

```jsonl
{"row_type":"coverage_matrix","round":"R4","loop":"83","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINUM_COPPER_SPREAD_SUPERCYCLE_BRIDGE_VS_PRICE_SPIKE_ROUNDTRIP","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":2,"reused_case_count":1,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C15 counterexample gap reduced; exact evidence URL repair remains pending."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 2
reused_case_count: 1
reused_case_ids: C15_R4L83_103140_POONGSAN_COPPER_DEFENSE_POSITIVE_CONTROL
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 2
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - C15 price/spread spike with high 90D/180D MAE
  - local MFE followed by full-window roundtrip
new_axis_proposed:
  - C15_spread_to_margin_bridge_required_shadow_only
  - C15_high_MAE_price_spike_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C15
  - full_4b_requires_non_price_evidence within C15
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

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"83","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":2,"reused_case_count":1,"new_symbol_count":2,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C15_high_MAE_after_material_spread_spike","C15_price_spike_roundtrip_without_margin_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- actual Stock-Web tradable raw OHLC rows
- entry_date / entry_price
- 30D / 90D / 180D MFE and MAE
- corporate-action contamination check from symbol profile
- round / sector / canonical consistency
- duplicate ledger policy
```

Non-validation scope:

```text
- exact evidence URL validation is pending
- production scoring is not changed
- no live candidate discovery
- no stock_agent code patch
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C15_spread_to_margin_bridge_required,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"C15 price/spread spike needs non-price bridge before Stage2/Yellow promotion","reduces 006110/001780 false-positive pressure while preserving 103140 positive control","R4L83_C15_103140_20240222_STAGE2_COPPER_DEFENSE_POSITIVE_CONTROL|R4L83_C15_006110_20240214_STAGE2_FALSE_POSITIVE_ALUMINUM_FOIL_HIGH_MAE|R4L83_C15_001780_20240314_STAGE2_FALSE_POSITIVE_ALUMINUM_PRICE_SPIKE_ROUNDTRIP",3,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C15_high_MAE_price_spike_guard,canonical_archetype,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"If MFE comes from price spike but MAE90 <= -20 and bridge is unconfirmed, classify as 4B-watch/high-MAE guard","marks two counterexamples as risk/watch rather than positive Stage2","R4L83_C15_006110_20240214_STAGE2_FALSE_POSITIVE_ALUMINUM_FOIL_HIGH_MAE|R4L83_C15_001780_20240314_STAGE2_FALSE_POSITIVE_ALUMINUM_PRICE_SPIKE_ROUNDTRIP",3,2,2,medium,canonical_shadow_only,"not production; no Green loosening"
```

## 25. Machine-Readable Rows

Machine-readable rows are embedded above in the relevant sections:

```text
price_source_validation rows: 4
case rows: 3
trigger rows: 3
score_simulation rows: 3
coverage_matrix rows: 1
residual_contribution rows: 1
shadow_weight rows: 2
narrative_only rows: 6
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

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer canonical-archetype-specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- Price-only rows cannot promote Stage2/Stage3.
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
completed_loop = 83
next_round = R5
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 28. Source Notes

```text
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
stock_agent_code_accessed = false
evidence_source_quality = source_proxy_only / evidence_url_pending
```
