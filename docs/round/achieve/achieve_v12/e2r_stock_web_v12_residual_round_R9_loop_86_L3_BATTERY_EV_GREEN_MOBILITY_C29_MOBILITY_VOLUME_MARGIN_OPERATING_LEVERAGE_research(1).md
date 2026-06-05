# E2R Stock-Web v12 Residual Research — R9 Loop 86 / L3 / C29

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R9
loop: 86
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: TIRE_VOLUME_MARGIN_BRIDGE_VS_AUTONOMOUS_EV_PARTS_AND_SMALLCAP_HYDROGEN_THEME_DECAY
sector: mobility / tire / auto parts / autonomous-driving / hydrogen parts / operating leverage
output_file: e2r_stock_web_v12_residual_round_R9_loop_86_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R8 loop 86`.

```text
scheduled_round = R9
scheduled_loop = 86
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

R9 is the mobility / transport / operating-leverage lane.  
C29 is selected again, but this loop deliberately avoids the C29 top-covered list:

```text
011210, 000270, 005380, 005850, 010690, 018880
```

It also avoids the earlier C29 sets already used in this session:

```text
R9 loop85: 000120, 003620, 215360
R9 loop84: 086280, 161390, 271940
earlier known C29 set: 012330, 002350, 204320
```

This loop tests a different C29 pocket: tire volume/mix/margin bridge versus autonomous-driving/EV-parts or small-cap hydrogen/auto-parts theme rebounds without volume and margin conversion.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"073240","company_name":"금호타이어","profile_path":"atlas/symbol_profiles/073/073240.json","first_date":"2005-02-17","last_date":"2026-02-20","trading_day_count":5170,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2010-11-02","2010-12-14","2018-07-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"118990","company_name":"모트렉스","profile_path":"atlas/symbol_profiles/118/118990.json","first_date":"2017-08-04","last_date":"2026-02-20","trading_day_count":2075,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2018-08-22","2022-04-29","2022-06-02","2022-06-27"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"090080","company_name":"평화산업","profile_path":"atlas/symbol_profiles/090/090080.json","first_date":"2006-06-02","last_date":"2026-02-20","trading_day_count":4844,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2008-05-26","2009-07-22","2014-05-21","2019-08-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"073240","trigger_type":"Stage2-Actionable-TireVolumeMixMarginBridge-Positive","entry_date":"2024-01-25","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"118990","trigger_type":"Stage2-FalsePositive-AutonomousEVPartsTheme-NoVolumeMarginBridge","entry_date":"2024-04-30","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"090080","trigger_type":"Stage2-FalsePositive-SmallcapHydrogenAutoPartsTheme-NoCustomerVolumeBridge","entry_date":"2024-02-02","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
```

## 4. Research question

C29 is not “mobility stock moved.”  
The useful signal is the operating-leverage bridge: volume, mix, pricing, utilization, customer quality, margin expansion, and cash conversion. The bridge is the axle. Without it, the wheel spins in place.

Residual question:

```text
Can C29 distinguish:
1. tire volume/mix/margin bridge with strong MFE and tolerable MAE,
2. autonomous/EV-parts theme rebound where the price spike is not backed by customer volume or margin conversion,
3. small-cap hydrogen/auto-parts theme where there is no durable volume/mix/cash bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C29_R9L86_073240_KUMHOTIRE_VOLUME_MIX_MARGIN","symbol":"073240","company_name":"금호타이어","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_VOLUME_MIX_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-TireVolumeMixMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct_if_volume_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Tire volume/mix/margin proxy produced strong 90D MFE and low forward MAE. Green still requires exact export volume, mix, margin and cash evidence."}
{"row_type":"case","case_id":"C29_R9L86_118990_MOTREX_EV_AUTONOMOUS_THEME","symbol":"118990","company_name":"모트렉스","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTONOMOUS_EV_PARTS_THEME_WITHOUT_VOLUME_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AutonomousEVPartsTheme-NoVolumeMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_EV_parts_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Autonomous/EV-parts theme spike produced limited MFE and deep 180D drawdown without customer volume, utilization and margin bridge."}
{"row_type":"case","case_id":"C29_R9L86_090080_PYEONGHWA_HYDROGEN_AUTOPARTS_THEME","symbol":"090080","company_name":"평화산업","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SMALLCAP_HYDROGEN_AUTOPARTS_THEME_WITHOUT_CUSTOMER_VOLUME_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallcapHydrogenAutoPartsTheme-NoCustomerVolumeBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_hydrogen_autoparts_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Small-cap hydrogen/auto-parts theme had almost no MFE and large MAE without customer-volume and margin bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 073240 금호타이어 — tire volume/mix/margin bridge positive

Entry row: `2024-01-25 c=5900`.  
Observed path: early low `2024-01-29 l=5590`, 30D high `2024-02-19 h=6880`, 90D high `2024-05-07 h=8360`, and later low around `2024-07-18 l=5410`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L86_C29_073240_20240125_STAGE2_TIRE_VOLUME_MARGIN","case_id":"C29_R9L86_073240_KUMHOTIRE_VOLUME_MIX_MARGIN","symbol":"073240","company_name":"금호타이어","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_VOLUME_MIX_MARGIN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-TireVolumeMixMarginBridge-Positive","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":5900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_tire_volume_mix_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; tire volume/mix/margin and operating-leverage bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["tire_volume_proxy","mix_margin_proxy","export_demand_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_margin_bridge_pending","cash_conversion_pending","channel_inventory_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv","profile_path":"atlas/symbol_profiles/073/073240.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.61,"MFE_90D_pct":41.69,"MFE_180D_pct":41.69,"MAE_30D_pct":-5.25,"MAE_90D_pct":-5.42,"MAE_180D_pct":-8.31,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":8360.0,"max_drawdown_low_date":"2024-07-18","max_drawdown_low":5410.0,"drawdown_after_peak_pct":-35.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct_if_volume_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"073240_2024-01-25_5900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 can allow Stage2/Yellow when tire price strength is tied to volume, mix, margin and export-demand bridge. Green still requires exact margin and cash-conversion evidence."}
```

### 6.2 118990 모트렉스 — autonomous/EV-parts theme without volume/margin bridge

Entry row: `2024-04-30 c=14480`.  
Observed path: same-day high `h=15840`, then lows around `2024-07-22 l=12210`, `2024-10-22 l=9870`, and `2024-12-09 l=8770`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L86_C29_118990_20240430_STAGE2_FALSE_POSITIVE_AUTONOMOUS_EV_PARTS","case_id":"C29_R9L86_118990_MOTREX_EV_AUTONOMOUS_THEME","symbol":"118990","company_name":"모트렉스","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTONOMOUS_EV_PARTS_THEME_WITHOUT_VOLUME_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-AutonomousEVPartsTheme-NoVolumeMarginBridge","trigger_date":"2024-04-30","entry_date":"2024-04-30","entry_price":14480.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_autonomous_EV_parts_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; autonomous/EV-parts theme treated as insufficient without customer volume, utilization, mix and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["autonomous_EV_parts_theme","relative_strength_spike"],"stage3_evidence_fields":["customer_volume_bridge_missing","utilization_bridge_missing","margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/118/118990/2024.csv","profile_path":"atlas/symbol_profiles/118/118990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.39,"MFE_90D_pct":9.39,"MFE_180D_pct":9.39,"MAE_30D_pct":-8.08,"MAE_90D_pct":-18.44,"MAE_180D_pct":-39.43,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-30","peak_price":15840.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":8770.0,"drawdown_after_peak_pct":-44.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"autonomous_EV_parts_theme_without_volume_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_EV_parts_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"118990_2024-04-30_14480","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not upgrade autonomous/EV-parts price spikes without customer volume, utilization and margin bridge. Low MFE and deep 180D MAE support Watch/4B-risk."}
```

### 6.3 090080 평화산업 — small-cap hydrogen/auto-parts theme without customer-volume bridge

Entry row: `2024-02-02 c=1298`.  
Observed path: same-day high `h=1309`, then lows `2024-04-15 l=1115`, `2024-07-22 l=1105`, and `2024-12-10 l=760`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L86_C29_090080_20240202_STAGE2_FALSE_POSITIVE_HYDROGEN_AUTOPARTS","case_id":"C29_R9L86_090080_PYEONGHWA_HYDROGEN_AUTOPARTS_THEME","symbol":"090080","company_name":"평화산업","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SMALLCAP_HYDROGEN_AUTOPARTS_THEME_WITHOUT_CUSTOMER_VOLUME_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-SmallcapHydrogenAutoPartsTheme-NoCustomerVolumeBridge","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":1298.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_hydrogen_auto_parts_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small-cap hydrogen/auto-parts theme treated as insufficient without customer volume, order quality, utilization and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["hydrogen_auto_parts_theme","relative_strength_rebound"],"stage3_evidence_fields":["customer_volume_bridge_missing","order_quality_missing","utilization_bridge_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","customer_volume_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090080/2024.csv","profile_path":"atlas/symbol_profiles/090/090080.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.85,"MFE_90D_pct":0.85,"MFE_180D_pct":0.85,"MAE_30D_pct":-14.10,"MAE_90D_pct":-14.87,"MAE_180D_pct":-41.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":1309.0,"max_drawdown_low_date":"2024-12-10","max_drawdown_low":760.0,"drawdown_after_peak_pct":-41.94,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smallcap_hydrogen_autoparts_theme_without_customer_volume_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","customer_volume_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_hydrogen_autoparts_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"090080_2024-02-02_1298","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not promote hydrogen/auto-parts theme rebounds unless customer volume, order quality, utilization and margin bridge are present. Near-zero MFE and deep later MAE support Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C29_R9L86_073240_KUMHOTIRE_VOLUME_MIX_MARGIN","trigger_id":"R9L86_C29_073240_20240125_STAGE2_TIRE_VOLUME_MARGIN","symbol":"073240","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C29 requires volume/mix/margin bridge rather than mobility theme alone","raw_component_scores_before":{"volume_bridge_score":13,"mix_margin_score":13,"operating_leverage_score":12,"customer_or_channel_quality":9,"cash_conversion_score":7,"relative_strength_score":11,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Watch/Yellow-candidate","raw_component_scores_after":{"volume_bridge_score":16,"mix_margin_score":16,"operating_leverage_score":14,"customer_or_channel_quality":11,"cash_conversion_score":9,"relative_strength_score":12,"valuation_repricing_score":9,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Volume/mix/margin bridge and low MAE support Yellow-watch; exact margin/cash evidence still blocks Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C29_R9L86_118990_MOTREX_EV_AUTONOMOUS_THEME","trigger_id":"R9L86_C29_118990_20240430_STAGE2_FALSE_POSITIVE_AUTONOMOUS_EV_PARTS","symbol":"118990","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"autonomous/EV-parts theme without customer-volume and margin bridge should be blocked","raw_component_scores_before":{"volume_bridge_score":4,"mix_margin_score":2,"operating_leverage_score":3,"customer_or_channel_quality":2,"cash_conversion_score":1,"relative_strength_score":12,"valuation_repricing_score":6,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":20,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"volume_bridge_score":0,"mix_margin_score":0,"operating_leverage_score":0,"customer_or_channel_quality":0,"cash_conversion_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep 180D MAE convert the EV-parts theme into missing-bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C29_R9L86_090080_PYEONGHWA_HYDROGEN_AUTOPARTS_THEME","trigger_id":"R9L86_C29_090080_20240202_STAGE2_FALSE_POSITIVE_HYDROGEN_AUTOPARTS","symbol":"090080","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"small-cap hydrogen/auto-parts theme without customer volume bridge should remain Watch/blocked","raw_component_scores_before":{"volume_bridge_score":2,"mix_margin_score":1,"operating_leverage_score":1,"customer_or_channel_quality":1,"cash_conversion_score":0,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"volume_bridge_score":0,"mix_margin_score":0,"operating_leverage_score":0,"customer_or_channel_quality":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-20,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Near-zero MFE and deep 180D MAE require customer-volume and margin bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R9L86_C29_P0_CURRENT","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C29 needs explicit volume/mix/margin/customer bridge distinction across tires, EV-parts and hydrogen parts","eligible_trigger_count":3,"avg_MFE90_pct":17.31,"avg_MAE90_pct":-12.91,"avg_MFE180_pct":17.31,"avg_MAE180_pct":-29.73,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C29_volume_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R9L86_C29_P1_SECTOR_SPECIFIC","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P1_L3_mobility_volume_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"Mobility signals need volume, mix, margin, utilization, customer volume or cash bridge before Stage2-Actionable","changed_axes":["volume_mix_bridge_required","margin_cash_bridge_required","theme_beta_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_volume_mix_margin_customer_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":17.31,"avg_MAE90_pct":-12.91,"avg_MFE180_pct":17.31,"avg_MAE180_pct":-29.73,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R9L86_C29_P2_CANONICAL","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P2_C29_volume_mix_margin_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C29 should reward operating leverage mechanics, not EV-parts or hydrogen/auto-parts theme spikes","changed_axes":["C29_volume_mix_margin_bridge_required","C29_theme_beta_local_4B_guard","C29_deep_180D_MAE_guard"],"changed_thresholds":{"stage2_yellow_gate":"volume_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":17.31,"avg_MAE90_pct":-12.91,"avg_MFE180_pct":17.31,"avg_MAE180_pct":-29.73,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R9L86_C29_P3_COUNTEREXAMPLE_GUARD","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P3_C29_deep_180D_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE180<=-35 while volume/margin bridge is missing, block Yellow/Green","changed_axes":["C29_deep_180D_MAE_guardrail","C29_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE180_le_minus_35"},"eligible_trigger_count":3,"avg_MFE90_pct":17.31,"avg_MAE90_pct":-12.91,"avg_MFE180_pct":17.31,"avg_MAE180_pct":-29.73,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_TIRE_VOLUME_MARGIN_VS_EV_HYDROGEN_THEME","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":17.31,"avg_MAE90_pct":-12.91,"avg_MFE180_pct":17.31,"avg_MAE180_pct":-29.73,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE180_le_minus_35":0.67,"interpretation":"C29 needs bridge discipline. 금호타이어 shows a tire volume/mix/margin bridge can rerate with low MAE, while 모트렉스 and 평화산업 show EV/autonomous/hydrogen auto-parts themes can fail without customer volume, utilization and margin conversion."}
{"row_type":"stage_transition_summary","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"073240","trigger_type":"Stage2-Actionable-TireVolumeMixMarginBridge-Positive","entry_date":"2024-01-25","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_tire_volume_margin_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when tire volume, mix, margin and export-demand bridge exists; Green requires exact cash and multi-quarter margin evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"118990","trigger_type":"Stage2-FalsePositive-AutonomousEVPartsTheme-NoVolumeMarginBridge","entry_date":"2024-04-30","stage2_to_90D_outcome":"weak_stage2_low_MFE","stage2_to_180D_outcome":"failed_EV_parts_theme_deep_MAE","MFE90_ge_20":false,"MAE180_le_minus_35":true,"transition_note":"Autonomous/EV-parts theme without customer-volume and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"090080","trigger_type":"Stage2-FalsePositive-SmallcapHydrogenAutoPartsTheme-NoCustomerVolumeBridge","entry_date":"2024-02-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE","stage2_to_180D_outcome":"failed_hydrogen_autoparts_theme_deep_MAE","MFE90_ge_20":false,"MAE180_le_minus_35":true,"transition_note":"Small-cap hydrogen/auto-parts theme without customer-volume/margin bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"mobility_EV_hydrogen_theme_overcredit_without_volume_mix_margin_bridge","contribution":"Adds two C29 local 4B/deep-MAE counterexamples against one tire volume/margin bridge positive, avoiding C29 top-covered and previous C29 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_VOLUME_MARGIN_BRIDGE_VS_AUTONOMOUS_EV_PARTS_AND_SMALLCAP_HYDROGEN_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C29 now has non-top-symbol EV/hydrogen auto-parts theme counterexamples plus a tire margin control; next R9 loops should exact-URL repair volume, mix, utilization, customer quality, margin and cash evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_volume_mix_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"073240 worked with tire volume/mix/margin proxy; 118990 and 090080 failed when only EV/autonomous/hydrogen auto-parts theme existed."}
{"row_type":"shadow_weight","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_EV_hydrogen_parts_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"EV/autonomous and hydrogen/auto-parts theme rows had low or near-zero MFE and deep 180D MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R9","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_deep_180D_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE180<=-35 while volume/margin bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - EV_autonomous_parts_theme_overcredit
  - hydrogen_autoparts_theme_no_customer_volume_bridge
  - volume_mix_margin_bridge_missing
  - deep_180D_MAE_without_operating_leverage
new_axis_proposed:
  - C29_volume_mix_margin_bridge_required_shadow_only
  - C29_EV_hydrogen_parts_theme_local_4B_watch_guard_shadow_only
  - C29_deep_180D_MAE_guardrail_shadow_only
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
   - R9 loop85 C29 symbols
   - R9 loop84 C29 symbols
   - earlier C29 symbols listed in the MD
6. If aggregate support remains stable after exact evidence URL repair, consider C29-scoped safe patch candidates:
   - C29_volume_mix_margin_bridge_required
   - C29_EV_hydrogen_parts_theme_local_4B_watch_guard
   - C29_deep_180D_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R9
completed_loop = 86
next_round = R10
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.
```
