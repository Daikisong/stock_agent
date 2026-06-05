# E2R Stock-Web v12 Residual Research — R3 Loop 86 / L3 / C12

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 86
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_CUSTOMER_CAPACITY_CALLOFF_BRIDGE_VS_CATHODE_SEPARATOR_CONTRACT_THEME_DECAY
sector: battery / EV / customer contract / call-off risk / shipment conversion
output_file: e2r_stock_web_v12_residual_round_R3_loop_86_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R2 loop 86`.

```text
scheduled_round = R3
scheduled_loop = 86
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

R3 is restricted to battery / EV / green mobility.  
C12 is selected because it still has no explicit 4B/4C coverage in the No-Repeat Index:

```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
rows = 28
symbols = 11
good/bad Stage2 = 9/6
4B/4C = 0/0
top-covered = 121600, 278280, 020150, 348370, 091580, 137400
```

This loop avoids that top-covered list and also avoids the immediately previous R3 loop85 C11 symbols:

```text
078600, 247540, 393890
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"317330","company_name":"덕산테코피아","profile_path":"atlas/symbol_profiles/317/317330.json","first_date":"2019-08-02","last_date":"2026-02-20","trading_day_count":1607,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"066970","company_name":"엘앤에프","profile_path":"atlas/symbol_profiles/066/066970.json","first_date":"2003-01-02","last_date":"2026-02-20","trading_day_count":5711,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2016-02-19","2021-08-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here; market changed from KOSDAQ GLOBAL to KOSPI on 2024-01-29 without a 2024 price discontinuity candidate.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"361610","company_name":"SK아이이테크놀로지","profile_path":"atlas/symbol_profiles/361/361610.json","first_date":"2021-05-11","last_date":"2026-02-20","trading_day_count":1171,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"317330","trigger_type":"Stage2-Actionable-BatteryMaterialCustomerCapacityCalloffBridge-Positive","entry_date":"2024-02-14","duplicate_status":"new C12 symbol/trigger/date combination outside top-covered list and previous R3 loop85 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"066970","trigger_type":"Stage2-FalsePositive-CathodeCustomerContractTheme-CalloffMarginRisk","entry_date":"2024-03-25","duplicate_status":"new C12 symbol/trigger/date combination outside top-covered list and previous R3 loop85 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"361610","trigger_type":"Stage2-FalsePositive-SeparatorCustomerContractTheme-NoShipmentUtilizationBridge","entry_date":"2024-03-25","duplicate_status":"new C12 symbol/trigger/date combination outside top-covered list and previous R3 loop85 symbols"}
```

## 4. Research question

C12 is not a generic battery-contract bucket. The contract is only the first handshake. E2R needs to know whether the customer actually calls off volume, whether shipments leave the plant, whether utilization rises, whether ASP/mix holds, and whether margin follows. A battery contract headline without call-off is like a signed reservation at an empty factory.

Residual question:

```text
Can C12 distinguish:
1. battery-material customer/capacity bridge with strong MFE and shallow MAE,
2. cathode contract/customer theme that collapses when call-off and margin visibility weaken,
3. separator contract/customer theme that fails when shipment, utilization and margin bridge are missing?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C12_R3L86_317330_DUKSAN_BATTERY_MATERIAL_CUSTOMER_CAPACITY","symbol":"317330","company_name":"덕산테코피아","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_MATERIAL_CUSTOMER_CAPACITY_CALLOFF_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-BatteryMaterialCustomerCapacityCalloffBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_tolerable_initial_MAE","current_profile_verdict":"current_profile_correct_if_calloff_capacity_bridge_required","price_source":"Songdaiki/stock-web","notes":"Battery-material/customer-capacity proxy produced very high forward MFE. Green still requires exact customer, call-off, shipment and margin evidence."}
{"row_type":"case","case_id":"C12_R3L86_066970_LNF_CATHODE_CALLOFF_MARGIN_RISK","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CUSTOMER_CONTRACT_THEME_WITH_CALLOFF_MARGIN_RISK","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CathodeCustomerContractTheme-CalloffMarginRisk","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_contract_headline_overcredited","price_source":"Songdaiki/stock-web","notes":"Cathode/customer-contract theme near a local extension produced low MFE and deep MAE when call-off, ASP and margin bridge were not confirmed."}
{"row_type":"case","case_id":"C12_R3L86_361610_SKIET_SEPARATOR_SHIPMENT_UTILIZATION_RISK","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SEPARATOR_CUSTOMER_CONTRACT_THEME_WITHOUT_SHIPMENT_UTILIZATION_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SeparatorCustomerContractTheme-NoShipmentUtilizationBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_separator_contract_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Separator/customer-contract theme failed badly without shipment, utilization and margin bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 317330 덕산테코피아 — battery-material customer/capacity call-off bridge positive

Entry row: `2024-02-14 c=23850`.  
Observed path: entry-day low `2024-02-14 l=21450`, 30D high `2024-03-28 h=46900`, and 90/180D high `2024-06-24 h=67500`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L86_C12_317330_20240214_STAGE2_BATTERY_MATERIAL_CALLOFF_BRIDGE","case_id":"C12_R3L86_317330_DUKSAN_BATTERY_MATERIAL_CUSTOMER_CAPACITY","symbol":"317330","company_name":"덕산테코피아","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_MATERIAL_CUSTOMER_CAPACITY_CALLOFF_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-BatteryMaterialCustomerCapacityCalloffBridge-Positive","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":23850.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_material_customer_capacity_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; customer/capacity and call-off bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["customer_capacity_proxy","calloff_quality_proxy","shipment_visibility_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_confirmation_pending","volume_calloff_pending","margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/317/317330/2024.csv","profile_path":"atlas/symbol_profiles/317/317330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":96.65,"MFE_90D_pct":183.02,"MFE_180D_pct":183.02,"MAE_30D_pct":-10.06,"MAE_90D_pct":-10.06,"MAE_180D_pct":-10.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-24","peak_price":67500.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":26600.0,"drawdown_after_peak_pct":-60.59,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_tolerable_initial_MAE","current_profile_verdict":"current_profile_correct_if_calloff_capacity_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"317330_2024-02-14_23850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C12 can allow Stage2/Yellow when battery-material strength is tied to customer, capacity, call-off and shipment bridge. Green still requires exact customer and margin evidence."}
```

### 6.2 066970 엘앤에프 — cathode customer-contract theme / call-off and margin risk

