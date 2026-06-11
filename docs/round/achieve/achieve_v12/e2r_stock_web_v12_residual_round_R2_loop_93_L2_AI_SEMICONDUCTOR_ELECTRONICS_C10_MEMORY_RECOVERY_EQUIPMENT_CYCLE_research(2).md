# E2R Stock-Web v12 Residual Research — R2 Loop 93 / L2 / C10

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 93
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: CMP_WET_CLEAN_MEMORY_RECOVERY_ORDER_MARGIN_BRIDGE_VS_CHILLER_PARTS_VOCABULARY_DECAY
sector: AI / semiconductor / memory recovery / equipment cycle / CMP / wet clean / scrubber / chiller / consumable parts / order bridge / margin bridge
output_file: e2r_stock_web_v12_residual_round_R2_loop_93_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after local loop93 expansions in C09, C01, C07 and C06.

```text
selected_round = R2
selected_loop = 93
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

Reason for selecting C10:

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
C06_HBM_MEMORY_CUSTOMER_CAPACITY = 21 rows
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE = 21 rows
```

Local run-stream hygiene:

```text
C08 was expanded in loop92.
C09, C01, C07 and C06 were expanded in loop93.
Therefore this run moves to C10, the remaining still-thin Priority-0 archetype in the semiconductor cluster.
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
R2 loop93 C07: 031980, 110990, 067310
R2 loop93 C06: 402340, 195870, 222800
```

Candidate hygiene note:

```text
During this execution path, recently used C07/C06 candidate rows such as 031980, 110990, 067310, 402340, 195870 and 222800 were touched or available from the stream.
They are excluded from this C10 output because they were just used in the previous valid loops.
```

Selected symbols:

```text
281820, 036200, 101160
```

The selected pocket is:

```text
CMP / wet-clean / memory recovery equipment order-margin bridge positive-control
vs
scrubber/chiller memory-recovery equipment vocabulary after a price spike without durable order/revision/margin bridge
vs
quartz/silicon parts recovery vocabulary without direct memory-equipment cycle, customer pull-in, margin and cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"281820","company_name":"케이씨텍","profile_path":"atlas/symbol_profiles/281/281820.json","first_date":"2017-12-05","last_date":"2026-02-20","trading_day_count":2013,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"036200","company_name":"유니셈","profile_path":"atlas/symbol_profiles/036/036200.json","first_date":"1999-12-10","last_date":"2026-02-20","trading_day_count":6452,"corporate_action_candidate_count":"profile_tail_not_fetched_in_this_run","corporate_action_candidate_dates":"historical_candidates_before_2024; selected_2024_window_clean_for_entry","has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist long before selected 2024 forward window. Selected 2024 spike-decay window is usable for residual price-path analysis.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
{"row_type":"price_source_validation","symbol":"101160","company_name":"월덱스","profile_path":"atlas/symbol_profiles/101/101160.json","first_date":"2008-06-19","last_date":"2026-02-20","trading_day_count":4359,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2014-11-03"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"281820","trigger_type":"Stage2-Actionable-CMPWetCleanMemoryRecoveryOrderMarginBridge-PositiveWatch","entry_date":"2024-02-14","duplicate_status":"new C10 symbol/trigger/date combination outside recent R2 C06/C07/C08/C09/C10 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"036200","trigger_type":"Stage2-FalsePositive-ChillerScrubberMemoryRecoverySpikeNoDurableOrderRevisionMarginBridge","entry_date":"2024-05-29","duplicate_status":"new C10 symbol/trigger/date combination outside recent R2 C06/C07/C08/C09/C10 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"101160","trigger_type":"Stage2-FalsePositive-QuartzSiliconPartsRecoveryVocabularyNoDirectMemoryEquipmentCycleBridge","entry_date":"2024-01-02","duplicate_status":"new C10 symbol/trigger/date combination outside recent R2 C06/C07/C08/C09/C10 loop symbols"}
```

## 4. Research question

C10 is not “메모리 반등이 온다.”
The useful memory-recovery equipment signal must prove the equipment-cycle-to-margin chain:

```text
memory capex recovery signal
tool / part / consumable relevance to memory customers
order or shipment conversion
delivery / acceptance schedule
customer pull-in or utilization recovery
revenue revision visibility
ASP / mix quality
gross-margin / operating-margin bridge
working-capital discipline
cash conversion
```

A memory recovery headline without this bridge is a tool powered on in the bay but not accepted by the customer. E2R needs order, delivery, utilization, revision, margin and cash.

Residual question:

```text
Can C10 distinguish:
1. CMP / wet-clean / memory recovery equipment bridge with strong MFE but later cycle drawdown,
2. chiller/scrubber memory-recovery equipment vocabulary where post-spike entry lacked durable order/revision bridge,
3. quartz/silicon parts recovery vocabulary where no direct memory-equipment cycle bridge appeared and price path stayed weak?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C10_R2L93_281820_KCTECH_CMP_WETCLEAN_BRIDGE","symbol":"281820","company_name":"케이씨텍","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CMP_WETCLEAN_MEMORY_RECOVERY_ORDER_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-CMPWetCleanMemoryRecoveryOrderMarginBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE90_and_MFE180_controlled_entry_MAE_memory_recovery_equipment_bridge","current_profile_verdict":"current_profile_correct_if_memory_recovery_order_delivery_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"CMP/wet-clean memory recovery equipment proxy produced high MFE90/180 with controlled early MAE. Late drawdown keeps Green strict unless exact customer order, delivery, revision, margin and cash evidence is repaired."}
{"row_type":"case","case_id":"C10_R2L93_036200_UNISEM_CHILLER_SCRUBBER_SPIKE_DECAY","symbol":"036200","company_name":"유니셈","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CHILLER_SCRUBBER_MEMORY_RECOVERY_SPIKE_WITHOUT_DURABLE_ORDER_REVISION_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ChillerScrubberMemoryRecoverySpikeNoDurableOrderRevisionMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"score_price_alignment":"counterexample_low_MFE_deep_MAE_after_spike_no_order_revision_bridge","current_profile_verdict":"current_profile_false_positive_if_chiller_scrubber_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Chiller/scrubber memory-recovery equipment spike on 2024-05-29 had low forward MFE and deep MAE when order/revision/margin bridge was not repaired."}
{"row_type":"case","case_id":"C10_R2L93_101160_WORLDEX_PARTS_RECOVERY_DECAY","symbol":"101160","company_name":"월덱스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_SILICON_PARTS_RECOVERY_VOCABULARY_WITHOUT_DIRECT_MEMORY_EQUIPMENT_CYCLE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-QuartzSiliconPartsRecoveryVocabularyNoDirectMemoryEquipmentCycleBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_parts_recovery_vocabulary_no_direct_equipment_cycle_bridge","current_profile_verdict":"current_profile_false_positive_if_parts_recovery_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Quartz/silicon parts recovery vocabulary had near-zero MFE and deep MAE without customer pull-in, utilization, order/revision, margin or cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 281820 케이씨텍 — CMP / wet-clean memory recovery order-margin bridge

Entry row: `2024-02-14 c=35300`.
Observed path: early high `2024-03-08 h=54100`, later high `2024-07-11 h=59000`, and late-year low `2024-11-15 l=27700`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C10_281820_20240214_STAGE2_CMP_WETCLEAN_MEMORY_RECOVERY","case_id":"C10_R2L93_281820_KCTECH_CMP_WETCLEAN_BRIDGE","symbol":"281820","company_name":"케이씨텍","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CMP_WETCLEAN_MEMORY_RECOVERY_ORDER_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-CMPWetCleanMemoryRecoveryOrderMarginBridge-PositiveWatch","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":35300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_CMP_wet_clean_memory_recovery_order_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; CMP/wet-clean memory recovery order, delivery, revision and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["CMP_wet_clean_equipment_proxy","memory_recovery_order_proxy","customer_utilization_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_order_source_pending","delivery_acceptance_source_pending","revenue_revision_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch","Green_exact_evidence_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/281/281820/2024.csv","profile_path":"atlas/symbol_profiles/281/281820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":53.26,"MFE_90D_pct":53.26,"MFE_180D_pct":67.14,"MAE_30D_pct":-9.49,"MAE_90D_pct":-9.49,"MAE_180D_pct":-21.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":59000.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":27700.0,"drawdown_after_peak_pct":-53.05,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.90,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_customer_order_delivery_revision_margin_cash_evidence_and_late_drawdown_review","four_b_evidence_type":["price_extension_watch","late_drawdown_watch","Green_exact_evidence_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_and_MFE180_controlled_entry_MAE_memory_recovery_equipment_bridge","current_profile_verdict":"current_profile_correct_if_memory_recovery_order_delivery_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"281820_2024-02-14_35300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C10 can allow Yellow/Green-candidate-watch when memory recovery equipment strength is tied to order, delivery, revision, utilization and margin/cash conversion. Late drawdown and source-proxy evidence block automatic Green."}
```

