# E2R Stock-Web v12 Residual Research — R2 Loop 93 / L2 / C09

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 93
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_SEMI_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_METROLOGY_ORDER_BRIDGE_FALSE_OVERBLOCK
sector: AI / semiconductor / advanced equipment / ALD / overlay metrology / AFM metrology / valuation blowoff / order bridge / margin bridge
output_file: e2r_stock_web_v12_residual_round_R2_loop_93_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after completed `R13 loop 92`.

```text
selected_round = R2
selected_loop = 93
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

Reason for selecting C09 instead of mechanically continuing R1:

```text
v12 current scheduler = coverage_index_first
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
selected_archetype_drives_round = true
```

No-Repeat Index Priority 0 snapshot:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY = 14 rows
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF = 15 rows
C01_ORDER_BACKLOG_MARGIN_BRIDGE = 16 rows
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH = 18 rows
```

C08 was just expanded in loop92 by the local run stream. To avoid immediate same-archetype rematerialization, this loop selects the next thinnest Priority 0 archetype:

```text
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
research point = advanced equipment valuation overheat, price blowoff without order, 4B/4C transition
```

This loop avoids recent R2 loop symbols:

```text
R2 loop85 C06: 000660, 005930, 009150
R2 loop86 C07: 042700, 064760, 003160
R2 loop87 C08: 232140, 425420, 098120
R2 loop88 C09: 039030, 412350, 253590
R2 loop89 C10: 403870, 166090, 074600
R2 loop90 C06: 036540, 033170, 394280
R2 loop91 C07: 084370, 086390, 217190
R2 loop92 C08: 092870, 080580, 237750
```

Selected symbols:

```text
036930, 322310, 140860
```

The selected pocket is:

```text
advanced ALD / semiconductor equipment price blowoff without delivery-margin bridge
vs
overlay metrology price-MFE blowoff without durable customer-order bridge
vs
high-end AFM metrology customer/order bridge that should not be overblocked as simple valuation blowoff after reset
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"036930","company_name":"주성엔지니어링","profile_path":"atlas/symbol_profiles/036/036930.json","first_date":"1999-12-24","last_date":"2026-02-20","trading_day_count":6444,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2000-06-22"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidate exists long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"322310","company_name":"오로스테크놀로지","profile_path":"atlas/symbol_profiles/322/322310.json","first_date":"2021-02-24","last_date":"2026-02-20","trading_day_count":1223,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"140860","company_name":"파크시스템스","profile_path":"atlas/symbol_profiles/140/140860.json","first_date":"2015-12-17","last_date":"2026-02-20","trading_day_count":2494,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Market flag changes from KOSDAQ to KOSDAQ GLOBAL in 2025, outside selected 2024 window; selected window is usable.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"036930","trigger_type":"Stage2-4B-Validated-AdvancedALDEquipmentValuationBlowoffNoOrderDeliveryMarginBridge","entry_date":"2024-02-28","duplicate_status":"new C09 symbol/trigger/date combination outside recent R2 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"322310","trigger_type":"Stage2-FalsePositive-OverlayMetrologyPriceMFEBlowoffNoDurableCustomerOrderBridge","entry_date":"2024-02-27","duplicate_status":"new C09 symbol/trigger/date combination outside recent R2 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"140860","trigger_type":"Stage2-FalsePositive-OverbroadValuationBlowoffWouldMissAFMMetrologyOrderBridgeAfterReset","entry_date":"2024-04-23","duplicate_status":"new C09 symbol/trigger/date combination outside recent R2 loop symbols; false-overblock bridge repair case"}
```

## 4. Research question

C09 is not “고급 장비주가 많이 올랐다.”
The useful C09 guard must decide whether price is backed by an order-to-margin bridge or only by valuation heat.

The required chain is:

```text
named customer or application
customer qualification / process step relevance
order or delivery conversion
tool shipment / acceptance schedule
revision or revenue visibility
ASP / mix quality
gross-margin or operating-margin bridge
working-capital discipline
cash conversion
valuation discipline after the first price blowoff
```

A semiconductor equipment spike without this bridge is a vacuum chamber humming with no wafer loaded. The hum is real, but throughput, acceptance, margin and cash are still missing.

