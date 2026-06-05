# E2R Stock-Web v12 Residual Research — R2 Loop 87 / L2 / C08

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 87
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: MEMORY_TESTER_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_EQUIPMENT_BETA_BLOWOFF
sector: AI / semiconductor / electronics / test equipment / socket / customer quality
output_file: e2r_stock_web_v12_residual_round_R2_loop_87_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R1 loop 87`.

```text
scheduled_round = R2
scheduled_loop = 87
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

R2 is restricted to AI / semiconductor / electronics.  
C08 is selected because the immediately previous R2 loops used C06 memory/HBM capacity and C07 equipment order relative-strength. C08 still has unresolved customer-quality and test/socket false-positive risk:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
rows = 21
symbols = 11
good/bad Stage2 = 9/5
4B/4C = 2/0
top-covered = UNKNOWN_SYMBOL, 089030, 095340, 131290, 252990, 058470
```

This loop avoids the top-covered symbols and uses a fresh set:

```text
232140, 425420, 098120
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"232140","company_name":"와이씨","profile_path":"atlas/symbol_profiles/232/232140.json","first_date":"2015-12-24","last_date":"2026-02-20","trading_day_count":2425,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2017-04-05"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here. Name changed from 와이아이케이 to 와이씨 on 2024-04-25 without a 2024 corporate-action candidate.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"425420","company_name":"티에프이","profile_path":"atlas/symbol_profiles/425/425420.json","first_date":"2022-11-17","last_date":"2026-02-20","trading_day_count":795,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"098120","company_name":"마이크로컨텍솔","profile_path":"atlas/symbol_profiles/098/098120.json","first_date":"2008-09-23","last_date":"2026-02-20","trading_day_count":4294,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2011-04-19","2011-05-17"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"232140","trigger_type":"Stage2-Actionable-MemoryTesterCustomerQualityBridge-Positive","entry_date":"2024-02-28","duplicate_status":"new C08 symbol/trigger/date combination outside top-covered list and previous R2 loop85/86 C06/C07 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"425420","trigger_type":"Stage2-FalsePositive-TestSocketCustomerQualityBetaBlowoff-NoFreshQualificationBridge","entry_date":"2024-03-20","duplicate_status":"new C08 symbol/trigger/date combination outside top-covered list and previous R2 loop85/86 C06/C07 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"098120","trigger_type":"Stage2-FalsePositive-TestSocketThemeRebound-NoCustomerShipmentMarginBridge","entry_date":"2024-04-29","duplicate_status":"new C08 symbol/trigger/date combination outside top-covered list and previous R2 loop85/86 C06/C07 symbols"}
```

## 4. Research question

C08 is not “semiconductor test/socket stock is strong.”  
The useful signal is the customer-quality bridge: actual tester or socket qualification, customer concentration quality, HBM/AI memory program fit, shipment timing, burn-in or final-test bottleneck, recurring socket demand, pricing power, margin bridge, and cash conversion.

A test/socket headline without customer qualification is like a probe card touching air: the signal fires, but nothing is measured.

Residual question:

```text
Can C08 distinguish:
1. memory-tester customer-quality bridge with huge forward MFE,
2. test/socket equipment beta blowoff where price runs ahead of qualification, shipment, and margin evidence,
3. socket-theme rebound that lacks customer shipment and margin bridge and decays into deep MAE?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C08_R2L87_232140_YC_MEMORY_TESTER_CUSTOMER_QUALITY","symbol":"232140","company_name":"와이씨","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMORY_TESTER_CUSTOMER_QUALITY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-MemoryTesterCustomerQualityBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_customer_quality_shipment_bridge_required","price_source":"Songdaiki/stock-web","notes":"Memory-tester/customer-quality proxy produced very high MFE with tolerable MAE. Green still requires exact customer, shipment, qualification, margin and cash evidence."}
{"row_type":"case","case_id":"C08_R2L87_425420_TFE_TEST_SOCKET_BLOWOFF_NO_FRESH_QUALIFICATION","symbol":"425420","company_name":"티에프이","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_BETA_BLOWOFF_WITHOUT_FRESH_QUALIFICATION_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-TestSocketCustomerQualityBetaBlowoff-NoFreshQualificationBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_socket_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Late beta/blowoff entry had near-zero MFE and extreme MAE when fresh customer qualification, shipment timing and margin bridge were missing."}
{"row_type":"case","case_id":"C08_R2L87_098120_MICROCONTACT_SOCKET_THEME_NO_SHIPMENT","symbol":"098120","company_name":"마이크로컨텍솔","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_THEME_REBOUND_WITHOUT_CUSTOMER_SHIPMENT_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-TestSocketThemeRebound-NoCustomerShipmentMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_socket_theme_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Socket-theme rebound showed almost no forward MFE and deep MAE without customer shipment, recurring demand and margin bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 232140 와이씨 — memory tester / customer-quality bridge positive

Entry row: `2024-02-28 c=6690`.  
Observed path: entry-day low `2024-02-28 l=5970`, 30D high `2024-03-21 h=8470`, 90D high `2024-06-13 h=22950`, and later low `2024-12-09 l=8290` stayed above entry.

```jsonl
{"row_type":"trigger","trigger_id":"R2L87_C08_232140_20240228_STAGE2_MEMORY_TESTER_CUSTOMER_QUALITY","case_id":"C08_R2L87_232140_YC_MEMORY_TESTER_CUSTOMER_QUALITY","symbol":"232140","company_name":"와이씨","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMORY_TESTER_CUSTOMER_QUALITY_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-MemoryTesterCustomerQualityBridge-Positive","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":6690.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_memory_tester_customer_quality_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; memory tester customer quality, AI/HBM program fit and shipment bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["customer_quality_proxy","memory_tester_demand_proxy","AI_HBM_test_bottleneck_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_qualification_pending","shipment_timing_pending","margin_bridge_pending","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv","profile_path":"atlas/symbol_profiles/232/232140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.61,"MFE_90D_pct":243.05,"MFE_180D_pct":243.05,"MAE_30D_pct":-10.76,"MAE_90D_pct":-10.76,"MAE_180D_pct":-10.76,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-13","peak_price":22950.0,"max_drawdown_low_date":"2024-02-28","max_drawdown_low":5970.0,"drawdown_after_peak_pct":-63.88,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_positioning_overheat_watch; do not upgrade to Green without exact customer/shipment/margin evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_customer_quality_shipment_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; name_change_only_on_2024-04-25","same_entry_group_id":"232140_2024-02-28_6690","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C08 can allow Stage2/Yellow when memory tester strength is tied to customer quality, AI/HBM test bottleneck and shipment bridge. Green still requires exact qualification, margin and cash evidence."}
```

### 6.2 425420 티에프이 — test/socket beta blowoff without fresh qualification bridge

Entry row: `2024-03-20 c=43100`.  
Observed path: local high `2024-03-21 h=43950`, then lows `2024-07-12 l=14110`, `2024-10-30 l=15050`, and `2024-11-15 l=11390`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L87_C08_425420_20240320_STAGE2_FALSE_POSITIVE_SOCKET_BLOWOFF","case_id":"C08_R2L87_425420_TFE_TEST_SOCKET_BLOWOFF_NO_FRESH_QUALIFICATION","symbol":"425420","company_name":"티에프이","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_BETA_BLOWOFF_WITHOUT_FRESH_QUALIFICATION_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-TestSocketCustomerQualityBetaBlowoff-NoFreshQualificationBridge","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":43100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_test_socket_beta_blowoff_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; test/socket price beta treated as insufficient without fresh qualification, customer shipment and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["test_socket_beta","relative_strength_blowoff"],"stage3_evidence_fields":["fresh_customer_qualification_missing","shipment_visibility_missing","recurring_socket_demand_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","qualification_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv","profile_path":"atlas/symbol_profiles/425/425420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.97,"MFE_90D_pct":1.97,"MFE_180D_pct":1.97,"MAE_30D_pct":-24.25,"MAE_90D_pct":-67.26,"MAE_180D_pct":-73.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":43950.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":11390.0,"drawdown_after_peak_pct":-74.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"test_socket_blowoff_without_fresh_customer_qualification_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","qualification_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_socket_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"425420_2024-03-20_43100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C08 should not upgrade socket/test-equipment blowoff without fresh customer qualification, shipment and recurring-demand bridge. Near-zero MFE and extreme MAE force Watch/4B-risk."}
```

### 6.3 098120 마이크로컨텍솔 — socket-theme rebound without customer shipment/margin bridge

Entry row: `2024-04-29 c=10970`.  
Observed path: local high `2024-04-29~04-30 h=11130`, then lows `2024-07-23 l=7600`, `2024-11-13 l=4730`, and `2024-12-09 l=4245`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L87_C08_098120_20240429_STAGE2_FALSE_POSITIVE_SOCKET_THEME_REBOUND","case_id":"C08_R2L87_098120_MICROCONTACT_SOCKET_THEME_NO_SHIPMENT","symbol":"098120","company_name":"마이크로컨텍솔","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_THEME_REBOUND_WITHOUT_CUSTOMER_SHIPMENT_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-TestSocketThemeRebound-NoCustomerShipmentMarginBridge","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":10970.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_test_socket_theme_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; socket rebound treated as insufficient without customer shipment, recurring demand and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["test_socket_theme_rebound","relative_strength_rebound"],"stage3_evidence_fields":["customer_shipment_bridge_missing","recurring_socket_demand_missing","pricing_power_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","customer_shipment_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv","profile_path":"atlas/symbol_profiles/098/098120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.46,"MFE_90D_pct":1.46,"MFE_180D_pct":1.46,"MAE_30D_pct":-15.86,"MAE_90D_pct":-30.72,"MAE_180D_pct":-61.30,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-30","peak_price":11130.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":4245.0,"drawdown_after_peak_pct":-61.86,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"socket_theme_rebound_without_customer_shipment_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","customer_shipment_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_socket_theme_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"098120_2024-04-29_10970","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C08 should not promote socket-theme rebound unless customer shipment, recurring socket demand, pricing power and margin bridge are verified. Near-zero MFE and deep MAE argue for 4B-watch."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C08_R2L87_232140_YC_MEMORY_TESTER_CUSTOMER_QUALITY","trigger_id":"R2L87_C08_232140_20240228_STAGE2_MEMORY_TESTER_CUSTOMER_QUALITY","symbol":"232140","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C08 requires customer-quality and shipment bridge rather than test/socket beta alone","raw_component_scores_before":{"customer_quality_score":14,"qualification_bridge_score":13,"shipment_visibility_score":12,"AI_HBM_program_fit_score":12,"margin_bridge_score":9,"relative_strength_score":15,"valuation_repricing_score":10,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"customer_quality_score":17,"qualification_bridge_score":16,"shipment_visibility_score":15,"AI_HBM_program_fit_score":15,"margin_bridge_score":11,"relative_strength_score":16,"valuation_repricing_score":11,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":87,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Customer-quality and tester shipment proxy plus huge MFE support Yellow/Green-candidate watch, but exact customer and margin evidence still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C08_R2L87_425420_TFE_TEST_SOCKET_BLOWOFF_NO_FRESH_QUALIFICATION","trigger_id":"R2L87_C08_425420_20240320_STAGE2_FALSE_POSITIVE_SOCKET_BLOWOFF","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_scope":"current_default_proxy","profile_hypothesis":"late socket beta without fresh qualification should be blocked","raw_component_scores_before":{"customer_quality_score":5,"qualification_bridge_score":1,"shipment_visibility_score":1,"AI_HBM_program_fit_score":4,"margin_bridge_score":1,"relative_strength_score":14,"valuation_repricing_score":6,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_quality_score":1,"qualification_bridge_score":0,"shipment_visibility_score":0,"AI_HBM_program_fit_score":1,"margin_bridge_score":0,"relative_strength_score":4,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and extreme MAE convert the socket beta blowoff into missing-qualification bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C08_R2L87_098120_MICROCONTACT_SOCKET_THEME_NO_SHIPMENT","trigger_id":"R2L87_C08_098120_20240429_STAGE2_FALSE_POSITIVE_SOCKET_THEME_REBOUND","symbol":"098120","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_scope":"current_default_proxy","profile_hypothesis":"socket rebound without customer shipment and margin bridge should remain Watch/blocked","raw_component_scores_before":{"customer_quality_score":4,"qualification_bridge_score":1,"shipment_visibility_score":1,"AI_HBM_program_fit_score":3,"margin_bridge_score":1,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_quality_score":0,"qualification_bridge_score":0,"shipment_visibility_score":0,"AI_HBM_program_fit_score":1,"margin_bridge_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Near-zero MFE and deep MAE require customer shipment, recurring demand and margin bridge before Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L87_C08_P0_CURRENT","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C08 needs explicit customer quality, qualification, shipment and margin bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":82.16,"avg_MAE90_pct":-36.25,"avg_MFE180_pct":82.16,"avg_MAE180_pct":-48.54,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C08_customer_quality_shipment_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L87_C08_P1_SECTOR_SPECIFIC","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_id":"P1_L2_test_socket_customer_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 test/socket signals need customer qualification, shipment visibility, AI/HBM program fit, recurring socket demand or margin bridge before Stage2-Actionable","changed_axes":["customer_quality_required","qualification_shipment_required","test_socket_beta_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_qualification_shipment_AIHbm_program_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":82.16,"avg_MAE90_pct":-36.25,"avg_MFE180_pct":82.16,"avg_MAE180_pct":-48.54,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L87_C08_P2_CANONICAL","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_id":"P2_C08_customer_quality_shipment_margin_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C08 should reward customer-quality/shipment mechanics, not socket/test beta blowoffs","changed_axes":["C08_customer_quality_shipment_bridge_required","C08_socket_beta_local_4B_guard","C08_high_MAE_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_quality_plus_qualification_or_shipment_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":82.16,"avg_MAE90_pct":-36.25,"avg_MFE180_pct":82.16,"avg_MAE180_pct":-48.54,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L87_C08_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_id":"P3_C08_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and MAE90<=-25 while qualification/shipment bridge is missing, block Yellow/Green","changed_axes":["C08_low_MFE_guardrail","C08_high_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_MAE90_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":82.16,"avg_MAE90_pct":-36.25,"avg_MFE180_pct":82.16,"avg_MAE180_pct":-48.54,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TESTER_CUSTOMER_QUALITY_VS_SOCKET_BETA_BLOWOFF","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":82.16,"avg_MAE90_pct":-36.25,"avg_MFE180_pct":82.16,"avg_MAE180_pct":-48.54,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE90_le_minus_25":0.67,"interpretation":"C08 needs bridge discipline. 와이씨 shows a memory-tester customer-quality bridge can rerate massively, while 티에프이 and 마이크로컨텍솔 show socket/test-equipment beta can fail badly without fresh customer qualification, shipment, recurring demand and margin bridge."}
{"row_type":"stage_transition_summary","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"232140","trigger_type":"Stage2-Actionable-MemoryTesterCustomerQualityBridge-Positive","entry_date":"2024-02-28","stage2_to_90D_outcome":"good_stage2_very_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_memory_tester_customer_quality_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when customer quality, qualification, tester shipment and AI/HBM program bridge exists; Green requires exact customer and margin evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"425420","trigger_type":"Stage2-FalsePositive-TestSocketCustomerQualityBetaBlowoff-NoFreshQualificationBridge","entry_date":"2024-03-20","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_extreme_MAE","stage2_to_180D_outcome":"failed_socket_beta_blowoff","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Test/socket beta blowoff without fresh customer qualification and shipment bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"098120","trigger_type":"Stage2-FalsePositive-TestSocketThemeRebound-NoCustomerShipmentMarginBridge","entry_date":"2024-04-29","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_socket_theme_rebound","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Socket-theme rebound without customer shipment and margin bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","residual_type":"test_socket_equipment_beta_overcredit_without_customer_qualification_shipment_margin_bridge","contribution":"Adds two C08 local 4B/high-MAE counterexamples against one memory-tester customer-quality positive, avoiding C08 top-covered and recent R2 C06/C07 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMORY_TESTER_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_EQUIPMENT_BETA_BLOWOFF","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C08 now has non-top-symbol memory tester positive and socket/test-equipment blowoff counterexamples; next R2 loops should exact-URL repair customer qualification, shipment timing, AI/HBM program fit, recurring demand, margin and cash evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_customer_quality_shipment_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"232140 worked when customer-quality/tester shipment proxy was present; 425420 and 098120 failed when socket/test beta lacked customer qualification and shipment bridge."}
{"row_type":"shadow_weight","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_socket_beta_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Socket/test equipment beta rows had near-zero MFE and deep/extreme MAE without fresh non-price bridge."}
{"row_type":"shadow_weight","round":"R2","loop":"87","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_low_MFE_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<5 and MAE90<=-25 while customer qualification/shipment bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - test_socket_beta_overcredit
  - customer_qualification_bridge_missing
  - shipment_visibility_missing
  - recurring_socket_demand_margin_bridge_missing
new_axis_proposed:
  - C08_customer_quality_shipment_bridge_required_shadow_only
  - C08_socket_beta_local_4B_watch_guard_shadow_only
  - C08_low_MFE_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C08
  - full_4b_requires_non_price_evidence within C08
  - hard_4c_thesis_break_routes_to_4c within C08
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
3. Confirm R2 / L2 / C08 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C08 top-covered symbols
   - previous R2 loop85 C06 symbols
   - previous R2 loop86 C07 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C08-scoped safe patch candidates:
   - C08_customer_quality_shipment_bridge_required
   - C08_socket_beta_local_4B_watch_guard
   - C08_low_MFE_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 87
next_round = R3
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.
```
