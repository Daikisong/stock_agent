# E2R Stock-Web v12 Residual Research — R2 Loop 85 / L2 / C06

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 85
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_CUSTOMER_CAPACITY_BRIDGE_VS_SEMI_BETA_MATERIAL_FOUNDRY_SPIKE
sector: AI / semiconductor / electronics / HBM memory customer capacity
output_file: e2r_stock_web_v12_residual_round_R2_loop_85_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after the completed `R1 loop 85` result.

```text
scheduled_round = R2
scheduled_loop = 85
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

R2 is restricted to AI / semiconductor / electronics.  
C06 is selected because the No-Repeat Index shows C06 is still thin: only 7 rows, 6 symbols, 4/1 good/bad Stage2, and no 4B/4C coverage. This run avoids the C06 top-covered list:

```text
000660, 005930, 009150, 014680, 067310, 402340
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"039030","company_name":"이오테크닉스","profile_path":"atlas/symbol_profiles/039/039030.json","first_date":"2000-08-24","last_date":"2026-02-20","trading_day_count":6285,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2003-02-03"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"000990","company_name":"DB하이텍","profile_path":"atlas/symbol_profiles/000/000990.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7763,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1997-04-01","1997-11-07","1999-06-11","2007-05-21"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"005290","company_name":"동진쎄미켐","profile_path":"atlas/symbol_profiles/005/005290.json","first_date":"1999-12-21","last_date":"2026-02-20","trading_day_count":6445,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2000-05-02"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"039030","trigger_type":"Stage2-Actionable-HBMCustomerCapacityLaserAnnealBridge-Positive","entry_date":"2024-02-28","duplicate_status":"new C06 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"000990","trigger_type":"Stage2-FalsePositive-FoundryMemoryBetaSpike-NoHBMCustomerBridge","entry_date":"2024-06-20","duplicate_status":"new C06 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"005290","trigger_type":"Stage2-FalsePositive-SemiMaterialBetaSpike-NoHBMCustomerCapacityBridge","entry_date":"2024-03-21","duplicate_status":"new C06 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C06 should not read every semiconductor recovery as HBM customer capacity. The real bridge is customer qualification, capacity allocation, shipment visibility, tool/process bottleneck, margin conversion, and revision quality.

Residual question:

```text
Can C06 distinguish:
1. HBM/customer-capacity equipment bridge with real MFE,
2. foundry/memory-beta spike with no HBM customer bridge,
3. semiconductor material beta spike with no customer-capacity conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C06_R2L85_039030_EOTECHNICS_HBM_CAPACITY_BRIDGE","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_LASER_ANNEAL_CUSTOMER_CAPACITY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-HBMCustomerCapacityLaserAnnealBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_customer_capacity_bridge_required","price_source":"Songdaiki/stock-web","notes":"HBM-adjacent laser/process bottleneck and customer-capacity proxy aligned with strong price follow-through."}
{"row_type":"case","case_id":"C06_R2L85_000990_DBHITEC_FOUNDRY_BETA_SPIKE","symbol":"000990","company_name":"DB하이텍","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"FOUNDRY_MEMORY_BETA_SPIKE_WITHOUT_HBM_CUSTOMER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-FoundryMemoryBetaSpike-NoHBMCustomerBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_after_blowoff_high_MAE","current_profile_verdict":"current_profile_false_positive_if_memory_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Foundry/memory beta spike lacked HBM customer-capacity bridge; entry near local blowoff produced high drawdown."}
{"row_type":"case","case_id":"C06_R2L85_005290_DONGJIN_MATERIAL_BETA_SPIKE","symbol":"005290","company_name":"동진쎄미켐","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"SEMI_MATERIAL_BETA_SPIKE_WITHOUT_HBM_CUSTOMER_CAPACITY_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SemiMaterialBetaSpike-NoHBMCustomerCapacityBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_material_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Semiconductor material beta rally had no direct customer-capacity bridge and faded after local spike."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 039030 이오테크닉스 — HBM/customer-capacity bridge positive

Entry row: `2024-02-28 c=202000`.  
Observed price path: high `2024-04-04 h=266000`, early low `2024-03-14 l=174400`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L85_C06_039030_20240228_STAGE2_HBM_CUSTOMER_CAPACITY_BRIDGE","case_id":"C06_R2L85_039030_EOTECHNICS_HBM_CAPACITY_BRIDGE","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_LASER_ANNEAL_CUSTOMER_CAPACITY_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-HBMCustomerCapacityLaserAnnealBridge-Positive","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":202000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_HBM_process_bottleneck_customer_capacity_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; HBM/customer-capacity bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["HBM_customer_capacity_proxy","process_bottleneck_proxy","relative_strength_turn"],"stage3_evidence_fields":["customer_qualification_bridge_pending","shipment_visibility_pending","margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv","profile_path":"atlas/symbol_profiles/039/039030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.68,"MFE_90D_pct":31.68,"MFE_180D_pct":31.68,"MAE_30D_pct":-13.66,"MAE_90D_pct":-13.66,"MAE_180D_pct":-13.66,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-04","peak_price":266000.0,"max_drawdown_low_date":"2024-03-14","max_drawdown_low":174400.0,"drawdown_after_peak_pct":-34.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_customer_capacity_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"039030_2024-02-28_202000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C06 should allow Stage2/Yellow when HBM process/customer-capacity bridge exists. Green still requires exact customer qualification, shipment and margin evidence."}
```

