# E2R Stock-Web v12 Residual Research — R2 Loop 88 / L2 / C09

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 88
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_LASER_EQUIPMENT_CUSTOMER_ORDER_MARGIN_BRIDGE_VS_TESTER_LASER_VALUATION_BLOWOFF
sector: AI / semiconductor / electronics / advanced equipment / laser / tester / valuation blowoff
output_file: e2r_stock_web_v12_residual_round_R2_loop_88_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R1 loop 88`.

```text
scheduled_round = R2
scheduled_loop = 88
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

R2 is restricted to AI / semiconductor / electronics.  
C09 is selected because the immediately previous R2 loops used C06 memory/HBM capacity, C07 equipment-order relative strength, and C08 test/socket customer quality. C09 is the advanced-equipment valuation-blowoff bucket and is a good place to test the R13 loop87 lesson: price-only or theme-only MFE must not become positive evidence when the customer/order/margin bridge is missing.

No-Repeat Index snapshot:

```text
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
rows = 17
symbols = 11
good/bad Stage2 = 7/3
4B/4C = 1/0
top-covered = 322310, 348210, 089030, 140860, 031980, 064290
```

This loop avoids those top-covered symbols and avoids the recent R2 loop symbols:

```text
R2 loop85 C06: 000660, 005930, 009150
R2 loop86 C07: 042700, 064760, 003160
R2 loop87 C08: 232140, 425420, 098120
```

Selected symbols:

```text
039030, 412350, 253590
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"039030","company_name":"이오테크닉스","profile_path":"atlas/symbol_profiles/039/039030.json","first_date":"2000-08-24","last_date":"2026-02-20","trading_day_count":6285,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2003-02-03"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists long before the selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"412350","company_name":"레이저쎌","profile_path":"atlas/symbol_profiles/412/412350.json","first_date":"2022-06-24","last_date":"2026-02-20","trading_day_count":894,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2026-01-09"],"has_major_raw_discontinuity":true,"calibration_caveat":"Future corporate-action candidate is outside the selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"253590","company_name":"네오셈","profile_path":"atlas/symbol_profiles/253/253590.json","first_date":"2018-04-04","last_date":"2026-02-20","trading_day_count":1890,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2019-01-31"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"039030","trigger_type":"Stage2-Actionable-AdvancedLaserEquipmentCustomerOrderMarginBridge-Positive","entry_date":"2024-02-28","duplicate_status":"new C09 symbol/trigger/date combination outside top-covered and recent R2 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"412350","trigger_type":"Stage2-FalsePositive-LaserBondingThemeBlowoff-NoCustomerShipmentMarginBridge","entry_date":"2024-05-02","duplicate_status":"new C09 symbol/trigger/date combination outside top-covered and recent R2 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"253590","trigger_type":"Stage2-FalsePositive-LateMemoryTesterValuationExtension-NoFreshOrderBridge","entry_date":"2024-07-04","duplicate_status":"new C09 symbol/trigger/date combination outside top-covered and recent R2 loop symbols"}
```

## 4. Research question

C09 is not “semiconductor equipment price went up.”  
The useful advanced-equipment signal must prove the bridge from valuation to business: qualified customer, repeat order or acceptance, shipment timing, tool utilization, ASP or margin mix, HBM / advanced-packaging program fit, and cash conversion. If this bridge is absent, a chart can look like a laser pulse: bright, precise, and then gone.

Residual question:

