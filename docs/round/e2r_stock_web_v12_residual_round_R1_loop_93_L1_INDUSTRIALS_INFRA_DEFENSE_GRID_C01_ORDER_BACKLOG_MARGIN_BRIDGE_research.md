# E2R Stock-Web v12 Residual Research — R1 Loop 93 / L1 / C01

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R1
loop: 93
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_ORDER_BACKLOG_MARGIN_BRIDGE_VS_WEAK_BACKLOG_LATE_SPIKE_AND_FALSE_OVERBLOCK
sector: industrials / order backlog / shipbuilding / industrial orderbook / margin bridge / working capital / cash conversion
output_file: e2r_stock_web_v12_residual_round_R1_loop_93_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after completed `R13 loop 92`.

```text
selected_round = R1
selected_loop = 93
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

Reason for selecting C01:

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
C09 was expanded in loop93 immediately before this corrected output.
Therefore this run moves to the next still-thin Priority 0 archetype: C01.
```

Candidate hygiene note:

```text
During this execution path, a stale duplicate C09 file was touched before correcting to C01.
That duplicate C09 output is not the valid output for this user request.
The valid output is this R1/C01 loop93 MD.
```

Selected symbols:

```text
329180, 097230, 010620
```

The selected pocket is:

```text
shipbuilding / industrial order backlog and margin bridge
vs
weak backlog vocabulary and late spike that does not validate the original entry
vs
overbroad margin-gap block that would miss a post-reset orderbook/margin-recovery bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"329180","company_name":"HD현대중공업","profile_path":"atlas/symbol_profiles/329/329180.json","first_date":"2021-09-17","last_date":"2026-02-20","trading_day_count":1080,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"097230","company_name":"HJ중공업","profile_path":"atlas/symbol_profiles/097/097230.json","first_date":"2007-08-31","last_date":"2026-02-20","trading_day_count":4493,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2013-04-05","2014-08-29","2019-05-21","2019-05-23"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; late_spike_nonvalidation_watch"}
{"row_type":"price_source_validation","symbol":"010620","company_name":"HD현대미포","profile_path":"atlas/symbol_profiles/010/010620.json","first_date":"1995-05-02","last_date":"2025-11-26","trading_day_count":7707,"corporate_action_candidate_count":"profile_tail_not_fetched_in_this_run","corporate_action_candidate_dates":"historical_candidates_before_2024; 2024_name_transition_watch","has_major_raw_discontinuity":true,"calibration_caveat":"Historical candidates before selected 2024 window; name changed from 현대미포조선 to HD현대미포 on 2024-04-15, after selected 2024-03-14 entry. Keep data-quality/name-transition watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_entry_before_2024_name_transition; data_quality_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"329180","trigger_type":"Stage2-Actionable-ShipbuildingOrderBacklogMarginBridge-Positive","entry_date":"2024-04-18","duplicate_status":"new C01 symbol/trigger/date combination; selected after C09 duplicate touch was discarded"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"097230","trigger_type":"Stage2-FalsePositive-WeakBacklogVocabularyLateSpikeNoOriginalMarginBridge","entry_date":"2024-01-02","duplicate_status":"new C01 symbol/trigger/date combination; late spike requires fresh trigger evidence"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"010620","trigger_type":"Stage2-FalsePositive-OverbroadMarginGapWouldMissPostResetOrderbookMarginBridge","entry_date":"2024-03-14","duplicate_status":"new C01 symbol/trigger/date combination; false-overblock bridge repair case with 2024 name-transition watch"}
```

## 4. Research question

C01 is not “수주잔고가 많다.”
The useful order-backlog signal must prove the backlog-to-margin chain:

```text
credible order backlog
customer / vessel / project mix
delivery schedule
price-cost spread or escalation
utilization / production slot visibility
margin bridge
working-capital discipline
cash conversion
```

A backlog headline without this bridge is a shipyard filled with steel plates but no launch schedule. E2R needs the hull number, slot, price, cost discipline, margin and cash.

Residual question:

