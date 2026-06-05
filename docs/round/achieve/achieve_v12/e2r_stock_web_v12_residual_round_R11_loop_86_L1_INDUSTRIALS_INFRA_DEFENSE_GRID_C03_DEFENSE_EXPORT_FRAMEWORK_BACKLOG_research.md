# E2R Stock-Web v12 Residual Research — R11 Loop 86 / L1 / C03

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R11
loop: 86
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE_VS_GEOPOLITICAL_DEFENSE_THEME_SPIKE
sector: industrials / defense / export framework / backlog / margin bridge
output_file: e2r_stock_web_v12_residual_round_R11_loop_86_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R10 loop 86`.

```text
scheduled_round = R11
scheduled_loop = 86
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```

R11 is the L1 policy/defense/infra linkage lane.  
C03 is selected because R11 loop85 used C02 power-grid/data-center CAPEX, while C03 still has no 4B/4C coverage in the No-Repeat Index:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
rows = 21
symbols = 12
good/bad Stage2 = 11/3
4B/4C = 0/0
top-covered = 079550, 047810, 065450, 005870, 103140, 003570
```

This loop avoids those top-covered symbols and also avoids the immediately previous R11 loop85 C02 symbols:

```text
267260, 010120, 103590
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"012450","company_name":"한화에어로스페이스","profile_path":"atlas/symbol_profiles/012/012450.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7730,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1996-01-03","1997-01-03","1999-04-08","1999-07-06","2009-02-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"010820","company_name":"퍼스텍","profile_path":"atlas/symbol_profiles/010/010820.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7694,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1999-11-05","2002-02-19","2003-07-16","2006-12-22"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"013810","company_name":"스페코","profile_path":"atlas/symbol_profiles/013/013810.json","first_date":"1997-11-03","last_date":"2026-02-20","trading_day_count":6731,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1999-12-28","2000-04-07","2006-10-24"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"012450","trigger_type":"Stage2-Actionable-DefenseExportFrameworkBacklogMarginBridge-Positive","entry_date":"2024-02-14","duplicate_status":"new C03 symbol/trigger/date combination outside top-covered and previous R11 loop85 C02 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"010820","trigger_type":"Stage2-FalsePositive-DefenseRobotTheme-NoExportFrameworkBacklogBridge","entry_date":"2024-01-17","duplicate_status":"new C03 symbol/trigger/date combination outside top-covered and previous R11 loop85 C02 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"013810","trigger_type":"Stage2-FalsePositive-GeopoliticalDefenseThemeSpike-NoExportBacklogMarginBridge","entry_date":"2024-01-18","duplicate_status":"new C03 symbol/trigger/date combination outside top-covered and previous R11 loop85 C02 symbols"}
```

## 4. Research question

C03 is not “defense stock moved on war news.”  
The useful defense signal is the export framework: signed framework or main contract, backlog visibility, delivery schedule, government-to-government channel quality, production slot scarcity, margin conversion, and cash collection. A geopolitical headline without this bridge is siren noise: loud, urgent, and often fading once the tape asks for purchase orders.

Residual question:

```text
Can C03 distinguish:
1. true defense export framework / backlog / margin bridge with very high MFE,
2. defense-robot theme spike without export framework backlog or delivery slot evidence,
3. small-cap geopolitical defense theme spike without export backlog and margin conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C03_R11L86_012450_HANWHA_AERO_DEFENSE_EXPORT_FRAMEWORK","symbol":"012450","company_name":"한화에어로스페이스","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-DefenseExportFrameworkBacklogMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_export_framework_backlog_bridge_required","price_source":"Songdaiki/stock-web","notes":"Defense export framework/backlog proxy produced very high MFE with tolerable MAE. Green still requires exact contract, delivery, margin and cash evidence."}
{"row_type":"case","case_id":"C03_R11L86_010820_FIRSTEC_DEFENSE_ROBOT_THEME","symbol":"010820","company_name":"퍼스텍","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_ROBOT_THEME_WITHOUT_EXPORT_FRAMEWORK_BACKLOG_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DefenseRobotTheme-NoExportFrameworkBacklogBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_medium_to_high_MAE","current_profile_verdict":"current_profile_false_positive_if_defense_robot_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Defense/robot theme spike had low MFE and eventually high MAE without export framework, delivery slot, backlog quality and margin bridge."}
{"row_type":"case","case_id":"C03_R11L86_013810_SPECOP_GEOPOLITICAL_DEFENSE_SPIKE","symbol":"013810","company_name":"스페코","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"GEOPOLITICAL_DEFENSE_THEME_SPIKE_WITHOUT_EXPORT_BACKLOG_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-GeopoliticalDefenseThemeSpike-NoExportBacklogMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_initial_blowoff_then_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_geopolitical_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Geopolitical defense spike peaked immediately and then drew down deeply when export backlog and margin conversion did not confirm."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 012450 한화에어로스페이스 — defense export framework/backlog bridge positive

Entry row: `2024-02-14 c=146300`.  
Observed path: same-day low `134100`, 30D high `2024-03-27 h=225000`, 90D high `2024-06-19 h=256000`, and full-window high `2024-11-12 h=425000`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L86_C03_012450_20240214_STAGE2_DEFENSE_EXPORT_FRAMEWORK","case_id":"C03_R11L86_012450_HANWHA_AERO_DEFENSE_EXPORT_FRAMEWORK","symbol":"012450","company_name":"한화에어로스페이스","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-DefenseExportFrameworkBacklogMarginBridge-Positive","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":146300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_defense_export_framework_backlog_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; defense export framework, delivery schedule and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["export_framework_proxy","backlog_visibility_proxy","delivery_schedule_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_contract_source_pending","production_slot_bridge_pending","margin_bridge_pending","cash_collection_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv","profile_path":"atlas/symbol_profiles/012/012450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":53.79,"MFE_90D_pct":74.98,"MFE_180D_pct":190.50,"MAE_30D_pct":-8.34,"MAE_90D_pct":-8.34,"MAE_180D_pct":-8.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":425000.0,"max_drawdown_low_date":"2024-02-14","max_drawdown_low":134100.0,"drawdown_after_peak_pct":-36.47,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_export_framework_backlog_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"012450_2024-02-14_146300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C03 can allow Stage2/Yellow when defense strength is tied to export framework, backlog visibility, delivery schedule and margin bridge. Green still requires exact contract and margin/cash evidence."}
```