Residual question:

```text
Can C09 distinguish:
1. validated 4B blowoff where advanced equipment vocabulary and price spike lacked order/delivery/margin evidence,
2. price-MFE blowoff where metrology vocabulary failed to hold without durable customer-order bridge,
3. false-overblock case where high-end metrology had a reset and then a customer/order bridge, so broad valuation-blowoff blocking would be too blunt?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C09_R2L93_036930_JUSUNG_ALD_BLOWOFF_4B","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_ALD_EQUIPMENT_VALUATION_BLOWOFF_WITHOUT_ORDER_DELIVERY_MARGIN_BRIDGE","case_type":"validated_4B_blowoff_guard","positive_or_counterexample":"positive_risk_guard","best_trigger":"Stage2-4B-Validated-AdvancedALDEquipmentValuationBlowoffNoOrderDeliveryMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"valid_4B_low_MFE_deep_MAE_after_price_blowoff_no_order_bridge","current_profile_verdict":"current_profile_correct_if_valuation_blowoff_without_order_delivery_margin_routes_to_4B","price_source":"Songdaiki/stock-web","notes":"Advanced ALD/equipment price blowoff on 2024-02-28 had low forward MFE and then deep MAE. Without exact order, delivery, revision and margin evidence, C09 should route to Watch/4B."}
{"row_type":"case","case_id":"C09_R2L93_322310_AUROS_OVERLAY_METROLOGY_MFE_DECAY","symbol":"322310","company_name":"오로스테크놀로지","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"OVERLAY_METROLOGY_PRICE_MFE_WITHOUT_DURABLE_CUSTOMER_ORDER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-OverlayMetrologyPriceMFEBlowoffNoDurableCustomerOrderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_MFE_but_deep_MAE_no_durable_order_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_overlay_metrology_price_MFE_overcredited","price_source":"Songdaiki/stock-web","notes":"Overlay metrology vocabulary generated a price-MFE burst but later decayed deeply. Price-MFE should not validate C09 without durable customer order, delivery and margin/cash bridge."}
{"row_type":"case","case_id":"C09_R2L93_140860_PARKSYSTEMS_METROLOGY_FALSE_OVERBLOCK","symbol":"140860","company_name":"파크시스템스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"AFM_METROLOGY_CUSTOMER_ORDER_BRIDGE_FALSE_OVERBLOCK_AFTER_VALUATION_RESET","case_type":"false_overblock","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-OverbroadValuationBlowoffWouldMissAFMMetrologyOrderBridgeAfterReset","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_overblock_high_MFE_after_reset_if_metrology_order_bridge_exists","current_profile_verdict":"current_profile_false_positive_if_C09_guard_blocks_reset_plus_customer_order_bridge","price_source":"Songdaiki/stock-web","notes":"After a valuation reset, high-end AFM/metrology order-bridge proxy produced strong later MFE. C09 must not become a blanket advanced-equipment overblock; customer order/revenue bridge should override generic valuation-blowoff vocabulary."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 036930 주성엔지니어링 — advanced ALD/equipment valuation blowoff, validated 4B

Entry row: `2024-02-28 c=40000`, after a large equipment price-spike row.
Observed path: local high near `2024-04-08 h=41450`, then deterioration to `2024-09-24 l=24800`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C09_036930_20240228_STAGE2_4B_ALD_VALUATION_BLOWOFF","case_id":"C09_R2L93_036930_JUSUNG_ALD_BLOWOFF_4B","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_ALD_EQUIPMENT_VALUATION_BLOWOFF_WITHOUT_ORDER_DELIVERY_MARGIN_BRIDGE","loop_objective":"validated_4B_guard;valuation_blowoff_stress_test;canonical_archetype_rule_candidate","trigger_type":"Stage2-4B-Validated-AdvancedALDEquipmentValuationBlowoffNoOrderDeliveryMarginBridge","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":40000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_advanced_ALD_equipment_price_blowoff_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; advanced ALD/equipment price blowoff treated as insufficient without customer order, delivery schedule, revenue revision and margin/cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["advanced_ALD_equipment_keyword","relative_strength_blowoff","valuation_heat_proxy"],"stage3_evidence_fields":["customer_order_missing","delivery_schedule_missing","revision_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_forward_MFE","deep_MAE","valuation_blowoff_guard"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv","profile_path":"atlas/symbol_profiles/036/036930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.63,"MFE_90D_pct":3.63,"MFE_180D_pct":3.63,"MAE_30D_pct":-16.38,"MAE_90D_pct":-21.25,"MAE_180D_pct":-38.00,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":41450.0,"max_drawdown_low_date":"2024-09-24","max_drawdown_low":24800.0,"drawdown_after_peak_pct":-40.17,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"advanced_equipment_price_blowoff_without_order_delivery_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_forward_MFE","deep_MAE","valuation_blowoff_guard"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"valid_4B_low_MFE_deep_MAE_after_price_blowoff_no_order_bridge","current_profile_verdict":"current_profile_correct_if_valuation_blowoff_without_order_delivery_margin_routes_to_4B","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"036930_2024-02-28_40000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C09 should hard-route advanced-equipment valuation blowoff rows to 4B when exact order, delivery, revision and margin/cash bridge are missing and price path shows low MFE plus deep MAE."}
```

