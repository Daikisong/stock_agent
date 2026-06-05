# E2R Stock-Web v12 Residual Research — R10 Loop 85 / L9 / C30

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R10
loop: 85
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: REGIONAL_CONTRACTOR_BALANCE_SHEET_REPAIR_CONTROL_VS_SMALLCAP_CONSTRUCTION_THEME_SPIKE
sector: construction / real estate / housing / PF balance sheet / financing trust
output_file: e2r_stock_web_v12_residual_round_R10_loop_85_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R9 loop 85`.

```text
scheduled_round = R10
scheduled_loop = 85
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

R10 is restricted to construction / real estate / housing.  
C30 is the construction-PF balance-sheet stress bucket. The run avoids the C30 top-covered symbols in the No-Repeat Index:

```text
002990, 294870, 375500, 004960, 013580, 006360
```

It also avoids the previous R10 loop84 set:

```text
035890, 001470, 002780
```

and the earlier R10 loop83 symbols:

```text
047040, 014790, 005960
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"021320","company_name":"KCC건설","profile_path":"atlas/symbol_profiles/021/021320.json","first_date":"2001-08-21","last_date":"2026-02-20","trading_day_count":6045,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"001840","company_name":"이화공영","profile_path":"atlas/symbol_profiles/001/001840.json","first_date":"1996-07-30","last_date":"2025-04-01","trading_day_count":6423,"corporate_action_candidate_count":7,"corporate_action_candidate_dates":["1997-12-11","1998-01-31","2003-12-01","2003-12-29","2010-04-22","2010-05-17","2014-07-18"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"002410","company_name":"범양건영","profile_path":"atlas/symbol_profiles/002/002410.json","first_date":"1995-05-02","last_date":"2025-03-20","trading_day_count":6992,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1996-01-03","2009-12-21","2014-07-07","2015-07-09","2015-12-30","2017-12-06"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"021320","trigger_type":"Stage2-Actionable-RegionalContractorBalanceSheetRepairControl-Positive","entry_date":"2024-01-23","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered list and previous R10 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"001840","trigger_type":"Stage2-FalsePositive-SmallcapConstructionTheme-NoFinancingBacklogBridge","entry_date":"2024-01-11","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered list and previous R10 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002410","trigger_type":"Stage2-FalsePositive-PFReliefSmallcapTheme-NoLiquidityBridge","entry_date":"2024-01-02","duplicate_status":"new C30 symbol/trigger/date combination outside top-covered list and previous R10 loop sets"}
```

## 4. Research question

C30 is not a construction rebound bucket. It is a balance-sheet stress chamber. The useful signal is not “construction stock bounced,” but whether PF exposure, liquidity, financing trust, backlog quality, and margin conversion are repairing.

Residual question:

```text
Can C30 distinguish:
1. a regional contractor repair-control path with low MAE and moderate MFE,
2. a small-cap construction policy/theme rebound with no financing or backlog bridge,
3. a PF-relief/theme price spike that fails before liquidity and margin evidence can arrive?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C30_R10L85_021320_KCC_CONSTRUCTION_REPAIR_CONTROL","symbol":"021320","company_name":"KCC건설","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONTRACTOR_BALANCE_SHEET_REPAIR_CONTROL","case_type":"watch_positive_control","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-RegionalContractorBalanceSheetRepairControl-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_moderate_MFE_low_to_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_balance_sheet_repair_bridge_required","price_source":"Songdaiki/stock-web","notes":"Regional contractor repair-control path with tolerable MAE and moderate MFE. This supports Watch/Yellow-control only, not Green loosening."}
{"row_type":"case","case_id":"C30_R10L85_001840_EHWA_CONSTRUCTION_THEME_NO_BRIDGE","symbol":"001840","company_name":"이화공영","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALLCAP_CONSTRUCTION_THEME_WITHOUT_FINANCING_BACKLOG_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallcapConstructionTheme-NoFinancingBacklogBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_construction_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Small-cap construction theme showed almost no MFE and high MAE without financing trust, backlog quality and margin bridge."}
{"row_type":"case","case_id":"C30_R10L85_002410_BUMYANG_PF_RELIEF_THEME_NO_LIQUIDITY","symbol":"002410","company_name":"범양건영","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_RELIEF_SMALLCAP_THEME_WITHOUT_LIQUIDITY_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PFReliefSmallcapTheme-NoLiquidityBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_extreme_MAE_before_late_unrelated_rebound","current_profile_verdict":"current_profile_false_positive_if_PF_relief_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"PF-relief/small-cap construction theme had limited initial MFE and severe MAE before any late-year unrelated rebound. C30 should block Yellow/Green without liquidity and margin bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 021320 KCC건설 — regional contractor repair-control positive

Entry row: `2024-01-23 c=4575`.  
Forward path: high `2024-04-08 h=5750`, local lows around `2024-04-16 l=4310` and later `2024-10-16 l=4230`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L85_C30_021320_20240123_STAGE2_REGIONAL_CONTRACTOR_REPAIR_CONTROL","case_id":"C30_R10L85_021320_KCC_CONSTRUCTION_REPAIR_CONTROL","symbol":"021320","company_name":"KCC건설","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONTRACTOR_BALANCE_SHEET_REPAIR_CONTROL","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-RegionalContractorBalanceSheetRepairControl-Positive","trigger_date":"2024-01-23","entry_date":"2024-01-23","entry_price":4575.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_regional_contractor_balance_sheet_repair_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; regional contractor PF exposure containment and balance-sheet repair treated as non-price bridge proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["PF_exposure_containment_proxy","balance_sheet_repair_proxy","backlog_quality_proxy","relative_strength_turn"],"stage3_evidence_fields":["financing_trust_source_url_pending","margin_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/021/021320/2024.csv","profile_path":"atlas/symbol_profiles/021/021320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.82,"MFE_90D_pct":25.68,"MFE_180D_pct":25.68,"MAE_30D_pct":-0.55,"MAE_90D_pct":-5.79,"MAE_180D_pct":-7.54,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":5750.0,"max_drawdown_low_date":"2024-10-16","max_drawdown_low":4230.0,"drawdown_after_peak_pct":-26.43,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_moderate_MFE_low_to_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_balance_sheet_repair_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"021320_2024-01-23_4575","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C30 should allow Watch/Yellow-control when balance-sheet/PF repair proxy exists and MAE remains tolerable. This is not enough for Green without URL-grade financing, backlog and margin evidence."}
```