```text
Can C01 distinguish:
1. shipbuilding orderbook / margin bridge with high MFE and controlled MAE,
2. weak backlog vocabulary where later price spike does not validate the original entry,
3. overbroad margin-gap blocking that would miss a post-reset orderbook / margin-recovery bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C01_R1L93_329180_HDHHI_SHIPBUILDING_BACKLOG","symbol":"329180","company_name":"HD현대중공업","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_DELIVERY_MARGIN_CASH_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ShipbuildingOrderBacklogMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_extreme_MFE180_low_MAE_orderbook_margin_bridge","current_profile_verdict":"current_profile_correct_if_orderbacklog_delivery_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"Shipbuilding orderbook/margin bridge proxy produced high MFE and shallow entry MAE. Green still requires exact backlog, delivery, margin and cash evidence."}
{"row_type":"case","case_id":"C01_R1L93_097230_HJ_WEAK_BACKLOG_LATE_SPIKE","symbol":"097230","company_name":"HJ중공업","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"WEAK_BACKLOG_VOCABULARY_LATE_SPIKE_WITHOUT_ORIGINAL_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-WeakBacklogVocabularyLateSpikeNoOriginalMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_late_spike_not_original_backlog_margin_validation","current_profile_verdict":"current_profile_false_positive_if_late_spike_validates_original_weak_backlog_entry","price_source":"Songdaiki/stock-web","notes":"Weak backlog/turnaround vocabulary had low forward MFE and deep drawdown. Late November/December spike requires fresh trigger evidence and cannot validate the original entry."}
{"row_type":"case","case_id":"C01_R1L93_010620_HMD_FALSE_OVERBLOCK","symbol":"010620","company_name":"HD현대미포","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"POST_RESET_ORDERBOOK_MARGIN_BRIDGE_FALSE_OVERBLOCK","case_type":"false_overblock","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-OverbroadMarginGapWouldMissPostResetOrderbookMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"false_overblock_high_MFE_low_MAE_after_reset_if_orderbook_margin_bridge_exists","current_profile_verdict":"current_profile_false_positive_if_margin_gap_guard_blocks_reset_plus_orderbook_margin_recovery","price_source":"Songdaiki/stock-web","notes":"After a reset, HD현대미포 showed strong MFE from orderbook/margin-recovery proxy. Broad C01 blocking would be too blunt; exact evidence and name-transition repair are still required."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 329180 HD현대중공업 — shipbuilding orderbook / delivery / margin bridge positive-control

Entry row: `2024-04-18 c=120300`.
Observed path: entry low `2024-04-18 l=112500`, midyear high `2024-07-17 h=175000`, and full-window high `2024-12-26 h=299000`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L93_C01_329180_20240418_STAGE2_SHIPBUILDING_BACKLOG_MARGIN","case_id":"C01_R1L93_329180_HDHHI_SHIPBUILDING_BACKLOG","symbol":"329180","company_name":"HD현대중공업","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_DELIVERY_MARGIN_CASH_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ShipbuildingOrderBacklogMarginBridge-Positive","trigger_date":"2024-04-18","entry_date":"2024-04-18","entry_price":120300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_shipbuilding_orderbook_delivery_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; shipbuilding backlog, vessel mix, delivery slot, price-cost spread, margin and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["orderbacklog_proxy","delivery_slot_proxy","ship_mix_proxy","margin_recovery_proxy"],"stage3_evidence_fields":["exact_backlog_source_pending","delivery_schedule_source_pending","price_cost_spread_source_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","Green_exact_evidence_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv","profile_path":"atlas/symbol_profiles/329/329180.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.03,"MFE_90D_pct":45.47,"MFE_180D_pct":148.55,"MAE_30D_pct":-6.48,"MAE_90D_pct":-6.48,"MAE_180D_pct":-6.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-26","peak_price":299000.0,"max_drawdown_low_date":"2024-04-18","max_drawdown_low":112500.0,"drawdown_after_peak_pct":-3.18,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.14,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_backlog_delivery_price_cost_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","Green_exact_evidence_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_extreme_MFE180_low_MAE_orderbook_margin_bridge","current_profile_verdict":"current_profile_correct_if_orderbacklog_delivery_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"329180_2024-04-18_120300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C01 can allow Stage2/Yellow or Green-candidate-watch when backlog strength is tied to delivery, price-cost spread, margin and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 097230 HJ중공업 — weak backlog vocabulary and late spike non-validation

Entry row: `2024-01-02 c=4040`.
Observed path: local high `2024-01-02 h=4310`, 180D-zone decline toward the 2,600~2,700 range, and later full-year spike to `2024-12-23 h=7190`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L93_C01_097230_20240102_STAGE2_FALSE_POSITIVE_WEAK_BACKLOG_LATE_SPIKE","case_id":"C01_R1L93_097230_HJ_WEAK_BACKLOG_LATE_SPIKE","symbol":"097230","company_name":"HJ중공업","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"WEAK_BACKLOG_VOCABULARY_LATE_SPIKE_WITHOUT_ORIGINAL_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;late_spike_not_entry_validation","trigger_type":"Stage2-FalsePositive-WeakBacklogVocabularyLateSpikeNoOriginalMarginBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":4040.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_shipbuilding_or_construction_backlog_turnaround_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; backlog/turnaround vocabulary treated as insufficient without signed order quality, delivery schedule, margin repair and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["backlog_turnaround_vocabulary","industrial_order_keyword","relative_strength_watch"],"stage3_evidence_fields":["signed_order_quality_missing","delivery_schedule_missing","margin_cash_bridge_missing","working_capital_bridge_missing"],"stage4b_evidence_fields":["low_forward_MFE","deep_MAE","late_spike_not_entry_validation"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv","profile_path":"atlas/symbol_profiles/097/097230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.68,"MFE_90D_pct":6.68,"MFE_180D_pct":6.68,"MAE_30D_pct":-14.73,"MAE_90D_pct":-25.62,"MAE_180D_pct":-33.66,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":4310.0,"max_drawdown_low_date":"2024-09-24","max_drawdown_low":2680.0,"drawdown_after_peak_pct":-49.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.60,"four_b_timing_verdict":"late_November_December_spike_requires_fresh_trigger_and_does_not_validate_original_backlog_margin_bridge","four_b_evidence_type":["low_forward_MFE","deep_MAE","late_spike_not_entry_validation"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_late_spike_not_original_backlog_margin_validation","current_profile_verdict":"current_profile_false_positive_if_late_spike_validates_original_weak_backlog_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"097230_2024-01-02_4040","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C01 should not let a late price spike retroactively validate an original weak backlog/margin entry. A late move needs a fresh trigger and fresh order/margin/cash evidence."}
```

