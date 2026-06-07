# E2R Stock-Web v12 Residual Research — R2 Loop 93 / L2 / C08 Tertiary

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 93
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TESTBOARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_VS_INSPECTION_PRICE_SPIKE_DECAY
sector: AI / semiconductor / test board / probe board / package inspection / customer qualification / repeat demand / margin / cash conversion
output_file: e2r_stock_web_v12_residual_round_R2_loop_93_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_TERTIARY_TESTBOARD_INSPECTION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 coverage-index-first scheduler.

```text
selected_round = R2
selected_loop = 93
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

Reason for selecting C08:

```text
v12 scheduler = coverage_index_first
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
selected_archetype_drives_round = true
```

No-Repeat Index Priority 0 snapshot:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY = 14 rows / need_to_30 = 16
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF = 15 rows
C01_ORDER_BACKLOG_MARGIN_BRIDGE = 16 rows
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH = 18 rows
```

C08 remains the thinnest raw Priority-0 archetype.
This run is a third non-overlapping C08 pocket and avoids all previously used C08 symbols.

Avoided C08 and adjacent recent R2 symbols:

```text
R2 loop87 C08: 232140, 425420, 098120
R2 loop92 C08: 092870, 080580, 237750
R2 loop93 C08 secondary: 058470, 095340, 131290
R2 loop93 C09: 036930, 322310, 140860, 089030, 036810, 101490
R2 loop93 C07/C06/C10: 031980, 110990, 067310, 402340, 195870, 222800, 281820, 036200, 101160
```

Selected symbols:

```text
219130, 064290, 420770
```

The selected pocket:

```text
test board / probe-board customer qualification and repeat-demand bridge positive-watch
vs
inspection-equipment customer-quality vocabulary with share-count movement and no durable margin bridge
vs
package-inspection theme spike with weak forward MFE and severe drawdown
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"219130","company_name":"타이거일렉","profile_path":"atlas/symbol_profiles/219/219130.json","first_date":"2015-09-25","last_date":"2026-02-20","trading_day_count":2550,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"064290","company_name":"인텍플러스","profile_path":"atlas/symbol_profiles/064/064290.json","first_date":"2011-01-05","last_date":"2026-02-20","trading_day_count":3719,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Profile has no corporate-action candidate, but visible share-count movement appears inside the 2024 row stream; keep share-count watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; share_count_movement_watch"}
{"row_type":"price_source_validation","symbol":"420770","company_name":"기가비스","profile_path":"atlas/symbol_profiles/420/420770.json","first_date":"2023-05-24","last_date":"2026-02-20","trading_day_count":667,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Recent listing relative to older corpus; selected 2024 window is clean but keep recent-listing/short-history watch before production patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window; recent_listing_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"219130","trigger_type":"Stage2-Actionable-TestBoardCustomerQualificationRepeatDemandBridge-PositiveWatch","entry_date":"2024-02-13","duplicate_status":"new C08 symbol/trigger/date combination outside prior C08 loops"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"064290","trigger_type":"Stage2-FalsePositive-InspectionEquipmentCustomerQualityVocabularyNoDurableMarginCashBridge","entry_date":"2024-02-20","duplicate_status":"new C08 symbol/trigger/date combination outside prior C08 loops; share-count movement watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"420770","trigger_type":"Stage2-FalsePositive-PackageInspectionThemeSpikeNoCustomerRepeatDemandBridge","entry_date":"2024-04-04","duplicate_status":"new C08 symbol/trigger/date combination outside prior C08 loops; recent-listing watch"}
```

## 4. Research question

C08 is not “검사장비/소켓/프로브 단어가 있다.”
The useful customer-quality signal must prove the process-to-repeat-demand chain:

```text
customer qualification or design-in
actual production process relevance
repeat consumable demand or recurring inspection demand
shipment / PO conversion
ASP / mix quality
gross-margin / operating-margin bridge
working-capital discipline
cash conversion
```

A probe board can flash on the chart, but that flash is not the signal. The signal is qualification passed, repeat order generated, ASP protected, margin retained, and cash collected.

Residual question:

