# E2R Stock-Web v12 Residual Research — R3 Loop 85 / L3 / C11

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 85
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_ORDERBOOK_CUSTOMER_CAPACITY_BRIDGE_VS_ORDERBOOK_HEADLINE_CALLOFF_RISK
sector: battery / EV / green mobility / orderbook rerating
output_file: e2r_stock_web_v12_residual_round_R3_loop_85_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R2 loop 85`.

```text
scheduled_round = R3
scheduled_loop = 85
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
```

R3 is restricted to L3 battery / EV / green mobility.  
C11 is selected because the No-Repeat Index shows the bucket still has meaningful room for counterexample expansion: `21 rows / 14 symbols / good-bad S2 8-4 / 4B-4C 1-0`. This loop avoids the C11 top-covered symbols:

```text
137400, 299030, 003670, 302430, 001570, 005070
```

The goal is not to re-prove that battery orderbook rerating can work. The residual question is whether E2R can separate a true customer/capacity/orderbook bridge from a battery beta or orderbook headline that lacks call-off, shipment, utilization, or margin conversion.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"078600","company_name":"대주전자재료","profile_path":"atlas/symbol_profiles/078/078600.json","first_date":"2004-12-10","last_date":"2026-02-20","trading_day_count":5230,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"247540","company_name":"에코프로비엠","profile_path":"atlas/symbol_profiles/247/247540.json","first_date":"2019-03-05","last_date":"2026-02-20","trading_day_count":1712,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2022-06-27","2022-07-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"393890","company_name":"더블유씨피","profile_path":"atlas/symbol_profiles/393/393890.json","first_date":"2022-09-30","last_date":"2026-02-20","trading_day_count":827,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window; market changed from KOSDAQ to KOSDAQ GLOBAL on 2024-06-14 but no corporate-action candidate"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"078600","trigger_type":"Stage2-Actionable-SiliconAnodeOrderbookCustomerCapacityBridge-Positive","entry_date":"2024-03-21","duplicate_status":"new C11 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"247540","trigger_type":"Stage2-FalsePositive-CathodeOrderbookHeadline-CalloffMarginRisk","entry_date":"2024-03-25","duplicate_status":"new C11 symbol/trigger/date combination outside top-covered list; symbol appears in C14 top coverage but not C11 top list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"393890","trigger_type":"Stage2-FalsePositive-SeparatorOrderbookTheme-NoShipmentMarginBridge","entry_date":"2024-02-21","duplicate_status":"new C11 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C11 is not “battery stock has orderbook.” It is the bridge between backlog and earnings power. A quoted orderbook is a promise; E2R should ask whether customers call it off, shipments leave the dock, capacity is allocated, utilization rises, and margin follows.

Residual question:

```text
Can C11 distinguish:
1. battery materials orderbook rerating backed by customer/capacity bridge,
2. cathode orderbook headline that fails when call-off and margin visibility weaken,
3. separator orderbook/theme rebound that lacks shipment/utilization/margin conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C11_R3L85_078600_DAEJOO_SILICON_ANODE_CUSTOMER_CAPACITY","symbol":"078600","company_name":"대주전자재료","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SILICON_ANODE_ORDERBOOK_CUSTOMER_CAPACITY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-SiliconAnodeOrderbookCustomerCapacityBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_tolerable_90D_MAE","current_profile_verdict":"current_profile_correct_if_customer_capacity_bridge_required","price_source":"Songdaiki/stock-web","notes":"Silicon-anode/customer-capacity proxy produced a strong forward MFE. Later drawdown shows Green still requires exact customer, shipment and margin evidence."}
{"row_type":"case","case_id":"C11_R3L85_247540_ECOPROBM_ORDERBOOK_HEADLINE_CALLOFF_RISK","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_HEADLINE_WITH_CALLOFF_MARGIN_RISK","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CathodeOrderbookHeadline-CalloffMarginRisk","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_orderbook_headline_overcredited","price_source":"Songdaiki/stock-web","notes":"Cathode orderbook headline/battery beta near local peak lacked call-off and margin bridge; forward path showed deep MAE."}
{"row_type":"case","case_id":"C11_R3L85_393890_WCP_SEPARATOR_ORDERBOOK_THEME","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SEPARATOR_ORDERBOOK_THEME_WITHOUT_SHIPMENT_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SeparatorOrderbookTheme-NoShipmentMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_separator_orderbook_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Separator orderbook/theme spike gave a small local MFE but decayed into severe drawdown without shipment/utilization/margin bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 078600 대주전자재료 — silicon-anode orderbook/customer-capacity bridge positive

Entry row: `2024-03-21 c=98900`.  
Observed path: early low around `2024-04-08 l=85000`, then rerating to `2024-06-12 h=163400`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L85_C11_078600_20240321_STAGE2_SILICON_ANODE_ORDERBOOK_BRIDGE","case_id":"C11_R3L85_078600_DAEJOO_SILICON_ANODE_CUSTOMER_CAPACITY","symbol":"078600","company_name":"대주전자재료","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SILICON_ANODE_ORDERBOOK_CUSTOMER_CAPACITY_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-SiliconAnodeOrderbookCustomerCapacityBridge-Positive","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":98900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_silicon_anode_customer_capacity_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; silicon-anode customer/capacity bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["orderbook_bridge_proxy","customer_capacity_proxy","shipment_visibility_proxy","relative_strength_turn"],"stage3_evidence_fields":["customer_calloff_confirmation_pending","margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv","profile_path":"atlas/symbol_profiles/078/078600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.35,"MFE_90D_pct":65.22,"MFE_180D_pct":65.22,"MAE_30D_pct":-14.05,"MAE_90D_pct":-14.05,"MAE_180D_pct":-25.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-12","peak_price":163400.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":73600.0,"drawdown_after_peak_pct":-54.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_90D_MAE","current_profile_verdict":"current_profile_correct_if_customer_capacity_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"078600_2024-03-21_98900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C11 can allow Stage2/Yellow when orderbook rerating is tied to customer/capacity/shipment bridge. Green still requires exact evidence and margin conversion."}
```

### 6.2 247540 에코프로비엠 — cathode orderbook headline / call-off risk counterexample

Entry row: `2024-03-25 c=291000`.  
Observed path: local high `2024-03-27 h=298500`, then lows around `2024-06-28 l=175200` and `2024-11-15 l=120400`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L85_C11_247540_20240325_STAGE2_FALSE_POSITIVE_CATHODE_ORDERBOOK","case_id":"C11_R3L85_247540_ECOPROBM_ORDERBOOK_HEADLINE_CALLOFF_RISK","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_HEADLINE_WITH_CALLOFF_MARGIN_RISK","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-CathodeOrderbookHeadline-CalloffMarginRisk","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":291000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cathode_orderbook_headline_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cathode orderbook/battery beta treated as insufficient without customer call-off, shipment and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["orderbook_headline","battery_beta_relative_strength"],"stage3_evidence_fields":["customer_calloff_bridge_missing","shipment_visibility_missing","margin_bridge_missing","inventory_or_price_pressure_unresolved"],"stage4b_evidence_fields":["price_only_local_peak","calloff_margin_risk_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.58,"MFE_90D_pct":2.58,"MFE_180D_pct":2.58,"MAE_30D_pct":-22.51,"MAE_90D_pct":-39.79,"MAE_180D_pct":-58.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-27","peak_price":298500.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":120400.0,"drawdown_after_peak_pct":-59.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"orderbook_headline_peak_without_calloff_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","calloff_margin_risk_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_orderbook_headline_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"247540_2024-03-25_291000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C11 needs a call-off/shipment/margin bridge gate. Orderbook headline near local peak produced almost no MFE and severe MAE."}
```

