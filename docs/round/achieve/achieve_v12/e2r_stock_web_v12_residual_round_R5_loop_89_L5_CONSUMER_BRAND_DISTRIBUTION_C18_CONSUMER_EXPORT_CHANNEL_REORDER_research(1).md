# E2R Stock-Web v12 Residual Research — R5 Loop 89 / L5 / C18

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R5
loop: 89
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_SNACK_SAUCE_THEME_SPIKE_DECAY
sector: consumer / food / export channel / reorder / sell-through / margin bridge
output_file: e2r_stock_web_v12_residual_round_R5_loop_89_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R4 loop 89`.

```text
scheduled_round = R5
scheduled_loop = 89
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

R5 is restricted to consumer / brand / distribution.  
C18 is selected because recent R5 loops already covered:

```text
R5 loop86: C18_CONSUMER_EXPORT_CHANNEL_REORDER
R5 loop87: C19_BRAND_RETAIL_INVENTORY_MARGIN
R5 loop88: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

No-Repeat Index snapshot:

```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER
rows = 38
symbols = 19
good/bad Stage2 = 17/9
4B/4C = 0/0
top-covered = 001680, 280360, UNKNOWN_SYMBOL, 049770, 271560, 003960
```

This loop avoids the C18 top-covered symbols and also avoids recent R5 loop symbols:

```text
R5 loop86 C18: 003230, 005610, 007310
R5 loop87 C19: 069960, 008770, 031430
R5 loop88 C20: 352480, 237880, 018250
```

Selected symbols:

```text
005180, 101530, 248170
```

This loop tests a different C18 pocket:

```text
K-food / dairy / ice-cream export channel reorder bridge
vs
snack-food late spike without repeat reorder or channel sell-through bridge
vs
sauce / food export theme spike without SKU velocity, reorder and margin bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"005180","company_name":"빙그레","profile_path":"atlas/symbol_profiles/005/005180.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7764,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1995-09-29","1996-09-25","1998-12-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"101530","company_name":"해태제과식품","profile_path":"atlas/symbol_profiles/101/101530.json","first_date":"2016-05-11","last_date":"2026-02-20","trading_day_count":2400,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2016-06-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"248170","company_name":"샘표식품","profile_path":"atlas/symbol_profiles/248/248170.json","first_date":"2016-08-09","last_date":"2026-02-20","trading_day_count":2337,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"005180","trigger_type":"Stage2-Actionable-KFoodExportChannelReorderMarginBridge-Positive","entry_date":"2024-04-15","duplicate_status":"new C18 symbol/trigger/date combination outside top-covered and previous R5 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"101530","trigger_type":"Stage2-FalsePositive-SnackFoodLateThemeSpike-NoFreshReorderSellthroughBridge","entry_date":"2024-06-14","duplicate_status":"new C18 symbol/trigger/date combination outside top-covered and previous R5 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"248170","trigger_type":"Stage2-FalsePositive-SauceFoodExportThemeSpike-NoChannelReorderMarginBridge","entry_date":"2024-06-20","duplicate_status":"new C18 symbol/trigger/date combination outside top-covered and previous R5 loop symbols"}
```

## 4. Research question

C18 is not “K-food theme가 강하다.”  
The useful C18 signal must prove a channel-to-reorder bridge: export distributor quality, sell-through, repeat reorder, SKU velocity, channel inventory discipline, brand pricing, mix, gross margin and cash conversion. A shelf placement is only the first handshake. E2R needs the second purchase order.

Residual question:

```text
Can C18 distinguish:
1. K-food / dairy export channel reorder bridge with very high MFE and tolerable entry MAE,
2. snack-food late spike where theme price action does not prove fresh reorder or sell-through,
3. sauce/food export theme spike where local MFE exists but channel inventory, reorder and margin bridge are missing?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C18_R5L89_005180_BINGGRAE_EXPORT_CHANNEL_REORDER","symbol":"005180","company_name":"빙그레","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-KFoodExportChannelReorderMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_export_reorder_sellthrough_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"K-food/dairy export-channel proxy produced very high MFE with tolerable early MAE. Later drawdown keeps Green strict and requires exact distributor, sell-through, reorder and margin evidence."}
{"row_type":"case","case_id":"C18_R5L89_101530_HAITAI_SNACK_LATE_THEME","symbol":"101530","company_name":"해태제과식품","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"SNACK_FOOD_LATE_THEME_SPIKE_WITHOUT_FRESH_REORDER_SELLTHROUGH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SnackFoodLateThemeSpike-NoFreshReorderSellthroughBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_after_late_spike","current_profile_verdict":"current_profile_false_positive_if_snack_theme_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Snack-food late theme spike had almost no forward MFE and deep MAE when fresh reorder, sell-through, channel inventory and margin bridge failed to confirm."}
{"row_type":"case","case_id":"C18_R5L89_248170_SEMPIO_SAUCE_EXPORT_THEME","symbol":"248170","company_name":"샘표식품","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"SAUCE_FOOD_EXPORT_THEME_SPIKE_WITHOUT_CHANNEL_REORDER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SauceFoodExportThemeSpike-NoChannelReorderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_local_MFE_but_deep_MAE_no_reorder_bridge","current_profile_verdict":"current_profile_false_positive_if_sauce_export_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Sauce/food export theme had local MFE but deep forward MAE without channel reorder, SKU velocity, sell-through and margin bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 005180 빙그레 — K-food / dairy export channel reorder positive

Entry row: `2024-04-15 c=61900`.  
Observed path: early low `2024-04-15 l=57800`, high `2024-06-11 h=118400`, and late-year low area around `2024-11-13 l=60300`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L89_C18_005180_20240415_STAGE2_KFOOD_EXPORT_REORDER","case_id":"C18_R5L89_005180_BINGGRAE_EXPORT_CHANNEL_REORDER","symbol":"005180","company_name":"빙그레","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-KFoodExportChannelReorderMarginBridge-Positive","trigger_date":"2024-04-15","entry_date":"2024-04-15","entry_price":61900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_Kfood_dairy_export_channel_reorder_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; export channel, repeat reorder, sell-through and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["export_channel_proxy","repeat_reorder_proxy","SKU_velocity_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_distributor_source_pending","sellthrough_source_pending","channel_inventory_pending","margin_mix_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv","profile_path":"atlas/symbol_profiles/005/005180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":57.84,"MFE_90D_pct":91.28,"MFE_180D_pct":91.28,"MAE_30D_pct":-6.62,"MAE_90D_pct":-6.62,"MAE_180D_pct":-6.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":118400.0,"max_drawdown_low_date":"2024-04-15","max_drawdown_low":57800.0,"drawdown_after_peak_pct":-49.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_price_extension_and_late_drawdown_watch; Green requires exact distributor/sellthrough/reorder/margin evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_export_reorder_sellthrough_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"005180_2024-04-15_61900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C18 can allow Stage2/Yellow when consumer export strength is tied to channel quality, repeat reorder, SKU velocity, sell-through, margin mix and cash conversion. Green still requires exact evidence."}
```

### 6.2 101530 해태제과식품 — snack-food late theme spike without fresh reorder/sell-through bridge

Entry row: `2024-06-14 c=9310`.  
Observed path: local high `2024-06-18 h=9450`, then lows around `2024-10-21 l=5450` and `2024-12-09 l=5410`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L89_C18_101530_20240614_STAGE2_FALSE_POSITIVE_SNACK_LATE_THEME","case_id":"C18_R5L89_101530_HAITAI_SNACK_LATE_THEME","symbol":"101530","company_name":"해태제과식품","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"SNACK_FOOD_LATE_THEME_SPIKE_WITHOUT_FRESH_REORDER_SELLTHROUGH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SnackFoodLateThemeSpike-NoFreshReorderSellthroughBridge","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":9310.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_snack_food_Kfood_late_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; snack-food late theme spike treated as insufficient without fresh repeat reorder, export distributor quality, sell-through and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["snack_food_theme_spike","Kfood_keyword","relative_strength_spike"],"stage3_evidence_fields":["fresh_reorder_bridge_missing","export_channel_quality_missing","sellthrough_bridge_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","fresh_reorder_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/101/101530/2024.csv","profile_path":"atlas/symbol_profiles/101/101530.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.50,"MFE_90D_pct":1.50,"MFE_180D_pct":1.50,"MAE_30D_pct":-28.36,"MAE_90D_pct":-41.46,"MAE_180D_pct":-41.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":9450.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":5410.0,"drawdown_after_peak_pct":-42.75,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"snack_food_late_theme_without_fresh_reorder_sellthrough_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","fresh_reorder_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_after_late_spike","current_profile_verdict":"current_profile_false_positive_if_snack_theme_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"101530_2024-06-14_9310","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C18 should not promote snack-food theme spikes without export distributor quality, fresh reorder, sell-through, channel inventory and margin evidence. Near-zero MFE and deep MAE require 4B-watch routing."}
```

### 6.3 248170 샘표식품 — sauce/food export theme spike without channel reorder/margin bridge

Entry row: `2024-06-20 c=40950`.  
Observed path: same-day high `45500`, then lows around `2024-11-14 l=24850` and `2024-12-09 l=22300`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L89_C18_248170_20240620_STAGE2_FALSE_POSITIVE_SAUCE_EXPORT_THEME","case_id":"C18_R5L89_248170_SEMPIO_SAUCE_EXPORT_THEME","symbol":"248170","company_name":"샘표식품","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"SAUCE_FOOD_EXPORT_THEME_SPIKE_WITHOUT_CHANNEL_REORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate;price_only_blowoff_stress_test","trigger_type":"Stage2-FalsePositive-SauceFoodExportThemeSpike-NoChannelReorderMarginBridge","trigger_date":"2024-06-20","entry_date":"2024-06-20","entry_price":40950.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_sauce_food_export_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; sauce/food export theme treated as insufficient without repeat reorder, channel sell-through, SKU velocity, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["sauce_food_export_theme","relative_strength_spike"],"stage3_evidence_fields":["repeat_reorder_missing","channel_sellthrough_missing","SKU_velocity_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","channel_reorder_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/248/248170/2024.csv","profile_path":"atlas/symbol_profiles/248/248170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.11,"MFE_90D_pct":11.11,"MFE_180D_pct":11.11,"MAE_30D_pct":-21.86,"MAE_90D_pct":-32.11,"MAE_180D_pct":-45.54,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-20","peak_price":45500.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":22300.0,"drawdown_after_peak_pct":-50.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"sauce_food_export_theme_without_channel_reorder_margin_bridge_should_be_4B_watch_not_positive_even_with_local_MFE","four_b_evidence_type":["price_only","channel_reorder_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_local_MFE_but_deep_MAE_no_reorder_bridge","current_profile_verdict":"current_profile_false_positive_if_sauce_export_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"248170_2024-06-20_40950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C18 should not count local food-export theme MFE as reorder proof. Repeat reorder, sell-through, SKU velocity, margin and cash conversion must be verified before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5L89_005180_BINGGRAE_EXPORT_CHANNEL_REORDER","trigger_id":"R5L89_C18_005180_20240415_STAGE2_KFOOD_EXPORT_REORDER","symbol":"005180","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C18 requires export channel, repeat reorder, sell-through, SKU velocity, margin and cash bridge rather than K-food theme alone","raw_component_scores_before":{"export_channel_score":14,"repeat_reorder_score":13,"sellthrough_score":12,"SKU_velocity_score":11,"channel_inventory_score":9,"margin_mix_score":10,"cash_conversion_score":7,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"export_channel_score":17,"repeat_reorder_score":16,"sellthrough_score":15,"SKU_velocity_score":14,"channel_inventory_score":11,"margin_mix_score":12,"cash_conversion_score":9,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":90,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Export-channel/reorder bridge plus very high MFE supports Yellow/Green-candidate watch; exact distributor, sell-through and margin evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5L89_101530_HAITAI_SNACK_LATE_THEME","trigger_id":"R5L89_C18_101530_20240614_STAGE2_FALSE_POSITIVE_SNACK_LATE_THEME","symbol":"101530","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_scope":"current_default_proxy","profile_hypothesis":"snack-food late spike without fresh reorder and sell-through should be blocked","raw_component_scores_before":{"export_channel_score":2,"repeat_reorder_score":0,"sellthrough_score":0,"SKU_velocity_score":1,"channel_inventory_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":13,"valuation_repricing_score":4,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_channel_score":0,"repeat_reorder_score":0,"sellthrough_score":0,"SKU_velocity_score":0,"channel_inventory_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE convert snack-food theme spike into missing reorder/sell-through bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C18_R5L89_248170_SEMPIO_SAUCE_EXPORT_THEME","trigger_id":"R5L89_C18_248170_20240620_STAGE2_FALSE_POSITIVE_SAUCE_EXPORT_THEME","symbol":"248170","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_scope":"current_default_proxy","profile_hypothesis":"sauce/food export theme without reorder and margin bridge should remain 4B-watch even with local MFE","raw_component_scores_before":{"export_channel_score":4,"repeat_reorder_score":0,"sellthrough_score":1,"SKU_velocity_score":1,"channel_inventory_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":14,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_channel_score":1,"repeat_reorder_score":0,"sellthrough_score":0,"SKU_velocity_score":0,"channel_inventory_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Local MFE is price-only; deep MAE and missing reorder/margin bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R5L89_C18_P0_CURRENT","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C18 needs explicit channel reorder, sell-through, SKU velocity, channel inventory, margin and cash bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":34.63,"avg_MAE90_pct":-26.73,"avg_MFE180_pct":34.63,"avg_MAE180_pct":-31.35,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C18_reorder_sellthrough_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R5L89_C18_P1_SECTOR_SPECIFIC","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P1_L5_consumer_export_reorder_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L5 consumer export signals need export channel quality, repeat reorder, sell-through, SKU velocity, channel inventory, margin mix or cash conversion before Stage2-Actionable","changed_axes":["export_channel_quality_required","reorder_sellthrough_required","food_theme_spike_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_export_channel_repeat_reorder_sellthrough_SKU_inventory_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":34.63,"avg_MAE90_pct":-26.73,"avg_MFE180_pct":34.63,"avg_MAE180_pct":-31.35,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R5L89_C18_P2_CANONICAL","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P2_C18_channel_reorder_sellthrough_margin_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C18 should reward reorder-to-margin mechanics, not K-food theme labels","changed_axes":["C18_channel_reorder_sellthrough_margin_bridge_required","C18_food_theme_spike_local_4B_guard","C18_price_only_MFE_not_reorder_proof_guard"],"changed_thresholds":{"stage2_yellow_gate":"export_channel_or_reorder_plus_sellthrough_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":34.63,"avg_MAE90_pct":-26.73,"avg_MFE180_pct":34.63,"avg_MAE180_pct":-31.35,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R5L89_C18_P3_COUNTEREXAMPLE_GUARD","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P3_C18_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<12 and MAE90<=-25 while reorder/sell-through/margin bridge is missing, block Yellow/Green and route to 4B-watch","changed_axes":["C18_low_MFE_guardrail","C18_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_12_and_MAE90_le_minus_25_with_reorder_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":34.63,"avg_MAE90_pct":-26.73,"avg_MFE180_pct":34.63,"avg_MAE180_pct":-31.35,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_KFOOD_EXPORT_REORDER_VS_SNACK_SAUCE_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":34.63,"avg_MAE90_pct":-26.73,"avg_MFE180_pct":34.63,"avg_MAE180_pct":-31.35,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_12":0.67,"stage2_bad_entry_rate_MAE90_le_minus25":0.67,"interpretation":"C18 needs bridge discipline. 빙그레 shows export-channel/reorder bridge can create very high MFE, while 해태제과식품 and 샘표식품 show K-food/snack/sauce theme spikes should not be promoted without fresh reorder, sell-through, SKU velocity, inventory, margin and cash-conversion evidence."}
{"row_type":"stage_transition_summary","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"005180","trigger_type":"Stage2-Actionable-KFoodExportChannelReorderMarginBridge-Positive","entry_date":"2024-04-15","stage2_to_90D_outcome":"good_stage2_very_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_export_reorder_rerating_with_late_drawdown_watch","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when export channel, repeat reorder, SKU velocity, sell-through and margin bridge exists; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"101530","trigger_type":"Stage2-FalsePositive-SnackFoodLateThemeSpike-NoFreshReorderSellthroughBridge","entry_date":"2024-06-14","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_snack_food_late_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Snack-food late theme without fresh reorder/sell-through bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"248170","trigger_type":"Stage2-FalsePositive-SauceFoodExportThemeSpike-NoChannelReorderMarginBridge","entry_date":"2024-06-20","stage2_to_90D_outcome":"price_only_local_MFE_high_MAE","stage2_to_180D_outcome":"failed_sauce_export_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Sauce/food export theme MFE without channel reorder and margin bridge should be treated as 4B-watch, not positive evidence."}
{"row_type":"residual_contribution","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","residual_type":"Kfood_snack_sauce_theme_overcredit_without_channel_reorder_sellthrough_margin_bridge","contribution":"Adds two C18 local 4B/deep-MAE counterexamples against one K-food export reorder positive, avoiding C18 top-covered and previous R5 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_EXPORT_CHANNEL_REORDER_BRIDGE_VS_SNACK_SAUCE_THEME_SPIKE_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C18 now has non-top-symbol K-food export-channel positive and two snack/sauce theme weak-bridge counterexamples; next R5 loops should exact-URL repair export distributor quality, repeat reorder, sell-through, SKU velocity, channel inventory, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","axis":"C18_channel_reorder_sellthrough_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"005180 worked when export channel/reorder proxy was present; 101530 and 248170 failed when only snack/sauce/K-food theme strength existed."}
{"row_type":"shadow_weight","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","axis":"C18_food_theme_spike_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Snack and sauce theme rows showed sub-12 MFE90 and deep MAE without non-price channel-reorder bridge."}
{"row_type":"shadow_weight","round":"R5","loop":"89","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","axis":"C18_price_only_MFE_not_reorder_proof_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"248170 shows local event MFE should not be counted as positive evidence when repeat reorder, sell-through, channel inventory and margin bridge are missing."}
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
  - Kfood_theme_overcredit
  - snack_food_late_spike_overcredit
  - sauce_food_export_theme_overcredit
  - fresh_reorder_sellthrough_margin_bridge_missing
new_axis_proposed:
  - C18_channel_reorder_sellthrough_margin_bridge_required_shadow_only
  - C18_food_theme_spike_local_4B_watch_guard_shadow_only
  - C18_price_only_MFE_not_reorder_proof_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C18
  - full_4b_requires_non_price_evidence within C18
  - hard_4c_thesis_break_routes_to_4c within C18
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

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.  
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
3. Confirm R5 / L5 / C18 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C18 top-covered symbols
   - previous R5 loop86 C18 symbols
   - previous R5 loop87 C19 symbols
   - previous R5 loop88 C20 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C18-scoped safe patch candidates:
   - C18_channel_reorder_sellthrough_margin_bridge_required
   - C18_food_theme_spike_local_4B_watch_guard
   - C18_price_only_MFE_not_reorder_proof_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R5
completed_loop = 89
next_round = R6
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.
```
