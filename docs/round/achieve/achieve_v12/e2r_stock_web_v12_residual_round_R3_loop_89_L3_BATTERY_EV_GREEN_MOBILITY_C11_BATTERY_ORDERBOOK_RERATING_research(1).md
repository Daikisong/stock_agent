# E2R Stock-Web v12 Residual Research — R3 Loop 89 / L3 / C11

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 89
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_RAMP_BRIDGE_VS_SEPARATOR_MAGNETIC_EQUIPMENT_REBOUND_DECAY
sector: battery / EV / equipment / separator-materials / orderbook / customer ramp / margin bridge
output_file: e2r_stock_web_v12_residual_round_R3_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R2 loop 89`.

```text
scheduled_round = R3
scheduled_loop = 89
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
```

R3 is restricted to battery / EV / green mobility.  
C11 is selected because the recent R3 sector cycle already walked through:

```text
R3 loop85: C11_BATTERY_ORDERBOOK_RERATING
R3 loop86: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
R3 loop87: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
R3 loop88: C14_EV_DEMAND_SLOWDOWN_4B_4C
```

No-Repeat Index snapshot:

```text
C11_BATTERY_ORDERBOOK_RERATING
rows = 21
symbols = 14
good/bad Stage2 = 8/4
4B/4C = 1/0
top-covered = 137400, 299030, 003670, 302430, 001570, 005070
```

This loop avoids the C11 top-covered list and also avoids recent R3 loop symbols:

```text
R3 loop85 C11: 078600, 247540, 393890
R3 loop86 C12: 317330, 066970, 361610
R3 loop87 C13: 096770, 011790, 051910
R3 loop88 C14: 093370, 336370, 382840
```

Selected symbols:

```text
222080, 290670, 089980
```

The selected pocket is deliberately not a battery-cell mega-cap pocket.  
It tests whether E2R can separate:

```text
battery-equipment orderbook/customer-ramp bridge
vs
battery-equipment rebound without fresh order/margin bridge
vs
separator/materials rebound without customer call-off and margin bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"222080","company_name":"씨아이에스","profile_path":"atlas/symbol_profiles/222/222080.json","first_date":"2015-09-02","last_date":"2026-02-20","trading_day_count":2529,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2017-01-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"SPAC transition / corporate-action candidate exists long before the selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"290670","company_name":"대보마그네틱","profile_path":"atlas/symbol_profiles/290/290670.json","first_date":"2018-11-06","last_date":"2026-02-20","trading_day_count":1790,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2019-11-06","2019-11-26"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"089980","company_name":"상아프론테크","profile_path":"atlas/symbol_profiles/089/089980.json","first_date":"2011-07-21","last_date":"2026-02-20","trading_day_count":3585,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"222080","trigger_type":"Stage2-Actionable-BatteryEquipmentOrderbookCustomerRampBridge-Positive","entry_date":"2024-02-15","duplicate_status":"new C11 symbol/trigger/date combination outside top-covered and previous R3 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"290670","trigger_type":"Stage2-FalsePositive-BatteryMagneticEquipmentRebound-NoFreshOrderMarginBridge","entry_date":"2024-02-21","duplicate_status":"new C11 symbol/trigger/date combination outside top-covered and previous R3 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"089980","trigger_type":"Stage2-FalsePositive-SeparatorMaterialsRebound-NoCustomerCalloffMarginBridge","entry_date":"2024-05-22","duplicate_status":"new C11 symbol/trigger/date combination outside top-covered and previous R3 loop symbols"}
```

## 4. Research question

C11 is not “battery stock bounced.”  
The useful C11 signal must prove that price is connected to orderbook mechanics: order backlog, customer ramp, equipment acceptance, shipment schedule, utilization, call-off confidence, margin mix and cash conversion. A battery-equipment chart can spark like a welder, but E2R needs the signed purchase order, the delivery cadence and the margin schedule.

Residual question:

```text
Can C11 distinguish:
1. battery equipment orderbook/customer-ramp bridge with strong MFE,
2. battery magnetic-equipment rebound where no fresh order and margin bridge exists,
3. separator/materials rebound where no customer call-off, utilization or margin bridge exists?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C11_R3L89_222080_CIS_BATTERY_EQUIPMENT_ORDERBOOK","symbol":"222080","company_name":"씨아이에스","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_RAMP_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-BatteryEquipmentOrderbookCustomerRampBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge30_tolerable_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_orderbook_customer_ramp_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Battery-equipment orderbook/customer-ramp proxy produced MFE above 35% with tolerable early MAE. Later drawdown keeps Green strict and requires exact order/customer/margin evidence."}
{"row_type":"case","case_id":"C11_R3L89_290670_DAEBO_MAGNETIC_NO_FRESH_ORDER","symbol":"290670","company_name":"대보마그네틱","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_MAGNETIC_EQUIPMENT_REBOUND_WITHOUT_FRESH_ORDER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-BatteryMagneticEquipmentRebound-NoFreshOrderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_without_order_bridge","current_profile_verdict":"current_profile_false_positive_if_equipment_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Magnetic/battery-equipment rebound had sub-Yellow MFE and very deep MAE without fresh order, customer call-off, utilization or margin bridge."}
{"row_type":"case","case_id":"C11_R3L89_089980_SANGA_SEPARATOR_MATERIALS_REBOUND","symbol":"089980","company_name":"상아프론테크","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SEPARATOR_MATERIALS_REBOUND_WITHOUT_CUSTOMER_CALLOFF_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SeparatorMaterialsRebound-NoCustomerCalloffMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub_Yellow_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_separator_materials_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Separator/materials rebound had only modest MFE and later meaningful drawdown when customer call-off, utilization, margin and cash bridge failed to confirm."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 222080 씨아이에스 — battery-equipment orderbook/customer-ramp positive

Entry row: `2024-02-15 c=11000`.  
Observed path: entry-day low `10000`, peak `2024-03-11 h=15110`, and late-year low `2024-12-09 l=7050`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L89_C11_222080_20240215_STAGE2_BATTERY_EQUIPMENT_ORDERBOOK","case_id":"C11_R3L89_222080_CIS_BATTERY_EQUIPMENT_ORDERBOOK","symbol":"222080","company_name":"씨아이에스","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_RAMP_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-BatteryEquipmentOrderbookCustomerRampBridge-Positive","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":11000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_equipment_orderbook_customer_ramp_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; battery equipment orderbook, customer ramp and shipment bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["battery_equipment_orderbook_proxy","customer_ramp_proxy","shipment_schedule_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_order_pending","delivery_schedule_pending","margin_mix_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv","profile_path":"atlas/symbol_profiles/222/222080.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":37.36,"MFE_90D_pct":37.36,"MFE_180D_pct":37.36,"MAE_30D_pct":-9.09,"MAE_90D_pct":-9.09,"MAE_180D_pct":-28.00,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-11","peak_price":15110.0,"max_drawdown_low_date":"2024-10-18","max_drawdown_low":7920.0,"drawdown_after_peak_pct":-47.58,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B; late drawdown blocks Green without exact orderbook/customer/margin evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge30_tolerable_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_orderbook_customer_ramp_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"222080_2024-02-15_11000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C11 can allow Stage2/Yellow when equipment strength is tied to orderbook, customer ramp, shipment schedule, margin mix and cash bridge. Green remains strict because late drawdown can be large."}
```

### 6.2 290670 대보마그네틱 — battery magnetic-equipment rebound without fresh order/margin bridge

Entry row: `2024-02-21 c=30400`.  
Observed path: high `2024-03-08 h=33200`, later low `2024-12-09 l=10310`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L89_C11_290670_20240221_STAGE2_FALSE_POSITIVE_MAGNETIC_EQUIPMENT","case_id":"C11_R3L89_290670_DAEBO_MAGNETIC_NO_FRESH_ORDER","symbol":"290670","company_name":"대보마그네틱","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_MAGNETIC_EQUIPMENT_REBOUND_WITHOUT_FRESH_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-BatteryMagneticEquipmentRebound-NoFreshOrderMarginBridge","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":30400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_magnetic_equipment_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; magnetic/battery-equipment rebound treated as insufficient without fresh customer order, call-off, utilization, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["battery_equipment_rebound","relative_strength_rebound"],"stage3_evidence_fields":["fresh_order_bridge_missing","customer_calloff_missing","utilization_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","fresh_order_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/290/290670/2024.csv","profile_path":"atlas/symbol_profiles/290/290670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.21,"MFE_90D_pct":9.21,"MFE_180D_pct":9.21,"MAE_30D_pct":-13.16,"MAE_90D_pct":-33.06,"MAE_180D_pct":-66.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":33200.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":10310.0,"drawdown_after_peak_pct":-68.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"battery_equipment_rebound_without_fresh_order_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","fresh_order_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_without_order_bridge","current_profile_verdict":"current_profile_false_positive_if_equipment_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"290670_2024-02-21_30400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C11 should not promote battery-equipment rebound without fresh order, customer call-off, utilization, margin and cash bridge. Sub-10 MFE90 and severe MAE force Watch/4B-risk routing."}
```