### 6.2 001840 이화공영 — small-cap construction theme without financing/backlog bridge

Entry row: `2024-01-11 c=3310`.  
Forward path: high only `2024-01-11 h=3315`, then lows around `2024-04-15 l=2550` and `2024-10-22 l=2300`.

```jsonl
{"row_type":"trigger","trigger_id":"R10L85_C30_001840_20240111_STAGE2_FALSE_POSITIVE_SMALLCAP_CONSTRUCTION_THEME","case_id":"C30_R10L85_001840_EHWA_CONSTRUCTION_THEME_NO_BRIDGE","symbol":"001840","company_name":"이화공영","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALLCAP_CONSTRUCTION_THEME_WITHOUT_FINANCING_BACKLOG_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SmallcapConstructionTheme-NoFinancingBacklogBridge","trigger_date":"2024-01-11","entry_date":"2024-01-11","entry_price":3310.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_smallcap_construction_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small-cap construction theme treated as insufficient without financing trust, PF exposure repair, backlog quality and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["construction_policy_theme","relative_strength_rebound"],"stage3_evidence_fields":["financing_trust_missing","PF_repair_missing","backlog_quality_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001840/2024.csv","profile_path":"atlas/symbol_profiles/001/001840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.15,"MFE_90D_pct":0.15,"MFE_180D_pct":0.15,"MAE_30D_pct":-9.52,"MAE_90D_pct":-22.96,"MAE_180D_pct":-30.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-11","peak_price":3315.0,"max_drawdown_low_date":"2024-10-22","max_drawdown_low":2300.0,"drawdown_after_peak_pct":-30.62,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smallcap_theme_peak_without_financing_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_construction_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"001840_2024-01-11_3310","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"A small-cap construction theme without financing and backlog bridge had almost no upside and large MAE. C30 needs a local bridge guard before Stage2-Actionable/Yellow."}
```

### 6.3 002410 범양건영 — PF-relief/small-cap theme without liquidity bridge

Entry row: `2024-01-02 c=2220`.  
Forward path: local high `2024-01-02 h=2345`, then lows near `2024-04-08 l=1367` and `2024-09-25 l=1114`. A later November rebound is not used to rehabilitate the weak January entry.

