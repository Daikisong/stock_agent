# E2R Stock-Web v12 Residual Research — R1 Loop 93 / L1 / C01 Secondary

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R1
loop: 93
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: POWER_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_CABLE_THEME_PRICE_MFE_AND_SHARECOUNT_NOISE
sector: industrials / power equipment / grid / cable / transformer / order backlog / margin bridge / working capital / cash conversion
output_file: e2r_stock_web_v12_residual_round_R1_loop_93_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_SECONDARY_POWER_EQUIPMENT_CABLE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This is the valid output for the current execution.

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

After the local loop93 additions, the reconciled thin axes still leave C01 as one of the lightest non-stabilized buckets. C09 was just expanded in the previous valid run, so this run rotates back to C01 while avoiding the earlier C01 shipbuilding pocket.

Avoided C01 and adjacent recent symbols:

```text
R1 loop93 C01 prior: 329180, 097230, 010620
R1 loop92 C02: 267260, 037030, 237750
R2 loop93 C08/C09/C07/C06/C10 symbols are excluded as semiconductor pockets.
```

Selected symbols:

```text
010120, 001440, 006340
```

Selected pocket:

```text
power-equipment / automation backlog-margin bridge positive-watch
vs
cable order/backlog theme price-MFE without clean margin/cash bridge
vs
wire/cable theme blowoff with share-count movement and no durable backlog-margin bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"010120","company_name":"LS ELECTRIC","profile_path":"atlas/symbol_profiles/010/010120.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7749,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1995-09-28","1999-04-08","1999-07-26","2003-04-16"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist long before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
{"row_type":"price_source_validation","symbol":"001440","company_name":"대한전선","profile_path":"atlas/symbol_profiles/001/001440.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7465,"corporate_action_candidate_count":11,"corporate_action_candidate_dates":["2002-04-22","2003-10-13","2010-05-03","2010-10-18","2012-11-08","2012-12-21","2014-01-10","2015-12-08","2022-03-30","2023-05-16","2024-04-02"],"has_major_raw_discontinuity":true,"calibration_caveat":"2024-04-02 corporate-action/share-count candidate occurs before selected post-spike entry; use only with data-quality repair watch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_2024_entry_after_CA_candidate; data_quality_watch"}
{"row_type":"price_source_validation","symbol":"006340","company_name":"대원전선","profile_path":"atlas/symbol_profiles/006/006340.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7742,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1996-11-29","1997-06-19","1999-09-10","2000-03-21","2007-01-25","2010-05-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 window; however 2024 row stream shows share-count movement after April, so keep share-count watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; share_count_movement_watch"}
```