Entry row: `2024-03-25 c=186300`.  
Observed path: local high `2024-03-25 h=199000`, then lows `2024-04-17 l=140600`, `2024-07-18 l=121500`, and `2024-12-20 l=90500`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L86_C12_066970_20240325_STAGE2_FALSE_POSITIVE_CATHODE_CALLOFF_RISK","case_id":"C12_R3L86_066970_LNF_CATHODE_CALLOFF_MARGIN_RISK","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CUSTOMER_CONTRACT_THEME_WITH_CALLOFF_MARGIN_RISK","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-CathodeCustomerContractTheme-CalloffMarginRisk","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":186300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cathode_customer_contract_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cathode customer/contract theme treated as insufficient without call-off, shipment, ASP and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["customer_contract_theme","battery_beta_relative_strength"],"stage3_evidence_fields":["calloff_bridge_missing","shipment_visibility_missing","ASP_margin_bridge_missing","inventory_price_pressure_unresolved"],"stage4b_evidence_fields":["price_only_local_peak","calloff_margin_risk_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.82,"MFE_90D_pct":6.82,"MFE_180D_pct":6.82,"MAE_30D_pct":-24.53,"MAE_90D_pct":-34.78,"MAE_180D_pct":-51.42,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":199000.0,"max_drawdown_low_date":"2024-12-20","max_drawdown_low":90500.0,"drawdown_after_peak_pct":-54.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"cathode_contract_theme_peak_without_calloff_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","calloff_margin_risk_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_contract_headline_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; market_change_only_on_2024-01-29","same_entry_group_id":"066970_2024-03-25_186300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C12 should block cathode customer-contract headlines when call-off, shipment, ASP and margin bridges are missing. Low MFE and deep MAE argue for Watch/4B-risk."}
```

### 6.3 361610 SK아이이테크놀로지 — separator customer-contract theme without shipment/utilization bridge

Entry row: `2024-03-25 c=76300`.  
Observed path: local high `2024-03-26 h=77700`, then lows `2024-05-30 l=43200`, `2024-07-17 l=40200`, and `2024-12-27 l=22250`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L86_C12_361610_20240325_STAGE2_FALSE_POSITIVE_SEPARATOR_UTILIZATION_RISK","case_id":"C12_R3L86_361610_SKIET_SEPARATOR_SHIPMENT_UTILIZATION_RISK","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SEPARATOR_CUSTOMER_CONTRACT_THEME_WITHOUT_SHIPMENT_UTILIZATION_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-SeparatorCustomerContractTheme-NoShipmentUtilizationBridge","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":76300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_separator_customer_contract_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; separator customer/contract theme treated as insufficient without shipment, utilization, call-off and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["separator_contract_theme","relative_strength_rebound"],"stage3_evidence_fields":["shipment_bridge_missing","utilization_bridge_missing","customer_calloff_quality_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","utilization_risk_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv","profile_path":"atlas/symbol_profiles/361/361610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.83,"MFE_90D_pct":1.83,"MFE_180D_pct":1.83,"MAE_30D_pct":-23.33,"MAE_90D_pct":-47.31,"MAE_180D_pct":-70.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":77700.0,"max_drawdown_low_date":"2024-12-27","max_drawdown_low":22250.0,"drawdown_after_peak_pct":-71.36,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"separator_contract_theme_without_shipment_utilization_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","utilization_risk_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_separator_contract_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"361610_2024-03-25_76300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C12 should not equate separator contract theme with actual shipment and utilization conversion. Near-zero MFE and extreme MAE require Watch/4B-risk routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C12_R3L86_317330_DUKSAN_BATTERY_MATERIAL_CUSTOMER_CAPACITY","trigger_id":"R3L86_C12_317330_20240214_STAGE2_BATTERY_MATERIAL_CALLOFF_BRIDGE","symbol":"317330","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C12 requires call-off, capacity and shipment bridge rather than contract wording alone","raw_component_scores_before":{"customer_contract_quality":14,"calloff_quality_score":13,"shipment_visibility_score":12,"capacity_allocation_score":12,"margin_bridge_score":9,"relative_strength_score":15,"valuation_repricing_score":10,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"customer_contract_quality":17,"calloff_quality_score":16,"shipment_visibility_score":15,"capacity_allocation_score":15,"margin_bridge_score":11,"relative_strength_score":16,"valuation_repricing_score":11,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":87,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Customer/capacity bridge and huge MFE support Yellow/Green-candidate watch; exact call-off and margin evidence still block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C12_R3L86_066970_LNF_CATHODE_CALLOFF_MARGIN_RISK","trigger_id":"R3L86_C12_066970_20240325_STAGE2_FALSE_POSITIVE_CATHODE_CALLOFF_RISK","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"cathode contract headline without call-off and margin bridge should be blocked","raw_component_scores_before":{"customer_contract_quality":9,"calloff_quality_score":2,"shipment_visibility_score":2,"capacity_allocation_score":3,"margin_bridge_score":1,"relative_strength_score":12,"valuation_repricing_score":7,"execution_risk_score":-14,"theme_spike_risk":-13,"information_confidence":3},"weighted_score_before":28,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_contract_quality":4,"calloff_quality_score":0,"shipment_visibility_score":0,"capacity_allocation_score":1,"margin_bridge_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-20,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert the cathode customer-contract theme into call-off/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C12_R3L86_361610_SKIET_SEPARATOR_SHIPMENT_UTILIZATION_RISK","trigger_id":"R3L86_C12_361610_20240325_STAGE2_FALSE_POSITIVE_SEPARATOR_UTILIZATION_RISK","symbol":"361610","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"separator contract theme without shipment/utilization bridge should remain Watch/blocked","raw_component_scores_before":{"customer_contract_quality":7,"calloff_quality_score":1,"shipment_visibility_score":1,"capacity_allocation_score":2,"margin_bridge_score":1,"relative_strength_score":10,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":18,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_contract_quality":2,"calloff_quality_score":0,"shipment_visibility_score":0,"capacity_allocation_score":0,"margin_bridge_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Near-zero MFE and extreme MAE require shipment/utilization bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L86_C12_P0_CURRENT","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C12 needs explicit customer call-off, shipment, utilization and margin bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":63.89,"avg_MAE90_pct":-30.72,"avg_MFE180_pct":63.89,"avg_MAE180_pct":-44.11,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C12_calloff_shipment_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R3L86_C12_P1_SECTOR_SPECIFIC","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_id":"P1_L3_calloff_shipment_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 battery customer-contract signals need call-off, shipment, utilization, capacity allocation or margin bridge before Stage2-Actionable","changed_axes":["calloff_quality_required","shipment_visibility_required","utilization_margin_bridge_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_calloff_shipment_utilization_capacity_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":63.89,"avg_MAE90_pct":-30.72,"avg_MFE180_pct":63.89,"avg_MAE180_pct":-44.11,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R3L86_C12_P2_CANONICAL","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_id":"P2_C12_calloff_shipment_margin_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C12 should reward call-off conversion, not customer-contract headlines","changed_axes":["C12_calloff_shipment_bridge_required","C12_contract_headline_local_4B_guard","C12_utilization_margin_bridge_required"],"changed_thresholds":{"stage2_yellow_gate":"customer_contract_plus_calloff_or_shipment_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":63.89,"avg_MAE90_pct":-30.72,"avg_MFE180_pct":63.89,"avg_MAE180_pct":-44.11,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R3L86_C12_P3_COUNTEREXAMPLE_GUARD","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_id":"P3_C12_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-30 while call-off/shipment bridge is missing, block Yellow/Green","changed_axes":["C12_high_MAE_guardrail","C12_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_30"},"eligible_trigger_count":3,"avg_MFE90_pct":63.89,"avg_MAE90_pct":-30.72,"avg_MFE180_pct":63.89,"avg_MAE180_pct":-44.11,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_CALLOFF_BRIDGE_VS_CONTRACT_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":63.89,"avg_MAE90_pct":-30.72,"avg_MFE180_pct":63.89,"avg_MAE180_pct":-44.11,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_30":0.67,"interpretation":"C12 needs bridge discipline. 317330 shows battery customer/capacity call-off bridge can rerate sharply, while 066970 and 361610 show that cathode/separator contract themes fail when call-off, shipment, utilization and margin evidence do not follow."}
{"row_type":"stage_transition_summary","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"317330","trigger_type":"Stage2-Actionable-BatteryMaterialCustomerCapacityCalloffBridge-Positive","entry_date":"2024-02-14","stage2_to_90D_outcome":"good_stage2_very_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_customer_capacity_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when customer capacity, call-off and shipment bridge exists; Green requires exact customer and margin evidence."}
{"row_type":"stage_transition_summary","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"066970","trigger_type":"Stage2-FalsePositive-CathodeCustomerContractTheme-CalloffMarginRisk","entry_date":"2024-03-25","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_cathode_contract_theme","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Cathode customer-contract theme without call-off, ASP and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"361610","trigger_type":"Stage2-FalsePositive-SeparatorCustomerContractTheme-NoShipmentUtilizationBridge","entry_date":"2024-03-25","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_extreme_MAE","stage2_to_180D_outcome":"failed_separator_contract_theme","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Separator customer-contract theme without shipment/utilization and margin bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","residual_type":"battery_contract_headline_overcredit_without_calloff_shipment_utilization_margin_bridge","contribution":"Adds two C12 local 4B/high-MAE counterexamples against one customer-capacity call-off bridge positive, avoiding C12 top-covered and previous R3 loop85 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CAPACITY_CALLOFF_BRIDGE_VS_CATHODE_SEPARATOR_CONTRACT_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C12 now has non-top-symbol cathode/separator contract-theme counterexamples; next R3 loops should exact-URL repair customer call-off, shipment, utilization, ASP and margin evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_calloff_shipment_utilization_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"317330 worked with customer/capacity call-off proxy; 066970 and 361610 failed when contract themes lacked call-off, shipment, utilization and margin bridge."}
{"row_type":"shadow_weight","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_contract_headline_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Cathode and separator customer-contract theme rows showed low MFE and high/extreme MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R3","loop":"86","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-30 while call-off/shipment bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - contract_headline_overcredit
  - calloff_bridge_missing
  - shipment_utilization_bridge_missing
  - margin_bridge_missing
new_axis_proposed:
  - C12_calloff_shipment_utilization_bridge_required_shadow_only
  - C12_contract_headline_local_4B_watch_guard_shadow_only
  - C12_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C12
  - full_4b_requires_non_price_evidence within C12
  - hard_4c_thesis_break_routes_to_4c within C12
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
3. Confirm R3 / L3 / C12 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C12 top-covered symbols
   - previous R3 loop85 C11 symbols listed in the MD
6. If aggregate support remains stable after exact evidence URL repair, consider C12-scoped safe patch candidates:
   - C12_calloff_shipment_utilization_bridge_required
   - C12_contract_headline_local_4B_watch_guard
   - C12_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R3
completed_loop = 86
next_round = R4
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.
```
