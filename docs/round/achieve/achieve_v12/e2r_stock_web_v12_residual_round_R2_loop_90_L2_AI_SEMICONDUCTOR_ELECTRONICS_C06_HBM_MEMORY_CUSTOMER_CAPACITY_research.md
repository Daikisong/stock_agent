# E2R Stock-Web v12 Residual Research — R2 Loop 90 / L2 / C06

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 90
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: MEMORY_BACKEND_CAPACITY_CUSTOMER_BRIDGE_VS_OSAT_AI_IP_PRICE_ONLY_DECAY
sector: AI / semiconductor / HBM / memory capacity / backend OSAT / AI semiconductor IP
output_file: e2r_stock_web_v12_residual_round_R2_loop_90_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R1 loop 90`.

```text
scheduled_round = R2
scheduled_loop = 90
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

R2 is restricted to AI / semiconductor / electronics.  
C06 is selected because the previous R2 loop sequence already rotated through:

```text
R2 loop85: C06_HBM_MEMORY_CUSTOMER_CAPACITY
R2 loop86: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
R2 loop87: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
R2 loop88: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
R2 loop89: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

After C10, the R2 lane returns to C06.  
No-Repeat Index snapshot:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
rows = 7
symbols = 6
good/bad Stage2 = 4/1
4B/4C = 0/0
top-covered = 000660, 005930, 009150, 014680, 067310, 402340
```

This loop avoids C06 top-covered symbols and recent R2 loop symbols:

```text
R2 loop85 C06: 000660, 005930, 009150
R2 loop86 C07: 042700, 064760, 003160
R2 loop87 C08: 232140, 425420, 098120
R2 loop88 C09: 039030, 412350, 253590
R2 loop89 C10: 403870, 166090, 074600
```

Selected symbols:

```text
036540, 033170, 394280
```

The selected pocket is:

```text
memory backend / OSAT customer-capacity bridge
vs
OSAT packaging price spike without confirmed HBM customer-capacity conversion
vs
AI semiconductor IP blowoff without HBM memory capacity, wafer/customer or shipment bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"036540","company_name":"SFA반도체","profile_path":"atlas/symbol_profiles/036/036540.json","first_date":"2001-05-02","last_date":"2026-02-20","trading_day_count":6121,"corporate_action_candidate_count":7,"corporate_action_candidate_dates":["2003-12-22","2009-06-24","2010-07-20","2011-06-30","2014-06-13","2015-10-06","2016-01-04"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"033170","company_name":"시그네틱스","profile_path":"atlas/symbol_profiles/033/033170.json","first_date":"2010-11-26","last_date":"2026-02-20","trading_day_count":3746,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"394280","company_name":"오픈엣지테크놀로지","profile_path":"atlas/symbol_profiles/394/394280.json","first_date":"2022-09-26","last_date":"2026-02-20","trading_day_count":831,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"036540","trigger_type":"Stage2-Actionable-MemoryBackendCustomerCapacityBridge-Positive","entry_date":"2024-01-18","duplicate_status":"new C06 symbol/trigger/date combination outside C06 top-covered and previous R2 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"033170","trigger_type":"Stage2-FalsePositive-OSATPackagingThemeNoHBMCustomerCapacityBridge","entry_date":"2024-02-22","duplicate_status":"new C06 symbol/trigger/date combination outside C06 top-covered and previous R2 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"394280","trigger_type":"Stage2-FalsePositive-AISemiconductorIPBlowoffNoMemoryCustomerCapacityBridge","entry_date":"2024-02-22","duplicate_status":"new C06 symbol/trigger/date combination outside C06 top-covered and previous R2 loop symbols"}
```

## 4. Research question

C06 is not “AI 반도체가 올랐다.”  
The useful HBM / memory customer-capacity signal must prove a physical capacity bridge:

```text
memory customer capex
HBM or advanced memory exposure
wafer / package / backend capacity utilization
customer ramp
shipment or qualification acceptance
order visibility
margin mix
cash conversion
```

An AI-semiconductor headline without that bridge is a wafer map projected on a wall; it looks technical, but no tested device has shipped. C06 should reward the factory line, not the slide deck.

Residual question:

