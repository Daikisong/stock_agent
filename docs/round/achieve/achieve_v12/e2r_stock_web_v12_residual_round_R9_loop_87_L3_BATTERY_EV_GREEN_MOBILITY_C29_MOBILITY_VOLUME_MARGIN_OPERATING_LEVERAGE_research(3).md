# E2R Stock-Web v12 Residual Research — R9 Loop 87 / L3 / C29

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R9
loop: 87
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_BATTERY_REPLACEMENT_VOLUME_MARGIN_BRIDGE_VS_EV_AUTOPARTS_CUSTOMER_VOLUME_THEME_DECAY
sector: mobility / auto parts / auto battery / EV parts / volume margin operating leverage
output_file: e2r_stock_web_v12_residual_round_R9_loop_87_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R8 loop 87`.

```text
scheduled_round = R9
scheduled_loop = 87
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

R9 is the mobility / transport / operating-leverage lane.  
C29 remains the target, but this loop avoids the C29 top-covered list:

```text
011210, 000270, 005380, 005850, 010690, 018880
```

It also avoids the earlier C29 evidence sets already used in prior loops:

```text
R9 loop86: 073240, 118990, 090080
R9 loop85: 000120, 003620, 215360
R9 loop84: 086280, 161390, 271940
earlier known C29 set: 012330, 002350, 204320
```

