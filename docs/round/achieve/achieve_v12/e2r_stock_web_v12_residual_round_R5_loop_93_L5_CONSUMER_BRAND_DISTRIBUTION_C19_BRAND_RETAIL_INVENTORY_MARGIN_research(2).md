# E2R Stock-Web v12 Residual Research — R5 Loop 93 / L5 / C19

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R5
loop: 93
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: CONVENIENCE_STORE_INVENTORY_MARGIN_RESET_VS_DEPARTMENT_STORE_AND_RETAIL_MARGIN_DECAY
sector: consumer / brand / retail / convenience store / department store / inventory / sell-through / gross margin / operating margin / cash conversion
output_file: e2r_stock_web_v12_residual_round_R5_loop_93_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after local loop93 expansions in C09, C01, C07, C06, C10 and C11.

```text
selected_round = R5
selected_loop = 93
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
```

Reason for selecting C19:

```text
v12 scheduler = coverage_index_first
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
selected_archetype_drives_round = true
```

No-Repeat Index Priority 0 snapshot used as duplicate-avoidance ledger:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY = 14 rows
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF = 15 rows
C01_ORDER_BACKLOG_MARGIN_BRIDGE = 16 rows
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH = 18 rows
C06_HBM_MEMORY_CUSTOMER_CAPACITY = 21 rows
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE = 21 rows
C14_EV_DEMAND_SLOWDOWN_4B_4C = 21 rows
C11_BATTERY_ORDERBOOK_RERATING = 23 rows
C02_POWER_GRID_DATACENTER_CAPEX = 24 rows
C19_BRAND_RETAIL_INVENTORY_MARGIN = 24 rows
C27_CONTENT_IP_GLOBAL_MONETIZATION = 24 rows
```

Local run-stream hygiene:

```text
C08 was expanded in loop92.
C09, C01, C07, C06, C10 and C11 were expanded in loop93.
C02 was expanded in loop92 by the local stream.
Therefore this run moves to C19, a still-thin Priority-0 consumer archetype that has not been expanded in the recent local loop93 stream.
```

This loop avoids recent R5 symbols:

```text
R5 loop86 C18: 003230, 005610, 007310
R5 loop87 C19: 069960, 008770, 031430
R5 loop88 C20: 352480, 237880, 018250
R5 loop89 C18: 005180, 101530, 248170
R5 loop90 C19: 090430, 383220, 020000
R5 loop91 C20: 003350, 051900, 004370
R5 loop92 C18: 017810, 267980, 264900
```

Candidate hygiene note:

```text
During this execution path, recently touched R3/C11 battery rows such as 348370, 121600 and 020150 were queried while checking alternatives.
They are excluded from this C19 output because the valid output must be R5/L5/C19.
```

Selected symbols:

```text
282330, 004170, 007070
```

The selected pocket is:

```text
convenience-store inventory reset / margin discipline / cash bridge positive-watch
vs
department-store discretionary-demand and duty-free/brand inventory vocabulary without sell-through and margin bridge
vs
retail-platform/convenience vocabulary where inventory/OPM bridge is not enough and corporate-action candidate watch blocks patching
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"282330","company_name":"BGF리테일","profile_path":"atlas/symbol_profiles/282/282330.json","first_date":"2017-12-08","last_date":"2026-02-20","trading_day_count":2010,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"004170","company_name":"신세계","profile_path":"atlas/symbol_profiles/004/004170.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7737,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1996-01-03","2004-12-22","2011-02-01","2011-02-25","2011-06-10"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"007070","company_name":"GS리테일","profile_path":"atlas/symbol_profiles/007/007070.json","first_date":"2011-12-23","last_date":"2026-02-20","trading_day_count":3461,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2021-07-16","2024-12-23"],"has_major_raw_discontinuity":true,"calibration_caveat":"2024-12-23 corporate-action candidate is after the selected entry and outside the early forward window; keep data-quality watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_2024_entry_window_usable; late_2024_CA_candidate_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"282330","trigger_type":"Stage2-Actionable-ConvenienceStoreInventoryResetMarginCashBridge-PositiveWatch","entry_date":"2024-07-05","duplicate_status":"new C19 symbol/trigger/date combination outside recent R5 C18/C19/C20 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"004170","trigger_type":"Stage2-FalsePositive-DepartmentStoreBrandInventoryVocabularyNoSellThroughMarginBridge","entry_date":"2024-02-08","duplicate_status":"new C19 symbol/trigger/date combination outside recent R5 C18/C19/C20 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"007070","trigger_type":"Stage2-FalsePositive-RetailPlatformConvenienceVocabularyNoOPMCashBridge","entry_date":"2024-01-02","duplicate_status":"new C19 symbol/trigger/date combination outside recent R5 C18/C19/C20 loop symbols; late-2024 CA candidate watch"}
```

## 4. Research question

C19 is not “소비재/리테일 브랜드가 있다.”
The useful retail/inventory signal must prove the sell-through-to-margin chain:

```text
same-store or channel traffic
sell-through rather than shipment stuffing
inventory days improvement
markdown pressure containment
gross-margin repair
store/franchise operating leverage
receivables / working-capital discipline
OPM revision
cash conversion
```

A retail headline without this bridge is a shelf filled with boxes. It becomes an E2R signal only when the box leaves the shelf at the right price, the markdown does not eat the margin, and the cash comes back.

Residual question:

```text
Can C19 distinguish:
1. convenience-store inventory reset / margin discipline with moderate MFE and shallow MAE,
2. department-store / brand-discretionary vocabulary where sell-through and margin bridge are not repaired,
3. retail-platform vocabulary where weak MFE and data-quality watch should block promotion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C19_R5L93_282330_BGF_RETAIL_INVENTORY_RESET","symbol":"282330","company_name":"BGF리테일","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_STORE_INVENTORY_RESET_MARGIN_CASH_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ConvenienceStoreInventoryResetMarginCashBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_watch_MFE90_ge20_shallow_MAE_inventory_margin_reset_bridge","current_profile_verdict":"current_profile_correct_if_sellthrough_inventory_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"Convenience-store inventory reset / margin-cash proxy after midyear reset produced MFE90 above 20 with shallow MAE. It is Yellow/positive-watch only unless exact sell-through, inventory days, OPM and cash evidence is repaired."}
{"row_type":"case","case_id":"C19_R5L93_004170_SHINSEGAE_DEPARTMENT_STORE_DECAY","symbol":"004170","company_name":"신세계","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_BRAND_INVENTORY_VOCABULARY_WITHOUT_SELLTHROUGH_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DepartmentStoreBrandInventoryVocabularyNoSellThroughMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_sellthrough_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_department_store_brand_inventory_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Department-store/brand discretionary vocabulary had low MFE and deep later MAE without fresh sell-through, markdown containment, inventory-days or OPM/cash bridge."}
{"row_type":"case","case_id":"C19_R5L93_007070_GSRETAIL_OPM_CASH_DECAY","symbol":"007070","company_name":"GS리테일","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"RETAIL_PLATFORM_CONVENIENCE_VOCABULARY_WITHOUT_OPM_CASH_BRIDGE","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-RetailPlatformConvenienceVocabularyNoOPMCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_near_zero_MFE_MAE_expansion_no_OPM_cash_bridge_late_CA_watch","current_profile_verdict":"current_profile_false_positive_if_retail_platform_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Retail-platform/convenience vocabulary had near-zero forward MFE and persistent drawdown when OPM/cash bridge was not repaired. Late-2024 corporate-action candidate keeps data-quality watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 282330 BGF리테일 — convenience-store inventory reset / margin-cash bridge positive-watch

Entry row: `2024-07-05 c=99900`, after a first-half drawdown and inventory/margin reset area.
Observed path: high `2024-09-25 h=125000` and shallow later low `2024-12-09 l=98000`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L93_C19_282330_20240705_STAGE2_CONVENIENCE_INVENTORY_MARGIN","case_id":"C19_R5L93_282330_BGF_RETAIL_INVENTORY_RESET","symbol":"282330","company_name":"BGF리테일","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_STORE_INVENTORY_RESET_MARGIN_CASH_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ConvenienceStoreInventoryResetMarginCashBridge-PositiveWatch","trigger_date":"2024-07-05","entry_date":"2024-07-05","entry_price":99900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_convenience_store_inventory_margin_cash_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; convenience-store inventory reset, same-store/sell-through, margin discipline and cash conversion treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["inventory_reset_proxy","sellthrough_proxy","store_margin_proxy","cash_conversion_proxy"],"stage3_evidence_fields":["exact_same_store_source_pending","inventory_days_source_pending","OPM_revision_source_pending","cash_conversion_source_pending"],"stage4b_evidence_fields":["moderate_MFE_watch","Green_strict_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv","profile_path":"atlas/symbol_profiles/282/282330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.92,"MFE_90D_pct":25.13,"MFE_180D_pct":25.13,"MAE_30D_pct":-0.90,"MAE_90D_pct":-0.90,"MAE_180D_pct":-1.90,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-25","peak_price":125000.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":98000.0,"drawdown_after_peak_pct":-21.60,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.63,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_sellthrough_inventory_days_OPM_cash_evidence","four_b_evidence_type":["moderate_MFE_watch","Green_strict_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_watch_MFE90_ge20_shallow_MAE_inventory_margin_reset_bridge","current_profile_verdict":"current_profile_correct_if_sellthrough_inventory_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"282330_2024-07-05_99900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C19 can allow Yellow/positive-watch when retail strength is tied to sell-through, inventory-days repair, margin discipline, OPM revision and cash conversion. Green requires exact source-grade evidence."}
```

### 6.2 004170 신세계 — department-store / brand inventory vocabulary without sell-through margin bridge

Entry row: `2024-02-08 c=186900`, after a department-store / discretionary-reopening rebound.
Observed path: local high `2024-02-19 h=190300`, then deterioration to `2024-08-05 l=138800`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L93_C19_004170_20240208_STAGE2_FALSE_POSITIVE_DEPARTMENT_STORE","case_id":"C19_R5L93_004170_SHINSEGAE_DEPARTMENT_STORE_DECAY","symbol":"004170","company_name":"신세계","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_BRAND_INVENTORY_VOCABULARY_WITHOUT_SELLTHROUGH_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-DepartmentStoreBrandInventoryVocabularyNoSellThroughMarginBridge","trigger_date":"2024-02-08","entry_date":"2024-02-08","entry_price":186900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_department_store_brand_inventory_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; department-store / brand discretionary / duty-free inventory vocabulary treated as insufficient without fresh sell-through, markdown containment, inventory days, OPM and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["department_store_vocabulary","brand_discretionary_rebound","relative_strength_watch"],"stage3_evidence_fields":["fresh_sellthrough_missing","markdown_pressure_containment_missing","inventory_days_bridge_missing","OPM_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE","deep_MAE","sellthrough_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004170/2024.csv","profile_path":"atlas/symbol_profiles/004/004170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.82,"MFE_90D_pct":1.82,"MFE_180D_pct":1.82,"MAE_30D_pct":-8.51,"MAE_90D_pct":-18.24,"MAE_180D_pct":-25.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":190300.0,"max_drawdown_low_date":"2024-08-05","max_drawdown_low":138800.0,"drawdown_after_peak_pct":-27.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"department_store_brand_inventory_vocabulary_without_sellthrough_markdown_OPM_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","deep_MAE","sellthrough_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_sellthrough_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_department_store_brand_inventory_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"004170_2024-02-08_186900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C19 should not promote department-store/brand inventory vocabulary unless sell-through, markdown containment, inventory-days repair, OPM revision and cash conversion are exact-repaired. Low MFE and deep MAE force Watch/4B routing."}
```

