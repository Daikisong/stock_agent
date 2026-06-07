# E2R Stock-Web v12 Residual Research — R2 Loop 93 / L2 / C07

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 93
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: HBM_BACKEND_EQUIPMENT_ORDER_REVISION_BRIDGE_VS_LASER_ANNEALING_AND_PACKAGING_CROSSLABEL_PRICE_MFE_DECAY
sector: AI / semiconductor / HBM equipment / backend equipment / laser annealing / packaging capacity / customer order / revision / margin bridge
output_file: e2r_stock_web_v12_residual_round_R2_loop_93_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after the local stream corrected loop93 C01 output.

```text
selected_round = R2
selected_loop = 93
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

Reason for selecting C07:

```text
v12 scheduler = coverage_index_first
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

Local run-stream hygiene:

```text
C08 was expanded in loop92.
C09 was expanded in loop93.
C01 was expanded in loop93.
Therefore this run moves to the next still-thin Priority 0 archetype: C07.
```

This loop avoids recent R2 symbols:

```text
R2 loop85 C06: 000660, 005930, 009150
R2 loop86 C07: 042700, 064760, 003160
R2 loop87 C08: 232140, 425420, 098120
R2 loop88 C09: 039030, 412350, 253590
R2 loop89 C10: 403870, 166090, 074600
R2 loop90 C06: 036540, 033170, 394280
R2 loop91 C07: 084370, 086390, 217190
R2 loop92 C08: 092870, 080580, 237750
R2 loop93 C09: 036930, 322310, 140860
```

Selected symbols:

```text
031980, 110990, 067310
```

The selected pocket is:

```text
HBM backend equipment / order-revision / delivery-margin bridge positive-control
vs
HBM laser-annealing equipment vocabulary where price strength lacked durable order/revision bridge
vs
HBM packaging capacity / cross-label price-MFE where market-segment/share-count noise and no equipment-order bridge should block C07 promotion
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"031980","company_name":"피에스케이홀딩스","profile_path":"atlas/symbol_profiles/031/031980.json","first_date":"1997-01-07","last_date":"2026-02-20","trading_day_count":6873,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1998-07-28","2000-04-20","2007-03-16","2019-05-10","2020-02-21"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"110990","company_name":"디아이티","profile_path":"atlas/symbol_profiles/110/110990.json","first_date":"2018-08-07","last_date":"2026-02-20","trading_day_count":1849,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"067310","company_name":"하나마이크론","profile_path":"atlas/symbol_profiles/067/067310.json","first_date":"2005-10-11","last_date":"2026-02-20","trading_day_count":5024,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2009-11-10","2021-12-29"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 window. Market flag changes from KOSDAQ GLOBAL to KOSDAQ after 2024-06-13, and share-count movement appears in 2024; keep data-quality watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_2024_window_usable; market_segment_change_and_share_count_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"031980","trigger_type":"Stage2-Actionable-HBMBackendEquipmentOrderRevisionDeliveryMarginBridge-Positive","entry_date":"2024-02-22","duplicate_status":"new C07 symbol/trigger/date combination outside recent R2 C07/C08/C09 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"110990","trigger_type":"Stage2-FalsePositive-HBMLaserAnnealingVocabularyNoDurableOrderRevisionMarginBridge","entry_date":"2024-02-14","duplicate_status":"new C07 symbol/trigger/date combination outside recent R2 C07/C08/C09 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"067310","trigger_type":"Stage2-FalsePositive-HBMPackagingCapacityCrossLabelPriceMFE-NoEquipmentOrderBridge","entry_date":"2024-03-27","duplicate_status":"new C07 symbol/trigger/date combination outside recent R2 C07/C08/C09 loop symbols; cross-label packaging capacity stress with market-segment/share-count watch"}
```

## 4. Research question

C07 is not “HBM 장비 단어가 붙었다.”
The useful HBM equipment signal must prove the order-to-revision chain:

```text
named HBM process step or backend process relevance
customer qualification
order / PO / shipment conversion
delivery or acceptance schedule
revenue revision visibility
ASP / mix quality
gross-margin or operating-margin bridge
working-capital discipline
cash conversion
relative strength that is not merely price-only
```

A HBM equipment headline without this bridge is a bond head hovering above the stack. The motion looks precise, but E2R needs touchdown: customer qualification, order, delivery, revision, margin and cash.

Residual question:

```text
Can C07 distinguish:
1. HBM backend equipment / order-revision bridge with high MFE and controlled entry MAE,
2. laser annealing / HBM equipment vocabulary where price strength lacked durable order/revision bridge,
3. packaging capacity / cross-label HBM price-MFE where no direct equipment order bridge exists and data-quality repair is required?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C07_R2L93_031980_PSKH_HBM_BACKEND_ORDER","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_BACKEND_EQUIPMENT_ORDER_REVISION_DELIVERY_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-HBMBackendEquipmentOrderRevisionDeliveryMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_extreme_MFE90_low_MAE_HBM_backend_order_revision_bridge","current_profile_verdict":"current_profile_correct_if_order_delivery_revision_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"HBM/backend equipment order-revision proxy produced high MFE90 with controlled entry MAE. Green still requires exact customer, order, delivery, revision and margin evidence."}
{"row_type":"case","case_id":"C07_R2L93_110990_DIT_HBM_LASER_WEAK_BRIDGE","symbol":"110990","company_name":"디아이티","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_LASER_ANNEALING_VOCABULARY_WITHOUT_DURABLE_ORDER_REVISION_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HBMLaserAnnealingVocabularyNoDurableOrderRevisionMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_durable_order_revision_bridge","current_profile_verdict":"current_profile_false_positive_if_HBM_laser_equipment_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"HBM/laser annealing equipment vocabulary had limited forward MFE and then deep MAE. Without durable order, delivery, revision and margin bridge, it should remain Watch/4B."}
{"row_type":"case","case_id":"C07_R2L93_067310_HANAMICRON_CROSSLABEL_PACKAGING","symbol":"067310","company_name":"하나마이크론","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_PACKAGING_CAPACITY_CROSSLABEL_PRICE_MFE_WITHOUT_EQUIPMENT_ORDER_BRIDGE","case_type":"cross_label_failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HBMPackagingCapacityCrossLabelPriceMFE-NoEquipmentOrderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"score_price_alignment":"counterexample_price_MFE_but_deep_MAE_cross_label_no_equipment_order_bridge","current_profile_verdict":"current_profile_false_positive_if_packaging_capacity_price_MFE_counted_as_C07_equipment_order_evidence","price_source":"Songdaiki/stock-web","notes":"HBM packaging/capacity price-MFE is not direct C07 equipment-order evidence. Market-segment and share-count watch require data-quality repair before patching."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 031980 피에스케이홀딩스 — HBM backend equipment order / revision / delivery-margin bridge

Entry row: `2024-02-22 c=41900`.
Observed path: entry-area low `2024-02-23 l=38600`, peak `2024-06-19 h=85300`, and later full-year drawdown to `2024-12-09 l=27700`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C07_031980_20240222_STAGE2_HBM_BACKEND_ORDER_REVISION","case_id":"C07_R2L93_031980_PSKH_HBM_BACKEND_ORDER","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_BACKEND_EQUIPMENT_ORDER_REVISION_DELIVERY_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-HBMBackendEquipmentOrderRevisionDeliveryMarginBridge-Positive","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":41900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_HBM_backend_equipment_order_revision_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; HBM backend equipment order, delivery schedule, revenue revision and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["HBM_backend_process_proxy","customer_order_proxy","revision_visibility_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_order_source_pending","delivery_acceptance_source_pending","revenue_revision_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","profile_path":"atlas/symbol_profiles/031/031980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.38,"MFE_90D_pct":103.58,"MFE_180D_pct":103.58,"MAE_30D_pct":-7.88,"MAE_90D_pct":-7.88,"MAE_180D_pct":-8.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":85300.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":27700.0,"drawdown_after_peak_pct":-67.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.21,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_customer_order_delivery_revision_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_extreme_MFE90_low_MAE_HBM_backend_order_revision_bridge","current_profile_verdict":"current_profile_correct_if_order_delivery_revision_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"031980_2024-02-22_41900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C07 can allow Stage2/Yellow or Green-candidate-watch when HBM equipment strength is tied to customer order, delivery acceptance, revenue revision, margin and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 110990 디아이티 — HBM laser-annealing vocabulary without durable order/revision bridge

Entry row: `2024-02-14 c=24500`, after HBM/equipment relative-strength spike.
Observed path: local high `2024-06-26 h=27200`, but downside expanded sharply into the second half.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C07_110990_20240214_STAGE2_FALSE_POSITIVE_HBM_LASER_WEAK_BRIDGE","case_id":"C07_R2L93_110990_DIT_HBM_LASER_WEAK_BRIDGE","symbol":"110990","company_name":"디아이티","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_LASER_ANNEALING_VOCABULARY_WITHOUT_DURABLE_ORDER_REVISION_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-HBMLaserAnnealingVocabularyNoDurableOrderRevisionMarginBridge","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":24500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_HBM_laser_annealing_equipment_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; HBM laser annealing / equipment vocabulary treated as insufficient without durable order, delivery, revenue revision, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["HBM_laser_annealing_keyword","equipment_relative_strength_spike","theme_order_vocabulary"],"stage3_evidence_fields":["durable_customer_order_missing","delivery_acceptance_missing","revision_visibility_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE","deep_MAE","order_revision_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv","profile_path":"atlas/symbol_profiles/110/110990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.27,"MFE_90D_pct":11.02,"MFE_180D_pct":11.84,"MAE_30D_pct":-24.41,"MAE_90D_pct":-31.63,"MAE_180D_pct":-41.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":27200.0,"max_drawdown_low_date":"2024-09-04","max_drawdown_low":14300.0,"drawdown_after_peak_pct":-47.43,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.12,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"HBM_laser_equipment_vocabulary_without_order_delivery_revision_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","deep_MAE","order_revision_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_durable_order_revision_bridge","current_profile_verdict":"current_profile_false_positive_if_HBM_laser_equipment_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"110990_2024-02-14_24500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C07 should not promote HBM/laser equipment vocabulary unless customer order, delivery, revision, margin and cash evidence are exact-repaired. Low MFE and deep MAE force Watch/4B routing."}
```

