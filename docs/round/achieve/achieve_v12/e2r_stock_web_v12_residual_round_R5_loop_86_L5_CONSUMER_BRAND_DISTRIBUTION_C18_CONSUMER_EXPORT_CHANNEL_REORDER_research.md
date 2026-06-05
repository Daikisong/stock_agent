# E2R Stock-Web v12 Residual Research — R5 Loop 86 / L5 / C18

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R5
loop: 86
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_EXPORT_REORDER_SELLTHROUGH_BRIDGE_VS_DOMESTIC_FOOD_THEME_REBOUND
sector: consumer / brand / food / export channel / reorder
output_file: e2r_stock_web_v12_residual_round_R5_loop_86_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R4 loop 86`.

```text
scheduled_round = R5
scheduled_loop = 86
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

R5 is restricted to consumer / brand / distribution.  
C18 is selected because the immediately previous R5 run used C20 beauty/global-distribution, while C18 still has no explicit 4B/4C coverage in the No-Repeat Index:

```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER
rows = 38
symbols = 19
good/bad Stage2 = 17/9
4B/4C = 0/0
top-covered = 001680, 280360, UNKNOWN_SYMBOL, 049770, 271560, 003960
```

This loop avoids the top-covered list and also avoids the previous R5/C20 loop85 symbols:

```text
018290, 051900, 090430
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"003230","company_name":"삼양식품","profile_path":"atlas/symbol_profiles/003/003230.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7704,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2003-07-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"005610","company_name":"SPC삼립","profile_path":"atlas/symbol_profiles/005/005610.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7664,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1996-01-03","1997-05-27","1999-03-05","2002-11-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"007310","company_name":"오뚜기","profile_path":"atlas/symbol_profiles/007/007310.json","first_date":"1995-05-03","last_date":"2026-02-20","trading_day_count":7759,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"003230","trigger_type":"Stage2-Actionable-KFoodExportReorderSellthroughBridge-Positive","entry_date":"2024-02-16","duplicate_status":"new C18 symbol/trigger/date combination outside top-covered list and previous R5 loop85 C20 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"005610","trigger_type":"Stage2-FalsePositive-DomesticFoodRebound-NoExportReorderMarginBridge","entry_date":"2024-06-14","duplicate_status":"new C18 symbol/trigger/date combination outside top-covered list and previous R5 loop85 C20 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"007310","trigger_type":"Stage2-FalsePositive-LargecapFoodChannelTheme-NoFreshReorderBridge","entry_date":"2024-06-17","duplicate_status":"new C18 symbol/trigger/date combination outside top-covered list and previous R5 loop85 C20 symbols"}
```

## 4. Research question

C18 is not “food or consumer brand went up.”  
The useful consumer-export signal is the second purchase, not the first shelf placement. E2R should reward the mechanism where overseas sell-through pulls repeat reorder, distributors restock, SKU velocity improves, and margin expands. A domestic-food or generic consumer rebound without that bridge is only a checkout receipt, not a reorder cycle.

Residual question:

```text
Can C18 distinguish:
1. K-food export sell-through / repeat reorder bridge with huge MFE,
2. domestic food rebound without export-channel reorder and margin bridge,
3. large-cap food channel theme where price rises but fresh reorder and margin evidence are weak?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C18_R5L86_003230_SAMYANG_KFOOD_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_SELLTHROUGH_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-KFoodExportReorderSellthroughBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_export_reorder_bridge_required","price_source":"Songdaiki/stock-web","notes":"K-food export/sell-through proxy led to very large 90D/180D MFE with tolerable initial MAE. Green still requires exact channel, reorder, SKU and margin evidence."}
{"row_type":"case","case_id":"C18_R5L86_005610_SPC_DOMESTIC_FOOD_REBOUND_NO_REORDER","symbol":"005610","company_name":"SPC삼립","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"DOMESTIC_FOOD_REBOUND_WITHOUT_EXPORT_REORDER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DomesticFoodRebound-NoExportReorderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_food_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Domestic-food rebound had low MFE and later high MAE without global reorder, SKU velocity or margin bridge."}
{"row_type":"case","case_id":"C18_R5L86_007310_OTTOGI_CHANNEL_THEME_NO_FRESH_REORDER","symbol":"007310","company_name":"오뚜기","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"LARGECAP_FOOD_CHANNEL_THEME_WITHOUT_FRESH_REORDER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LargecapFoodChannelTheme-NoFreshReorderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_medium_MAE","current_profile_verdict":"current_profile_false_positive_if_channel_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Large-cap food/channel theme showed a short bounce but lacked a fresh reorder and margin bridge, then drifted into medium MAE."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 003230 삼양식품 — K-food export / repeat reorder bridge positive

Entry row: `2024-02-16 c=183800`.  
Observed path: initial low `2024-02-29 l=169600`, 30D high `2024-03-28 h=215000`, 90D/180D high `2024-06-19 h=718000`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L86_C18_003230_20240216_STAGE2_KFOOD_EXPORT_REORDER_BRIDGE","case_id":"C18_R5L86_003230_SAMYANG_KFOOD_EXPORT_REORDER","symbol":"003230","company_name":"삼양식품","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_SELLTHROUGH_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-KFoodExportReorderSellthroughBridge-Positive","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":183800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_K_food_export_sellthrough_reorder_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; K-food export sell-through, repeat reorder and channel expansion treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["export_channel_sellthrough_proxy","repeat_reorder_proxy","SKU_velocity_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_channel_reorder_source_pending","margin_bridge_pending","inventory_discipline_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003230/2024.csv","profile_path":"atlas/symbol_profiles/003/003230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.97,"MFE_90D_pct":290.64,"MFE_180D_pct":290.64,"MAE_30D_pct":-7.73,"MAE_90D_pct":-7.73,"MAE_180D_pct":-7.73,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":718000.0,"max_drawdown_low_date":"2024-02-29","max_drawdown_low":169600.0,"drawdown_after_peak_pct":-32.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_export_reorder_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"003230_2024-02-16_183800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C18 can allow Stage2/Yellow when consumer strength is tied to export sell-through, repeat reorder, SKU velocity and margin bridge. Green still requires exact channel and margin evidence."}
```

### 6.2 005610 SPC삼립 — domestic food rebound without export reorder / margin bridge