### 6.3 393890 더블유씨피 — separator orderbook/theme rebound without shipment bridge

Entry row: `2024-02-21 c=45750`.  
Observed path: local high `2024-03-07 h=49500`, then lows around `2024-06-28 l=29300` and `2024-11-15 l=12000`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L85_C11_393890_20240221_STAGE2_FALSE_POSITIVE_SEPARATOR_ORDERBOOK_THEME","case_id":"C11_R3L85_393890_WCP_SEPARATOR_ORDERBOOK_THEME","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SEPARATOR_ORDERBOOK_THEME_WITHOUT_SHIPMENT_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-SeparatorOrderbookTheme-NoShipmentMarginBridge","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":45750.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_separator_orderbook_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; separator orderbook/theme rebound treated as insufficient without shipment, utilization and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["separator_orderbook_theme","relative_strength_rebound"],"stage3_evidence_fields":["shipment_bridge_missing","utilization_bridge_missing","customer_calloff_quality_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","shipment_utilization_risk_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","profile_path":"atlas/symbol_profiles/393/393890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.20,"MFE_90D_pct":8.20,"MFE_180D_pct":8.20,"MAE_30D_pct":-13.88,"MAE_90D_pct":-35.96,"MAE_180D_pct":-73.77,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":49500.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":12000.0,"drawdown_after_peak_pct":-75.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"separator_orderbook_theme_peak_without_shipment_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","shipment_utilization_risk_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_separator_orderbook_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean; market_category_change_only_on_2024-06-14","same_entry_group_id":"393890_2024-02-21_45750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C11 should not equate separator orderbook theme with shipment/utilization bridge. Small MFE and deep MAE argue for a local 4B guard."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3L85_078600_DAEJOO_SILICON_ANODE_CUSTOMER_CAPACITY","trigger_id":"R3L85_C11_078600_20240321_STAGE2_SILICON_ANODE_ORDERBOOK_BRIDGE","symbol":"078600","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C11 requires customer/capacity/shipment bridge, not orderbook wording alone","raw_component_scores_before":{"orderbook_score":15,"customer_calloff_quality":13,"capacity_allocation_score":12,"shipment_visibility_score":11,"margin_bridge_score":8,"relative_strength_score":13,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"orderbook_score":17,"customer_calloff_quality":16,"capacity_allocation_score":15,"shipment_visibility_score":13,"margin_bridge_score":10,"relative_strength_score":14,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Customer/capacity bridge and high MFE support Yellow-watch, while exact shipment and margin evidence still block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3L85_247540_ECOPROBM_ORDERBOOK_HEADLINE_CALLOFF_RISK","trigger_id":"R3L85_C11_247540_20240325_STAGE2_FALSE_POSITIVE_CATHODE_ORDERBOOK","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_scope":"current_default_proxy","profile_hypothesis":"orderbook headline without call-off/margin bridge should be blocked","raw_component_scores_before":{"orderbook_score":13,"customer_calloff_quality":3,"capacity_allocation_score":4,"shipment_visibility_score":3,"margin_bridge_score":2,"relative_strength_score":12,"valuation_repricing_score":7,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":33,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"orderbook_score":6,"customer_calloff_quality":0,"capacity_allocation_score":1,"shipment_visibility_score":0,"margin_bridge_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and severe MAE convert orderbook headline into call-off/margin-risk failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3L85_393890_WCP_SEPARATOR_ORDERBOOK_THEME","trigger_id":"R3L85_C11_393890_20240221_STAGE2_FALSE_POSITIVE_SEPARATOR_ORDERBOOK_THEME","symbol":"393890","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_scope":"current_default_proxy","profile_hypothesis":"separator orderbook theme without shipment/utilization bridge should remain Watch/blocked","raw_component_scores_before":{"orderbook_score":9,"customer_calloff_quality":2,"capacity_allocation_score":3,"shipment_visibility_score":2,"margin_bridge_score":1,"relative_strength_score":11,"valuation_repricing_score":6,"execution_risk_score":-13,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":24,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"orderbook_score":3,"customer_calloff_quality":0,"capacity_allocation_score":0,"shipment_visibility_score":0,"margin_bridge_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-20,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and deep MAE require shipment/utilization bridge before any upgrade."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L85_C11_P0_CURRENT","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C11 needs explicit call-off, shipment, capacity and margin bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":25.33,"avg_MAE90_pct":-29.93,"avg_MFE180_pct":25.33,"avg_MAE180_pct":-52.66,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C11_orderbook_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R3L85_C11_P1_SECTOR_SPECIFIC","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_id":"P1_L3_orderbook_calloff_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 battery orderbook signals need customer call-off, capacity allocation, shipment or margin bridge before Stage2-Actionable","changed_axes":["customer_calloff_bridge_required","shipment_visibility_required","margin_bridge_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_calloff_shipment_capacity_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":25.33,"avg_MAE90_pct":-29.93,"avg_MFE180_pct":25.33,"avg_MAE180_pct":-52.66,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R3L85_C11_P2_CANONICAL","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_id":"P2_C11_orderbook_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C11 should reward real orderbook conversion, not headline backlog or battery beta","changed_axes":["C11_calloff_shipment_bridge_required","C11_orderbook_headline_penalty","C11_separator_cathode_bridge_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_calloff_or_shipment_or_capacity_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":25.33,"avg_MAE90_pct":-29.93,"avg_MFE180_pct":25.33,"avg_MAE180_pct":-52.66,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R3L85_C11_P3_COUNTEREXAMPLE_GUARD","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","profile_id":"P3_C11_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-20 while call-off/shipment bridge is missing, block Yellow/Green","changed_axes":["C11_high_MAE_guardrail","C11_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE90_pct":25.33,"avg_MAE90_pct":-29.93,"avg_MFE180_pct":25.33,"avg_MAE180_pct":-52.66,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_ORDERBOOK_CONVERSION_VS_HEADLINE_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":25.33,"avg_MAE90_pct":-29.93,"avg_MFE180_pct":25.33,"avg_MAE180_pct":-52.66,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C11 needs bridge discipline. 078600 shows orderbook rerating works when customer/capacity bridge exists, while 247540 and 393890 show orderbook or battery-beta headlines can fail badly without call-off, shipment, utilization and margin conversion."}
{"row_type":"stage_transition_summary","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"078600","trigger_type":"Stage2-Actionable-SiliconAnodeOrderbookCustomerCapacityBridge-Positive","entry_date":"2024-03-21","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_90D_MAE","stage2_to_180D_outcome":"positive_bridge_with_later_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when customer/capacity bridge exists; Green requires exact call-off, shipment and margin evidence."}
{"row_type":"stage_transition_summary","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"247540","trigger_type":"Stage2-FalsePositive-CathodeOrderbookHeadline-CalloffMarginRisk","entry_date":"2024-03-25","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_orderbook_headline_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Cathode orderbook headline without call-off and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","symbol":"393890","trigger_type":"Stage2-FalsePositive-SeparatorOrderbookTheme-NoShipmentMarginBridge","entry_date":"2024-02-21","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_separator_orderbook_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Separator orderbook/theme rebound without shipment/utilization bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","residual_type":"battery_orderbook_headline_overcredit_without_calloff_shipment_margin_bridge","contribution":"Adds two C11 local 4B/high-MAE counterexamples against one customer/capacity bridge positive, avoiding C11 top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_CUSTOMER_CAPACITY_BRIDGE_VS_ORDERBOOK_HEADLINE_CALLOFF_RISK","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C11 now has non-top-symbol orderbook-headline counterexamples; next R3 loops should exact-URL repair customer call-off, shipment, utilization and margin bridge evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","axis":"C11_calloff_shipment_capacity_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"078600 worked with customer/capacity bridge proxy; 247540 and 393890 failed when orderbook headline lacked call-off, shipment, utilization and margin conversion."}
{"row_type":"shadow_weight","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","axis":"C11_orderbook_headline_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Cathode and separator orderbook/theme spikes showed low MFE and high/deep MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R3","loop":"85","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","axis":"C11_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-20 while call-off/shipment bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - battery_orderbook_headline_overcredit
  - calloff_shipment_bridge_missing
  - separator_utilization_margin_bridge_missing
  - cathode_margin_pressure_high_MAE
new_axis_proposed:
  - C11_calloff_shipment_capacity_bridge_required_shadow_only
  - C11_orderbook_headline_local_4B_watch_guard_shadow_only
  - C11_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C11
  - full_4b_requires_non_price_evidence within C11
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
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
3. Confirm R3 / L3 / C11 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C11 top-covered symbols.
6. If aggregate support remains stable after exact evidence URL repair, consider C11-scoped safe patch candidates:
   - C11_calloff_shipment_capacity_bridge_required
   - C11_orderbook_headline_local_4B_watch_guard
   - C11_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R3
completed_loop = 85
next_round = R4
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.
```
