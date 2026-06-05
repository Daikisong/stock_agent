# E2R Stock-Web v12 Residual Research — R2 Loop 89 / L2 / C10

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 89
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: HBM_MEMORY_EQUIPMENT_CUSTOMER_RAMP_BRIDGE_VS_PARTS_MATERIALS_LATE_CYCLE_REBOUND_DECAY
sector: AI / semiconductor / memory recovery / equipment cycle / HBM / parts / materials
output_file: e2r_stock_web_v12_residual_round_R2_loop_89_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R1 loop 89`.

```text
scheduled_round = R2
scheduled_loop = 89
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

R2 is restricted to AI / semiconductor / electronics.  
C10 is selected because recent R2 loops already covered:

```text
R2 loop85: C06_HBM_MEMORY_CUSTOMER_CAPACITY
R2 loop86: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
R2 loop87: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
R2 loop88: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

No-Repeat Index snapshot:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
rows = 29
symbols = 18
good/bad Stage2 = 15/5
4B/4C = 1/0
top-covered = 089970, 281820, 319660, 042700, 064290, 079370
```

This loop avoids the C10 top-covered set and also avoids the recent R2 loop symbols:

```text
R2 loop85 C06: 000660, 005930, 009150
R2 loop86 C07: 042700, 064760, 003160
R2 loop87 C08: 232140, 425420, 098120
R2 loop88 C09: 039030, 412350, 253590
```

Selected symbols:

```text
403870, 166090, 074600
```