Entry row: `2024-06-14 c=65500`.  
Observed path: same-day high `2024-06-14 h=66700`, then lows `2024-07-19 l=55200`, `2024-10-25 l=48850`, and `2024-11-13 l=43350`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L86_C18_005610_20240614_STAGE2_FALSE_POSITIVE_DOMESTIC_FOOD_REBOUND","case_id":"C18_R5L86_005610_SPC_DOMESTIC_FOOD_REBOUND_NO_REORDER","symbol":"005610","company_name":"SPC삼립","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"DOMESTIC_FOOD_REBOUND_WITHOUT_EXPORT_REORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-DomesticFoodRebound-NoExportReorderMarginBridge","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":65500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_domestic_food_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; domestic food rebound treated as insufficient without export channel reorder, sell-through and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["domestic_food_rebound","relative_strength_spike"],"stage3_evidence_fields":["export_reorder_bridge_missing","SKU_velocity_missing","margin_bridge_missing","inventory_quality_missing"],"stage4b_evidence_fields":["price_only_local_peak","reorder_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005610/2024.csv","profile_path":"atlas/symbol_profiles/005/005610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.83,"MFE_90D_pct":1.83,"MFE_180D_pct":1.83,"MAE_30D_pct":-15.73,"MAE_90D_pct":-25.42,"MAE_180D_pct":-33.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":66700.0,"max_drawdown_low_date":"2024-11-13","max_drawdown_low":43350.0,"drawdown_after_peak_pct":-35.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"domestic_food_rebound_without_export_reorder_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","reorder_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_food_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"005610_2024-06-14_65500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C18 should not upgrade domestic food rebound without export reorder, SKU velocity and margin bridge. Low MFE and high MAE support Watch/4B-risk."}
```

### 6.3 007310 오뚜기 — large-cap food channel theme without fresh reorder bridge

Entry row: `2024-06-17 c=497500`.  
Observed path: local high `2024-06-18 h=503000`, then lows `2024-07-04 l=412000` and `2024-11-13 l=383000`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L86_C18_007310_20240617_STAGE2_FALSE_POSITIVE_LARGECAP_FOOD_CHANNEL","case_id":"C18_R5L86_007310_OTTOGI_CHANNEL_THEME_NO_FRESH_REORDER","symbol":"007310","company_name":"오뚜기","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"LARGECAP_FOOD_CHANNEL_THEME_WITHOUT_FRESH_REORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-LargecapFoodChannelTheme-NoFreshReorderBridge","trigger_date":"2024-06-17","entry_date":"2024-06-17","entry_price":497500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_largecap_food_channel_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; large-cap food channel theme treated as insufficient without fresh reorder, sell-through and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["largecap_food_channel_theme","relative_strength_rebound"],"stage3_evidence_fields":["fresh_reorder_bridge_missing","export_sellthrough_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","fresh_reorder_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007310/2024.csv","profile_path":"atlas/symbol_profiles/007/007310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.11,"MFE_90D_pct":1.11,"MFE_180D_pct":1.11,"MAE_30D_pct":-17.19,"MAE_90D_pct":-19.1,"MAE_180D_pct":-23.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":503000.0,"max_drawdown_low_date":"2024-11-13","max_drawdown_low":383000.0,"drawdown_after_peak_pct":-23.86,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"largecap_food_channel_theme_without_fresh_reorder_bridge_should_remain_watch","four_b_evidence_type":["price_only","fresh_reorder_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_medium_MAE","current_profile_verdict":"current_profile_false_positive_if_channel_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"007310_2024-06-17_497500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C18 should distinguish a short food/channel bounce from a true reorder cycle. Low MFE and medium MAE argue for Watch rather than Yellow/Green without fresh evidence."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C18_R5L86_003230_SAMYANG_KFOOD_EXPORT_REORDER","trigger_id":"R5L86_C18_003230_20240216_STAGE2_KFOOD_EXPORT_REORDER_BRIDGE","symbol":"003230","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C18 requires export sell-through and repeat reorder bridge rather than food theme alone","raw_component_scores_before":{"export_channel_score":16,"sellthrough_reorder_score":15,"SKU_velocity_score":13,"margin_bridge_score":10,"inventory_discipline_score":9,"relative_strength_score":14,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"export_channel_score":19,"sellthrough_reorder_score":18,"SKU_velocity_score":16,"margin_bridge_score":12,"inventory_discipline_score":11,"relative_strength_score":15,"valuation_repricing_score":11,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Export sell-through and repeat reorder bridge support Yellow/Green-candidate watch, but exact channel and margin evidence still block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C18_R5L86_005610_SPC_DOMESTIC_FOOD_REBOUND_NO_REORDER","trigger_id":"R5L86_C18_005610_20240614_STAGE2_FALSE_POSITIVE_DOMESTIC_FOOD_REBOUND","symbol":"005610","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_scope":"current_default_proxy","profile_hypothesis":"domestic food rebound without export reorder bridge should be blocked","raw_component_scores_before":{"export_channel_score":2,"sellthrough_reorder_score":1,"SKU_velocity_score":2,"margin_bridge_score":2,"inventory_discipline_score":2,"relative_strength_score":11,"valuation_repricing_score":5,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":22,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_channel_score":0,"sellthrough_reorder_score":0,"SKU_velocity_score":0,"margin_bridge_score":0,"inventory_discipline_score":1,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE convert domestic food rebound into missing export-reorder bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C18_R5L86_007310_OTTOGI_CHANNEL_THEME_NO_FRESH_REORDER","trigger_id":"R5L86_C18_007310_20240617_STAGE2_FALSE_POSITIVE_LARGECAP_FOOD_CHANNEL","symbol":"007310","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_scope":"current_default_proxy","profile_hypothesis":"large-cap food channel theme without fresh reorder bridge should remain Watch/blocked","raw_component_scores_before":{"export_channel_score":3,"sellthrough_reorder_score":2,"SKU_velocity_score":2,"margin_bridge_score":2,"inventory_discipline_score":3,"relative_strength_score":10,"valuation_repricing_score":5,"execution_risk_score":-10,"theme_spike_risk":-10,"information_confidence":3},"weighted_score_before":27,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_channel_score":1,"sellthrough_reorder_score":0,"SKU_velocity_score":0,"margin_bridge_score":0,"inventory_discipline_score":2,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Watch-Blocked","component_delta_explanation":"Low MFE and missing fresh reorder evidence keep the row Watch/blocked even before extreme MAE appears."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R5L86_C18_P0_CURRENT","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C18 needs explicit export-channel sell-through, repeat reorder and margin bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":97.86,"avg_MAE90_pct":-17.42,"avg_MFE180_pct":97.86,"avg_MAE180_pct":-21.52,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C18_export_reorder_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R5L86_C18_P1_SECTOR_SPECIFIC","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P1_L5_export_channel_reorder_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L5 consumer export signals need sell-through, repeat reorder, SKU velocity, distribution quality or margin bridge before Stage2-Actionable","changed_axes":["export_reorder_bridge_required","sellthrough_quality_required","domestic_food_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_export_channel_sellthrough_reorder_SKU_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":97.86,"avg_MAE90_pct":-17.42,"avg_MFE180_pct":97.86,"avg_MAE180_pct":-21.52,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R5L86_C18_P2_CANONICAL","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P2_C18_export_reorder_margin_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C18 should reward reorder cycles, not domestic food/channel theme spikes","changed_axes":["C18_export_sellthrough_reorder_bridge_required","C18_food_theme_local_4B_guard","C18_margin_inventory_bridge_required"],"changed_thresholds":{"stage2_yellow_gate":"export_sellthrough_or_repeat_reorder_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":97.86,"avg_MAE90_pct":-17.42,"avg_MFE180_pct":97.86,"avg_MAE180_pct":-21.52,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R5L86_C18_P3_COUNTEREXAMPLE_GUARD","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","profile_id":"P3_C18_low_MFE_missing_reorder_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and export/sell-through reorder bridge is missing, block Yellow/Green; if MAE90<=-20, force 4B-watch","changed_axes":["C18_low_MFE_guardrail","C18_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_bridge_missing; hard_4B_if_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE90_pct":97.86,"avg_MAE90_pct":-17.42,"avg_MFE180_pct":97.86,"avg_MAE180_pct":-21.52,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"C18_KFOOD_EXPORT_REORDER_VS_DOMESTIC_FOOD_THEME","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":97.86,"avg_MAE90_pct":-17.42,"avg_MFE180_pct":97.86,"avg_MAE180_pct":-21.52,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20":0.33,"interpretation":"C18 needs bridge discipline. 삼양식품 shows true export sell-through and repeat reorder can create a huge rerating, while SPC삼립 and 오뚜기 show that domestic food/channel themes fail or stagnate without fresh reorder and margin bridge."}
{"row_type":"stage_transition_summary","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"003230","trigger_type":"Stage2-Actionable-KFoodExportReorderSellthroughBridge-Positive","entry_date":"2024-02-16","stage2_to_90D_outcome":"good_stage2_very_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_export_reorder_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when export sell-through and repeat reorder bridge exists; Green requires exact channel and margin evidence."}
{"row_type":"stage_transition_summary","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"005610","trigger_type":"Stage2-FalsePositive-DomesticFoodRebound-NoExportReorderMarginBridge","entry_date":"2024-06-14","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_domestic_food_rebound","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Domestic food rebound without export reorder and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"007310","trigger_type":"Stage2-FalsePositive-LargecapFoodChannelTheme-NoFreshReorderBridge","entry_date":"2024-06-17","stage2_to_90D_outcome":"weak_stage2_low_MFE_medium_MAE","stage2_to_180D_outcome":"failed_or_stagnant_channel_theme","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Large-cap food/channel theme without fresh reorder bridge should remain Watch/blocked from Yellow/Green."}
{"row_type":"residual_contribution","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","residual_type":"consumer_food_theme_overcredit_without_export_sellthrough_reorder_margin_bridge","contribution":"Adds two C18 local 4B/weak-bridge counterexamples against one K-food export reorder positive, avoiding C18 top-covered and previous R5 loop85 C20 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_REORDER_SELLTHROUGH_BRIDGE_VS_DOMESTIC_FOOD_THEME_REBOUND","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C18 now has non-top-symbol domestic-food/channel-theme counterexamples; next R5 loops should exact-URL repair export channel, repeat reorder, SKU velocity, inventory discipline and margin bridge evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","axis":"C18_export_sellthrough_reorder_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"003230 worked with export sell-through/reorder proxy; 005610 and 007310 failed or stagnated when only domestic food/channel theme existed."}
{"row_type":"shadow_weight","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","axis":"C18_food_channel_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Domestic food and large-cap channel theme rows showed low MFE without fresh reorder, sell-through or margin bridge."}
{"row_type":"shadow_weight","round":"R5","loop":"86","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","axis":"C18_low_MFE_missing_reorder_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<5 while export/sell-through reorder bridge is missing, block Stage2-Actionable/Yellow; if MAE90<=-20, route to 4B-watch."}
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
  - domestic_food_theme_overcredit
  - channel_theme_no_fresh_reorder
  - export_sellthrough_bridge_missing
  - low_MFE_without_reorder_bridge
new_axis_proposed:
  - C18_export_sellthrough_reorder_bridge_required_shadow_only
  - C18_food_channel_theme_local_4B_watch_guard_shadow_only
  - C18_low_MFE_missing_reorder_guardrail_shadow_only
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
3. Confirm R5 / L5 / C18 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C18 top-covered symbols
   - previous R5 loop85 C20 symbols listed in the MD
6. If aggregate support remains stable after exact evidence URL repair, consider C18-scoped safe patch candidates:
   - C18_export_sellthrough_reorder_bridge_required
   - C18_food_channel_theme_local_4B_watch_guard
   - C18_low_MFE_missing_reorder_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R5
completed_loop = 86
next_round = R6
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.
```