```text
Can C06 distinguish:
1. backend / OSAT customer-capacity bridge that creates a high MFE path but still requires exact evidence before Green,
2. OSAT packaging price spike where later collapse proves missing HBM customer-capacity bridge,
3. AI semiconductor IP blowoff where local MFE is not memory capacity evidence?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C06_R2L90_036540_SFA_MEMORY_BACKEND_CAPACITY","symbol":"036540","company_name":"SFA반도체","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"MEMORY_BACKEND_CUSTOMER_CAPACITY_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-MemoryBackendCustomerCapacityBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_low_early_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_customer_capacity_ramp_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Backend/OSAT memory customer-capacity proxy produced high early MFE with low early MAE. Late drawdown keeps Green strict and requires exact customer ramp, utilization, shipment and margin evidence."}
{"row_type":"case","case_id":"C06_R2L90_033170_SIGNETICS_OSAT_PACKAGING_THEME","symbol":"033170","company_name":"시그네틱스","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"OSAT_PACKAGING_THEME_WITHOUT_HBM_CUSTOMER_CAPACITY_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-OSATPackagingThemeNoHBMCustomerCapacityBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub_Yellow_MFE_deep_MAE_no_capacity_bridge","current_profile_verdict":"current_profile_false_positive_if_OSAT_packaging_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"OSAT packaging theme had sub-Yellow MFE and deep later MAE without confirmed HBM customer-capacity conversion, utilization or margin bridge."}
{"row_type":"case","case_id":"C06_R2L90_394280_OPENEDGE_AI_IP_BLOWOFF","symbol":"394280","company_name":"오픈엣지테크놀로지","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_SEMICONDUCTOR_IP_BLOWOFF_WITHOUT_MEMORY_CUSTOMER_CAPACITY_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AISemiconductorIPBlowoffNoMemoryCustomerCapacityBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_local_MFE_deep_MAE_no_customer_capacity_bridge","current_profile_verdict":"current_profile_false_positive_if_AI_IP_blowoff_counted_as_HBM_capacity","price_source":"Songdaiki/stock-web","notes":"AI semiconductor IP blowoff had local MFE but deep MAE. Without memory customer capex, capacity, qualification/shipment and margin bridge, it should stay 4B-watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 036540 SFA반도체 — memory backend / OSAT customer-capacity bridge positive

Entry row: `2024-01-18 c=5920`.  
Observed path: entry low `2024-01-18 l=5800`, high `2024-01-24 h=8150`, and late-year low `2024-12-09 l=2820`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L90_C06_036540_20240118_STAGE2_MEMORY_BACKEND_CAPACITY","case_id":"C06_R2L90_036540_SFA_MEMORY_BACKEND_CAPACITY","symbol":"036540","company_name":"SFA반도체","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"MEMORY_BACKEND_CUSTOMER_CAPACITY_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-MemoryBackendCustomerCapacityBridge-Positive","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":5920.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_memory_backend_customer_capacity_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; backend/OSAT memory customer capacity, utilization and shipment bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["memory_customer_capacity_proxy","backend_OSAT_utilization_proxy","customer_ramp_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_capacity_source_pending","qualification_or_shipment_acceptance_pending","utilization_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036540/2024.csv","profile_path":"atlas/symbol_profiles/036/036540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":37.67,"MFE_90D_pct":37.67,"MFE_180D_pct":37.67,"MAE_30D_pct":-2.03,"MAE_90D_pct":-7.09,"MAE_180D_pct":-52.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-24","peak_price":8150.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":2820.0,"drawdown_after_peak_pct":-65.40,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_late_drawdown_blocks_Green_without_exact_customer_capacity_utilization_margin_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_low_early_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_customer_capacity_ramp_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"036540_2024-01-18_5920","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C06 can allow Stage2/Yellow when HBM/memory strength is tied to customer capacity, backend utilization, customer ramp, shipment acceptance, margin and cash bridge. Green still requires exact source-grade evidence."}
```

### 6.2 033170 시그네틱스 — OSAT packaging theme without HBM customer-capacity bridge

