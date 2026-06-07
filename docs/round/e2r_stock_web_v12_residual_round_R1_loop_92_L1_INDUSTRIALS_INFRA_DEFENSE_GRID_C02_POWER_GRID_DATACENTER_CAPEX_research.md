# E2R Stock-Web v12 Residual Research — R1 Loop 92 / L1 / C02

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R1
loop: 92
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_DATACENTER_BACKLOG_BRIDGE_VS_POWER_SUPPLY_DIGITAL_GRID_VOCABULARY_DECAY
sector: industrials / grid / datacenter capex / transformer / electrical equipment / power supply / digital grid
output_file: e2r_stock_web_v12_residual_round_R1_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R13 loop 91`.

```text
scheduled_round = R1
scheduled_loop = 92
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
```

R1 is restricted to L1 industrials / infrastructure / defense / grid.
C02 is selected because the immediate R1 sequence rotated through C03, C04, and C05, so the next residual expansion returns to grid / datacenter capex.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C02_POWER_GRID_DATACENTER_CAPEX
rows = 22
symbols = 12
good/bad Stage2 = 11/4
4B/4C = 2/0
top-covered = 000500, 006340, 033100, 001440, 017040, 189860
```

This loop avoids the C02 top-covered list and recent L1/C02 or L1-adjacent loop symbols:

```text
R11 loop89 C02: 229640, 199820, 006910
R11 loop90 C03: 272210, 095190, 218410
R11 loop91 C04: 126720, 457550, 036190
R1 loop89 C03: 064350, 099320, 214430
R1 loop90 C04: 130660, 105840, 019990
R1 loop91 C05: 100840, 028050, 037350
C02 top-covered: 000500, 006340, 033100, 001440, 017040, 189860
```

Candidate hygiene note:

```text
During this execution path, 007610 and 065770 were touched while checking alternatives. They are not used in this R1/C02 output.
```

Selected symbols:

```text
267260, 037030, 237750
```

The selected pocket is:

```text
transformer / datacenter capex / grid backlog bridge
vs
power-supply vocabulary without datacenter customer-order and margin bridge
vs
digital grid / protection relay vocabulary with price MFE but no durable customer/order bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"267260","company_name":"HD현대일렉트릭","profile_path":"atlas/symbol_profiles/267/267260.json","first_date":"2017-05-10","last_date":"2026-02-20","trading_day_count":2154,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["2017-11-17","2017-11-28","2017-12-11","2018-11-23","2018-12-18","2019-12-30"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"037030","company_name":"파워넷","profile_path":"atlas/symbol_profiles/037/037030.json","first_date":"1999-12-24","last_date":"2026-02-20","trading_day_count":3100,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2000-05-25","2001-01-15","2005-08-22","2018-06-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"237750","company_name":"피앤씨테크","profile_path":"atlas/symbol_profiles/237/237750.json","first_date":"2016-07-04","last_date":"2026-02-20","trading_day_count":2363,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"267260","trigger_type":"Stage2-Actionable-TransformerDatacenterBacklogMarginBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C02 symbol/trigger/date combination outside C02 top-covered and recent L1/C02 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"037030","trigger_type":"Stage2-FalsePositive-PowerSupplyVocabularyNoDatacenterCustomerOrderMarginBridge","entry_date":"2024-01-02","duplicate_status":"new C02 symbol/trigger/date combination outside C02 top-covered and recent L1/C02 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"237750","trigger_type":"Stage2-FalsePositive-DigitalGridRelayPriceMFE-NoDurableCustomerOrderBridge","entry_date":"2024-01-02","duplicate_status":"new C02 symbol/trigger/date combination outside C02 top-covered and recent L1/C02 loop symbols"}
```

## 4. Research question

C02 is not “전력·AI·데이터센터 단어가 있다.”
The useful grid/datacenter capex signal must prove the conversion chain:

```text
transformer / switchgear / protection-equipment exposure
datacenter or grid customer order
capacity expansion or delivery schedule
backlog conversion
ASP or mix improvement
utilization
margin bridge
working-capital discipline
cash conversion
```

A grid headline without this bridge is a substation drawn in bright ink. It becomes E2R evidence only when equipment ships into the capex cycle, invoices convert, margin expands, and cash returns through the circuit.

