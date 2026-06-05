# E2R Stock-Web v12 Residual Research — R2 Loop 91 / L2 / C07

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 91
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_DEPOSITION_EQUIPMENT_ORDER_RAMP_BRIDGE_VS_TESTER_POSTPROCESS_EQUIPMENT_THEME_DECAY
sector: AI / semiconductor / HBM equipment / deposition equipment / test equipment / back-end equipment / customer order ramp
output_file: e2r_stock_web_v12_residual_round_R2_loop_91_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R1 loop 91`.

```text
scheduled_round = R2
scheduled_loop = 91
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

R2 is restricted to AI / semiconductor / electronics.  
C07 is selected because R2 loop90 used C06, and the R2 rotation returns to HBM equipment order / relative-strength evidence.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
rows = 11
symbols = 9
good/bad Stage2 = 7/0
4B/4C = 1/0
top-covered = 042700, 064760, 003160, 036200, 036540, 039440
```

This loop avoids the top-covered list and recent R2 loop symbols:

```text
R2 loop85 C06: 000660, 005930, 009150
R2 loop86 C07: 042700, 064760, 003160
R2 loop87 C08: 232140, 425420, 098120
R2 loop88 C09: 039030, 412350, 253590
R2 loop89 C10: 403870, 166090, 074600
R2 loop90 C06: 036540, 033170, 394280
```

Selected symbols:

```text
084370, 086390, 217190
```

The selected pocket is:

```text
HBM / advanced-memory deposition equipment order-ramp bridge
vs
memory tester relative-strength spike without confirmed HBM customer order and conversion bridge
vs
back-end / HBM post-process equipment rebound without durable order backlog and margin bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"084370","company_name":"유진테크","profile_path":"atlas/symbol_profiles/084/084370.json","first_date":"2006-01-17","last_date":"2026-02-20","trading_day_count":4955,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2007-05-17","2010-01-22","2012-06-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 forward window. Market flag changes from KOSDAQ GLOBAL to KOSDAQ in June 2024; keep market-segment-change watch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; market_segment_change_watch"}
{"row_type":"price_source_validation","symbol":"086390","company_name":"유니테스트","profile_path":"atlas/symbol_profiles/086/086390.json","first_date":"2006-12-05","last_date":"2026-02-20","trading_day_count":4725,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2007-04-30","2007-05-28","2010-09-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"217190","company_name":"제너셈","profile_path":"atlas/symbol_profiles/217/217190.json","first_date":"2015-09-25","last_date":"2026-02-20","trading_day_count":2550,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2015-11-10","2015-12-07","2025-11-24","2025-12-17"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical 2015 candidates and future 2025 candidates exist outside selected 2024 calibration window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; 2025_candidates_outside_window"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"084370","trigger_type":"Stage2-Actionable-HBMDepositionEquipmentOrderRampBridge-Positive","entry_date":"2024-02-22","duplicate_status":"new C07 symbol/trigger/date combination outside C07 top-covered and previous R2 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"086390","trigger_type":"Stage2-FalsePositive-MemoryTesterThemePriceMFE-NoHBMCustomerOrderBridge","entry_date":"2024-03-08","duplicate_status":"new C07 symbol/trigger/date combination outside C07 top-covered and previous R2 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"217190","trigger_type":"Stage2-FalsePositive-BackendHBMPostprocessEquipmentRebound-NoDurableOrderMarginBridge","entry_date":"2024-01-24","duplicate_status":"new C07 symbol/trigger/date combination outside C07 top-covered and previous R2 loop symbols"}
```

## 4. Research question

C07 is not “반도체 장비주가 강하다.”  
The useful HBM equipment signal must prove a bridge from relative strength to actual order economics:

```text
HBM / advanced-memory tool exposure
customer order or purchase-order visibility
tool qualification or acceptance
delivery schedule
capacity expansion tie-in
backlog conversion
margin mix
working-capital discipline
cash conversion
```

A tool-theme spike without this bridge is a chamber warmed up with no wafer lot scheduled. The lamp is on, but the order book has not fed the tool.

Residual question:

```text
Can C07 distinguish:
1. HBM/deposition equipment order-ramp bridge with strong MFE and controlled early MAE,
2. memory tester relative-strength spike where local MFE is price-only without customer/order conversion evidence,
3. back-end / post-process HBM equipment rebound where no durable order, backlog and margin bridge exists?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C07_R2L91_084370_EUGENE_TECH_HBM_DEPOSITION_ORDER_RAMP","symbol":"084370","company_name":"유진테크","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_DEPOSITION_EQUIPMENT_ORDER_RAMP_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-HBMDepositionEquipmentOrderRampBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"score_price_alignment":"positive_high_MFE90_controlled_MAE_market_segment_watch","current_profile_verdict":"current_profile_correct_if_HBM_customer_order_delivery_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"HBM/deposition-equipment order-ramp proxy produced high MFE90 with shallow early MAE. Green remains strict because exact customer/order, delivery and margin evidence is required, and 2024 market-segment-change watch is retained."}
{"row_type":"case","case_id":"C07_R2L91_086390_UNITEST_MEMORY_TESTER_THEME","symbol":"086390","company_name":"유니테스트","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"MEMORY_TESTER_THEME_PRICE_MFE_WITHOUT_HBM_CUSTOMER_ORDER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-MemoryTesterThemePriceMFE-NoHBMCustomerOrderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_only_MFE_deep_MAE_no_order_bridge","current_profile_verdict":"current_profile_false_positive_if_memory_tester_MFE_overcredited","price_source":"Songdaiki/stock-web","notes":"Memory tester / equipment relative strength had MFE above 20%, but later deep drawdown shows that price-only MFE should not validate C07 without customer order, qualification and margin bridge."}
{"row_type":"case","case_id":"C07_R2L91_217190_GENESSEM_BACKEND_HBM_POSTPROCESS","symbol":"217190","company_name":"제너셈","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"BACKEND_HBM_POSTPROCESS_EQUIPMENT_REBOUND_WITHOUT_DURABLE_ORDER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-BackendHBMPostprocessEquipmentRebound-NoDurableOrderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_extreme_MAE_no_backlog_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_backend_equipment_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Back-end / HBM post-process equipment rebound had low forward MFE and extreme later MAE without durable order backlog, delivery schedule, margin or cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 084370 유진테크 — HBM/deposition equipment order-ramp bridge

Entry row: `2024-02-22 c=37500`.  
Observed path: early low `2024-02-27 l=36100`, peak `2024-05-28 h=60000`, and late-year low `2024-12-20 l=30300`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L91_C07_084370_20240222_STAGE2_HBM_DEPOSITION_EQUIPMENT_ORDER_RAMP","case_id":"C07_R2L91_084370_EUGENE_TECH_HBM_DEPOSITION_ORDER_RAMP","symbol":"084370","company_name":"유진테크","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_DEPOSITION_EQUIPMENT_ORDER_RAMP_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-HBMDepositionEquipmentOrderRampBridge-Positive","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":37500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_HBM_deposition_equipment_order_ramp_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; HBM/deposition equipment order ramp, customer demand and delivery schedule treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["HBM_equipment_exposure_proxy","customer_order_ramp_proxy","tool_delivery_schedule_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_order_source_pending","tool_qualification_acceptance_pending","delivery_schedule_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","market_segment_change_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","profile_path":"atlas/symbol_profiles/084/084370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.67,"MFE_90D_pct":60.00,"MFE_180D_pct":60.00,"MAE_30D_pct":-3.73,"MAE_90D_pct":-3.73,"MAE_180D_pct":-19.20,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":60000.0,"max_drawdown_low_date":"2024-12-20","max_drawdown_low":30300.0,"drawdown_after_peak_pct":-49.50,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.58,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_customer_order_tool_acceptance_delivery_margin_evidence","four_b_evidence_type":["price_extension_watch","market_segment_change_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_controlled_MAE_market_segment_watch","current_profile_verdict":"current_profile_correct_if_HBM_customer_order_delivery_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_segment_change_watch_KOSDAQ_GLOBAL_to_KOSDAQ_after_entry"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"084370_2024-02-22_37500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"do_not_count_as_new_case":false,"current_profile_residual":"C07 can allow Stage2/Yellow when equipment strength is tied to HBM/customer order, tool qualification or delivery, margin and cash bridge. Green still requires exact source-grade evidence."}
```

### 6.2 086390 유니테스트 — memory tester theme with price-only MFE

Entry row: `2024-03-08 c=15420`.  
Observed path: local high `2024-05-23 h=19500`, then late-year low `2024-12-09 l=7470`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L91_C07_086390_20240308_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_THEME","case_id":"C07_R2L91_086390_UNITEST_MEMORY_TESTER_THEME","symbol":"086390","company_name":"유니테스트","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"MEMORY_TESTER_THEME_PRICE_MFE_WITHOUT_HBM_CUSTOMER_ORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_only_MFE_stress_test","trigger_type":"Stage2-FalsePositive-MemoryTesterThemePriceMFE-NoHBMCustomerOrderBridge","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":15420.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_memory_tester_HBM_equipment_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; memory tester / HBM equipment theme treated as insufficient without confirmed customer PO, tool acceptance, delivery schedule and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["memory_tester_theme","relative_strength_spike","HBM_keyword"],"stage3_evidence_fields":["confirmed_customer_order_missing","tool_qualification_acceptance_missing","delivery_schedule_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_MFE","order_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086390/2024.csv","profile_path":"atlas/symbol_profiles/086/086390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.65,"MFE_90D_pct":26.46,"MFE_180D_pct":26.46,"MAE_30D_pct":-9.86,"MAE_90D_pct":-13.36,"MAE_180D_pct":-51.56,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-23","peak_price":19500.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":7470.0,"drawdown_after_peak_pct":-61.69,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.76,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_tester_theme_MFE_without_customer_order_tool_acceptance_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only_MFE","order_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_only_MFE_deep_MAE_no_order_bridge","current_profile_verdict":"current_profile_false_positive_if_memory_tester_MFE_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"086390_2024-03-08_15420","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C07 should not count memory tester MFE as HBM equipment order evidence unless customer order, tool acceptance, delivery and margin/cash bridge are exact-repaired. Deep 180D MAE forces 4B-watch."}
```

### 6.3 217190 제너셈 — back-end / HBM post-process equipment rebound without durable order-margin bridge

Entry row: `2024-01-24 c=15800`.  
Observed path: high `2024-03-14 h=18450`, then decline to `2024-12-09 l=5930`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L91_C07_217190_20240124_STAGE2_FALSE_POSITIVE_BACKEND_HBM_POSTPROCESS","case_id":"C07_R2L91_217190_GENESSEM_BACKEND_HBM_POSTPROCESS","symbol":"217190","company_name":"제너셈","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"BACKEND_HBM_POSTPROCESS_EQUIPMENT_REBOUND_WITHOUT_DURABLE_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-BackendHBMPostprocessEquipmentRebound-NoDurableOrderMarginBridge","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":15800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_backend_HBM_postprocess_equipment_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; back-end/HBM post-process equipment rebound treated as insufficient without durable customer order, backlog, delivery and margin/cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["backend_equipment_theme","HBM_postprocess_keyword","relative_strength_rebound"],"stage3_evidence_fields":["durable_customer_order_missing","backlog_conversion_missing","delivery_schedule_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE_watch","backlog_margin_bridge_missing_watch","extreme_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/217/217190/2024.csv","profile_path":"atlas/symbol_profiles/217/217190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.16,"MFE_90D_pct":16.77,"MFE_180D_pct":16.77,"MAE_30D_pct":-23.92,"MAE_90D_pct":-23.92,"MAE_180D_pct":-62.47,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-14","peak_price":18450.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":5930.0,"drawdown_after_peak_pct":-67.86,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.19,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"backend_HBM_postprocess_rebound_without_durable_order_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","backlog_margin_bridge_missing_watch","extreme_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE_no_backlog_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_backend_equipment_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"2024_window_clean; 2025_candidates_outside_window","same_entry_group_id":"217190_2024-01-24_15800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C07 should not promote back-end equipment rebound without durable order backlog, delivery, margin and cash evidence. Low MFE and extreme MAE require Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_R2L91_084370_EUGENE_TECH_HBM_DEPOSITION_ORDER_RAMP","trigger_id":"R2L91_C07_084370_20240222_STAGE2_HBM_DEPOSITION_EQUIPMENT_ORDER_RAMP","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C07 requires HBM equipment exposure, customer order visibility, tool qualification or delivery schedule, margin and cash bridge rather than equipment relative strength alone","raw_component_scores_before":{"HBM_equipment_exposure_score":13,"customer_order_visibility_score":12,"tool_qualification_score":10,"delivery_schedule_score":11,"backlog_conversion_score":10,"margin_mix_score":9,"cash_conversion_score":7,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"HBM_equipment_exposure_score":16,"customer_order_visibility_score":15,"tool_qualification_score":13,"delivery_schedule_score":14,"backlog_conversion_score":12,"margin_mix_score":11,"cash_conversion_score":9,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"HBM/deposition equipment order-ramp bridge plus high MFE90 supports Yellow/Green-candidate watch; exact customer-order and tool-acceptance evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_R2L91_086390_UNITEST_MEMORY_TESTER_THEME","trigger_id":"R2L91_C07_086390_20240308_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_THEME","symbol":"086390","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_scope":"current_default_proxy","profile_hypothesis":"memory tester relative-strength MFE without customer order bridge should be blocked","raw_component_scores_before":{"HBM_equipment_exposure_score":3,"customer_order_visibility_score":0,"tool_qualification_score":1,"delivery_schedule_score":0,"backlog_conversion_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":13,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"HBM_equipment_exposure_score":1,"customer_order_visibility_score":0,"tool_qualification_score":0,"delivery_schedule_score":0,"backlog_conversion_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"MFE is price-only; deep MAE and missing customer-order/qualification bridge block Yellow/Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_R2L91_217190_GENESSEM_BACKEND_HBM_POSTPROCESS","trigger_id":"R2L91_C07_217190_20240124_STAGE2_FALSE_POSITIVE_BACKEND_HBM_POSTPROCESS","symbol":"217190","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_scope":"current_default_proxy","profile_hypothesis":"back-end HBM equipment rebound without durable backlog and margin bridge should remain Watch/4B","raw_component_scores_before":{"HBM_equipment_exposure_score":2,"customer_order_visibility_score":0,"tool_qualification_score":0,"delivery_schedule_score":0,"backlog_conversion_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":5,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"HBM_equipment_exposure_score":1,"customer_order_visibility_score":0,"tool_qualification_score":0,"delivery_schedule_score":0,"backlog_conversion_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-28,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and extreme MAE convert back-end equipment rebound into missing backlog/margin bridge failure."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L91_C07_P0_CURRENT","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C07 needs explicit HBM customer order, tool qualification, delivery schedule, backlog conversion, margin/cash and price-only tester/post-process taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":34.41,"avg_MAE90_pct":-13.67,"avg_MFE180_pct":34.41,"avg_MAE180_pct":-44.41,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.51,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C07_customer_order_delivery_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L91_C07_P1_SECTOR_SPECIFIC","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P1_L2_HBM_equipment_order_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 HBM equipment signals need customer order visibility, tool qualification, delivery schedule, backlog conversion, margin or cash before Stage2-Actionable","changed_axes":["HBM_order_required","tool_qualification_delivery_required","tester_postprocess_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_order_tool_qualification_delivery_backlog_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":34.41,"avg_MAE90_pct":-13.67,"avg_MFE180_pct":34.41,"avg_MAE180_pct":-44.41,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L91_C07_P2_CANONICAL","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P2_C07_customer_order_delivery_margin_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C07 should reward order-to-delivery mechanics, not tester/post-process equipment price labels","changed_axes":["C07_customer_order_tool_delivery_margin_bridge_required","C07_memory_tester_backend_theme_local_4B_guard","C07_price_only_MFE_not_order_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_order_or_tool_qualification_plus_delivery_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":34.41,"avg_MAE90_pct":-13.67,"avg_MFE180_pct":34.41,"avg_MAE180_pct":-44.41,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L91_C07_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P3_C07_deep_MAE_price_only_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If order/delivery bridge is missing, MFE can only be credited after exact non-price evidence; MAE180<=-50 hard-routes to 4B-watch","changed_axes":["C07_price_only_MFE_guardrail","C07_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_MAE180_le_minus_50); high_MFE_without_bridge_not_positive"},"eligible_trigger_count":3,"avg_MFE90_pct":34.41,"avg_MAE90_pct":-13.67,"avg_MFE180_pct":34.41,"avg_MAE180_pct":-44.41,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_DEPOSITION_POSITIVE_VS_TESTER_BACKEND_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":34.41,"avg_MAE90_pct":-13.67,"avg_MFE180_pct":34.41,"avg_MAE180_pct":-44.41,"stage2_hit_rate_MFE90_ge20":0.67,"price_only_MFE_counterexample_count":1,"stage2_bad_entry_rate_bridge_missing":0.67,"interpretation":"C07 needs bridge discipline. 유진테크 shows HBM/deposition equipment order-ramp bridge can support Yellow/Green-candidate-watch, while 유니테스트 and 제너셈 show memory tester/back-end equipment theme strength should not be promoted without confirmed customer order, tool qualification, delivery schedule, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"084370","trigger_type":"Stage2-Actionable-HBMDepositionEquipmentOrderRampBridge-Positive","entry_date":"2024-02-22","stage2_to_90D_outcome":"good_stage2_high_MFE_controlled_MAE","stage2_to_180D_outcome":"positive_HBM_equipment_order_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when equipment strength is tied to HBM customer order, qualification, delivery and margin/cash bridge; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"086390","trigger_type":"Stage2-FalsePositive-MemoryTesterThemePriceMFE-NoHBMCustomerOrderBridge","entry_date":"2024-03-08","stage2_to_90D_outcome":"price_only_MFE_without_order_bridge","stage2_to_180D_outcome":"failed_memory_tester_theme_deep_MAE","MFE90_ge20":true,"MAE180_le_minus50":true,"transition_note":"Memory tester MFE without customer order/qualification bridge should be treated as 4B-watch, not positive C07 evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"217190","trigger_type":"Stage2-FalsePositive-BackendHBMPostprocessEquipmentRebound-NoDurableOrderMarginBridge","entry_date":"2024-01-24","stage2_to_90D_outcome":"weak_stage2_low_MFE_extreme_MAE","stage2_to_180D_outcome":"failed_backend_HBM_postprocess_rebound_extreme_MAE","MFE90_ge20":false,"MAE180_le_minus50":true,"transition_note":"Back-end equipment rebound without durable order backlog and margin bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","residual_type":"memory_tester_backend_equipment_theme_overcredit_without_customer_order_delivery_margin_bridge","contribution":"Adds two C07 4B counterexamples against one HBM/deposition equipment order-ramp positive, avoiding C07 top-covered and previous R2 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_DEPOSITION_EQUIPMENT_ORDER_RAMP_BRIDGE_VS_TESTER_POSTPROCESS_EQUIPMENT_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C07 now has non-top-symbol HBM/deposition equipment order-ramp positive and two tester/back-end weak-bridge counterexamples; next R2 C07 loops should exact-URL repair customer order, tool qualification, delivery schedule, backlog conversion, margin mix and cash evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_customer_order_tool_delivery_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"084370 worked when HBM equipment/order-ramp proxy existed; 086390 and 217190 failed when tester/back-end equipment price action lacked customer order, qualification, delivery and margin bridge."}
{"row_type":"shadow_weight","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_memory_tester_backend_theme_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Memory tester and back-end equipment rows showed either price-only MFE with deep MAE or low MFE with extreme MAE when non-price order evidence was missing."}
{"row_type":"shadow_weight","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_price_only_MFE_not_order_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"086390 shows MFE90 above 20 should not count as C07 positive evidence when customer-order/qualification bridge is missing and MAE180 is deep."}
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
  - memory_tester_theme_overcredit
  - backend_HBM_postprocess_theme_overcredit
  - customer_order_bridge_missing
  - tool_qualification_delivery_margin_bridge_missing
new_axis_proposed:
  - C07_customer_order_tool_delivery_margin_bridge_required_shadow_only
  - C07_memory_tester_backend_theme_local_4B_guard_shadow_only
  - C07_price_only_MFE_not_order_validation_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C07
  - full_4b_requires_non_price_evidence within C07
  - hard_4c_thesis_break_routes_to_4c within C07
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

All selected triggers use Stock-Web tradable raw OHLC rows.  
`084370` has no selected-window corporate-action contamination, but the market flag changes from KOSDAQ GLOBAL to KOSDAQ after entry, so the row keeps `market_segment_change_watch`.  
`086390` and `217190` have historical or future corporate-action candidates outside the selected 2024 windows.  
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
market_segment_change_watch = true for 084370
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
3. Confirm R2 / L2 / C07 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C07 top-covered symbols
   - previous R2 loop85 C06 symbols
   - previous R2 loop86 C07 symbols
   - previous R2 loop87 C08 symbols
   - previous R2 loop88 C09 symbols
   - previous R2 loop89 C10 symbols
   - previous R2 loop90 C06 symbols
6. Keep 084370 in market-segment-change watch before patch consideration.
7. If aggregate support remains stable after exact evidence URL repair, consider C07-scoped safe patch candidates:
   - C07_customer_order_tool_delivery_margin_bridge_required
   - C07_memory_tester_backend_theme_local_4B_guard
   - C07_price_only_MFE_not_order_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 91
next_round = R3
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.
```