```text
Can C09 distinguish:
1. advanced laser / semicap equipment strength backed by customer-order and margin bridge,
2. laser bonding / advanced packaging theme blowoff without shipment and margin evidence,
3. late memory tester valuation extension where previous HBM beta does not equal fresh order evidence?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C09_R2L88_039030_EOTECH_ADVANCED_LASER_ORDER_MARGIN","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_LASER_EQUIPMENT_CUSTOMER_ORDER_MARGIN_BRIDGE","case_type":"watch_positive_control","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-AdvancedLaserEquipmentCustomerOrderMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_moderate_90D_MAE_deep_late_drawdown","current_profile_verdict":"current_profile_correct_if_customer_order_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Advanced laser equipment/customer-order proxy produced high MFE, but later 180D drawdown keeps Green strict. This is Yellow-watch, not Green loosening."}
{"row_type":"case","case_id":"C09_R2L88_412350_LASERSEL_THEME_BLOWOFF","symbol":"412350","company_name":"레이저쎌","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"LASER_BONDING_THEME_BLOWOFF_WITHOUT_CUSTOMER_SHIPMENT_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LaserBondingThemeBlowoff-NoCustomerShipmentMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_laser_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Laser/advanced-packaging theme had low MFE and deep MAE without customer qualification, shipment and margin bridge."}
{"row_type":"case","case_id":"C09_R2L88_253590_NEOSEM_LATE_TESTER_VALUATION_EXTENSION","symbol":"253590","company_name":"네오셈","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"LATE_MEMORY_TESTER_VALUATION_EXTENSION_WITHOUT_FRESH_ORDER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LateMemoryTesterValuationExtension-NoFreshOrderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub_Yellow_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_late_tester_extension_overcredited","price_source":"Songdaiki/stock-web","notes":"Late memory-tester valuation extension had sub-Yellow MFE and deep later MAE when fresh customer/order and margin bridge were missing."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 039030 이오테크닉스 — advanced laser equipment / customer order-margin bridge positive

Entry row: `2024-02-28 c=202000`.  
Observed path: high `2024-04-12 h=281000`, 90D low around `2024-06-25 l=170400`, and later low `2024-11-18 l=117500`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L88_C09_039030_20240228_STAGE2_ADVANCED_LASER_ORDER_MARGIN","case_id":"C09_R2L88_039030_EOTECH_ADVANCED_LASER_ORDER_MARGIN","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_LASER_EQUIPMENT_CUSTOMER_ORDER_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-AdvancedLaserEquipmentCustomerOrderMarginBridge-Positive","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":202000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_advanced_laser_equipment_customer_order_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; laser equipment customer/order, HBM advanced packaging program fit and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["customer_order_proxy","advanced_packaging_laser_proxy","HBM_program_fit_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_acceptance_pending","shipment_timing_pending","margin_mix_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_only_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv","profile_path":"atlas/symbol_profiles/039/039030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":39.11,"MFE_90D_pct":39.11,"MFE_180D_pct":39.11,"MAE_30D_pct":-13.66,"MAE_90D_pct":-15.64,"MAE_180D_pct":-41.83,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-12","peak_price":281000.0,"max_drawdown_low_date":"2024-11-18","max_drawdown_low":117500.0,"drawdown_after_peak_pct":-58.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B; late drawdown blocks Green without exact customer/order/margin evidence","four_b_evidence_type":["price_only_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_moderate_90D_MAE_deep_late_drawdown","current_profile_verdict":"current_profile_correct_if_customer_order_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"039030_2024-02-28_202000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C09 can allow Stage2/Yellow when valuation strength is tied to customer order, accepted shipment, HBM/advanced packaging program fit and margin bridge. Green still requires exact source-grade evidence because late drawdown can be severe."}
```

### 6.2 412350 레이저쎌 — laser bonding theme blowoff without customer shipment/margin bridge