Entry row: `2024-02-22 c=2035`, after the price spike.  
Observed path: high `2024-03-13 h=2335`, then deep lows through `2024-12-09 l=657`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L90_C06_033170_20240222_STAGE2_FALSE_POSITIVE_OSAT_PACKAGING_THEME","case_id":"C06_R2L90_033170_SIGNETICS_OSAT_PACKAGING_THEME","symbol":"033170","company_name":"시그네틱스","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"OSAT_PACKAGING_THEME_WITHOUT_HBM_CUSTOMER_CAPACITY_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-OSATPackagingThemeNoHBMCustomerCapacityBridge","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":2035.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_OSAT_packaging_HBM_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; OSAT/packaging theme treated as insufficient without confirmed HBM customer capacity, utilization, shipment and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["OSAT_packaging_theme","HBM_keyword","relative_strength_spike"],"stage3_evidence_fields":["confirmed_HBM_customer_capacity_missing","utilization_bridge_missing","qualification_shipment_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_MFE","capacity_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033170/2024.csv","profile_path":"atlas/symbol_profiles/033/033170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.74,"MFE_90D_pct":14.74,"MFE_180D_pct":14.74,"MAE_30D_pct":-19.21,"MAE_90D_pct":-29.24,"MAE_180D_pct":-67.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":2335.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":657.0,"drawdown_after_peak_pct":-71.86,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"OSAT_packaging_theme_without_HBM_customer_capacity_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","customer_capacity_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_MAE_no_capacity_bridge","current_profile_verdict":"current_profile_false_positive_if_OSAT_packaging_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"033170_2024-02-22_2035","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C06 should not promote OSAT/packaging theme strength unless HBM customer capacity, utilization, qualification/shipment, margin and cash bridge are exact-repaired. Sub-Yellow MFE and deep MAE require 4B-watch routing."}
```

### 6.3 394280 오픈엣지테크놀로지 — AI semiconductor IP blowoff without HBM memory customer-capacity bridge

Entry row: `2024-02-22 c=35000`, after the AI semiconductor IP blowoff.  
Observed path: high `2024-03-07 h=38800`, then deep lows to `2024-12-09 l=9550`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L90_C06_394280_20240222_STAGE2_FALSE_POSITIVE_AI_IP_BLOWOFF","case_id":"C06_R2L90_394280_OPENEDGE_AI_IP_BLOWOFF","symbol":"394280","company_name":"오픈엣지테크놀로지","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_SEMICONDUCTOR_IP_BLOWOFF_WITHOUT_MEMORY_CUSTOMER_CAPACITY_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate;price_only_blowoff_stress_test","trigger_type":"Stage2-FalsePositive-AISemiconductorIPBlowoffNoMemoryCustomerCapacityBridge","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":35000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_AI_semiconductor_IP_blowoff_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; AI semiconductor IP theme treated as insufficient for C06 without memory customer capacity, wafer/package ramp, shipment qualification and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["AI_semiconductor_IP_theme","relative_strength_blowoff"],"stage3_evidence_fields":["memory_customer_capacity_missing","wafer_package_ramp_missing","shipment_qualification_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_MFE","customer_capacity_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/394/394280/2024.csv","profile_path":"atlas/symbol_profiles/394/394280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.86,"MFE_90D_pct":10.86,"MFE_180D_pct":10.86,"MAE_30D_pct":-23.43,"MAE_90D_pct":-42.71,"MAE_180D_pct":-72.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":38800.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":9550.0,"drawdown_after_peak_pct":-75.39,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"AI_semiconductor_IP_blowoff_without_memory_customer_capacity_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","customer_capacity_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_local_MFE_deep_MAE_no_customer_capacity_bridge","current_profile_verdict":"current_profile_false_positive_if_AI_IP_blowoff_counted_as_HBM_capacity","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"394280_2024-02-22_35000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C06 should not count AI semiconductor IP local MFE as HBM memory capacity evidence. Customer capex, capacity ramp, qualification/shipment and margin/cash bridge must be repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L90_036540_SFA_MEMORY_BACKEND_CAPACITY","trigger_id":"R2L90_C06_036540_20240118_STAGE2_MEMORY_BACKEND_CAPACITY","symbol":"036540","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C06 requires HBM/memory customer capacity, backend utilization, customer ramp, qualification/shipment, margin and cash bridge rather than AI semiconductor label alone","raw_component_scores_before":{"customer_capacity_score":13,"HBM_memory_exposure_score":11,"backend_utilization_score":12,"customer_ramp_score":11,"qualification_shipment_score":9,"margin_mix_score":8,"cash_conversion_score":6,"relative_strength_score":13,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"customer_capacity_score":16,"HBM_memory_exposure_score":14,"backend_utilization_score":15,"customer_ramp_score":14,"qualification_shipment_score":11,"margin_mix_score":10,"cash_conversion_score":8,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Capacity/ramp bridge plus high early MFE supports Yellow/Green-candidate watch; exact source-grade evidence and late drawdown block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L90_033170_SIGNETICS_OSAT_PACKAGING_THEME","trigger_id":"R2L90_C06_033170_20240222_STAGE2_FALSE_POSITIVE_OSAT_PACKAGING_THEME","symbol":"033170","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_scope":"current_default_proxy","profile_hypothesis":"OSAT packaging theme without HBM customer capacity and margin bridge should be blocked","raw_component_scores_before":{"customer_capacity_score":2,"HBM_memory_exposure_score":3,"backend_utilization_score":1,"customer_ramp_score":0,"qualification_shipment_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_capacity_score":0,"HBM_memory_exposure_score":1,"backend_utilization_score":0,"customer_ramp_score":0,"qualification_shipment_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-Yellow MFE and deep MAE convert OSAT packaging theme into missing customer-capacity bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L90_394280_OPENEDGE_AI_IP_BLOWOFF","trigger_id":"R2L90_C06_394280_20240222_STAGE2_FALSE_POSITIVE_AI_IP_BLOWOFF","symbol":"394280","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_scope":"current_default_proxy","profile_hypothesis":"AI semiconductor IP blowoff without memory customer capacity should remain 4B-watch even with local MFE","raw_component_scores_before":{"customer_capacity_score":0,"HBM_memory_exposure_score":1,"backend_utilization_score":0,"customer_ramp_score":0,"qualification_shipment_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":13,"valuation_repricing_score":5,"execution_risk_score":-18,"theme_spike_risk":-22,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_capacity_score":0,"HBM_memory_exposure_score":0,"backend_utilization_score":0,"customer_ramp_score":0,"qualification_shipment_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-26,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Local MFE is price-only; deep MAE and missing customer-capacity bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L90_C06_P0_CURRENT","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C06 needs explicit customer capacity, utilization, qualification/shipment, margin/cash and AI-IP/OSAT price-only taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":21.09,"avg_MAE90_pct":-26.35,"avg_MFE180_pct":21.09,"avg_MAE180_pct":-64.26,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C06_customer_capacity_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L90_C06_P1_SECTOR_SPECIFIC","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_id":"P1_L2_HBM_customer_capacity_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 HBM/memory-capacity signals need memory customer capex, capacity ramp, backend utilization, qualification/shipment, margin or cash conversion before Stage2-Actionable","changed_axes":["customer_capacity_required","utilization_shipment_required","AI_IP_OSAT_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_capacity_utilization_ramp_shipment_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":21.09,"avg_MAE90_pct":-26.35,"avg_MFE180_pct":21.09,"avg_MAE180_pct":-64.26,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L90_C06_P2_CANONICAL","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_id":"P2_C06_customer_capacity_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C06 should reward customer-capacity-to-shipment mechanics, not AI-IP or OSAT theme labels","changed_axes":["C06_customer_capacity_margin_cash_bridge_required","C06_AI_IP_OSAT_theme_local_4B_guard","C06_price_only_MFE_not_capacity_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_capacity_or_utilization_plus_shipment_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":21.09,"avg_MAE90_pct":-26.35,"avg_MFE180_pct":21.09,"avg_MAE180_pct":-64.26,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L90_C06_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_id":"P3_C06_price_only_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If customer-capacity bridge is missing, MFE90<20 or MAE90<=-20 should block Yellow/Green; MFE cannot validate capacity when MAE180<=-50","changed_axes":["C06_price_only_MFE_guardrail","C06_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_MAE90_le_minus_20); price_only_MFE_invalid_if_MAE180_le_minus_50"},"eligible_trigger_count":3,"avg_MFE90_pct":21.09,"avg_MAE90_pct":-26.35,"avg_MFE180_pct":21.09,"avg_MAE180_pct":-64.26,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_MEMORY_BACKEND_POSITIVE_VS_OSAT_AI_IP_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":21.09,"avg_MAE90_pct":-26.35,"avg_MFE180_pct":21.09,"avg_MAE180_pct":-64.26,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"price_only_MFE_counterexample_count":2,"interpretation":"C06 needs bridge discipline. SFA반도체 shows memory/backend customer-capacity bridge can support Yellow/Green-candidate-watch, while 시그네틱스 and 오픈엣지테크놀로지 show OSAT/AI-IP theme MFE should not be promoted without customer capacity, utilization, qualification/shipment, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"036540","trigger_type":"Stage2-Actionable-MemoryBackendCustomerCapacityBridge-Positive","entry_date":"2024-01-18","stage2_to_90D_outcome":"good_stage2_high_MFE_low_early_MAE","stage2_to_180D_outcome":"positive_capacity_bridge_but_late_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when customer capacity, backend utilization, qualification/shipment and margin bridge exists; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"033170","trigger_type":"Stage2-FalsePositive-OSATPackagingThemeNoHBMCustomerCapacityBridge","entry_date":"2024-02-22","stage2_to_90D_outcome":"bad_stage2_sub_Yellow_MFE_deep_MAE","stage2_to_180D_outcome":"failed_OSAT_packaging_theme_extreme_MAE","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"OSAT packaging theme without HBM customer-capacity and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"394280","trigger_type":"Stage2-FalsePositive-AISemiconductorIPBlowoffNoMemoryCustomerCapacityBridge","entry_date":"2024-02-22","stage2_to_90D_outcome":"price_only_local_MFE_deep_MAE","stage2_to_180D_outcome":"failed_AI_IP_blowoff_extreme_MAE","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"AI semiconductor IP blowoff without memory customer-capacity bridge should be treated as 4B-watch, not positive C06 evidence."}
{"row_type":"residual_contribution","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","residual_type":"OSAT_AI_IP_theme_overcredit_without_HBM_memory_customer_capacity_bridge","contribution":"Adds two C06 4B counterexamples against one backend/customer-capacity positive, avoiding C06 top-covered and recent R2 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"MEMORY_BACKEND_CAPACITY_CUSTOMER_BRIDGE_VS_OSAT_AI_IP_PRICE_ONLY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C06 now has non-top-symbol backend/customer-capacity positive and two OSAT/AI-IP weak-bridge counterexamples; next R2 C06 loops should exact-URL repair customer capex, HBM exposure, utilization, qualification/shipment acceptance, margin mix and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","axis":"C06_customer_capacity_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"036540 worked when backend/customer-capacity proxy existed; 033170 and 394280 failed when OSAT/AI-IP price action lacked customer capacity, utilization, shipment and margin bridge."}
{"row_type":"shadow_weight","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","axis":"C06_AI_IP_OSAT_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"OSAT packaging and AI-IP rows showed sub-20 MFE90 and severe MAE when non-price customer-capacity evidence was missing."}
{"row_type":"shadow_weight","round":"R2","loop":"90","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","axis":"C06_price_only_MFE_not_capacity_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"394280 and 033170 show local MFE should not validate C06 unless HBM/memory customer capacity and shipment/margin evidence are repaired."}
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
  - AI_semiconductor_IP_overcredit
  - OSAT_packaging_theme_overcredit
  - customer_capacity_bridge_missing
  - qualification_shipment_margin_cash_bridge_missing
new_axis_proposed:
  - C06_customer_capacity_margin_cash_bridge_required_shadow_only
  - C06_AI_IP_OSAT_theme_local_4B_watch_guard_shadow_only
  - C06_price_only_MFE_not_capacity_validation_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C06
  - full_4b_requires_non_price_evidence within C06
  - hard_4c_thesis_break_routes_to_4c within C06
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
`036540` has historical corporate-action candidate dates long before 2024, but the selected 2024 forward window is usable for price-path calibration.  
The non-price evidence layer remains source-name/proxy level for all three rows.

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
3. Confirm R2 / L2 / C06 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C06 top-covered symbols
   - previous R2 loop85 C06 symbols
   - previous R2 loop86 C07 symbols
   - previous R2 loop87 C08 symbols
   - previous R2 loop88 C09 symbols
   - previous R2 loop89 C10 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C06-scoped safe patch candidates:
   - C06_customer_capacity_margin_cash_bridge_required
   - C06_AI_IP_OSAT_theme_local_4B_watch_guard
   - C06_price_only_MFE_not_capacity_validation_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 90
next_round = R3
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.
```
