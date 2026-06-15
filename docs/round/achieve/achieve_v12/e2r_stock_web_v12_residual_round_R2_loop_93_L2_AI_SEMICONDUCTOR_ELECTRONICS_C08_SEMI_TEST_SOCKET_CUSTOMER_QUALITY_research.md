# E2R Stock-Web v12 Residual Research — R2 Loop 93 / L2 / C08

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 93
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: IC_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_VS_SOCKET_PROBE_PRICE_SPIKE_DECAY
sector: AI / semiconductor / test socket / probe card / consumables / customer qualification / repeat demand / margin / cash conversion
output_file: e2r_stock_web_v12_residual_round_R2_loop_93_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after recent loop93 expansions in C09, C01, C07, C06, C10, C11, C19, C27, C24, C12, C13, C17, C23 and C28.

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

No-Repeat Index Priority 0 snapshot used as duplicate-avoidance ledger:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY = 14 rows / need_to_30 = 16
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF = 15 rows
C01_ORDER_BACKLOG_MARGIN_BRIDGE = 16 rows
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH = 18 rows
```

Although C08 was expanded once in the local loop92 stream, it remains the thinnest raw Priority-0 archetype. This run therefore returns to C08, while avoiding the previous C08 symbol families.

Avoided recent R2/C08 and adjacent semiconductor loop symbols:

```text
R2 loop87 C08: 232140, 425420, 098120
R2 loop92 C08: 092870, 080580, 237750
R2 loop93 C09: 036930, 322310, 140860
R2 loop93 C07: 031980, 110990, 067310
R2 loop93 C06: 402340, 195870, 222800
R2 loop93 C10: 281820, 036200, 101160
```

Selected symbols:

```text
058470, 095340, 131290
```

The selected pocket is:

```text
IC test socket / consumables customer-quality repeat-demand bridge positive-watch
vs
test-socket acquisition / price-MFE without durable customer qualification and margin bridge
vs
probe-card / test-interface post-spike price path without renewal/revision and margin-cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"058470","company_name":"리노공업","profile_path":"atlas/symbol_profiles/058/058470.json","first_date":"2001-12-18","last_date":"2026-02-20","trading_day_count":5952,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2013-06-13","2013-07-08","2025-04-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical candidates are before selected 2024 window; future 2025 candidate is outside the selected forward window. Selected 2024 window is usable for residual price-path analysis.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; future_candidate_watch_only"}
{"row_type":"price_source_validation","symbol":"095340","company_name":"ISC","profile_path":"atlas/symbol_profiles/095/095340.json","first_date":"2007-10-01","last_date":"2026-02-20","trading_day_count":4535,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2014-12-26","2023-10-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
{"row_type":"price_source_validation","symbol":"131290","company_name":"티에스이","profile_path":"atlas/symbol_profiles/131/131290.json","first_date":"2011-01-05","last_date":"2026-02-20","trading_day_count":3719,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2011-04-05","2011-04-28"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 window. Market segment changes from KOSDAQ GLOBAL to KOSDAQ after 2024-06-14; keep market-segment watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; market_segment_change_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"058470","trigger_type":"Stage2-Actionable-ICTestSocketCustomerQualityRepeatDemandBridge-PositiveWatch","entry_date":"2024-02-13","duplicate_status":"new C08 symbol/trigger/date combination outside recent C08 loop87/loop92 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"095340","trigger_type":"Stage2-FalsePositive-TestSocketPriceMFEWithoutDurableCustomerQualificationMarginBridge","entry_date":"2024-03-08","duplicate_status":"new C08 symbol/trigger/date combination outside recent C08 loop87/loop92 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"131290","trigger_type":"Stage2-FalsePositive-ProbeCardTestInterfacePostSpikeNoRenewalRevisionMarginBridge","entry_date":"2024-04-26","duplicate_status":"new C08 symbol/trigger/date combination outside recent C08 loop87/loop92 symbols; market-segment-change watch"}
```

## 4. Research question

C08 is not “테스트 소켓/반도체 부품 단어가 있다.”
The useful signal must prove the customer-quality-to-repeat-demand chain:

```text
customer qualification / design-in
repeat consumable demand
socket/probe/test-interface relevance to actual customer process
shipment or PO conversion
replacement cycle / consumable pull
ASP / mix quality
gross-margin / operating-margin bridge
working-capital discipline
cash conversion
price strength not merely post-theme MFE
```

A test socket headline without this bridge is a probe touching a pad but not passing qualification. E2R needs the pass result, the repeat order, the ASP/mix, the margin and the cash.

Residual question:

```text
Can C08 distinguish:
1. IC test socket / consumables customer-quality bridge with strong MFE and controlled entry MAE,
2. test-socket price-MFE row that decays when durable qualification and margin bridge are missing,
3. probe-card/test-interface post-spike entry that fails when renewal/revision evidence and cash bridge are absent?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C08_R2L93_058470_LEENO_SOCKET_REPEAT","symbol":"058470","company_name":"리노공업","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"IC_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ICTestSocketCustomerQualityRepeatDemandBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"score_price_alignment":"positive_watch_MFE90_ge25_controlled_MAE_but_late_drawdown","current_profile_verdict":"current_profile_correct_if_customer_qualification_repeat_demand_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"IC test socket/customer-quality repeat-demand proxy produced MFE90 above 25 with controlled early MAE. Later drawdown and future-candidate watch keep Green strict until exact customer/repeat-demand evidence is repaired."}
{"row_type":"case","case_id":"C08_R2L93_095340_ISC_PRICE_MFE_DECAY","symbol":"095340","company_name":"ISC","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PRICE_MFE_WITHOUT_DURABLE_CUSTOMER_QUALIFICATION_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-TestSocketPriceMFEWithoutDurableCustomerQualificationMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub15_MFE_deep_MAE_no_durable_customer_qualification_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_test_socket_price_MFE_overcredited","price_source":"Songdaiki/stock-web","notes":"Test socket / customer-quality vocabulary around the March price spike had only sub-15 MFE and later deep MAE when durable qualification, repeat order, margin and cash bridge were missing."}
{"row_type":"case","case_id":"C08_R2L93_131290_TSE_PROBE_POST_SPIKE_DECAY","symbol":"131290","company_name":"티에스이","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PROBE_CARD_TEST_INTERFACE_POST_SPIKE_WITHOUT_RENEWAL_REVISION_MARGIN_BRIDGE","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ProbeCardTestInterfacePostSpikeNoRenewalRevisionMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_post_spike_low_MFE_deep_MAE_market_segment_watch_no_renewal_revision_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_probe_testinterface_post_spike_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Probe card / test-interface vocabulary after April spike had low forward MFE and deep drawdown without renewal/revision/margin evidence. Market-segment change keeps data-quality watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 058470 리노공업 — IC test socket / customer-quality repeat-demand bridge

Entry row: `2024-02-13 c=219000`.
Observed path: local high `2024-03-15 h=266500`, full-window high `2024-04-04 h=278500`, and later drawdown to `2024-11-14 l=143300`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C08_058470_20240213_STAGE2_IC_TEST_SOCKET_REPEAT","case_id":"C08_R2L93_058470_LEENO_SOCKET_REPEAT","symbol":"058470","company_name":"리노공업","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"IC_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ICTestSocketCustomerQualityRepeatDemandBridge-PositiveWatch","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":219000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_IC_test_socket_customer_quality_repeat_demand_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; IC test socket qualification, repeat consumable demand, ASP/mix, margin and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["customer_quality_proxy","repeat_consumable_demand_proxy","test_socket_process_relevance_proxy","relative_strength_after_reset"],"stage3_evidence_fields":["exact_customer_qualification_source_pending","repeat_order_source_pending","ASP_mix_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["MFE90_ge25_watch","late_drawdown_watch","Green_exact_evidence_watch","future_candidate_watch"],"stage4c_evidence_fields":["customer_quality_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.69,"MFE_90D_pct":27.17,"MFE_180D_pct":27.17,"MAE_30D_pct":-10.64,"MAE_90D_pct":-10.64,"MAE_180D_pct":-21.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-04","peak_price":278500.0,"max_drawdown_low_date":"2024-11-14","max_drawdown_low":143300.0,"drawdown_after_peak_pct":-48.55,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_customer_qualification_repeat_order_ASP_margin_cash_evidence_and_late_drawdown_review","four_b_evidence_type":["MFE90_ge25_watch","late_drawdown_watch","Green_exact_evidence_watch","future_candidate_watch"],"four_c_protection_label":"customer_quality_break_watch_only","trigger_outcome_label":"positive_watch_MFE90_ge25_controlled_MAE_but_late_drawdown","current_profile_verdict":"current_profile_correct_if_customer_qualification_repeat_demand_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["future_2025-04-25_candidate_watch_only"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_2024_window_usable; future_candidate_watch","same_entry_group_id":"058470_2024-02-13_219000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"do_not_count_as_new_case":false,"current_profile_residual":"C08 can allow Yellow/positive-watch when test-socket strength is tied to customer qualification, repeat consumable demand, ASP/mix, margin and cash conversion. Late drawdown and source-proxy evidence block automatic Green."}
```

### 6.2 095340 ISC — test-socket price MFE without durable qualification / margin bridge

Entry row: `2024-03-08 c=95000`, after the March socket / semiconductor quality spike.
Observed path: high `2024-03-28 h=108000`, followed by a long decline to `2024-09-09 l=44950`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C08_095340_20240308_STAGE2_FALSE_POSITIVE_SOCKET_MFE_DECAY","case_id":"C08_R2L93_095340_ISC_PRICE_MFE_DECAY","symbol":"095340","company_name":"ISC","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PRICE_MFE_WITHOUT_DURABLE_CUSTOMER_QUALIFICATION_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_MFE_not_qualification_validation","trigger_type":"Stage2-FalsePositive-TestSocketPriceMFEWithoutDurableCustomerQualificationMarginBridge","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":95000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_test_socket_price_MFE_customer_quality_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; socket/customer-quality vocabulary and price-MFE treated as insufficient without durable customer qualification, repeat order, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["test_socket_keyword","price_MFE","customer_quality_vocabulary"],"stage3_evidence_fields":["durable_customer_qualification_missing","repeat_order_missing","margin_cash_bridge_missing","revision_visibility_missing"],"stage4b_evidence_fields":["sub15_MFE","deep_MAE","price_MFE_not_qualification_validation"],"stage4c_evidence_fields":["customer_loss_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.68,"MFE_90D_pct":13.68,"MFE_180D_pct":13.68,"MAE_30D_pct":-16.21,"MAE_90D_pct":-36.74,"MAE_180D_pct":-52.68,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000.0,"max_drawdown_low_date":"2024-09-09","max_drawdown_low":44950.0,"drawdown_after_peak_pct":-58.38,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"socket_price_MFE_without_durable_customer_qualification_repeat_order_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["sub15_MFE","deep_MAE","price_MFE_not_qualification_validation"],"four_c_protection_label":"customer_loss_watch_only","trigger_outcome_label":"counterexample_sub15_MFE_deep_MAE_no_durable_customer_qualification_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_test_socket_price_MFE_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"095340_2024-03-08_95000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C08 should not count price-MFE or socket vocabulary as customer-quality validation unless customer qualification, repeat order, margin and cash evidence are exact-repaired. Deep MAE forces Watch/4B routing."}
```

### 6.3 131290 티에스이 — probe-card/test-interface post-spike entry without renewal / revision bridge

Entry row: `2024-04-26 c=79000`, after the April probe/test-interface price burst.
Observed path: later high `2024-05-03 h=87800`, followed by decline to `2024-09-09 l=40350` and `2024-12-09 l=35000`. Market segment changes from KOSDAQ GLOBAL to KOSDAQ after `2024-06-14`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C08_131290_20240426_STAGE2_FALSE_POSITIVE_PROBE_POST_SPIKE","case_id":"C08_R2L93_131290_TSE_PROBE_POST_SPIKE_DECAY","symbol":"131290","company_name":"티에스이","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PROBE_CARD_TEST_INTERFACE_POST_SPIKE_WITHOUT_RENEWAL_REVISION_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;post_spike_entry_guard;data_quality_watch","trigger_type":"Stage2-FalsePositive-ProbeCardTestInterfacePostSpikeNoRenewalRevisionMarginBridge","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":79000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_probe_card_test_interface_post_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; probe-card/test-interface vocabulary treated as insufficient without renewal, customer revision, repeat demand, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["probe_card_keyword","test_interface_vocabulary","post_spike_relative_strength"],"stage3_evidence_fields":["customer_revision_missing","renewal_repeat_order_missing","margin_cash_bridge_missing","market_segment_repair_pending"],"stage4b_evidence_fields":["low_forward_MFE","deep_MAE","post_spike_entry_watch","market_segment_change_watch"],"stage4c_evidence_fields":["customer_quality_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.14,"MFE_90D_pct":11.14,"MFE_180D_pct":11.14,"MAE_30D_pct":-22.91,"MAE_90D_pct":-48.92,"MAE_180D_pct":-55.70,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":87800.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":35000.0,"drawdown_after_peak_pct":-60.14,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"probe_testinterface_post_spike_without_customer_revision_repeat_order_margin_cash_bridge_should_be_4B_watch_not_positive; market_segment_change_requires_repair","four_b_evidence_type":["low_forward_MFE","deep_MAE","post_spike_entry_watch","market_segment_change_watch"],"four_c_protection_label":"customer_quality_break_watch_only","trigger_outcome_label":"counterexample_post_spike_low_MFE_deep_MAE_market_segment_watch_no_renewal_revision_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_probe_testinterface_post_spike_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_segment_change_watch_KOSDAQ_GLOBAL_to_KOSDAQ_after_2024-06-14"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_usable; market_segment_change_watch","same_entry_group_id":"131290_2024-04-26_79000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C08 should not promote probe-card/test-interface post-spike vocabulary unless customer revision, renewal/repeat order, margin and cash evidence are repaired. Market-segment rows require data-quality repair."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L93_058470_LEENO_SOCKET_REPEAT","trigger_id":"R2L93_C08_058470_20240213_STAGE2_IC_TEST_SOCKET_REPEAT","symbol":"058470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C08 requires customer qualification, repeat consumable demand, ASP/mix, margin and cash bridge rather than test-socket vocabulary alone","raw_component_scores_before":{"customer_qualification_score":12,"repeat_consumable_demand_score":12,"test_socket_process_relevance_score":11,"customer_quality_score":11,"shipment_PO_score":9,"ASP_mix_score":9,"margin_bridge_score":10,"cash_conversion_score":8,"relative_strength_score":12,"valuation_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"customer_qualification_score":15,"repeat_consumable_demand_score":15,"test_socket_process_relevance_score":14,"customer_quality_score":13,"shipment_PO_score":11,"ASP_mix_score":11,"margin_bridge_score":12,"cash_conversion_score":10,"relative_strength_score":13,"valuation_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Customer-quality/repeat-demand bridge plus MFE90 supports Green-candidate watch; exact evidence and late drawdown repair block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L93_095340_ISC_PRICE_MFE_DECAY","trigger_id":"R2L93_C08_095340_20240308_STAGE2_FALSE_POSITIVE_SOCKET_MFE_DECAY","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_scope":"current_default_proxy","profile_hypothesis":"test-socket price MFE without durable qualification and margin bridge should be blocked","raw_component_scores_before":{"customer_qualification_score":2,"repeat_consumable_demand_score":1,"test_socket_process_relevance_score":3,"customer_quality_score":1,"shipment_PO_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":5,"valuation_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_qualification_score":0,"repeat_consumable_demand_score":0,"test_socket_process_relevance_score":1,"customer_quality_score":0,"shipment_PO_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-15 MFE and deep MAE require customer qualification, repeat order and margin/cash evidence before promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_R2L93_131290_TSE_PROBE_POST_SPIKE_DECAY","trigger_id":"R2L93_C08_131290_20240426_STAGE2_FALSE_POSITIVE_PROBE_POST_SPIKE","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_scope":"current_default_proxy","profile_hypothesis":"probe-card/test-interface post-spike vocabulary without renewal/revision and margin bridge should remain Watch/4B","raw_component_scores_before":{"customer_qualification_score":1,"repeat_consumable_demand_score":0,"test_socket_process_relevance_score":2,"customer_quality_score":0,"shipment_PO_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":5,"valuation_risk_score":-16,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"customer_qualification_score":0,"repeat_consumable_demand_score":0,"test_socket_process_relevance_score":0,"customer_quality_score":0,"shipment_PO_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_risk_score":-28,"theme_spike_risk":-24,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Post-spike low MFE, deep MAE and market-segment change require renewal/revision and margin/cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L93_C08_P0_CURRENT","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C08 needs explicit customer qualification, repeat consumable demand, renewal/revision, ASP/mix, margin/cash and data-quality taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":17.33,"avg_MAE90_pct":-32.10,"avg_MFE180_pct":17.33,"avg_MAE180_pct":-43.43,"false_positive_rate":0.67,"data_quality_watch_count":1,"score_return_alignment_verdict":"mixed_without_C08_customer_qualification_repeat_order_margin_cash_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C08_P1_SECTOR_SPECIFIC","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_id":"P1_L2_test_socket_customer_quality_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 test/socket signals need customer qualification, repeat order, shipment conversion, ASP/mix, margin or cash conversion before Stage2-Actionable","changed_axes":["customer_qualification_required","repeat_order_required","price_MFE_penalty","market_segment_data_quality_guard"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_qualification_repeat_order_shipment_margin_or_cash_proxy"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C08_P2_CANONICAL","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_id":"P2_C08_customer_quality_repeat_order_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C08 should reward customer-quality/repeat-order mechanics, not socket/probe vocabulary or price MFE","changed_axes":["C08_customer_qualification_repeat_order_margin_cash_bridge_required","C08_socket_probe_price_MFE_local_4B_guard","C08_post_spike_entry_guard","C08_market_segment_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_qualification_or_repeat_order_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C08_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","profile_id":"P3_C08_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If customer/repeat-order bridge is missing, MFE90<15 or MAE90<=-20 blocks Yellow/Green and routes to Watch/4B","changed_axes":["C08_low_MFE_guardrail","C08_deep_MAE_guardrail","C08_price_MFE_not_qualification_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_15_or_MAE90_le_minus20)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate and transition rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"C08_IC_SOCKET_POSITIVE_VS_SOCKET_PROBE_SPIKE_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":17.33,"avg_MAE90_pct":-32.10,"avg_MFE180_pct":17.33,"avg_MAE180_pct":-43.43,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE90_le_minus20":0.67,"interpretation":"C08 needs customer-quality/repeat-demand discipline. 리노공업 shows IC test socket customer-quality repeat demand can support Yellow/Green-candidate-watch, while ISC and 티에스이 show socket/probe vocabulary or price-MFE should not be promoted without durable customer qualification, repeat order, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"058470","trigger_type":"Stage2-Actionable-ICTestSocketCustomerQualityRepeatDemandBridge-PositiveWatch","entry_date":"2024-02-13","stage2_to_90D_outcome":"positive_watch_MFE90_ge25_controlled_MAE","stage2_to_180D_outcome":"IC_socket_repeat_demand_bridge_but_late_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/Green-candidate when socket strength is tied to customer qualification, repeat demand, ASP/mix, margin and cash bridge; exact evidence required for Green."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"095340","trigger_type":"Stage2-FalsePositive-TestSocketPriceMFEWithoutDurableCustomerQualificationMarginBridge","entry_date":"2024-03-08","stage2_to_90D_outcome":"bad_stage2_sub15_MFE_deep_MAE","stage2_to_180D_outcome":"failed_socket_price_MFE_no_customer_qualification_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Socket price-MFE without durable qualification/repeat order and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"131290","trigger_type":"Stage2-FalsePositive-ProbeCardTestInterfacePostSpikeNoRenewalRevisionMarginBridge","entry_date":"2024-04-26","stage2_to_90D_outcome":"bad_stage2_post_spike_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_probe_testinterface_post_spike_no_renewal_revision_margin_bridge_market_segment_watch","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Probe/test-interface vocabulary after a spike without renewal/revision and margin bridge should remain Watch/4B; market-segment repair required."}
{"row_type":"residual_contribution","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","residual_type":"socket_probe_vocabulary_overcredit_without_customer_qualification_repeat_order_margin_cash_bridge","contribution":"Adds two C08 4B counterexamples against one IC test socket repeat-demand positive-watch, selected because C08 remains the thinnest Priority-0 archetype in the GitHub No-Repeat Index.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"IC_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_VS_SOCKET_PROBE_PRICE_SPIKE_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C08 now has one IC test socket customer-quality repeat-demand positive-watch and two socket/probe weak-bridge counterexamples; next C08 loops should exact-URL repair customer qualification, repeat consumable demand, shipment conversion, ASP/mix, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_customer_qualification_repeat_order_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"058470 worked as positive-watch when customer-quality/repeat-demand proxy existed; 095340 and 131290 failed when durable qualification/repeat-order evidence was missing."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_socket_probe_price_MFE_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"095340 and 131290 showed low/sub15 forward MFE or deep MAE when socket/probe vocabulary was not tied to customer qualification and margin evidence."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_post_spike_entry_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"131290 shows post-spike probe/test-interface vocabulary should not be promoted without fresh renewal/revision and cash evidence."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","axis":"C08_market_segment_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"131290 changes market segment after selected entry; production patching requires price-path/evidence repair."}
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
  - socket_price_MFE_overcredit
  - probe_testinterface_post_spike_overcredit
  - customer_qualification_bridge_missing
  - repeat_order_margin_cash_bridge_missing
  - market_segment_data_quality_watch
new_axis_proposed:
  - C08_customer_qualification_repeat_order_margin_cash_bridge_required_shadow_only
  - C08_socket_probe_price_MFE_local_4B_guard_shadow_only
  - C08_post_spike_entry_guard_shadow_only
  - C08_market_segment_data_quality_guard_shadow_only
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
`058470` has older 2013 corporate-action candidates before selected 2024 window and a future 2025 candidate outside selected forward window; selected 2024 window is usable.
`095340` has a 2023 corporate-action candidate before selected 2024 window; selected 2024 window is usable.
`131290` has old 2011 corporate-action candidates before 2024, but market segment changes from KOSDAQ GLOBAL to KOSDAQ after 2024-06-14; keep market-segment watch before patching.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for residual price-path analysis
evidence_url_pending = true
source_proxy_only = true
future_candidate_watch = true for 058470
market_segment_change_watch = true for 131290
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
3. Confirm R2 / L2 / C08 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop was selected by coverage-index-first because raw C08 remains the thinnest Priority-0 archetype.
6. Confirm this loop avoided:
   - previous R2 loop87 C08 symbols
   - previous R2 loop92 C08 symbols
   - recent R2 loop93 C09/C07/C06/C10 symbols
7. Confirm recently touched C28/C23/C17/C13/C12 candidate rows are not ingested from this MD.
8. Treat 058470 as Yellow/Green-candidate-watch only, not Green, until exact customer-qualification/repeat-order/margin/cash evidence is repaired.
9. Treat 095340 and 131290 as weak-bridge failure modes unless exact customer/repeat-order/margin/cash evidence is added later.
10. Keep 131290 in market-segment data-quality watch before patch consideration.
11. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C08-scoped safe patch candidates:
   - C08_customer_qualification_repeat_order_margin_cash_bridge_required
   - C08_socket_probe_price_MFE_local_4B_guard
   - C08_post_spike_entry_guard
   - C08_market_segment_data_quality_guard
12. Do not loosen Stage3-Green.
13. Do not use future MFE/MAE in runtime scoring.
14. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C08 again if strictly following raw index, otherwise C09/C01 depending on local-loop fatigue and newest reconciled No-Repeat Index
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 IC test-socket repeat-demand positive-watch, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.
```
