# E2R Stock-Web v12 Residual Research — R2 Loop 92 / L2 / C08

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 92
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: MEMORY_TEST_EQUIPMENT_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_THEME_PRICE_MFE_DECAY
sector: AI / semiconductor / test equipment / socket / probe / customer quality / order conversion / margin bridge
output_file: e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R1 loop 92`.

```text
scheduled_round = R2
scheduled_loop = 92
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

R2 is restricted to AI / semiconductor / electronics.
C08 is selected because the recent R2 loop sequence has rotated `C06 → C07`, so loop92 returns to semiconductor test / socket / customer-quality residuals.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
rows = 21
symbols = 11
good/bad Stage2 = 9/5
4B/4C = 2/0
top-covered = UNKNOWN_SYMBOL, 089030, 095340, 131290, 252990, 058470
```

This loop avoids the C08 top-covered list and recent R2 loop symbols:

```text
R2 loop85 C06: 000660, 005930, 009150
R2 loop86 C07: 042700, 064760, 003160
R2 loop87 C08: 232140, 425420, 098120
R2 loop88 C09: 039030, 412350, 253590
R2 loop89 C10: 403870, 166090, 074600
R2 loop90 C06: 036540, 033170, 394280
R2 loop91 C07: 084370, 086390, 217190
```

Candidate hygiene note:

```text
During this execution path, a stale R1/C02 file and unused R1/C02 candidate rows such as 007610, 065770, 037030 and 237750 were touched while checking alternatives.
Those rows are not used in this R2/C08 output.
```

Selected symbols:

```text
092870, 080580, 237750
```

The selected pocket is:

```text
memory tester / customer-quality / order-conversion bridge
vs
test-socket vocabulary with high early volatility and no durable customer-order bridge
vs
digital-grid/protection-relay price MFE stress reused only as a non-C08 weak-bridge contrast
```

`237750` is intentionally treated as a cross-label stress row here because the symbol can look “electrical/digital-grid” rather than true semiconductor test/socket. It is not counted as a C02 contribution in this MD.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"092870","company_name":"엑시콘","profile_path":"atlas/symbol_profiles/092/092870.json","first_date":"2014-12-24","last_date":"2026-02-20","trading_day_count":2730,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2015-10-22","2024-07-31"],"has_major_raw_discontinuity":true,"calibration_caveat":"2024-07-31 corporate-action candidate occurs after selected 2024-02-28 entry; keep data-quality watch before any patch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_entry_before_2024-07-31_candidate; data_quality_watch"}
{"row_type":"price_source_validation","symbol":"080580","company_name":"오킨스전자","profile_path":"atlas/symbol_profiles/080/080580.json","first_date":"2014-12-24","last_date":"2026-02-20","trading_day_count":2737,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2021-01-07","2021-01-29"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"237750","company_name":"피앤씨테크","profile_path":"atlas/symbol_profiles/237/237750.json","first_date":"2016-07-04","last_date":"2026-02-20","trading_day_count":2363,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"092870","trigger_type":"Stage2-Actionable-MemoryTesterCustomerQualityOrderBridge-PositiveWatch","entry_date":"2024-02-28","duplicate_status":"new C08 symbol/trigger/date combination outside C08 top-covered and recent R2 loop symbols; 2024-07-31 data-quality watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"080580","trigger_type":"Stage2-FalsePositive-TestSocketThemeVolatilityNoDurableCustomerOrderBridge","entry_date":"2024-01-22","duplicate_status":"new C08 symbol/trigger/date combination outside C08 top-covered and recent R2 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"237750","trigger_type":"Stage2-FalsePositive-DigitalGridRelayPriceMFE-NoSemiCustomerQualityBridge","entry_date":"2024-01-02","duplicate_status":"new C08 symbol/trigger/date combination outside C08 top-covered and recent R2 loop symbols; cross-label stress row, not C02 contribution"}
```

## 4. Research question

C08 is not “반도체 테스트/소켓 단어가 있다.”
The useful signal must prove the customer-quality chain:

```text
customer qualification or design-in
specific memory / advanced-package exposure
socket / tester / probe-card order visibility
delivery or acceptance schedule
repeat order or utilization
ASP / mix improvement
gross-margin bridge
working-capital discipline
cash conversion
```

A test-equipment headline without this bridge is a probe card hovering above the wafer. Contact has not happened yet. E2R needs the touchdown: customer qualification, order, delivery, yield support, margin and cash.

Residual question:

```text
Can C08 distinguish:
1. memory tester / customer-quality / order-conversion bridge with strong MFE but data-quality watch,
2. test-socket theme volatility where the price move is not backed by durable customer order,
3. price-MFE or cross-label grid/electrical vocabulary that does not prove semiconductor customer quality?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C08_R2L92_092870_EXICON_MEMORY_TESTER_ORDER","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMORY_TESTER_CUSTOMER_QUALITY_ORDER_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-MemoryTesterCustomerQualityOrderBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"positive_high_MFE90_low_entry_MAE_but_2024_CA_data_quality_watch","current_profile_verdict":"current_profile_correct_if_customer_qualification_order_delivery_margin_cash_bridge_required_and_data_quality_repaired","price_source":"Songdaiki/stock-web","notes":"Memory tester/customer-quality proxy produced high MFE90 with shallow entry MAE. Because a 2024-07-31 corporate-action candidate exists after entry, this is positive-watch only before patch."}
{"row_type":"case","case_id":"C08_R2L92_080580_OH_KEYINS_TEST_SOCKET_THEME","symbol":"080580","company_name":"오킨스전자","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_THEME_VOLATILITY_WITHOUT_DURABLE_CUSTOMER_ORDER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-TestSocketThemeVolatilityNoDurableCustomerOrderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub20_MFE_deep_MAE_no_durable_customer_order_bridge","current_profile_verdict":"current_profile_false_positive_if_test_socket_theme_volatility_overcredited","price_source":"Songdaiki/stock-web","notes":"Test-socket theme volatility had sub-20 MFE and then deep MAE without durable customer/order, design-in, delivery or margin bridge."}
{"row_type":"case","case_id":"C08_R2L92_237750_PNC_CROSSLABEL_PRICE_MFE","symbol":"237750","company_name":"피앤씨테크","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"CROSSLABEL_DIGITAL_GRID_PRICE_MFE_WITHOUT_SEMI_CUSTOMER_QUALITY_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DigitalGridRelayPriceMFE-NoSemiCustomerQualityBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"score_price_alignment":"counterexample_price_MFE_deep_MAE_no_semi_customer_quality_bridge","current_profile_verdict":"current_profile_false_positive_if_cross_label_price_MFE_overcredited","price_source":"Songdaiki/stock-web","notes":"Digital-grid/protection-relay vocabulary can generate MFE, but it does not prove C08 semiconductor customer quality. Use only as cross-label 4B stress, not positive C08 evidence."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 092870 엑시콘 — memory tester / customer-quality / order bridge positive-watch

Entry row: `2024-02-28 c=17930`.
Observed path: entry low `2024-02-28 l=17070`, peak `2024-04-02 h=35400`, and later drawdown to `2024-11-14 l=9800`.
A 2024-07-31 corporate-action candidate exists after the selected entry, so this remains data-quality watch.

```jsonl
{"row_type":"trigger","trigger_id":"R2L92_C08_092870_20240228_STAGE2_MEMORY_TESTER_CUSTOMER_QUALITY","case_id":"C08_R2L92_092870_EXICON_MEMORY_TESTER_ORDER","symbol":"092870","company_name":"엑시콘","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMORY_TESTER_CUSTOMER_QUALITY_ORDER_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test;data_quality_watch","trigger_type":"Stage2-Actionable-MemoryTesterCustomerQualityOrderBridge-PositiveWatch","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":17930.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_memory_tester_customer_quality_order_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; memory tester customer qualification, design-in/order, delivery and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["memory_tester_exposure_proxy","customer_quality_proxy","order_conversion_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_qualification_source_pending","order_or_design_in_source_pending","delivery_schedule_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","2024_CA_candidate_data_quality_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv","profile_path":"atlas/symbol_profiles/092/092870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":97.43,"MFE_90D_pct":97.43,"MFE_180D_pct":97.43,"MAE_30D_pct":-4.80,"MAE_90D_pct":-4.80,"MAE_180D_pct":-45.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-02","peak_price":35400.0,"max_drawdown_low_date":"2024-11-14","max_drawdown_low":9800.0,"drawdown_after_peak_pct":-72.32,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_customer_qualification_order_delivery_margin_cash_evidence_and_2024_CA_data_quality_repair","four_b_evidence_type":["price_extension_watch","2024_CA_candidate_data_quality_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_low_entry_MAE_but_2024_CA_data_quality_watch","current_profile_verdict":"current_profile_correct_if_customer_qualification_order_delivery_margin_cash_bridge_required_and_data_quality_repaired","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024-07-31_corporate_action_candidate_after_entry_data_quality_watch"],"corporate_action_window_status":"selected_entry_before_2024-07-31_candidate; data_quality_watch","same_entry_group_id":"092870_2024-02-28_17930","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C08 can allow Stage2/Yellow-watch when tester strength is tied to customer qualification, order/design-in, delivery, margin and cash conversion. Green requires exact evidence and data-quality repair."}
```

### 6.2 080580 오킨스전자 — test-socket theme volatility without durable customer-order bridge

Entry row: `2024-01-22 c=12930`.
Observed path: early high `2024-01-23 h=14910`, then deep decline to `2024-10-24 l=5500` and later `2024-12-09 l=3685`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L92_C08_080580_20240122_STAGE2_FALSE_POSITIVE_TEST_SOCKET_VOLATILITY","case_id":"C08_R2L92_080580_OH_KEYINS_TEST_SOCKET_THEME","symbol":"080580","company_name":"오킨스전자","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_THEME_VOLATILITY_WITHOUT_DURABLE_CUSTOMER_ORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-TestSocketThemeVolatilityNoDurableCustomerOrderBridge","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":12930.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_test_socket_theme_volatility_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; test-socket/HBM keyword strength treated as insufficient without durable customer design-in, repeat order, delivery, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["test_socket_keyword","relative_strength_spike","HBM_or_advanced_package_vocabulary"],"stage3_evidence_fields":["durable_customer_order_missing","design_in_missing","delivery_schedule_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["sub20_MFE","customer_order_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv","profile_path":"atlas/symbol_profiles/080/080580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.31,"MFE_90D_pct":15.31,"MFE_180D_pct":15.31,"MAE_30D_pct":-23.05,"MAE_90D_pct":-40.06,"MAE_180D_pct":-57.46,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-23","peak_price":14910.0,"max_drawdown_low_date":"2024-10-24","max_drawdown_low":5500.0,"drawdown_after_peak_pct":-63.11,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"test_socket_theme_volatility_without_customer_design_in_order_delivery_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["sub20_MFE","customer_order_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub20_MFE_deep_MAE_no_durable_customer_order_bridge","current_profile_verdict":"current_profile_false_positive_if_test_socket_theme_volatility_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"080580_2024-01-22_12930","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C08 should not promote socket-theme volatility without durable customer design-in/order, delivery, margin and cash evidence. Sub-20 MFE and deep MAE force Watch/4B routing."}
```

### 6.3 237750 피앤씨테크 — cross-label digital-grid price MFE without semiconductor customer-quality bridge

Entry row: `2024-01-02 c=5610`.
Observed path: price high `2024-05-08 h=7640`, but later low `2024-12-09 l=3280`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L92_C08_237750_20240102_STAGE2_FALSE_POSITIVE_CROSSLABEL_GRID_MFE","case_id":"C08_R2L92_237750_PNC_CROSSLABEL_PRICE_MFE","symbol":"237750","company_name":"피앤씨테크","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"CROSSLABEL_DIGITAL_GRID_PRICE_MFE_WITHOUT_SEMI_CUSTOMER_QUALITY_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;cross_label_price_MFE_stress_test","trigger_type":"Stage2-FalsePositive-DigitalGridRelayPriceMFE-NoSemiCustomerQualityBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":5610.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_digital_grid_relay_price_MFE_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; digital-grid/protection-relay price MFE treated as cross-label stress and insufficient for C08 without semiconductor customer qualification, socket/test order, delivery and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["cross_label_digital_grid_keyword","price_MFE","relay_protection_equipment_vocabulary"],"stage3_evidence_fields":["semi_customer_qualification_missing","test_socket_order_missing","delivery_schedule_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_MFE","cross_label_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237750/2024.csv","profile_path":"atlas/symbol_profiles/237/237750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.28,"MFE_90D_pct":36.19,"MFE_180D_pct":36.19,"MAE_30D_pct":-2.32,"MAE_90D_pct":-5.70,"MAE_180D_pct":-41.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-08","peak_price":7640.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":3280.0,"drawdown_after_peak_pct":-57.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.12,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"cross_label_digital_grid_price_MFE_without_semi_customer_quality_order_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only_MFE","cross_label_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_MFE_deep_MAE_no_semi_customer_quality_bridge","current_profile_verdict":"current_profile_false_positive_if_cross_label_price_MFE_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["cross_label_C02_like_row_used_only_as_C08_false_positive_stress"],"corporate_action_window_status":"clean","same_entry_group_id":"237750_2024-01-02_5610","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"do_not_count_as_new_case":false,"current_profile_residual":"C08 should not count price MFE from a non-semi customer-quality label as test/socket validation. Customer qualification, socket/test order, delivery, margin and cash evidence must be exact-repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L92_092870_EXICON_MEMORY_TESTER_ORDER","trigger_id":"R2L92_C08_092870_20240228_STAGE2_MEMORY_TESTER_CUSTOMER_QUALITY","symbol":"092870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C08 requires customer qualification, design-in/order, delivery schedule, ASP/mix, margin and cash bridge rather than test/socket label alone","raw_component_scores_before":{"customer_quality_score":13,"design_in_order_score":12,"memory_test_exposure_score":13,"delivery_schedule_score":10,"ASP_mix_score":9,"margin_bridge_score":10,"cash_conversion_score":7,"relative_strength_score":16,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch/DataQualityWatch","raw_component_scores_after":{"customer_quality_score":16,"design_in_order_score":15,"memory_test_exposure_score":16,"delivery_schedule_score":12,"ASP_mix_score":11,"margin_bridge_score":12,"cash_conversion_score":9,"relative_strength_score":17,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":87,"stage_label_after":"Stage3-Yellow/Green-candidate-watch/DataQualityWatch","component_delta_explanation":"Customer-quality/order bridge plus high MFE90 supports Yellow/Green-candidate watch; exact evidence and 2024 corporate-action repair block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L92_080580_OH_KEYINS_TEST_SOCKET_THEME","trigger_id":"R2L92_C08_080580_20240122_STAGE2_FALSE_POSITIVE_TEST_SOCKET_VOLATILITY","symbol":"080580","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_scope":"current_default_proxy","profile_hypothesis":"test-socket theme volatility without durable customer order and margin bridge should be blocked","raw_component_scores_before":{"customer_quality_score":2,"design_in_order_score":0,"memory_test_exposure_score":2,"delivery_schedule_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":8,"valuation_repricing_score":3,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_quality_score":0,"design_in_order_score":0,"memory_test_exposure_score":1,"delivery_schedule_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-26,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-20 MFE and deep MAE convert socket-theme strength into missing customer-order bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L92_237750_PNC_CROSSLABEL_PRICE_MFE","trigger_id":"R2L92_C08_237750_20240102_STAGE2_FALSE_POSITIVE_CROSSLABEL_GRID_MFE","symbol":"237750","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_scope":"current_default_proxy","profile_hypothesis":"cross-label price MFE without semiconductor customer-quality evidence should remain Watch/4B","raw_component_scores_before":{"customer_quality_score":0,"design_in_order_score":0,"memory_test_exposure_score":0,"delivery_schedule_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":12,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_quality_score":0,"design_in_order_score":0,"memory_test_exposure_score":0,"delivery_schedule_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Price MFE is not C08 validation without semiconductor customer qualification/order evidence."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L92_C08_P0_CURRENT","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C08 needs explicit customer qualification, design-in/order, delivery, ASP/mix, margin/cash and cross-label price-MFE taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":49.64,"avg_MAE90_pct":-16.85,"avg_MFE180_pct":49.64,"avg_MAE180_pct":-48.11,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.71,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C08_customer_qualification_order_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L92_C08_P1_SECTOR_SPECIFIC","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_id":"P1_L2_test_socket_customer_quality_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 test/socket signals need customer qualification, design-in/order, delivery schedule, repeat order, ASP/mix, margin or cash conversion before Stage2-Actionable","changed_axes":["customer_quality_required","design_in_order_required","cross_label_price_MFE_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_qualification_design_in_order_delivery_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":49.64,"avg_MAE90_pct":-16.85,"avg_MFE180_pct":49.64,"avg_MAE180_pct":-48.11,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L92_C08_P2_CANONICAL","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_id":"P2_C08_customer_quality_order_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C08 should reward customer-quality-to-order mechanics, not test/socket vocabulary or price MFE","changed_axes":["C08_customer_qualification_order_delivery_margin_cash_bridge_required","C08_test_socket_theme_volatility_local_4B_guard","C08_cross_label_price_MFE_not_customer_quality_validation_guard","C08_2024_CA_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_qualification_or_design_in_order_plus_delivery_or_margin_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":49.64,"avg_MAE90_pct":-16.85,"avg_MFE180_pct":49.64,"avg_MAE180_pct":-48.11,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L92_C08_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_id":"P3_C08_sub20_or_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If customer-quality/order bridge is missing, MFE90<20 or MAE180<=-35 should block Yellow/Green and route to Watch/4B","changed_axes":["C08_sub20_MFE_guardrail","C08_deep_MAE_4B_guardrail","C08_price_MFE_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_MAE180_le_minus_35); high_MFE_without_bridge_not_positive"},"eligible_trigger_count":3,"avg_MFE90_pct":49.64,"avg_MAE90_pct":-16.85,"avg_MFE180_pct":49.64,"avg_MAE180_pct":-48.11,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_MEMORY_TESTER_POSITIVE_VS_SOCKET_CROSSLABEL_PRICE_MFE_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":49.64,"avg_MAE90_pct":-16.85,"avg_MFE180_pct":49.64,"avg_MAE180_pct":-48.11,"stage2_hit_rate_MFE90_ge20":0.67,"price_MFE_without_bridge_counterexample_count":1,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus35":0.67,"interpretation":"C08 needs bridge discipline. 엑시콘 shows memory tester/customer-quality/order bridge can support Yellow/Green-candidate-watch after data-quality repair, while 오킨스전자 and 피앤씨테크 show socket-theme volatility or cross-label price MFE should not be promoted without customer qualification, design-in/order, delivery, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"092870","trigger_type":"Stage2-Actionable-MemoryTesterCustomerQualityOrderBridge-PositiveWatch","entry_date":"2024-02-28","stage2_to_90D_outcome":"good_stage2_high_MFE_low_entry_MAE_data_quality_watch","stage2_to_180D_outcome":"positive_customer_quality_bridge_but_CA_data_quality_and_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when tester strength is tied to customer qualification/order/delivery/margin bridge; Green requires exact evidence and 2024 CA repair."}
{"row_type":"stage_transition_summary","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"080580","trigger_type":"Stage2-FalsePositive-TestSocketThemeVolatilityNoDurableCustomerOrderBridge","entry_date":"2024-01-22","stage2_to_90D_outcome":"bad_stage2_sub20_MFE_deep_MAE","stage2_to_180D_outcome":"failed_socket_theme_volatility_no_customer_order_bridge","MFE90_ge20":false,"MAE180_le_minus35":true,"transition_note":"Test-socket theme volatility without durable design-in/order and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"237750","trigger_type":"Stage2-FalsePositive-DigitalGridRelayPriceMFE-NoSemiCustomerQualityBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"price_MFE_without_semi_customer_quality_bridge","stage2_to_180D_outcome":"failed_cross_label_price_MFE_deep_MAE","MFE90_ge20":true,"MAE180_le_minus35":true,"transition_note":"Cross-label price MFE without semiconductor customer-quality/order evidence should remain 4B-watch, not positive C08 evidence."}
{"row_type":"residual_contribution","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","residual_type":"test_socket_cross_label_price_MFE_overcredit_without_customer_qualification_order_margin_cash_bridge","contribution":"Adds two C08 4B counterexamples against one memory tester customer-quality positive-watch, avoiding C08 top-covered and recent R2 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMORY_TEST_EQUIPMENT_CUSTOMER_QUALITY_BRIDGE_VS_TEST_SOCKET_THEME_PRICE_MFE_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C08 now has non-top-symbol memory tester customer-quality positive-watch and two socket/cross-label weak-bridge counterexamples; next R2 C08 loops should exact-URL repair customer qualification, design-in/order, delivery schedule, repeat order, ASP/mix, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_customer_qualification_order_delivery_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"092870 worked when memory tester/customer-quality proxy existed; 080580 and 237750 failed when price action lacked durable semiconductor customer-quality/order evidence."}
{"row_type":"shadow_weight","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_test_socket_theme_volatility_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"080580 showed sub-20 MFE and deep MAE when test-socket vocabulary was not tied to durable customer design-in/order and margin evidence."}
{"row_type":"shadow_weight","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_cross_label_price_MFE_not_customer_quality_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"237750 shows MFE90 above 20 should not count as C08 positive evidence when the bridge is cross-label and no semi customer-quality/order evidence exists."}
{"row_type":"shadow_weight","round":"R2","loop":"92","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_2024_CA_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"092870 has a 2024-07-31 corporate-action candidate after selected entry, so patch consideration needs price-path/evidence repair even though the residual price path is useful."}
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
  - test_socket_theme_volatility_overcredit
  - cross_label_price_MFE_overcredit
  - customer_qualification_bridge_missing
  - design_in_order_delivery_margin_bridge_missing
  - 2024_CA_data_quality_watch
new_axis_proposed:
  - C08_customer_qualification_order_delivery_margin_cash_bridge_required_shadow_only
  - C08_test_socket_theme_volatility_local_4B_guard_shadow_only
  - C08_cross_label_price_MFE_not_customer_quality_validation_guard_shadow_only
  - C08_2024_CA_data_quality_guard_shadow_only
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

## 12. Data-quality caveat

All selected triggers use Stock-Web tradable raw OHLC rows.
`092870` has a 2024-07-31 corporate-action candidate after the selected 2024-02-28 entry and must remain data-quality-watch before production patching.
`080580` has older 2021 corporate-action candidates before the selected 2024 window.
`237750` has no corporate-action candidate in the profile, but it is cross-label stress and must not be double-counted as a C02 contribution from this MD.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 092870
cross_label_stress_only = true for 237750
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
3. Confirm R2 / L2 / C08 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C08 top-covered symbols
   - previous R2 loop85 C06 symbols
   - previous R2 loop86 C07 symbols
   - previous R2 loop87 C08 symbols
   - previous R2 loop88 C09 symbols
   - previous R2 loop89 C10 symbols
   - previous R2 loop90 C06 symbols
   - previous R2 loop91 C07 symbols
6. Confirm stale R1/C02 file generation and touched 007610/065770/037030 candidates are not ingested from this MD.
7. Keep 092870 in 2024 corporate-action data-quality watch before patch consideration.
8. Treat 237750 as cross-label C08 failure-mode stress only, not as a duplicate C02 contribution.
9. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C08-scoped safe patch candidates:
   - C08_customer_qualification_order_delivery_margin_cash_bridge_required
   - C08_test_socket_theme_volatility_local_4B_guard
   - C08_cross_label_price_MFE_not_customer_quality_validation_guard
   - C08_2024_CA_data_quality_guard
10. Do not loosen Stage3-Green.
11. Do not use future MFE/MAE in runtime scoring.
12. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 92
next_round = R3
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive-watch, 2 counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.
```