```jsonl
{"row_type":"trigger","trigger_id":"R10L85_C30_002410_20240102_STAGE2_FALSE_POSITIVE_PF_RELIEF_THEME","case_id":"C30_R10L85_002410_BUMYANG_PF_RELIEF_THEME_NO_LIQUIDITY","symbol":"002410","company_name":"범양건영","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_RELIEF_SMALLCAP_THEME_WITHOUT_LIQUIDITY_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-PFReliefSmallcapTheme-NoLiquidityBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":2220.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_PF_relief_smallcap_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; PF-relief/small-cap construction theme treated as insufficient without liquidity repair, financing trust, backlog quality and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["PF_relief_theme","smallcap_construction_relative_strength"],"stage3_evidence_fields":["liquidity_bridge_missing","financing_trust_missing","margin_bridge_missing","backlog_quality_missing"],"stage4b_evidence_fields":["price_only_local_peak","liquidity_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv","profile_path":"atlas/symbol_profiles/002/002410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.63,"MFE_90D_pct":5.63,"MFE_180D_pct":5.63,"MAE_30D_pct":-23.87,"MAE_90D_pct":-38.42,"MAE_180D_pct":-49.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":2345.0,"max_drawdown_low_date":"2024-09-25","max_drawdown_low":1114.0,"drawdown_after_peak_pct":-52.49,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"PF_relief_theme_peak_without_liquidity_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","liquidity_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE_before_late_unrelated_rebound","current_profile_verdict":"current_profile_false_positive_if_PF_relief_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"002410_2024-01-02_2220","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"PF-relief theme without liquidity and financing bridge produced low MFE and extreme MAE. Later unrelated rebound should not validate the weak original entry."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L85_021320_KCC_CONSTRUCTION_REPAIR_CONTROL","trigger_id":"R10L85_C30_021320_20240123_STAGE2_REGIONAL_CONTRACTOR_REPAIR_CONTROL","symbol":"021320","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C30 recognizes low-MAE repair-control but keeps Green strict","raw_component_scores_before":{"PF_exposure_repair":12,"liquidity_bridge":9,"backlog_quality":10,"margin_bridge":6,"financing_trust":9,"relative_strength_score":8,"valuation_repricing_score":6,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":58,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"PF_exposure_repair":15,"liquidity_bridge":11,"backlog_quality":12,"margin_bridge":8,"financing_trust":11,"relative_strength_score":9,"valuation_repricing_score":7,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":72,"stage_label_after":"Stage2-Watch/Yellow-control","component_delta_explanation":"Repair-control and low MAE support Watch/Yellow-control; exact financing/margin/cash conversion evidence still blocks Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L85_001840_EHWA_CONSTRUCTION_THEME_NO_BRIDGE","trigger_id":"R10L85_C30_001840_20240111_STAGE2_FALSE_POSITIVE_SMALLCAP_CONSTRUCTION_THEME","symbol":"001840","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"small-cap construction theme without financing/backlog bridge should be blocked","raw_component_scores_before":{"PF_exposure_repair":2,"liquidity_bridge":1,"backlog_quality":2,"margin_bridge":0,"financing_trust":1,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"backlog_quality":0,"margin_bridge":0,"financing_trust":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-20,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and high MAE convert construction theme into evidence-quality failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C30_R10L85_002410_BUMYANG_PF_RELIEF_THEME_NO_LIQUIDITY","trigger_id":"R10L85_C30_002410_20240102_STAGE2_FALSE_POSITIVE_PF_RELIEF_THEME","symbol":"002410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_scope":"current_default_proxy","profile_hypothesis":"PF-relief theme without liquidity bridge should remain Watch/blocked","raw_component_scores_before":{"PF_exposure_repair":3,"liquidity_bridge":1,"backlog_quality":1,"margin_bridge":0,"financing_trust":1,"relative_strength_score":10,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"PF_exposure_repair":0,"liquidity_bridge":0,"backlog_quality":0,"margin_bridge":0,"financing_trust":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and extreme MAE require liquidity/financing trust bridge before any Yellow/Green upgrade."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R10L85_C30_P0_CURRENT","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C30 still needs financing-trust, liquidity, backlog-quality and margin bridge gates","eligible_trigger_count":3,"avg_MFE90_pct":10.49,"avg_MAE90_pct":-22.39,"avg_MFE180_pct":10.49,"avg_MAE180_pct":-29.29,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C30_financing_liquidity_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R10L85_C30_P1_SECTOR_SPECIFIC","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P1_L9_financing_liquidity_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L9 construction signals need PF exposure containment, liquidity repair, backlog quality, financing trust or margin bridge before Stage2-Actionable","changed_axes":["PF_exposure_repair_required","liquidity_bridge_required","financing_trust_required","theme_spike_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_PF_repair_liquidity_financing_backlog_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":10.49,"avg_MAE90_pct":-22.39,"avg_MFE180_pct":10.49,"avg_MAE180_pct":-29.29,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R10L85_C30_P2_CANONICAL","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P2_C30_financing_liquidity_backlog_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C30 should reward balance-sheet repair, not small-cap construction or PF-relief price themes","changed_axes":["C30_financing_liquidity_bridge_required","C30_backlog_margin_bridge_required","C30_smallcap_theme_local_4B_guard"],"changed_thresholds":{"stage2_yellow_gate":"PF_repair_or_liquidity_financing_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":10.49,"avg_MAE90_pct":-22.39,"avg_MFE180_pct":10.49,"avg_MAE180_pct":-29.29,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R10L85_C30_P3_COUNTEREXAMPLE_GUARD","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","profile_id":"P3_C30_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-20 while financing/liquidity bridge is missing, block Yellow/Green","changed_axes":["C30_high_MAE_guardrail","C30_local_4B_watch_guard","C30_late_rebound_not_entry_validation_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE90_pct":10.49,"avg_MAE90_pct":-22.39,"avg_MFE180_pct":10.49,"avg_MAE180_pct":-29.29,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_REPAIR_CONTROL_VS_SMALLCAP_PF_THEME","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":10.49,"avg_MAE90_pct":-22.39,"avg_MFE180_pct":10.49,"avg_MAE180_pct":-29.29,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C30 needs bridge discipline. KCC건설 behaves like a low-MAE repair-control row, while 이화공영 and 범양건영 show construction/PF-relief themes that fail without financing trust, liquidity, backlog quality and margin conversion."}
{"row_type":"stage_transition_summary","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"021320","trigger_type":"Stage2-Actionable-RegionalContractorBalanceSheetRepairControl-Positive","entry_date":"2024-01-23","stage2_to_90D_outcome":"good_stage2_moderate_MFE_low_MAE","stage2_to_180D_outcome":"watch_positive_repair_control","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Watch/Yellow-control when balance-sheet/PF repair bridge exists; Green requires exact financing and margin evidence."}
{"row_type":"stage_transition_summary","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"001840","trigger_type":"Stage2-FalsePositive-SmallcapConstructionTheme-NoFinancingBacklogBridge","entry_date":"2024-01-11","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_high_MAE","stage2_to_180D_outcome":"failed_smallcap_construction_theme","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Construction theme without financing/backlog bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002410","trigger_type":"Stage2-FalsePositive-PFReliefSmallcapTheme-NoLiquidityBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_PF_relief_theme_before_late_rebound","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"PF-relief theme without liquidity and financing trust should stay Watch/blocked. Late unrelated rebound should not validate the original weak-bridge entry."}
{"row_type":"residual_contribution","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"construction_PF_theme_overcredit_without_financing_liquidity_backlog_margin_bridge","contribution":"Adds two C30 local 4B/high-MAE counterexamples against one repair-control positive while avoiding C30 top-covered and previous R10 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"REGIONAL_CONTRACTOR_BALANCE_SHEET_REPAIR_CONTROL_VS_SMALLCAP_CONSTRUCTION_THEME_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C30 now has non-top-symbol small-cap construction/PF-relief counterexamples and one low-MAE repair-control row; next R10 loops should exact-URL repair financing trust, PF exposure, liquidity and backlog-quality evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_financing_liquidity_backlog_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"021320 can be watched only when repair proxy is present; 001840 and 002410 failed without financing trust, liquidity, backlog quality and margin bridge."}
{"row_type":"shadow_weight","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_smallcap_construction_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Small-cap construction and PF-relief theme rows showed low or near-zero MFE and high MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R10","loop":"85","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","axis":"C30_late_rebound_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If the original entry has MFE90<10 and MAE90<=-20 with missing bridge, a later unrelated rebound should not retroactively validate Stage2-Actionable/Yellow."}
```

