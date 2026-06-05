# E2R Stock-Web v12 Residual Research — R9 Loop 85 / L3 / C29

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R9
loop: 85
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: LOGISTICS_VOLUME_MARGIN_BRIDGE_VS_OEM_TURNAROUND_AND_EV_THERMAL_THEME_SPIKE
sector: mobility / logistics / auto OEM / EV thermal parts
output_file: e2r_stock_web_v12_residual_round_R9_loop_85_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R8 loop 85`.

```text
scheduled_round = R9
scheduled_loop = 85
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

R9 is the mobility / transport / operating-leverage lane.  
C29 is selected again, but this loop deliberately avoids the C29 top-covered list:

```text
011210, 000270, 005380, 005850, 010690, 018880
```

It also avoids the earlier R9 loop84 symbols:

```text
086280, 161390, 271940
```

and the known previous-loop C29 set:

```text
012330, 002350, 204320
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"000120","company_name":"CJ대한통운","profile_path":"atlas/symbol_profiles/000/000120.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7732,"corporate_action_candidate_count":9,"corporate_action_candidate_dates":["1996-01-03","1997-02-28","1999-08-25","2000-05-19","2001-08-03","2001-10-19","2006-06-15","2008-03-21","2009-05-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here. Name history metadata has later overlap noise, but trigger-period name is CJ대한통운.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"003620","company_name":"KG모빌리티","profile_path":"atlas/symbol_profiles/003/003620.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7083,"corporate_action_candidate_count":9,"corporate_action_candidate_dates":["1995-06-21","1997-03-21","2000-03-08","2000-03-20","2002-01-24","2002-06-27","2010-02-12","2011-02-23","2023-04-28"],"has_major_raw_discontinuity":true,"calibration_caveat":"Most corporate-action candidates are before the 2024 forward window; selected entry is after 2024 share-count changes in the raw marcap table but not a price discontinuity candidate.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_price_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"215360","company_name":"우리산업","profile_path":"atlas/symbol_profiles/215/215360.json","first_date":"2015-05-06","last_date":"2026-02-20","trading_day_count":2650,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

The No-Repeat Index is used only as a duplicate-avoidance ledger.

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"000120","trigger_type":"Stage2-Actionable-LogisticsVolumeMarginBridge-Positive","entry_date":"2024-01-19","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered list and previous R9 loops"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"003620","trigger_type":"Stage2-FalsePositive-OEMTurnaroundVolumeTheme-NoMarginBridge","entry_date":"2024-04-23","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered list and previous R9 loops"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"215360","trigger_type":"Stage2-FalsePositive-EVThermalThemeSpike-NoCustomerVolumeBridge","entry_date":"2024-04-01","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered list and previous R9 loops"}
```

## 4. Research question

C29 should not read every auto, logistics, tire, hydrogen, or EV-parts move as operating leverage. The real bridge is volume, mix, margin, utilization, customer quality, freight or logistics throughput, and cash conversion. If only the theme or turnaround headline turns, the price can move like a wheel spinning on ice.

Residual question:

```text
Can C29 distinguish:
1. logistics volume/mix/margin bridge with positive rerating and tolerable MAE,
2. OEM turnaround / mobility volume theme where margin and cash bridge are missing,
3. EV thermal-management theme spike where customer/volume bridge does not follow the price spike?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C29_R9L85_000120_CJLOGISTICS_VOLUME_MARGIN_BRIDGE","symbol":"000120","company_name":"CJ대한통운","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LOGISTICS_VOLUME_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-LogisticsVolumeMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_moderate_MFE_low_initial_MAE","current_profile_verdict":"current_profile_correct_if_volume_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Logistics throughput / parcel mix / margin proxy produced a 30D/90D rerating. Later drawdown means Green still requires exact margin and cash conversion evidence."}
{"row_type":"case","case_id":"C29_R9L85_003620_KGM_OEM_TURNAROUND_THEME","symbol":"003620","company_name":"KG모빌리티","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_TURNAROUND_VOLUME_THEME_WITHOUT_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-OEMTurnaroundVolumeTheme-NoMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_OEM_turnaround_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"OEM turnaround/volume theme had limited MFE and deep 180D MAE without margin, mix and cash-conversion bridge."}
{"row_type":"case","case_id":"C29_R9L85_215360_WOORI_EV_THERMAL_THEME","symbol":"215360","company_name":"우리산업","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_THERMAL_THEME_SPIKE_WITHOUT_CUSTOMER_VOLUME_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-EVThermalThemeSpike-NoCustomerVolumeBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_extreme_MAE_after_theme_peak","current_profile_verdict":"current_profile_false_positive_if_EV_parts_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"EV thermal-management theme spike peaked first and then collapsed without customer volume, utilization and margin bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 000120 CJ대한통운 — logistics volume/margin bridge positive

Entry row: `2024-01-19 c=121900`.  
Observed path: early low `2024-01-19 l=119000`, high `2024-02-02 h=148600`, later drawdown to `2024-10-22 l=84200`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L85_C29_000120_20240119_STAGE2_LOGISTICS_VOLUME_MARGIN_BRIDGE","case_id":"C29_R9L85_000120_CJLOGISTICS_VOLUME_MARGIN_BRIDGE","symbol":"000120","company_name":"CJ대한통운","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LOGISTICS_VOLUME_MARGIN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-LogisticsVolumeMarginBridge-Positive","trigger_date":"2024-01-19","entry_date":"2024-01-19","entry_price":121900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_logistics_volume_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; logistics volume/mix and operating leverage thesis treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["logistics_throughput_proxy","parcel_mix_margin_proxy","relative_strength_turn"],"stage3_evidence_fields":["cash_conversion_pending","multi_quarter_margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000120/2024.csv","profile_path":"atlas/symbol_profiles/000/000120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.90,"MFE_90D_pct":21.90,"MFE_180D_pct":21.90,"MAE_30D_pct":-2.38,"MAE_90D_pct":-16.41,"MAE_180D_pct":-30.93,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":148600.0,"max_drawdown_low_date":"2024-10-22","max_drawdown_low":84200.0,"drawdown_after_peak_pct":-43.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_moderate_MFE_low_initial_MAE","current_profile_verdict":"current_profile_correct_if_volume_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"000120_2024-01-19_121900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 can allow Watch/Yellow when logistics throughput and margin bridge exists. Later drawdown argues for strict Green evidence: cash conversion and multi-quarter margin proof."}
```

### 6.2 003620 KG모빌리티 — OEM turnaround/volume theme without margin bridge