This loop tests a different pocket of C29: automotive battery / replacement-demand / margin bridge versus EV and auto-parts customer-volume theme decay.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"004490","company_name":"세방전지","profile_path":"atlas/symbol_profiles/004/004490.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7756,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2000-04-03"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"009900","company_name":"명신산업","profile_path":"atlas/symbol_profiles/009/009900.json","first_date":"2020-12-07","last_date":"2026-02-20","trading_day_count":1275,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2021-06-18"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"024900","company_name":"덕양산업","profile_path":"atlas/symbol_profiles/024/024900.json","first_date":"1996-07-30","last_date":"2026-02-20","trading_day_count":7178,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1997-06-23","1998-12-24","1999-01-28","2014-10-23"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here. The 2024 selected row uses the historical name 덕양산업 before the 2025 name change to 디와이덕양.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"004490","trigger_type":"Stage2-Actionable-AutoBatteryReplacementVolumeMarginBridge-Positive","entry_date":"2024-02-02","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and prior C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"009900","trigger_type":"Stage2-FalsePositive-EVBodyPartsCustomerVolumeTheme-NoMarginBridge","entry_date":"2024-02-02","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and prior C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"024900","trigger_type":"Stage2-FalsePositive-AutopartsCustomerVolumeTheme-NoOperatingLeverageBridge","entry_date":"2024-02-02","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and prior C29 loop sets"}
```

## 4. Research question

C29 is not “mobility stock moved.”  
The useful mobility signal is the operating bridge: vehicle or replacement demand, customer volume, mix, utilization, pricing, margin expansion, and cash conversion. A theme label without this bridge is a car on a lift: the wheels spin, but no road distance is made.

Residual question:

```text
Can C29 distinguish:
1. auto-battery replacement / volume / margin bridge with high MFE and shallow MAE,
2. EV body-parts customer-volume theme that lacks pricing, utilization and margin conversion,
3. auto-parts customer-volume theme where an initial spike fails to translate into operating leverage?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C29_R9L87_004490_SEBANG_AUTO_BATTERY_VOLUME_MARGIN","symbol":"004490","company_name":"세방전지","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_BATTERY_REPLACEMENT_VOLUME_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-AutoBatteryReplacementVolumeMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_shallow_MAE_later_fade","current_profile_verdict":"current_profile_correct_if_volume_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Auto battery/replacement-demand and margin proxy produced a very high MFE with shallow early MAE. Later fade keeps Green strict unless exact volume, mix, margin and cash evidence is repaired."}
{"row_type":"case","case_id":"C29_R9L87_009900_MYOUNGSHIN_EV_BODY_PARTS_THEME","symbol":"009900","company_name":"명신산업","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_BODY_PARTS_CUSTOMER_VOLUME_THEME_WITHOUT_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-EVBodyPartsCustomerVolumeTheme-NoMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_EV_body_parts_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"EV body-parts/customer-volume theme had near-zero MFE and deep MAE when utilization, pricing, customer order quality and margin bridge were missing."}
{"row_type":"case","case_id":"C29_R9L87_024900_DUCKYANG_AUTOPARTS_VOLUME_THEME","symbol":"024900","company_name":"덕양산업","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTOPARTS_CUSTOMER_VOLUME_THEME_WITHOUT_OPERATING_LEVERAGE_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AutopartsCustomerVolumeTheme-NoOperatingLeverageBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_initial_MFE_below_Yellow_threshold_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_autoparts_theme_promoted_without_operating_leverage","price_source":"Songdaiki/stock-web","notes":"Auto-parts/customer-volume theme had an early spike below strong Yellow threshold and then deep 180D MAE without utilization, mix, margin and cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 004490 세방전지 — auto-battery replacement volume / margin bridge positive

Entry row: `2024-02-02 c=61900`.  
Observed path: entry-window low `2024-02-02 l=58600`, 30D high `2024-03-07 h=90300`, and 90D/180D high `2024-05-13 h=122500`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L87_C29_004490_20240202_STAGE2_AUTO_BATTERY_VOLUME_MARGIN","case_id":"C29_R9L87_004490_SEBANG_AUTO_BATTERY_VOLUME_MARGIN","symbol":"004490","company_name":"세방전지","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_BATTERY_REPLACEMENT_VOLUME_MARGIN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-AutoBatteryReplacementVolumeMarginBridge-Positive","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":61900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_auto_battery_replacement_volume_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; replacement demand, volume/mix and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["replacement_demand_proxy","volume_mix_proxy","margin_bridge_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_or_channel_volume_pending","pricing_power_pending","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","late_fade_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004490/2024.csv","profile_path":"atlas/symbol_profiles/004/004490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":45.88,"MFE_90D_pct":97.90,"MFE_180D_pct":97.90,"MAE_30D_pct":-5.33,"MAE_90D_pct":-5.33,"MAE_180D_pct":-5.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-13","peak_price":122500.0,"max_drawdown_low_date":"2024-11-21","max_drawdown_low":62500.0,"drawdown_after_peak_pct":-48.98,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_price_extension_watch; Green requires exact volume/mix/margin/cash bridge","four_b_evidence_type":["price_only","late_fade_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_shallow_MAE_later_fade","current_profile_verdict":"current_profile_correct_if_volume_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"004490_2024-02-02_61900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 can allow Stage2/Yellow when mobility strength is tied to replacement demand, volume/mix, margin and cash bridge. Green still requires exact customer/channel volume and margin evidence."}
```

### 6.2 009900 명신산업 — EV body-parts/customer-volume theme without margin bridge

Entry row: `2024-02-02 c=17440`.  
Observed path: local high `2024-02-02 h=17720`, lows `2024-04-19 l=13700`, `2024-07-22 l=13800`, and `2024-12-09 l=10210`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L87_C29_009900_20240202_STAGE2_FALSE_POSITIVE_EV_BODY_PARTS","case_id":"C29_R9L87_009900_MYOUNGSHIN_EV_BODY_PARTS_THEME","symbol":"009900","company_name":"명신산업","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_BODY_PARTS_CUSTOMER_VOLUME_THEME_WITHOUT_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-EVBodyPartsCustomerVolumeTheme-NoMarginBridge","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":17440.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_EV_body_parts_customer_volume_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; EV body-parts/customer-volume theme treated as insufficient without verified customer order quality, utilization, mix, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["EV_body_parts_theme","customer_volume_keyword","relative_strength_rebound"],"stage3_evidence_fields":["verified_customer_order_quality_missing","utilization_bridge_missing","pricing_mix_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","customer_volume_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009900/2024.csv","profile_path":"atlas/symbol_profiles/009/009900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.61,"MFE_90D_pct":1.61,"MFE_180D_pct":1.61,"MAE_30D_pct":-13.19,"MAE_90D_pct":-21.44,"MAE_180D_pct":-41.46,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":17720.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":10210.0,"drawdown_after_peak_pct":-42.38,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"EV_body_parts_customer_volume_theme_without_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","customer_volume_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_EV_body_parts_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"009900_2024-02-02_17440","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not upgrade EV body-parts/customer-volume labels without utilization, pricing/mix, margin and cash bridge. Near-zero MFE and deep MAE force Watch/4B-risk routing."}
```

### 6.3 024900 덕양산업 — auto-parts customer-volume theme without operating-leverage bridge

Entry row: `2024-02-02 c=5240`.  
Observed path: event high `2024-02-05 h=6150`, but lows later reached `2024-10-22 l=3210`, `2024-11-12 l=2970`, and `2024-12-09 l=2615`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L87_C29_024900_20240202_STAGE2_FALSE_POSITIVE_AUTOPARTS_VOLUME_THEME","case_id":"C29_R9L87_024900_DUCKYANG_AUTOPARTS_VOLUME_THEME","symbol":"024900","company_name":"덕양산업","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTOPARTS_CUSTOMER_VOLUME_THEME_WITHOUT_OPERATING_LEVERAGE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-AutopartsCustomerVolumeTheme-NoOperatingLeverageBridge","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":5240.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_autoparts_customer_volume_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; auto-parts customer-volume theme treated as insufficient without operating leverage, utilization, mix, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["autoparts_customer_volume_theme","relative_strength_spike"],"stage3_evidence_fields":["operating_leverage_bridge_missing","utilization_bridge_missing","mix_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_spike","operating_leverage_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/024/024900/2024.csv","profile_path":"atlas/symbol_profiles/024/024900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.37,"MFE_90D_pct":17.37,"MFE_180D_pct":17.37,"MAE_30D_pct":-12.60,"MAE_90D_pct":-14.69,"MAE_180D_pct":-50.10,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":6150.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":2615.0,"drawdown_after_peak_pct":-57.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"autoparts_customer_volume_theme_without_operating_leverage_bridge_should_remain_watch_4B_not_Yellow","four_b_evidence_type":["price_only","operating_leverage_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_initial_MFE_below_Yellow_threshold_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_autoparts_theme_promoted_without_operating_leverage","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; historical_name_Duckyang_before_2025_name_change","same_entry_group_id":"024900_2024-02-02_5240","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should keep auto-parts customer-volume spikes in Watch unless utilization, mix, margin and cash conversion are verified. MFE below 20% plus deep 180D MAE supports 4B-watch routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C29_R9L87_004490_SEBANG_AUTO_BATTERY_VOLUME_MARGIN","trigger_id":"R9L87_C29_004490_20240202_STAGE2_AUTO_BATTERY_VOLUME_MARGIN","symbol":"004490","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C29 requires volume/mix/margin bridge rather than mobility theme alone","raw_component_scores_before":{"volume_bridge_score":14,"mix_margin_score":13,"operating_leverage_score":13,"customer_or_channel_quality":10,"cash_conversion_score":8,"relative_strength_score":14,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"volume_bridge_score":17,"mix_margin_score":16,"operating_leverage_score":15,"customer_or_channel_quality":12,"cash_conversion_score":10,"relative_strength_score":15,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Replacement-demand and volume/margin bridge plus very high MFE support Yellow/Green-candidate watch, but later fade and proxy-only evidence keep Green strict."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C29_R9L87_009900_MYOUNGSHIN_EV_BODY_PARTS_THEME","trigger_id":"R9L87_C29_009900_20240202_STAGE2_FALSE_POSITIVE_EV_BODY_PARTS","symbol":"009900","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"EV body-parts theme without customer volume and margin bridge should be blocked","raw_component_scores_before":{"volume_bridge_score":4,"mix_margin_score":1,"operating_leverage_score":2,"customer_or_channel_quality":3,"cash_conversion_score":0,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"volume_bridge_score":0,"mix_margin_score":0,"operating_leverage_score":0,"customer_or_channel_quality":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE convert customer-volume theme into missing operating-leverage bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C29_R9L87_024900_DUCKYANG_AUTOPARTS_VOLUME_THEME","trigger_id":"R9L87_C29_024900_20240202_STAGE2_FALSE_POSITIVE_AUTOPARTS_VOLUME_THEME","symbol":"024900","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"auto-parts spike without operating leverage and cash bridge should remain Watch","raw_component_scores_before":{"volume_bridge_score":5,"mix_margin_score":1,"operating_leverage_score":1,"customer_or_channel_quality":3,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"volume_bridge_score":1,"mix_margin_score":0,"operating_leverage_score":0,"customer_or_channel_quality":1,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"MFE below Yellow threshold and deep 180D MAE require volume/mix/margin and cash bridge before any promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R9L87_C29_P0_CURRENT","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C29 needs explicit volume/mix/margin/customer and cash bridge distinction across auto-battery and auto-parts cases","eligible_trigger_count":3,"avg_MFE90_pct":38.96,"avg_MAE90_pct":-13.82,"avg_MFE180_pct":38.96,"avg_MAE180_pct":-32.30,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C29_volume_margin_operating_leverage_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R9L87_C29_P1_SECTOR_SPECIFIC","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P1_L3_mobility_volume_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"Mobility signals need volume, mix, margin, utilization, customer quality or cash conversion bridge before Stage2-Actionable","changed_axes":["volume_mix_required","margin_cash_bridge_required","autoparts_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_volume_mix_margin_customer_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":38.96,"avg_MAE90_pct":-13.82,"avg_MFE180_pct":38.96,"avg_MAE180_pct":-32.30,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R9L87_C29_P2_CANONICAL","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P2_C29_volume_mix_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C29 should reward operating-leverage mechanics, not EV/auto-parts theme labels","changed_axes":["C29_volume_mix_margin_cash_bridge_required","C29_autoparts_theme_local_4B_guard","C29_deep_180D_MAE_guard"],"changed_thresholds":{"stage2_yellow_gate":"volume_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":38.96,"avg_MAE90_pct":-13.82,"avg_MFE180_pct":38.96,"avg_MAE180_pct":-32.30,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R9L87_C29_P3_COUNTEREXAMPLE_GUARD","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P3_C29_low_MFE_deep_180D_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<20 and MAE180<=-35 while volume/margin bridge is missing, block Yellow/Green","changed_axes":["C29_low_MFE_guardrail","C29_deep_180D_MAE_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_20_and_MAE180_le_minus_35"},"eligible_trigger_count":3,"avg_MFE90_pct":38.96,"avg_MAE90_pct":-13.82,"avg_MFE180_pct":38.96,"avg_MAE180_pct":-32.30,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_BATTERY_VOLUME_MARGIN_VS_EV_AUTOPARTS_THEME","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":38.96,"avg_MAE90_pct":-13.82,"avg_MFE180_pct":38.96,"avg_MAE180_pct":-32.30,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_20":0.67,"stage2_bad_entry_rate_MAE180_le_minus_35":0.67,"interpretation":"C29 needs bridge discipline. 세방전지 shows replacement-demand and volume/margin bridge can rerate sharply, while 명신산업 and 덕양산업 show EV/auto-parts themes can fail without verified customer volume, utilization, pricing/mix, margin and cash conversion."}
{"row_type":"stage_transition_summary","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"004490","trigger_type":"Stage2-Actionable-AutoBatteryReplacementVolumeMarginBridge-Positive","entry_date":"2024-02-02","stage2_to_90D_outcome":"good_stage2_very_high_MFE_shallow_MAE","stage2_to_180D_outcome":"positive_auto_battery_volume_margin_rerating_with_late_fade","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when replacement demand, volume/mix, margin and cash bridge exists; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"009900","trigger_type":"Stage2-FalsePositive-EVBodyPartsCustomerVolumeTheme-NoMarginBridge","entry_date":"2024-02-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_high_MAE","stage2_to_180D_outcome":"failed_EV_body_parts_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"EV body-parts customer-volume theme without margin/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"024900","trigger_type":"Stage2-FalsePositive-AutopartsCustomerVolumeTheme-NoOperatingLeverageBridge","entry_date":"2024-02-02","stage2_to_90D_outcome":"weak_stage2_MFE_below_Yellow_threshold","stage2_to_180D_outcome":"failed_autoparts_volume_theme_deep_180D_MAE","MFE90_ge_20":false,"MAE180_le_minus_35":true,"transition_note":"Auto-parts volume theme without operating-leverage bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"EV_autoparts_theme_overcredit_without_volume_mix_margin_cash_bridge","contribution":"Adds two C29 local 4B/deep-MAE counterexamples against one auto-battery volume/margin bridge positive, avoiding C29 top-covered and prior C29 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_BATTERY_REPLACEMENT_VOLUME_MARGIN_BRIDGE_VS_EV_AUTOPARTS_CUSTOMER_VOLUME_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C29 now has a non-top-symbol auto-battery volume/margin control and two EV/auto-parts theme counterexamples; next R9 loops should exact-URL repair customer volume, replacement demand, utilization, mix/margin, pricing power and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_volume_mix_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"004490 worked with replacement-demand volume/margin proxy; 009900 and 024900 failed when only EV/auto-parts customer-volume theme existed."}
{"row_type":"shadow_weight","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_EV_autoparts_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"EV/auto-parts theme rows showed near-zero or sub-Yellow MFE and deep 180D MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R9","loop":"87","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_low_MFE_deep_180D_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<20 and MAE180<=-35 while volume/margin bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - EV_autoparts_theme_overcredit
  - customer_volume_bridge_missing
  - operating_leverage_bridge_missing
  - mix_margin_cash_conversion_bridge_missing
new_axis_proposed:
  - C29_volume_mix_margin_cash_bridge_required_shadow_only
  - C29_EV_autoparts_theme_local_4B_watch_guard_shadow_only
  - C29_low_MFE_deep_180D_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C29
  - full_4b_requires_non_price_evidence within C29
  - hard_4c_thesis_break_routes_to_4c within C29
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
3. Confirm R9 / L3 / C29 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C29 top-covered symbols
   - R9 loop86 C29 symbols
   - R9 loop85 C29 symbols
   - R9 loop84 C29 symbols
   - earlier known C29 symbols listed in this MD
6. If aggregate support remains stable after exact evidence URL repair, consider C29-scoped safe patch candidates:
   - C29_volume_mix_margin_cash_bridge_required
   - C29_EV_autoparts_theme_local_4B_watch_guard
   - C29_low_MFE_deep_180D_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R9
completed_loop = 87
next_round = R10
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.
```
