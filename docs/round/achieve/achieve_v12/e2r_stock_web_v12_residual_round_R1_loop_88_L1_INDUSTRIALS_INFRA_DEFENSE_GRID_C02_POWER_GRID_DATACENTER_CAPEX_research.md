# E2R Stock-Web v12 Residual Research — R1 Loop 88 / L1 / C02

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R1
loop: 88
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_SMALLCAP_GRID_THEME_BLOWOFF
sector: industrials / power grid / datacenter capex / transformer / switchgear / order margin
output_file: e2r_stock_web_v12_residual_round_R1_loop_88_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R13 loop 87`.

```text
scheduled_round = R1
scheduled_loop = 88
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
```

R1 is restricted to L1 industrials / infra / defense / grid.  
C02 is selected because the recent loop87 R1 used C01 order/backlog, while the latest R13 cross-review emphasized that price-only event blowoffs should not override missing business bridges. C02 remains a useful L1 testbed because power-grid/datacenter CAPEX can produce both genuine multi-quarter order/margin rerating and small-cap theme blowoff.

The No-Repeat Index shows C02 as:

```text
C02_POWER_GRID_DATACENTER_CAPEX
rows = 22
symbols = 12
good/bad Stage2 = 11/4
4B/4C = 2/0
top-covered = 000500, 006340, 033100, 001440, 017040, 189860
```

This loop avoids the C02 top-covered list and also avoids the immediately previous C02 loop set:

```text
R11 loop85 C02: 267260, 010120, 103590
```

It also avoids the immediately recent L1 loop symbols from C01/C03/C04/C05 evidence families.

Selected symbols:

```text
298040, 388050, 147830
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"298040","company_name":"효성중공업","profile_path":"atlas/symbol_profiles/298/298040.json","first_date":"2018-07-13","last_date":"2026-02-20","trading_day_count":1866,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"388050","company_name":"지투파워","profile_path":"atlas/symbol_profiles/388/388050.json","first_date":"2022-04-01","last_date":"2026-02-20","trading_day_count":951,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2022-08-10","2022-09-06"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"147830","company_name":"제룡산업","profile_path":"atlas/symbol_profiles/147/147830.json","first_date":"2012-02-13","last_date":"2026-02-20","trading_day_count":3445,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2016-07-26","2021-09-23","2021-10-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"298040","trigger_type":"Stage2-Actionable-TransformerDatacenterCapexOrderMarginBridge-Positive","entry_date":"2024-03-04","duplicate_status":"new C02 symbol/trigger/date combination outside top-covered and previous C02 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"388050","trigger_type":"Stage2-FalsePositive-SmallcapGridThemeNoDatacenterOrderMarginBridge","entry_date":"2024-05-29","duplicate_status":"new C02 symbol/trigger/date combination outside top-covered and previous C02 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"147830","trigger_type":"Stage2-FalsePositive-LateGridEquipmentThemeNoFreshOrderBridge","entry_date":"2024-09-26","duplicate_status":"new C02 symbol/trigger/date combination outside top-covered and previous C02 loop symbols"}
```

## 4. Research question

C02 is not “전력망 테마가 강하다.”  
The useful signal is the order-to-margin bridge: transformer or grid-equipment order quality, datacenter or utility customer visibility, backlog duration, capacity utilization, ASP/mix, export margin, working-capital discipline, and cash conversion. Without this bridge, the tape can still spark, but it is a loose wire rather than a connected substation.

Residual question:

```text
Can C02 distinguish:
1. transformer/datacenter CAPEX order-margin bridge with huge MFE and tolerable MAE,
2. small-cap grid theme blowoff with no datacenter order, utility customer or margin bridge,
3. late grid-equipment extension where a previous theme run does not create fresh order/margin evidence?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C02_R1L88_298040_HYOSUNG_HEAVY_TRANSFORMER_CAPEX","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-TransformerDatacenterCapexOrderMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_order_customer_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Transformer/datacenter CAPEX order-quality proxy produced very high MFE with tolerable early MAE. Green still requires exact order, customer, margin and cash evidence."}
{"row_type":"case","case_id":"C02_R1L88_388050_G2POWER_GRID_THEME_NO_BRIDGE","symbol":"388050","company_name":"지투파워","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SMALLCAP_GRID_THEME_WITHOUT_DATACENTER_ORDER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallcapGridThemeNoDatacenterOrderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub_Yellow_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_smallcap_grid_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Small-cap grid theme produced sub-Yellow MFE and deep MAE when datacenter/utility order, backlog and margin bridge were missing."}
{"row_type":"case","case_id":"C02_R1L88_147830_CHERYONG_LATE_GRID_EQUIPMENT_EXTENSION","symbol":"147830","company_name":"제룡산업","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"LATE_GRID_EQUIPMENT_THEME_WITHOUT_FRESH_ORDER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LateGridEquipmentThemeNoFreshOrderBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_180D_MAE_after_late_extension","current_profile_verdict":"current_profile_false_positive_if_late_grid_equipment_extension_overcredited","price_source":"Songdaiki/stock-web","notes":"Late grid-equipment extension had low MFE and deep later MAE when fresh order, datacenter customer and margin evidence were missing."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 298040 효성중공업 — transformer/datacenter CAPEX order-margin bridge positive

Entry row: `2024-03-04 c=222500`.  
Observed path: entry low `2024-03-04 l=195000`, high `2024-05-28 h=469000`, and full-window high `2024-11-12 h=518000`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L88_C02_298040_20240304_STAGE2_TRANSFORMER_CAPEX","case_id":"C02_R1L88_298040_HYOSUNG_HEAVY_TRANSFORMER_CAPEX","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-TransformerDatacenterCapexOrderMarginBridge-Positive","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":222500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_transformer_datacenter_capex_order_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; transformer/datacenter CAPEX order quality, backlog and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["transformer_order_proxy","datacenter_CAPEX_proxy","backlog_duration_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_order_pending","margin_mix_bridge_pending","capacity_utilization_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv","profile_path":"atlas/symbol_profiles/298/298040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":60.45,"MFE_90D_pct":110.79,"MFE_180D_pct":132.81,"MAE_30D_pct":-12.36,"MAE_90D_pct":-12.36,"MAE_180D_pct":-12.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":518000.0,"max_drawdown_low_date":"2024-03-04","max_drawdown_low":195000.0,"drawdown_after_peak_pct":-39.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_price_extension_watch; Green requires exact order/customer/margin evidence","four_b_evidence_type":["price_only_extension_watch","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_order_customer_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"298040_2024-03-04_222500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C02 can allow Stage2/Yellow when power-grid strength is tied to transformer order quality, datacenter or utility customer visibility, backlog, margin mix and cash bridge. Green still requires exact evidence."}
```

### 6.2 388050 지투파워 — small-cap grid theme without datacenter order/margin bridge

Entry row: `2024-05-29 c=10640`.  
Observed path: same-day high `2024-05-29 h=12740`, then lows `2024-07-22 l=8010`, `2024-10-04 l=4960`, and later volatile theme rebounds that do not validate the original weak entry.

```jsonl
{"row_type":"trigger","trigger_id":"R1L88_C02_388050_20240529_STAGE2_FALSE_POSITIVE_SMALLCAP_GRID_THEME","case_id":"C02_R1L88_388050_G2POWER_GRID_THEME_NO_BRIDGE","symbol":"388050","company_name":"지투파워","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SMALLCAP_GRID_THEME_WITHOUT_DATACENTER_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SmallcapGridThemeNoDatacenterOrderMarginBridge","trigger_date":"2024-05-29","entry_date":"2024-05-29","entry_price":10640.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_smallcap_grid_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small-cap grid theme treated as insufficient without datacenter/utility order, backlog duration, customer quality and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["smallcap_grid_theme","relative_strength_blowoff"],"stage3_evidence_fields":["datacenter_customer_order_missing","utility_backlog_quality_missing","margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","late_rebound_not_entry_validation"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/388/388050/2024.csv","profile_path":"atlas/symbol_profiles/388/388050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.74,"MFE_90D_pct":19.74,"MFE_180D_pct":19.74,"MAE_30D_pct":-12.50,"MAE_90D_pct":-53.38,"MAE_180D_pct":-53.38,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-29","peak_price":12740.0,"max_drawdown_low_date":"2024-10-04","max_drawdown_low":4960.0,"drawdown_after_peak_pct":-61.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smallcap_grid_theme_without_datacenter_order_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","late_rebound_not_entry_validation"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_smallcap_grid_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"388050_2024-05-29_10640","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C02 should not promote small-cap grid theme blowoff unless datacenter or utility order, backlog, margin and cash bridge are verified. MFE below 20 plus deep MAE routes to 4B-watch."}
```

### 6.3 147830 제룡산업 — late grid-equipment extension without fresh order bridge

Entry row: `2024-09-26 c=7200`.  
Observed path: next-day high `2024-09-27 h=7430`, then lows `2024-11-29 l=5140` and `2024-12-09 l=4505`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L88_C02_147830_20240926_STAGE2_FALSE_POSITIVE_LATE_GRID_EXTENSION","case_id":"C02_R1L88_147830_CHERYONG_LATE_GRID_EQUIPMENT_EXTENSION","symbol":"147830","company_name":"제룡산업","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"LATE_GRID_EQUIPMENT_THEME_WITHOUT_FRESH_ORDER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-LateGridEquipmentThemeNoFreshOrderBridge","trigger_date":"2024-09-26","entry_date":"2024-09-26","entry_price":7200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_late_grid_equipment_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; late grid-equipment theme treated as insufficient without fresh customer order, backlog and margin/cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["late_grid_equipment_theme","relative_strength_extension"],"stage3_evidence_fields":["fresh_order_bridge_missing","datacenter_customer_bridge_missing","margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_late_extension","fresh_order_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/147/147830/2024.csv","profile_path":"atlas/symbol_profiles/147/147830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.19,"MFE_90D_pct":3.19,"MFE_180D_pct":3.19,"MAE_30D_pct":-15.83,"MAE_90D_pct":-37.43,"MAE_180D_pct":-37.43,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-27","peak_price":7430.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":4505.0,"drawdown_after_peak_pct":-39.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_grid_equipment_extension_without_fresh_order_bridge_should_remain_watch_4B_not_Yellow","four_b_evidence_type":["price_only","fresh_order_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_180D_MAE_after_late_extension","current_profile_verdict":"current_profile_false_positive_if_late_grid_equipment_extension_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"147830_2024-09-26_7200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C02 should not equate late grid-equipment strength with fresh datacenter/customer-order evidence. Low MFE and deep 180D MAE require Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C02_R1L88_298040_HYOSUNG_HEAVY_TRANSFORMER_CAPEX","trigger_id":"R1L88_C02_298040_20240304_STAGE2_TRANSFORMER_CAPEX","symbol":"298040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C02 requires order/customer/margin bridge rather than power-grid theme alone","raw_component_scores_before":{"order_quality_score":15,"datacenter_CAPEX_score":14,"utility_customer_score":12,"backlog_duration_score":13,"margin_mix_score":11,"capacity_utilization_score":10,"cash_conversion_score":7,"relative_strength_score":14,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"order_quality_score":18,"datacenter_CAPEX_score":17,"utility_customer_score":15,"backlog_duration_score":16,"margin_mix_score":14,"capacity_utilization_score":12,"cash_conversion_score":9,"relative_strength_score":15,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":91,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Order/customer/margin bridge and huge MFE support Yellow/Green-candidate watch, but exact customer and margin/cash evidence still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C02_R1L88_388050_G2POWER_GRID_THEME_NO_BRIDGE","trigger_id":"R1L88_C02_388050_20240529_STAGE2_FALSE_POSITIVE_SMALLCAP_GRID_THEME","symbol":"388050","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_scope":"current_default_proxy","profile_hypothesis":"small-cap grid theme without datacenter/utility order bridge should be blocked","raw_component_scores_before":{"order_quality_score":3,"datacenter_CAPEX_score":2,"utility_customer_score":2,"backlog_duration_score":1,"margin_mix_score":0,"capacity_utilization_score":1,"cash_conversion_score":0,"relative_strength_score":13,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"order_quality_score":0,"datacenter_CAPEX_score":0,"utility_customer_score":0,"backlog_duration_score":0,"margin_mix_score":0,"capacity_utilization_score":0,"cash_conversion_score":0,"relative_strength_score":4,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-Yellow MFE and deep MAE convert grid theme into missing order/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C02_R1L88_147830_CHERYONG_LATE_GRID_EQUIPMENT_EXTENSION","trigger_id":"R1L88_C02_147830_20240926_STAGE2_FALSE_POSITIVE_LATE_GRID_EXTENSION","symbol":"147830","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_scope":"current_default_proxy","profile_hypothesis":"late grid-equipment extension without fresh order bridge should remain Watch/blocked","raw_component_scores_before":{"order_quality_score":2,"datacenter_CAPEX_score":1,"utility_customer_score":2,"backlog_duration_score":1,"margin_mix_score":0,"capacity_utilization_score":1,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"order_quality_score":0,"datacenter_CAPEX_score":0,"utility_customer_score":0,"backlog_duration_score":0,"margin_mix_score":0,"capacity_utilization_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep 180D MAE require fresh order/customer and margin bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R1L88_C02_P0_CURRENT","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C02 needs explicit order/customer/backlog/margin/cash bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":44.57,"avg_MAE90_pct":-34.39,"avg_MFE180_pct":51.91,"avg_MAE180_pct":-34.39,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C02_order_customer_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R1L88_C02_P1_SECTOR_SPECIFIC","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P1_L1_grid_CAPEX_order_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 grid signals need transformer order quality, datacenter/utility customer, backlog, margin mix, utilization or cash bridge before Stage2-Actionable","changed_axes":["order_customer_bridge_required","margin_cash_bridge_required","smallcap_grid_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_order_customer_backlog_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":44.57,"avg_MAE90_pct":-34.39,"avg_MFE180_pct":51.91,"avg_MAE180_pct":-34.39,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R1L88_C02_P2_CANONICAL","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P2_C02_order_customer_margin_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C02 should reward order/customer/margin mechanics, not power-grid price themes","changed_axes":["C02_order_customer_margin_bridge_required","C02_smallcap_grid_theme_local_4B_guard","C02_late_extension_not_fresh_order_guard"],"changed_thresholds":{"stage2_yellow_gate":"order_quality_plus_customer_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":44.57,"avg_MAE90_pct":-34.39,"avg_MFE180_pct":51.91,"avg_MAE180_pct":-34.39,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R1L88_C02_P3_COUNTEREXAMPLE_GUARD","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","profile_id":"P3_C02_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<20 and MAE90<=-25 while order/customer/margin bridge is missing, block Yellow/Green","changed_axes":["C02_low_MFE_guardrail","C02_high_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_20_and_MAE90_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":44.57,"avg_MAE90_pct":-34.39,"avg_MFE180_pct":51.91,"avg_MAE180_pct":-34.39,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSFORMER_CAPEX_VS_SMALLCAP_GRID_THEME","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":44.57,"avg_MAE90_pct":-34.39,"avg_MFE180_pct":51.91,"avg_MAE180_pct":-34.39,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_20":0.67,"stage2_bad_entry_rate_MAE90_le_minus_25":0.67,"interpretation":"C02 needs bridge discipline. 효성중공업 shows transformer/datacenter CAPEX order-margin bridge can rerate massively, while 지투파워 and 제룡산업 show small-cap/late grid themes can fail when order, customer, backlog, margin and cash evidence are missing."}
{"row_type":"stage_transition_summary","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"298040","trigger_type":"Stage2-Actionable-TransformerDatacenterCapexOrderMarginBridge-Positive","entry_date":"2024-03-04","stage2_to_90D_outcome":"good_stage2_very_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_transformer_CAPEX_order_margin_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when order quality, datacenter/utility customer, backlog and margin bridge exists; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"388050","trigger_type":"Stage2-FalsePositive-SmallcapGridThemeNoDatacenterOrderMarginBridge","entry_date":"2024-05-29","stage2_to_90D_outcome":"bad_stage2_sub_Yellow_MFE_deep_MAE","stage2_to_180D_outcome":"failed_smallcap_grid_theme_late_rebound_not_validation","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Small-cap grid theme without order/customer/margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","symbol":"147830","trigger_type":"Stage2-FalsePositive-LateGridEquipmentThemeNoFreshOrderBridge","entry_date":"2024-09-26","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_late_grid_equipment_extension","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Late grid-equipment extension without fresh order bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","residual_type":"grid_CAPEX_theme_overcredit_without_order_customer_margin_cash_bridge","contribution":"Adds two C02 local 4B/deep-MAE counterexamples against one transformer/datacenter CAPEX positive, avoiding C02 top-covered and previous C02 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"TRANSFORMER_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_VS_SMALLCAP_GRID_THEME_BLOWOFF","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C02 now has a non-top-symbol transformer positive and two small-cap/late grid-theme counterexamples; next R1 loops should exact-URL repair order quality, datacenter/utility customer, backlog duration, margin mix, capacity utilization and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"C02_order_customer_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"298040 worked when transformer/datacenter CAPEX order-quality proxy was present; 388050 and 147830 failed when only grid theme or late extension existed."}
{"row_type":"shadow_weight","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"C02_smallcap_grid_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Small-cap/late grid theme rows showed sub-Yellow or low MFE and deep MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R1","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis":"C02_late_extension_not_fresh_order_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"Late grid-equipment extension should not be treated as fresh order/customer evidence unless exact customer, backlog and margin bridge is repaired."}
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
  - power_grid_theme_overcredit
  - datacenter_customer_bridge_missing
  - order_backlog_margin_bridge_missing
  - late_extension_not_fresh_order_validation
new_axis_proposed:
  - C02_order_customer_margin_bridge_required_shadow_only
  - C02_smallcap_grid_theme_local_4B_watch_guard_shadow_only
  - C02_late_extension_not_fresh_order_guardrail_shadow_only
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

All selected triggers use actual Stock-Web tradable raw OHLC rows and clean selected forward windows.  
The non-price evidence layer remains source-name/proxy level.

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
   - previous R11 loop85 C02 symbols
   - recent L1 C01/C03/C04/C05 loop symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C02-scoped safe patch candidates:
   - C02_order_customer_margin_bridge_required
   - C02_smallcap_grid_theme_local_4B_watch_guard
   - C02_late_extension_not_fresh_order_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R1
completed_loop = 88
next_round = R2
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.
```