### 6.2 010820 퍼스텍 — defense/robot theme without export framework backlog bridge

Entry row: `2024-01-17 c=3765`.  
Observed path: same-day high `3990`, 30D/90D low around `3165`, and later 180D low around `2795`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L86_C03_010820_20240117_STAGE2_FALSE_POSITIVE_DEFENSE_ROBOT_THEME","case_id":"C03_R11L86_010820_FIRSTEC_DEFENSE_ROBOT_THEME","symbol":"010820","company_name":"퍼스텍","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_ROBOT_THEME_WITHOUT_EXPORT_FRAMEWORK_BACKLOG_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-DefenseRobotTheme-NoExportFrameworkBacklogBridge","trigger_date":"2024-01-17","entry_date":"2024-01-17","entry_price":3765.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_defense_robot_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; defense/robot theme treated as insufficient without export framework, delivery slot, backlog quality and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["defense_robot_theme","geopolitical_relative_strength"],"stage3_evidence_fields":["export_framework_bridge_missing","delivery_slot_bridge_missing","backlog_quality_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","export_backlog_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010820/2024.csv","profile_path":"atlas/symbol_profiles/010/010820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.98,"MFE_90D_pct":5.98,"MFE_180D_pct":5.98,"MAE_30D_pct":-15.94,"MAE_90D_pct":-15.94,"MAE_180D_pct":-25.76,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-17","peak_price":3990.0,"max_drawdown_low_date":"2024-10-10","max_drawdown_low":2795.0,"drawdown_after_peak_pct":-29.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"defense_robot_theme_without_export_framework_backlog_bridge_should_be_watch_not_positive","four_b_evidence_type":["price_only","export_backlog_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_medium_to_high_MAE","current_profile_verdict":"current_profile_false_positive_if_defense_robot_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"010820_2024-01-17_3765","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C03 should not treat defense/robot theme strength as export framework backlog evidence. Low MFE and later MAE require Watch/4B-style evidence repair."}
```

### 6.3 013810 스페코 — geopolitical defense spike without export backlog/margin bridge

Entry row: `2024-01-18 c=5090`.  
Observed path: same-day high `5950`, lows reached `3705` by `2024-01-31`, `3645` by `2024-04-01`, and `2955` by `2024-07-12`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L86_C03_013810_20240118_STAGE2_FALSE_POSITIVE_GEOPOLITICAL_DEFENSE_SPIKE","case_id":"C03_R11L86_013810_SPECOP_GEOPOLITICAL_DEFENSE_SPIKE","symbol":"013810","company_name":"스페코","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"GEOPOLITICAL_DEFENSE_THEME_SPIKE_WITHOUT_EXPORT_BACKLOG_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-GeopoliticalDefenseThemeSpike-NoExportBacklogMarginBridge","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":5090.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_geopolitical_defense_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; geopolitical defense theme spike treated as insufficient without export backlog, framework contract, delivery schedule and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["geopolitical_defense_theme","relative_strength_blowoff"],"stage3_evidence_fields":["export_framework_bridge_missing","backlog_visibility_missing","delivery_schedule_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","geopolitical_theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013810/2024.csv","profile_path":"atlas/symbol_profiles/013/013810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.90,"MFE_90D_pct":16.90,"MFE_180D_pct":16.90,"MAE_30D_pct":-27.21,"MAE_90D_pct":-28.39,"MAE_180D_pct":-41.94,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-18","peak_price":5950.0,"max_drawdown_low_date":"2024-07-12","max_drawdown_low":2955.0,"drawdown_after_peak_pct":-50.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"geopolitical_defense_blowoff_without_export_backlog_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","geopolitical_theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_initial_blowoff_then_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_geopolitical_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"013810_2024-01-18_5090","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C03 should route geopolitical defense blowoff to 4B-watch unless export backlog, contract framework, delivery schedule and margin bridge are verified. Initial MFE is not enough when MAE opens deeply."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C03_R11L86_012450_HANWHA_AERO_DEFENSE_EXPORT_FRAMEWORK","trigger_id":"R11L86_C03_012450_20240214_STAGE2_DEFENSE_EXPORT_FRAMEWORK","symbol":"012450","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C03 requires export framework/backlog/margin bridge rather than defense headline alone","raw_component_scores_before":{"export_framework_score":16,"backlog_visibility_score":15,"delivery_schedule_score":13,"government_channel_quality":12,"production_slot_scarcity":12,"margin_bridge_score":10,"relative_strength_score":14,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":79,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"export_framework_score":19,"backlog_visibility_score":18,"delivery_schedule_score":16,"government_channel_quality":14,"production_slot_scarcity":14,"margin_bridge_score":12,"relative_strength_score":15,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":89,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Export framework/backlog and huge MFE support Yellow/Green-candidate watch, but exact contract and margin/cash evidence still block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C03_R11L86_010820_FIRSTEC_DEFENSE_ROBOT_THEME","trigger_id":"R11L86_C03_010820_20240117_STAGE2_FALSE_POSITIVE_DEFENSE_ROBOT_THEME","symbol":"010820","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_scope":"current_default_proxy","profile_hypothesis":"defense/robot theme without export framework should be blocked from Yellow/Green","raw_component_scores_before":{"export_framework_score":2,"backlog_visibility_score":1,"delivery_schedule_score":1,"government_channel_quality":1,"production_slot_scarcity":1,"margin_bridge_score":0,"relative_strength_score":11,"valuation_repricing_score":5,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_framework_score":0,"backlog_visibility_score":0,"delivery_schedule_score":0,"government_channel_quality":0,"production_slot_scarcity":0,"margin_bridge_score":0,"relative_strength_score":4,"valuation_repricing_score":1,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Watch-4B","component_delta_explanation":"Low MFE and missing export framework/backlog bridge block Stage2-Actionable/Yellow."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C03_R11L86_013810_SPECOP_GEOPOLITICAL_DEFENSE_SPIKE","trigger_id":"R11L86_C03_013810_20240118_STAGE2_FALSE_POSITIVE_GEOPOLITICAL_DEFENSE_SPIKE","symbol":"013810","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_scope":"current_default_proxy","profile_hypothesis":"geopolitical defense spike without export backlog/margin bridge should be 4B-watch","raw_component_scores_before":{"export_framework_score":1,"backlog_visibility_score":0,"delivery_schedule_score":0,"government_channel_quality":1,"production_slot_scarcity":0,"margin_bridge_score":0,"relative_strength_score":15,"valuation_repricing_score":6,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_framework_score":0,"backlog_visibility_score":0,"delivery_schedule_score":0,"government_channel_quality":0,"production_slot_scarcity":0,"margin_bridge_score":0,"relative_strength_score":4,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Initial blowoff MFE is outweighed by missing bridge and deep MAE; route to 4B-watch/evidence repair."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R11L86_C03_P0_CURRENT","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C03 needs explicit export framework/backlog/delivery/margin bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":32.62,"avg_MAE90_pct":-17.56,"avg_MFE180_pct":71.13,"avg_MAE180_pct":-25.35,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C03_export_backlog_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R11L86_C03_P1_SECTOR_SPECIFIC","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P1_L1_defense_export_framework_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 defense signals need export framework, backlog visibility, delivery schedule, government channel, production slot or margin bridge before Stage2-Actionable","changed_axes":["export_framework_required","backlog_delivery_required","geopolitical_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_export_framework_backlog_delivery_channel_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":32.62,"avg_MAE90_pct":-17.56,"avg_MFE180_pct":71.13,"avg_MAE180_pct":-25.35,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R11L86_C03_P2_CANONICAL","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P2_C03_export_backlog_margin_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C03 should reward export framework/backlog mechanics, not geopolitical defense beta","changed_axes":["C03_export_framework_backlog_bridge_required","C03_geopolitical_theme_local_4B_guard","C03_margin_delivery_bridge_required"],"changed_thresholds":{"stage2_yellow_gate":"export_framework_backlog_or_delivery_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":32.62,"avg_MAE90_pct":-17.56,"avg_MFE180_pct":71.13,"avg_MAE180_pct":-25.35,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R11L86_C03_P3_COUNTEREXAMPLE_GUARD","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P3_C03_high_MAE_theme_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If export/backlog bridge is missing and MAE90<=-20 or MAE180<=-25, block Yellow/Green even when MFE exists","changed_axes":["C03_high_MAE_guardrail","C03_price_only_theme_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MAE90_le_minus_20_or_MAE180_le_minus_25)"},"eligible_trigger_count":3,"avg_MFE90_pct":32.62,"avg_MAE90_pct":-17.56,"avg_MFE180_pct":71.13,"avg_MAE180_pct":-25.35,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_EXPORT_FRAMEWORK_BACKLOG_VS_DEFENSE_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":32.62,"avg_MAE90_pct":-17.56,"avg_MFE180_pct":71.13,"avg_MAE180_pct":-25.35,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_bridge_missing_and_MAE90_le_minus20_or_MAE180_le_minus25":0.67,"interpretation":"C03 needs bridge discipline. 한화에어로스페이스 shows export-framework/backlog bridge can rerate massively, while 퍼스텍 and 스페코 show defense/geopolitical theme spikes should not be promoted without export backlog, delivery, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"012450","trigger_type":"Stage2-Actionable-DefenseExportFrameworkBacklogMarginBridge-Positive","entry_date":"2024-02-14","stage2_to_90D_outcome":"good_stage2_very_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_defense_export_framework_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when export framework, backlog and delivery bridge exists; Green requires exact contract, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"010820","trigger_type":"Stage2-FalsePositive-DefenseRobotTheme-NoExportFrameworkBacklogBridge","entry_date":"2024-01-17","stage2_to_90D_outcome":"weak_stage2_low_MFE_medium_MAE","stage2_to_180D_outcome":"failed_theme_high_180D_MAE","MFE90_ge_20":false,"MAE180_le_minus_25":true,"transition_note":"Defense/robot theme without export framework/backlog bridge should remain Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"013810","trigger_type":"Stage2-FalsePositive-GeopoliticalDefenseThemeSpike-NoExportBacklogMarginBridge","entry_date":"2024-01-18","stage2_to_90D_outcome":"bad_stage2_initial_blowoff_deep_MAE","stage2_to_180D_outcome":"failed_geopolitical_defense_spike","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Geopolitical defense blowoff without export backlog/margin bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","residual_type":"defense_theme_overcredit_without_export_framework_backlog_delivery_margin_bridge","contribution":"Adds two C03 local 4B/watch counterexamples against one defense export-framework positive, avoiding C03 top-covered symbols and previous R11 loop85 C02 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE_VS_GEOPOLITICAL_DEFENSE_THEME_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C03 now has non-top-symbol defense/geopolitical theme counterexamples; next R11 loops should exact-URL repair export framework, framework-to-main-contract conversion, delivery schedule, production slot, margin and cash-collection evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"C03_export_framework_backlog_delivery_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"012450 worked with export-framework/backlog proxy; 010820 and 013810 failed or drew down when only defense/geopolitical theme strength existed."}
{"row_type":"shadow_weight","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"C03_geopolitical_defense_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Defense/geopolitical theme spikes showed low or unstable MFE and medium-to-deep MAE without non-price export backlog bridge."}
{"row_type":"shadow_weight","round":"R11","loop":"86","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"C03_high_MAE_theme_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If export/backlog bridge is missing and MAE90<=-20 or MAE180<=-25, block Stage2-Actionable/Yellow and route to Watch/4B-risk even if same-day MFE exists."}
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
  - geopolitical_defense_theme_overcredit
  - defense_robot_theme_no_export_framework_bridge
  - export_backlog_delivery_bridge_missing
  - price_only_defense_theme_local_4B
new_axis_proposed:
  - C03_export_framework_backlog_delivery_bridge_required_shadow_only
  - C03_geopolitical_defense_theme_local_4B_watch_guard_shadow_only
  - C03_high_MAE_theme_guardrail_shadow_only
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
3. Confirm R11 / L1 / C03 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C03 top-covered symbols
   - previous R11 loop85 C02 symbols listed in the MD
6. If aggregate support remains stable after exact evidence URL repair, consider C03-scoped safe patch candidates:
   - C03_export_framework_backlog_delivery_bridge_required
   - C03_geopolitical_defense_theme_local_4B_watch_guard
   - C03_high_MAE_theme_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R11
completed_loop = 86
next_round = R12
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R11/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.
```