This loop tests memory recovery / equipment-cycle mechanics, not simply “semiconductor chart strength.”  
The positive-control row is an HBM/advanced-equipment customer-ramp proxy. The counterexamples test parts/materials and quartz/material late-cycle rebounds where customer ramp, shipment, utilization, margin and cash bridge are missing or stale.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"403870","company_name":"HPSP","profile_path":"atlas/symbol_profiles/403/403870.json","first_date":"2022-07-15","last_date":"2026-02-20","trading_day_count":879,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2023-03-16","2023-04-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"166090","company_name":"하나머티리얼즈","profile_path":"atlas/symbol_profiles/166/166090.json","first_date":"2017-04-28","last_date":"2026-02-20","trading_day_count":2158,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2018-06-14","2018-07-10"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"074600","company_name":"원익QnC","profile_path":"atlas/symbol_profiles/074/074600.json","first_date":"2003-12-12","last_date":"2026-02-20","trading_day_count":5476,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2004-06-25","2004-07-21","2017-04-28","2017-05-24"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"403870","trigger_type":"Stage2-Actionable-HBMMemoryEquipmentCustomerRampBridge-Positive","entry_date":"2024-01-18","duplicate_status":"new C10 symbol/trigger/date combination outside top-covered and previous R2 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"166090","trigger_type":"Stage2-FalsePositive-SemiPartsLateCycleRampNoFreshCustomerMarginBridge","entry_date":"2024-06-26","duplicate_status":"new C10 symbol/trigger/date combination outside top-covered and previous R2 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"074600","trigger_type":"Stage2-FalsePositive-QuartzMaterialsLateCycleSpikeNoOrderMarginBridge","entry_date":"2024-06-07","duplicate_status":"new C10 symbol/trigger/date combination outside top-covered and previous R2 loop symbols"}
```

## 4. Research question

C10 is not “반도체가 회복된다.”  
The useful memory-recovery/equipment-cycle signal must show the bridge from cycle language to realized business: memory customer capex, HBM or advanced node fit, shipment acceptance, tool utilization, consumables demand, order visibility, margin mix and cash conversion. Otherwise, a semiconductor rebound is just a cleanroom light turning on; it does not prove wafers are running through profitable tools.

Residual question:

```text
Can C10 distinguish:
1. HBM / advanced memory equipment customer-ramp bridge with high MFE,
2. semiconductor parts late-cycle extension where previous memory beta does not equal fresh customer-order or margin bridge,
3. quartz/materials spike where local theme strength fades without shipment/utilization and cash conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C10_R2L89_403870_HPSP_HBM_EQUIPMENT_RAMP","symbol":"403870","company_name":"HPSP","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"HBM_MEMORY_EQUIPMENT_CUSTOMER_RAMP_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-HBMMemoryEquipmentCustomerRampBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE90_moderate_late_MAE","current_profile_verdict":"current_profile_correct_if_customer_ramp_shipment_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"HBM/advanced-equipment customer ramp proxy produced a strong early MFE. Later deep drawdown keeps Green strict and requires exact customer ramp, shipment and margin evidence."}
{"row_type":"case","case_id":"C10_R2L89_166090_HANA_MATERIALS_LATE_CYCLE","symbol":"166090","company_name":"하나머티리얼즈","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SEMI_PARTS_LATE_CYCLE_RAMP_WITHOUT_FRESH_CUSTOMER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SemiPartsLateCycleRampNoFreshCustomerMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub_Yellow_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_parts_late_cycle_extension_overcredited","price_source":"Songdaiki/stock-web","notes":"Late-cycle semiconductor parts ramp had sub-Yellow MFE and severe MAE without fresh customer order, utilization, margin or cash bridge."}
{"row_type":"case","case_id":"C10_R2L89_074600_WONIK_QNC_QUARTZ_MATERIALS_SPIKE","symbol":"074600","company_name":"원익QnC","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_MATERIALS_LATE_CYCLE_SPIKE_WITHOUT_ORDER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-QuartzMaterialsLateCycleSpikeNoOrderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_extreme_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_quartz_materials_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Quartz/materials spike had nearly zero MFE after the selected entry and extreme later MAE without order visibility, customer utilization, margin and cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 403870 HPSP — HBM / advanced memory equipment customer-ramp bridge positive

Entry row: `2024-01-18 c=44050`.  
Observed path: high `2024-02-15 h=63900`, later low `2024-11-22 l=28000`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L89_C10_403870_20240118_STAGE2_HBM_EQUIPMENT_RAMP","case_id":"C10_R2L89_403870_HPSP_HBM_EQUIPMENT_RAMP","symbol":"403870","company_name":"HPSP","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"HBM_MEMORY_EQUIPMENT_CUSTOMER_RAMP_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-HBMMemoryEquipmentCustomerRampBridge-Positive","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":44050.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_HBM_advanced_memory_equipment_customer_ramp_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; HBM/advanced memory equipment customer ramp and shipment bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["HBM_equipment_ramp_proxy","customer_CAPEX_proxy","shipment_acceptance_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_ramp_pending","order_visibility_pending","margin_mix_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv","profile_path":"atlas/symbol_profiles/403/403870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":45.06,"MFE_90D_pct":45.06,"MFE_180D_pct":45.06,"MAE_30D_pct":-6.47,"MAE_90D_pct":-19.07,"MAE_180D_pct":-36.44,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-15","peak_price":63900.0,"max_drawdown_low_date":"2024-11-22","max_drawdown_low":28000.0,"drawdown_after_peak_pct":-56.18,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_late_drawdown_blocks_Green_without_exact_customer_ramp_order_margin_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_moderate_late_MAE","current_profile_verdict":"current_profile_correct_if_customer_ramp_shipment_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"403870_2024-01-18_44050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C10 can allow Stage2/Yellow when memory recovery is tied to customer ramp, shipment acceptance, order visibility and margin bridge. Green remains strict because late drawdown can be large."}
```

### 6.2 166090 하나머티리얼즈 — semiconductor parts late-cycle ramp without fresh customer/margin bridge

Entry row: `2024-06-26 c=63900`.  
Observed path: high `2024-07-02 h=69300`, low `2024-09-24 l=29500`, and later low `2024-12-09 l=21850`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L89_C10_166090_20240626_STAGE2_FALSE_POSITIVE_PARTS_LATE_CYCLE","case_id":"C10_R2L89_166090_HANA_MATERIALS_LATE_CYCLE","symbol":"166090","company_name":"하나머티리얼즈","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"SEMI_PARTS_LATE_CYCLE_RAMP_WITHOUT_FRESH_CUSTOMER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SemiPartsLateCycleRampNoFreshCustomerMarginBridge","trigger_date":"2024-06-26","entry_date":"2024-06-26","entry_price":63900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_semiconductor_parts_late_cycle_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; semiconductor parts late-cycle rebound treated as insufficient without fresh customer order, utilization, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["semi_parts_late_cycle_rebound","memory_recovery_beta","relative_strength_extension"],"stage3_evidence_fields":["fresh_customer_order_missing","utilization_bridge_missing","margin_mix_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_late_extension","customer_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/166/166090/2024.csv","profile_path":"atlas/symbol_profiles/166/166090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.45,"MFE_90D_pct":8.45,"MFE_180D_pct":8.45,"MAE_30D_pct":-18.15,"MAE_90D_pct":-53.83,"MAE_180D_pct":-65.81,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":69300.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":21850.0,"drawdown_after_peak_pct":-68.47,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"semi_parts_late_cycle_rebound_without_fresh_customer_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","customer_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_parts_late_cycle_extension_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"166090_2024-06-26_63900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C10 should not promote semiconductor parts late-cycle strength unless fresh customer order, utilization, margin mix and cash bridge are repaired. Sub-Yellow MFE and severe MAE force Watch/4B-risk routing."}
```

### 6.3 074600 원익QnC — quartz/materials late-cycle spike without order/margin bridge

Entry row: `2024-06-07 c=40950`.  
Observed path: local high `2024-06-07 h=41000`, then lows `2024-09-24 l=23850`, `2024-11-14 l=19000`, and `2024-12-09 l=16680`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L89_C10_074600_20240607_STAGE2_FALSE_POSITIVE_QUARTZ_MATERIALS_SPIKE","case_id":"C10_R2L89_074600_WONIK_QNC_QUARTZ_MATERIALS_SPIKE","symbol":"074600","company_name":"원익QnC","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_MATERIALS_LATE_CYCLE_SPIKE_WITHOUT_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-QuartzMaterialsLateCycleSpikeNoOrderMarginBridge","trigger_date":"2024-06-07","entry_date":"2024-06-07","entry_price":40950.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_quartz_materials_memory_recovery_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; quartz/materials memory-cycle spike treated as insufficient without confirmed order visibility, utilization, shipment and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["quartz_materials_spike","memory_recovery_beta","relative_strength_blowoff"],"stage3_evidence_fields":["fresh_order_visibility_missing","customer_utilization_missing","shipment_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","order_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/074/074600/2024.csv","profile_path":"atlas/symbol_profiles/074/074600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.12,"MFE_90D_pct":0.12,"MFE_180D_pct":0.12,"MAE_30D_pct":-13.68,"MAE_90D_pct":-41.76,"MAE_180D_pct":-59.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-07","peak_price":41000.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":16680.0,"drawdown_after_peak_pct":-59.32,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"quartz_materials_memory_recovery_spike_without_order_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","order_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_extreme_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_quartz_materials_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"074600_2024-06-07_40950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C10 should not treat a quartz/materials memory-recovery spike as customer-ramp proof. Near-zero MFE and extreme 180D MAE require Watch/4B-risk unless order, utilization, shipment and margin evidence is exact-repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_R2L89_403870_HPSP_HBM_EQUIPMENT_RAMP","trigger_id":"R2L89_C10_403870_20240118_STAGE2_HBM_EQUIPMENT_RAMP","symbol":"403870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C10 requires customer ramp, shipment acceptance, order visibility, margin mix and cash bridge rather than memory-cycle label alone","raw_component_scores_before":{"customer_ramp_score":13,"HBM_equipment_fit_score":14,"shipment_acceptance_score":11,"order_visibility_score":10,"utilization_score":10,"margin_mix_score":9,"cash_conversion_score":6,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"customer_ramp_score":16,"HBM_equipment_fit_score":17,"shipment_acceptance_score":14,"order_visibility_score":13,"utilization_score":12,"margin_mix_score":11,"cash_conversion_score":8,"relative_strength_score":15,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Customer-ramp and HBM equipment bridge plus high early MFE support Yellow/Green-candidate watch; late drawdown and proxy-only evidence keep Green strict."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_R2L89_166090_HANA_MATERIALS_LATE_CYCLE","trigger_id":"R2L89_C10_166090_20240626_STAGE2_FALSE_POSITIVE_PARTS_LATE_CYCLE","symbol":"166090","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_scope":"current_default_proxy","profile_hypothesis":"late semi-parts rebound without fresh customer and margin bridge should be blocked","raw_component_scores_before":{"customer_ramp_score":2,"HBM_equipment_fit_score":3,"shipment_acceptance_score":1,"order_visibility_score":0,"utilization_score":1,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_ramp_score":0,"HBM_equipment_fit_score":1,"shipment_acceptance_score":0,"order_visibility_score":0,"utilization_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-Yellow MFE and deep MAE convert late semi-parts extension into missing customer/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_R2L89_074600_WONIK_QNC_QUARTZ_MATERIALS_SPIKE","trigger_id":"R2L89_C10_074600_20240607_STAGE2_FALSE_POSITIVE_QUARTZ_MATERIALS_SPIKE","symbol":"074600","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_scope":"current_default_proxy","profile_hypothesis":"quartz/materials spike without order and margin bridge should remain Watch/blocked","raw_component_scores_before":{"customer_ramp_score":1,"HBM_equipment_fit_score":2,"shipment_acceptance_score":0,"order_visibility_score":0,"utilization_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":9,"valuation_repricing_score":4,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_ramp_score":0,"HBM_equipment_fit_score":0,"shipment_acceptance_score":0,"order_visibility_score":0,"utilization_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and extreme MAE require order, utilization, shipment and margin bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L89_C10_P0_CURRENT","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C10 needs explicit customer-ramp, order visibility, utilization, shipment, margin and cash bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":17.88,"avg_MAE90_pct":-38.22,"avg_MFE180_pct":17.88,"avg_MAE180_pct":-53.84,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C10_customer_ramp_order_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L89_C10_P1_SECTOR_SPECIFIC","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_id":"P1_L2_memory_equipment_customer_ramp_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 memory-recovery signals need customer capex/ramp, shipment acceptance, order visibility, utilization, margin mix or cash conversion before Stage2-Actionable","changed_axes":["customer_ramp_required","shipment_order_required","parts_materials_late_cycle_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_ramp_order_shipment_utilization_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":17.88,"avg_MAE90_pct":-38.22,"avg_MFE180_pct":17.88,"avg_MAE180_pct":-53.84,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L89_C10_P2_CANONICAL","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_id":"P2_C10_customer_ramp_order_margin_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C10 should reward customer-ramp and order-to-margin mechanics, not late parts/materials cycle labels","changed_axes":["C10_customer_ramp_order_margin_bridge_required","C10_parts_materials_late_cycle_local_4B_guard","C10_late_drawdown_Green_strict_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_ramp_or_order_visibility_plus_shipment_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":17.88,"avg_MAE90_pct":-38.22,"avg_MFE180_pct":17.88,"avg_MAE180_pct":-53.84,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L89_C10_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_id":"P3_C10_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-35 while customer/order/margin bridge is missing, block Yellow/Green and route to 4B-watch","changed_axes":["C10_low_MFE_guardrail","C10_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_35_with_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":17.88,"avg_MAE90_pct":-38.22,"avg_MFE180_pct":17.88,"avg_MAE180_pct":-53.84,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_HBM_EQUIPMENT_RAMP_VS_PARTS_MATERIALS_LATE_CYCLE_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":17.88,"avg_MAE90_pct":-38.22,"avg_MFE180_pct":17.88,"avg_MAE180_pct":-53.84,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_35":0.67,"interpretation":"C10 needs bridge discipline. HPSP shows HBM/advanced equipment customer-ramp bridge can support Yellow-watch, while 하나머티리얼즈 and 원익QnC show late parts/materials cycle spikes should not be promoted without fresh customer order, utilization, shipment, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"403870","trigger_type":"Stage2-Actionable-HBMMemoryEquipmentCustomerRampBridge-Positive","entry_date":"2024-01-18","stage2_to_90D_outcome":"good_stage2_high_MFE_moderate_MAE","stage2_to_180D_outcome":"watch_positive_with_deep_late_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when customer ramp, order visibility, shipment and margin bridge exists; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"166090","trigger_type":"Stage2-FalsePositive-SemiPartsLateCycleRampNoFreshCustomerMarginBridge","entry_date":"2024-06-26","stage2_to_90D_outcome":"bad_stage2_sub_Yellow_MFE_deep_MAE","stage2_to_180D_outcome":"failed_semi_parts_late_cycle_extreme_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Late semi-parts cycle rebound without fresh customer/margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"074600","trigger_type":"Stage2-FalsePositive-QuartzMaterialsLateCycleSpikeNoOrderMarginBridge","entry_date":"2024-06-07","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_quartz_materials_spike_extreme_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Quartz/materials spike without order/utilization/margin bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","residual_type":"memory_recovery_parts_materials_late_cycle_overcredit_without_customer_ramp_order_margin_bridge","contribution":"Adds two C10 4B/deep-MAE counterexamples against one HBM equipment customer-ramp positive, avoiding C10 top-covered and recent R2 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"HBM_MEMORY_EQUIPMENT_CUSTOMER_RAMP_BRIDGE_VS_PARTS_MATERIALS_LATE_CYCLE_REBOUND_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C10 now has non-top-symbol HBM equipment ramp positive and two parts/materials late-cycle counterexamples; next R2 loops should exact-URL repair customer ramp, shipment acceptance, order visibility, utilization, margin mix and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","axis":"C10_customer_ramp_order_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"403870 worked when HBM equipment/customer-ramp proxy existed; 166090 and 074600 failed when only late-cycle parts/materials strength existed."}
{"row_type":"shadow_weight","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","axis":"C10_parts_materials_late_cycle_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Parts/materials late-cycle rows showed sub-10 MFE90 and severe MAE without non-price customer/order/margin bridge."}
{"row_type":"shadow_weight","round":"R2","loop":"89","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","axis":"C10_late_drawdown_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"403870 is a positive-control row but later drawdown shows that Green should require exact customer ramp, shipment, margin and cash evidence."}
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
  - memory_recovery_late_cycle_overcredit
  - parts_materials_theme_overcredit
  - fresh_customer_order_bridge_missing
  - utilization_margin_cash_bridge_missing
new_axis_proposed:
  - C10_customer_ramp_order_margin_bridge_required_shadow_only
  - C10_parts_materials_late_cycle_local_4B_watch_guard_shadow_only
  - C10_late_drawdown_Green_strict_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C10
  - full_4b_requires_non_price_evidence within C10
  - hard_4c_thesis_break_routes_to_4c within C10
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
3. Confirm R2 / L2 / C10 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C10 top-covered symbols
   - previous R2 loop85 C06 symbols
   - previous R2 loop86 C07 symbols
   - previous R2 loop87 C08 symbols
   - previous R2 loop88 C09 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C10-scoped safe patch candidates:
   - C10_customer_ramp_order_margin_bridge_required
   - C10_parts_materials_late_cycle_local_4B_watch_guard
   - C10_late_drawdown_Green_strict_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 89
next_round = R3
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.
```
