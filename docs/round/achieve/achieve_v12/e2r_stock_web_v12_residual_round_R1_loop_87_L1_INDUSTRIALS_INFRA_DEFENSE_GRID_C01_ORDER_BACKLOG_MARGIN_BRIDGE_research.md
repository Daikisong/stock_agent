# E2R Stock-Web v12 Residual Research — R1 Loop 87 / L1 / C01

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R1
loop: 87
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_VS_SHIPBUILDING_THEME_WITHOUT_CASH_CONVERSION
sector: industrials / order backlog / shipbuilding supply chain / margin bridge
output_file: e2r_stock_web_v12_residual_round_R1_loop_87_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R13 loop 86`.

```text
scheduled_round = R1
scheduled_loop = 87
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

R1 is restricted to L1 industrials / infra / defense / grid.  
C01 is selected because the recent L1 sequence already covered C04 nuclear, C05 EPC, C03 defense, and C02 power-grid. C01 is the core industrial order-backlog and margin-conversion bucket.

The No-Repeat Index shows C01 as:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE
rows = 25
symbols = 14
good/bad Stage2 = 16/4
4B/4C = 1/0
top-covered = 042660, 071970, 100090, 329180, 010140, 009540
```

This loop avoids those top-covered symbols and uses a fresh non-top-covered set:

```text
082740, 097230, 044450
```

It also avoids the immediately recent L1 loop symbols from C05/C03/C02/C04 evidence families.  
This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"082740","company_name":"한화엔진","profile_path":"atlas/symbol_profiles/082/082740.json","first_date":"2011-01-04","last_date":"2026-02-20","trading_day_count":3710,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2018-06-19","2021-03-17","2022-08-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here. Name changed from HSD엔진 to 한화엔진 on 2024-03-15 without a 2024 corporate-action candidate.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"097230","company_name":"HJ중공업","profile_path":"atlas/symbol_profiles/097/097230.json","first_date":"2007-08-31","last_date":"2026-02-20","trading_day_count":4493,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2013-04-05","2014-08-29","2019-05-21","2019-05-23"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"044450","company_name":"KSS해운","profile_path":"atlas/symbol_profiles/044/044450.json","first_date":"2007-10-26","last_date":"2026-02-20","trading_day_count":4511,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2008-05-13","2016-10-04","2016-10-21"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"082740","trigger_type":"Stage2-Actionable-ShipEngineOrderBacklogMarginBridge-Positive","entry_date":"2024-03-14","duplicate_status":"new C01 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"097230","trigger_type":"Stage2-FalsePositive-ShipbuildingBacklogTheme-NoMarginCashBridge","entry_date":"2024-02-07","duplicate_status":"new C01 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"044450","trigger_type":"Stage2-FalsePositive-ShippingBacklogTheme-NoFreshOrderMarginBridge","entry_date":"2024-01-17","duplicate_status":"new C01 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C01 is not “orders are large.” The backlog must become margin.  
A shipbuilding or industrial backlog label is only the warehouse shelf; E2R needs to see whether the shelf is stocked with good-margin work, delivery visibility, customer quality, pricing power, capacity utilization, cost control, and cash conversion.

Residual question:

```text
Can C01 distinguish:
1. ship-engine order backlog and margin bridge with high MFE,
2. shipbuilding backlog theme where price fails because margin and cash conversion are missing,
3. shipping/backlog theme where an initial price spike lacks fresh order and margin bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C01_R1L87_082740_HANWHA_ENGINE_ORDER_BACKLOG_MARGIN","symbol":"082740","company_name":"한화엔진","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ShipEngineOrderBacklogMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_order_backlog_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Ship-engine order/backlog and margin proxy produced strong MFE with tolerable early MAE. Green still requires exact order mix, margin, utilization and cash evidence."}
{"row_type":"case","case_id":"C01_R1L87_097230_HJ_SHIPBUILDING_BACKLOG_THEME","symbol":"097230","company_name":"HJ중공업","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_THEME_WITHOUT_MARGIN_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ShipbuildingBacklogTheme-NoMarginCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_backlog_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Shipbuilding/backlog theme did not convert into price path until much later; within the trigger window, MFE was near zero and MAE opened deeply."}
{"row_type":"case","case_id":"C01_R1L87_044450_KSS_SHIPPING_BACKLOG_THEME","symbol":"044450","company_name":"KSS해운","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPPING_BACKLOG_THEME_WITHOUT_FRESH_ORDER_MARGIN_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ShippingBacklogTheme-NoFreshOrderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_initial_MFE_below_Yellow_threshold_medium_MAE","current_profile_verdict":"current_profile_false_positive_if_shipping_backlog_theme_promoted_without_fresh_bridge","price_source":"Songdaiki/stock-web","notes":"Shipping/backlog theme had an initial spike but failed to clear a strong Stage2/Yellow path without fresh order, margin and cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 082740 한화엔진 — ship-engine order backlog / margin bridge positive

Entry row: `2024-03-14 c=9570`.  
Observed path: entry-day low `2024-03-14 l=8770`, 30D high `2024-04-24 h=13890`, 90D high `2024-06-25 h=16990`, and later high `2024-11-25 h=18340`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L87_C01_082740_20240314_STAGE2_SHIP_ENGINE_BACKLOG_MARGIN","case_id":"C01_R1L87_082740_HANWHA_ENGINE_ORDER_BACKLOG_MARGIN","symbol":"082740","company_name":"한화엔진","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ShipEngineOrderBacklogMarginBridge-Positive","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":9570.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_ship_engine_order_backlog_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; ship-engine backlog, customer order mix and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["order_backlog_proxy","ship_engine_demand_proxy","margin_bridge_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_order_mix_pending","utilization_bridge_pending","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/082/082740/2024.csv","profile_path":"atlas/symbol_profiles/082/082740.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":45.14,"MFE_90D_pct":77.53,"MFE_180D_pct":91.64,"MAE_30D_pct":-8.36,"MAE_90D_pct":-8.36,"MAE_180D_pct":-8.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-25","peak_price":18340.0,"max_drawdown_low_date":"2024-03-14","max_drawdown_low":8770.0,"drawdown_after_peak_pct":-23.45,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_order_backlog_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; name_change_only_on_2024-03-15","same_entry_group_id":"082740_2024-03-14_9570","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C01 can allow Stage2/Yellow when order backlog is tied to engine demand, utilization, margin and cash bridge. Green still requires exact order mix and cash conversion evidence."}
```

### 6.2 097230 HJ중공업 — shipbuilding backlog theme without margin/cash bridge

Entry row: `2024-02-07 c=3735`.  
Observed path: early peak remained near entry, while lows opened at `2024-04-16 l=2875` and later `2024-10-31 l=2180`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L87_C01_097230_20240207_STAGE2_FALSE_POSITIVE_SHIPBUILDING_BACKLOG","case_id":"C01_R1L87_097230_HJ_SHIPBUILDING_BACKLOG_THEME","symbol":"097230","company_name":"HJ중공업","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_BACKLOG_THEME_WITHOUT_MARGIN_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-ShipbuildingBacklogTheme-NoMarginCashBridge","trigger_date":"2024-02-07","entry_date":"2024-02-07","entry_price":3735.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_shipbuilding_backlog_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; backlog theme treated as insufficient without fresh order quality, margin and cash conversion bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["shipbuilding_backlog_theme","relative_strength_rebound"],"stage3_evidence_fields":["fresh_order_quality_missing","margin_bridge_missing","cash_conversion_missing","cost_overrun_risk_unresolved"],"stage4b_evidence_fields":["price_only_local_peak","margin_cash_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv","profile_path":"atlas/symbol_profiles/097/097230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.0,"MFE_90D_pct":1.34,"MFE_180D_pct":1.34,"MAE_30D_pct":-12.99,"MAE_90D_pct":-23.03,"MAE_180D_pct":-41.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":3785.0,"max_drawdown_low_date":"2024-10-31","max_drawdown_low":2180.0,"drawdown_after_peak_pct":-42.40,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"shipbuilding_backlog_theme_without_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","margin_cash_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_backlog_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"097230_2024-02-07_3735","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C01 should not upgrade backlog labels without margin and cash bridge. The forward path had near-zero MFE and deep MAE before any late rebound appeared."}
```

### 6.3 044450 KSS해운 — shipping/backlog theme without fresh order/margin bridge

Entry row: `2024-01-17 c=9510`.  
Observed path: same-day high `2024-01-17 h=10840`, then lows around `2024-04-08 l=7970`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L87_C01_044450_20240117_STAGE2_FALSE_POSITIVE_SHIPPING_BACKLOG_THEME","case_id":"C01_R1L87_044450_KSS_SHIPPING_BACKLOG_THEME","symbol":"044450","company_name":"KSS해운","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPPING_BACKLOG_THEME_WITHOUT_FRESH_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-ShippingBacklogTheme-NoFreshOrderMarginBridge","trigger_date":"2024-01-17","entry_date":"2024-01-17","entry_price":9510.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_shipping_backlog_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; shipping/backlog theme treated as insufficient without fresh order, contract margin, utilization and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["shipping_backlog_theme","relative_strength_spike"],"stage3_evidence_fields":["fresh_order_bridge_missing","margin_bridge_missing","cash_conversion_missing","utilization_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","fresh_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/044/044450/2024.csv","profile_path":"atlas/symbol_profiles/044/044450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.99,"MFE_90D_pct":13.99,"MFE_180D_pct":13.99,"MAE_30D_pct":-8.10,"MAE_90D_pct":-16.19,"MAE_180D_pct":-16.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-17","peak_price":10840.0,"max_drawdown_low_date":"2024-04-08","max_drawdown_low":7970.0,"drawdown_after_peak_pct":-26.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"shipping_backlog_price_spike_without_fresh_margin_bridge_should_remain_watch_not_Yellow","four_b_evidence_type":["price_only","fresh_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_initial_MFE_below_Yellow_threshold_medium_MAE","current_profile_verdict":"current_profile_false_positive_if_shipping_backlog_theme_promoted_without_fresh_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"044450_2024-01-17_9510","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C01 should keep shipping/backlog theme in Watch unless fresh order, utilization, margin and cash bridge are verified. Initial MFE below 15% does not justify Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C01_R1L87_082740_HANWHA_ENGINE_ORDER_BACKLOG_MARGIN","trigger_id":"R1L87_C01_082740_20240314_STAGE2_SHIP_ENGINE_BACKLOG_MARGIN","symbol":"082740","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C01 requires order backlog plus margin and cash bridge rather than backlog label alone","raw_component_scores_before":{"order_backlog_quality_score":14,"customer_order_mix_score":13,"margin_bridge_score":12,"utilization_bridge_score":11,"cash_conversion_score":8,"relative_strength_score":12,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"order_backlog_quality_score":17,"customer_order_mix_score":16,"margin_bridge_score":15,"utilization_bridge_score":13,"cash_conversion_score":10,"relative_strength_score":13,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Order backlog, engine demand and margin proxy support Yellow-watch; exact order mix and cash-conversion evidence still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C01_R1L87_097230_HJ_SHIPBUILDING_BACKLOG_THEME","trigger_id":"R1L87_C01_097230_20240207_STAGE2_FALSE_POSITIVE_SHIPBUILDING_BACKLOG","symbol":"097230","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_scope":"current_default_proxy","profile_hypothesis":"shipbuilding backlog theme without margin/cash bridge should be blocked","raw_component_scores_before":{"order_backlog_quality_score":5,"customer_order_mix_score":2,"margin_bridge_score":0,"utilization_bridge_score":2,"cash_conversion_score":0,"relative_strength_score":7,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"order_backlog_quality_score":1,"customer_order_mix_score":0,"margin_bridge_score":0,"utilization_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE convert backlog theme into missing margin/cash bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C01_R1L87_044450_KSS_SHIPPING_BACKLOG_THEME","trigger_id":"R1L87_C01_044450_20240117_STAGE2_FALSE_POSITIVE_SHIPPING_BACKLOG_THEME","symbol":"044450","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_scope":"current_default_proxy","profile_hypothesis":"shipping/backlog spike without fresh order/margin bridge should remain Watch","raw_component_scores_before":{"order_backlog_quality_score":5,"customer_order_mix_score":2,"margin_bridge_score":1,"utilization_bridge_score":3,"cash_conversion_score":1,"relative_strength_score":10,"valuation_repricing_score":5,"execution_risk_score":-10,"theme_spike_risk":-10,"information_confidence":3},"weighted_score_before":24,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"order_backlog_quality_score":2,"customer_order_mix_score":0,"margin_bridge_score":0,"utilization_bridge_score":1,"cash_conversion_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Watch-Blocked","component_delta_explanation":"Initial MFE below Yellow threshold and missing fresh order/margin bridge should keep the row Watch/blocked."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R1L87_C01_P0_CURRENT","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C01 needs explicit order quality, margin, utilization and cash conversion bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":30.95,"avg_MAE90_pct":-15.86,"avg_MFE180_pct":35.66,"avg_MAE180_pct":-22.06,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C01_order_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R1L87_C01_P1_SECTOR_SPECIFIC","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_id":"P1_L1_order_backlog_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 order/backlog signals need order quality, delivery visibility, margin, utilization or cash bridge before Stage2-Actionable","changed_axes":["order_quality_required","margin_cash_bridge_required","backlog_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_order_quality_margin_utilization_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":30.95,"avg_MAE90_pct":-15.86,"avg_MFE180_pct":35.66,"avg_MAE180_pct":-22.06,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R1L87_C01_P2_CANONICAL","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_id":"P2_C01_order_margin_cash_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C01 should reward backlog-to-margin conversion, not backlog-theme spikes","changed_axes":["C01_order_margin_cash_bridge_required","C01_backlog_theme_local_4B_watch_guard","C01_low_MFE_no_bridge_guard"],"changed_thresholds":{"stage2_yellow_gate":"order_quality_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":30.95,"avg_MAE90_pct":-15.86,"avg_MFE180_pct":35.66,"avg_MAE180_pct":-22.06,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R1L87_C01_P3_COUNTEREXAMPLE_GUARD","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_id":"P3_C01_low_MFE_missing_bridge_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<15 and margin/cash bridge is missing, block Yellow/Green; if MAE90<=-20 or MAE180<=-35, force 4B-watch","changed_axes":["C01_low_MFE_missing_bridge_guardrail","C01_high_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_15_and_bridge_missing; hard_4B_if_MAE90_le_minus_20_or_MAE180_le_minus_35"},"eligible_trigger_count":3,"avg_MFE90_pct":30.95,"avg_MAE90_pct":-15.86,"avg_MFE180_pct":35.66,"avg_MAE180_pct":-22.06,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIP_ENGINE_ORDER_MARGIN_VS_BACKLOG_THEME","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":30.95,"avg_MAE90_pct":-15.86,"avg_MFE180_pct":35.66,"avg_MAE180_pct":-22.06,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_15":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20_or_MAE180_le_minus_35":0.33,"interpretation":"C01 needs bridge discipline. 한화엔진 shows ship-engine order/backlog margin bridge can rerate sharply, while HJ중공업 and KSS해운 show that backlog/shipping theme strength should stay Watch/4B unless margin, utilization and cash conversion are verified."}
{"row_type":"stage_transition_summary","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"082740","trigger_type":"Stage2-Actionable-ShipEngineOrderBacklogMarginBridge-Positive","entry_date":"2024-03-14","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_order_backlog_margin_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when order backlog is tied to margin, utilization and cash bridge; Green requires exact order mix and cash evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"097230","trigger_type":"Stage2-FalsePositive-ShipbuildingBacklogTheme-NoMarginCashBridge","entry_date":"2024-02-07","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_high_MAE","stage2_to_180D_outcome":"failed_backlog_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Shipbuilding backlog theme without margin/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"044450","trigger_type":"Stage2-FalsePositive-ShippingBacklogTheme-NoFreshOrderMarginBridge","entry_date":"2024-01-17","stage2_to_90D_outcome":"weak_stage2_initial_MFE_below_threshold","stage2_to_180D_outcome":"watch_entry_no_Yellow_without_fresh_bridge","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Shipping/backlog theme without fresh order and margin bridge should remain Watch/blocked from Yellow/Green."}
{"row_type":"residual_contribution","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","residual_type":"order_backlog_theme_overcredit_without_margin_utilization_cash_bridge","contribution":"Adds two C01 4B/watch counterexamples against one ship-engine order backlog positive, avoiding C01 top-covered symbols and recent L1 canonical loops.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_ORDER_BACKLOG_MARGIN_BRIDGE_VS_SHIPBUILDING_THEME_WITHOUT_CASH_CONVERSION","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C01 now has non-top-symbol ship-engine positive and shipbuilding/shipping theme counterexamples; next R1 loops should exact-URL repair order mix, backlog quality, utilization, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"C01_order_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"082740 worked when order/backlog proxy was tied to engine demand and margin bridge; 097230 and 044450 failed or weakened when only backlog/shipping theme existed."}
{"row_type":"shadow_weight","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"C01_backlog_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Backlog/shipping theme rows had low or below-threshold MFE without verified margin/cash bridge."}
{"row_type":"shadow_weight","round":"R1","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"C01_low_MFE_missing_bridge_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<15 while margin/cash bridge is missing, block Stage2-Actionable/Yellow; if MAE90<=-20 or MAE180<=-35, force 4B-watch."}
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
  - order_backlog_theme_overcredit
  - margin_cash_conversion_bridge_missing
  - utilization_bridge_missing
  - low_MFE_without_fresh_order_quality
new_axis_proposed:
  - C01_order_margin_cash_bridge_required_shadow_only
  - C01_backlog_theme_local_4B_watch_guard_shadow_only
  - C01_low_MFE_missing_bridge_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C01
  - full_4b_requires_non_price_evidence within C01
  - hard_4c_thesis_break_routes_to_4c within C01
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
3. Confirm R1 / L1 / C01 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C01 top-covered symbols
   - recent L1 C02/C03/C04/C05 loop symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C01-scoped safe patch candidates:
   - C01_order_margin_cash_bridge_required
   - C01_backlog_theme_local_4B_watch_guard
   - C01_low_MFE_missing_bridge_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R1
completed_loop = 87
next_round = R2
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01_ORDER_BACKLOG_MARGIN_BRIDGE.
```