### 6.3 010620 HD현대미포 — post-reset orderbook / margin bridge false-overblock

Entry row: `2024-03-14 c=65000`, after a long drawdown/reset.
Observed path: later high `2024-12-23 h=142500` and shallow entry-zone MAE. Name changed after entry, so patching requires data-quality repair.

```jsonl
{"row_type":"trigger","trigger_id":"R1L93_C01_010620_20240314_STAGE2_FALSE_OVERBLOCK_ORDERBOOK_MARGIN_RESET","case_id":"C01_R1L93_010620_HMD_FALSE_OVERBLOCK","symbol":"010620","company_name":"HD현대미포","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"POST_RESET_ORDERBOOK_MARGIN_BRIDGE_FALSE_OVERBLOCK","loop_objective":"false_overblock_mining;counterexample_mining;data_quality_watch","trigger_type":"Stage2-FalsePositive-OverbroadMarginGapWouldMissPostResetOrderbookMarginBridge","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":65000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_shipbuilding_orderbook_margin_recovery_after_reset_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; post-reset shipbuilding backlog, vessel mix, margin recovery and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["orderbook_recovery_proxy","valuation_reset_proxy","margin_recovery_proxy","relative_strength_recovery"],"stage3_evidence_fields":["exact_backlog_source_pending","vessel_mix_source_pending","margin_recovery_source_pending","cash_conversion_pending","name_transition_repair_pending"],"stage4b_evidence_fields":["false_overblock_watch","data_quality_name_transition_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv","profile_path":"atlas/symbol_profiles/010/010620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.46,"MFE_90D_pct":12.46,"MFE_180D_pct":119.23,"MAE_30D_pct":-5.85,"MAE_90D_pct":-5.85,"MAE_180D_pct":-5.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-23","peak_price":142500.0,"max_drawdown_low_date":"2024-03-29","max_drawdown_low":61700.0,"drawdown_after_peak_pct":-5.89,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.05,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"do_not_overblock_after_reset_if_orderbook_margin_recovery_bridge_exists_but_exact_evidence_and_name_transition_repair_required","four_b_evidence_type":["false_overblock_watch","data_quality_name_transition_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"false_overblock_high_MFE_low_MAE_after_reset_if_orderbook_margin_bridge_exists","current_profile_verdict":"current_profile_false_positive_if_margin_gap_guard_blocks_reset_plus_orderbook_margin_recovery","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024-04-15_name_transition_watch_before_patch"],"corporate_action_window_status":"selected_entry_before_2024_name_transition; data_quality_watch","same_entry_group_id":"010620_2024-03-14_65000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C01 should not become a blanket margin-gap veto. If valuation has reset and backlog/mix/margin recovery is visible, route to evidence repair rather than hard 4B; name-transition repair is still required."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_R1L93_329180_HDHHI_SHIPBUILDING_BACKLOG","trigger_id":"R1L93_C01_329180_20240418_STAGE2_SHIPBUILDING_BACKLOG_MARGIN","symbol":"329180","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C01 requires order backlog, delivery schedule, mix, margin and cash bridge rather than backlog label alone","raw_component_scores_before":{"order_backlog_score":14,"customer_project_quality_score":12,"delivery_schedule_score":12,"mix_quality_score":11,"price_cost_spread_score":10,"utilization_score":10,"margin_bridge_score":11,"working_capital_score":8,"cash_conversion_score":8,"relative_strength_score":13,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"order_backlog_score":17,"customer_project_quality_score":15,"delivery_schedule_score":15,"mix_quality_score":13,"price_cost_spread_score":13,"utilization_score":12,"margin_bridge_score":14,"working_capital_score":10,"cash_conversion_score":10,"relative_strength_score":14,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":90,"stage_label_after":"Stage3-Green-candidate-watch","component_delta_explanation":"Backlog/delivery/margin bridge plus high MFE supports Green-candidate watch; exact source-grade evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_R1L93_097230_HJ_WEAK_BACKLOG_LATE_SPIKE","trigger_id":"R1L93_C01_097230_20240102_STAGE2_FALSE_POSITIVE_WEAK_BACKLOG_LATE_SPIKE","symbol":"097230","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_scope":"current_default_proxy","profile_hypothesis":"weak backlog vocabulary without margin/cash bridge should be blocked even if a later spike appears","raw_component_scores_before":{"order_backlog_score":2,"customer_project_quality_score":1,"delivery_schedule_score":0,"mix_quality_score":0,"price_cost_spread_score":0,"utilization_score":0,"margin_bridge_score":0,"working_capital_score":0,"cash_conversion_score":0,"relative_strength_score":2,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"order_backlog_score":0,"customer_project_quality_score":0,"delivery_schedule_score":0,"mix_quality_score":0,"price_cost_spread_score":0,"utilization_score":0,"margin_bridge_score":0,"working_capital_score":0,"cash_conversion_score":0,"relative_strength_score":0,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low forward MFE and deep MAE require Watch/4B; late spike needs fresh trigger evidence."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_R1L93_010620_HMD_FALSE_OVERBLOCK","trigger_id":"R1L93_C01_010620_20240314_STAGE2_FALSE_OVERBLOCK_ORDERBOOK_MARGIN_RESET","symbol":"010620","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_scope":"current_default_proxy","profile_hypothesis":"post-reset backlog/margin recovery bridge should override broad margin-gap blocking","raw_component_scores_before":{"order_backlog_score":10,"customer_project_quality_score":9,"delivery_schedule_score":8,"mix_quality_score":9,"price_cost_spread_score":7,"utilization_score":8,"margin_bridge_score":8,"working_capital_score":7,"cash_conversion_score":6,"relative_strength_score":8,"execution_risk_score":-6,"theme_spike_risk":-4,"information_confidence":4},"weighted_score_before":65,"stage_label_before":"Stage2-Watch/FalseOverblock","raw_component_scores_after":{"order_backlog_score":13,"customer_project_quality_score":12,"delivery_schedule_score":11,"mix_quality_score":12,"price_cost_spread_score":10,"utilization_score":10,"margin_bridge_score":11,"working_capital_score":9,"cash_conversion_score":8,"relative_strength_score":10,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_after":81,"stage_label_after":"Stage2-Actionable/Yellow-Watch/DataQualityWatch","component_delta_explanation":"Reset plus orderbook/margin recovery would be false-overblocked by a blunt margin-gap guard; exact evidence and name-transition repair still block automatic Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R1L93_C01_P0_CURRENT","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C01 needs explicit backlog-to-delivery-to-margin/cash bridge, late-spike non-validation and false-overblock reset override","eligible_trigger_count":3,"avg_MFE90_pct":21.87,"avg_MAE90_pct":-12.65,"avg_MFE180_pct":91.49,"avg_MAE180_pct":-15.33,"false_positive_rate":0.67,"late_spike_not_validation_count":1,"false_overblock_count":1,"score_return_alignment_verdict":"mixed_without_C01_backlog_margin_bridge_and_late_spike_reset_override"}
{"row_type":"profile_comparison","comparison_id":"R1L93_C01_P1_SECTOR_SPECIFIC","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_id":"P1_L1_orderbacklog_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 backlog signals need order quality, delivery schedule, mix, price-cost spread, margin or cash conversion before positive stage; late spikes do not backfill old weak entries","changed_axes":["order_quality_required","delivery_margin_cash_required","late_spike_nonvalidation","reset_plus_backlog_override"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_backlog_quality_delivery_mix_margin_or_cash_proxy","bad_entry_filter":"bridge_missing_and_late_spike_only","override_gate":"valuation_reset_plus_backlog_margin_bridge"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_name_transition_repaired"}
{"row_type":"profile_comparison","comparison_id":"R1L93_C01_P2_CANONICAL","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_id":"P2_C01_backlog_delivery_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C01 should reward backlog-to-margin mechanics, not backlog vocabulary or late price spikes","changed_axes":["C01_orderbacklog_delivery_margin_cash_bridge_required","C01_weak_backlog_vocabulary_local_4B_guard","C01_late_spike_not_entry_validation_guard","C01_reset_plus_backlog_margin_false_overblock_override","C01_name_transition_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"backlog_quality_or_customer_project_plus_delivery_or_margin_cash_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R1L93_C01_P3_COUNTEREXAMPLE_GUARD","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_id":"P3_C01_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If backlog-margin bridge is missing, MFE90<10 or MAE180<=-25 routes to 4B; if reset plus backlog-margin bridge exists, do not overblock","changed_axes":["C01_low_MFE_guardrail","C01_deep_MAE_guardrail","C01_false_overblock_override_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE180_le_minus25)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_BACKLOG_POSITIVE_VS_WEAK_BACKLOG_LATE_SPIKE_FALSE_OVERBLOCK","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":1,"false_overblock_count":1,"4B_case_count":1,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":21.87,"avg_MAE90_pct":-12.65,"avg_MFE180_pct":91.49,"avg_MAE180_pct":-15.33,"stage2_hit_rate_MFE90_ge20":0.33,"late_spike_not_validation_count":1,"interpretation":"C01 needs bridge discipline. HD현대중공업 shows backlog/delivery/margin bridge can support Green-candidate-watch, HJ중공업 shows weak backlog vocabulary plus late spike should not validate the original entry, and HD현대미포 shows a reset plus orderbook/margin bridge should not be overblocked by a blunt margin-gap guard."}
{"row_type":"stage_transition_summary","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"329180","trigger_type":"Stage2-Actionable-ShipbuildingOrderBacklogMarginBridge-Positive","entry_date":"2024-04-18","stage2_to_90D_outcome":"good_stage2_MFE90_ge40_low_MAE","stage2_to_180D_outcome":"positive_orderbacklog_margin_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/Green-candidate when backlog is tied to delivery schedule, price-cost spread, margin and cash bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"097230","trigger_type":"Stage2-FalsePositive-WeakBacklogVocabularyLateSpikeNoOriginalMarginBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"weak_backlog_deep_MAE_late_spike_not_validation","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Weak backlog vocabulary without order quality and margin/cash bridge should stay Watch/4B; late spike needs fresh trigger evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"010620","trigger_type":"Stage2-FalsePositive-OverbroadMarginGapWouldMissPostResetOrderbookMarginBridge","entry_date":"2024-03-14","stage2_to_90D_outcome":"false_overblock_initial_MFE_modest_but_low_MAE","stage2_to_180D_outcome":"reset_plus_orderbook_margin_bridge_high_MFE_name_transition_watch","MFE180_ge50":true,"MAE90_le_minus20":false,"transition_note":"Do not hard-block post-reset backlog/margin recovery when customer/order bridge exists; exact evidence and name-transition repair are required."}
{"row_type":"residual_contribution","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","residual_type":"shipbuilding_orderbacklog_margin_bridge_vs_weak_backlog_late_spike_and_false_overblock","contribution":"Adds one C01 backlog/margin positive, one weak-backlog late-spike 4B counterexample, and one false-overblock reset-plus-backlog bridge case, selected because C01 is Priority-0 under-30 coverage.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ORDER_BACKLOG_MARGIN_BRIDGE_VS_WEAK_BACKLOG_LATE_SPIKE_AND_FALSE_OVERBLOCK","positive_case_count":1,"counterexample_count":2,"false_overblock_count":1,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C01 now has shipbuilding backlog/margin bridge positive-control, late-spike non-validation counterexample, and reset-plus-backlog false-overblock case; next C01 loops should exact-URL repair backlog quality, delivery schedule, price-cost spread, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"C01_orderbacklog_delivery_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"329180 worked when backlog/delivery/margin proxy existed; 097230 failed when backlog vocabulary lacked order quality and margin/cash bridge."}
{"row_type":"shadow_weight","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"C01_weak_backlog_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"097230 showed low forward MFE and deep MAE when backlog/margin evidence was missing."}
{"row_type":"shadow_weight","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"C01_late_spike_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"097230 showed late November/December spike should not backfill the original weak backlog entry."}
{"row_type":"shadow_weight","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"C01_reset_plus_backlog_margin_false_overblock_override","scope":"canonical_archetype","candidate_delta":1.0,"direction":"override_guard","apply_now":false,"shadow_only":true,"evidence_basis":"010620 showed a post-reset orderbook/margin recovery path that would be missed by a blunt margin-gap block."}
{"row_type":"shadow_weight","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"C01_name_transition_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"010620 changed name after selected entry in 2024, so patch consideration requires price-path and evidence repair."}
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
  - weak_backlog_vocabulary_overcredit
  - late_spike_not_original_entry_validation
  - orderbacklog_delivery_margin_cash_bridge_required
  - reset_plus_backlog_margin_false_overblock
  - name_transition_data_quality_watch
new_axis_proposed:
  - C01_orderbacklog_delivery_margin_cash_bridge_required_shadow_only
  - C01_weak_backlog_vocabulary_local_4B_guard_shadow_only
  - C01_late_spike_not_entry_validation_guard_shadow_only
  - C01_reset_plus_backlog_margin_false_overblock_override_shadow_only
  - C01_name_transition_data_quality_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C01
  - full_4b_requires_non_price_evidence within C01
  - hard_4c_thesis_break_routes_to_4c within C01
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
`329180` has no corporate-action candidate in its profile and the selected 2024 window is clean.
`097230` has older corporate-action candidates before 2024; the selected 2024 window is usable.
`010620` has historical corporate-action/name-transition complexity and changed name after selected entry in 2024, so it remains data-quality watch before production patching.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
name_transition_watch = true for 010620
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
3. Confirm R1 / L1 / C01 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop was selected by coverage-index-first, not sequential round continuation.
6. Confirm stale duplicate C09 output touched in this execution path is not ingested as the valid output for this request.
7. Keep 010620 in name-transition data-quality watch before patch consideration.
8. Treat 097230 as late-spike non-validation failure mode unless fresh trigger evidence is added later.
9. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C01-scoped safe patch candidates:
   - C01_orderbacklog_delivery_margin_cash_bridge_required
   - C01_weak_backlog_vocabulary_local_4B_guard
   - C01_late_spike_not_entry_validation_guard
   - C01_reset_plus_backlog_margin_false_overblock_override
   - C01_name_transition_data_quality_guard
10. Do not loosen Stage3-Green.
11. Do not use future MFE/MAE in runtime scoring.
12. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R1
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH or remaining Priority-0 under-30 archetype
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive backlog/margin bridge, 1 weak-backlog late-spike 4B counterexample, and 1 reset-plus-backlog false-overblock row for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01_ORDER_BACKLOG_MARGIN_BRIDGE.
```
