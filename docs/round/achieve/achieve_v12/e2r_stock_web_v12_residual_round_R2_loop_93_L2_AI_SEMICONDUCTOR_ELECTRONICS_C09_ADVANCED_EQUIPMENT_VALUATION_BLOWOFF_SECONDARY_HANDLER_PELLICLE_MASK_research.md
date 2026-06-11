# E2R Stock-Web v12 Residual Research — R2 Loop 93 / L2 / C09 Secondary

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 93
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: HBM_TEST_HANDLER_EUV_PELLICLE_MASK_ADVANCED_EQUIPMENT_BLOWOFF_VS_ORDER_MARGIN_BRIDGE_DECAY
sector: AI / semiconductor / HBM handler / EUV pellicle / mask blank / advanced equipment / valuation blowoff / order bridge / margin bridge
output_file: e2r_stock_web_v12_residual_round_R2_loop_93_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_SECONDARY_HANDLER_PELLICLE_MASK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This is the corrected valid output for the current execution.

```text
selected_round = R2
selected_loop = 93
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

A stale C08 filename was touched during this execution path. It must not be treated as the valid output for this request. The valid artifact is this secondary C09 MD.

Reason for selection:

```text
v12 scheduler = coverage_index_first
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
selected_archetype_drives_round = true
```

After local loop93 additions, C09 remains one of the thinnest semiconductor Priority-0 archetypes. This run avoids prior C09 and adjacent R2 loop symbols.

```text
Avoided C09 prior symbols:
R2 loop88 C09: 039030, 412350, 253590
R2 loop93 C09: 036930, 322310, 140860

