# E2R Stock-Web v12 Residual Research — R1 Loop 89 / L1 / C03

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R1
loop: 89
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_BACKLOG_FRAMEWORK_BRIDGE_VS_SPACE_SENSOR_THEME_SPIKE_WITHOUT_EXPORT_MARGIN_BRIDGE
sector: industrials / defense / export framework / backlog / space-defense / sensor-defense
output_file: e2r_stock_web_v12_residual_round_R1_loop_89_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R13 loop 88`.

```text
scheduled_round = R1
scheduled_loop = 89
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```

R1 is restricted to L1 industrials / infra / defense / grid.  
C03 is selected because loop88 R1 used C02 power-grid/datacenter CAPEX, and recent R11 loops already walked through C03/C04/C05. C03 still has no 4B/4C count in the No-Repeat snapshot and therefore needs more weak-bridge / theme-spike examples.

No-Repeat Index snapshot:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
rows = 21
symbols = 12
good/bad Stage2 = 11/3
4B/4C = 0/0
top-covered = 079550, 047810, 065450, 005870, 103140, 003570
```

This loop avoids the C03 top-covered symbols and the recent L1 symbols:

```text
R11 loop86 C03: 012450, 010820, 013810
R11 loop87 C04: 051600, 032820, 094820
R11 loop88 C05: 052690, 026150, 028100
R1 loop88 C02: 298040, 388050, 147830
```

Selected symbols:

```text
064350, 099320, 214430
```

This loop tests a distinct C03 pocket:

```text
large defense prime export/backlog framework bridge
vs
space-defense / satellite theme spike without export-contract margin bridge
vs
small-cap defense sensor spike without confirmed export framework backlog bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"064350","company_name":"현대로템","profile_path":"atlas/symbol_profiles/064/064350.json","first_date":"2013-10-30","last_date":"2026-02-20","trading_day_count":3021,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2020-08-14"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"099320","company_name":"쎄트렉아이","profile_path":"atlas/symbol_profiles/099/099320.json","first_date":"2008-06-13","last_date":"2026-02-20","trading_day_count":4364,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["2008-06-27","2019-02-13","2019-03-07","2021-05-11","2024-01-08"],"has_major_raw_discontinuity":true,"calibration_caveat":"A 2024-01-08 corporate-action candidate exists. The selected entry is after that candidate and is marked data-quality watch before patch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_entry_after_2024-01-08_candidate; data_quality_watch"}
{"row_type":"price_source_validation","symbol":"214430","company_name":"아이쓰리시스템","profile_path":"atlas/symbol_profiles/214/214430.json","first_date":"2015-07-30","last_date":"2026-02-20","trading_day_count":2590,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2017-07-14","2017-08-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"064350","trigger_type":"Stage2-Actionable-DefenseExportFrameworkBacklogBridge-Positive","entry_date":"2024-02-22","duplicate_status":"new C03 symbol/trigger/date combination outside top-covered and previous L1 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"099320","trigger_type":"Stage2-FalsePositive-SpaceDefenseSatelliteTheme-NoExportFrameworkMarginBridge","entry_date":"2024-04-24","duplicate_status":"new C03 symbol/trigger/date combination outside top-covered and previous L1 loop symbols; selected after 2024-01-08 corporate-action candidate"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"214430","trigger_type":"Stage2-FalsePositive-DefenseSensorThemeSpike-NoConfirmedExportBacklogBridge","entry_date":"2024-03-25","duplicate_status":"new C03 symbol/trigger/date combination outside top-covered and previous L1 loop symbols"}
```

## 4. Research question

C03 is not “방산 테마가 올랐다.”  
The useful defense signal must show the export-framework bridge: confirmed overseas customer, signed framework or firm order, option visibility, delivery schedule, backlog conversion, government financing, FX / margin protection, localization risk control, and cash conversion. A defense theme without this bridge is only a parade formation; it may look organized from a distance, but E2R needs to see the signed orderbook and delivery cadence.

Residual question:

```text
Can C03 distinguish:
1. defense prime / export framework / backlog bridge with high MFE and manageable entry MAE,
2. space-defense / satellite theme spike where local MFE does not prove export contract or margin conversion,
3. defense sensor / thermal-equipment spike where price strength fades without confirmed export framework, backlog, margin and cash bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C03_R1L89_064350_HYUNDAI_ROTEM_EXPORT_BACKLOG","symbol":"064350","company_name":"현대로템","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-DefenseExportFrameworkBacklogBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE90_and_very_high_MFE180_moderate_MAE","current_profile_verdict":"current_profile_correct_if_export_framework_backlog_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Defense prime/export-framework proxy produced MFE90>20 and MFE180>100 with moderate entry MAE. Green still requires exact export contract, backlog conversion, delivery schedule and margin evidence."}
{"row_type":"case","case_id":"C03_R1L89_099320_SATREC_SPACE_DEFENSE_THEME","symbol":"099320","company_name":"쎄트렉아이","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"SPACE_DEFENSE_SATELLITE_THEME_WITHOUT_EXPORT_FRAMEWORK_MARGIN_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SpaceDefenseSatelliteTheme-NoExportFrameworkMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_sub_Yellow_MFE90_deep_180D_MAE_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_space_defense_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Space/satellite defense theme had sub-Yellow MFE90 from the selected entry and later deep MAE without export framework, delivery schedule, backlog or margin bridge. Data-quality watch remains because of the 2024-01-08 candidate before entry."}
{"row_type":"case","case_id":"C03_R1L89_214430_ITHREE_DEFENSE_SENSOR_THEME","symbol":"214430","company_name":"아이쓰리시스템","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_SENSOR_THEME_SPIKE_WITHOUT_CONFIRMED_EXPORT_BACKLOG_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DefenseSensorThemeSpike-NoConfirmedExportBacklogBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE90_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_sensor_theme_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Defense sensor/thermal-equipment theme spike had low MFE90 and later deep MAE without confirmed export backlog, firm order, delivery and margin bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 064350 현대로템 — defense export framework / backlog bridge positive

Entry row: `2024-02-22 c=34500`.  
Observed path: entry-window low `2024-03-12 l=29900`, 90D high `2024-06-17 h=43000`, and full-window high `2024-11-20 h=69500`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L89_C03_064350_20240222_STAGE2_DEFENSE_EXPORT_BACKLOG","case_id":"C03_R1L89_064350_HYUNDAI_ROTEM_EXPORT_BACKLOG","symbol":"064350","company_name":"현대로템","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-DefenseExportFrameworkBacklogBridge-Positive","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":34500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_defense_export_framework_backlog_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; export framework, delivery schedule and backlog conversion bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["export_framework_proxy","firm_order_or_option_proxy","delivery_schedule_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_export_contract_pending","backlog_conversion_pending","margin_protection_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.46,"MFE_90D_pct":24.64,"MFE_180D_pct":101.45,"MAE_30D_pct":-13.33,"MAE_90D_pct":-13.33,"MAE_180D_pct":-13.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-20","peak_price":69500.0,"max_drawdown_low_date":"2024-03-12","max_drawdown_low":29900.0,"drawdown_after_peak_pct":-36.26,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_export_contract_backlog_margin_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_and_very_high_MFE180_moderate_MAE","current_profile_verdict":"current_profile_correct_if_export_framework_backlog_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"064350_2024-02-22_34500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C03 can allow Stage2/Yellow when defense strength is tied to export framework, signed order or option visibility, delivery schedule, backlog conversion, margin protection and cash bridge. Green still requires exact evidence."}
```

### 6.2 099320 쎄트렉아이 — space-defense / satellite theme without export framework margin bridge