### 6.3 067310 하나마이크론 — HBM packaging/capacity cross-label price MFE without equipment-order bridge

Entry row: `2024-03-27 c=28150`, on HBM packaging/capacity price-MFE.
Observed path: price spike to `2024-04-04 h=34500`, but later decline to `2024-12-09 l=8320`. Market segment changed from KOSDAQ GLOBAL to KOSDAQ after 2024-06-13, with 2024 share-count movement visible in the row stream.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C07_067310_20240327_STAGE2_FALSE_POSITIVE_PACKAGING_CROSSLABEL","case_id":"C07_R2L93_067310_HANAMICRON_CROSSLABEL_PACKAGING","symbol":"067310","company_name":"하나마이크론","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_PACKAGING_CAPACITY_CROSSLABEL_PRICE_MFE_WITHOUT_EQUIPMENT_ORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;cross_label_price_MFE_stress_test;data_quality_watch","trigger_type":"Stage2-FalsePositive-HBMPackagingCapacityCrossLabelPriceMFE-NoEquipmentOrderBridge","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":28150.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_HBM_packaging_capacity_price_MFE_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; HBM packaging/capacity price MFE treated as cross-label stress and insufficient for C07 without equipment customer order, delivery acceptance, revision and margin/cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["HBM_packaging_capacity_keyword","price_MFE","relative_strength_spike"],"stage3_evidence_fields":["equipment_order_missing","delivery_acceptance_missing","revision_visibility_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_MFE_without_equipment_bridge","market_segment_change_watch","share_count_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067310/2024.csv","profile_path":"atlas/symbol_profiles/067/067310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.56,"MFE_90D_pct":22.56,"MFE_180D_pct":22.56,"MAE_30D_pct":-2.66,"MAE_90D_pct":-47.25,"MAE_180D_pct":-70.44,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-04","peak_price":34500.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":8320.0,"drawdown_after_peak_pct":-75.88,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"HBM_packaging_capacity_price_MFE_without_direct_equipment_order_revision_margin_bridge_should_be_4B_watch_not_C07_positive; data_quality_repair_required","four_b_evidence_type":["price_MFE_without_equipment_bridge","market_segment_change_watch","share_count_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_MFE_but_deep_MAE_cross_label_no_equipment_order_bridge","current_profile_verdict":"current_profile_false_positive_if_packaging_capacity_price_MFE_counted_as_C07_equipment_order_evidence","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_segment_change_watch_KOSDAQ_GLOBAL_to_KOSDAQ_after_2024-06-13","share_count_movement_watch","cross_label_packaging_not_equipment_order_bridge"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_usable; 2024_market_segment_and_share_count_watch","same_entry_group_id":"067310_2024-03-27_28150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"do_not_count_as_new_case":false,"current_profile_residual":"C07 should not count HBM packaging/capacity price MFE as equipment-order validation unless direct equipment customer order, delivery acceptance, revenue revision, margin and cash evidence are exact-repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_R2L93_031980_PSKH_HBM_BACKEND_ORDER","trigger_id":"R2L93_C07_031980_20240222_STAGE2_HBM_BACKEND_ORDER_REVISION","symbol":"031980","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C07 requires HBM process relevance, customer qualification, order/shipment, delivery acceptance, revision visibility, margin and cash bridge rather than relative strength alone","raw_component_scores_before":{"HBM_process_relevance_score":14,"customer_qualification_score":12,"order_conversion_score":13,"delivery_acceptance_score":11,"revision_visibility_score":12,"ASP_mix_score":9,"margin_bridge_score":10,"cash_conversion_score":7,"relative_strength_score":16,"valuation_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"HBM_process_relevance_score":17,"customer_qualification_score":15,"order_conversion_score":16,"delivery_acceptance_score":13,"revision_visibility_score":15,"ASP_mix_score":11,"margin_bridge_score":12,"cash_conversion_score":9,"relative_strength_score":17,"valuation_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":90,"stage_label_after":"Stage3-Green-candidate-watch","component_delta_explanation":"HBM backend equipment order/revision bridge plus extreme MFE supports Green-candidate watch; exact source evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_R2L93_110990_DIT_HBM_LASER_WEAK_BRIDGE","trigger_id":"R2L93_C07_110990_20240214_STAGE2_FALSE_POSITIVE_HBM_LASER_WEAK_BRIDGE","symbol":"110990","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_scope":"current_default_proxy","profile_hypothesis":"HBM laser/equipment vocabulary without durable order and revision bridge should be blocked","raw_component_scores_before":{"HBM_process_relevance_score":4,"customer_qualification_score":0,"order_conversion_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":1,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":7,"valuation_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"HBM_process_relevance_score":1,"customer_qualification_score":0,"order_conversion_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert HBM equipment vocabulary into missing customer-order/revision bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_R2L93_067310_HANAMICRON_CROSSLABEL_PACKAGING","trigger_id":"R2L93_C07_067310_20240327_STAGE2_FALSE_POSITIVE_PACKAGING_CROSSLABEL","symbol":"067310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_scope":"current_default_proxy","profile_hypothesis":"HBM packaging/capacity price-MFE without direct equipment order and revision bridge should remain cross-label Watch/4B","raw_component_scores_before":{"HBM_process_relevance_score":2,"customer_qualification_score":0,"order_conversion_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":12,"valuation_risk_score":-16,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/CrossLabel/DataQualityWatch","raw_component_scores_after":{"HBM_process_relevance_score":0,"customer_qualification_score":0,"order_conversion_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_risk_score":-28,"theme_spike_risk":-24,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/CrossLabel/DataQualityWatch","component_delta_explanation":"Price-MFE and packaging capacity vocabulary are not C07 equipment-order evidence; market/share-count data quality must be repaired."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L93_C07_P0_CURRENT","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C07 needs explicit HBM customer qualification, order, delivery, revision, margin/cash and cross-label price-MFE taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":45.72,"avg_MAE90_pct":-29.02,"avg_MFE180_pct":45.99,"avg_MAE180_pct":-40.06,"false_positive_rate":0.67,"price_MFE_without_equipment_order_count":1,"data_quality_watch_count":1,"score_return_alignment_verdict":"mixed_without_C07_order_delivery_revision_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C07_P1_SECTOR_SPECIFIC","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P1_L2_HBM_equipment_order_revision_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 HBM equipment signals need customer qualification, order conversion, delivery acceptance, revision visibility, margin or cash conversion before Stage2-Actionable","changed_axes":["customer_order_required","delivery_revision_required","cross_label_price_MFE_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_qualification_order_delivery_revision_margin_or_cash_proxy"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C07_P2_CANONICAL","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P2_C07_order_delivery_revision_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C07 should reward order-to-revision mechanics, not HBM vocabulary or cross-label price MFE","changed_axes":["C07_customer_order_delivery_revision_margin_cash_bridge_required","C07_HBM_vocabulary_local_4B_guard","C07_cross_label_packaging_price_MFE_guard","C07_market_segment_share_count_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"HBM_process_relevance_plus_order_or_delivery_revision_margin_cash_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C07_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"P3_C07_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If order/revision bridge is missing, MFE90<20 or MAE90<=-20 blocks Yellow/Green; price-MFE without equipment bridge stays 4B-watch","changed_axes":["C07_low_MFE_guardrail","C07_deep_MAE_guardrail","C07_price_MFE_cross_label_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_MAE90_le_minus20); high_MFE_without_equipment_bridge_not_positive"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_BACKEND_ORDER_POSITIVE_VS_LASER_PACKAGING_CROSSLABEL_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":45.72,"avg_MAE90_pct":-29.02,"avg_MFE180_pct":45.99,"avg_MAE180_pct":-40.06,"stage2_hit_rate_MFE90_ge20":0.67,"stage2_bad_entry_rate_bridge_missing":0.67,"price_MFE_without_equipment_bridge_counterexample_count":1,"interpretation":"C07 needs bridge discipline. 피에스케이홀딩스 shows HBM backend equipment order/revision bridge can support Green-candidate-watch, while 디아이티 and 하나마이크론 show HBM vocabulary, laser-annealing theme or packaging capacity price-MFE should not be promoted without direct customer order, delivery, revision, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"031980","trigger_type":"Stage2-Actionable-HBMBackendEquipmentOrderRevisionDeliveryMarginBridge-Positive","entry_date":"2024-02-22","stage2_to_90D_outcome":"good_stage2_extreme_MFE_low_MAE","stage2_to_180D_outcome":"positive_HBM_order_revision_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow/Green-candidate when HBM equipment strength is tied to customer order, delivery acceptance, revision and margin/cash bridge; exact evidence required for Green."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"110990","trigger_type":"Stage2-FalsePositive-HBMLaserAnnealingVocabularyNoDurableOrderRevisionMarginBridge","entry_date":"2024-02-14","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_HBM_laser_vocabulary_no_order_revision_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"HBM laser/equipment vocabulary without durable order/revision and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","symbol":"067310","trigger_type":"Stage2-FalsePositive-HBMPackagingCapacityCrossLabelPriceMFE-NoEquipmentOrderBridge","entry_date":"2024-03-27","stage2_to_90D_outcome":"price_MFE_without_equipment_order_bridge","stage2_to_180D_outcome":"cross_label_packaging_capacity_price_MFE_deep_MAE_data_quality_watch","MFE90_ge20":true,"MAE90_le_minus20":true,"transition_note":"HBM packaging/capacity MFE without equipment customer order/revision evidence should remain cross-label Watch/4B; market/share-count repair required."}
{"row_type":"residual_contribution","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","residual_type":"HBM_vocabulary_and_packaging_price_MFE_overcredit_without_equipment_order_revision_margin_bridge","contribution":"Adds two C07 4B counterexamples against one HBM backend equipment order/revision positive, selected because C07 is Priority-0 under-30 coverage.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_BACKEND_EQUIPMENT_ORDER_REVISION_BRIDGE_VS_LASER_ANNEALING_AND_PACKAGING_CROSSLABEL_PRICE_MFE_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C07 now has one non-recent HBM backend equipment order/revision positive and two bridge-missing counterexamples; next C07 loops should exact-URL repair customer qualification, order, delivery acceptance, revenue revision, ASP/mix, margin and cash evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_customer_order_delivery_revision_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"031980 worked when HBM backend order/revision proxy existed; 110990 and 067310 failed or became cross-label when direct equipment order/revision evidence was missing."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_HBM_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"110990 showed low MFE and deep MAE when HBM/laser equipment vocabulary was not tied to durable order/revision evidence."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_cross_label_packaging_price_MFE_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"067310 shows packaging/capacity price MFE should not validate C07 equipment-order mechanics without direct customer order, delivery and revision evidence."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","axis":"C07_market_segment_share_count_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"067310 has KOSDAQ GLOBAL to KOSDAQ market-segment change and visible 2024 share-count movement; patching needs price-path/evidence repair."}
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
  - HBM_equipment_vocabulary_overcredit
  - laser_annealing_theme_without_order_bridge
  - packaging_capacity_cross_label_price_MFE_overcredit
  - customer_order_delivery_revision_bridge_missing
  - market_segment_share_count_data_quality_watch
new_axis_proposed:
  - C07_customer_order_delivery_revision_margin_cash_bridge_required_shadow_only
  - C07_HBM_vocabulary_local_4B_guard_shadow_only
  - C07_cross_label_packaging_price_MFE_guard_shadow_only
  - C07_market_segment_share_count_data_quality_guard_shadow_only
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
`031980` has older corporate-action/name-transition candidates before 2024; the selected 2024 window is usable.
`110990` has no corporate-action candidate and the selected 2024 window is clean.
`067310` has older corporate-action candidates before 2024, market-segment change after 2024-06-13, and visible share-count movement in 2024; it remains data-quality watch before patching.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
market_segment_change_watch = true for 067310
share_count_watch = true for 067310
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
3. Confirm R2 / L2 / C07 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop was selected by coverage-index-first after C08/C09/C01 local expansions.
6. Confirm this loop avoided:
   - previous R2 loop85 C06 symbols
   - previous R2 loop86 C07 symbols
   - previous R2 loop87 C08 symbols
   - previous R2 loop88 C09 symbols
   - previous R2 loop89 C10 symbols
   - previous R2 loop90 C06 symbols
   - previous R2 loop91 C07 symbols
   - previous R2 loop92 C08 symbols
   - previous R2 loop93 C09 symbols
7. Keep 067310 in market-segment/share-count data-quality watch before patch consideration.
8. Treat 067310 as cross-label packaging-capacity price-MFE failure-mode stress only, not as direct equipment-order evidence.
9. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C07-scoped safe patch candidates:
   - C07_customer_order_delivery_revision_margin_cash_bridge_required
   - C07_HBM_vocabulary_local_4B_guard
   - C07_cross_label_packaging_price_MFE_guard
   - C07_market_segment_share_count_data_quality_guard
10. Do not loosen Stage3-Green.
11. Do not use future MFE/MAE in runtime scoring.
12. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY or C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE or remaining Priority-0 under-30 archetype
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive HBM backend equipment order/revision bridge, 2 counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.
```
