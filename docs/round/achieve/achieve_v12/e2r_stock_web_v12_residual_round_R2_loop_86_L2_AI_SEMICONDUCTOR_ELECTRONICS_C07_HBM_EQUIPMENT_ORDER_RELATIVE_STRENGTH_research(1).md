# E2R Stock-Web v12 Residual Research — R2 Loop 86 / L2 / C07

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 86
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_EQUIPMENT_ORDER_ALD_BRIDGE_VS_MEMORY_EQUIPMENT_BETA_EXTENSION
sector: AI / semiconductor / electronics / HBM equipment / order-relative-strength
output_file: e2r_stock_web_v12_residual_round_R2_loop_86_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R1 loop 86`.

```text
scheduled_round = R2
scheduled_loop = 86
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

R2 is restricted to AI / semiconductor / electronics.  
C07 is selected because it remains thin on counterexamples:

```text
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
rows = 11
symbols = 9
good/bad Stage2 = 7/0
4B/4C = 1/0
top-covered = 042700, 064760, 003160, 036200, 036540, 039440
```

This loop avoids the top-covered set. It also avoids the recent R2 loop85 C06 names:

```text
039030, 000990, 005290
```

The research target is not broad semiconductor recovery. The target is the C07 split:

```text
Does HBM equipment relative strength have a real order/customer/capacity bridge,
or is it simply memory-equipment beta / late price extension without fresh bridge?
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"036930","company_name":"주성엔지니어링","profile_path":"atlas/symbol_profiles/036/036930.json","first_date":"1999-12-24","last_date":"2026-02-20","trading_day_count":6444,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2000-06-22"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"084370","company_name":"유진테크","profile_path":"atlas/symbol_profiles/084/084370.json","first_date":"2006-01-17","last_date":"2026-02-20","trading_day_count":4955,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2007-05-17","2010-01-22","2012-06-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here. Market category changed from KOSDAQ GLOBAL to KOSDAQ on 2024-06-14; this is not a corporate-action candidate.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"240810","company_name":"원익IPS","profile_path":"atlas/symbol_profiles/240/240810.json","first_date":"2016-05-02","last_date":"2026-02-20","trading_day_count":2405,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"036930","trigger_type":"Stage2-Actionable-HBMEquipmentALDOrderBridge-Positive","entry_date":"2024-02-26","duplicate_status":"new C07 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"084370","trigger_type":"Stage2-FalsePositive-HBMEquipmentLateExtension-NoFreshOrderBridge","entry_date":"2024-05-28","duplicate_status":"new C07 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"240810","trigger_type":"Stage2-FalsePositive-MemoryEquipmentBetaSpike-NoHBMOrderBridge","entry_date":"2024-07-04","duplicate_status":"new C07 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C07 is not “semiconductor equipment went up.” It is an HBM-equipment order relative-strength bucket.  
The real bridge is customer qualification, HBM-specific process bottleneck, capacity expansion, order visibility, delivery timing, margin conversion, and revision quality. If the price candle runs faster than that bridge, the signal becomes a late-cycle equipment beta trap.

Residual question:

```text
Can C07 distinguish:
1. HBM-adjacent ALD / process-equipment order bridge with usable MFE,
2. a good equipment name entered too late after price extension, without fresh order bridge,
3. broad memory equipment beta spike without HBM-specific order/customer evidence?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C07_R2L86_036930_JUSUNG_HBM_ALD_ORDER_BRIDGE","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_ALD_PROCESS_EQUIPMENT_ORDER_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-HBMEquipmentALDOrderBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_moderate_MFE_low_90D_MAE_later_drawdown","current_profile_verdict":"current_profile_correct_if_order_bridge_required","price_source":"Songdaiki/stock-web","notes":"HBM/process-equipment order bridge proxy produced a usable 90D MFE with controlled early MAE. Later 180D drawdown keeps Green strict."}
{"row_type":"case","case_id":"C07_R2L86_084370_EUGENE_LATE_EXTENSION_NO_FRESH_ORDER","symbol":"084370","company_name":"유진테크","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_EQUIPMENT_LATE_EXTENSION_WITHOUT_FRESH_ORDER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HBMEquipmentLateExtension-NoFreshOrderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE_after_late_extension","current_profile_verdict":"current_profile_false_positive_if_late_equipment_extension_overcredited","price_source":"Songdaiki/stock-web","notes":"Good equipment franchise, bad entry type: late extension had small MFE and deep MAE when fresh HBM order/margin bridge was not verified."}
{"row_type":"case","case_id":"C07_R2L86_240810_WONIKIPS_MEMORY_EQUIPMENT_BETA_SPIKE","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"MEMORY_EQUIPMENT_BETA_SPIKE_WITHOUT_HBM_ORDER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-MemoryEquipmentBetaSpike-NoHBMOrderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_memory_equipment_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Broad memory-equipment beta spike near July price extension gave almost no MFE and severe MAE without HBM-specific customer/order bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 036930 주성엔지니어링 — HBM/ALD process-equipment order bridge positive

Entry row: `2024-02-26 c=33800`.  
Observed path: near-term high `2024-02-28 h=40750`, later local high `2024-04-08 h≈41450`, and later drawdown to `2024-09-24 l=24800`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L86_C07_036930_20240226_STAGE2_HBM_ALD_ORDER_BRIDGE","case_id":"C07_R2L86_036930_JUSUNG_HBM_ALD_ORDER_BRIDGE","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_ALD_PROCESS_EQUIPMENT_ORDER_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-HBMEquipmentALDOrderBridge-Positive","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":33800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_HBM_ALD_process_equipment_order_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; HBM/process-equipment order bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["HBM_process_bottleneck_proxy","equipment_order_visibility_proxy","relative_strength_turn"],"stage3_evidence_fields":["customer_qualification_pending","shipment_timing_pending","margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv","profile_path":"atlas/symbol_profiles/036/036930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.63,"MFE_90D_pct":22.63,"MFE_180D_pct":22.63,"MAE_30D_pct":-1.04,"MAE_90D_pct":-6.80,"MAE_180D_pct":-26.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":41450.0,"max_drawdown_low_date":"2024-09-24","max_drawdown_low":24800.0,"drawdown_after_peak_pct":-40.17,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_moderate_MFE_low_90D_MAE_later_drawdown","current_profile_verdict":"current_profile_correct_if_order_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"036930_2024-02-26_33800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C07 should allow Stage2/Yellow when relative strength is tied to HBM process bottleneck and equipment order bridge. Green still requires exact customer, shipment and margin evidence."}
```

### 6.2 084370 유진테크 — HBM equipment late extension without fresh order bridge

Entry row: `2024-05-28 c=56500`.  
Observed path: same-day high `h=60000`, then decay to `2024-10-18 l=34250`, `2024-11-18 l=32700`, and `2024-12-20 l=30300`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L86_C07_084370_20240528_STAGE2_FALSE_POSITIVE_LATE_EQUIPMENT_EXTENSION","case_id":"C07_R2L86_084370_EUGENE_LATE_EXTENSION_NO_FRESH_ORDER","symbol":"084370","company_name":"유진테크","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_EQUIPMENT_LATE_EXTENSION_WITHOUT_FRESH_ORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-HBMEquipmentLateExtension-NoFreshOrderBridge","trigger_date":"2024-05-28","entry_date":"2024-05-28","entry_price":56500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_HBM_equipment_late_extension_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; equipment/HBM relative-strength extension treated as insufficient without fresh order, customer qualification and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["equipment_relative_strength_extension","HBM_theme_keyword"],"stage3_evidence_fields":["fresh_order_bridge_missing","customer_qualification_missing","shipment_timing_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","fresh_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","profile_path":"atlas/symbol_profiles/084/084370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.19,"MFE_90D_pct":6.19,"MFE_180D_pct":6.19,"MAE_30D_pct":-17.00,"MAE_90D_pct":-35.75,"MAE_180D_pct":-46.37,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":60000.0,"max_drawdown_low_date":"2024-12-20","max_drawdown_low":30300.0,"drawdown_after_peak_pct":-49.50,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_equipment_price_extension_without_fresh_order_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","fresh_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE_after_late_extension","current_profile_verdict":"current_profile_false_positive_if_late_equipment_extension_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; market_category_change_only_on_2024-06-14","same_entry_group_id":"084370_2024-05-28_56500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C07 should not treat late equipment relative strength as HBM order proof. Without fresh order/customer/margin bridge, local peak plus high MAE routes to Watch/4B-risk."}
```

### 6.3 240810 원익IPS — broad memory-equipment beta spike without HBM order bridge

Entry row: `2024-07-04 c=40100`.  
Observed path: same-day high `h=40300`, then lows around `2024-10-25 l=26950`, `2024-11-08 l=25200`, and `2024-12-09 l=21150`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L86_C07_240810_20240704_STAGE2_FALSE_POSITIVE_MEMORY_EQUIPMENT_BETA","case_id":"C07_R2L86_240810_WONIKIPS_MEMORY_EQUIPMENT_BETA_SPIKE","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"MEMORY_EQUIPMENT_BETA_SPIKE_WITHOUT_HBM_ORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-MemoryEquipmentBetaSpike-NoHBMOrderBridge","trigger_date":"2024-07-04","entry_date":"2024-07-04","entry_price":40100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_memory_equipment_beta_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; broad memory-equipment beta treated as insufficient without HBM-specific order/customer/capacity bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["memory_equipment_beta_spike","relative_strength_extension"],"stage3_evidence_fields":["HBM_specific_order_bridge_missing","customer_capacity_bridge_missing","shipment_visibility_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","HBM_order_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","profile_path":"atlas/symbol_profiles/240/240810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.50,"MFE_90D_pct":0.50,"MFE_180D_pct":0.50,"MAE_30D_pct":-23.57,"MAE_90D_pct":-37.16,"MAE_180D_pct":-47.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-04","peak_price":40300.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":21150.0,"drawdown_after_peak_pct":-47.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_equipment_beta_peak_without_HBM_order_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","HBM_order_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_memory_equipment_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"240810_2024-07-04_40100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C07 should separate HBM order relative strength from broad memory-equipment beta. This row shows price-only beta with near-zero MFE and deep MAE."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C07_R2L86_036930_JUSUNG_HBM_ALD_ORDER_BRIDGE","trigger_id":"R2L86_C07_036930_20240226_STAGE2_HBM_ALD_ORDER_BRIDGE","symbol":"036930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C07 requires HBM equipment order/customer bridge rather than equipment beta alone","raw_component_scores_before":{"HBM_equipment_order_score":14,"customer_qualification_score":10,"process_bottleneck_score":13,"shipment_visibility_score":8,"margin_bridge_score":7,"relative_strength_score":13,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-3,"information_confidence":5},"weighted_score_before":70,"stage_label_before":"Stage2-Watch/Yellow-candidate","raw_component_scores_after":{"HBM_equipment_order_score":17,"customer_qualification_score":12,"process_bottleneck_score":15,"shipment_visibility_score":10,"margin_bridge_score":9,"relative_strength_score":14,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":6},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"HBM/process equipment bridge and usable MFE support Yellow-watch; later drawdown and proxy evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C07_R2L86_084370_EUGENE_LATE_EXTENSION_NO_FRESH_ORDER","trigger_id":"R2L86_C07_084370_20240528_STAGE2_FALSE_POSITIVE_LATE_EQUIPMENT_EXTENSION","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_scope":"current_default_proxy","profile_hypothesis":"late equipment price extension without fresh bridge should be blocked","raw_component_scores_before":{"HBM_equipment_order_score":8,"customer_qualification_score":3,"process_bottleneck_score":6,"shipment_visibility_score":2,"margin_bridge_score":2,"relative_strength_score":14,"valuation_repricing_score":7,"execution_risk_score":-11,"theme_spike_risk":-13,"information_confidence":3},"weighted_score_before":31,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"HBM_equipment_order_score":3,"customer_qualification_score":0,"process_bottleneck_score":2,"shipment_visibility_score":0,"margin_bridge_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE convert late equipment extension into fresh-order bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C07_R2L86_240810_WONIKIPS_MEMORY_EQUIPMENT_BETA_SPIKE","trigger_id":"R2L86_C07_240810_20240704_STAGE2_FALSE_POSITIVE_MEMORY_EQUIPMENT_BETA","symbol":"240810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_scope":"current_default_proxy","profile_hypothesis":"broad memory equipment beta without HBM order bridge should remain Watch/blocked","raw_component_scores_before":{"HBM_equipment_order_score":4,"customer_qualification_score":1,"process_bottleneck_score":3,"shipment_visibility_score":1,"margin_bridge_score":1,"relative_strength_score":13,"valuation_repricing_score":6,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":18,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"HBM_equipment_order_score":0,"customer_qualification_score":0,"process_bottleneck_score":1,"shipment_visibility_score":0,"margin_bridge_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-20,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Near-zero MFE and deep MAE require HBM-specific order/customer evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L86_C07_P0_CURRENT","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C07 needs explicit HBM-specific order/customer/shipment bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":9.77,"avg_MAE90_pct":-26.57,"avg_MFE180_pct":9.77,"avg_MAE180_pct":-40.09,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C07_fresh_order_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L86_C07_P1_SECTOR_SPECIFIC","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P1_L2_HBM_equipment_order_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 HBM equipment signals need fresh order, customer qualification, process bottleneck, shipment or margin bridge before Stage2-Actionable","changed_axes":["fresh_order_bridge_required","customer_qualification_required","equipment_beta_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_fresh_order_customer_process_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":9.77,"avg_MAE90_pct":-26.57,"avg_MFE180_pct":9.77,"avg_MAE180_pct":-40.09,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L86_C07_P2_CANONICAL","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P2_C07_fresh_order_customer_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C07 should reward HBM equipment order bridge, not late equipment beta","changed_axes":["C07_fresh_order_customer_bridge_required","C07_late_extension_penalty","C07_memory_equipment_beta_local_4B_guard"],"changed_thresholds":{"stage2_yellow_gate":"fresh_HBM_order_or_customer_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":9.77,"avg_MAE90_pct":-26.57,"avg_MFE180_pct":9.77,"avg_MAE180_pct":-40.09,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L86_C07_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P3_C07_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-25 while HBM-specific order bridge is missing, block Yellow/Green","changed_axes":["C07_high_MAE_guardrail","C07_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":9.77,"avg_MAE90_pct":-26.57,"avg_MFE180_pct":9.77,"avg_MAE180_pct":-40.09,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_ORDER_BRIDGE_VS_EQUIPMENT_BETA_EXTENSION","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":9.77,"avg_MAE90_pct":-26.57,"avg_MFE180_pct":9.77,"avg_MAE180_pct":-40.09,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_25":0.67,"interpretation":"C07 needs bridge discipline. 주성엔지니어링 shows usable HBM/process-equipment bridge evidence, while 유진테크 and 원익IPS show late equipment beta extensions that fail without fresh order, customer qualification, shipment timing and margin bridge."}
{"row_type":"stage_transition_summary","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"036930","trigger_type":"Stage2-Actionable-HBMEquipmentALDOrderBridge-Positive","entry_date":"2024-02-26","stage2_to_90D_outcome":"good_stage2_moderate_MFE_low_MAE","stage2_to_180D_outcome":"watch_positive_with_later_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when HBM equipment order/customer bridge exists; Green requires exact customer, shipment and margin evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"084370","trigger_type":"Stage2-FalsePositive-HBMEquipmentLateExtension-NoFreshOrderBridge","entry_date":"2024-05-28","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_late_equipment_extension","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Late equipment extension without fresh order/customer/margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"240810","trigger_type":"Stage2-FalsePositive-MemoryEquipmentBetaSpike-NoHBMOrderBridge","entry_date":"2024-07-04","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_high_MAE","stage2_to_180D_outcome":"failed_memory_equipment_beta_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Broad memory-equipment beta without HBM-specific order bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","residual_type":"HBM_equipment_relative_strength_overcredit_when_only_late_equipment_beta_exists","contribution":"Adds two C07 local 4B/high-MAE counterexamples against one HBM/process-equipment order bridge positive, avoiding C07 top-covered and recent R2 C06 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_EQUIPMENT_ORDER_ALD_BRIDGE_VS_MEMORY_EQUIPMENT_BETA_EXTENSION","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C07 now has non-top-symbol bad Stage2 / late-extension rows; next R2 loops should exact-URL repair customer qualification, HBM order visibility, shipment timing and margin bridge evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_fresh_order_customer_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"036930 worked with HBM/process-equipment order bridge proxy; 084370 and 240810 failed when relative strength was only late equipment beta without fresh bridge."}
{"row_type":"shadow_weight","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_equipment_beta_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Late equipment beta extension showed low/near-zero MFE and high MAE without HBM-specific order/customer evidence."}
{"row_type":"shadow_weight","round":"R2","loop":"86","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-25 while fresh HBM order bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - HBM_equipment_late_extension_overcredit
  - memory_equipment_beta_no_HBM_order_bridge
  - customer_qualification_bridge_missing
  - low_MFE_high_MAE_without_fresh_order
new_axis_proposed:
  - C07_fresh_order_customer_bridge_required_shadow_only
  - C07_equipment_beta_local_4B_watch_guard_shadow_only
  - C07_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C07
  - full_4b_requires_non_price_evidence within C07
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
3. Confirm R2 / L2 / C07 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C07 top-covered symbols
   - recent R2 loop85 C06 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C07-scoped safe patch candidates:
   - C07_fresh_order_customer_bridge_required
   - C07_equipment_beta_local_4B_watch_guard
   - C07_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 86
next_round = R3
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.
```