Entry row: `2024-05-02 c=12620`.  
Observed path: next local high `2024-05-03 h=13590`, 90D lows below 8,000, and later low `2024-12-09 l=3050`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L88_C09_412350_20240502_STAGE2_FALSE_POSITIVE_LASER_THEME","case_id":"C09_R2L88_412350_LASERSEL_THEME_BLOWOFF","symbol":"412350","company_name":"레이저쎌","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"LASER_BONDING_THEME_BLOWOFF_WITHOUT_CUSTOMER_SHIPMENT_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-LaserBondingThemeBlowoff-NoCustomerShipmentMarginBridge","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":12620.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_laser_bonding_advanced_packaging_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; laser bonding/advanced-packaging theme treated as insufficient without verified customer qualification, shipment, repeat order and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["laser_bonding_theme","advanced_packaging_keyword","relative_strength_spike"],"stage3_evidence_fields":["customer_qualification_missing","shipment_visibility_missing","repeat_order_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","customer_shipment_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/412/412350/2024.csv","profile_path":"atlas/symbol_profiles/412/412350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.69,"MFE_90D_pct":7.69,"MFE_180D_pct":7.69,"MAE_30D_pct":-17.35,"MAE_90D_pct":-40.25,"MAE_180D_pct":-75.83,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":13590.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":3050.0,"drawdown_after_peak_pct":-77.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"laser_bonding_theme_without_customer_shipment_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","customer_shipment_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_laser_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; 2026-01-09_candidate_outside_window","same_entry_group_id":"412350_2024-05-02_12620","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C09 should not promote laser/advanced-packaging theme strength without customer qualification, shipment visibility, repeat order and margin bridge. Low MFE and deep MAE force 4B-watch routing."}
```

### 6.3 253590 네오셈 — late memory tester valuation extension without fresh order bridge

Entry row: `2024-07-04 c=15530`.  
Observed path: same-day high `h=17270`, later low `2024-12-09 l=8190`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L88_C09_253590_20240704_STAGE2_FALSE_POSITIVE_LATE_TESTER_EXTENSION","case_id":"C09_R2L88_253590_NEOSEM_LATE_TESTER_VALUATION_EXTENSION","symbol":"253590","company_name":"네오셈","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"LATE_MEMORY_TESTER_VALUATION_EXTENSION_WITHOUT_FRESH_ORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-LateMemoryTesterValuationExtension-NoFreshOrderBridge","trigger_date":"2024-07-04","entry_date":"2024-07-04","entry_price":15530.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_late_memory_tester_HBM_valuation_extension_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; late memory-tester valuation extension treated as insufficient without fresh customer order, acceptance, shipment and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["late_tester_valuation_extension","HBM_memory_test_theme"],"stage3_evidence_fields":["fresh_customer_order_missing","tool_acceptance_missing","shipment_timing_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_late_extension","fresh_order_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253590/2024.csv","profile_path":"atlas/symbol_profiles/253/253590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.20,"MFE_90D_pct":11.20,"MFE_180D_pct":11.20,"MAE_30D_pct":-19.51,"MAE_90D_pct":-46.23,"MAE_180D_pct":-47.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-04","peak_price":17270.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":8190.0,"drawdown_after_peak_pct":-52.58,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_memory_tester_extension_without_fresh_order_bridge_should_remain_watch_4B_not_Yellow","four_b_evidence_type":["price_only","fresh_order_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_late_tester_extension_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"253590_2024-07-04_15530","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C09 should not equate late HBM/memory-tester valuation extension with fresh order evidence. Sub-Yellow MFE and deep MAE require 4B-watch unless exact customer/order/shipment bridge is repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C09_R2L88_039030_EOTECH_ADVANCED_LASER_ORDER_MARGIN","trigger_id":"R2L88_C09_039030_20240228_STAGE2_ADVANCED_LASER_ORDER_MARGIN","symbol":"039030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C09 requires customer/order/margin bridge rather than advanced equipment valuation alone","raw_component_scores_before":{"customer_order_score":13,"technology_fit_score":13,"shipment_visibility_score":10,"margin_mix_score":9,"cash_conversion_score":6,"relative_strength_score":13,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-3,"information_confidence":5},"weighted_score_before":69,"stage_label_before":"Stage2-Watch/Yellow-candidate","raw_component_scores_after":{"customer_order_score":16,"technology_fit_score":16,"shipment_visibility_score":13,"margin_mix_score":11,"cash_conversion_score":8,"relative_strength_score":14,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":6},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Customer/order and advanced laser bridge plus high MFE support Yellow-watch; deep late drawdown and proxy-only evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C09_R2L88_412350_LASERSEL_THEME_BLOWOFF","trigger_id":"R2L88_C09_412350_20240502_STAGE2_FALSE_POSITIVE_LASER_THEME","symbol":"412350","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_scope":"current_default_proxy","profile_hypothesis":"laser bonding theme without customer shipment and margin bridge should be blocked","raw_component_scores_before":{"customer_order_score":2,"technology_fit_score":6,"shipment_visibility_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_order_score":0,"technology_fit_score":1,"shipment_visibility_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert laser theme into missing customer/shipment bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C09_R2L88_253590_NEOSEM_LATE_TESTER_VALUATION_EXTENSION","trigger_id":"R2L88_C09_253590_20240704_STAGE2_FALSE_POSITIVE_LATE_TESTER_EXTENSION","symbol":"253590","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_scope":"current_default_proxy","profile_hypothesis":"late memory tester valuation extension without fresh order bridge should remain Watch/blocked","raw_component_scores_before":{"customer_order_score":3,"technology_fit_score":7,"shipment_visibility_score":1,"margin_mix_score":1,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":5,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_order_score":0,"technology_fit_score":2,"shipment_visibility_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-Yellow MFE and deep MAE require fresh order/shipment/margin evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L88_C09_P0_CURRENT","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C09 needs explicit customer/order/shipment/margin bridge and late-extension 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":19.33,"avg_MAE90_pct":-34.04,"avg_MFE180_pct":19.33,"avg_MAE180_pct":-54.97,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C09_customer_order_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L88_C09_P1_SECTOR_SPECIFIC","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_id":"P1_L2_advanced_equipment_order_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 advanced-equipment signals need customer order, acceptance, shipment timing, technology-program fit, margin mix or cash conversion before Stage2-Actionable","changed_axes":["customer_order_required","shipment_margin_required","valuation_blowoff_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_order_acceptance_shipment_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":19.33,"avg_MAE90_pct":-34.04,"avg_MFE180_pct":19.33,"avg_MAE180_pct":-54.97,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L88_C09_P2_CANONICAL","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_id":"P2_C09_customer_order_margin_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C09 should reward order-to-margin mechanics, not advanced-equipment theme or late valuation extension labels","changed_axes":["C09_customer_order_margin_bridge_required","C09_laser_tester_theme_local_4B_guard","C09_late_extension_not_fresh_order_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_order_plus_shipment_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":19.33,"avg_MAE90_pct":-34.04,"avg_MFE180_pct":19.33,"avg_MAE180_pct":-54.97,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L88_C09_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_id":"P3_C09_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<20 and MAE90<=-30 while customer/order bridge is missing, block Yellow/Green and route to 4B-watch","changed_axes":["C09_low_MFE_guardrail","C09_high_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_20_and_MAE90_le_minus_30"},"eligible_trigger_count":3,"avg_MFE90_pct":19.33,"avg_MAE90_pct":-34.04,"avg_MFE180_pct":19.33,"avg_MAE180_pct":-54.97,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_LASER_ORDER_BRIDGE_VS_EQUIPMENT_VALUATION_BLOWOFF","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":19.33,"avg_MAE90_pct":-34.04,"avg_MFE180_pct":19.33,"avg_MAE180_pct":-54.97,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_20":0.67,"stage2_bad_entry_rate_MAE90_le_minus_30":0.67,"interpretation":"C09 needs bridge discipline. 이오테크닉스 shows advanced laser equipment/customer-order bridge can support Yellow-watch, while 레이저쎌 and 네오셈 show laser/tester themes or late valuation extensions fail when customer qualification, shipment, order and margin evidence are missing."}
{"row_type":"stage_transition_summary","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"039030","trigger_type":"Stage2-Actionable-AdvancedLaserEquipmentCustomerOrderMarginBridge-Positive","entry_date":"2024-02-28","stage2_to_90D_outcome":"good_stage2_high_MFE_moderate_MAE","stage2_to_180D_outcome":"watch_positive_with_deep_late_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when customer order, shipment and margin bridge exists; Green requires exact evidence and late-drawdown guard."}
{"row_type":"stage_transition_summary","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"412350","trigger_type":"Stage2-FalsePositive-LaserBondingThemeBlowoff-NoCustomerShipmentMarginBridge","entry_date":"2024-05-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_laser_bonding_theme_extreme_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Laser/advanced-packaging theme without customer shipment and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"253590","trigger_type":"Stage2-FalsePositive-LateMemoryTesterValuationExtension-NoFreshOrderBridge","entry_date":"2024-07-04","stage2_to_90D_outcome":"bad_stage2_sub_Yellow_MFE_deep_MAE","stage2_to_180D_outcome":"failed_late_tester_extension_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Late memory-tester valuation extension without fresh order/shipment bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","residual_type":"advanced_equipment_valuation_theme_overcredit_without_customer_order_shipment_margin_bridge","contribution":"Adds two C09 local 4B/deep-MAE counterexamples against one advanced laser customer-order positive, avoiding C09 top-covered and previous R2 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_LASER_EQUIPMENT_CUSTOMER_ORDER_MARGIN_BRIDGE_VS_TESTER_LASER_VALUATION_BLOWOFF","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C09 now has non-top-symbol advanced laser positive plus laser/tester valuation-blowoff counterexamples; next R2 loops should exact-URL repair customer qualification, order acceptance, shipment timing, margin mix, capacity utilization and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_customer_order_shipment_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"039030 worked when customer-order/margin proxy was present; 412350 and 253590 failed when only laser/tester theme or late valuation extension existed."}
{"row_type":"shadow_weight","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_equipment_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Laser/tester theme rows showed sub-Yellow or low MFE and deep MAE without non-price customer/order bridge."}
{"row_type":"shadow_weight","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_late_extension_not_fresh_order_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"Late equipment valuation extension should not be treated as fresh customer-order evidence unless exact customer, shipment and margin bridge is repaired."}
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
  - advanced_equipment_valuation_theme_overcredit
  - customer_qualification_bridge_missing
  - shipment_order_bridge_missing
  - late_extension_not_fresh_order_validation
new_axis_proposed:
  - C09_customer_order_shipment_margin_bridge_required_shadow_only
  - C09_equipment_theme_local_4B_watch_guard_shadow_only
  - C09_late_extension_not_fresh_order_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C09
  - full_4b_requires_non_price_evidence within C09
  - hard_4c_thesis_break_routes_to_4c within C09
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
3. Confirm R2 / L2 / C09 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C09 top-covered symbols
   - previous R2 loop85 C06 symbols
   - previous R2 loop86 C07 symbols
   - previous R2 loop87 C08 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C09-scoped safe patch candidates:
   - C09_customer_order_shipment_margin_bridge_required
   - C09_equipment_theme_local_4B_watch_guard
   - C09_late_extension_not_fresh_order_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 88
next_round = R3
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.
```