Residual question:

```text
Can C02 distinguish:
1. transformer/datacenter capex backlog bridge with extreme MFE and shallow entry MAE,
2. power-supply vocabulary where no datacenter customer order or margin bridge is repaired,
3. digital-grid/protection-relay vocabulary where price MFE exists but is not durable order/backlog evidence?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C02_R1L92_267260_HDHE_TRANSFORMER_DATACENTER","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_DATACENTER_BACKLOG_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-TransformerDatacenterBacklogMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_extreme_MFE90_and_MFE180_low_MAE_transformer_backlog_bridge","current_profile_verdict":"current_profile_correct_if_customer_order_delivery_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Transformer/datacenter grid capex proxy produced extreme MFE with shallow MAE. Green still requires exact customer order, backlog, delivery, ASP/mix, margin and cash evidence."}
{"row_type":"case","case_id":"C02_R1L92_037030_POWERNET_POWER_SUPPLY_DECAY","symbol":"037030","company_name":"파워넷","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_SUPPLY_VOCABULARY_WITHOUT_DATACENTER_CUSTOMER_ORDER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PowerSupplyVocabularyNoDatacenterCustomerOrderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_datacenter_order_bridge","current_profile_verdict":"current_profile_false_positive_if_power_supply_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Power-supply vocabulary had low forward MFE and deep later MAE without datacenter/grid customer order, delivery schedule, margin or cash bridge."}
{"row_type":"case","case_id":"C02_R1L92_237750_PNC_DIGITAL_GRID_PRICE_MFE","symbol":"237750","company_name":"피앤씨테크","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"DIGITAL_GRID_RELAY_PRICE_MFE_WITHOUT_DURABLE_CUSTOMER_ORDER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DigitalGridRelayPriceMFE-NoDurableCustomerOrderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_MFE_deep_MAE_no_order_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_digital_grid_price_MFE_overcredited","price_source":"Songdaiki/stock-web","notes":"Digital-grid/protection relay vocabulary produced price MFE, but later deep MAE shows price alone should not validate C02 without durable customer order, backlog, margin and cash evidence."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 267260 HD현대일렉트릭 — transformer / datacenter capex backlog bridge

Entry row: `2024-01-29 c=101200`.
Observed path: early low `2024-02-01 l=97500`, 90D peak around `2024-05-27 h=314000`, and full-window peak `2024-11-12 h=413500`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L92_C02_267260_20240129_STAGE2_TRANSFORMER_DATACENTER_BACKLOG","case_id":"C02_R1L92_267260_HDHE_TRANSFORMER_DATACENTER","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_DATACENTER_BACKLOG_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-TransformerDatacenterBacklogMarginBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":101200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_transformer_grid_datacenter_backlog_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; transformer backlog, datacenter/grid capex order, delivery schedule, ASP/mix and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["transformer_backlog_proxy","datacenter_grid_capex_proxy","delivery_schedule_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_order_source_pending","backlog_conversion_source_pending","ASP_mix_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":45.85,"MFE_90D_pct":210.28,"MFE_180D_pct":308.60,"MAE_30D_pct":-3.66,"MAE_90D_pct":-3.66,"MAE_180D_pct":-3.66,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":413500.0,"max_drawdown_low_date":"2024-02-01","max_drawdown_low":97500.0,"drawdown_after_peak_pct":-19.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.76,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_customer_order_backlog_delivery_ASP_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_extreme_MFE90_and_MFE180_low_MAE_transformer_backlog_bridge","current_profile_verdict":"current_profile_correct_if_customer_order_delivery_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"267260_2024-01-29_101200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C02 can allow Stage2/Yellow when grid strength is tied to transformer/datacenter order backlog, delivery schedule, ASP/mix, margin and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 037030 파워넷 — power-supply vocabulary without datacenter customer-order / margin bridge

Entry row: `2024-01-02 c=3175`.
Observed path: local high `2024-02-19 h=3375`, then long decline to `2024-12-09 l=2005`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L92_C02_037030_20240102_STAGE2_FALSE_POSITIVE_POWER_SUPPLY","case_id":"C02_R1L92_037030_POWERNET_POWER_SUPPLY_DECAY","symbol":"037030","company_name":"파워넷","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_SUPPLY_VOCABULARY_WITHOUT_DATACENTER_CUSTOMER_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-PowerSupplyVocabularyNoDatacenterCustomerOrderMarginBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":3175.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_power_supply_datacenter_grid_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; power-supply/grid vocabulary treated as insufficient without datacenter customer order, delivery schedule, backlog conversion, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["power_supply_keyword","grid_datacenter_vocabulary","relative_strength_rebound"],"stage3_evidence_fields":["datacenter_customer_order_missing","backlog_conversion_missing","margin_cash_bridge_missing","delivery_schedule_missing"],"stage4b_evidence_fields":["low_MFE_watch","order_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/037/037030/2024.csv","profile_path":"atlas/symbol_profiles/037/037030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.30,"MFE_90D_pct":6.30,"MFE_180D_pct":6.30,"MAE_30D_pct":-7.72,"MAE_90D_pct":-14.02,"MAE_180D_pct":-36.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":3375.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":2005.0,"drawdown_after_peak_pct":-40.59,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"power_supply_vocabulary_without_datacenter_customer_order_backlog_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","order_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_datacenter_order_bridge","current_profile_verdict":"current_profile_false_positive_if_power_supply_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"037030_2024-01-02_3175","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C02 should not promote power-supply vocabulary without datacenter/grid customer order, delivery, backlog conversion, margin and cash evidence. Low MFE and deep MAE require Watch/4B routing."}
```