### 6.3 089980 상아프론테크 — separator/materials rebound without customer call-off/margin bridge

Entry row: `2024-05-22 c=26350`.  
Observed path: high `2024-05-31 h=29350`, later low `2024-12-09 l=17710`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L89_C11_089980_20240522_STAGE2_FALSE_POSITIVE_SEPARATOR_MATERIALS","case_id":"C11_R3L89_089980_SANGA_SEPARATOR_MATERIALS_REBOUND","symbol":"089980","company_name":"상아프론테크","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SEPARATOR_MATERIALS_REBOUND_WITHOUT_CUSTOMER_CALLOFF_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-SeparatorMaterialsRebound-NoCustomerCalloffMarginBridge","trigger_date":"2024-05-22","entry_date":"2024-05-22","entry_price":26350.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_separator_materials_battery_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; separator/materials rebound treated as insufficient without customer call-off, shipment, utilization, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["separator_materials_rebound","battery_material_theme","relative_strength_extension"],"stage3_evidence_fields":["customer_calloff_missing","shipment_visibility_missing","utilization_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","customer_calloff_bridge_missing_watch","late_drawdown_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089980/2024.csv","profile_path":"atlas/symbol_profiles/089/089980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.39,"MFE_90D_pct":11.39,"MFE_180D_pct":11.39,"MAE_30D_pct":-10.25,"MAE_90D_pct":-18.03,"MAE_180D_pct":-32.79,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":29350.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":17710.0,"drawdown_after_peak_pct":-39.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"separator_materials_rebound_without_customer_calloff_margin_bridge_should_remain_watch_4B_not_Yellow","four_b_evidence_type":["price_only","customer_calloff_bridge_missing_watch","late_drawdown_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_separator_materials_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"089980_2024-05-22_26350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C11 should not equate separator/material rebound with orderbook rerating. Customer call-off, shipment, utilization and margin/cash bridge must be repaired before Yellow/Green promotion."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3L89_222080_CIS_BATTERY_EQUIPMENT_ORDERBOOK","trigger_id":"R3L89_C11_222080_20240215_STAGE2_BATTERY_EQUIPMENT_ORDERBOOK","symbol":"222080","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C11 requires orderbook, customer ramp, shipment schedule, margin mix and cash bridge rather than battery equipment theme alone","raw_component_scores_before":{"orderbook_quality_score":13,"customer_ramp_score":12,"shipment_schedule_score":11,"utilization_score":10,"margin_mix_score":9,"cash_conversion_score":6,"relative_strength_score":13,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"orderbook_quality_score":16,"customer_ramp_score":15,"shipment_schedule_score":14,"utilization_score":12,"margin_mix_score":11,"cash_conversion_score":8,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Orderbook/customer-ramp bridge plus MFE90>30 supports Yellow-watch; late drawdown and proxy-only evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3L89_290670_DAEBO_MAGNETIC_NO_FRESH_ORDER","trigger_id":"R3L89_C11_290670_20240221_STAGE2_FALSE_POSITIVE_MAGNETIC_EQUIPMENT","symbol":"290670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_scope":"current_default_proxy","profile_hypothesis":"battery equipment rebound without fresh order and margin bridge should be blocked","raw_component_scores_before":{"orderbook_quality_score":2,"customer_ramp_score":1,"shipment_schedule_score":0,"utilization_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":8,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"orderbook_quality_score":0,"customer_ramp_score":0,"shipment_schedule_score":0,"utilization_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-10 MFE90 and severe MAE convert equipment rebound into missing order/customer bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3L89_089980_SANGA_SEPARATOR_MATERIALS_REBOUND","trigger_id":"R3L89_C11_089980_20240522_STAGE2_FALSE_POSITIVE_SEPARATOR_MATERIALS","symbol":"089980","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_scope":"current_default_proxy","profile_hypothesis":"separator/materials rebound without customer call-off and margin bridge should remain Watch/blocked","raw_component_scores_before":{"orderbook_quality_score":1,"customer_ramp_score":1,"shipment_schedule_score":1,"utilization_score":1,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":9,"valuation_repricing_score":4,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"orderbook_quality_score":0,"customer_ramp_score":0,"shipment_schedule_score":0,"utilization_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-18,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-Yellow MFE and late drawdown require customer call-off, shipment/utilization and margin/cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L89_C11_P0_CURRENT","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C11 needs explicit orderbook/customer-ramp/shipment/utilization/margin/cash bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":19.32,"avg_MAE90_pct":-20.06,"avg_MFE180_pct":19.32,"avg_MAE180_pct":-42.29,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C11_orderbook_customer_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R3L89_C11_P1_SECTOR_SPECIFIC","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_id":"P1_L3_battery_orderbook_customer_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 battery-orderbook signals need orderbook quality, customer ramp, shipment schedule, utilization, margin mix or cash conversion before Stage2-Actionable","changed_axes":["orderbook_quality_required","customer_calloff_required","equipment_material_rebound_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_orderbook_customer_ramp_shipment_utilization_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":19.32,"avg_MAE90_pct":-20.06,"avg_MFE180_pct":19.32,"avg_MAE180_pct":-42.29,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R3L89_C11_P2_CANONICAL","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_id":"P2_C11_orderbook_customer_margin_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C11 should reward orderbook-to-margin mechanics, not equipment/material rebound labels","changed_axes":["C11_orderbook_customer_ramp_margin_bridge_required","C11_equipment_material_rebound_local_4B_guard","C11_late_drawdown_Green_strict_guard"],"changed_thresholds":{"stage2_yellow_gate":"orderbook_or_customer_ramp_plus_shipment_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":19.32,"avg_MAE90_pct":-20.06,"avg_MFE180_pct":19.32,"avg_MAE180_pct":-42.29,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R3L89_C11_P3_COUNTEREXAMPLE_GUARD","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_id":"P3_C11_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<12 and MAE180<=-30 while orderbook/customer bridge is missing, block Yellow/Green and route to 4B-watch","changed_axes":["C11_low_MFE_guardrail","C11_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_12_and_MAE180_le_minus_30_with_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":19.32,"avg_MAE90_pct":-20.06,"avg_MFE180_pct":19.32,"avg_MAE180_pct":-42.29,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_ORDERBOOK_VS_MATERIAL_REBOUND_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":19.32,"avg_MAE90_pct":-20.06,"avg_MFE180_pct":19.32,"avg_MAE180_pct":-42.29,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_12":0.67,"stage2_bad_entry_rate_MAE180_le_minus_30":1.0,"interpretation":"C11 needs bridge discipline. 씨아이에스 shows battery-equipment orderbook/customer-ramp bridge can support Yellow-watch, while 대보마그네틱 and 상아프론테크 show equipment/material rebounds should not be promoted without fresh order, customer call-off, utilization, margin and cash bridge."}
{"row_type":"stage_transition_summary","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"222080","trigger_type":"Stage2-Actionable-BatteryEquipmentOrderbookCustomerRampBridge-Positive","entry_date":"2024-02-15","stage2_to_90D_outcome":"good_stage2_MFE90_ge30_tolerable_MAE","stage2_to_180D_outcome":"watch_positive_with_late_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when orderbook, customer ramp, shipment and margin bridge exists; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"290670","trigger_type":"Stage2-FalsePositive-BatteryMagneticEquipmentRebound-NoFreshOrderMarginBridge","entry_date":"2024-02-21","stage2_to_90D_outcome":"bad_stage2_sub_10_MFE_deep_MAE","stage2_to_180D_outcome":"failed_equipment_rebound_extreme_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Battery equipment rebound without fresh order/customer bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"089980","trigger_type":"Stage2-FalsePositive-SeparatorMaterialsRebound-NoCustomerCalloffMarginBridge","entry_date":"2024-05-22","stage2_to_90D_outcome":"weak_stage2_sub_Yellow_MFE","stage2_to_180D_outcome":"failed_material_rebound_late_drawdown","MFE90_ge_20":false,"MAE180_le_minus_30":true,"transition_note":"Separator/materials rebound without customer call-off and margin bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","residual_type":"battery_equipment_material_rebound_overcredit_without_orderbook_customer_margin_bridge","contribution":"Adds two C11 local 4B/deep-MAE counterexamples against one battery-equipment orderbook positive, avoiding C11 top-covered and previous R3 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_RAMP_BRIDGE_VS_SEPARATOR_MAGNETIC_EQUIPMENT_REBOUND_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C11 now has non-top-symbol battery-equipment orderbook positive and two magnetic-equipment / separator-materials weak-bridge counterexamples; next R3 loops should exact-URL repair orderbook quality, customer ramp, shipment schedule, utilization, margin mix and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","axis":"C11_orderbook_customer_ramp_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"222080 worked when orderbook/customer-ramp proxy was present; 290670 and 089980 failed when only battery equipment/material rebound existed."}
{"row_type":"shadow_weight","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","axis":"C11_equipment_material_rebound_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Equipment/material rebound rows showed sub-12 MFE90 and deep 180D MAE without non-price orderbook/customer bridge."}
{"row_type":"shadow_weight","round":"R3","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","axis":"C11_late_drawdown_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"222080 is a positive-control row but later drawdown shows that Green should require exact orderbook, delivery, margin and cash evidence."}
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
  - battery_equipment_rebound_overcredit
  - separator_materials_rebound_overcredit
  - fresh_order_customer_calloff_bridge_missing
  - utilization_margin_cash_bridge_missing
new_axis_proposed:
  - C11_orderbook_customer_ramp_margin_bridge_required_shadow_only
  - C11_equipment_material_rebound_local_4B_watch_guard_shadow_only
  - C11_late_drawdown_Green_strict_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C11
  - full_4b_requires_non_price_evidence within C11
  - hard_4c_thesis_break_routes_to_4c within C11
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
3. Confirm R3 / L3 / C11 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C11 top-covered symbols
   - previous R3 loop85 C11 symbols
   - previous R3 loop86 C12 symbols
   - previous R3 loop87 C13 symbols
   - previous R3 loop88 C14 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C11-scoped safe patch candidates:
   - C11_orderbook_customer_ramp_margin_bridge_required
   - C11_equipment_material_rebound_local_4B_watch_guard
   - C11_late_drawdown_Green_strict_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R3
completed_loop = 89
next_round = R4
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.
```