```text
Can C08 distinguish:
1. test-board/customer-qualification repeat-demand bridge with high MFE but Green-strict drawdown risk,
2. inspection-equipment vocabulary that fails when repeat order and margin/cash bridge are missing,
3. package-inspection theme spike where clean price path collapses without customer/repeat-demand evidence?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C08_R2L93C_219130_TIGER_TESTBOARD_REPEAT","symbol":"219130","company_name":"타이거일렉","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TESTBOARD_CUSTOMER_QUALIFICATION_REPEAT_DEMAND_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-TestBoardCustomerQualificationRepeatDemandBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_watch_MFE90_ge50_controlled_initial_MAE_but_late_drawdown","current_profile_verdict":"current_profile_correct_if_customer_qualification_repeat_demand_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"Test-board/probe-board customer-quality proxy produced strong MFE after entry. It remains positive-watch only because later drawdown shows Green requires exact repeat-demand and margin/cash evidence."}
{"row_type":"case","case_id":"C08_R2L93C_064290_INTEKPLUS_INSPECTION_DECAY","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"INSPECTION_EQUIPMENT_CUSTOMER_QUALITY_VOCABULARY_WITHOUT_DURABLE_MARGIN_CASH_BRIDGE","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-InspectionEquipmentCustomerQualityVocabularyNoDurableMarginCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_sub15_MFE_deep_MAE_share_count_watch_no_margin_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_inspection_customer_quality_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Inspection/customer-quality vocabulary after a February spike had sub-15 MFE and then deep MAE when durable repeat-order and margin/cash evidence were missing. 2024 share-count movement requires repair."}
{"row_type":"case","case_id":"C08_R2L93C_420770_GIGAVIS_PACKAGE_INSPECTION_DECAY","symbol":"420770","company_name":"기가비스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PACKAGE_INSPECTION_THEME_SPIKE_WITHOUT_CUSTOMER_REPEAT_DEMAND_BRIDGE","case_type":"failed_entry_recent_listing_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PackageInspectionThemeSpikeNoCustomerRepeatDemandBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"counterexample_low_MFE_extreme_MAE_recent_listing_watch_no_repeat_demand_bridge","current_profile_verdict":"current_profile_false_positive_if_package_inspection_theme_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Package-inspection theme spike had only small MFE and then severe drawdown. Recent listing and missing repeat-demand/margin bridge keep this in 4B/data-quality watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 219130 타이거일렉 — test-board / customer qualification repeat-demand bridge

Entry row: `2024-02-13 c=28250`.
Observed path: `2024-05-14 h=45300`, then later drawdown into the second half.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93C_C08_219130_20240213_STAGE2_TESTBOARD_REPEAT","case_id":"C08_R2L93C_219130_TIGER_TESTBOARD_REPEAT","symbol":"219130","company_name":"타이거일렉","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TESTBOARD_CUSTOMER_QUALIFICATION_REPEAT_DEMAND_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-TestBoardCustomerQualificationRepeatDemandBridge-PositiveWatch","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":28250.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_testboard_probe_board_customer_quality_repeat_demand_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; test-board/probe-board customer qualification, repeat demand, ASP/mix, margin and cash bridge treated as non-price proxy","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["testboard_customer_quality_proxy","probe_board_process_relevance_proxy","repeat_demand_proxy","relative_strength_after_reset"],"stage3_evidence_fields":["exact_customer_qualification_source_pending","repeat_order_source_pending","ASP_mix_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["MFE90_ge50_watch","late_drawdown_watch","Green_exact_evidence_watch"],"stage4c_evidence_fields":["customer_quality_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/219/219130/2024.csv","profile_path":"atlas/symbol_profiles/219/219130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":51.86,"MFE_90D_pct":60.35,"MFE_180D_pct":60.35,"MAE_30D_pct":-6.90,"MAE_90D_pct":-6.90,"MAE_180D_pct":-36.04,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-14","peak_price":45300.0,"max_drawdown_low_date":"2024-11-18","max_drawdown_low":13050.0,"drawdown_after_peak_pct":-71.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_customer_qualification_repeat_order_ASP_margin_cash_evidence_and_late_drawdown_review","four_b_evidence_type":["MFE90_ge50_watch","late_drawdown_watch","Green_exact_evidence_watch"],"four_c_protection_label":"customer_quality_break_watch_only","trigger_outcome_label":"positive_watch_MFE90_ge50_controlled_initial_MAE_but_late_drawdown","current_profile_verdict":"current_profile_correct_if_customer_qualification_repeat_demand_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"219130_2024-02-13_28250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C08 can allow Yellow/Green-candidate-watch when test-board strength is tied to customer qualification, repeat demand, ASP/mix, margin and cash conversion. Late drawdown blocks automatic Green."}
```

### 6.2 064290 인텍플러스 — inspection-equipment vocabulary without durable margin-cash bridge