Avoided adjacent recent R2 symbols:
C08: 232140, 425420, 098120, 092870, 080580, 237750, 058470, 095340, 131290
C07: 042700, 064760, 003160, 084370, 086390, 217190, 031980, 110990, 067310
C06/C10 local loop93: 402340, 195870, 222800, 281820, 036200, 101160
```

Selected symbols:

```text
089030, 036810, 101490
```

The selected pocket:

```text
HBM test handler order/revision bridge positive-control
vs
EUV pellicle / chiller / advanced-equipment price-MFE blowoff without durable order-margin bridge
vs
mask-blank / EUV material-equipment vocabulary after a spike without order/revision/margin bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"089030","company_name":"테크윙","profile_path":"atlas/symbol_profiles/089/089030.json","first_date":"2011-11-10","last_date":"2026-02-20","trading_day_count":3509,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2011-12-13","2011-12-29","2022-08-01","2022-08-23"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
{"row_type":"price_source_validation","symbol":"036810","company_name":"에프에스티","profile_path":"atlas/symbol_profiles/036/036810.json","first_date":"2000-01-18","last_date":"2026-02-20","trading_day_count":6430,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2000-05-02","2004-06-17"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
{"row_type":"price_source_validation","symbol":"101490","company_name":"에스앤에스텍","profile_path":"atlas/symbol_profiles/101/101490.json","first_date":"2009-04-14","last_date":"2026-02-20","trading_day_count":4155,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2009-04-30"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
```

## 3. Novelty check

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"089030","trigger_type":"Stage2-Actionable-HBMTestHandlerOrderRevisionBridge-PositiveWatch","entry_date":"2024-02-22","duplicate_status":"new C09 symbol/trigger/date combination outside prior C09 loops"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"036810","trigger_type":"Stage2-FalsePositive-EUVPellicleAdvancedEquipmentPriceMFENoDurableOrderMarginBridge","entry_date":"2024-04-09","duplicate_status":"new C09 symbol/trigger/date combination outside prior C09 loops"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"101490","trigger_type":"Stage2-FalsePositive-MaskBlankEUVVocabularyNoOrderRevisionMarginBridge","entry_date":"2024-02-28","duplicate_status":"new C09 symbol/trigger/date combination outside prior C09 loops"}
```

## 4. Research question

C09 is not “advanced equipment가 올랐다.”
The useful guard must ask whether the price move is backed by order, delivery, acceptance, revision, margin and cash.

```text
advanced equipment / EUV / HBM vocabulary
customer qualification or process relevance
signed order / shipment / delivery acceptance
revenue revision visibility
ASP or mix quality
gross-margin / operating-margin bridge
working-capital discipline
cash conversion
valuation discipline after first blowoff
```

A clean-room tool can hum loudly without moving a wafer. The signal is not the hum; the signal is accepted throughput, revised revenue, margin and cash.

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C09_R2L93B_089030_TECHWING_HBM_HANDLER_ORDER","symbol":"089030","company_name":"테크윙","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_TEST_HANDLER_ORDER_REVISION_DELIVERY_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-HBMTestHandlerOrderRevisionBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_extreme_MFE90_controlled_entry_MAE_but_late_blowoff_drawdown","current_profile_verdict":"current_profile_correct_if_order_delivery_revision_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"HBM handler / advanced-equipment order-revision proxy produced extreme MFE. It remains Green-candidate-watch, not automatic Green, because exact order/revision/margin evidence and blowoff drawdown review are required."}
{"row_type":"case","case_id":"C09_R2L93B_036810_FST_EUV_PRICE_MFE_DECAY","symbol":"036810","company_name":"에프에스티","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"EUV_PELLICLE_CHILLER_PRICE_MFE_WITHOUT_DURABLE_ORDER_MARGIN_BRIDGE","case_type":"failed_entry_price_MFE_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-EUVPellicleAdvancedEquipmentPriceMFENoDurableOrderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_MFE_but_extreme_late_MAE_without_durable_order_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_EUV_price_MFE_overcredited","price_source":"Songdaiki/stock-web","notes":"EUV/pellicle/chiller vocabulary produced price-MFE, but the later collapse shows that price-MFE should not validate C09 without durable order, delivery, revision, margin and cash evidence."}
{"row_type":"case","case_id":"C09_R2L93B_101490_SNS_MASKBLANK_DECAY","symbol":"101490","company_name":"에스앤에스텍","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"MASKBLANK_EUV_VOCABULARY_WITHOUT_ORDER_REVISION_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-MaskBlankEUVVocabularyNoOrderRevisionMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_late_MAE_no_order_revision_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_maskblank_EUV_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Mask blank / EUV vocabulary after a spike had limited forward MFE and later drawdown without customer order, revision, margin or cash bridge."}
```

## 6. Trigger-level Stock-Web rows

```jsonl
{"row_type":"trigger","trigger_id":"R2L93B_C09_089030_20240222_STAGE2_HBM_HANDLER_ORDER","case_id":"C09_R2L93B_089030_TECHWING_HBM_HANDLER_ORDER","symbol":"089030","company_name":"테크윙","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_TEST_HANDLER_ORDER_REVISION_DELIVERY_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-HBMTestHandlerOrderRevisionBridge-PositiveWatch","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":22300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_HBM_test_handler_order_revision_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; HBM handler order/revision/margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["HBM_handler_equipment_proxy","customer_order_proxy","revision_visibility_proxy","relative_strength_after_reset"],"stage3_evidence_fields":["exact_customer_order_source_pending","delivery_acceptance_source_pending","revenue_revision_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["extreme_MFE_watch","late_blowoff_drawdown_watch","Green_exact_evidence_watch"],"stage4c_evidence_fields":["order_cut_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":69.73,"MFE_90D_pct":204.48,"MFE_180D_pct":217.49,"MAE_30D_pct":-10.40,"MAE_90D_pct":-10.40,"MAE_180D_pct":-10.40,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800.0,"max_drawdown_low_date":"2024-12-11","max_drawdown_low":28250.0,"drawdown_after_peak_pct":-60.10,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.22,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_order_delivery_revision_margin_cash_evidence_and_blowoff_drawdown_review","four_b_evidence_type":["extreme_MFE_watch","late_blowoff_drawdown_watch","Green_exact_evidence_watch"],"four_c_protection_label":"order_cut_watch_only","trigger_outcome_label":"positive_extreme_MFE90_controlled_entry_MAE_but_late_blowoff_drawdown","current_profile_verdict":"current_profile_correct_if_order_delivery_revision_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"089030_2024-02-22_22300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C09 should allow Green-candidate-watch only when advanced-equipment strength is tied to exact order/revision/margin bridge; extreme price does not remove Green strictness."}
{"row_type":"trigger","trigger_id":"R2L93B_C09_036810_20240409_STAGE2_FALSE_POSITIVE_EUV_PRICE_MFE","case_id":"C09_R2L93B_036810_FST_EUV_PRICE_MFE_DECAY","symbol":"036810","company_name":"에프에스티","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"EUV_PELLICLE_CHILLER_PRICE_MFE_WITHOUT_DURABLE_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_MFE_not_order_validation","trigger_type":"Stage2-FalsePositive-EUVPellicleAdvancedEquipmentPriceMFENoDurableOrderMarginBridge","trigger_date":"2024-04-09","entry_date":"2024-04-09","entry_price":27900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_EUV_pellicle_advanced_equipment_price_MFE_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; EUV/pellicle/chiller vocabulary and price-MFE treated as insufficient without durable customer order, delivery, revision and margin bridge","evidence_source_type":"historical_public_theme_report_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["EUV_pellicle_keyword","advanced_equipment_price_MFE","theme_relative_strength"],"stage3_evidence_fields":["durable_customer_order_missing","delivery_acceptance_missing","revision_visibility_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_MFE_without_bridge","extreme_late_MAE","order_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036810/2024.csv","profile_path":"atlas/symbol_profiles/036/036810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":37.63,"MFE_90D_pct":50.00,"MFE_180D_pct":50.00,"MAE_30D_pct":-4.66,"MAE_90D_pct":-4.66,"MAE_180D_pct":-49.14,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":41850.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":14190.0,"drawdown_after_peak_pct":-66.09,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.75,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_MFE_without_durable_order_delivery_revision_margin_cash_bridge_should_remain_4B_watch_not_positive","four_b_evidence_type":["price_MFE_without_bridge","extreme_late_MAE","order_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MFE_but_extreme_late_MAE_without_durable_order_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_EUV_price_MFE_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"036810_2024-04-09_27900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C09 should not allow price-MFE to substitute for durable order/revision/margin evidence. This is a price-MFE false positive row."}
{"row_type":"trigger","trigger_id":"R2L93B_C09_101490_20240228_STAGE2_FALSE_POSITIVE_MASKBLANK_DECAY","case_id":"C09_R2L93B_101490_SNS_MASKBLANK_DECAY","symbol":"101490","company_name":"에스앤에스텍","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"MASKBLANK_EUV_VOCABULARY_WITHOUT_ORDER_REVISION_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-MaskBlankEUVVocabularyNoOrderRevisionMarginBridge","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":44650.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_maskblank_EUV_vocabulary_price_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; mask blank / EUV vocabulary treated as insufficient without customer order, revenue revision, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["maskblank_EUV_keyword","advanced_process_vocabulary","price_spike"],"stage3_evidence_fields":["customer_order_missing","revision_visibility_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE","late_MAE","order_revision_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/101/101490/2024.csv","profile_path":"atlas/symbol_profiles/101/101490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.64,"MFE_90D_pct":11.31,"MFE_180D_pct":11.31,"MAE_30D_pct":-7.50,"MAE_90D_pct":-7.50,"MAE_180D_pct":-21.50,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":49400.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":35050.0,"drawdown_after_peak_pct":-29.05,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"maskblank_EUV_vocabulary_without_customer_order_revision_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","late_MAE","order_revision_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_late_MAE_no_order_revision_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_maskblank_EUV_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"101490_2024-02-28_44650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C09 should keep mask-blank/EUV vocabulary in Watch/4B unless exact customer order, revision, margin and cash evidence are repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L93B_089030_TECHWING_HBM_HANDLER_ORDER","trigger_id":"R2L93B_C09_089030_20240222_STAGE2_HBM_HANDLER_ORDER","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_scope":"current_default_proxy","profile_hypothesis":"C09 should reward HBM equipment order/revision bridge but keep Green strict after valuation blowoff","raw_component_scores_before":{"advanced_equipment_theme_score":12,"customer_order_score":12,"delivery_acceptance_score":10,"revision_visibility_score":11,"ASP_mix_score":9,"margin_bridge_score":9,"cash_conversion_score":7,"relative_strength_score":16,"valuation_heat_score":8,"execution_risk_score":-5,"theme_spike_risk":-3,"information_confidence":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"advanced_equipment_theme_score":15,"customer_order_score":15,"delivery_acceptance_score":12,"revision_visibility_score":14,"ASP_mix_score":11,"margin_bridge_score":11,"cash_conversion_score":9,"relative_strength_score":17,"valuation_heat_score":10,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Order/revision bridge plus extreme MFE supports Green-candidate watch; exact evidence and blowoff drawdown review block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L93B_036810_FST_EUV_PRICE_MFE_DECAY","trigger_id":"R2L93B_C09_036810_20240409_STAGE2_FALSE_POSITIVE_EUV_PRICE_MFE","symbol":"036810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_scope":"current_default_proxy","profile_hypothesis":"EUV/pellicle price-MFE without order/revision and margin bridge should be blocked","raw_component_scores_before":{"advanced_equipment_theme_score":6,"customer_order_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":1,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":10,"valuation_heat_score":14,"execution_risk_score":-18,"theme_spike_risk":-22,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"advanced_equipment_theme_score":2,"customer_order_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_heat_score":18,"execution_risk_score":-30,"theme_spike_risk":-26,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Price-MFE followed by extreme late MAE confirms that price path alone cannot validate missing order/revision evidence."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L93B_101490_SNS_MASKBLANK_DECAY","trigger_id":"R2L93B_C09_101490_20240228_STAGE2_FALSE_POSITIVE_MASKBLANK_DECAY","symbol":"101490","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_scope":"current_default_proxy","profile_hypothesis":"maskblank/EUV vocabulary without customer order and margin bridge should remain Watch/4B","raw_component_scores_before":{"advanced_equipment_theme_score":4,"customer_order_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":4,"valuation_heat_score":10,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"advanced_equipment_theme_score":1,"customer_order_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_heat_score":14,"execution_risk_score":-20,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and late MAE require exact customer order, revision and margin evidence before promotion."}
```

## 8. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_HBM_HANDLER_POSITIVE_VS_EUV_MASKBLANK_PRICE_MFE_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":88.60,"avg_MAE90_pct":-7.52,"avg_MFE180_pct":92.93,"avg_MAE180_pct":-27.01,"price_MFE_without_bridge_counterexample_count":1,"stage2_hit_rate_MFE90_ge20":0.67,"interpretation":"C09 needs order/revision discipline. 테크윙 shows HBM handler order/revision bridge can support Green-candidate-watch, while 에프에스티 and 에스앤에스텍 show EUV/pellicle/mask vocabulary or price-MFE should not be promoted without durable customer order, delivery, revision, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"089030","trigger_type":"Stage2-Actionable-HBMTestHandlerOrderRevisionBridge-PositiveWatch","entry_date":"2024-02-22","stage2_to_90D_outcome":"positive_extreme_MFE90_controlled_MAE","stage2_to_180D_outcome":"HBM_handler_order_bridge_but_blowoff_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/Green-candidate only when HBM equipment strength is tied to customer order, delivery, revision, margin and cash bridge."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"036810","trigger_type":"Stage2-FalsePositive-EUVPellicleAdvancedEquipmentPriceMFENoDurableOrderMarginBridge","entry_date":"2024-04-09","stage2_to_90D_outcome":"price_MFE_without_bridge","stage2_to_180D_outcome":"failed_EUV_price_MFE_extreme_MAE_no_order_margin_bridge","MFE90_ge20":true,"MAE180_le_minus25":true,"transition_note":"EUV/pellicle price-MFE without durable order/revision and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"101490","trigger_type":"Stage2-FalsePositive-MaskBlankEUVVocabularyNoOrderRevisionMarginBridge","entry_date":"2024-02-28","stage2_to_90D_outcome":"bad_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_maskblank_EUV_vocabulary_no_order_revision_margin_bridge","MFE90_ge20":false,"MAE180_le_minus20":true,"transition_note":"Mask-blank/EUV vocabulary without order/revision/margin bridge should remain Watch/4B."}
{"row_type":"coverage_matrix","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_TEST_HANDLER_EUV_PELLICLE_MASK_ADVANCED_EQUIPMENT_BLOWOFF_VS_ORDER_MARGIN_BRIDGE_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C09 now has a second non-overlapping loop93 pocket: HBM handler positive-watch plus EUV/pellicle/mask weak-bridge price-MFE counterexamples."}
```

## 9. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_order_delivery_revision_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"089030 worked when HBM handler order/revision proxy existed; 036810 and 101490 failed or collapsed when durable order/revision/margin evidence was missing."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_price_MFE_not_order_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"036810 shows high price-MFE can still become a false positive when order/revision/margin bridge is missing and late MAE expands."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_EUV_mask_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"101490 shows EUV/mask vocabulary alone had low MFE and no durable order/revision bridge."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_blowoff_drawdown_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"089030 had extreme MFE but large after-peak drawdown; Green requires exact non-price evidence."}
```

## 10. Residual Contribution Summary

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
  - advanced_equipment_price_MFE_overcredit
  - EUV_pellicle_mask_vocabulary_overcredit
  - durable_customer_order_revision_bridge_missing
  - margin_cash_bridge_missing
  - blowoff_drawdown_Green_strict_watch
new_axis_proposed:
  - C09_order_delivery_revision_margin_cash_bridge_required_shadow_only
  - C09_price_MFE_not_order_validation_guard_shadow_only
  - C09_EUV_mask_vocabulary_local_4B_guard_shadow_only
  - C09_blowoff_drawdown_Green_strict_guard_shadow_only
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

## 11. Data-quality caveat

All selected triggers use Stock-Web tradable raw OHLC rows.
`089030`, `036810`, and `101490` have only historical corporate-action candidates before selected 2024 windows.
All three selected 2024 windows are usable for residual price-path analysis.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for residual price-path analysis
evidence_url_pending = true
source_proxy_only = true
promotion should prefer hold / exact evidence repair until exact URLs are added
```

## 12. Deferred Coding Agent Handoff Prompt

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
5. Confirm stale C08 duplicate touched during this execution is not ingested as the valid output.
6. Confirm this loop avoided prior C09 loop88 and loop93 symbols.
7. Confirm recently touched C08/C28/C23/C17/C13/C12 rows are not ingested from this MD.
8. Treat 089030 as Green-candidate-watch only, not Green, until exact order/revision/margin/cash evidence is repaired.
9. Treat 036810 and 101490 as weak-bridge failure modes unless exact customer order/revision/margin/cash evidence is added later.
10. If aggregate support remains stable after exact evidence URL repair, consider C09-scoped safe patch candidates:
   - C09_order_delivery_revision_margin_cash_bridge_required
   - C09_price_MFE_not_order_validation_guard
   - C09_EUV_mask_vocabulary_local_4B_guard
   - C09_blowoff_drawdown_Green_strict_guard
11. Do not loosen Stage3-Green.
12. Do not use future MFE/MAE in runtime scoring.
13. Use this MD only for calibration profile planning.
```

## 13. Round state

```text
completed_round = R2
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C01 or C08 depending on reconciled local-loop count and fatigue controls
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 14. Final one-line contribution

```text
This corrected loop adds 3 new independent C09 cases, 1 HBM handler order/revision positive-watch, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.
```