## 11. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - construction_theme_overcredit
  - PF_relief_theme_no_liquidity_bridge
  - financing_trust_bridge_missing
  - backlog_margin_bridge_missing
  - late_rebound_not_entry_validation
new_axis_proposed:
  - C30_financing_liquidity_backlog_bridge_required_shadow_only
  - C30_smallcap_construction_theme_local_4B_watch_guard_shadow_only
  - C30_late_rebound_not_entry_validation_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C30
  - full_4b_requires_non_price_evidence within C30
  - hard_4c_thesis_break_routes_to_4c within C30
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

## 12. Data-quality caveat

All selected triggers use actual Stock-Web tradable raw OHLC rows and clean selected forward windows.  
The non-price evidence layer remains source-name/proxy level.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
promotion should prefer hold / data-quality repair until exact URLs are added
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this MD through run-v12-calibration.
2. Confirm all trigger rows validate with:
   - price_data_source=Songdaiki/stock-web
   - price_basis=tradable_raw
   - price_adjustment_status=raw_unadjusted_marcap
3. Confirm R10 / L9 / C30 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C30 top-covered symbols
   - R10 loop84 symbols
   - R10 loop83 symbols listed in the MD
6. If aggregate support remains stable after exact evidence URL repair, consider C30-scoped safe patch candidates:
   - C30_financing_liquidity_backlog_bridge_required
   - C30_smallcap_construction_theme_local_4B_watch_guard
   - C30_late_rebound_not_entry_validation_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R10
completed_loop = 85
next_round = R11
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.
```