### 6.2 322310 오로스테크놀로지 — overlay metrology price-MFE blowoff without durable customer-order bridge

Entry row: `2024-02-27 c=37200`, after a metrology/advanced equipment price burst.
Observed path: local high `2024-02-27 h=40750`, then persistent decay to `2024-11-14 l=13360`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C09_322310_20240227_STAGE2_FALSE_POSITIVE_OVERLAY_METROLOGY_MFE","case_id":"C09_R2L93_322310_AUROS_OVERLAY_METROLOGY_MFE_DECAY","symbol":"322310","company_name":"오로스테크놀로지","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"OVERLAY_METROLOGY_PRICE_MFE_WITHOUT_DURABLE_CUSTOMER_ORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_MFE_not_order_validation","trigger_type":"Stage2-FalsePositive-OverlayMetrologyPriceMFEBlowoffNoDurableCustomerOrderBridge","trigger_date":"2024-02-27","entry_date":"2024-02-27","entry_price":37200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_overlay_metrology_price_MFE_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; overlay metrology / advanced equipment vocabulary and price-MFE treated as insufficient without durable customer order, delivery acceptance, revision and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["overlay_metrology_keyword","advanced_equipment_price_MFE","relative_strength_spike"],"stage3_evidence_fields":["durable_customer_order_missing","delivery_acceptance_missing","revenue_revision_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_MFE_without_bridge","deep_MAE","valuation_blowoff_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv","profile_path":"atlas/symbol_profiles/322/322310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.54,"MFE_90D_pct":9.54,"MFE_180D_pct":9.54,"MAE_30D_pct":-13.17,"MAE_90D_pct":-15.05,"MAE_180D_pct":-64.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":40750.0,"max_drawdown_low_date":"2024-11-14","max_drawdown_low":13360.0,"drawdown_after_peak_pct":-67.21,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"overlay_metrology_price_MFE_without_durable_customer_order_revision_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_MFE_without_bridge","deep_MAE","valuation_blowoff_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_MFE_but_deep_MAE_no_durable_order_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_overlay_metrology_price_MFE_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"322310_2024-02-27_37200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C09 should not count price-MFE from metrology vocabulary as positive validation unless durable customer order, delivery acceptance, revenue revision and margin/cash evidence are exact-repaired."}
```

### 6.3 140860 파크시스템스 — AFM/metrology customer-order bridge false-overblock after valuation reset

Entry row: `2024-04-23 c=140400`, after a valuation reset from early-year highs.
Observed path: high `2024-07-04 h=198600` within the forward window and later full-window high `2024-11-07 h=224000`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C09_140860_20240423_STAGE2_FALSE_OVERBLOCK_AFM_METROLOGY_ORDER","case_id":"C09_R2L93_140860_PARKSYSTEMS_METROLOGY_FALSE_OVERBLOCK","symbol":"140860","company_name":"파크시스템스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"AFM_METROLOGY_CUSTOMER_ORDER_BRIDGE_FALSE_OVERBLOCK_AFTER_VALUATION_RESET","loop_objective":"false_overblock_mining;counterexample_mining;green_strictness_stress_test","trigger_type":"Stage2-FalsePositive-OverbroadValuationBlowoffWouldMissAFMMetrologyOrderBridgeAfterReset","trigger_date":"2024-04-23","entry_date":"2024-04-23","entry_price":140400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_AFM_metrology_customer_order_reset_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; AFM/metrology customer order, acceptance, revenue visibility and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["AFM_metrology_order_proxy","valuation_reset_proxy","customer_quality_proxy","relative_strength_recovery"],"stage3_evidence_fields":["exact_customer_order_source_pending","delivery_acceptance_source_pending","revenue_visibility_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["false_overblock_watch","Green_exact_evidence_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv","profile_path":"atlas/symbol_profiles/140/140860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.49,"MFE_90D_pct":41.45,"MFE_180D_pct":59.54,"MAE_30D_pct":-0.93,"MAE_90D_pct":-0.93,"MAE_180D_pct":-0.93,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":224000.0,"max_drawdown_low_date":"2024-04-23","max_drawdown_low":139100.0,"drawdown_after_peak_pct":-18.75,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.69,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"do_not_overblock_after_valuation_reset_if_exact_customer_order_metrology_bridge_exists_but_Green_requires_source_repair","four_b_evidence_type":["false_overblock_watch","Green_exact_evidence_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"false_overblock_high_MFE_after_reset_if_metrology_order_bridge_exists","current_profile_verdict":"current_profile_false_positive_if_C09_guard_blocks_reset_plus_customer_order_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"140860_2024-04-23_140400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C09 should not become a blanket advanced-equipment overblock. If valuation has reset and customer order / metrology demand / revenue visibility / margin bridge exists, route to evidence repair rather than hard 4B."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L93_036930_JUSUNG_ALD_BLOWOFF_4B","trigger_id":"R2L93_C09_036930_20240228_STAGE2_4B_ALD_VALUATION_BLOWOFF","symbol":"036930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_scope":"current_default_proxy","profile_hypothesis":"C09 should block advanced equipment price blowoff when customer order, delivery, revision and margin bridge are missing","raw_component_scores_before":{"advanced_equipment_theme_score":8,"valuation_heat_score":16,"customer_order_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":1,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":12,"execution_risk_score":-18,"theme_spike_risk":-22,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/4B-Guard","raw_component_scores_after":{"advanced_equipment_theme_score":3,"valuation_heat_score":18,"customer_order_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"execution_risk_score":-30,"theme_spike_risk":-26,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Validated","component_delta_explanation":"Low MFE and deep MAE validate the valuation-blowoff 4B guard, not any positive stage."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L93_322310_AUROS_OVERLAY_METROLOGY_MFE_DECAY","trigger_id":"R2L93_C09_322310_20240227_STAGE2_FALSE_POSITIVE_OVERLAY_METROLOGY_MFE","symbol":"322310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_scope":"current_default_proxy","profile_hypothesis":"metrology price-MFE without durable customer order and margin bridge should remain Watch/4B","raw_component_scores_before":{"advanced_equipment_theme_score":6,"valuation_heat_score":13,"customer_order_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":8,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"advanced_equipment_theme_score":2,"valuation_heat_score":16,"customer_order_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"execution_risk_score":-28,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Price-MFE is not order/revision validation; deep MAE keeps this in 4B-watch."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L93_140860_PARKSYSTEMS_METROLOGY_FALSE_OVERBLOCK","trigger_id":"R2L93_C09_140860_20240423_STAGE2_FALSE_OVERBLOCK_AFM_METROLOGY_ORDER","symbol":"140860","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_scope":"current_default_proxy","profile_hypothesis":"after valuation reset, exact AFM/metrology customer order and revenue bridge should override broad blowoff blocking","raw_component_scores_before":{"advanced_equipment_theme_score":8,"valuation_heat_score":2,"customer_order_score":13,"delivery_acceptance_score":10,"revision_visibility_score":10,"ASP_mix_score":9,"margin_bridge_score":9,"cash_conversion_score":7,"relative_strength_score":12,"execution_risk_score":-5,"theme_spike_risk":-3,"information_confidence":4},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"advanced_equipment_theme_score":10,"valuation_heat_score":0,"customer_order_score":16,"delivery_acceptance_score":12,"revision_visibility_score":12,"ASP_mix_score":11,"margin_bridge_score":11,"cash_conversion_score":9,"relative_strength_score":13,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Reset plus customer-order bridge would be false-overblocked by a blunt C09 guard; exact evidence still blocks automatic Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L93_C09_P0_CURRENT","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails work if C09 separates price blowoff without order bridge from reset-plus-order false-overblock cases","eligible_trigger_count":3,"avg_MFE90_pct":18.21,"avg_MAE90_pct":-12.41,"avg_MFE180_pct":24.24,"avg_MAE180_pct":-34.34,"validated_4B_guard_count":1,"false_positive_price_MFE_count":1,"false_overblock_count":1,"score_return_alignment_verdict":"mixed_without_C09_order_bridge_vs_blowoff_override"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C09_P1_SECTOR_SPECIFIC","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_id":"P1_L2_advanced_equipment_blowoff_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 advanced equipment signals need customer order, delivery acceptance, revision visibility, ASP/mix, margin or cash before positive stage; valuation heat without bridge is 4B","changed_axes":["order_delivery_required","valuation_heat_4B_guard","reset_plus_order_override"],"changed_thresholds":{"hard_4B_gate":"valuation_heat_and_bridge_missing_and_(MFE90_lt_20_or_MAE180_le_minus25)","override_gate":"valuation_reset_plus_customer_order_or_delivery_bridge"},"eligible_trigger_count":3,"validated_4B_guard_count":1,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C09_P2_CANONICAL","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_id":"P2_C09_order_delivery_margin_vs_blowoff_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C09 should be a valuation-blowoff guard, not a blanket advanced-equipment veto","changed_axes":["C09_valuation_blowoff_no_order_4B_guard","C09_price_MFE_not_order_validation_guard","C09_reset_plus_customer_order_false_overblock_override"],"changed_thresholds":{"4B_gate":"order_bridge_missing_and_(MFE90_lt_20_or_MAE180_le_minus25)","override_gate":"reset_after_drawdown_plus_order_delivery_margin_bridge"},"eligible_trigger_count":3,"validated_4B_guard_count":1,"false_overblock_count":1,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C09_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_id":"P3_C09_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If order/delivery/revision bridge is missing, MFE90<20 or MAE180<=-25 routes to 4B; if reset plus order bridge exists, do not overblock","changed_axes":["C09_low_MFE_guardrail","C09_deep_MAE_guardrail","C09_false_overblock_override_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_MAE180_le_minus25)"},"eligible_trigger_count":3,"validated_4B_guard_count":1,"false_overblock_count":1,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_ADVANCED_EQUIPMENT_BLOWOFF_GUARD_VS_METROLOGY_FALSE_OVERBLOCK","row_count":3,"unique_symbol_count":3,"positive_case_count":0,"positive_risk_guard_count":1,"counterexample_count":2,"validated_4B_guard_count":1,"false_overblock_count":1,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":18.21,"avg_MAE90_pct":-12.41,"avg_MFE180_pct":24.24,"avg_MAE180_pct":-34.34,"blowoff_guard_avg_MFE90_pct":6.59,"blowoff_guard_avg_MAE180_pct":-51.05,"false_overblock_MFE90_pct":41.45,"interpretation":"C09 works as a precise valuation-blowoff guard. 주성엔지니어링 and 오로스테크놀로지 show that advanced-equipment price strength without order/delivery/margin bridge should stay Watch/4B, while 파크시스템스 shows a reset plus customer-order/metrology bridge should override a broad overblock."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"036930","trigger_type":"Stage2-4B-Validated-AdvancedALDEquipmentValuationBlowoffNoOrderDeliveryMarginBridge","entry_date":"2024-02-28","stage2_to_90D_outcome":"valid_4B_low_MFE_order_bridge_missing","stage2_to_180D_outcome":"validated_equipment_blowoff_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Advanced ALD/equipment price blowoff without customer order, delivery and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"322310","trigger_type":"Stage2-FalsePositive-OverlayMetrologyPriceMFEBlowoffNoDurableCustomerOrderBridge","entry_date":"2024-02-27","stage2_to_90D_outcome":"price_MFE_without_order_bridge","stage2_to_180D_outcome":"failed_overlay_metrology_price_MFE_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Overlay metrology MFE without customer order/revision/margin evidence should be 4B-watch, not positive C09 evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"140860","trigger_type":"Stage2-FalsePositive-OverbroadValuationBlowoffWouldMissAFMMetrologyOrderBridgeAfterReset","entry_date":"2024-04-23","stage2_to_90D_outcome":"false_overblock_high_MFE_low_MAE","stage2_to_180D_outcome":"reset_plus_metrology_order_bridge_should_not_be_hard_blocked","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"After valuation reset, customer-order/metrology bridge should override broad blowoff blocking; exact evidence still required."}
{"row_type":"residual_contribution","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","residual_type":"advanced_equipment_price_blowoff_4B_guard_and_reset_plus_order_false_overblock_override","contribution":"Adds one C09 validated 4B blowoff guard, one price-MFE counterexample, and one reset-plus-order false-overblock case, avoiding recent R2 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_SEMI_EQUIPMENT_VALUATION_BLOWOFF_GUARD_VS_METROLOGY_ORDER_BRIDGE_FALSE_OVERBLOCK","positive_risk_guard_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C09 now has non-recent advanced-equipment blowoff guard rows plus one false-overblock override case; next R2 C09 loops should exact-URL repair customer order, delivery acceptance, revenue revision, ASP/mix, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_valuation_blowoff_no_order_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"036930 validates 4B routing when advanced-equipment price blowoff lacks order/delivery/margin bridge and later MAE expands deeply."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_price_MFE_not_order_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"322310 shows metrology price-MFE should not count as order/revision validation when durable customer bridge is missing."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_reset_plus_customer_order_false_overblock_override","scope":"canonical_archetype","candidate_delta":1.0,"direction":"override_guard","apply_now":false,"shadow_only":true,"evidence_basis":"140860 shows broad valuation-blowoff blocking can be false after a valuation reset if customer order / delivery / margin bridge exists."}
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
  - advanced_equipment_valuation_blowoff_valid_4B_guard
  - overlay_metrology_price_MFE_overcredit
  - order_delivery_revision_bridge_missing
  - reset_plus_customer_order_false_overblock
new_axis_proposed:
  - C09_valuation_blowoff_no_order_4B_guard_shadow_only
  - C09_price_MFE_not_order_validation_guard_shadow_only
  - C09_reset_plus_customer_order_false_overblock_override_shadow_only
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

## 12. Data-quality caveat

All selected triggers use Stock-Web tradable raw OHLC rows.
`036930` has only an old 2000 corporate-action candidate long before selected 2024 window.
`322310` and `140860` have no corporate-action candidate in profile, and selected 2024 windows are clean.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
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
3. Confirm R2 / L2 / C09 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - previous R2 loop85 C06 symbols
   - previous R2 loop86 C07 symbols
   - previous R2 loop87 C08 symbols
   - previous R2 loop88 C09 symbols
   - previous R2 loop89 C10 symbols
   - previous R2 loop90 C06 symbols
   - previous R2 loop91 C07 symbols
   - previous R2 loop92 C08 symbols
6. Confirm stale R13/R12/R11/R10/R8/R7 candidate rows are not ingested from this MD.
7. Treat 036930 as validated C09 4B valuation-blowoff guard.
8. Treat 322310 as price-MFE-not-order-validation counterexample.
9. Treat 140860 as false-overblock override case that needs exact customer-order evidence repair before any Green consideration.
10. If aggregate support remains stable after exact evidence URL repair, consider C09-scoped safe patch candidates:
   - C09_valuation_blowoff_no_order_4B_guard
   - C09_price_MFE_not_order_validation_guard
   - C09_reset_plus_customer_order_false_overblock_override
11. Do not loosen Stage3-Green.
12. Do not use future MFE/MAE in runtime scoring.
13. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C01_ORDER_BACKLOG_MARGIN_BRIDGE or remaining Priority-0 under-30 archetype
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 validated 4B valuation-blowoff guard, 1 price-MFE counterexample, and 1 reset-plus-order false-overblock row for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.
```
