# E2R Stock-Web v12 Residual Research — R3 Loop 93 / L3 / C11

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 93
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: ELECTROLYTE_ORDERBOOK_FCF_RERATING_VS_CNT_COPPER_FOIL_BACKLOG_VOCABULARY_DECAY
sector: battery / EV / electrolyte / conductive additive / copper foil / orderbook / customer contract / margin / FCF conversion
output_file: e2r_stock_web_v12_residual_round_R3_loop_93_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after local loop93 expansions in C09, C01, C07, C06 and C10.

```text
selected_round = R3
selected_loop = 93
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
```

Reason for selecting C11:

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
```

Local run-stream hygiene:

```text
C08 was expanded in loop92.
C09, C01, C07, C06 and C10 were expanded in loop93.
C14 was expanded in loop92 by the local stream.
Therefore this run moves to C11, a still-thin Priority-0 battery archetype.
```

This loop avoids recent R3 symbols:

```text
R3 loop85 C11: 078600, 247540, 393890
R3 loop86 C12: 317330, 066970, 361610
R3 loop87 C13: 096770, 011790, 051910
R3 loop88 C14: 093370, 336370, 382840
R3 loop89 C11: 222080, 290670, 089980
R3 loop90 C12: 114190, 450080, 417200
R3 loop91 C13: 036830, 014820, 095500
R3 loop92 C14: 006110, 101360, 282880
```

Candidate hygiene note:

```text
During this execution path, recently used R2/C10 and earlier semiconductor candidate rows were touched by the tool stream.
They are excluded from this C11 output because the valid output must be R3/L3/C11.
```

Selected symbols:

```text
348370, 121600, 020150
```

The selected pocket is:

```text
electrolyte orderbook / overseas capacity / customer allocation / FCF bridge positive-watch
vs
CNT conductive-additive orderbook vocabulary after a spike without visible FCF bridge
vs
copper-foil orderbook vocabulary where EV demand and margin pressure block rerating
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"348370","company_name":"엔켐","profile_path":"atlas/symbol_profiles/348/348370.json","first_date":"2021-11-01","last_date":"2026-02-20","trading_day_count":1053,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"No corporate-action candidate in profile, but visible 2024 share-count movement in OHLC rows; keep share-count data-quality watch before production patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; share_count_movement_watch"}
{"row_type":"price_source_validation","symbol":"121600","company_name":"나노신소재","profile_path":"atlas/symbol_profiles/121/121600.json","first_date":"2011-02-09","last_date":"2026-02-20","trading_day_count":3697,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2015-12-17"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"020150","company_name":"롯데에너지머티리얼즈","profile_path":"atlas/symbol_profiles/020/020150.json","first_date":"2011-03-04","last_date":"2026-02-20","trading_day_count":3681,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Name changed from 일진머티리얼즈 to 롯데에너지머티리얼즈 in 2023, before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"348370","trigger_type":"Stage2-Actionable-ElectrolyteOrderbookOverseasCapacityFCFBridge-PositiveWatch","entry_date":"2024-01-29","duplicate_status":"new C11 symbol/trigger/date combination outside recent R3 C11/C12/C13/C14 loop symbols; share-count watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"121600","trigger_type":"Stage2-FalsePositive-CNTConductiveAdditiveOrderbookSpikeNoVisibleFCFBridge","entry_date":"2024-03-12","duplicate_status":"new C11 symbol/trigger/date combination outside recent R3 C11/C12/C13/C14 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"020150","trigger_type":"Stage2-FalsePositive-CopperFoilOrderbookVocabularyNoMarginFCFBridge","entry_date":"2024-01-02","duplicate_status":"new C11 symbol/trigger/date combination outside recent R3 C11/C12/C13/C14 loop symbols"}
```

## 4. Research question

C11 is not “배터리 수주잔고가 많다.”
The useful orderbook-rerating signal must prove the backlog-to-cash chain:

```text
credible customer contract or allocation
capacity ramp that matches customer demand
shipment or delivery visibility
ASP / mix quality
utilization and yield path
working-capital discipline
gross-margin / operating-margin bridge
FCF conversion
balance-sheet ability to fund ramp
```

A battery orderbook headline without this bridge is a warehouse full of cells with no cash register at the exit. E2R needs contract quality, shipment timing, margin and FCF.

Residual question:

```text
Can C11 distinguish:
1. electrolyte orderbook / overseas capacity bridge with strong MFE but share-count watch,
2. CNT conductive-additive vocabulary where a spike lacks visible FCF conversion,
3. copper-foil orderbook vocabulary where margin and EV-demand pressure block rerating?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C11_R3L93_348370_ENCHEM_ELECTROLYTE_ORDERBOOK","symbol":"348370","company_name":"엔켐","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_ORDERBOOK_OVERSEAS_CAPACITY_CUSTOMER_ALLOCATION_FCF_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ElectrolyteOrderbookOverseasCapacityFCFBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"positive_extreme_MFE90_but_share_count_watch_and_after_peak_drawdown","current_profile_verdict":"current_profile_correct_if_customer_allocation_capacity_margin_FCF_bridge_required_but_data_quality_and_Green_strict","price_source":"Songdaiki/stock-web","notes":"Electrolyte orderbook / overseas-capacity proxy produced extreme MFE90, but share-count movement and large after-peak drawdown keep this as positive-watch, not automatic Green."}
{"row_type":"case","case_id":"C11_R3L93_121600_NANO_CNT_SPIKE_NO_FCF","symbol":"121600","company_name":"나노신소재","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CNT_CONDUCTIVE_ADDITIVE_ORDERBOOK_SPIKE_WITHOUT_VISIBLE_FCF_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CNTConductiveAdditiveOrderbookSpikeNoVisibleFCFBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_post_spike_low_forward_MFE_deep_late_MAE_no_FCF_bridge","current_profile_verdict":"current_profile_false_positive_if_CNT_orderbook_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"CNT conductive-additive vocabulary after a spike had limited follow-through and deep later drawdown when FCF/margin conversion was not visible."}
{"row_type":"case","case_id":"C11_R3L93_020150_LEM_COPPER_FOIL_DECAY","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"COPPER_FOIL_ORDERBOOK_VOCABULARY_WITHOUT_MARGIN_FCF_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CopperFoilOrderbookVocabularyNoMarginFCFBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub20_MFE_deep_MAE_no_margin_FCF_bridge","current_profile_verdict":"current_profile_false_positive_if_copper_foil_orderbook_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Copper-foil orderbook vocabulary did not prove margin or FCF conversion. Sub-20 MFE and deep drawdown route this to Watch/4B."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 348370 엔켐 — electrolyte orderbook / overseas capacity / FCF bridge positive-watch

Entry row: `2024-01-29 c=169500`.
Observed path: entry low `2024-01-29 l=139500`, contest/valuation peak `2024-04-08 h=394500`, and later full-year low `2024-11-15 l=108000`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L93_C11_348370_20240129_STAGE2_ELECTROLYTE_ORDERBOOK_FCF","case_id":"C11_R3L93_348370_ENCHEM_ELECTROLYTE_ORDERBOOK","symbol":"348370","company_name":"엔켐","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_ORDERBOOK_OVERSEAS_CAPACITY_CUSTOMER_ALLOCATION_FCF_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test;data_quality_watch","trigger_type":"Stage2-Actionable-ElectrolyteOrderbookOverseasCapacityFCFBridge-PositiveWatch","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":169500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_electrolyte_orderbook_overseas_capacity_customer_allocation_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; electrolyte customer allocation, overseas capacity ramp, shipment, margin and FCF bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["electrolyte_orderbook_proxy","overseas_capacity_ramp_proxy","customer_allocation_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_contract_source_pending","capacity_ramp_source_pending","shipment_schedule_pending","margin_FCF_bridge_pending","share_count_repair_pending"],"stage4b_evidence_fields":["price_extension_watch","share_count_movement_watch","after_peak_drawdown_watch"],"stage4c_evidence_fields":["funding_dilution_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv","profile_path":"atlas/symbol_profiles/348/348370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":111.5,"MFE_90D_pct":132.74,"MFE_180D_pct":132.74,"MAE_30D_pct":-17.70,"MAE_90D_pct":-17.70,"MAE_180D_pct":-17.70,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":394500.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":108000.0,"drawdown_after_peak_pct":-72.62,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_customer_allocation_capacity_shipment_margin_FCF_and_share_count_repair","four_b_evidence_type":["price_extension_watch","share_count_movement_watch","after_peak_drawdown_watch"],"four_c_protection_label":"funding_dilution_watch_only","trigger_outcome_label":"positive_extreme_MFE90_but_share_count_watch_and_after_peak_drawdown","current_profile_verdict":"current_profile_correct_if_customer_allocation_capacity_margin_FCF_bridge_required_but_data_quality_and_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["visible_2024_share_count_movement_watch"],"corporate_action_window_status":"no_profile_CA_candidate; share_count_movement_watch","same_entry_group_id":"348370_2024-01-29_169500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C11 can allow Yellow/Green-candidate-watch when orderbook strength is tied to customer allocation, capacity ramp, shipment, margin and FCF. Share-count movement and after-peak drawdown require repair before Green."}
```

### 6.2 121600 나노신소재 — CNT conductive-additive orderbook spike without visible FCF bridge

Entry row: `2024-03-12 c=142800`, after the February CNT/orderbook spike.
Observed path: local high `2024-03-19 h=151600`, then deterioration to `2024-12-27 l=57800`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L93_C11_121600_20240312_STAGE2_FALSE_POSITIVE_CNT_SPIKE_NO_FCF","case_id":"C11_R3L93_121600_NANO_CNT_SPIKE_NO_FCF","symbol":"121600","company_name":"나노신소재","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CNT_CONDUCTIVE_ADDITIVE_ORDERBOOK_SPIKE_WITHOUT_VISIBLE_FCF_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;post_spike_entry_guard","trigger_type":"Stage2-FalsePositive-CNTConductiveAdditiveOrderbookSpikeNoVisibleFCFBridge","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":142800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_CNT_conductive_additive_orderbook_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; CNT conductive additive orderbook vocabulary treated as insufficient without shipment schedule, ASP/mix, working-capital and FCF bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["CNT_conductive_additive_keyword","orderbook_vocabulary","post_spike_relative_strength"],"stage3_evidence_fields":["shipment_schedule_missing","ASP_mix_bridge_missing","working_capital_bridge_missing","FCF_conversion_missing"],"stage4b_evidence_fields":["low_forward_MFE_after_spike","deep_late_MAE","FCF_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv","profile_path":"atlas/symbol_profiles/121/121600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.16,"MFE_90D_pct":6.16,"MFE_180D_pct":6.16,"MAE_30D_pct":-18.77,"MAE_90D_pct":-18.77,"MAE_180D_pct":-43.28,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-19","peak_price":151600.0,"max_drawdown_low_date":"2024-12-27","max_drawdown_low":57800.0,"drawdown_after_peak_pct":-61.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"CNT_orderbook_spike_without_visible_ASP_margin_working_capital_FCF_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_forward_MFE_after_spike","deep_late_MAE","FCF_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_post_spike_low_forward_MFE_deep_late_MAE_no_FCF_bridge","current_profile_verdict":"current_profile_false_positive_if_CNT_orderbook_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"121600_2024-03-12_142800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C11 should not promote CNT/orderbook vocabulary after a spike unless shipment schedule, ASP/mix, working-capital and FCF conversion are exact-repaired. Low forward MFE and deep later MAE force Watch/4B routing."}
```

### 6.3 020150 롯데에너지머티리얼즈 — copper-foil orderbook vocabulary without margin / FCF bridge

Entry row: `2024-01-02 c=41500`.
Observed path: local high `2024-03-21 h=49200`, then persistent decline to `2024-12-09 l=20900`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L93_C11_020150_20240102_STAGE2_FALSE_POSITIVE_COPPER_FOIL_ORDERBOOK","case_id":"C11_R3L93_020150_LEM_COPPER_FOIL_DECAY","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"COPPER_FOIL_ORDERBOOK_VOCABULARY_WITHOUT_MARGIN_FCF_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-CopperFoilOrderbookVocabularyNoMarginFCFBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":41500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_copper_foil_orderbook_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; copper-foil orderbook vocabulary treated as insufficient without ASP/margin, utilization, shipment, working-capital and FCF bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["copper_foil_orderbook_keyword","battery_material_recovery_vocabulary","relative_strength_rebound"],"stage3_evidence_fields":["ASP_margin_bridge_missing","utilization_bridge_missing","working_capital_bridge_missing","FCF_conversion_missing"],"stage4b_evidence_fields":["sub20_MFE","deep_MAE","margin_FCF_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv","profile_path":"atlas/symbol_profiles/020/020150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.69,"MFE_90D_pct":18.55,"MFE_180D_pct":18.55,"MAE_30D_pct":-24.34,"MAE_90D_pct":-24.34,"MAE_180D_pct":-24.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":49200.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":20900.0,"drawdown_after_peak_pct":-57.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.09,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"copper_foil_orderbook_vocabulary_without_ASP_margin_working_capital_FCF_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["sub20_MFE","deep_MAE","margin_FCF_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub20_MFE_deep_MAE_no_margin_FCF_bridge","current_profile_verdict":"current_profile_false_positive_if_copper_foil_orderbook_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean; 2023_name_change_before_entry","same_entry_group_id":"020150_2024-01-02_41500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C11 should not count copper-foil orderbook vocabulary as rerating evidence unless ASP/margin, utilization, working-capital and FCF conversion are exact-repaired. Sub-20 MFE and deep drawdown require Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3L93_348370_ENCHEM_ELECTROLYTE_ORDERBOOK","trigger_id":"R3L93_C11_348370_20240129_STAGE2_ELECTROLYTE_ORDERBOOK_FCF","symbol":"348370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C11 requires customer allocation, capacity ramp, shipment, ASP/mix, margin and FCF bridge rather than orderbook vocabulary alone","raw_component_scores_before":{"orderbook_quality_score":14,"customer_allocation_score":13,"capacity_ramp_score":13,"shipment_schedule_score":10,"ASP_mix_score":10,"utilization_yield_score":8,"margin_bridge_score":10,"working_capital_score":7,"FCF_bridge_score":7,"relative_strength_score":16,"funding_dilution_risk":-6,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow-Watch/DataQualityWatch","raw_component_scores_after":{"orderbook_quality_score":17,"customer_allocation_score":16,"capacity_ramp_score":16,"shipment_schedule_score":12,"ASP_mix_score":12,"utilization_yield_score":10,"margin_bridge_score":12,"working_capital_score":9,"FCF_bridge_score":9,"relative_strength_score":17,"funding_dilution_risk":-5,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":91,"stage_label_after":"Stage3-Green-candidate-watch/DataQualityWatch","component_delta_explanation":"Electrolyte orderbook/capacity bridge plus extreme MFE supports Green-candidate watch; share-count movement, funding risk and source-proxy evidence block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3L93_121600_NANO_CNT_SPIKE_NO_FCF","trigger_id":"R3L93_C11_121600_20240312_STAGE2_FALSE_POSITIVE_CNT_SPIKE_NO_FCF","symbol":"121600","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_scope":"current_default_proxy","profile_hypothesis":"CNT/orderbook spike without visible working-capital and FCF bridge should be blocked","raw_component_scores_before":{"orderbook_quality_score":3,"customer_allocation_score":1,"capacity_ramp_score":2,"shipment_schedule_score":0,"ASP_mix_score":1,"utilization_yield_score":0,"margin_bridge_score":0,"working_capital_score":0,"FCF_bridge_score":0,"relative_strength_score":5,"funding_dilution_risk":-8,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"orderbook_quality_score":1,"customer_allocation_score":0,"capacity_ramp_score":0,"shipment_schedule_score":0,"ASP_mix_score":0,"utilization_yield_score":0,"margin_bridge_score":0,"working_capital_score":0,"FCF_bridge_score":0,"relative_strength_score":1,"funding_dilution_risk":-16,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low forward MFE and deep later MAE require shipment, margin and FCF evidence before any Yellow/Green promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3L93_020150_LEM_COPPER_FOIL_DECAY","trigger_id":"R3L93_C11_020150_20240102_STAGE2_FALSE_POSITIVE_COPPER_FOIL_ORDERBOOK","symbol":"020150","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_scope":"current_default_proxy","profile_hypothesis":"copper-foil orderbook vocabulary without ASP/margin and FCF conversion should remain Watch/4B","raw_component_scores_before":{"orderbook_quality_score":2,"customer_allocation_score":1,"capacity_ramp_score":2,"shipment_schedule_score":0,"ASP_mix_score":0,"utilization_yield_score":0,"margin_bridge_score":0,"working_capital_score":0,"FCF_bridge_score":0,"relative_strength_score":3,"funding_dilution_risk":-6,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"orderbook_quality_score":0,"customer_allocation_score":0,"capacity_ramp_score":0,"shipment_schedule_score":0,"ASP_mix_score":0,"utilization_yield_score":0,"margin_bridge_score":0,"working_capital_score":0,"FCF_bridge_score":0,"relative_strength_score":0,"funding_dilution_risk":-12,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-20 MFE and deep MAE require ASP/margin, working-capital and FCF bridge before any promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L93_C11_P0_CURRENT","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C11 needs explicit customer allocation, capacity ramp, shipment, ASP/margin, working-capital and FCF bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":52.48,"avg_MAE90_pct":-20.27,"avg_MFE180_pct":52.48,"avg_MAE180_pct":-28.44,"false_positive_rate":0.67,"data_quality_watch_count":1,"share_count_watch_count":1,"score_return_alignment_verdict":"mixed_without_C11_orderbook_margin_FCF_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R3L93_C11_P1_SECTOR_SPECIFIC","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_id":"P1_L3_battery_orderbook_margin_FCF_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 battery orderbook signals need customer allocation, shipment, ASP/mix, utilization, margin or FCF conversion before Stage2-Actionable","changed_axes":["customer_allocation_required","margin_FCF_required","share_count_funding_watch"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_allocation_shipment_ASP_margin_or_FCF_proxy"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R3L93_C11_P2_CANONICAL","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_id":"P2_C11_orderbook_margin_FCF_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C11 should reward orderbook-to-FCF mechanics, not battery-material orderbook vocabulary","changed_axes":["C11_customer_allocation_capacity_margin_FCF_bridge_required","C11_CNT_copper_foil_vocabulary_local_4B_guard","C11_share_count_funding_data_quality_guard","C11_after_peak_drawdown_Green_strict_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_allocation_or_capacity_plus_margin_or_FCF_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R3L93_C11_P3_COUNTEREXAMPLE_GUARD","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_id":"P3_C11_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If margin/FCF bridge is missing, MFE90<20 or MAE90<=-20 blocks Yellow/Green and routes to Watch/4B","changed_axes":["C11_low_MFE_guardrail","C11_deep_MAE_4B_guardrail","C11_FCF_bridge_missing_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_MAE90_le_minus20)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_ELECTROLYTE_POSITIVE_VS_CNT_COPPER_FOIL_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":52.48,"avg_MAE90_pct":-20.27,"avg_MFE180_pct":52.48,"avg_MAE180_pct":-28.44,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE90_le_minus20":0.33,"interpretation":"C11 needs bridge discipline. 엔켐 shows electrolyte orderbook/capacity/customer allocation can support Green-candidate-watch after evidence and share-count repair, while 나노신소재 and 롯데에너지머티리얼즈 show CNT/copper-foil orderbook vocabulary should not be promoted without ASP/margin, working-capital and FCF conversion."}
{"row_type":"stage_transition_summary","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"348370","trigger_type":"Stage2-Actionable-ElectrolyteOrderbookOverseasCapacityFCFBridge-PositiveWatch","entry_date":"2024-01-29","stage2_to_90D_outcome":"positive_extreme_MFE90_but_data_quality_watch","stage2_to_180D_outcome":"orderbook_capacity_positive_but_after_peak_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/Green-candidate when electrolyte orderbook strength is tied to customer allocation, capacity ramp, margin and FCF; share-count and exact evidence repair required."}
{"row_type":"stage_transition_summary","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"121600","trigger_type":"Stage2-FalsePositive-CNTConductiveAdditiveOrderbookSpikeNoVisibleFCFBridge","entry_date":"2024-03-12","stage2_to_90D_outcome":"bad_stage2_low_forward_MFE_after_spike","stage2_to_180D_outcome":"failed_CNT_orderbook_spike_no_FCF_bridge_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"CNT/orderbook vocabulary after a spike without visible FCF bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"020150","trigger_type":"Stage2-FalsePositive-CopperFoilOrderbookVocabularyNoMarginFCFBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_sub20_MFE_deep_MAE","stage2_to_180D_outcome":"failed_copper_foil_orderbook_vocabulary_no_margin_FCF_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Copper-foil orderbook vocabulary without ASP/margin and FCF conversion should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","residual_type":"CNT_copper_foil_orderbook_vocabulary_overcredit_without_margin_FCF_bridge","contribution":"Adds two C11 4B counterexamples against one electrolyte orderbook/capacity positive-watch, selected because C11 is Priority-0 under-30 coverage.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_ORDERBOOK_FCF_RERATING_VS_CNT_COPPER_FOIL_BACKLOG_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C11 now has one electrolyte orderbook/capacity positive-watch and two CNT/copper-foil weak-bridge counterexamples; next C11 loops should exact-URL repair customer contract, capacity ramp, shipment, ASP/mix, working capital, margin and FCF evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","axis":"C11_customer_allocation_capacity_margin_FCF_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"348370 worked when electrolyte orderbook/capacity proxy existed; 121600 and 020150 failed when FCF/margin bridge was missing."}
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","axis":"C11_CNT_copper_foil_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"121600 and 020150 showed weak/sub20 forward MFE or deep MAE when orderbook vocabulary was not tied to FCF conversion."}
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","axis":"C11_share_count_funding_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"348370 has visible 2024 share-count movement despite no profile-level corporate-action candidate, so production patching requires price-path/evidence repair."}
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","axis":"C11_after_peak_drawdown_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"348370 had extreme MFE but also large after-peak drawdown; Green requires exact contract, shipment, margin and FCF evidence."}
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
  - CNT_orderbook_vocabulary_overcredit
  - copper_foil_orderbook_vocabulary_overcredit
  - margin_FCF_bridge_missing
  - post_spike_entry_guard
  - share_count_funding_data_quality_watch
new_axis_proposed:
  - C11_customer_allocation_capacity_margin_FCF_bridge_required_shadow_only
  - C11_CNT_copper_foil_vocabulary_local_4B_guard_shadow_only
  - C11_share_count_funding_data_quality_guard_shadow_only
  - C11_after_peak_drawdown_Green_strict_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C11
  - full_4b_requires_non_price_evidence within C11
  - hard_4c_thesis_break_routes_to_4c within C11
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
`348370` has no profile-level corporate-action candidate but visible 2024 share-count movement in the OHLC rows, so it remains share-count data-quality watch before production patching.
`121600` has an older 2015 corporate-action candidate before selected 2024 window; the selected 2024 window is usable.
`020150` has no corporate-action candidate in its profile, and the 2023 name change occurred before the selected 2024 window.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
share_count_watch = true for 348370
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
3. Confirm R3 / L3 / C11 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop was selected by coverage-index-first after C08/C09/C01/C07/C06/C10 local expansions.
6. Confirm this loop avoided:
   - previous R3 loop85 C11 symbols
   - previous R3 loop86 C12 symbols
   - previous R3 loop87 C13 symbols
   - previous R3 loop88 C14 symbols
   - previous R3 loop89 C11 symbols
   - previous R3 loop90 C12 symbols
   - previous R3 loop91 C13 symbols
   - previous R3 loop92 C14 symbols
7. Confirm touched R2/C10 and earlier semiconductor candidate rows are not ingested from this MD.
8. Keep 348370 in share-count/funding data-quality watch before patch consideration.
9. Treat 121600 and 020150 as weak-bridge failure modes unless exact shipment/margin/FCF evidence is added later.
10. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C11-scoped safe patch candidates:
   - C11_customer_allocation_capacity_margin_FCF_bridge_required
   - C11_CNT_copper_foil_vocabulary_local_4B_guard
   - C11_share_count_funding_data_quality_guard
   - C11_after_peak_drawdown_Green_strict_guard
11. Do not loosen Stage3-Green.
12. Do not use future MFE/MAE in runtime scoring.
13. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R3
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C19_BRAND_RETAIL_INVENTORY_MARGIN or C27_CONTENT_IP_GLOBAL_MONETIZATION or remaining Priority-0 under-30 archetype
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 electrolyte orderbook/FCF positive-watch, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.
```