### 6.3 007070 GS리테일 — retail-platform / convenience vocabulary without OPM-cash bridge

Entry row: `2024-01-02 c=23500`.
Observed path: local high `2024-01-08 h=23900`, then a steady first-half decline to the 20,000 area; 2024-12-23 corporate-action candidate remains a late data-quality watch.

```jsonl
{"row_type":"trigger","trigger_id":"R5L93_C19_007070_20240102_STAGE2_FALSE_POSITIVE_RETAIL_OPM_CASH","case_id":"C19_R5L93_007070_GSRETAIL_OPM_CASH_DECAY","symbol":"007070","company_name":"GS리테일","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"RETAIL_PLATFORM_CONVENIENCE_VOCABULARY_WITHOUT_OPM_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;data_quality_watch;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-RetailPlatformConvenienceVocabularyNoOPMCashBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":23500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_retail_platform_convenience_inventory_margin_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; retail platform / convenience / inventory vocabulary treated as insufficient without same-store, inventory-days, OPM revision and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["retail_platform_vocabulary","convenience_store_keyword","inventory_margin_vocabulary"],"stage3_evidence_fields":["same_store_missing","inventory_days_bridge_missing","OPM_revision_missing","cash_conversion_missing"],"stage4b_evidence_fields":["near_zero_MFE","OPM_cash_bridge_missing_watch","late_CA_candidate_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007070/2024.csv","profile_path":"atlas/symbol_profiles/007/007070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.70,"MFE_90D_pct":1.70,"MFE_180D_pct":1.70,"MAE_30D_pct":-9.15,"MAE_90D_pct":-15.15,"MAE_180D_pct":-15.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-08","peak_price":23900.0,"max_drawdown_low_date":"2024-04-09","max_drawdown_low":19940.0,"drawdown_after_peak_pct":-16.57,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"retail_platform_convenience_vocabulary_without_OPM_cash_bridge_should_be_4B_watch_not_positive; late_CA_candidate_requires_repair","four_b_evidence_type":["near_zero_MFE","OPM_cash_bridge_missing_watch","late_CA_candidate_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_MAE_expansion_no_OPM_cash_bridge_late_CA_watch","current_profile_verdict":"current_profile_false_positive_if_retail_platform_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024-12-23_corporate_action_candidate_after_selected_forward_window_watch"],"corporate_action_window_status":"selected_entry_window_usable; late_2024_CA_candidate_watch","same_entry_group_id":"007070_2024-01-02_23500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C19 should not count retail/convenience vocabulary as margin evidence unless same-store, sell-through, inventory-days, OPM and cash evidence are repaired. Late 2024 CA candidate blocks production patching until repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C19_R5L93_282330_BGF_RETAIL_INVENTORY_RESET","trigger_id":"R5L93_C19_282330_20240705_STAGE2_CONVENIENCE_INVENTORY_MARGIN","symbol":"282330","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C19 requires sell-through, inventory days, markdown containment, OPM revision and cash bridge rather than retail vocabulary alone","raw_component_scores_before":{"sellthrough_score":10,"inventory_days_score":11,"markdown_containment_score":9,"gross_margin_score":9,"OPM_revision_score":8,"working_capital_score":8,"cash_conversion_score":8,"relative_strength_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":62,"stage_label_before":"Stage2-Watch/PositiveControl","raw_component_scores_after":{"sellthrough_score":13,"inventory_days_score":14,"markdown_containment_score":11,"gross_margin_score":11,"OPM_revision_score":10,"working_capital_score":10,"cash_conversion_score":10,"relative_strength_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable/Yellow-Watch","component_delta_explanation":"Inventory reset and margin-cash bridge supports Yellow-watch; moderate MFE and proxy-only evidence block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C19_R5L93_004170_SHINSEGAE_DEPARTMENT_STORE_DECAY","trigger_id":"R5L93_C19_004170_20240208_STAGE2_FALSE_POSITIVE_DEPARTMENT_STORE","symbol":"004170","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_scope":"current_default_proxy","profile_hypothesis":"department-store brand inventory vocabulary without sell-through and margin bridge should be blocked","raw_component_scores_before":{"sellthrough_score":1,"inventory_days_score":1,"markdown_containment_score":0,"gross_margin_score":0,"OPM_revision_score":0,"working_capital_score":0,"cash_conversion_score":0,"relative_strength_score":2,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"sellthrough_score":0,"inventory_days_score":0,"markdown_containment_score":0,"gross_margin_score":0,"OPM_revision_score":0,"working_capital_score":0,"cash_conversion_score":0,"relative_strength_score":0,"execution_risk_score":-24,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE require sell-through, markdown containment, OPM and cash evidence before any Yellow/Green promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C19_R5L93_007070_GSRETAIL_OPM_CASH_DECAY","trigger_id":"R5L93_C19_007070_20240102_STAGE2_FALSE_POSITIVE_RETAIL_OPM_CASH","symbol":"007070","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_scope":"current_default_proxy","profile_hypothesis":"retail/convenience vocabulary without OPM and cash conversion should remain Watch/4B","raw_component_scores_before":{"sellthrough_score":1,"inventory_days_score":1,"markdown_containment_score":0,"gross_margin_score":0,"OPM_revision_score":0,"working_capital_score":0,"cash_conversion_score":0,"relative_strength_score":1,"execution_risk_score":-10,"theme_spike_risk":-12,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"sellthrough_score":0,"inventory_days_score":0,"markdown_containment_score":0,"gross_margin_score":0,"OPM_revision_score":0,"working_capital_score":0,"cash_conversion_score":0,"relative_strength_score":0,"execution_risk_score":-18,"theme_spike_risk":-16,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Near-zero MFE plus missing OPM/cash bridge and late CA candidate keep this in Watch/4B."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R5L93_C19_P0_CURRENT","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C19 needs explicit sell-through, inventory-days, markdown, OPM/cash and data-quality taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":9.55,"avg_MAE90_pct":-11.43,"avg_MFE180_pct":9.55,"avg_MAE180_pct":-14.26,"false_positive_rate":0.67,"data_quality_watch_count":1,"score_return_alignment_verdict":"mixed_without_C19_sellthrough_inventory_OPM_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R5L93_C19_P1_SECTOR_SPECIFIC","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_id":"P1_L5_retail_inventory_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L5 retail signals need sell-through, inventory-days improvement, markdown containment, gross margin, OPM revision or cash conversion before Stage2-Actionable","changed_axes":["sellthrough_required","inventory_margin_required","OPM_cash_required","late_CA_data_quality_guard"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_sellthrough_inventory_days_margin_OPM_or_cash_proxy"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R5L93_C19_P2_CANONICAL","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_id":"P2_C19_sellthrough_inventory_OPM_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C19 should reward sell-through-to-margin mechanics, not retail/brand vocabulary","changed_axes":["C19_sellthrough_inventory_OPM_cash_bridge_required","C19_department_store_retail_vocabulary_local_4B_guard","C19_late_CA_data_quality_guard","C19_moderate_MFE_Green_strict_guard"],"changed_thresholds":{"stage2_yellow_gate":"sellthrough_or_inventory_days_plus_OPM_or_cash_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R5L93_C19_P3_COUNTEREXAMPLE_GUARD","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_id":"P3_C19_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If sell-through/OPM bridge is missing, MFE90<5 or MAE180<=-20 blocks Yellow/Green and routes to Watch/4B","changed_axes":["C19_low_MFE_guardrail","C19_deep_MAE_guardrail","C19_cash_bridge_missing_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_5_or_MAE180_le_minus20)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_CONVENIENCE_INVENTORY_POSITIVE_VS_DEPARTMENT_RETAIL_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":9.55,"avg_MAE90_pct":-11.43,"avg_MFE180_pct":9.55,"avg_MAE180_pct":-14.26,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"interpretation":"C19 needs bridge discipline. BGF리테일 shows convenience-store inventory reset and OPM/cash bridge can support Yellow-watch, while 신세계 and GS리테일 show retail/brand vocabulary should not be promoted without sell-through, markdown containment, inventory-days, OPM and cash evidence."}
{"row_type":"stage_transition_summary","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"282330","trigger_type":"Stage2-Actionable-ConvenienceStoreInventoryResetMarginCashBridge-PositiveWatch","entry_date":"2024-07-05","stage2_to_90D_outcome":"positive_watch_MFE90_ge20_shallow_MAE","stage2_to_180D_outcome":"inventory_margin_reset_bridge_but_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/positive-watch when retail strength is tied to sell-through, inventory-days, OPM and cash bridge; exact evidence required for Green."}
{"row_type":"stage_transition_summary","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"004170","trigger_type":"Stage2-FalsePositive-DepartmentStoreBrandInventoryVocabularyNoSellThroughMarginBridge","entry_date":"2024-02-08","stage2_to_90D_outcome":"bad_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_department_store_inventory_vocabulary_deep_MAE","MFE90_ge20":false,"MAE180_le_minus20":true,"transition_note":"Department-store/brand vocabulary without sell-through and margin/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"007070","trigger_type":"Stage2-FalsePositive-RetailPlatformConvenienceVocabularyNoOPMCashBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_OPM_cash_missing","stage2_to_180D_outcome":"retail_platform_vocabulary_4B_watch_late_CA_candidate","MFE90_ge20":false,"late_CA_candidate_watch":true,"transition_note":"Retail/convenience vocabulary without OPM and cash bridge should remain Watch/4B; late 2024 CA candidate requires repair."}
{"row_type":"residual_contribution","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","residual_type":"department_store_retail_vocabulary_overcredit_without_sellthrough_inventory_OPM_cash_bridge","contribution":"Adds two C19 4B counterexamples against one convenience-store inventory reset positive-watch, selected because C19 is Priority-0 under-30 coverage.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"CONVENIENCE_STORE_INVENTORY_MARGIN_RESET_VS_DEPARTMENT_STORE_AND_RETAIL_MARGIN_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C19 now has one convenience-store inventory-margin positive-watch and two retail/department weak-bridge counterexamples; next C19 loops should exact-URL repair sell-through, inventory-days, markdown pressure, gross margin, OPM revision and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_sellthrough_inventory_OPM_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"282330 worked when inventory-reset/margin-cash proxy existed; 004170 and 007070 failed when sell-through/OPM/cash bridge was missing."}
{"row_type":"shadow_weight","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_department_store_retail_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"004170 and 007070 showed low/near-zero MFE when retail/brand vocabulary was not tied to sell-through, markdown containment, OPM and cash evidence."}
{"row_type":"shadow_weight","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_late_CA_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"007070 has a 2024-12-23 corporate-action candidate after selected entry, so production patching requires price-path/evidence repair."}
{"row_type":"shadow_weight","round":"R5","loop":"93","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_moderate_MFE_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"282330 is constructive but moderate MFE; Green requires exact same-store, inventory-days, OPM and cash evidence."}
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
  - retail_brand_vocabulary_overcredit
  - department_store_inventory_vocabulary_overcredit
  - sellthrough_inventory_OPM_cash_bridge_missing
  - late_CA_data_quality_watch
  - moderate_MFE_Green_strict_watch
new_axis_proposed:
  - C19_sellthrough_inventory_OPM_cash_bridge_required_shadow_only
  - C19_department_store_retail_vocabulary_local_4B_guard_shadow_only
  - C19_late_CA_data_quality_guard_shadow_only
  - C19_moderate_MFE_Green_strict_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows.
`282330` has no corporate-action candidate and the selected 2024 window is clean.
`004170` has old corporate-action/name-transition candidates before 2024; the selected 2024 window is usable.
`007070` has a 2024-12-23 corporate-action candidate after selected entry and remains late-CA data-quality watch before production patching.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
late_CA_candidate_watch = true for 007070
promotion should prefer hold / exact evidence repair until exact URLs are added
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
5. Confirm this loop was selected by coverage-index-first after recent C08/C09/C01/C07/C06/C10/C11 local expansions.
6. Confirm this loop avoided:
   - previous R5 loop86 C18 symbols
   - previous R5 loop87 C19 symbols
   - previous R5 loop88 C20 symbols
   - previous R5 loop89 C18 symbols
   - previous R5 loop90 C19 symbols
   - previous R5 loop91 C20 symbols
   - previous R5 loop92 C18 symbols
7. Confirm touched R3/C11 and earlier semiconductor/battery rows are not ingested from this MD.
8. Keep 007070 in late-CA data-quality watch before patch consideration.
9. Treat 004170 and 007070 as weak-bridge failure modes unless exact sell-through/OPM/cash evidence is added later.
10. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C19-scoped safe patch candidates:
   - C19_sellthrough_inventory_OPM_cash_bridge_required
   - C19_department_store_retail_vocabulary_local_4B_guard
   - C19_late_CA_data_quality_guard
   - C19_moderate_MFE_Green_strict_guard
11. Do not loosen Stage3-Green.
12. Do not use future MFE/MAE in runtime scoring.
13. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R5
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C27_CONTENT_IP_GLOBAL_MONETIZATION or remaining Priority-0 under-30 archetype
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 convenience-store inventory/margin positive-watch, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.
```