### 6.3 237750 피앤씨테크 — digital-grid / relay price MFE without durable order bridge

Entry row: `2024-01-02 c=5610`.
Observed path: price spike to `2024-05-08 h=7640`, but then later decline to `2024-12-09 l=3280`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L92_C02_237750_20240102_STAGE2_FALSE_POSITIVE_DIGITAL_GRID_RELAY","case_id":"C02_R1L92_237750_PNC_DIGITAL_GRID_PRICE_MFE","symbol":"237750","company_name":"피앤씨테크","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"DIGITAL_GRID_RELAY_PRICE_MFE_WITHOUT_DURABLE_CUSTOMER_ORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_only_MFE_stress_test","trigger_type":"Stage2-FalsePositive-DigitalGridRelayPriceMFE-NoDurableCustomerOrderBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":5610.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_digital_grid_relay_power_equipment_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; digital-grid/protection relay vocabulary and price strength treated as insufficient without durable customer order, backlog, delivery schedule, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["digital_grid_keyword","relay_protection_equipment_vocabulary","price_MFE"],"stage3_evidence_fields":["durable_customer_order_missing","backlog_conversion_missing","delivery_schedule_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_MFE","order_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237750/2024.csv","profile_path":"atlas/symbol_profiles/237/237750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.28,"MFE_90D_pct":36.19,"MFE_180D_pct":36.19,"MAE_30D_pct":-2.32,"MAE_90D_pct":-5.70,"MAE_180D_pct":-41.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-08","peak_price":7640.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":3280.0,"drawdown_after_peak_pct":-57.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.12,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"digital_grid_relay_price_MFE_without_customer_order_delivery_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only_MFE","order_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_MFE_deep_MAE_no_order_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_digital_grid_price_MFE_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"237750_2024-01-02_5610","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C02 should not count digital-grid relay MFE as grid/datacenter capex validation unless customer order, backlog, delivery schedule, margin and cash evidence are exact-repaired. Price-only MFE with deep MAE remains 4B-watch."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L92_267260_HDHE_TRANSFORMER_DATACENTER","trigger_id":"R1L92_C02_267260_20240129_STAGE2_TRANSFORMER_DATACENTER_BACKLOG","symbol":"267260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C02 requires grid/datacenter customer order, transformer backlog, delivery schedule, ASP/mix, margin and cash bridge rather than grid vocabulary alone","raw_component_scores_before":{"grid_capex_score":14,"datacenter_order_score":13,"transformer_backlog_score":15,"delivery_schedule_score":12,"ASP_mix_score":11,"margin_bridge_score":12,"cash_conversion_score":8,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"grid_capex_score":17,"datacenter_order_score":16,"transformer_backlog_score":18,"delivery_schedule_score":15,"ASP_mix_score":14,"margin_bridge_score":15,"cash_conversion_score":10,"relative_strength_score":17,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":94,"stage_label_after":"Stage3-Green-candidate-watch","component_delta_explanation":"Transformer/datacenter backlog bridge plus extreme MFE supports Green-candidate watch; exact customer-order, backlog and margin evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L92_037030_POWERNET_POWER_SUPPLY_DECAY","trigger_id":"R1L92_C02_037030_20240102_STAGE2_FALSE_POSITIVE_POWER_SUPPLY","symbol":"037030","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_scope":"current_default_proxy","profile_hypothesis":"power-supply vocabulary without datacenter customer order and margin bridge should be blocked","raw_component_scores_before":{"grid_capex_score":2,"datacenter_order_score":0,"transformer_backlog_score":0,"delivery_schedule_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"grid_capex_score":0,"datacenter_order_score":0,"transformer_backlog_score":0,"delivery_schedule_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert power-supply vocabulary into missing customer-order/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L92_237750_PNC_DIGITAL_GRID_PRICE_MFE","trigger_id":"R1L92_C02_237750_20240102_STAGE2_FALSE_POSITIVE_DIGITAL_GRID_RELAY","symbol":"237750","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_scope":"current_default_proxy","profile_hypothesis":"digital-grid relay price MFE without durable customer order bridge should remain Watch/4B","raw_component_scores_before":{"grid_capex_score":3,"datacenter_order_score":0,"transformer_backlog_score":0,"delivery_schedule_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":12,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"grid_capex_score":1,"datacenter_order_score":0,"transformer_backlog_score":0,"delivery_schedule_score":0,"ASP_mix_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Price MFE is not positive C02 validation without customer order, backlog, delivery, margin and cash bridge."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R1L92_C02_P0_CURRENT","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C02 needs explicit customer order, transformer/switchgear backlog, delivery schedule, ASP/mix, margin/cash and price-MFE taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":84.26,"avg_MAE90_pct":-7.79,"avg_MFE180_pct":117.03,"avg_MAE180_pct":-27.35,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.63,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C02_customer_order_backlog_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R1L92_C02_P1_SECTOR_SPECIFIC","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P1_L1_grid_datacenter_order_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 grid/datacenter signals need customer order, backlog, delivery schedule, ASP/mix, margin or cash conversion before Stage2-Actionable","changed_axes":["customer_order_required","backlog_delivery_required","price_MFE_grid_vocabulary_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_order_backlog_delivery_ASP_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":84.26,"avg_MAE90_pct":-7.79,"avg_MFE180_pct":117.03,"avg_MAE180_pct":-27.35,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R1L92_C02_P2_CANONICAL","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P2_C02_customer_order_backlog_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C02 should reward order-to-backlog-to-margin mechanics, not power/grid vocabulary or price MFE","changed_axes":["C02_customer_order_backlog_delivery_margin_cash_bridge_required","C02_power_supply_digital_grid_vocabulary_local_4B_guard","C02_price_MFE_not_capex_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_order_or_backlog_plus_delivery_or_margin_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":84.26,"avg_MAE90_pct":-7.79,"avg_MFE180_pct":117.03,"avg_MAE180_pct":-27.35,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R1L92_C02_P3_COUNTEREXAMPLE_GUARD","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P3_C02_low_MFE_or_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If customer-order/backlog bridge is missing, MFE90<20 or MAE180<=-25 should block Yellow/Green; price MFE without bridge stays 4B-watch","changed_axes":["C02_low_MFE_guardrail","C02_deep_MAE_4B_guardrail","C02_price_MFE_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_MAE180_le_minus_25); high_MFE_without_bridge_not_positive"},"eligible_trigger_count":3,"avg_MFE90_pct":84.26,"avg_MAE90_pct":-7.79,"avg_MFE180_pct":117.03,"avg_MAE180_pct":-27.35,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_POSITIVE_VS_POWER_SUPPLY_DIGITAL_GRID_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":84.26,"avg_MAE90_pct":-7.79,"avg_MFE180_pct":117.03,"avg_MAE180_pct":-27.35,"stage2_hit_rate_MFE90_ge20":0.67,"price_MFE_without_bridge_counterexample_count":1,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus25":0.67,"interpretation":"C02 needs bridge discipline. HD현대일렉트릭 shows transformer/datacenter backlog bridge can support Yellow/Green-candidate-watch, while 파워넷 and 피앤씨테크 show power-supply/digital-grid vocabulary should not be promoted without customer order, backlog conversion, delivery schedule, ASP/mix, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"267260","trigger_type":"Stage2-Actionable-TransformerDatacenterBacklogMarginBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_extreme_MFE_low_MAE","stage2_to_180D_outcome":"positive_transformer_datacenter_backlog_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when grid strength is tied to customer order, transformer backlog, delivery, ASP/mix and margin/cash bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"037030","trigger_type":"Stage2-FalsePositive-PowerSupplyVocabularyNoDatacenterCustomerOrderMarginBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_power_supply_vocabulary_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Power-supply vocabulary without datacenter customer order and margin/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"237750","trigger_type":"Stage2-FalsePositive-DigitalGridRelayPriceMFE-NoDurableCustomerOrderBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"price_MFE_without_order_backlog_bridge","stage2_to_180D_outcome":"failed_digital_grid_relay_price_MFE_deep_MAE","MFE90_ge20":true,"MAE180_le_minus25":true,"transition_note":"Digital-grid/protection-relay MFE without customer order, backlog and margin/cash bridge should be 4B-watch, not positive C02 evidence."}
{"row_type":"residual_contribution","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","residual_type":"power_supply_digital_grid_vocabulary_overcredit_without_customer_order_backlog_margin_cash_bridge","contribution":"Adds two C02 4B counterexamples against one transformer/datacenter backlog positive, avoiding C02 top-covered and recent L1 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_DATACENTER_BACKLOG_BRIDGE_VS_POWER_SUPPLY_DIGITAL_GRID_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C02 now has non-top-symbol transformer/datacenter backlog positive and two power-supply/digital-grid weak-bridge counterexamples; next C02 loops should exact-URL repair customer order, backlog conversion, delivery schedule, ASP/mix, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"C02_customer_order_backlog_delivery_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"267260 worked when transformer/datacenter backlog proxy existed; 037030 and 237750 failed when power/grid vocabulary lacked durable customer order, delivery and margin bridge."}
{"row_type":"shadow_weight","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"C02_power_supply_digital_grid_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Power-supply and digital-grid relay rows showed either low MFE or price-MFE followed by deep MAE when non-price order evidence was missing."}
{"row_type":"shadow_weight","round":"R1","loop":"92","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"C02_price_MFE_not_capex_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"237750 shows MFE90 above 20 should not count as positive C02 evidence when customer-order/backlog/margin bridge is missing and MAE180 is deep."}
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
  - power_supply_grid_vocabulary_overcredit
  - digital_grid_relay_price_MFE_overcredit
  - customer_order_bridge_missing
  - backlog_delivery_margin_cash_bridge_missing
new_axis_proposed:
  - C02_customer_order_backlog_delivery_margin_cash_bridge_required_shadow_only
  - C02_power_supply_digital_grid_vocabulary_local_4B_guard_shadow_only
  - C02_price_MFE_not_capex_validation_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C02
  - full_4b_requires_non_price_evidence within C02
  - hard_4c_thesis_break_routes_to_4c within C02
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

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.
`267260` and `037030` have older corporate-action or name-transition candidates before 2024; those candidates are outside the selected 2024 windows and do not contaminate this residual price-path analysis.
`237750` has no corporate-action candidate in its profile.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
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
3. Confirm R1 / L1 / C02 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C02 top-covered symbols
   - previous R11 loop89 C02 symbols
   - previous R11 loop90 C03 symbols
   - previous R11 loop91 C04 symbols
   - previous R1 loop89 C03 symbols
   - previous R1 loop90 C04 symbols
   - previous R1 loop91 C05 symbols
6. Confirm touched-but-unused 007610 and 065770 are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C02-scoped safe patch candidates:
   - C02_customer_order_backlog_delivery_margin_cash_bridge_required
   - C02_power_supply_digital_grid_vocabulary_local_4B_guard
   - C02_price_MFE_not_capex_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R1
completed_loop = 92
next_round = R2
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.
```