Entry row: `2024-04-24 c=49300`, after the 2024-01-08 corporate-action candidate.  
Observed path: local high `2024-07-01 h=58500`, then lows around `2024-09-24 l=35250` and `2024-12-09 l=36000`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L89_C03_099320_20240424_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_THEME","case_id":"C03_R1L89_099320_SATREC_SPACE_DEFENSE_THEME","symbol":"099320","company_name":"쎄트렉아이","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"SPACE_DEFENSE_SATELLITE_THEME_WITHOUT_EXPORT_FRAMEWORK_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SpaceDefenseSatelliteTheme-NoExportFrameworkMarginBridge","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":49300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_space_defense_satellite_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; space-defense/satellite theme treated as insufficient without export framework, firm order, delivery schedule, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["space_defense_theme","satellite_export_keyword","relative_strength_extension"],"stage3_evidence_fields":["export_framework_missing","firm_order_missing","delivery_schedule_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","export_margin_bridge_missing_watch","data_quality_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/099/099320/2024.csv","profile_path":"atlas/symbol_profiles/099/099320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.65,"MFE_90D_pct":18.66,"MFE_180D_pct":18.66,"MAE_30D_pct":-6.59,"MAE_90D_pct":-9.94,"MAE_180D_pct":-28.50,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-01","peak_price":58500.0,"max_drawdown_low_date":"2024-09-24","max_drawdown_low":35250.0,"drawdown_after_peak_pct":-39.74,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"space_defense_theme_without_export_framework_margin_bridge_should_remain_watch_4B_not_Yellow","four_b_evidence_type":["price_only","export_margin_bridge_missing_watch","data_quality_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE90_deep_180D_MAE_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_space_defense_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["data_quality_watch_due_to_2024-01-08_candidate_before_entry"],"corporate_action_window_status":"selected_entry_after_2024-01-08_candidate","same_entry_group_id":"099320_2024-04-24_49300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C03 should not promote space-defense or satellite theme strength unless export framework, firm order, delivery and margin/cash bridge are repaired. Sub-Yellow MFE90 and deep 180D MAE require Watch/4B routing."}
```

### 6.3 214430 아이쓰리시스템 — defense sensor theme spike without confirmed export backlog bridge

Entry row: `2024-03-25 c=46750`.  
Observed path: local high `2024-03-29 h=51200`, then low `2024-10-02 l=31200`, and later partial rebound that should not validate the original weak-bridge entry.

```jsonl
{"row_type":"trigger","trigger_id":"R1L89_C03_214430_20240325_STAGE2_FALSE_POSITIVE_DEFENSE_SENSOR_THEME","case_id":"C03_R1L89_214430_ITHREE_DEFENSE_SENSOR_THEME","symbol":"214430","company_name":"아이쓰리시스템","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_SENSOR_THEME_SPIKE_WITHOUT_CONFIRMED_EXPORT_BACKLOG_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-DefenseSensorThemeSpike-NoConfirmedExportBacklogBridge","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":46750.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_defense_sensor_thermal_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; defense sensor/thermal-equipment theme treated as insufficient without export framework, confirmed backlog, delivery schedule and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["defense_sensor_theme","thermal_equipment_keyword","relative_strength_spike"],"stage3_evidence_fields":["confirmed_export_backlog_missing","delivery_schedule_missing","margin_protection_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","export_backlog_bridge_missing_watch","late_rebound_not_entry_validation"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214430/2024.csv","profile_path":"atlas/symbol_profiles/214/214430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.52,"MFE_90D_pct":9.52,"MFE_180D_pct":9.52,"MAE_30D_pct":-18.50,"MAE_90D_pct":-18.50,"MAE_180D_pct":-33.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-29","peak_price":51200.0,"max_drawdown_low_date":"2024-10-02","max_drawdown_low":31200.0,"drawdown_after_peak_pct":-39.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"defense_sensor_theme_without_confirmed_export_backlog_bridge_should_be_4B_watch_not_positive; late_rebound_not_entry_validation","four_b_evidence_type":["price_only","export_backlog_bridge_missing_watch","late_rebound_not_entry_validation"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE90_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_sensor_theme_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"214430_2024-03-25_46750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C03 should not count defense sensor theme MFE as export-backlog proof. Low MFE90 and deep 180D MAE support 4B-watch unless exact export framework, backlog, delivery and margin evidence is repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C03_R1L89_064350_HYUNDAI_ROTEM_EXPORT_BACKLOG","trigger_id":"R1L89_C03_064350_20240222_STAGE2_DEFENSE_EXPORT_BACKLOG","symbol":"064350","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C03 requires export framework, delivery schedule, backlog conversion and margin bridge rather than defense theme alone","raw_component_scores_before":{"export_framework_score":14,"firm_order_option_score":12,"delivery_schedule_score":11,"backlog_conversion_score":12,"margin_protection_score":8,"cash_conversion_score":6,"relative_strength_score":12,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"export_framework_score":17,"firm_order_option_score":15,"delivery_schedule_score":14,"backlog_conversion_score":15,"margin_protection_score":10,"cash_conversion_score":8,"relative_strength_score":13,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Export framework and backlog bridge plus MFE90>20 support Yellow-watch; exact order/backlog/margin evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C03_R1L89_099320_SATREC_SPACE_DEFENSE_THEME","trigger_id":"R1L89_C03_099320_20240424_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_THEME","symbol":"099320","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_scope":"current_default_proxy","profile_hypothesis":"space-defense theme without export framework and margin bridge should remain Watch/4B","raw_component_scores_before":{"export_framework_score":2,"firm_order_option_score":1,"delivery_schedule_score":1,"backlog_conversion_score":0,"margin_protection_score":0,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":5,"execution_risk_score":-10,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_framework_score":0,"firm_order_option_score":0,"delivery_schedule_score":0,"backlog_conversion_score":0,"margin_protection_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-Yellow MFE90 and deep 180D MAE require export framework, delivery and margin evidence before any Yellow/Green promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C03_R1L89_214430_ITHREE_DEFENSE_SENSOR_THEME","trigger_id":"R1L89_C03_214430_20240325_STAGE2_FALSE_POSITIVE_DEFENSE_SENSOR_THEME","symbol":"214430","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_scope":"current_default_proxy","profile_hypothesis":"defense sensor theme spike without confirmed export backlog should be blocked","raw_component_scores_before":{"export_framework_score":1,"firm_order_option_score":1,"delivery_schedule_score":0,"backlog_conversion_score":0,"margin_protection_score":0,"cash_conversion_score":0,"relative_strength_score":11,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_framework_score":0,"firm_order_option_score":0,"delivery_schedule_score":0,"backlog_conversion_score":0,"margin_protection_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE90 and deep 180D MAE convert the defense sensor spike into missing export-backlog bridge failure."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R1L89_C03_P0_CURRENT","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C03 needs explicit export-framework, delivery, backlog, margin and cash bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":17.61,"avg_MAE90_pct":-13.92,"avg_MFE180_pct":43.21,"avg_MAE180_pct":-25.03,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.67,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C03_export_backlog_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R1L89_C03_P1_SECTOR_SPECIFIC","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P1_L1_defense_export_backlog_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 defense signals need export framework, confirmed order, delivery schedule, backlog conversion, margin protection or cash bridge before Stage2-Actionable","changed_axes":["export_framework_required","backlog_margin_required","defense_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_export_framework_firm_order_delivery_backlog_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":17.61,"avg_MAE90_pct":-13.92,"avg_MFE180_pct":43.21,"avg_MAE180_pct":-25.03,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R1L89_C03_P2_CANONICAL","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P2_C03_export_backlog_margin_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C03 should reward export/order/backlog mechanics, not defense-space-sensor theme labels","changed_axes":["C03_export_framework_backlog_margin_bridge_required","C03_space_sensor_theme_local_4B_guard","C03_late_rebound_not_export_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"export_framework_or_firm_order_plus_delivery_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":17.61,"avg_MAE90_pct":-13.92,"avg_MFE180_pct":43.21,"avg_MAE180_pct":-25.03,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R1L89_C03_P3_COUNTEREXAMPLE_GUARD","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P3_C03_low_MFE_deep_180D_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<20 and MAE180<=-25 while export/backlog/margin bridge is missing, block Yellow/Green and route to 4B-watch","changed_axes":["C03_low_MFE_guardrail","C03_deep_180D_MAE_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_20_and_MAE180_le_minus_25_with_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":17.61,"avg_MAE90_pct":-13.92,"avg_MFE180_pct":43.21,"avg_MAE180_pct":-25.03,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_DEFENSE_EXPORT_BACKLOG_VS_SPACE_SENSOR_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":17.61,"avg_MAE90_pct":-13.92,"avg_MFE180_pct":43.21,"avg_MAE180_pct":-25.03,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_20":0.67,"stage2_bad_entry_rate_MAE180_le_minus_25":0.67,"interpretation":"C03 needs bridge discipline. 현대로템 shows defense export framework/backlog bridge can rerate over 90D and 180D, while 쎄트렉아이 and 아이쓰리시스템 show space-defense/sensor theme strength should not be promoted without confirmed export framework, order, delivery, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"064350","trigger_type":"Stage2-Actionable-DefenseExportFrameworkBacklogBridge-Positive","entry_date":"2024-02-22","stage2_to_90D_outcome":"good_stage2_MFE90_ge20_moderate_MAE","stage2_to_180D_outcome":"positive_export_backlog_rerating_with_late_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when export framework, delivery schedule, backlog and margin bridge exists; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"099320","trigger_type":"Stage2-FalsePositive-SpaceDefenseSatelliteTheme-NoExportFrameworkMarginBridge","entry_date":"2024-04-24","stage2_to_90D_outcome":"weak_stage2_sub_Yellow_MFE","stage2_to_180D_outcome":"failed_space_defense_theme_deep_180D_MAE","MFE90_ge_20":false,"MAE180_le_minus_25":true,"transition_note":"Space-defense/satellite theme without export framework and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"214430","trigger_type":"Stage2-FalsePositive-DefenseSensorThemeSpike-NoConfirmedExportBacklogBridge","entry_date":"2024-03-25","stage2_to_90D_outcome":"weak_stage2_low_MFE_moderate_MAE","stage2_to_180D_outcome":"failed_sensor_theme_deep_180D_MAE","MFE90_ge_20":false,"MAE180_le_minus_25":true,"transition_note":"Defense sensor theme spike without export backlog bridge should remain Watch/4B-risk; late rebound is not original-entry validation."}
{"row_type":"residual_contribution","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","residual_type":"defense_space_sensor_theme_overcredit_without_export_framework_backlog_margin_bridge","contribution":"Adds two C03 local 4B/Watch counterexamples against one defense-prime export/backlog positive, avoiding C03 top-covered and previous L1 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_BACKLOG_FRAMEWORK_BRIDGE_VS_SPACE_SENSOR_THEME_SPIKE_WITHOUT_EXPORT_MARGIN_BRIDGE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C03 now has a non-top-symbol defense-prime export positive and two space/sensor defense weak-bridge counterexamples; next R1 loops should exact-URL repair export contract, delivery schedule, order option, backlog conversion, margin protection and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"C03_export_framework_backlog_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"064350 worked when export-framework/backlog proxy was present; 099320 and 214430 were weak or failed when only space-defense/sensor theme existed."}
{"row_type":"shadow_weight","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"C03_space_sensor_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Space/sensor defense rows showed sub-20 MFE90 and deep 180D MAE without non-price export bridge."}
{"row_type":"shadow_weight","round":"R1","loop":"89","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"C03_late_rebound_not_export_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"214430 shows later rebound should not validate the original sensor-theme entry without confirmed export framework, backlog, delivery and margin bridge."}
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
  - defense_space_theme_overcredit
  - defense_sensor_theme_overcredit
  - export_framework_bridge_missing
  - backlog_margin_cash_bridge_missing
new_axis_proposed:
  - C03_export_framework_backlog_margin_bridge_required_shadow_only
  - C03_space_sensor_theme_local_4B_watch_guard_shadow_only
  - C03_late_rebound_not_export_validation_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C03
  - full_4b_requires_non_price_evidence within C03
  - hard_4c_thesis_break_routes_to_4c within C03
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
`099320` has a 2024-01-08 corporate-action candidate before the selected entry, so it remains usable as post-candidate price-path evidence but should keep a data-quality watch before any production patch.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 099320
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
3. Confirm R1 / L1 / C03 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C03 top-covered symbols
   - previous R11 loop86 C03 symbols
   - previous R11 loop87 C04 symbols
   - previous R11 loop88 C05 symbols
   - previous R1 loop88 C02 symbols
6. Keep 099320 in data-quality watch because of the 2024-01-08 corporate-action candidate.
7. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C03-scoped safe patch candidates:
   - C03_export_framework_backlog_margin_bridge_required
   - C03_space_sensor_theme_local_4B_watch_guard
   - C03_late_rebound_not_export_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R1
completed_loop = 89
next_round = R2
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.
```