### 6.2 000990 DB하이텍 — foundry/memory beta spike without HBM customer bridge

Entry row: `2024-06-20 c=57100`.  
Observed price path: same-day high `58900`, then decline toward the 48k area within the 90D path and deeper risk later.

```jsonl
{"row_type":"trigger","trigger_id":"R2L85_C06_000990_20240620_STAGE2_FALSE_POSITIVE_FOUNDRY_MEMORY_BETA","case_id":"C06_R2L85_000990_DBHITEC_FOUNDRY_BETA_SPIKE","symbol":"000990","company_name":"DB하이텍","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"FOUNDRY_MEMORY_BETA_SPIKE_WITHOUT_HBM_CUSTOMER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-FoundryMemoryBetaSpike-NoHBMCustomerBridge","trigger_date":"2024-06-20","entry_date":"2024-06-20","entry_price":57100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_memory_foundry_beta_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; memory/foundry beta treated as insufficient without HBM customer capacity or qualification bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["memory_beta_spike","relative_strength_spike"],"stage3_evidence_fields":["HBM_customer_bridge_missing","capacity_allocation_missing","shipment_visibility_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000990/2024.csv","profile_path":"atlas/symbol_profiles/000/000990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.15,"MFE_90D_pct":3.15,"MFE_180D_pct":3.15,"MAE_30D_pct":-17.16,"MAE_90D_pct":-24.69,"MAE_180D_pct":-31.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-20","peak_price":58900.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":39300.0,"drawdown_after_peak_pct":-33.28,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_beta_peak_without_HBM_customer_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_after_blowoff_high_MAE","current_profile_verdict":"current_profile_false_positive_if_memory_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"000990_2024-06-20_57100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C06 should not treat foundry/memory beta as HBM customer capacity. Without customer qualification or capacity allocation bridge, local blowoff should remain 4B-watch."}
```

### 6.3 005290 동진쎄미켐 — semiconductor material beta spike without capacity bridge

Entry row: `2024-03-21 c=47950`.  
Observed price path: local high `2024-04-01 h=51500`, then materially weaker forward path after the spike.

