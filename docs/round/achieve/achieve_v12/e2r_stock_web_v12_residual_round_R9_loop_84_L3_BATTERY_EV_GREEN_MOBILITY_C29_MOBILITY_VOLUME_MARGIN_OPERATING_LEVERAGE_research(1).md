# E2R Stock-Web v12 Residual Research — R9 Loop 84 / L3 / C29

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R9
loop: 84
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: MOBILITY_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE_VS_TIRE_HYDROGEN_OPTIONALITY_SPIKE
sector: mobility / auto parts / logistics / tire / hydrogen mobility
output_file: e2r_stock_web_v12_residual_round_R9_loop_84_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R8 loop 84`.

```text
scheduled_round = R9
scheduled_loop = 84
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

R9 is the special mobility/transport lane. Although C29 is mapped under L3, the scheduler treats R9 as the mobility volume/mix/margin operating-leverage checkpoint.

This run avoids the C29 top-covered list from the No-Repeat ledger:

```text
011210, 000270, 005380, 005850, 010690, 018880
```

It also avoids the previous C29 loop83 symbols:

```text
012330, 002350, 204320
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"086280","company_name":"현대글로비스","profile_path":"atlas/symbol_profiles/086/086280.json","first_date":"2005-12-26","last_date":"2026-02-20","trading_day_count":4970,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2024-07-12","2024-08-02"],"has_major_raw_discontinuity":true,"calibration_caveat":"Entry is deliberately placed after the 2024-08-02 corporate-action candidate; forward window is treated as clean for selected entry.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"post_2024-08-02_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"161390","company_name":"한국타이어앤테크놀로지","profile_path":"atlas/symbol_profiles/161/161390.json","first_date":"2012-10-04","last_date":"2026-02-20","trading_day_count":3285,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"271940","company_name":"일진하이솔루스","profile_path":"atlas/symbol_profiles/271/271940.json","first_date":"2021-09-01","last_date":"2026-02-20","trading_day_count":1092,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"086280","trigger_type":"Stage2-Actionable-MobilityLogisticsVolumeMixBridge-Positive","entry_date":"2024-08-19","duplicate_status":"new C29 symbol/trigger/date combination; entry after 2024-08-02 corporate-action candidate"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"161390","trigger_type":"Stage2-FalsePositive-TireMarginPeak-NoVolumeMixBridge-HighMAE","entry_date":"2024-04-11","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"271940","trigger_type":"Stage2-FalsePositive-HydrogenMobilityOptionality-NoVolumeBridge","entry_date":"2024-05-22","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C29 is not an “auto theme” bucket. It is a bridge test: volume, mix, freight/logistics throughput, margin leverage, and cash conversion must move together. If only one wheel spins, the vehicle does not move.

Residual question:

```text
Can C29 distinguish:
1. post-corporate-action mobility logistics volume/mix bridge with slow but durable MFE,
2. tire margin/price peak that fails without volume/mix continuation,
3. hydrogen mobility optionality spike that fails without real volume/order/utilization bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C29_R9L84_086280_HYUNDAIGLOVIS_LOGISTICS_VOLUME_MIX_BRIDGE","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-MobilityLogisticsVolumeMixBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_slow_MFE_low_MAE","current_profile_verdict":"current_profile_correct_if_volume_mix_bridge_required","price_source":"Songdaiki/stock-web","notes":"Post-corporate-action entry avoids the July/August contamination window. Slow 90D and strong 180D MFE support volume/mix/logistics bridge but not automatic Green."}
{"row_type":"case","case_id":"C29_R9L84_161390_HANKOOKTIRE_MARGIN_PEAK_NO_BRIDGE","symbol":"161390","company_name":"한국타이어앤테크놀로지","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_MARGIN_PEAK_WITHOUT_VOLUME_MIX_CONTINUATION","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-TireMarginPeak-NoVolumeMixBridge-HighMAE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_tire_margin_peak_overcredited","price_source":"Songdaiki/stock-web","notes":"Tire margin/price peak had very small MFE and deep MAE. C29 should require volume/mix continuation and margin durability before Stage2-Actionable/Yellow."}
{"row_type":"case","case_id":"C29_R9L84_271940_ILJIN_HYDROGEN_MOBILITY_OPTIONALITY_NO_VOLUME_BRIDGE","symbol":"271940","company_name":"일진하이솔루스","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"HYDROGEN_MOBILITY_OPTIONALITY_WITHOUT_VOLUME_ORDER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HydrogenMobilityOptionality-NoVolumeBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_initial_MFE_then_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_hydrogen_optionality_overcredited","price_source":"Songdaiki/stock-web","notes":"Hydrogen mobility optionality had a short tradable bounce but failed without order/volume/utilization bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 086280 현대글로비스 — mobility logistics volume/mix bridge positive

Entry is placed after the `2024-08-02` corporate-action candidate.

Entry row: `2024-08-19 c=104700`.  
Forward path: `2024-09-30 h=125600`, `2024-10-25 h=127400`, and `2025-01-31 h=151000`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L84_C29_086280_20240819_STAGE2_MOBILITY_LOGISTICS_VOLUME_MIX_BRIDGE","case_id":"C29_R9L84_086280_HYUNDAIGLOVIS_LOGISTICS_VOLUME_MIX_BRIDGE","symbol":"086280","company_name":"현대글로비스","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;holdout_validation","trigger_type":"Stage2-Actionable-MobilityLogisticsVolumeMixBridge-Positive","trigger_date":"2024-08-19","entry_date":"2024-08-19","entry_price":104700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_volume_mix_logistics_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; mobility logistics volume/mix and margin bridge thesis treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["volume_mix_bridge_proxy","logistics_throughput_proxy","margin_leverage_proxy","relative_strength_turn"],"stage3_evidence_fields":["multi_quarter_volume_bridge_pending","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086280/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/086/086280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.96,"MFE_90D_pct":21.68,"MFE_180D_pct":44.22,"MAE_30D_pct":-0.76,"MAE_90D_pct":-0.76,"MAE_180D_pct":-0.76,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-31","peak_price":151000.0,"max_drawdown_low_date":"2024-08-19","max_drawdown_low":103900.0,"drawdown_after_peak_pct":-30.46,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_slow_MFE_low_MAE","current_profile_verdict":"current_profile_correct_if_volume_mix_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"entry_after_2024-08-02_candidate_clean_forward_window","same_entry_group_id":"086280_2024-08-19_104700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should allow Stage2/Yellow when volume/mix/logistics bridge has low MAE and strong 180D follow-through. Green still requires exact source repair and confirmed multi-quarter margin/cash conversion."}
```

### 6.2 161390 한국타이어앤테크놀로지 — tire margin peak without volume/mix continuation

Entry row: `2024-04-11 c=60500`.  
Forward path: near-term peak `2024-04-16 h=63300`, then collapse to `2024-05-07 l=42150`, `2024-08-05 l=37850`, and `2024-10-29 l=34500`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L84_C29_161390_20240411_STAGE2_FALSE_POSITIVE_TIRE_MARGIN_PEAK","case_id":"C29_R9L84_161390_HANKOOKTIRE_MARGIN_PEAK_NO_BRIDGE","symbol":"161390","company_name":"한국타이어앤테크놀로지","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TIRE_MARGIN_PEAK_WITHOUT_VOLUME_MIX_CONTINUATION","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-TireMarginPeak-NoVolumeMixBridge-HighMAE","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":60500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_tire_margin_peak_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; tire margin/price peak treated as insufficient unless volume/mix and margin durability are verified","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["tire_margin_peak_proxy","relative_strength_extension"],"stage3_evidence_fields":["volume_mix_bridge_missing","margin_durability_missing","inventory_channel_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_volume_slowdown_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv","profile_path":"atlas/symbol_profiles/161/161390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.63,"MFE_90D_pct":4.63,"MFE_180D_pct":4.63,"MAE_30D_pct":-30.33,"MAE_90D_pct":-37.44,"MAE_180D_pct":-42.98,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-16","peak_price":63300.0,"max_drawdown_low_date":"2024-10-29","max_drawdown_low":34500.0,"drawdown_after_peak_pct":-45.50,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_peak_without_volume_mix_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","margin_or_volume_slowdown_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_tire_margin_peak_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"161390_2024-04-11_60500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Tire margin peak alone is not C29 structural rerating. Without volume/mix continuation and margin durability, early relative strength becomes a high-MAE false positive."}
```

### 6.3 271940 일진하이솔루스 — hydrogen mobility optionality without volume bridge

Entry row: `2024-05-22 c=24500`.  
Forward path: local peak `2024-05-28 h=28400`, then decay to `2024-10-02 l=20700` and `2024-12-09 l=16090`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L84_C29_271940_20240522_STAGE2_FALSE_POSITIVE_HYDROGEN_OPTIONALITY","case_id":"C29_R9L84_271940_ILJIN_HYDROGEN_MOBILITY_OPTIONALITY_NO_VOLUME_BRIDGE","symbol":"271940","company_name":"일진하이솔루스","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"HYDROGEN_MOBILITY_OPTIONALITY_WITHOUT_VOLUME_ORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-HydrogenMobilityOptionality-NoVolumeBridge","trigger_date":"2024-05-22","entry_date":"2024-05-22","entry_price":24500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_hydrogen_mobility_optionality_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; hydrogen mobility/tank optionality treated as insufficient unless order, volume, utilization, and margin bridge are verified","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["hydrogen_mobility_optionality","relative_strength_rebound"],"stage3_evidence_fields":["order_bridge_missing","volume_bridge_missing","utilization_bridge_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/271/271940/2024.csv","profile_path":"atlas/symbol_profiles/271/271940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.92,"MFE_90D_pct":15.92,"MFE_180D_pct":15.92,"MAE_30D_pct":-12.86,"MAE_90D_pct":-15.51,"MAE_180D_pct":-34.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":28400.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":16090.0,"drawdown_after_peak_pct":-43.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"initial_optionality_peak_without_volume_order_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_initial_MFE_then_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_hydrogen_optionality_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"271940_2024-05-22_24500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Hydrogen mobility optionality can produce a short bounce, but without real order, volume, utilization, and margin bridge it decays into a deep 180D MAE false positive."}
```

## 7. Score simulation rows

These rows are research proxy simulations only and do not change production scoring.

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L84_086280_HYUNDAIGLOVIS_LOGISTICS_VOLUME_MIX_BRIDGE","trigger_id":"R9L84_C29_086280_20240819_STAGE2_MOBILITY_LOGISTICS_VOLUME_MIX_BRIDGE","symbol":"086280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C29 recognizes volume/mix/logistics bridge after corporate-action window is clean","raw_component_scores_before":{"volume_bridge_score":13,"mix_margin_score":12,"operating_leverage_score":11,"customer_or_channel_quality":10,"capital_return_or_cash_conversion":8,"relative_strength_score":10,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":71,"stage_label_before":"Stage2-Watch/Yellow-candidate","raw_component_scores_after":{"volume_bridge_score":16,"mix_margin_score":15,"operating_leverage_score":13,"customer_or_channel_quality":12,"capital_return_or_cash_conversion":10,"relative_strength_score":12,"valuation_repricing_score":9,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Low MAE and strong 180D MFE support C29 bridge upgrade, but exact volume/margin/cash evidence blocks Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L84_161390_HANKOOKTIRE_MARGIN_PEAK_NO_BRIDGE","trigger_id":"R9L84_C29_161390_20240411_STAGE2_FALSE_POSITIVE_TIRE_MARGIN_PEAK","symbol":"161390","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"tire margin peak without volume/mix bridge should be blocked","raw_component_scores_before":{"volume_bridge_score":5,"mix_margin_score":9,"operating_leverage_score":7,"customer_or_channel_quality":5,"capital_return_or_cash_conversion":4,"relative_strength_score":12,"valuation_repricing_score":7,"execution_risk_score":-12,"theme_spike_risk":-9,"information_confidence":4},"weighted_score_before":41,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"volume_bridge_score":2,"mix_margin_score":3,"operating_leverage_score":2,"customer_or_channel_quality":3,"capital_return_or_cash_conversion":2,"relative_strength_score":4,"valuation_repricing_score":3,"execution_risk_score":-18,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and deep MAE convert tire margin peak into volume/mix bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L84_271940_ILJIN_HYDROGEN_MOBILITY_OPTIONALITY_NO_VOLUME_BRIDGE","trigger_id":"R9L84_C29_271940_20240522_STAGE2_FALSE_POSITIVE_HYDROGEN_OPTIONALITY","symbol":"271940","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"hydrogen mobility optionality without volume/order bridge should remain Watch/4B-risk","raw_component_scores_before":{"volume_bridge_score":4,"mix_margin_score":3,"operating_leverage_score":3,"customer_or_channel_quality":4,"capital_return_or_cash_conversion":2,"relative_strength_score":11,"valuation_repricing_score":7,"execution_risk_score":-10,"theme_spike_risk":-10,"information_confidence":3},"weighted_score_before":34,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"volume_bridge_score":1,"mix_margin_score":1,"operating_leverage_score":1,"customer_or_channel_quality":2,"capital_return_or_cash_conversion":1,"relative_strength_score":5,"valuation_repricing_score":3,"execution_risk_score":-16,"theme_spike_risk":-16,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Initial optionality MFE cannot compensate for missing volume/order/utilization bridge and deep 180D MAE."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R9L84_C29_P0_CURRENT","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C29 needs explicit volume/mix/margin bridge distinction","eligible_trigger_count":3,"avg_MFE_90D_pct":14.08,"avg_MAE_90D_pct":-17.90,"avg_MFE_180D_pct":21.59,"avg_MAE_180D_pct":-26.02,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C29_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R9L84_C29_P1_SECTOR_SPECIFIC","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P1_L3_mobility_volume_mix_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"mobility signals need volume, mix, margin, order, or logistics throughput bridge before Stage2-Actionable","changed_axes":["volume_bridge_required","mix_margin_bridge_required","optionality_spike_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_volume_mix_margin_or_logistics_proxy"},"eligible_trigger_count":3,"avg_MFE_90D_pct":14.08,"avg_MAE_90D_pct":-17.90,"avg_MFE_180D_pct":21.59,"avg_MAE_180D_pct":-26.02,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R9L84_C29_P2_CANONICAL","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P2_C29_volume_mix_margin_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C29 should reward real mobility operating leverage, not tire/hydrogen optionality spikes","changed_axes":["C29_volume_mix_margin_bridge_required","C29_tire_peak_penalty","C29_hydrogen_optionality_penalty"],"changed_thresholds":{"stage2_yellow_gate":"volume_mix_margin_or_logistics_bridge_required"},"eligible_trigger_count":3,"avg_MFE_90D_pct":14.08,"avg_MAE_90D_pct":-17.90,"avg_MFE_180D_pct":21.59,"avg_MAE_180D_pct":-26.02,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R9L84_C29_P3_COUNTEREXAMPLE_GUARD","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P3_C29_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<20 and MAE180<=-30 while volume/mix/margin bridge is missing, block Yellow/Green","changed_axes":["C29_high_MAE_guardrail","C29_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_20_and_MAE180_le_minus_30"},"eligible_trigger_count":3,"avg_MFE_90D_pct":14.08,"avg_MAE_90D_pct":-17.90,"avg_MFE_180D_pct":21.59,"avg_MAE_180D_pct":-26.02,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_VOLUME_MIX_MARGIN_BRIDGE_VS_OPTIONALITY_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":14.08,"avg_MAE90_pct":-17.90,"avg_MFE180_pct":21.59,"avg_MAE180_pct":-26.02,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.33,"stage2_bad_entry_rate_MAE180_le_minus_30":0.67,"interpretation":"C29 needs bridge discipline. 현대글로비스 shows a clean low-MAE volume/logistics bridge after corporate-action window, while 한국타이어앤테크놀로지 and 일진하이솔루스 show price/optionality peaks that fail without volume/mix/margin bridge."}
{"row_type":"stage_transition_summary","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"086280","trigger_type":"Stage2-Actionable-MobilityLogisticsVolumeMixBridge-Positive","entry_date":"2024-08-19","stage2_to_90D_outcome":"good_stage2_slow_MFE_low_MAE","stage2_to_180D_outcome":"positive_re_rating_path","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when volume/mix/logistics bridge exists; Green requires exact source and cash/margin evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"161390","trigger_type":"Stage2-FalsePositive-TireMarginPeak-NoVolumeMixBridge-HighMAE","entry_date":"2024-04-11","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_entry_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Tire margin/price peak without volume/mix continuation should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"271940","trigger_type":"Stage2-FalsePositive-HydrogenMobilityOptionality-NoVolumeBridge","entry_date":"2024-05-22","stage2_to_90D_outcome":"mixed_stage2_initial_MFE_but_weak_bridge","stage2_to_180D_outcome":"failed_entry_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Hydrogen mobility optionality needs order/volume/utilization bridge; otherwise initial MFE should not upgrade to Yellow/Green."}
{"row_type":"residual_contribution","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"mobility_optionality_or_margin_peak_overcredit_without_volume_mix_margin_bridge","contribution":"Adds two C29 high-MAE residual counterexamples against one post-corporate-action volume/logistics bridge positive, avoiding top-covered auto OEM and previous-loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE_VS_TIRE_HYDROGEN_OPTIONALITY_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C29 now has non-top-symbol tire/hydrogen optionality counterexamples and a post-corporate-action logistics bridge positive; next R9 loops should exact-URL repair volume/mix/margin evidence and add true 4C demand-break rows."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_volume_mix_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"086280 worked only when volume/mix/logistics bridge proxy was present; 161390 and 271940 failed without volume/mix/order/utilization bridge."}
{"row_type":"shadow_weight","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_optionality_or_margin_peak_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Tire margin peak and hydrogen optionality generated local peaks but became deep MAE when non-price operating bridge was missing."}
{"row_type":"shadow_weight","round":"R9","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<20 and MAE180<=-30 while volume/mix/margin bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
residual_error_types_found:
  - mobility_optionality_overcredit
  - tire_margin_peak_no_volume_mix_continuation
  - hydrogen_mobility_optionality_no_order_volume_bridge
new_axis_proposed:
  - C29_volume_mix_margin_bridge_required_shadow_only
  - C29_optionality_or_margin_peak_local_4B_watch_guard_shadow_only
  - C29_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C29
  - full_4b_requires_non_price_evidence within C29
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
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
5. Confirm 086280 entry is after the 2024-08-02 corporate-action candidate.
6. If aggregate support remains stable after exact evidence URL repair, consider C29-scoped safe patch candidates:
   - C29_volume_mix_margin_bridge_required
   - C29_optionality_or_margin_peak_local_4B_watch_guard
   - C29_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R9
completed_loop = 84
next_round = R10
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.
```
