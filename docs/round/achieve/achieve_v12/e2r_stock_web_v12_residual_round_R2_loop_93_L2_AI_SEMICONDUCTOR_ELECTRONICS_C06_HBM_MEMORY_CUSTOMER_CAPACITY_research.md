# E2R Stock-Web v12 Residual Research — R2 Loop 93 / L2 / C06

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R2
loop: 93
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_MEMORY_CUSTOMER_CAPACITY_LOOKTHROUGH_BRIDGE_VS_SUBSTRATE_CAPACITY_CROSSLABEL_DECAY
sector: AI / semiconductor / HBM memory / customer capacity / mix / ASP / FCF / substrate / packaging cross-label
output_file: e2r_stock_web_v12_residual_round_R2_loop_93_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after local loop93 expansions in C09, C01, and C07.

```text
selected_round = R2
selected_loop = 93
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

Reason for selecting C06:

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
C09, C01 and C07 were expanded in loop93.
Therefore this run moves to C06, the next still-thin Priority-0 archetype.
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
```

Candidate hygiene note:

```text
During this execution path, R2/C07 candidate rows such as 031980, 110990 and 067310 were touched while checking alternatives.
They are excluded from this C06 output because they were just used in the previous valid C07 loop.
```

Selected symbols:

```text
402340, 195870, 222800
```

The selected pocket is:

```text
HBM memory capacity / customer-mix / FCF look-through positive-watch
vs
memory package substrate vocabulary without HBM mix / ASP / FCF bridge
vs
PCB/substrate capacity vocabulary and market-segment change where price path confirms cross-label 4B, not C06 memory capacity validation
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"402340","company_name":"SK스퀘어","profile_path":"atlas/symbol_profiles/402/402340.json","first_date":"2021-11-29","last_date":"2026-02-20","trading_day_count":1034,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Clean price profile; however C06 use is look-through HBM memory capacity exposure rather than direct memory manufacturing.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window; lookthrough_holdco_watch"}
{"row_type":"price_source_validation","symbol":"195870","company_name":"해성디에스","profile_path":"atlas/symbol_profiles/195/195870.json","first_date":"2016-06-24","last_date":"2026-02-20","trading_day_count":2369,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"222800","company_name":"심텍","profile_path":"atlas/symbol_profiles/222/222800.json","first_date":"2015-08-07","last_date":"2026-02-20","trading_day_count":2584,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2015-09-22","2020-05-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 window. Market flag changes from KOSDAQ to KOSDAQ GLOBAL after 2024-06-14; keep market-segment data-quality watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; market_segment_change_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"402340","trigger_type":"Stage2-Actionable-HBMMemoryCustomerCapacityMixFCFLookthroughBridge-PositiveWatch","entry_date":"2024-02-01","duplicate_status":"new C06 symbol/trigger/date combination outside recent R2 C06/C07/C08/C09 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"195870","trigger_type":"Stage2-FalsePositive-MemorySubstrateVocabularyNoHBMMixASPFCFBridge","entry_date":"2024-01-02","duplicate_status":"new C06 symbol/trigger/date combination outside recent R2 C06/C07/C08/C09 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"222800","trigger_type":"Stage2-FalsePositive-PCBSubstrateCapacityVocabularyNoHBMCustomerMixFCFBridge","entry_date":"2024-01-02","duplicate_status":"new C06 symbol/trigger/date combination outside recent R2 C06/C07/C08/C09 loop symbols; market-segment-change watch"}
```

## 4. Research question

C06 is not “HBM 사이클이 좋다.”
The useful C06 signal must prove the memory-capacity-to-cash chain:

```text
HBM memory customer demand or mix
qualified customer allocation
capacity expansion / bit or stack mix visibility
ASP or premium mix
yield / utilization
revenue revision
gross-margin / operating-margin bridge
FCF / cash conversion
capital allocation or holding-company discount repair when exposure is indirect
```

A memory-cycle headline without this bridge is a fab lit at night. The lights are real, but E2R needs wafers through the bottleneck, premium mix, customer allocation, margin and cash.

Residual question:

```text
Can C06 distinguish:
1. HBM memory capacity / customer-mix / FCF look-through bridge with strong MFE and shallow MAE,
2. memory substrate vocabulary where no HBM mix / ASP / FCF bridge exists,
3. PCB/substrate capacity vocabulary where market-segment noise and price decay block C06 promotion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C06_R2L93_402340_SKSQUARE_HBM_LOOKTHROUGH","symbol":"402340","company_name":"SK스퀘어","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_MIX_FCF_LOOKTHROUGH_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-HBMMemoryCustomerCapacityMixFCFLookthroughBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"positive_high_MFE90_and_MFE180_low_MAE_HBM_memory_capacity_lookthrough_bridge","current_profile_verdict":"current_profile_correct_if_HBM_mix_capacity_FCF_bridge_and_holdco_discount_repair_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"HBM memory capacity and customer-mix look-through proxy produced strong MFE with shallow MAE. Because this is indirect holdco exposure, Green still requires exact exposure, discount repair, cash-flow and capital allocation evidence."}
{"row_type":"case","case_id":"C06_R2L93_195870_HDS_SUBSTRATE_DECAY","symbol":"195870","company_name":"해성디에스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"MEMORY_PACKAGE_SUBSTRATE_VOCABULARY_WITHOUT_HBM_MIX_ASP_FCF_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-MemorySubstrateVocabularyNoHBMMixASPFCFBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_no_HBM_mix_FCF_bridge","current_profile_verdict":"current_profile_false_positive_if_memory_substrate_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Memory/package substrate vocabulary had near-zero forward MFE and deep MAE without HBM customer mix, ASP, utilization, revision or FCF bridge."}
{"row_type":"case","case_id":"C06_R2L93_222800_SIMMTECH_PCB_SUBSTRATE_CROSSLABEL","symbol":"222800","company_name":"심텍","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"PCB_SUBSTRATE_CAPACITY_VOCABULARY_WITHOUT_HBM_CUSTOMER_MIX_FCF_BRIDGE","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PCBSubstrateCapacityVocabularyNoHBMCustomerMixFCFBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_low_MFE_deep_MAE_market_segment_watch_no_HBM_customer_mix_bridge","current_profile_verdict":"current_profile_false_positive_if_PCB_substrate_capacity_vocabulary_counted_as_C06_memory_capacity_bridge","price_source":"Songdaiki/stock-web","notes":"PCB/substrate capacity vocabulary did not prove HBM memory customer capacity or FCF bridge. Price decay and market-segment change require 4B/data-quality watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 402340 SK스퀘어 — HBM memory capacity / customer mix / FCF look-through bridge

Entry row: `2024-02-01 c=53600`.
Observed path: early high `2024-03-22 h=81000`, full-window high `2024-10-28 h=97200`, and shallow early MAE.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C06_402340_20240201_STAGE2_HBM_MEMORY_LOOKTHROUGH","case_id":"C06_R2L93_402340_SKSQUARE_HBM_LOOKTHROUGH","symbol":"402340","company_name":"SK스퀘어","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_MIX_FCF_LOOKTHROUGH_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-HBMMemoryCustomerCapacityMixFCFLookthroughBridge-PositiveWatch","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":53600.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_HBM_memory_capacity_customer_mix_FCF_lookthrough_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; HBM memory capacity, customer mix, ASP/FCF and holdco discount repair treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["HBM_customer_capacity_proxy","HBM_mix_ASP_proxy","FCF_lookthrough_proxy","holdco_discount_repair_proxy"],"stage3_evidence_fields":["exact_HBM_capacity_source_pending","customer_mix_source_pending","ASP_margin_FCF_source_pending","capital_allocation_source_pending"],"stage4b_evidence_fields":["lookthrough_holdco_watch","Green_exact_evidence_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/402/402340/2024.csv","profile_path":"atlas/symbol_profiles/402/402340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":35.99,"MFE_90D_pct":51.12,"MFE_180D_pct":81.34,"MAE_30D_pct":-3.92,"MAE_90D_pct":-3.92,"MAE_180D_pct":-3.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-28","peak_price":97200.0,"max_drawdown_low_date":"2024-02-01","max_drawdown_low":51500.0,"drawdown_after_peak_pct":-25.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.37,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_HBM_capacity_customer_mix_ASP_FCF_and_holdco_discount_repair_evidence","four_b_evidence_type":["lookthrough_holdco_watch","Green_exact_evidence_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_and_MFE180_low_MAE_HBM_memory_capacity_lookthrough_bridge","current_profile_verdict":"current_profile_correct_if_HBM_mix_capacity_FCF_bridge_and_holdco_discount_repair_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["lookthrough_holdco_exposure_not_direct_memory_manufacturer"],"corporate_action_window_status":"clean","same_entry_group_id":"402340_2024-02-01_53600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C06 can allow Yellow/positive-watch when HBM memory strength is tied to customer capacity, premium mix, ASP/margin and FCF; indirect holdco exposure requires exact source repair before Green."}
```