```jsonl
{"row_type":"trigger","trigger_id":"R2L85_C06_005290_20240321_STAGE2_FALSE_POSITIVE_SEMI_MATERIAL_BETA","case_id":"C06_R2L85_005290_DONGJIN_MATERIAL_BETA_SPIKE","symbol":"005290","company_name":"동진쎄미켐","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"SEMI_MATERIAL_BETA_SPIKE_WITHOUT_HBM_CUSTOMER_CAPACITY_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-SemiMaterialBetaSpike-NoHBMCustomerCapacityBridge","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":47950.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_semiconductor_material_beta_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; semiconductor material beta treated as insufficient without HBM customer capacity, process allocation or shipment bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["semiconductor_material_beta","relative_strength_spike"],"stage3_evidence_fields":["HBM_customer_capacity_missing","process_allocation_missing","shipment_bridge_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005290/2024.csv","profile_path":"atlas/symbol_profiles/005/005290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.40,"MFE_90D_pct":7.40,"MFE_180D_pct":7.40,"MAE_30D_pct":-11.36,"MAE_90D_pct":-25.55,"MAE_180D_pct":-29.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":51500.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":33800.0,"drawdown_after_peak_pct":-34.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"material_beta_spike_without_customer_capacity_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_material_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"005290_2024-03-21_47950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Semiconductor material beta spike does not equal HBM customer capacity. C06 needs a customer/capacity/shipment bridge gate before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L85_039030_EOTECHNICS_HBM_CAPACITY_BRIDGE","trigger_id":"R2L85_C06_039030_20240228_STAGE2_HBM_CUSTOMER_CAPACITY_BRIDGE","symbol":"039030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C06 requires HBM customer/capacity bridge","raw_component_scores_before":{"HBM_customer_score":15,"capacity_allocation_score":13,"process_bottleneck_score":15,"shipment_visibility_score":9,"margin_bridge_score":8,"relative_strength_score":14,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"HBM_customer_score":18,"capacity_allocation_score":16,"process_bottleneck_score":17,"shipment_visibility_score":11,"margin_bridge_score":10,"relative_strength_score":15,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"HBM process/customer-capacity bridge supports Yellow-watch, while exact customer qualification and margin proof still block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L85_000990_DBHITEC_FOUNDRY_BETA_SPIKE","trigger_id":"R2L85_C06_000990_20240620_STAGE2_FALSE_POSITIVE_FOUNDRY_MEMORY_BETA","symbol":"000990","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_scope":"current_default_proxy","profile_hypothesis":"foundry/memory beta without HBM customer bridge should be blocked","raw_component_scores_before":{"HBM_customer_score":2,"capacity_allocation_score":2,"process_bottleneck_score":3,"shipment_visibility_score":2,"margin_bridge_score":2,"relative_strength_score":15,"valuation_repricing_score":7,"execution_risk_score":-10,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":30,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"HBM_customer_score":0,"capacity_allocation_score":0,"process_bottleneck_score":1,"shipment_visibility_score":0,"margin_bridge_score":0,"relative_strength_score":5,"valuation_repricing_score":3,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Local blowoff plus missing customer bridge and high MAE routes to 4B-watch."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L85_005290_DONGJIN_MATERIAL_BETA_SPIKE","trigger_id":"R2L85_C06_005290_20240321_STAGE2_FALSE_POSITIVE_SEMI_MATERIAL_BETA","symbol":"005290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_scope":"current_default_proxy","profile_hypothesis":"material beta without customer capacity bridge should remain Watch/blocked","raw_component_scores_before":{"HBM_customer_score":3,"capacity_allocation_score":2,"process_bottleneck_score":4,"shipment_visibility_score":2,"margin_bridge_score":2,"relative_strength_score":13,"valuation_repricing_score":7,"execution_risk_score":-9,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":35,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"HBM_customer_score":0,"capacity_allocation_score":0,"process_bottleneck_score":1,"shipment_visibility_score":0,"margin_bridge_score":0,"relative_strength_score":5,"valuation_repricing_score":3,"execution_risk_score":-15,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and high MAE convert material beta spike into evidence-quality failure."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L85_C06_P0_CURRENT","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C06 needs explicit customer/capacity/shipment bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":14.08,"avg_MAE90_pct":-21.30,"avg_MFE180_pct":14.08,"avg_MAE180_pct":-24.78,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C06_customer_capacity_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L85_C06_P1_SECTOR_SPECIFIC","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_id":"P1_L2_HBM_customer_capacity_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 HBM/memory signals need customer, capacity allocation, shipment or margin bridge before Stage2-Actionable","changed_axes":["customer_capacity_bridge_required","shipment_visibility_required","memory_beta_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_capacity_shipment_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":14.08,"avg_MAE90_pct":-21.30,"avg_MFE180_pct":14.08,"avg_MAE180_pct":-24.78,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L85_C06_P2_CANONICAL","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_id":"P2_C06_customer_capacity_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C06 should reward customer-capacity bridge, not broad semiconductor beta","changed_axes":["C06_HBM_customer_capacity_bridge_required","C06_memory_beta_spike_penalty","C06_material_foundry_beta_local_4B_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_capacity_or_shipment_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":14.08,"avg_MAE90_pct":-21.30,"avg_MFE180_pct":14.08,"avg_MAE180_pct":-24.78,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L85_C06_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_id":"P3_C06_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-20 while HBM customer bridge is missing, block Yellow/Green","changed_axes":["C06_high_MAE_guardrail","C06_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE90_pct":14.08,"avg_MAE90_pct":-21.30,"avg_MFE180_pct":14.08,"avg_MAE180_pct":-24.78,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_CUSTOMER_CAPACITY_VS_SEMI_BETA_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":14.08,"avg_MAE90_pct":-21.30,"avg_MFE180_pct":14.08,"avg_MAE180_pct":-24.78,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C06 needs bridge discipline. 039030 shows a valid HBM process/customer-capacity bridge, while 000990 and 005290 show broad semiconductor beta spikes that fail without customer/capacity/shipment evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"039030","trigger_type":"Stage2-Actionable-HBMCustomerCapacityLaserAnnealBridge-Positive","entry_date":"2024-02-28","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_capacity_bridge","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when HBM customer/capacity bridge exists; Green requires exact customer and margin evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"000990","trigger_type":"Stage2-FalsePositive-FoundryMemoryBetaSpike-NoHBMCustomerBridge","entry_date":"2024-06-20","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_entry_after_blowoff","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Foundry/memory beta without HBM customer bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"005290","trigger_type":"Stage2-FalsePositive-SemiMaterialBetaSpike-NoHBMCustomerCapacityBridge","entry_date":"2024-03-21","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_material_beta_spike","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Material beta spike without customer-capacity bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","residual_type":"HBM_customer_capacity_overcredit_when_only_semiconductor_beta_exists","contribution":"Adds two C06 local 4B/high-MAE counterexamples against one HBM customer-capacity bridge positive, avoiding C06 top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_CUSTOMER_CAPACITY_BRIDGE_VS_SEMI_BETA_MATERIAL_FOUNDRY_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C06 now has non-top-symbol semiconductor-beta counterexamples; next R2 loops should exact-URL repair customer qualification, capacity allocation, shipment and margin evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","axis":"C06_customer_capacity_shipment_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"039030 worked with HBM process/customer-capacity bridge proxy; 000990 and 005290 failed when only semiconductor beta existed."}
{"row_type":"shadow_weight","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","axis":"C06_memory_material_beta_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Foundry/material semiconductor beta spikes showed low MFE and high MAE without customer-capacity bridge."}
{"row_type":"shadow_weight","round":"R2","loop":"85","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","axis":"C06_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-20 while HBM customer/capacity bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - semiconductor_beta_overcredit
  - material_foundry_beta_no_HBM_customer_bridge
  - local_blowoff_without_capacity_allocation
new_axis_proposed:
  - C06_customer_capacity_shipment_bridge_required_shadow_only
  - C06_memory_material_beta_local_4B_watch_guard_shadow_only
  - C06_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C06
  - full_4b_requires_non_price_evidence within C06
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
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
3. Confirm R2 / L2 / C06 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C06 top-covered symbols.
6. If aggregate support remains stable after exact evidence URL repair, consider C06-scoped safe patch candidates:
   - C06_customer_capacity_shipment_bridge_required
   - C06_memory_material_beta_local_4B_watch_guard
   - C06_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 85
next_round = R3
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.
```