Entry row: `2024-02-20 c=35750`.
Observed path: `2024-03-06 h=40850`, then deterioration through June/July with visible share-count movement in the 2024 rows.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93C_C08_064290_20240220_STAGE2_FALSE_POSITIVE_INSPECTION_DECAY","case_id":"C08_R2L93C_064290_INTEKPLUS_INSPECTION_DECAY","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"INSPECTION_EQUIPMENT_CUSTOMER_QUALITY_VOCABULARY_WITHOUT_DURABLE_MARGIN_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;share_count_data_quality_watch","trigger_type":"Stage2-FalsePositive-InspectionEquipmentCustomerQualityVocabularyNoDurableMarginCashBridge","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":35750.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_inspection_equipment_customer_quality_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; inspection/customer-quality vocabulary treated as insufficient without repeat order, revision visibility, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["inspection_equipment_keyword","customer_quality_vocabulary","price_spike"],"stage3_evidence_fields":["repeat_order_missing","revision_visibility_missing","margin_cash_bridge_missing","share_count_repair_pending"],"stage4b_evidence_fields":["sub15_MFE","deep_MAE","share_count_movement_watch","margin_cash_bridge_missing_watch"],"stage4c_evidence_fields":["customer_quality_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.27,"MFE_90D_pct":14.27,"MFE_180D_pct":14.27,"MAE_30D_pct":-4.90,"MAE_90D_pct":-28.95,"MAE_180D_pct":-46.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-06","peak_price":40850.0,"max_drawdown_low_date":"2024-07-23","max_drawdown_low":19100.0,"drawdown_after_peak_pct":-53.24,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"inspection_equipment_customer_quality_vocabulary_without_repeat_order_revision_margin_cash_bridge_should_be_4B_watch_not_positive; share_count_repair_required","four_b_evidence_type":["sub15_MFE","deep_MAE","share_count_movement_watch","margin_cash_bridge_missing_watch"],"four_c_protection_label":"customer_quality_break_watch_only","trigger_outcome_label":"counterexample_sub15_MFE_deep_MAE_share_count_watch_no_margin_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_inspection_customer_quality_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["visible_2024_share_count_movement_watch"],"corporate_action_window_status":"no_profile_CA_candidate; share_count_movement_watch","same_entry_group_id":"064290_2024-02-20_35750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C08 should not promote inspection/customer-quality vocabulary unless repeat order, revision visibility, margin and cash evidence are repaired. Sub-15 MFE and deep MAE force Watch/4B."}
```

### 6.3 420770 기가비스 — package-inspection theme spike without repeat-demand bridge

Entry row: `2024-04-04 c=79000`, the package-inspection theme spike.
Observed path: `2024-04-09 h=82500`, then long decline to `2024-12-09 l=20300`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93C_C08_420770_20240404_STAGE2_FALSE_POSITIVE_PACKAGE_INSPECTION_SPIKE","case_id":"C08_R2L93C_420770_GIGAVIS_PACKAGE_INSPECTION_DECAY","symbol":"420770","company_name":"기가비스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PACKAGE_INSPECTION_THEME_SPIKE_WITHOUT_CUSTOMER_REPEAT_DEMAND_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;recent_listing_watch","trigger_type":"Stage2-FalsePositive-PackageInspectionThemeSpikeNoCustomerRepeatDemandBridge","trigger_date":"2024-04-04","entry_date":"2024-04-04","entry_price":79000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_package_inspection_theme_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; package inspection / advanced inspection vocabulary treated as insufficient without customer qualification, repeat demand, margin and cash bridge","evidence_source_type":"historical_public_theme_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["package_inspection_theme","advanced_inspection_vocabulary","price_spike"],"stage3_evidence_fields":["customer_qualification_missing","repeat_demand_missing","margin_cash_bridge_missing","recent_listing_repair_pending"],"stage4b_evidence_fields":["low_MFE","extreme_MAE","recent_listing_watch","repeat_demand_bridge_missing_watch"],"stage4c_evidence_fields":["customer_quality_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/420/420770/2024.csv","profile_path":"atlas/symbol_profiles/420/420770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.43,"MFE_90D_pct":4.43,"MFE_180D_pct":4.43,"MAE_30D_pct":-21.52,"MAE_90D_pct":-39.56,"MAE_180D_pct":-74.30,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-09","peak_price":82500.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":20300.0,"drawdown_after_peak_pct":-75.39,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"package_inspection_theme_spike_without_customer_qualification_repeat_demand_margin_cash_bridge_should_be_4B_watch_not_positive; recent_listing_watch","four_b_evidence_type":["low_MFE","extreme_MAE","recent_listing_watch","repeat_demand_bridge_missing_watch"],"four_c_protection_label":"customer_quality_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE_recent_listing_watch_no_repeat_demand_bridge","current_profile_verdict":"current_profile_false_positive_if_package_inspection_theme_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["recent_listing_short_history_watch"],"corporate_action_window_status":"clean; recent_listing_watch","same_entry_group_id":"420770_2024-04-04_79000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C08 should not count package-inspection theme spikes as customer-quality/repeat-demand validation unless customer qualification, repeat demand, margin and cash evidence are repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L93C_219130_TIGER_TESTBOARD_REPEAT","trigger_id":"R2L93C_C08_219130_20240213_STAGE2_TESTBOARD_REPEAT","symbol":"219130","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_scope":"current_default_proxy","profile_hypothesis":"C08 should reward customer qualification and repeat-demand mechanics, not test-board vocabulary alone","raw_component_scores_before":{"customer_qualification_score":12,"repeat_consumable_demand_score":11,"process_relevance_score":11,"shipment_PO_score":9,"ASP_mix_score":9,"margin_bridge_score":9,"cash_conversion_score":7,"relative_strength_score":13,"valuation_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"customer_qualification_score":15,"repeat_consumable_demand_score":14,"process_relevance_score":13,"shipment_PO_score":11,"ASP_mix_score":11,"margin_bridge_score":11,"cash_conversion_score":9,"relative_strength_score":14,"valuation_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Strong MFE supports Green-candidate-watch only if exact customer qualification/repeat order/margin evidence is repaired; late drawdown blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L93C_064290_INTEKPLUS_INSPECTION_DECAY","trigger_id":"R2L93C_C08_064290_20240220_STAGE2_FALSE_POSITIVE_INSPECTION_DECAY","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_scope":"current_default_proxy","profile_hypothesis":"inspection/customer-quality vocabulary without repeat order and margin bridge should be blocked","raw_component_scores_before":{"customer_qualification_score":2,"repeat_consumable_demand_score":0,"process_relevance_score":3,"shipment_PO_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":4,"valuation_risk_score":-14,"theme_spike_risk":-16,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"customer_qualification_score":0,"repeat_consumable_demand_score":0,"process_relevance_score":1,"shipment_PO_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_risk_score":-24,"theme_spike_risk":-22,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Sub-15 MFE, deep MAE and share-count movement require exact repeat-order and margin/cash evidence before any promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L93C_420770_GIGAVIS_PACKAGE_INSPECTION_DECAY","trigger_id":"R2L93C_C08_420770_20240404_STAGE2_FALSE_POSITIVE_PACKAGE_INSPECTION_SPIKE","symbol":"420770","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_scope":"current_default_proxy","profile_hypothesis":"package-inspection theme spike without customer qualification and repeat demand should remain Watch/4B","raw_component_scores_before":{"customer_qualification_score":1,"repeat_consumable_demand_score":0,"process_relevance_score":2,"shipment_PO_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":4,"valuation_risk_score":-16,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/RecentListingWatch","raw_component_scores_after":{"customer_qualification_score":0,"repeat_consumable_demand_score":0,"process_relevance_score":0,"shipment_PO_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_risk_score":-28,"theme_spike_risk":-24,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/RecentListingWatch","component_delta_explanation":"Low MFE, extreme MAE and recent-listing watch require customer/repeat-demand evidence and price-quality repair before promotion."}
```

## 8. Aggregate and transition rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_TESTBOARD_POSITIVE_VS_INSPECTION_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":2,"avg_MFE90_pct":26.35,"avg_MAE90_pct":-25.14,"avg_MFE180_pct":26.35,"avg_MAE180_pct":-52.30,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE90_le_minus20":0.67,"interpretation":"C08 needs customer-quality/repeat-demand discipline. 타이거일렉 shows a test-board repeat-demand bridge can support Green-candidate-watch, while 인텍플러스 and 기가비스 show inspection/customer-quality vocabulary or theme spikes should not be promoted without repeat order, ASP/mix, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"219130","trigger_type":"Stage2-Actionable-TestBoardCustomerQualificationRepeatDemandBridge-PositiveWatch","entry_date":"2024-02-13","stage2_to_90D_outcome":"positive_watch_MFE90_ge50_controlled_initial_MAE","stage2_to_180D_outcome":"testboard_repeat_demand_bridge_but_late_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/Green-candidate only when customer qualification, repeat demand, ASP/mix, margin and cash bridge are exact-repaired."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"064290","trigger_type":"Stage2-FalsePositive-InspectionEquipmentCustomerQualityVocabularyNoDurableMarginCashBridge","entry_date":"2024-02-20","stage2_to_90D_outcome":"bad_stage2_sub15_MFE_deep_MAE_share_count_watch","stage2_to_180D_outcome":"failed_inspection_customer_quality_vocabulary_no_repeat_order_margin_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Inspection/customer-quality vocabulary without repeat order and margin bridge should remain Watch/4B; share-count repair required."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"420770","trigger_type":"Stage2-FalsePositive-PackageInspectionThemeSpikeNoCustomerRepeatDemandBridge","entry_date":"2024-04-04","stage2_to_90D_outcome":"bad_stage2_low_MFE_extreme_MAE_recent_listing_watch","stage2_to_180D_outcome":"failed_package_inspection_theme_spike_no_repeat_demand_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Package-inspection theme spike without customer qualification/repeat-demand bridge should remain Watch/4B; recent-listing repair required."}
{"row_type":"residual_contribution","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","residual_type":"inspection_theme_vocabulary_overcredit_without_customer_qualification_repeat_order_margin_cash_bridge","contribution":"Adds one C08 test-board repeat-demand positive-watch and two inspection/theme weak-bridge counterexamples, selected because C08 remains the thinnest raw Priority-0 archetype.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TESTBOARD_INSPECTION_CUSTOMER_QUALITY_REPEAT_DEMAND_VS_INSPECTION_PRICE_SPIKE_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C08 now has a tertiary pocket: test-board repeat-demand positive-watch plus inspection/package-inspection weak-bridge counterexamples; next C08 loops should exact-URL repair customer qualification, repeat demand, shipment conversion, ASP/mix, margin and cash evidence."}
```

## 9. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_customer_qualification_repeat_order_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"219130 worked as positive-watch when test-board/customer-quality repeat-demand proxy existed; 064290 and 420770 failed when repeat-order and margin/cash evidence were missing."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_inspection_theme_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"064290 and 420770 showed inspection/customer-quality vocabulary or theme spikes should not validate missing repeat-demand/margin bridge."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_share_count_recent_listing_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"064290 has 2024 share-count movement and 420770 is short-history/recent-listing relative to the corpus; patching requires price-quality repair."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_late_drawdown_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"219130 had high MFE but large after-peak drawdown; Green requires exact customer/repeat-demand/margin evidence."}
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
  - inspection_equipment_vocabulary_overcredit
  - package_inspection_theme_spike_overcredit
  - customer_qualification_bridge_missing
  - repeat_order_margin_cash_bridge_missing
  - share_count_recent_listing_data_quality_watch
new_axis_proposed:
  - C08_customer_qualification_repeat_order_margin_cash_bridge_required_shadow_only
  - C08_inspection_theme_local_4B_guard_shadow_only
  - C08_share_count_recent_listing_data_quality_guard_shadow_only
  - C08_late_drawdown_Green_strict_guard_shadow_only
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

## 11. Data-quality caveat

All selected triggers use Stock-Web tradable raw OHLC rows.
`219130` has no corporate-action candidate and the selected 2024 window is clean.
`064290` has no profile-level corporate-action candidate but visible 2024 share-count movement in OHLC rows; it remains share-count watch before production patching.
`420770` has no corporate-action candidate, but it is a recent-listing/short-history row relative to the older corpus and needs price-quality repair before any patch promotion.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for residual price-path analysis
evidence_url_pending = true
source_proxy_only = true
share_count_movement_watch = true for 064290
recent_listing_watch = true for 420770
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
3. Confirm R2 / L2 / C08 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - previous R2 loop87 C08 symbols
   - previous R2 loop92 C08 symbols
   - previous R2 loop93 C08 secondary symbols
   - recent R2 loop93 C09/C07/C06/C10 symbols
6. Confirm recently touched C01/C09/C28/C23/C17/C13/C12 rows are not ingested from this MD.
7. Treat 219130 as Yellow/Green-candidate-watch only, not Green, until exact customer qualification/repeat-order/margin/cash evidence is repaired.
8. Treat 064290 and 420770 as weak-bridge/data-quality failure modes unless exact repeat-demand/margin/cash evidence is added later.
9. Keep 064290 in share-count data-quality watch before patch consideration.
10. Keep 420770 in recent-listing/short-history watch before patch consideration.
11. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C08-scoped safe patch candidates:
   - C08_customer_qualification_repeat_order_margin_cash_bridge_required
   - C08_inspection_theme_local_4B_guard
   - C08_share_count_recent_listing_data_quality_guard
   - C08_late_drawdown_Green_strict_guard
12. Do not loosen Stage3-Green.
13. Do not use future MFE/MAE in runtime scoring.
14. Use this MD only for calibration profile planning.
```

## 13. Round state

```text
completed_round = R2
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C08 again if strictly following raw index, otherwise C09/C01 based on reconciled local-loop count and fatigue controls
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 14. Final one-line contribution

```text
This loop adds 3 new independent C08 cases, 1 test-board customer-qualification repeat-demand positive-watch, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.
```
