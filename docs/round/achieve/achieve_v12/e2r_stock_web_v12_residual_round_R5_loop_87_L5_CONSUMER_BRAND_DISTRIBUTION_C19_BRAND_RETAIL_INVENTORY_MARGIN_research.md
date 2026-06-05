# E2R Stock-Web v12 Residual Research — R5 Loop 87 / L5 / C19

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R5
loop: 87
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: RETAIL_VALUEUP_INVENTORY_MARGIN_BRIDGE_VS_DUTYFREE_FASHION_INVENTORY_THEME_DECAY
sector: consumer / brand / retail / inventory / margin bridge
output_file: e2r_stock_web_v12_residual_round_R5_loop_87_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R4 loop 87`.

```text
scheduled_round = R5
scheduled_loop = 87
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
```

R5 is restricted to consumer / brand / distribution.  
C19 is selected because recent R5 loops already used C18 export-channel reorder and C20 beauty/global distribution, while C19 remains the inventory/margin retail bucket.

The No-Repeat Index shows C19 as:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN
rows = 38
symbols = 13
good/bad Stage2 = 8/9
4B/4C = 3/0
top-covered = 282330, 004170, 007070, 093050, 337930, 139480
```

This loop avoids the top-covered list and also avoids the immediately previous R5 symbols:

```text
R5 loop85 C20: 018290, 051900, 090430
R5 loop86 C18: 003230, 005610, 007310
```

Selected symbols:

```text
069960, 008770, 031430
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"069960","company_name":"현대백화점","profile_path":"atlas/symbol_profiles/069/069960.json","first_date":"2002-11-25","last_date":"2026-02-20","trading_day_count":5735,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"008770","company_name":"호텔신라","profile_path":"atlas/symbol_profiles/008/008770.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7764,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["1999-01-20","1999-07-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"031430","company_name":"신세계인터내셔날","profile_path":"atlas/symbol_profiles/031/031430.json","first_date":"2011-07-14","last_date":"2026-02-20","trading_day_count":3587,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2022-04-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"069960","trigger_type":"Stage2-Actionable-RetailInventoryMarginValueupBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C19 symbol/trigger/date combination outside top-covered and previous R5 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"008770","trigger_type":"Stage2-FalsePositive-DutyfreeRetailRebound-NoInventoryMarginBridge","entry_date":"2024-04-01","duplicate_status":"new C19 symbol/trigger/date combination outside top-covered and previous R5 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"031430","trigger_type":"Stage2-FalsePositive-FashionBrandInventoryRebound-NoMarginBridge","entry_date":"2024-04-01","duplicate_status":"new C19 symbol/trigger/date combination outside top-covered and previous R5 loop symbols"}
```

## 4. Research question

C19 is not “retail stock rebounded.”  
A retail or brand signal must show sell-through, inventory normalization, markdown control, channel mix, gross-margin bridge, operating leverage, and cash conversion. Otherwise price is only a shop-window display: bright glass, no checkout line.

Residual question:

```text
Can C19 distinguish:
1. retailer value-up / inventory-margin bridge with usable rerating and shallow-to-moderate MAE,
2. duty-free retail rebound that fails when traffic, inventory and margin bridge do not confirm,
3. fashion-brand rebound that decays when inventory, markdown, sell-through and gross-margin bridge remain weak?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C19_R5L87_069960_HYUNDAI_RETAIL_INVENTORY_MARGIN","symbol":"069960","company_name":"현대백화점","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"RETAIL_VALUEUP_INVENTORY_MARGIN_BRIDGE","case_type":"watch_positive_control","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-RetailInventoryMarginValueupBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge20_moderate_MAE_then_later_fade","current_profile_verdict":"current_profile_correct_if_inventory_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Retail/value-up/inventory-margin proxy generated a 20%+ MFE with tolerable early MAE. Later fade keeps this as Yellow-watch rather than Green."}
{"row_type":"case","case_id":"C19_R5L87_008770_SHILLA_DUTYFREE_NO_MARGIN_BRIDGE","symbol":"008770","company_name":"호텔신라","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DUTYFREE_RETAIL_REBOUND_WITHOUT_INVENTORY_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DutyfreeRetailRebound-NoInventoryMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_dutyfree_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Duty-free/retail rebound had near-zero MFE and deep MAE when traffic, inventory, markdown and gross-margin bridge failed to confirm."}
{"row_type":"case","case_id":"C19_R5L87_031430_SI_FASHION_INVENTORY_NO_MARGIN","symbol":"031430","company_name":"신세계인터내셔날","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"FASHION_BRAND_INVENTORY_REBOUND_WITHOUT_GROSS_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-FashionBrandInventoryRebound-NoMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_brand_inventory_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Fashion-brand rebound had tiny MFE and later deep MAE without sell-through, markdown control and gross-margin bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 069960 현대백화점 — retail value-up / inventory-margin bridge positive control

Entry row: `2024-01-29 c=51200`.  
Observed path: same-day low `47400`, high `2024-02-07 h=61900`, then later lows into autumn.

```jsonl
{"row_type":"trigger","trigger_id":"R5L87_C19_069960_20240129_STAGE2_RETAIL_INVENTORY_MARGIN","case_id":"C19_R5L87_069960_HYUNDAI_RETAIL_INVENTORY_MARGIN","symbol":"069960","company_name":"현대백화점","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"RETAIL_VALUEUP_INVENTORY_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-RetailInventoryMarginValueupBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":51200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_retail_inventory_margin_valueup_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; retail inventory normalization, margin and value-up bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["retail_valueup_proxy","inventory_normalization_proxy","gross_margin_bridge_proxy","relative_strength_turn"],"stage3_evidence_fields":["same_store_sales_pending","markdown_control_pending","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","late_fade_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/069/069960/2024.csv","profile_path":"atlas/symbol_profiles/069/069960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.90,"MFE_90D_pct":20.90,"MFE_180D_pct":20.90,"MAE_30D_pct":-7.42,"MAE_90D_pct":-7.42,"MAE_180D_pct":-10.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-07","peak_price":61900.0,"max_drawdown_low_date":"2024-10-16","max_drawdown_low":45750.0,"drawdown_after_peak_pct":-26.09,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_full_4B_without_non_price_slowdown; later fade blocks Green","four_b_evidence_type":["price_only","late_fade_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge20_moderate_MAE_then_later_fade","current_profile_verdict":"current_profile_correct_if_inventory_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"069960_2024-01-29_51200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C19 can allow Stage2/Yellow when retail strength is tied to inventory normalization, markdown control and margin bridge. Green still requires exact sell-through/margin/cash evidence."}
```

### 6.2 008770 호텔신라 — duty-free retail rebound without inventory/margin bridge

Entry row: `2024-04-01 c=62900`.  
Observed path: local high `2024-04-01~04-02 h=63000`, then lows `2024-07-17 l=46950`, `2024-11-13 l=36850`, and `2024-12-09 l=35900`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L87_C19_008770_20240401_STAGE2_FALSE_POSITIVE_DUTYFREE_RETAIL","case_id":"C19_R5L87_008770_SHILLA_DUTYFREE_NO_MARGIN_BRIDGE","symbol":"008770","company_name":"호텔신라","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DUTYFREE_RETAIL_REBOUND_WITHOUT_INVENTORY_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-DutyfreeRetailRebound-NoInventoryMarginBridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":62900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_dutyfree_retail_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; duty-free retail rebound treated as insufficient without traffic, inventory turnover, markdown control and gross-margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["dutyfree_rebound_theme","retail_traffic_recovery_proxy","relative_strength_rebound"],"stage3_evidence_fields":["inventory_turnover_bridge_missing","gross_margin_bridge_missing","markdown_control_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","inventory_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008770/2024.csv","profile_path":"atlas/symbol_profiles/008/008770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.16,"MFE_90D_pct":0.16,"MFE_180D_pct":0.16,"MAE_30D_pct":-5.56,"MAE_90D_pct":-25.36,"MAE_180D_pct":-42.93,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":63000.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":35900.0,"drawdown_after_peak_pct":-43.02,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"dutyfree_retail_rebound_without_inventory_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","inventory_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_dutyfree_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"008770_2024-04-01_62900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C19 should not upgrade duty-free retail rebound without inventory turnover, markdown control and gross-margin bridge. Near-zero MFE and deep MAE force Watch/4B-risk routing."}
```

### 6.3 031430 신세계인터내셔날 — fashion-brand inventory rebound without gross-margin bridge

Entry row: `2024-04-01 c=18270`.  
Observed path: same-day high `h=18360`, then lows `2024-11-14 l=10180` and `2024-12-09 l=9850`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L87_C19_031430_20240401_STAGE2_FALSE_POSITIVE_FASHION_BRAND","case_id":"C19_R5L87_031430_SI_FASHION_INVENTORY_NO_MARGIN","symbol":"031430","company_name":"신세계인터내셔날","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"FASHION_BRAND_INVENTORY_REBOUND_WITHOUT_GROSS_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-FashionBrandInventoryRebound-NoMarginBridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":18270.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_fashion_brand_inventory_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; fashion-brand inventory rebound treated as insufficient without sell-through, markdown control, channel mix and gross-margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["fashion_brand_rebound","inventory_reset_theme","relative_strength_rebound"],"stage3_evidence_fields":["sellthrough_bridge_missing","markdown_control_missing","gross_margin_bridge_missing","channel_mix_quality_missing"],"stage4b_evidence_fields":["price_only_local_peak","margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/031/031430/2024.csv","profile_path":"atlas/symbol_profiles/031/031430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.49,"MFE_90D_pct":0.49,"MFE_180D_pct":0.49,"MAE_30D_pct":-8.00,"MAE_90D_pct":-15.00,"MAE_180D_pct":-46.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":18360.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":9850.0,"drawdown_after_peak_pct":-46.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"fashion_brand_rebound_without_sellthrough_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_brand_inventory_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"031430_2024-04-01_18270","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C19 should not promote fashion-brand rebound without sell-through, markdown control, channel mix and gross-margin bridge. Tiny MFE and deep 180D MAE support Watch/4B-risk."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C19_R5L87_069960_HYUNDAI_RETAIL_INVENTORY_MARGIN","trigger_id":"R5L87_C19_069960_20240129_STAGE2_RETAIL_INVENTORY_MARGIN","symbol":"069960","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C19 requires inventory normalization and margin bridge rather than retail rebound alone","raw_component_scores_before":{"inventory_normalization_score":12,"sellthrough_quality_score":10,"gross_margin_bridge_score":11,"markdown_control_score":9,"channel_mix_score":8,"cash_conversion_score":6,"relative_strength_score":10,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":71,"stage_label_before":"Stage2-Watch/Yellow-candidate","raw_component_scores_after":{"inventory_normalization_score":15,"sellthrough_quality_score":12,"gross_margin_bridge_score":14,"markdown_control_score":11,"channel_mix_score":10,"cash_conversion_score":8,"relative_strength_score":11,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Inventory/margin bridge and MFE90>=20 support Yellow-watch; later fade and proxy-only evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C19_R5L87_008770_SHILLA_DUTYFREE_NO_MARGIN_BRIDGE","trigger_id":"R5L87_C19_008770_20240401_STAGE2_FALSE_POSITIVE_DUTYFREE_RETAIL","symbol":"008770","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_scope":"current_default_proxy","profile_hypothesis":"duty-free rebound without inventory and margin bridge should be blocked","raw_component_scores_before":{"inventory_normalization_score":3,"sellthrough_quality_score":2,"gross_margin_bridge_score":1,"markdown_control_score":1,"channel_mix_score":3,"cash_conversion_score":0,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"inventory_normalization_score":0,"sellthrough_quality_score":0,"gross_margin_bridge_score":0,"markdown_control_score":0,"channel_mix_score":1,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE convert duty-free rebound into missing inventory/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C19_R5L87_031430_SI_FASHION_INVENTORY_NO_MARGIN","trigger_id":"R5L87_C19_031430_20240401_STAGE2_FALSE_POSITIVE_FASHION_BRAND","symbol":"031430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_scope":"current_default_proxy","profile_hypothesis":"fashion-brand rebound without sell-through and gross-margin bridge should remain Watch/blocked","raw_component_scores_before":{"inventory_normalization_score":4,"sellthrough_quality_score":1,"gross_margin_bridge_score":1,"markdown_control_score":1,"channel_mix_score":2,"cash_conversion_score":0,"relative_strength_score":7,"valuation_repricing_score":3,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"inventory_normalization_score":1,"sellthrough_quality_score":0,"gross_margin_bridge_score":0,"markdown_control_score":0,"channel_mix_score":1,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-20,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Tiny MFE and deep 180D MAE require sell-through and gross-margin bridge before Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R5L87_C19_P0_CURRENT","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C19 needs explicit inventory, sell-through, markdown and gross-margin bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":7.18,"avg_MAE90_pct":-15.93,"avg_MFE180_pct":7.18,"avg_MAE180_pct":-33.22,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C19_inventory_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R5L87_C19_P1_SECTOR_SPECIFIC","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_id":"P1_L5_inventory_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L5 retail/brand signals need inventory normalization, sell-through, markdown control, channel mix, gross margin or cash bridge before Stage2-Actionable","changed_axes":["inventory_margin_bridge_required","sellthrough_markdown_required","retail_rebound_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_inventory_sellthrough_markdown_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":7.18,"avg_MAE90_pct":-15.93,"avg_MFE180_pct":7.18,"avg_MAE180_pct":-33.22,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R5L87_C19_P2_CANONICAL","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_id":"P2_C19_inventory_sellthrough_margin_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C19 should reward inventory-to-margin conversion, not retail/fashion/duty-free rebound themes","changed_axes":["C19_inventory_sellthrough_margin_bridge_required","C19_retail_theme_local_4B_guard","C19_low_MFE_no_bridge_guard"],"changed_thresholds":{"stage2_yellow_gate":"inventory_normalization_plus_margin_or_sellthrough_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":7.18,"avg_MAE90_pct":-15.93,"avg_MFE180_pct":7.18,"avg_MAE180_pct":-33.22,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R5L87_C19_P3_COUNTEREXAMPLE_GUARD","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_id":"P3_C19_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and MAE180<=-30 while inventory/margin bridge is missing, block Yellow/Green and route to 4B-watch","changed_axes":["C19_low_MFE_guardrail","C19_high_180D_MAE_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_MAE180_le_minus_30"},"eligible_trigger_count":3,"avg_MFE90_pct":7.18,"avg_MAE90_pct":-15.93,"avg_MFE180_pct":7.18,"avg_MAE180_pct":-33.22,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_RETAIL_VALUEUP_INVENTORY_MARGIN_VS_DUTYFREE_FASHION_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":7.18,"avg_MAE90_pct":-15.93,"avg_MFE180_pct":7.18,"avg_MAE180_pct":-33.22,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE180_le_minus_30":0.67,"interpretation":"C19 needs bridge discipline. 현대백화점 shows retail inventory/margin bridge can support Yellow-watch, while 호텔신라 and 신세계인터내셔날 show duty-free/fashion rebounds fail when sell-through, markdown control, inventory turnover and gross-margin evidence do not follow."}
{"row_type":"stage_transition_summary","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"069960","trigger_type":"Stage2-Actionable-RetailInventoryMarginValueupBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_MFE90_ge20_moderate_MAE","stage2_to_180D_outcome":"watch_positive_with_later_fade","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when inventory normalization and margin bridge exists; Green requires exact sell-through, markdown and cash evidence."}
{"row_type":"stage_transition_summary","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"008770","trigger_type":"Stage2-FalsePositive-DutyfreeRetailRebound-NoInventoryMarginBridge","entry_date":"2024-04-01","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_dutyfree_retail_rebound","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Duty-free retail rebound without inventory and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"031430","trigger_type":"Stage2-FalsePositive-FashionBrandInventoryRebound-NoMarginBridge","entry_date":"2024-04-01","stage2_to_90D_outcome":"weak_stage2_tiny_MFE","stage2_to_180D_outcome":"failed_fashion_brand_inventory_rebound_deep_MAE","MFE90_ge_20":false,"MAE180_le_minus_30":true,"transition_note":"Fashion-brand rebound without sell-through and margin bridge should remain Watch/blocked."}
{"row_type":"residual_contribution","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","residual_type":"retail_brand_rebound_overcredit_without_inventory_sellthrough_margin_bridge","contribution":"Adds two C19 local 4B/deep-MAE counterexamples against one retail inventory-margin positive control, avoiding C19 top-covered and previous R5 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"RETAIL_VALUEUP_INVENTORY_MARGIN_BRIDGE_VS_DUTYFREE_FASHION_INVENTORY_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C19 now has non-top-symbol duty-free/fashion counterexamples plus a retail inventory-margin watch-positive; next R5 loops should exact-URL repair inventory, sell-through, markdown, gross margin, channel mix and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_inventory_sellthrough_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"069960 worked when inventory/margin bridge proxy existed; 008770 and 031430 failed when retail/fashion rebound lacked sell-through, markdown and margin bridge."}
{"row_type":"shadow_weight","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_retail_rebound_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Duty-free and fashion-brand rebound rows had near-zero MFE and deep MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R5","loop":"87","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_low_MFE_high_180D_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<5 and MAE180<=-30 while inventory/margin bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - dutyfree_retail_rebound_overcredit
  - fashion_brand_inventory_theme_overcredit
  - sellthrough_bridge_missing
  - markdown_gross_margin_bridge_missing
new_axis_proposed:
  - C19_inventory_sellthrough_margin_bridge_required_shadow_only
  - C19_retail_rebound_theme_local_4B_watch_guard_shadow_only
  - C19_low_MFE_high_180D_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C19
  - full_4b_requires_non_price_evidence within C19
  - hard_4c_thesis_break_routes_to_4c within C19
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
3. Confirm R5 / L5 / C19 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C19 top-covered symbols
   - previous R5 loop85 C20 symbols
   - previous R5 loop86 C18 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C19-scoped safe patch candidates:
   - C19_inventory_sellthrough_margin_bridge_required
   - C19_retail_rebound_theme_local_4B_watch_guard
   - C19_low_MFE_high_180D_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R5
completed_loop = 87
next_round = R6
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.
```
