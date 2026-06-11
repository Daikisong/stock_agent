# E2R Stock-Web v12 Residual Research — R2 Loop 93 / L2 / C09 Tertiary

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 93
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: FRONTEND_WET_CLEAN_CCSS_ADVANCED_EQUIPMENT_PRICE_MFE_VS_ORDER_MARGIN_BRIDGE
sector: AI / semiconductor / frontend equipment / wet clean / CCSS / wafer handling / advanced equipment / order revision / margin bridge / valuation blowoff
output_file: e2r_stock_web_v12_residual_round_R2_loop_93_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_TERTIARY_FRONTEND_WET_CLEAN_CCSSL_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This is the corrected valid output for the current execution. A stale C08 tertiary file was touched in the execution path, but it is duplicate-like relative to the immediately prior local output and must not be treated as the valid artifact.

```text
selected_round = R2
selected_loop = 93
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

Reason for selecting C09:

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
```

Local-stream hygiene:

```text
C08 was expanded immediately before this execution.
C09 was previously expanded with 036930/322310/140860 and secondary 089030/036810/101490.
This run selects a tertiary C09 pocket with no repeated symbol.
```

Avoided symbols:

```text
Prior C09: 039030, 412350, 253590, 036930, 322310, 140860, 089030, 036810, 101490
Prior C08: 232140, 425420, 098120, 092870, 080580, 237750, 058470, 095340, 131290, 219130, 064290, 420770
Prior local C07/C06/C10: 031980, 110990, 067310, 402340, 195870, 222800, 281820, 036200, 101160
```

Selected symbols:

```text
240810, 079370, 039440
```

Selected pocket:

```text
frontend equipment order/revision bridge positive-watch
vs
wet-clean / robot / equipment vocabulary contaminated by corporate-action/share-count window
vs
CCSS / semiconductor equipment price spike without durable order/revision/margin bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"240810","company_name":"원익IPS","profile_path":"atlas/symbol_profiles/240/240810.json","first_date":"2016-05-02","last_date":"2026-02-20","trading_day_count":2405,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"markets":["KOSDAQ","KOSDAQ GLOBAL"],"status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"079370","company_name":"제우스","profile_path":"atlas/symbol_profiles/079/079370.json","first_date":"2006-02-01","last_date":"2026-02-20","trading_day_count":4945,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2024-01-16","2024-02-08"],"has_major_raw_discontinuity":true,"calibration_caveat":"2024 corporate-action/share-count candidate occurs before selected post-candidate entry; data-quality repair required before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_entry_after_CA_candidate; data_quality_watch"}
{"row_type":"price_source_validation","symbol":"039440","company_name":"에스티아이","profile_path":"atlas/symbol_profiles/039/039440.json","first_date":"2002-02-28","last_date":"2026-02-20","trading_day_count":5883,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2002-11-11","2006-01-24","2018-04-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
```