### 6.2 036200 유니셈 — chiller/scrubber memory-recovery spike without durable order/revision bridge

Entry row: `2024-05-29 c=11940`, after a large equipment spike.
Observed path: local high `2024-07-04 h=12480`, then decline to `2024-08-05 l=6160`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C10_036200_20240529_STAGE2_FALSE_POSITIVE_CHILLER_SCRUBBER_SPIKE","case_id":"C10_R2L93_036200_UNISEM_CHILLER_SCRUBBER_SPIKE_DECAY","symbol":"036200","company_name":"유니셈","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CHILLER_SCRUBBER_MEMORY_RECOVERY_SPIKE_WITHOUT_DURABLE_ORDER_REVISION_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;post_spike_entry_guard","trigger_type":"Stage2-FalsePositive-ChillerScrubberMemoryRecoverySpikeNoDurableOrderRevisionMarginBridge","trigger_date":"2024-05-29","entry_date":"2024-05-29","entry_price":11940.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_chiller_scrubber_memory_recovery_equipment_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; chiller/scrubber equipment spike treated as insufficient without durable memory customer order, delivery, revenue revision, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["chiller_scrubber_equipment_keyword","memory_recovery_vocabulary","post_spike_relative_strength"],"stage3_evidence_fields":["durable_customer_order_missing","delivery_acceptance_missing","revision_visibility_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_forward_MFE","deep_MAE","post_spike_entry_watch","order_revision_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036200/2024.csv","profile_path":"atlas/symbol_profiles/036/036200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.52,"MFE_90D_pct":4.52,"MFE_180D_pct":4.52,"MAE_30D_pct":-17.84,"MAE_90D_pct":-48.41,"MAE_180D_pct":-48.41,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-04","peak_price":12480.0,"max_drawdown_low_date":"2024-08-05","max_drawdown_low":6160.0,"drawdown_after_peak_pct":-50.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.36,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"post_spike_chiller_scrubber_equipment_vocabulary_without_order_delivery_revision_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_forward_MFE","deep_MAE","post_spike_entry_watch","order_revision_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_after_spike_no_order_revision_bridge","current_profile_verdict":"current_profile_false_positive_if_chiller_scrubber_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_usable","same_entry_group_id":"036200_2024-05-29_11940","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"do_not_count_as_new_case":false,"current_profile_residual":"C10 should not promote post-spike chiller/scrubber equipment vocabulary unless exact customer order, delivery, revision, margin and cash evidence are repaired. Low MFE and deep MAE force Watch/4B routing."}
```

### 6.3 101160 월덱스 — quartz/silicon parts recovery vocabulary without direct memory-equipment cycle bridge

Entry row: `2024-01-02 c=26800`.
Observed path: local high `2024-01-04 h=27400`, then deterioration to `2024-08-05 l=18550`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C10_101160_20240102_STAGE2_FALSE_POSITIVE_PARTS_RECOVERY_DECAY","case_id":"C10_R2L93_101160_WORLDEX_PARTS_RECOVERY_DECAY","symbol":"101160","company_name":"월덱스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_SILICON_PARTS_RECOVERY_VOCABULARY_WITHOUT_DIRECT_MEMORY_EQUIPMENT_CYCLE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;parts_cycle_cross_label_stress_test","trigger_type":"Stage2-FalsePositive-QuartzSiliconPartsRecoveryVocabularyNoDirectMemoryEquipmentCycleBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":26800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_quartz_silicon_parts_memory_recovery_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; quartz/silicon parts recovery vocabulary treated as insufficient without direct memory equipment cycle, customer pull-in, utilization, revision, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["quartz_silicon_parts_keyword","memory_recovery_vocabulary","cycle_rebound_keyword"],"stage3_evidence_fields":["direct_memory_customer_pullin_missing","utilization_revision_missing","ASP_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["near_zero_MFE","deep_MAE","parts_cycle_cross_label_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/101/101160/2024.csv","profile_path":"atlas/symbol_profiles/101/101160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.24,"MFE_90D_pct":2.24,"MFE_180D_pct":2.24,"MAE_30D_pct":-13.25,"MAE_90D_pct":-16.79,"MAE_180D_pct":-30.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-04","peak_price":27400.0,"max_drawdown_low_date":"2024-08-05","max_drawdown_low":18550.0,"drawdown_after_peak_pct":-32.30,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"parts_recovery_vocabulary_without_direct_memory_equipment_cycle_customer_pullin_revision_margin_cash_bridge_should_be_4B_watch_not_C10_positive","four_b_evidence_type":["near_zero_MFE","deep_MAE","parts_cycle_cross_label_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_parts_recovery_vocabulary_no_direct_equipment_cycle_bridge","current_profile_verdict":"current_profile_false_positive_if_parts_recovery_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"101160_2024-01-02_26800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C10 should not count parts-cycle recovery vocabulary as memory equipment-cycle evidence unless customer pull-in, utilization, revision, margin and cash bridge are repaired. Near-zero MFE and deep MAE require Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_R2L93_281820_KCTECH_CMP_WETCLEAN_BRIDGE","trigger_id":"R2L93_C10_281820_20240214_STAGE2_CMP_WETCLEAN_MEMORY_RECOVERY","symbol":"281820","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C10 requires memory recovery order, delivery acceptance, utilization/revision, margin and cash bridge rather than equipment-cycle vocabulary alone","raw_component_scores_before":{"memory_recovery_score":13,"equipment_relevance_score":12,"customer_order_score":11,"delivery_acceptance_score":9,"utilization_recovery_score":10,"revision_visibility_score":9,"ASP_mix_score":8,"margin_bridge_score":10,"cash_conversion_score":7,"relative_strength_score":14,"valuation_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"memory_recovery_score":16,"equipment_relevance_score":15,"customer_order_score":14,"delivery_acceptance_score":12,"utilization_recovery_score":12,"revision_visibility_score":12,"ASP_mix_score":10,"margin_bridge_score":12,"cash_conversion_score":9,"relative_strength_score":15,"valuation_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"CMP/wet-clean order-margin bridge plus high MFE supports Green-candidate watch; late drawdown and source-proxy evidence block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_R2L93_036200_UNISEM_CHILLER_SCRUBBER_SPIKE_DECAY","trigger_id":"R2L93_C10_036200_20240529_STAGE2_FALSE_POSITIVE_CHILLER_SCRUBBER_SPIKE","symbol":"036200","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_scope":"current_default_proxy","profile_hypothesis":"post-spike equipment vocabulary without durable order/revision and margin bridge should be blocked","raw_component_scores_before":{"memory_recovery_score":4,"equipment_relevance_score":4,"customer_order_score":0,"delivery_acceptance_score":0,"utilization_recovery_score":1,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":8,"valuation_risk_score":-16,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"memory_recovery_score":1,"equipment_relevance_score":1,"customer_order_score":0,"delivery_acceptance_score":0,"utilization_recovery_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_risk_score":-28,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert post-spike equipment vocabulary into missing order/revision bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_R2L93_101160_WORLDEX_PARTS_RECOVERY_DECAY","trigger_id":"R2L93_C10_101160_20240102_STAGE2_FALSE_POSITIVE_PARTS_RECOVERY_DECAY","symbol":"101160","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_scope":"current_default_proxy","profile_hypothesis":"parts-cycle vocabulary without direct memory equipment-cycle customer pull-in and margin bridge should remain Watch/4B","raw_component_scores_before":{"memory_recovery_score":2,"equipment_relevance_score":1,"customer_order_score":0,"delivery_acceptance_score":0,"utilization_recovery_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_risk_score":-10,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"memory_recovery_score":0,"equipment_relevance_score":0,"customer_order_score":0,"delivery_acceptance_score":0,"utilization_recovery_score":0,"revision_visibility_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_risk_score":-20,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE require customer pull-in, utilization, margin and cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L93_C10_P0_CURRENT","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C10 needs explicit memory recovery order, delivery, revision, utilization, margin/cash and post-spike/parts-cycle 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":20.01,"avg_MAE90_pct":-24.90,"avg_MFE180_pct":24.63,"avg_MAE180_pct":-33.57,"false_positive_rate":0.67,"post_spike_counterexample_count":1,"parts_cycle_cross_label_count":1,"score_return_alignment_verdict":"mixed_without_C10_memory_recovery_order_revision_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C10_P1_SECTOR_SPECIFIC","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_id":"P1_L2_memory_recovery_equipment_order_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 memory recovery signals need direct equipment/customer pull-in, order conversion, delivery, utilization, revision, margin or cash conversion before Stage2-Actionable","changed_axes":["memory_recovery_order_required","revision_margin_required","post_spike_equipment_penalty","parts_cross_label_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_order_delivery_revision_utilization_margin_or_cash_proxy"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C10_P2_CANONICAL","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_id":"P2_C10_order_revision_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C10 should reward customer-order/revision-to-margin mechanics, not equipment-cycle or parts-recovery vocabulary","changed_axes":["C10_customer_order_delivery_revision_margin_cash_bridge_required","C10_post_spike_equipment_vocabulary_local_4B_guard","C10_parts_cycle_cross_label_4B_guard","C10_late_drawdown_Green_strict_guard"],"changed_thresholds":{"stage2_yellow_gate":"memory_recovery_relevance_plus_order_or_revision_margin_cash_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C10_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","profile_id":"P3_C10_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If order/revision bridge is missing, MFE90<10 or MAE90<=-20 blocks Yellow/Green and routes to Watch/4B","changed_axes":["C10_low_MFE_guardrail","C10_deep_MAE_4B_guardrail","C10_post_spike_entry_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE90_le_minus20)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_CMP_WETCLEAN_POSITIVE_VS_CHILLER_PARTS_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":20.01,"avg_MAE90_pct":-24.90,"avg_MFE180_pct":24.63,"avg_MAE180_pct":-33.57,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE90_le_minus20":0.67,"interpretation":"C10 needs bridge discipline. 케이씨텍 shows CMP/wet-clean memory recovery order-margin bridge can support Green-candidate-watch, while 유니셈 and 월덱스 show equipment-cycle or parts-recovery vocabulary should not be promoted without customer order, delivery, revision, utilization, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"281820","trigger_type":"Stage2-Actionable-CMPWetCleanMemoryRecoveryOrderMarginBridge-PositiveWatch","entry_date":"2024-02-14","stage2_to_90D_outcome":"positive_high_MFE90_controlled_entry_MAE","stage2_to_180D_outcome":"positive_memory_recovery_equipment_bridge_but_late_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/Green-candidate when memory recovery equipment strength is tied to order, delivery, revision, utilization and margin/cash bridge; exact evidence required for Green."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"036200","trigger_type":"Stage2-FalsePositive-ChillerScrubberMemoryRecoverySpikeNoDurableOrderRevisionMarginBridge","entry_date":"2024-05-29","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE_after_spike","stage2_to_180D_outcome":"failed_chiller_scrubber_equipment_spike_no_order_revision_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Post-spike equipment vocabulary without durable order/revision and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","symbol":"101160","trigger_type":"Stage2-FalsePositive-QuartzSiliconPartsRecoveryVocabularyNoDirectMemoryEquipmentCycleBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_bridge_missing","stage2_to_180D_outcome":"failed_parts_recovery_vocabulary_no_direct_memory_equipment_cycle_bridge","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Quartz/silicon parts recovery vocabulary without direct customer pull-in, utilization and margin/cash bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","residual_type":"post_spike_equipment_and_parts_cycle_vocabulary_overcredit_without_order_revision_margin_cash_bridge","contribution":"Adds two C10 4B counterexamples against one CMP/wet-clean memory recovery positive-watch, selected because C10 is Priority-0 under-30 coverage.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"CMP_WET_CLEAN_MEMORY_RECOVERY_ORDER_MARGIN_BRIDGE_VS_CHILLER_PARTS_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C10 now has one CMP/wet-clean memory recovery order-margin positive-watch and two weak-bridge counterexamples; next C10 loops should exact-URL repair memory customer order, delivery acceptance, utilization pull-in, revenue revision, ASP/mix, margin and cash evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","axis":"C10_customer_order_delivery_revision_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"281820 worked when CMP/wet-clean memory recovery order-margin proxy existed; 036200 and 101160 failed when order/revision/margin evidence was missing."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","axis":"C10_post_spike_equipment_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"036200 showed low MFE and deep MAE when chiller/scrubber memory-recovery vocabulary entered after a price spike without durable order bridge."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","axis":"C10_parts_cycle_cross_label_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"101160 showed near-zero MFE and deep MAE when quartz/silicon parts recovery vocabulary lacked direct memory equipment-cycle customer pull-in and margin evidence."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","axis":"C10_late_drawdown_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"281820 had high MFE but later drawdown; Green requires exact order/delivery/revision/margin/cash evidence."}
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
  - post_spike_equipment_vocabulary_overcredit
  - parts_cycle_recovery_vocabulary_overcredit
  - order_delivery_revision_bridge_missing
  - utilization_margin_cash_bridge_missing
  - late_drawdown_Green_strict_watch
new_axis_proposed:
  - C10_customer_order_delivery_revision_margin_cash_bridge_required_shadow_only
  - C10_post_spike_equipment_vocabulary_local_4B_guard_shadow_only
  - C10_parts_cycle_cross_label_4B_guard_shadow_only
  - C10_late_drawdown_Green_strict_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C10
  - full_4b_requires_non_price_evidence within C10
  - hard_4c_thesis_break_routes_to_4c within C10
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
`281820` has no corporate-action candidate in the profile and the selected 2024 window is clean.
`036200` has historical corporate-action/name-transition complexity before 2024, but the selected 2024 spike-decay window is usable for residual price-path analysis.
`101160` has an older 2014 corporate-action candidate before 2024; the selected 2024 window is usable.
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
3. Confirm R2 / L2 / C10 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop was selected by coverage-index-first after C08/C09/C01/C07/C06 local expansions.
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
   - previous R2 loop93 C07 symbols
   - previous R2 loop93 C06 symbols
7. Confirm touched 031980/110990/067310/402340/195870/222800 rows are not ingested from this MD.
8. Treat 036200 as post-spike memory-equipment vocabulary failure-mode unless fresh order/revision evidence is repaired.
9. Treat 101160 as parts-cycle cross-label vocabulary failure-mode, not direct memory recovery equipment evidence.
10. If aggregate support remains stable after exact evidence URL repair, consider C10-scoped safe patch candidates:
   - C10_customer_order_delivery_revision_margin_cash_bridge_required
   - C10_post_spike_equipment_vocabulary_local_4B_guard
   - C10_parts_cycle_cross_label_4B_guard
   - C10_late_drawdown_Green_strict_guard
11. Do not loosen Stage3-Green.
12. Do not use future MFE/MAE in runtime scoring.
13. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = remaining under-30 archetype from No-Repeat Index, preferably outside recently repeated R2 if coverage pressure allows
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 CMP/wet-clean memory recovery order-margin positive-watch, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.
```