## 3. Novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"010120","trigger_type":"Stage2-Actionable-PowerEquipmentOrderBacklogMarginBridge-PositiveWatch","entry_date":"2024-02-27","duplicate_status":"new C01 symbol/trigger/date combination outside prior C01 loop93 shipbuilding symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"001440","trigger_type":"Stage2-FalsePositive-CableOrderBacklogThemePriceMFENoCleanMarginCashBridge","entry_date":"2024-05-20","duplicate_status":"new C01 symbol/trigger/date combination; post-CA/share-count data-quality watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"006340","trigger_type":"Stage2-FalsePositive-WireCableThemeBlowoffNoDurableBacklogMarginBridge","entry_date":"2024-05-13","duplicate_status":"new C01 symbol/trigger/date combination; share-count movement watch"}
```

## 4. Research question

C01 is not “수주잔고가 많다.”
The useful order-backlog signal has to show the backlog-to-margin chain:

```text
credible customer or project backlog
order quality and delivery schedule
price-cost spread
production slot / utilization visibility
margin bridge
working-capital discipline
cash conversion
```

A backlog headline is a signed work order on a clipboard. It becomes an E2R signal only when the factory slot, delivery schedule, price-cost spread, margin and cash ledger line up.

Residual question:

```text
Can C01 distinguish:
1. power equipment / grid automation order-backlog bridge with extreme MFE and controlled entry MAE,
2. cable backlog theme price-MFE that was data-quality noisy and later rolled over,
3. wire/cable theme blowoff with share-count movement and no durable backlog-margin bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C01_R1L93B_010120_LS_ELECTRIC_POWER_BACKLOG","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"POWER_EQUIPMENT_GRID_AUTOMATION_ORDER_BACKLOG_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-PowerEquipmentOrderBacklogMarginBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_extreme_MFE90_controlled_MAE_orderbacklog_margin_bridge","current_profile_verdict":"current_profile_correct_if_order_quality_delivery_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"Power equipment / grid automation backlog-margin proxy after a February reset produced extreme MFE with controlled MAE. Green still requires exact customer/order/delivery/margin/cash evidence."}
{"row_type":"case","case_id":"C01_R1L93B_001440_TAIHAN_CABLE_MFE_DATAQUALITY","symbol":"001440","company_name":"대한전선","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CABLE_ORDER_BACKLOG_THEME_PRICE_MFE_WITHOUT_CLEAN_MARGIN_CASH_BRIDGE","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CableOrderBacklogThemePriceMFENoCleanMarginCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"score_price_alignment":"counterexample_price_MFE_but_deep_MAE_share_count_watch_no_clean_margin_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_cable_theme_price_MFE_overcredited_without_margin_cash_and_CA_repair","price_source":"Songdaiki/stock-web","notes":"Cable/orderbook theme produced price-MFE but the post-CA/share-count context and later drawdown mean it should remain evidence-repair/4B-watch, not C01 positive."}
{"row_type":"case","case_id":"C01_R1L93B_006340_DAEWON_CABLE_BLOWOFF","symbol":"006340","company_name":"대원전선","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"WIRE_CABLE_THEME_BLOWOFF_WITHOUT_DURABLE_BACKLOG_MARGIN_BRIDGE","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-WireCableThemeBlowoffNoDurableBacklogMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"counterexample_post_spike_low_MFE_deep_MAE_share_count_watch_no_backlog_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_wire_cable_theme_blowoff_counted_as_orderbacklog_margin_bridge","price_source":"Songdaiki/stock-web","notes":"Wire/cable theme blowoff after May spike had low forward MFE and deep drawdown when durable backlog, delivery, spread/margin and cash bridge were not repaired."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 010120 LS ELECTRIC — power equipment / grid automation backlog-margin bridge

Entry row: `2024-02-27 c=63200`, after early-year reset.
Observed path: high `2024-05-29 h=244000`; entry-zone low `2024-02-28 l=63100`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L93B_C01_010120_20240227_STAGE2_POWER_EQUIPMENT_BACKLOG","case_id":"C01_R1L93B_010120_LS_ELECTRIC_POWER_BACKLOG","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"POWER_EQUIPMENT_GRID_AUTOMATION_ORDER_BACKLOG_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-PowerEquipmentOrderBacklogMarginBridge-PositiveWatch","trigger_date":"2024-02-27","entry_date":"2024-02-27","entry_price":63200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_power_equipment_grid_orderbacklog_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; power equipment/grid automation backlog, delivery schedule, price-cost spread, margin and cash bridge treated as non-price proxy","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["power_equipment_orderbacklog_proxy","grid_automation_customer_proxy","delivery_schedule_proxy","price_cost_spread_proxy"],"stage3_evidence_fields":["exact_order_source_pending","delivery_schedule_source_pending","margin_source_pending","cash_conversion_source_pending"],"stage4b_evidence_fields":["extreme_MFE_watch","Green_exact_evidence_watch"],"stage4c_evidence_fields":["order_margin_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":104.43,"MFE_90D_pct":286.08,"MFE_180D_pct":286.08,"MAE_30D_pct":-0.16,"MAE_90D_pct":-0.16,"MAE_180D_pct":-0.16,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-29","peak_price":244000.0,"max_drawdown_low_date":"2024-02-28","max_drawdown_low":63100.0,"drawdown_after_peak_pct":-22.05,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.37,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_order_delivery_margin_cash_evidence","four_b_evidence_type":["extreme_MFE_watch","Green_exact_evidence_watch"],"four_c_protection_label":"order_margin_break_watch_only","trigger_outcome_label":"positive_extreme_MFE90_controlled_MAE_orderbacklog_margin_bridge","current_profile_verdict":"current_profile_correct_if_order_quality_delivery_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"010120_2024-02-27_63200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C01 can allow Yellow/Green-candidate-watch when backlog strength is tied to order quality, delivery, margin and cash conversion. Extreme MFE alone does not loosen Green."}
```

### 6.2 001440 대한전선 — cable order/backlog theme price-MFE without clean margin-cash bridge

Entry row: `2024-05-20 c=19680`, after a sharp cable theme spike.
Observed path: high `2024-05-21 h=20950`, later low `2024-12-09 l=10000`. Profile includes a 2024-04-02 corporate-action/share-count candidate before entry.

```jsonl
{"row_type":"trigger","trigger_id":"R1L93B_C01_001440_20240520_STAGE2_FALSE_POSITIVE_CABLE_PRICE_MFE","case_id":"C01_R1L93B_001440_TAIHAN_CABLE_MFE_DATAQUALITY","symbol":"001440","company_name":"대한전선","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CABLE_ORDER_BACKLOG_THEME_PRICE_MFE_WITHOUT_CLEAN_MARGIN_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;data_quality_watch;price_MFE_not_bridge_validation","trigger_type":"Stage2-FalsePositive-CableOrderBacklogThemePriceMFENoCleanMarginCashBridge","trigger_date":"2024-05-20","entry_date":"2024-05-20","entry_price":19680.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cable_orderbook_theme_price_MFE_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cable/orderbook theme and price-MFE treated as insufficient without clean backlog quality, delivery schedule, margin/cash bridge and CA/share-count repair","evidence_source_type":"historical_public_theme_report_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["cable_orderbook_theme","price_MFE","grid_infra_vocabulary"],"stage3_evidence_fields":["clean_order_quality_missing","delivery_margin_bridge_missing","cash_conversion_missing","CA_share_count_repair_pending"],"stage4b_evidence_fields":["price_MFE_without_bridge","deep_late_MAE","CA_share_count_watch"],"stage4c_evidence_fields":["margin_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001440/2024.csv","profile_path":"atlas/symbol_profiles/001/001440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.45,"MFE_90D_pct":6.45,"MFE_180D_pct":6.45,"MAE_30D_pct":-22.10,"MAE_90D_pct":-27.19,"MAE_180D_pct":-49.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":20950.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":10000.0,"drawdown_after_peak_pct":-52.27,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"cable_theme_price_MFE_without_clean_order_delivery_margin_cash_bridge_and_CA_repair_should_be_4B_watch","four_b_evidence_type":["price_MFE_without_bridge","deep_late_MAE","CA_share_count_watch"],"four_c_protection_label":"margin_break_watch_only","trigger_outcome_label":"counterexample_price_MFE_but_deep_MAE_share_count_watch_no_clean_margin_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_cable_theme_price_MFE_overcredited_without_margin_cash_and_CA_repair","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024-04-02_corporate_action_share_count_candidate_before_entry"],"corporate_action_window_status":"selected_entry_after_2024-04-02_candidate; data_quality_watch","same_entry_group_id":"001440_2024-05-20_19680","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"do_not_count_as_new_case":false,"current_profile_residual":"C01 should not count cable theme price-MFE as backlog-margin validation unless order quality, delivery, margin/cash and CA/share-count evidence are repaired."}
```

### 6.3 006340 대원전선 — wire/cable blowoff without durable backlog-margin bridge

Entry row: `2024-05-13 c=4885`, near the cable theme blowoff.
Observed path: same-day high `2024-05-13 h=5450`, later low `2024-12-09 l=2205`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L93B_C01_006340_20240513_STAGE2_FALSE_POSITIVE_WIRE_CABLE_BLOWOFF","case_id":"C01_R1L93B_006340_DAEWON_CABLE_BLOWOFF","symbol":"006340","company_name":"대원전선","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"WIRE_CABLE_THEME_BLOWOFF_WITHOUT_DURABLE_BACKLOG_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;post_spike_entry_guard;share_count_watch","trigger_type":"Stage2-FalsePositive-WireCableThemeBlowoffNoDurableBacklogMarginBridge","trigger_date":"2024-05-13","entry_date":"2024-05-13","entry_price":4885.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_wire_cable_grid_theme_blowoff_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; wire/cable grid theme treated as insufficient without durable backlog, delivery, price-cost spread, margin and cash bridge","evidence_source_type":"historical_public_theme_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["wire_cable_theme","grid_infra_vocabulary","post_spike_relative_strength"],"stage3_evidence_fields":["durable_backlog_missing","delivery_schedule_missing","price_cost_spread_missing","margin_cash_bridge_missing","share_count_repair_pending"],"stage4b_evidence_fields":["post_spike_low_MFE","deep_MAE","share_count_movement_watch"],"stage4c_evidence_fields":["theme_blowoff_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv","profile_path":"atlas/symbol_profiles/006/006340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.57,"MFE_90D_pct":11.57,"MFE_180D_pct":11.57,"MAE_30D_pct":-31.73,"MAE_90D_pct":-31.73,"MAE_180D_pct":-54.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-13","peak_price":5450.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":2205.0,"drawdown_after_peak_pct":-59.54,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"wire_cable_theme_blowoff_without_durable_backlog_delivery_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["post_spike_low_MFE","deep_MAE","share_count_movement_watch"],"four_c_protection_label":"theme_blowoff_watch_only","trigger_outcome_label":"counterexample_post_spike_low_MFE_deep_MAE_share_count_watch_no_backlog_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_wire_cable_theme_blowoff_counted_as_orderbacklog_margin_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["visible_2024_share_count_movement_watch"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_usable; 2024_share_count_watch","same_entry_group_id":"006340_2024-05-13_4885","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C01 should not treat wire/cable theme blowoff as backlog-margin evidence unless durable backlog, delivery, price-cost spread, margin and cash evidence are repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_R1L93B_010120_LS_ELECTRIC_POWER_BACKLOG","trigger_id":"R1L93B_C01_010120_20240227_STAGE2_POWER_EQUIPMENT_BACKLOG","symbol":"010120","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_scope":"current_default_proxy","profile_hypothesis":"C01 should reward backlog-to-margin mechanics, not merely power-equipment vocabulary","raw_component_scores_before":{"order_backlog_score":14,"customer_project_quality_score":13,"delivery_schedule_score":12,"price_cost_spread_score":11,"utilization_score":10,"margin_bridge_score":11,"working_capital_score":8,"cash_conversion_score":8,"relative_strength_score":15,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":4},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"order_backlog_score":17,"customer_project_quality_score":16,"delivery_schedule_score":15,"price_cost_spread_score":14,"utilization_score":12,"margin_bridge_score":14,"working_capital_score":10,"cash_conversion_score":10,"relative_strength_score":17,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":92,"stage_label_after":"Stage3-Green-candidate-watch","component_delta_explanation":"Extreme MFE and shallow MAE align with backlog-margin bridge, but exact evidence is still required before Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_R1L93B_001440_TAIHAN_CABLE_MFE_DATAQUALITY","trigger_id":"R1L93B_C01_001440_20240520_STAGE2_FALSE_POSITIVE_CABLE_PRICE_MFE","symbol":"001440","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_scope":"current_default_proxy","profile_hypothesis":"cable theme price-MFE without clean order quality and margin/cash bridge should be blocked","raw_component_scores_before":{"order_backlog_score":3,"customer_project_quality_score":1,"delivery_schedule_score":0,"price_cost_spread_score":0,"utilization_score":0,"margin_bridge_score":0,"working_capital_score":0,"cash_conversion_score":0,"relative_strength_score":5,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"order_backlog_score":0,"customer_project_quality_score":0,"delivery_schedule_score":0,"price_cost_spread_score":0,"utilization_score":0,"margin_bridge_score":0,"working_capital_score":0,"cash_conversion_score":0,"relative_strength_score":0,"execution_risk_score":-30,"theme_spike_risk":-22,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Price-MFE and cable vocabulary do not validate missing backlog-margin bridge, especially with CA/share-count watch and deep drawdown."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_R1L93B_006340_DAEWON_CABLE_BLOWOFF","trigger_id":"R1L93B_C01_006340_20240513_STAGE2_FALSE_POSITIVE_WIRE_CABLE_BLOWOFF","symbol":"006340","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","profile_scope":"current_default_proxy","profile_hypothesis":"wire/cable theme blowoff without durable backlog-margin and cash bridge should remain Watch/4B","raw_component_scores_before":{"order_backlog_score":2,"customer_project_quality_score":0,"delivery_schedule_score":0,"price_cost_spread_score":0,"utilization_score":0,"margin_bridge_score":0,"working_capital_score":0,"cash_conversion_score":0,"relative_strength_score":5,"execution_risk_score":-20,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"order_backlog_score":0,"customer_project_quality_score":0,"delivery_schedule_score":0,"price_cost_spread_score":0,"utilization_score":0,"margin_bridge_score":0,"working_capital_score":0,"cash_conversion_score":0,"relative_strength_score":0,"execution_risk_score":-32,"theme_spike_risk":-24,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Post-spike low MFE and deep MAE route cable-theme rows to 4B until backlog/margin/cash evidence is repaired."}
```

## 8. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_POWER_EQUIPMENT_POSITIVE_VS_CABLE_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":2,"avg_MFE90_pct":101.37,"avg_MAE90_pct":-19.69,"avg_MFE180_pct":101.37,"avg_MAE180_pct":-34.74,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"interpretation":"C01 needs bridge discipline. LS ELECTRIC shows order/delivery/margin/cash bridge can support Green-candidate-watch, while 대한전선 and 대원전선 show cable theme and price-MFE should not be promoted without clean backlog quality, delivery, price-cost spread, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"010120","trigger_type":"Stage2-Actionable-PowerEquipmentOrderBacklogMarginBridge-PositiveWatch","entry_date":"2024-02-27","stage2_to_90D_outcome":"positive_extreme_MFE90_low_MAE","stage2_to_180D_outcome":"power_equipment_backlog_margin_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/Green-candidate when backlog is tied to customer/order/delivery/margin/cash bridge; exact evidence required for Green."}
{"row_type":"stage_transition_summary","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"001440","trigger_type":"Stage2-FalsePositive-CableOrderBacklogThemePriceMFENoCleanMarginCashBridge","entry_date":"2024-05-20","stage2_to_90D_outcome":"bad_stage2_low_forward_MFE_deep_MAE_data_quality_watch","stage2_to_180D_outcome":"failed_cable_price_MFE_no_clean_margin_cash_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Cable theme price-MFE without clean backlog/margin/cash bridge and CA repair should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","symbol":"006340","trigger_type":"Stage2-FalsePositive-WireCableThemeBlowoffNoDurableBacklogMarginBridge","entry_date":"2024-05-13","stage2_to_90D_outcome":"bad_stage2_post_spike_low_MFE_deep_MAE_share_count_watch","stage2_to_180D_outcome":"failed_wire_cable_theme_no_backlog_margin_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Wire/cable theme blowoff without durable backlog, delivery and margin bridge should remain Watch/4B."}
{"row_type":"residual_contribution","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","residual_type":"power_equipment_orderbacklog_positive_vs_cable_theme_price_MFE_sharecount_decay","contribution":"Adds one C01 power-equipment backlog positive-watch and two cable-theme weak-bridge counterexamples, rotating away from prior shipbuilding C01 pocket.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"POWER_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_CABLE_THEME_PRICE_MFE_AND_SHARECOUNT_NOISE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C01 now has a secondary non-shipbuilding pocket: power-equipment backlog positive-watch and cable/wire weak-bridge price-MFE counterexamples; next C01 loops should exact-URL repair order quality, delivery schedule, price-cost spread, margin and cash conversion."}
```

## 9. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"C01_order_quality_delivery_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"010120 worked when power-equipment order/delivery/margin proxy existed; 001440 and 006340 failed when cable-theme vocabulary lacked clean margin/cash bridge."}
{"row_type":"shadow_weight","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"C01_cable_theme_price_MFE_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"001440 and 006340 showed price-MFE or blowoff behavior should not validate missing backlog-margin mechanics."}
{"row_type":"shadow_weight","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"C01_CA_share_count_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"001440 has a 2024-04-02 corporate-action/share-count candidate; 006340 shows 2024 share-count movement in row stream."}
{"row_type":"shadow_weight","round":"R1","loop":"93","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","axis":"C01_extreme_MFE_Green_exact_evidence_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"010120 had extreme MFE, but Green still requires exact order/delivery/margin/cash evidence."}
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
  - cable_theme_price_MFE_overcredit
  - wire_cable_blowoff_overcredit
  - order_quality_delivery_margin_cash_bridge_missing
  - CA_share_count_data_quality_watch
new_axis_proposed:
  - C01_order_quality_delivery_margin_cash_bridge_required_shadow_only
  - C01_cable_theme_price_MFE_local_4B_guard_shadow_only
  - C01_CA_share_count_data_quality_guard_shadow_only
  - C01_extreme_MFE_Green_exact_evidence_guard_shadow_only
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

## 11. Data-quality caveat

All selected triggers use Stock-Web tradable raw OHLC rows.
`010120` has only historical corporate-action/name-transition candidates before selected 2024 window; selected 2024 window is usable.
`001440` has a 2024-04-02 corporate-action/share-count candidate before selected post-spike entry; it is usable only as data-quality watch unless repaired.
`006340` has old corporate-action/name-transition candidates before 2024, but visible 2024 share-count movement appears in the row stream; it remains share-count watch before patching.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for residual price-path analysis
evidence_url_pending = true
source_proxy_only = true
CA_share_count_watch = true for 001440
share_count_movement_watch = true for 006340
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
3. Confirm R1 / L1 / C01 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided previous R1 loop93 C01 symbols 329180/097230/010620 and adjacent R1 loop92 C02 symbols.
6. Confirm recently touched C09/C08/C28/C23/C17/C13/C12 rows are not ingested from this MD.
7. Treat 010120 as Green-candidate-watch only, not Green, until exact order/delivery/margin/cash evidence is repaired.
8. Treat 001440 and 006340 as weak-bridge/data-quality failure modes unless exact order/margin/cash and share-count repairs are added later.
9. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C01-scoped safe patch candidates:
   - C01_order_quality_delivery_margin_cash_bridge_required
   - C01_cable_theme_price_MFE_local_4B_guard
   - C01_CA_share_count_data_quality_guard
   - C01_extreme_MFE_Green_exact_evidence_guard
10. Do not loosen Stage3-Green.
11. Do not use future MFE/MAE in runtime scoring.
12. Use this MD only for calibration profile planning.
```

## 13. Round state

```text
completed_round = R1
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C08 or C09 depending on reconciled local-loop count and fatigue controls
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 14. Final one-line contribution

```text
This loop adds 3 new independent C01 cases, 1 power-equipment order-backlog positive-watch, 2 cable-theme weak-bridge counterexamples, and 2 local 4B-watch rows for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01_ORDER_BACKLOG_MARGIN_BRIDGE.
```