Entry row: `2024-04-23 c=6090`.  
Observed path: local high `2024-07-19 h=6470`, lows `2024-06-27 l=5000`, `2024-10-29 l=4560`, and `2024-12-09 l=3800`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L85_C29_003620_20240423_STAGE2_FALSE_POSITIVE_OEM_TURNAROUND","case_id":"C29_R9L85_003620_KGM_OEM_TURNAROUND_THEME","symbol":"003620","company_name":"KG모빌리티","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_TURNAROUND_VOLUME_THEME_WITHOUT_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-OEMTurnaroundVolumeTheme-NoMarginBridge","trigger_date":"2024-04-23","entry_date":"2024-04-23","entry_price":6090.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_OEM_turnaround_volume_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; OEM turnaround/volume theme treated as insufficient without mix, margin and cash-conversion bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["OEM_turnaround_theme","volume_rebound_proxy"],"stage3_evidence_fields":["mix_margin_bridge_missing","cash_conversion_missing","order_quality_missing"],"stage4b_evidence_fields":["price_only_local_peak","turnaround_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003620/2024.csv","profile_path":"atlas/symbol_profiles/003/003620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.13,"MFE_90D_pct":6.24,"MFE_180D_pct":6.24,"MAE_30D_pct":-13.63,"MAE_90D_pct":-17.90,"MAE_180D_pct":-37.60,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-19","peak_price":6470.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":3800.0,"drawdown_after_peak_pct":-41.27,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"OEM_turnaround_peak_without_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","turnaround_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_OEM_turnaround_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"price_clean_for_2024_window; share_count_changes_are_not_used_as_return_adjustments","same_entry_group_id":"003620_2024-04-23_6090","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not upgrade OEM turnaround/volume keywords without mix, margin and cash conversion bridge. Low MFE and deep MAE support local 4B guard."}
```

### 6.3 215360 우리산업 — EV thermal-management theme spike without customer/volume bridge

Entry row: `2024-04-01 c=19540`.  
Observed path: same-day high `h=21100`, then lows `2024-04-11 l=14150`, `2024-07-22 l=13830`, and `2024-12-09 l=8900`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L85_C29_215360_20240401_STAGE2_FALSE_POSITIVE_EV_THERMAL_THEME","case_id":"C29_R9L85_215360_WOORI_EV_THERMAL_THEME","symbol":"215360","company_name":"우리산업","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_THERMAL_THEME_SPIKE_WITHOUT_CUSTOMER_VOLUME_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-EVThermalThemeSpike-NoCustomerVolumeBridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":19540.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_EV_thermal_management_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; EV thermal/parts theme treated as insufficient without customer, volume, utilization and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["EV_thermal_theme_spike","relative_strength_extension"],"stage3_evidence_fields":["customer_volume_bridge_missing","utilization_bridge_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/215/215360/2024.csv","profile_path":"atlas/symbol_profiles/215/215360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.98,"MFE_90D_pct":7.98,"MFE_180D_pct":7.98,"MAE_30D_pct":-27.58,"MAE_90D_pct":-29.22,"MAE_180D_pct":-54.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":21100.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":8900.0,"drawdown_after_peak_pct":-57.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"EV_parts_theme_peak_without_customer_volume_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE_after_theme_peak","current_profile_verdict":"current_profile_false_positive_if_EV_parts_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"215360_2024-04-01_19540","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"EV thermal-management theme spike is not C29 operating leverage unless customer volume and margin bridge follow. This path had low MFE and extreme MAE."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L85_000120_CJLOGISTICS_VOLUME_MARGIN_BRIDGE","trigger_id":"R9L85_C29_000120_20240119_STAGE2_LOGISTICS_VOLUME_MARGIN_BRIDGE","symbol":"000120","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C29 recognizes logistics volume/mix bridge but keeps Green strict","raw_component_scores_before":{"volume_bridge_score":13,"mix_margin_score":12,"operating_leverage_score":11,"customer_or_channel_quality":8,"capital_return_or_cash_conversion":6,"relative_strength_score":10,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"volume_bridge_score":16,"mix_margin_score":15,"operating_leverage_score":13,"customer_or_channel_quality":10,"capital_return_or_cash_conversion":8,"relative_strength_score":11,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable/Stage3-Yellow-Watch","component_delta_explanation":"Logistics throughput and margin proxy support Yellow-watch, while later drawdown requires exact cash conversion and multi-quarter margin evidence."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L85_003620_KGM_OEM_TURNAROUND_THEME","trigger_id":"R9L85_C29_003620_20240423_STAGE2_FALSE_POSITIVE_OEM_TURNAROUND","symbol":"003620","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"OEM turnaround theme without mix/margin/cash bridge should be blocked","raw_component_scores_before":{"volume_bridge_score":6,"mix_margin_score":2,"operating_leverage_score":3,"customer_or_channel_quality":3,"capital_return_or_cash_conversion":1,"relative_strength_score":8,"valuation_repricing_score":5,"execution_risk_score":-12,"theme_spike_risk":-10,"information_confidence":3},"weighted_score_before":20,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"volume_bridge_score":2,"mix_margin_score":0,"operating_leverage_score":0,"customer_or_channel_quality":1,"capital_return_or_cash_conversion":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-16,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert OEM turnaround theme into missing margin/cash bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L85_215360_WOORI_EV_THERMAL_THEME","trigger_id":"R9L85_C29_215360_20240401_STAGE2_FALSE_POSITIVE_EV_THERMAL_THEME","symbol":"215360","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"EV parts theme without customer volume bridge should remain Watch/blocked","raw_component_scores_before":{"volume_bridge_score":3,"mix_margin_score":2,"operating_leverage_score":3,"customer_or_channel_quality":2,"capital_return_or_cash_conversion":1,"relative_strength_score":14,"valuation_repricing_score":7,"execution_risk_score":-14,"theme_spike_risk":-15,"information_confidence":3},"weighted_score_before":19,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"volume_bridge_score":0,"mix_margin_score":0,"operating_leverage_score":0,"customer_or_channel_quality":0,"capital_return_or_cash_conversion":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Price-only EV parts spike plus missing customer/volume bridge and extreme MAE blocks Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R9L85_C29_P0_CURRENT","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C29 needs explicit volume/mix/margin/cash bridge distinction across logistics, OEM and EV parts","eligible_trigger_count":3,"avg_MFE90_pct":12.04,"avg_MAE90_pct":-21.18,"avg_MFE180_pct":12.04,"avg_MAE180_pct":-41.00,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C29_volume_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R9L85_C29_P1_SECTOR_SPECIFIC","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P1_L3_mobility_volume_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"Mobility signals need volume, mix, margin, logistics throughput, customer volume or cash bridge before Stage2-Actionable","changed_axes":["volume_mix_bridge_required","margin_cash_bridge_required","EV_parts_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_volume_mix_margin_logistics_or_customer_volume_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":12.04,"avg_MAE90_pct":-21.18,"avg_MFE180_pct":12.04,"avg_MAE180_pct":-41.00,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R9L85_C29_P2_CANONICAL","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P2_C29_volume_margin_cash_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C29 should reward operating leverage mechanics, not OEM turnaround or EV-parts theme spikes","changed_axes":["C29_volume_mix_margin_bridge_required","C29_OEM_turnaround_theme_penalty","C29_EV_parts_theme_local_4B_guard"],"changed_thresholds":{"stage2_yellow_gate":"volume_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":12.04,"avg_MAE90_pct":-21.18,"avg_MFE180_pct":12.04,"avg_MAE180_pct":-41.00,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R9L85_C29_P3_COUNTEREXAMPLE_GUARD","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P3_C29_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE180<=-35 while volume/margin bridge is missing, block Yellow/Green","changed_axes":["C29_high_MAE_guardrail","C29_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE180_le_minus_35"},"eligible_trigger_count":3,"avg_MFE90_pct":12.04,"avg_MAE90_pct":-21.18,"avg_MFE180_pct":12.04,"avg_MAE180_pct":-41.00,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_LOGISTICS_VOLUME_MARGIN_VS_OEM_EV_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":12.04,"avg_MAE90_pct":-21.18,"avg_MFE180_pct":12.04,"avg_MAE180_pct":-41.00,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE180_le_minus_35":0.67,"interpretation":"C29 needs bridge discipline. CJ대한통운 shows logistics throughput and margin bridge can support Watch/Yellow, while KG모빌리티 and 우리산업 show OEM turnaround or EV-parts theme spikes fail without mix, margin, customer volume and cash-conversion bridge."}
{"row_type":"stage_transition_summary","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"000120","trigger_type":"Stage2-Actionable-LogisticsVolumeMarginBridge-Positive","entry_date":"2024-01-19","stage2_to_90D_outcome":"good_stage2_moderate_MFE_low_initial_MAE","stage2_to_180D_outcome":"watch_positive_with_later_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Watch/Yellow when logistics volume and margin bridge exists; Green requires exact cash conversion and multi-quarter margin evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"003620","trigger_type":"Stage2-FalsePositive-OEMTurnaroundVolumeTheme-NoMarginBridge","entry_date":"2024-04-23","stage2_to_90D_outcome":"weak_stage2_low_MFE","stage2_to_180D_outcome":"failed_OEM_turnaround_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"OEM turnaround/volume theme without margin and cash conversion should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"215360","trigger_type":"Stage2-FalsePositive-EVThermalThemeSpike-NoCustomerVolumeBridge","entry_date":"2024-04-01","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_EV_parts_theme_extreme_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"EV thermal theme spike without customer/volume/margin bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"mobility_theme_overcredit_without_volume_mix_margin_cash_bridge","contribution":"Adds two C29 local 4B/high-MAE counterexamples against one logistics volume/margin bridge positive, avoiding C29 top-covered and previous R9 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"LOGISTICS_VOLUME_MARGIN_BRIDGE_VS_OEM_TURNAROUND_AND_EV_THERMAL_THEME_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C29 now has non-top-symbol OEM/EV-parts theme counterexamples and a logistics bridge control; next R9 loops should exact-URL repair volume, mix, margin, logistics throughput and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_volume_mix_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"000120 worked with logistics volume/margin bridge proxy; 003620 and 215360 failed when operating-leverage bridge was missing."}
{"row_type":"shadow_weight","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_OEM_EV_parts_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"OEM turnaround and EV-parts theme spikes showed low MFE and deep/extreme MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R9","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE180<=-35 while volume/margin/cash bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - mobility_theme_overcredit
  - OEM_turnaround_no_margin_cash_bridge
  - EV_parts_theme_no_customer_volume_bridge
  - low_MFE_deep_MAE_without_operating_leverage
new_axis_proposed:
  - C29_volume_mix_margin_cash_bridge_required_shadow_only
  - C29_OEM_EV_parts_theme_local_4B_watch_guard_shadow_only
  - C29_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C29
  - full_4b_requires_non_price_evidence within C29
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
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
   - R9 loop84 C29 symbols
   - previous-loop C29 symbols listed in the MD
6. If aggregate support remains stable after exact evidence URL repair, consider C29-scoped safe patch candidates:
   - C29_volume_mix_margin_cash_bridge_required
   - C29_OEM_EV_parts_theme_local_4B_watch_guard
   - C29_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R9
completed_loop = 85
next_round = R10
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.
```