## 3. Novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"240810","trigger_type":"Stage2-Actionable-FrontendEquipmentOrderRevisionMarginBridge-PositiveWatch","entry_date":"2024-02-29","duplicate_status":"new C09 symbol/trigger/date combination outside previous C09 loops"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"079370","trigger_type":"Stage2-FalsePositive-WetCleanRobotEquipmentVocabularyNoCleanOrderMarginBridge","entry_date":"2024-02-22","duplicate_status":"new C09 symbol/trigger/date combination; 2024 CA/share-count watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"039440","trigger_type":"Stage2-FalsePositive-CCSSEquipmentPriceSpikeNoDurableOrderRevisionMarginBridge","entry_date":"2024-02-13","duplicate_status":"new C09 symbol/trigger/date combination outside previous C09 loops"}
```

## 4. Research question

C09 is not “반도체 장비가 올랐다.”
The useful advanced-equipment signal must prove the equipment-to-margin chain:

```text
customer order / PO / shipment visibility
delivery or acceptance schedule
revenue revision
ASP / mix quality
gross-margin and OPM bridge
working-capital discipline
cash conversion
valuation discipline after price expansion
```

A semiconductor tool can sit on the clean-room floor like a bright machine without turning into revenue. E2R needs the order, acceptance, revision, margin and cash, not the machinery vocabulary alone.

Residual question:

```text
Can C09 distinguish:
1. frontend equipment order/revision bridge with MFE and controlled early MAE,
2. wet-clean / robot equipment vocabulary where corporate-action/share-count and missing margin bridge block promotion,
3. CCSS/equipment price spike that decays when durable order/revision/margin evidence is absent?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C09_R2L93C_240810_WONIK_FRONTEND_ORDER","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"FRONTEND_EQUIPMENT_ORDER_REVISION_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-FrontendEquipmentOrderRevisionMarginBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_watch_MFE90_ge30_low_initial_MAE_but_late_cycle_drawdown","current_profile_verdict":"current_profile_correct_if_order_delivery_revision_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"Frontend equipment/order-revision proxy after February reset produced MFE90 above 30 with shallow early MAE. Green still requires exact customer order, delivery, revision, margin and cash evidence."}
{"row_type":"case","case_id":"C09_R2L93C_079370_ZEUS_WET_CLEAN_CA_DECAY","symbol":"079370","company_name":"제우스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"WET_CLEAN_ROBOT_EQUIPMENT_VOCABULARY_WITHOUT_CLEAN_ORDER_MARGIN_BRIDGE","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-WetCleanRobotEquipmentVocabularyNoCleanOrderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"score_price_alignment":"counterexample_sub15_MFE_deep_MAE_CA_share_count_watch_no_clean_order_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_wet_clean_robot_equipment_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Wet-clean/robot/equipment vocabulary after the 2024 CA/share-count candidate had sub-15 MFE and deep drawdown when clean order, revision, margin and cash bridge were missing."}
{"row_type":"case","case_id":"C09_R2L93C_039440_STI_CCSS_SPIKE_DECAY","symbol":"039440","company_name":"에스티아이","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"CCSS_EQUIPMENT_PRICE_SPIKE_WITHOUT_ORDER_REVISION_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CCSSEquipmentPriceSpikeNoDurableOrderRevisionMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_spike_MFE_but_deep_late_MAE_no_durable_order_revision_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_CCSS_equipment_price_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"CCSS/equipment spike produced price-MFE, but later drawdown shows price expansion should not validate missing order/revision/margin evidence."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 240810 원익IPS — frontend equipment order/revision bridge positive-watch

Entry row: `2024-02-29 c=32800`.
Observed path: `2024-03-29 h=43400`, later cycle low around `2024-12-09 l≈20300` in the raw year stream.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93C_C09_240810_20240229_STAGE2_FRONTEND_ORDER","case_id":"C09_R2L93C_240810_WONIK_FRONTEND_ORDER","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"FRONTEND_EQUIPMENT_ORDER_REVISION_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-FrontendEquipmentOrderRevisionMarginBridge-PositiveWatch","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":32800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_frontend_equipment_order_revision_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; frontend equipment order, delivery, revision, ASP/mix, margin and cash bridge treated as non-price proxy","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["frontend_equipment_proxy","customer_order_proxy","revision_visibility_proxy","relative_strength_after_reset"],"stage3_evidence_fields":["exact_order_source_pending","delivery_acceptance_source_pending","revenue_revision_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["MFE90_ge30_watch","late_cycle_drawdown_watch","Green_exact_evidence_watch"],"stage4c_evidence_fields":["order_cut_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","profile_path":"atlas/symbol_profiles/240/240810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.32,"MFE_90D_pct":32.32,"MFE_180D_pct":32.32,"MAE_30D_pct":-2.29,"MAE_90D_pct":-2.29,"MAE_180D_pct":-4.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-29","peak_price":43400.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":20300.0,"drawdown_after_peak_pct":-53.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_order_delivery_revision_margin_cash_evidence_and_late_cycle_review","four_b_evidence_type":["MFE90_ge30_watch","late_cycle_drawdown_watch","Green_exact_evidence_watch"],"four_c_protection_label":"order_cut_watch_only","trigger_outcome_label":"positive_watch_MFE90_ge30_low_initial_MAE_but_late_cycle_drawdown","current_profile_verdict":"current_profile_correct_if_order_delivery_revision_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"240810_2024-02-29_32800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C09 can allow Green-candidate-watch when equipment strength is tied to customer order, delivery, revision, margin and cash conversion. MFE alone does not loosen Green."}
```

### 6.2 079370 제우스 — wet-clean / robot equipment vocabulary without clean order-margin bridge

Entry row: `2024-02-22 c=20500`, after the 2024-01-16 and 2024-02-08 CA/share-count candidate windows.
Observed path: `2024-02-28 h=22800`, then long decline to `2024-12-09 l=12100`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93C_C09_079370_20240222_STAGE2_FALSE_POSITIVE_WETCLEAN_CA","case_id":"C09_R2L93C_079370_ZEUS_WET_CLEAN_CA_DECAY","symbol":"079370","company_name":"제우스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"WET_CLEAN_ROBOT_EQUIPMENT_VOCABULARY_WITHOUT_CLEAN_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;data_quality_watch","trigger_type":"Stage2-FalsePositive-WetCleanRobotEquipmentVocabularyNoCleanOrderMarginBridge","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":20500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_wet_clean_robot_equipment_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; wet-clean/robot equipment vocabulary treated as insufficient without clean order, shipment/revision, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["wet_clean_equipment_keyword","robot_equipment_vocabulary","post_CA_relative_strength"],"stage3_evidence_fields":["clean_customer_order_missing","revision_visibility_missing","margin_cash_bridge_missing","CA_share_count_repair_pending"],"stage4b_evidence_fields":["sub15_MFE","deep_MAE","CA_share_count_watch","order_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv","profile_path":"atlas/symbol_profiles/079/079370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.22,"MFE_90D_pct":11.22,"MFE_180D_pct":11.22,"MAE_30D_pct":-8.73,"MAE_90D_pct":-18.88,"MAE_180D_pct":-40.93,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-28","peak_price":22800.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":12100.0,"drawdown_after_peak_pct":-46.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"wet_clean_robot_equipment_vocabulary_without_clean_order_revision_margin_cash_bridge_and_CA_repair_should_be_4B_watch_not_positive","four_b_evidence_type":["sub15_MFE","deep_MAE","CA_share_count_watch","order_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub15_MFE_deep_MAE_CA_share_count_watch_no_clean_order_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_wet_clean_robot_equipment_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024-01-16_and_2024-02-08_CA_share_count_candidate_watch"],"corporate_action_window_status":"selected_entry_after_2024_CA_candidates; data_quality_watch","same_entry_group_id":"079370_2024-02-22_20500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"do_not_count_as_new_case":false,"current_profile_residual":"C09 should not promote wet-clean/robot equipment vocabulary unless clean customer order, delivery/revision, margin and cash evidence are repaired."}
```

### 6.3 039440 에스티아이 — CCSS / equipment price spike without durable order-revision bridge

Entry row: `2024-02-13 c=33650`, after a CCSS / equipment theme spike.
Observed path: `2024-03-13 h=43250`, then later decline to `2024-12-09 l=13670`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93C_C09_039440_20240213_STAGE2_FALSE_POSITIVE_CCSS_SPIKE","case_id":"C09_R2L93C_039440_STI_CCSS_SPIKE_DECAY","symbol":"039440","company_name":"에스티아이","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"CCSS_EQUIPMENT_PRICE_SPIKE_WITHOUT_ORDER_REVISION_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_MFE_not_order_validation","trigger_type":"Stage2-FalsePositive-CCSSEquipmentPriceSpikeNoDurableOrderRevisionMarginBridge","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":33650.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_CCSS_equipment_price_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; CCSS/equipment price spike treated as insufficient without durable order, delivery, revision, margin and cash bridge","evidence_source_type":"historical_public_theme_report_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["CCSS_equipment_keyword","semiconductor_equipment_price_spike","relative_strength"],"stage3_evidence_fields":["durable_customer_order_missing","delivery_acceptance_missing","revision_visibility_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_MFE_without_bridge","deep_late_MAE","order_revision_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv","profile_path":"atlas/symbol_profiles/039/039440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.53,"MFE_90D_pct":28.53,"MFE_180D_pct":28.53,"MAE_30D_pct":-4.31,"MAE_90D_pct":-8.92,"MAE_180D_pct":-44.22,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":43250.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":13670.0,"drawdown_after_peak_pct":-68.39,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"CCSS_equipment_price_MFE_without_durable_order_delivery_revision_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_MFE_without_bridge","deep_late_MAE","order_revision_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_spike_MFE_but_deep_late_MAE_no_durable_order_revision_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_CCSS_equipment_price_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"039440_2024-02-13_33650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C09 should not let price-MFE substitute for durable customer order/revision/margin evidence. This row remains 4B-watch until exact evidence is repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L93C_240810_WONIK_FRONTEND_ORDER","trigger_id":"R2L93C_C09_240810_20240229_STAGE2_FRONTEND_ORDER","symbol":"240810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_scope":"current_default_proxy","profile_hypothesis":"C09 should reward order/revision-to-margin mechanics and keep valuation blowoff Green-strict","raw_component_scores_before":{"advanced_equipment_theme_score":10,"customer_order_score":10,"delivery_acceptance_score":8,"revision_visibility_score":9,"ASP_mix_score":8,"margin_bridge_score":8,"cash_conversion_score":6,"relative_strength_score":11,"valuation_heat_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":66,"stage_label_before":"Stage2-Watch/PositiveControl","raw_component_scores_after":{"advanced_equipment_theme_score":13,"customer_order_score":13,"delivery_acceptance_score":11,"revision_visibility_score":12,"ASP_mix_score":10,"margin_bridge_score":10,"cash_conversion_score":8,"relative_strength_score":12,"valuation_heat_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable/Yellow-Watch","component_delta_explanation":"MFE90 above 30 and shallow early MAE support Yellow-watch, but exact order/revision/margin/cash evidence is required before Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L93C_079370_ZEUS_WET_CLEAN_CA_DECAY","trigger_id":"R2L93C_C09_079370_20240222_STAGE2_FALSE_POSITIVE_WETCLEAN_CA","symbol":"079370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_scope":"current_default_proxy","profile_hypothesis":"wet-clean/robot equipment vocabulary without clean order and margin bridge should be blocked","raw_component_scores_before":{"advanced_equipment_theme_score":3,"customer_order_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_heat_score":8,"execution_risk_score":-16,"theme_spike_risk":-16,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"advanced_equipment_theme_score":0,"customer_order_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_heat_score":12,"execution_risk_score":-24,"theme_spike_risk":-20,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Sub-15 MFE, deep MAE and CA/share-count watch require order/margin evidence and price-quality repair."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_R2L93C_039440_STI_CCSS_SPIKE_DECAY","trigger_id":"R2L93C_C09_039440_20240213_STAGE2_FALSE_POSITIVE_CCSS_SPIKE","symbol":"039440","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","profile_scope":"current_default_proxy","profile_hypothesis":"CCSS/equipment price spike without durable order/revision and margin bridge should remain Watch/4B","raw_component_scores_before":{"advanced_equipment_theme_score":5,"customer_order_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":7,"valuation_heat_score":12,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"advanced_equipment_theme_score":1,"customer_order_score":0,"delivery_acceptance_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_heat_score":16,"execution_risk_score":-28,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Price-MFE followed by large drawdown confirms that price path alone cannot validate missing order/revision/margin evidence."}
```

## 8. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"C09_FRONTEND_EQUIPMENT_POSITIVE_VS_WETCLEAN_CCSS_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":24.02,"avg_MAE90_pct":-10.03,"avg_MFE180_pct":24.02,"avg_MAE180_pct":-30.01,"stage2_hit_rate_MFE90_ge20":0.67,"stage2_bad_entry_rate_bridge_missing":0.67,"interpretation":"C09 needs order/revision discipline. 원익IPS shows frontend equipment order/revision bridge can support Yellow-watch, while 제우스 and 에스티아이 show wet-clean/robot/CCSS vocabulary or price-MFE should not be promoted without clean order, delivery, revision, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"240810","trigger_type":"Stage2-Actionable-FrontendEquipmentOrderRevisionMarginBridge-PositiveWatch","entry_date":"2024-02-29","stage2_to_90D_outcome":"positive_watch_MFE90_ge30_low_initial_MAE","stage2_to_180D_outcome":"frontend_equipment_bridge_but_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow-watch when equipment strength is tied to order, delivery, revision, margin and cash bridge; exact evidence required for Green."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"079370","trigger_type":"Stage2-FalsePositive-WetCleanRobotEquipmentVocabularyNoCleanOrderMarginBridge","entry_date":"2024-02-22","stage2_to_90D_outcome":"bad_stage2_sub15_MFE_CA_watch","stage2_to_180D_outcome":"failed_wet_clean_robot_vocabulary_deep_MAE_no_clean_order_margin_bridge","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Wet-clean/robot equipment vocabulary after CA/share-count candidate without clean order/margin bridge should stay Watch/4B."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"039440","trigger_type":"Stage2-FalsePositive-CCSSEquipmentPriceSpikeNoDurableOrderRevisionMarginBridge","entry_date":"2024-02-13","stage2_to_90D_outcome":"price_MFE_without_bridge","stage2_to_180D_outcome":"failed_CCSS_price_MFE_deep_late_MAE_no_order_revision_bridge","MFE90_ge20":true,"MAE180_le_minus25":true,"transition_note":"CCSS/equipment price-MFE without order/revision/margin bridge should remain Watch/4B."}
{"row_type":"residual_contribution","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","residual_type":"frontend_equipment_positive_vs_wetclean_CCSS_price_MFE_overcredit_without_order_revision_margin_cash_bridge","contribution":"Adds one C09 frontend-equipment order/revision positive-watch and two weak-bridge counterexamples, after discarding duplicate-like C08 tertiary flow from this execution path.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"FRONTEND_WET_CLEAN_CCSS_ADVANCED_EQUIPMENT_PRICE_MFE_VS_ORDER_MARGIN_BRIDGE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C09 now has a third non-overlapping pocket: frontend-equipment positive-watch and wet-clean/CCSS weak-bridge counterexamples; next C09 loops should exact-URL repair order, delivery, revision, margin and cash evidence."}
```

## 9. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_order_delivery_revision_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"240810 worked as positive-watch when frontend equipment order/revision proxy existed; 079370 and 039440 failed when order/revision/margin evidence was missing."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_wetclean_CCSS_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"079370 and 039440 showed wet-clean/robot/CCSS equipment vocabulary should not validate C09 unless order/revision/margin evidence is repaired."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_price_MFE_not_order_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"039440 had price-MFE but then deep drawdown; price path cannot substitute for customer-order evidence."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_CA_share_count_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"079370 has 2024 CA/share-count candidate windows before selected entry; patching requires data-quality repair."}
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
  - wetclean_robot_equipment_vocabulary_overcredit
  - CCSS_equipment_price_MFE_overcredit
  - order_delivery_revision_bridge_missing
  - margin_cash_bridge_missing
  - CA_share_count_data_quality_watch
new_axis_proposed:
  - C09_order_delivery_revision_margin_cash_bridge_required_shadow_only
  - C09_wetclean_CCSS_vocabulary_local_4B_guard_shadow_only
  - C09_price_MFE_not_order_validation_guard_shadow_only
  - C09_CA_share_count_data_quality_guard_shadow_only
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
`240810` has no corporate-action candidate and the selected 2024 window is clean.
`079370` has 2024-01-16 and 2024-02-08 corporate-action/share-count candidate windows before the selected entry, so it remains data-quality watch before patching.
`039440` has older corporate-action candidates before 2024; selected 2024 window is usable.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for residual price-path analysis
evidence_url_pending = true
source_proxy_only = true
CA_share_count_watch = true for 079370
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
5. Confirm duplicate-like C08 tertiary file touched in this execution is not ingested as the valid artifact for this request.
6. Confirm this loop avoided prior C09 loop88, loop93, and secondary C09 symbols.
7. Confirm recently touched C08/C01/C28/C23/C17/C13/C12 rows are not ingested from this MD.
8. Treat 240810 as Yellow/positive-watch only, not Green, until exact order/revision/margin/cash evidence is repaired.
9. Treat 079370 and 039440 as weak-bridge failure modes unless exact order/revision/margin/cash evidence is added later.
10. Keep 079370 in CA/share-count data-quality watch before patch consideration.
11. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C09-scoped safe patch candidates:
   - C09_order_delivery_revision_margin_cash_bridge_required
   - C09_wetclean_CCSS_vocabulary_local_4B_guard
   - C09_price_MFE_not_order_validation_guard
   - C09_CA_share_count_data_quality_guard
12. Do not loosen Stage3-Green.
13. Do not use future MFE/MAE in runtime scoring.
14. Use this MD only for calibration profile planning.
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
This corrected loop adds 3 new independent C09 cases, 1 frontend-equipment order/revision positive-watch, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF.
```