### 6.2 195870 해성디에스 — memory/package substrate vocabulary without HBM mix / ASP / FCF bridge

Entry row: `2024-01-02 c=61500`.
Observed path: same-day high `2024-01-02 h=61700`, then long decline to `2024-09-24 l=27150` and `2024-11-14 l=20500`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C06_195870_20240102_STAGE2_FALSE_POSITIVE_SUBSTRATE_DECAY","case_id":"C06_R2L93_195870_HDS_SUBSTRATE_DECAY","symbol":"195870","company_name":"해성디에스","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"MEMORY_PACKAGE_SUBSTRATE_VOCABULARY_WITHOUT_HBM_MIX_ASP_FCF_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-MemorySubstrateVocabularyNoHBMMixASPFCFBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":61500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_memory_package_substrate_cycle_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; memory/package substrate vocabulary treated as insufficient without HBM customer allocation, premium mix, ASP, margin, utilization and FCF bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["memory_substrate_vocabulary","cycle_recovery_keyword","relative_strength_watch"],"stage3_evidence_fields":["HBM_customer_mix_missing","ASP_margin_bridge_missing","utilization_revision_missing","FCF_bridge_missing"],"stage4b_evidence_fields":["near_zero_MFE","deep_MAE","HBM_mix_FCF_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/195/195870/2024.csv","profile_path":"atlas/symbol_profiles/195/195870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.33,"MFE_90D_pct":0.33,"MFE_180D_pct":0.33,"MAE_30D_pct":-20.65,"MAE_90D_pct":-26.75,"MAE_180D_pct":-55.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":61700.0,"max_drawdown_low_date":"2024-11-14","max_drawdown_low":20500.0,"drawdown_after_peak_pct":-66.77,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_substrate_vocabulary_without_HBM_customer_mix_ASP_margin_FCF_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","deep_MAE","HBM_mix_FCF_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_HBM_mix_FCF_bridge","current_profile_verdict":"current_profile_false_positive_if_memory_substrate_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"195870_2024-01-02_61500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C06 should not promote memory substrate vocabulary unless HBM customer mix, ASP/margin, utilization revision and FCF evidence are exact-repaired. Near-zero MFE and deep MAE force Watch/4B."}
```

### 6.3 222800 심텍 — PCB/substrate capacity vocabulary without HBM customer mix / FCF bridge

Entry row: `2024-01-02 c=42200`.
Observed path: same-week high `2024-01-04 h=43100`, followed by persistent deterioration to `2024-12-09 l=9690`. Market flag moved from KOSDAQ to KOSDAQ GLOBAL after `2024-06-14`.

```jsonl
{"row_type":"trigger","trigger_id":"R2L93_C06_222800_20240102_STAGE2_FALSE_POSITIVE_PCB_SUBSTRATE_CAPACITY","case_id":"C06_R2L93_222800_SIMMTECH_PCB_SUBSTRATE_CROSSLABEL","symbol":"222800","company_name":"심텍","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"PCB_SUBSTRATE_CAPACITY_VOCABULARY_WITHOUT_HBM_CUSTOMER_MIX_FCF_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;data_quality_watch;cross_label_capacity_stress_test","trigger_type":"Stage2-FalsePositive-PCBSubstrateCapacityVocabularyNoHBMCustomerMixFCFBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":42200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_PCB_substrate_capacity_cycle_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; PCB/substrate capacity vocabulary treated as insufficient for C06 without HBM memory customer mix, ASP, utilization, revision and FCF bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["PCB_substrate_capacity_vocabulary","memory_cycle_keyword","relative_strength_rebound"],"stage3_evidence_fields":["HBM_customer_mix_missing","premium_ASP_missing","revision_visibility_missing","FCF_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE","deep_MAE","market_segment_change_watch","cross_label_substrate_not_memory_capacity_bridge"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/222/222800/2024.csv","profile_path":"atlas/symbol_profiles/222/222800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.13,"MFE_90D_pct":2.13,"MFE_180D_pct":2.13,"MAE_30D_pct":-22.75,"MAE_90D_pct":-33.06,"MAE_180D_pct":-57.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-04","peak_price":43100.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":9690.0,"drawdown_after_peak_pct":-77.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"PCB_substrate_capacity_vocabulary_without_HBM_memory_customer_mix_ASP_FCF_bridge_should_be_4B_watch_not_C06_positive; market_segment_change_requires_repair","four_b_evidence_type":["low_MFE","deep_MAE","market_segment_change_watch","cross_label_substrate_not_memory_capacity_bridge"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_market_segment_watch_no_HBM_customer_mix_bridge","current_profile_verdict":"current_profile_false_positive_if_PCB_substrate_capacity_vocabulary_counted_as_C06_memory_capacity_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["market_segment_change_watch_KOSDAQ_to_KOSDAQ_GLOBAL_after_2024-06-14","cross_label_substrate_not_direct_memory_capacity_bridge"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_usable; market_segment_change_watch","same_entry_group_id":"222800_2024-01-02_42200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C06 should not count PCB/substrate capacity vocabulary as HBM memory customer-capacity evidence unless customer mix, ASP/margin, utilization/revision and FCF bridge are exact-repaired. Market-segment rows need repair."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L93_402340_SKSQUARE_HBM_LOOKTHROUGH","trigger_id":"R2L93_C06_402340_20240201_STAGE2_HBM_MEMORY_LOOKTHROUGH","symbol":"402340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C06 requires HBM customer capacity, premium mix, ASP/margin, FCF and capital allocation or discount repair rather than memory-cycle vocabulary alone","raw_component_scores_before":{"HBM_customer_capacity_score":13,"customer_mix_score":12,"ASP_premium_score":12,"utilization_yield_score":10,"revenue_revision_score":10,"margin_bridge_score":10,"FCF_bridge_score":9,"capital_allocation_score":8,"relative_strength_score":14,"lookthrough_discount_risk":-4,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"HBM_customer_capacity_score":16,"customer_mix_score":15,"ASP_premium_score":15,"utilization_yield_score":12,"revenue_revision_score":12,"margin_bridge_score":12,"FCF_bridge_score":11,"capital_allocation_score":10,"relative_strength_score":15,"lookthrough_discount_risk":-3,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch/LookthroughWatch","component_delta_explanation":"HBM capacity/mix/FCF look-through bridge plus high MFE supports Green-candidate watch; indirect exposure and source-proxy evidence block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L93_195870_HDS_SUBSTRATE_DECAY","trigger_id":"R2L93_C06_195870_20240102_STAGE2_FALSE_POSITIVE_SUBSTRATE_DECAY","symbol":"195870","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_scope":"current_default_proxy","profile_hypothesis":"memory/package substrate vocabulary without HBM customer mix and FCF bridge should be blocked","raw_component_scores_before":{"HBM_customer_capacity_score":1,"customer_mix_score":0,"ASP_premium_score":0,"utilization_yield_score":0,"revenue_revision_score":0,"margin_bridge_score":0,"FCF_bridge_score":0,"capital_allocation_score":0,"relative_strength_score":1,"lookthrough_discount_risk":0,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"HBM_customer_capacity_score":0,"customer_mix_score":0,"ASP_premium_score":0,"utilization_yield_score":0,"revenue_revision_score":0,"margin_bridge_score":0,"FCF_bridge_score":0,"capital_allocation_score":0,"relative_strength_score":0,"lookthrough_discount_risk":0,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE require HBM mix/ASP/FCF evidence before any Yellow/Green promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_R2L93_222800_SIMMTECH_PCB_SUBSTRATE_CROSSLABEL","trigger_id":"R2L93_C06_222800_20240102_STAGE2_FALSE_POSITIVE_PCB_SUBSTRATE_CAPACITY","symbol":"222800","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_scope":"current_default_proxy","profile_hypothesis":"PCB/substrate capacity vocabulary and market-segment noise without HBM customer mix and FCF bridge should remain Watch/4B","raw_component_scores_before":{"HBM_customer_capacity_score":1,"customer_mix_score":0,"ASP_premium_score":0,"utilization_yield_score":0,"revenue_revision_score":0,"margin_bridge_score":0,"FCF_bridge_score":0,"capital_allocation_score":0,"relative_strength_score":1,"lookthrough_discount_risk":0,"theme_spike_risk":-14,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"HBM_customer_capacity_score":0,"customer_mix_score":0,"ASP_premium_score":0,"utilization_yield_score":0,"revenue_revision_score":0,"margin_bridge_score":0,"FCF_bridge_score":0,"capital_allocation_score":0,"relative_strength_score":0,"lookthrough_discount_risk":0,"theme_spike_risk":-22,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Low MFE, deep MAE and market-segment change block C06 promotion; substrate vocabulary is cross-label without memory-capacity bridge."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R2L93_C06_P0_CURRENT","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C06 needs explicit HBM customer capacity, premium mix, ASP/margin, FCF and cross-label substrate taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":17.86,"avg_MAE90_pct":-20.91,"avg_MFE180_pct":27.93,"avg_MAE180_pct":-38.95,"false_positive_rate":0.67,"data_quality_watch_count":1,"lookthrough_positive_watch_count":1,"score_return_alignment_verdict":"mixed_without_C06_HBM_mix_ASP_FCF_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C06_P1_SECTOR_SPECIFIC","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_id":"P1_L2_HBM_memory_capacity_mix_FCF_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L2 HBM memory-capacity signals need customer allocation, premium mix, ASP, utilization, revision, margin or FCF conversion before Stage2-Actionable","changed_axes":["HBM_customer_mix_required","ASP_margin_FCF_required","substrate_cross_label_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_capacity_mix_ASP_revision_margin_or_FCF_proxy"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C06_P2_CANONICAL","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_id":"P2_C06_HBM_mix_ASP_FCF_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C06 should reward memory customer-capacity to FCF mechanics, not substrate/PCB vocabulary","changed_axes":["C06_HBM_customer_mix_ASP_FCF_bridge_required","C06_substrate_PCB_vocabulary_local_4B_guard","C06_holdco_lookthrough_Green_strict_guard","C06_market_segment_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"HBM_capacity_or_customer_mix_plus_ASP_margin_or_FCF_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R2L93_C06_P3_COUNTEREXAMPLE_GUARD","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","profile_id":"P3_C06_near_zero_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If HBM mix/FCF bridge is missing, MFE90<5 or MAE90<=-20 blocks Yellow/Green and routes to Watch/4B","changed_axes":["C06_near_zero_MFE_guardrail","C06_deep_MAE_4B_guardrail","C06_cross_label_substrate_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_5_or_MAE90_le_minus20)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"C06_HBM_LOOKTHROUGH_POSITIVE_VS_SUBSTRATE_PCB_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":17.86,"avg_MAE90_pct":-20.91,"avg_MFE180_pct":27.93,"avg_MAE180_pct":-38.95,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE90_le_minus20":0.67,"interpretation":"C06 needs bridge discipline. SK스퀘어 shows HBM memory capacity/mix/FCF look-through can support Yellow/Green-candidate-watch, while 해성디에스 and 심텍 show memory substrate or PCB capacity vocabulary should not be promoted without HBM customer mix, premium ASP, utilization, revision, margin and FCF evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"402340","trigger_type":"Stage2-Actionable-HBMMemoryCustomerCapacityMixFCFLookthroughBridge-PositiveWatch","entry_date":"2024-02-01","stage2_to_90D_outcome":"positive_watch_high_MFE_low_MAE","stage2_to_180D_outcome":"HBM_capacity_lookthrough_bridge_but_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/Green-candidate when HBM customer capacity, premium mix, ASP/margin and FCF bridge exists; indirect holdco exposure requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"195870","trigger_type":"Stage2-FalsePositive-MemorySubstrateVocabularyNoHBMMixASPFCFBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_memory_substrate_vocabulary_no_HBM_mix_FCF_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Memory substrate vocabulary without HBM mix/ASP/margin/FCF evidence should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","symbol":"222800","trigger_type":"Stage2-FalsePositive-PCBSubstrateCapacityVocabularyNoHBMCustomerMixFCFBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE_market_segment_watch","stage2_to_180D_outcome":"failed_PCB_substrate_capacity_no_HBM_customer_mix_FCF_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"PCB/substrate vocabulary and market-segment change without HBM customer mix and FCF bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","residual_type":"substrate_PCB_vocabulary_overcredit_without_HBM_customer_mix_ASP_FCF_bridge","contribution":"Adds two C06 4B counterexamples against one HBM capacity/mix look-through positive-watch, selected because C06 is Priority-0 under-30 coverage.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_LOOKTHROUGH_BRIDGE_VS_SUBSTRATE_CAPACITY_CROSSLABEL_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C06 now has one HBM capacity/mix/FCF look-through positive-watch and two substrate/PCB weak-bridge counterexamples; next C06 loops should exact-URL repair customer allocation, HBM mix, ASP, utilization, margin, FCF and capital-allocation evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","axis":"C06_HBM_customer_mix_ASP_FCF_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"402340 worked when HBM capacity/mix/FCF look-through proxy existed; 195870 and 222800 failed when substrate/PCB vocabulary lacked HBM customer mix and FCF evidence."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","axis":"C06_substrate_PCB_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"195870 and 222800 showed near-zero/low MFE and deep MAE when memory substrate or PCB capacity vocabulary was not tied to HBM mix, ASP, margin and FCF."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","axis":"C06_holdco_lookthrough_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"402340 is a constructive HBM look-through row but not direct memory manufacturing; Green requires exact exposure, discount repair and capital-allocation evidence."}
{"row_type":"shadow_weight","round":"R2","loop":"93","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","axis":"C06_market_segment_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"222800 changed from KOSDAQ to KOSDAQ GLOBAL after selected entry, so production patching requires data-quality repair."}
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
  - substrate_PCB_vocabulary_overcredit
  - HBM_customer_mix_bridge_missing
  - ASP_margin_FCF_bridge_missing
  - holdco_lookthrough_Green_strict_watch
  - market_segment_change_watch
new_axis_proposed:
  - C06_HBM_customer_mix_ASP_FCF_bridge_required_shadow_only
  - C06_substrate_PCB_vocabulary_local_4B_guard_shadow_only
  - C06_holdco_lookthrough_Green_strict_guard_shadow_only
  - C06_market_segment_data_quality_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C06
  - full_4b_requires_non_price_evidence within C06
  - hard_4c_thesis_break_routes_to_4c within C06
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
`402340` has no corporate-action candidate and the selected 2024 window is clean, but the exposure is HBM-memory look-through rather than direct manufacturing.
`195870` has no corporate-action candidate and the selected 2024 window is clean.
`222800` has older corporate-action candidates before 2024 and a market-segment change from KOSDAQ to KOSDAQ GLOBAL after 2024-06-14, so it remains data-quality watch before patching.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
market_segment_change_watch = true for 222800
lookthrough_holdco_watch = true for 402340
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
3. Confirm R2 / L2 / C06 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop was selected by coverage-index-first after C08/C09/C01/C07 local expansions.
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
7. Confirm touched 031980/110990/067310 candidate rows are not ingested from this MD.
8. Keep 402340 as look-through/holdco Green-strict watch, not direct memory manufacturing evidence.
9. Keep 222800 in market-segment data-quality watch before patch consideration.
10. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C06-scoped safe patch candidates:
   - C06_HBM_customer_mix_ASP_FCF_bridge_required
   - C06_substrate_PCB_vocabulary_local_4B_guard
   - C06_holdco_lookthrough_Green_strict_guard
   - C06_market_segment_data_quality_guard
11. Do not loosen Stage3-Green.
12. Do not use future MFE/MAE in runtime scoring.
13. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R2
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE or remaining Priority-0 under-30 archetype
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 HBM memory capacity/mix/FCF look-through positive-watch, 2 substrate/PCB weak-bridge counterexamples, and 2 local 4B-watch rows for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.
```
