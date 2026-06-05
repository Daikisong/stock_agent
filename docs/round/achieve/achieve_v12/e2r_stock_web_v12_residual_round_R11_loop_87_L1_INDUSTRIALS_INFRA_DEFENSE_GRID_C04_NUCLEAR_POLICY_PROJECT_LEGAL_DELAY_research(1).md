# E2R Stock-Web v12 Residual Research — R11 Loop 87 / L1 / C04

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R11
loop: 87
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_O_AND_M_PROJECT_BRIDGE_VS_POLICY_THEME_AND_LEGAL_DELAY_BLOWOFF
sector: industrials / infra / nuclear policy / project backlog / legal-delay risk
output_file: e2r_stock_web_v12_residual_round_R11_loop_87_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R10 loop 87`.

```text
scheduled_round = R11
scheduled_loop = 87
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```

R11 is the L1 policy / defense / infra linkage lane.  
C04 is selected because the previous R11 loops used C02 power-grid/data-center CAPEX and C03 defense export framework, while C04 still has relatively small coverage and only one 4B row.

The No-Repeat Index shows C04 as:

```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
rows = 12
symbols = 7
good/bad Stage2 = 5/3
4B/4C = 1/0
top-covered = 011700, 083650, 006910, 034020, 042370, 046120
```

This loop avoids those top-covered symbols and also avoids the immediately previous R11 loop symbols:

```text
R11 loop85 C02: 267260, 010120, 103590
R11 loop86 C03: 012450, 010820, 013810
```

Selected symbols:

```text
051600, 032820, 094820
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"051600","company_name":"한전KPS","profile_path":"atlas/symbol_profiles/051/051600.json","first_date":"2007-12-14","last_date":"2026-02-20","trading_day_count":4482,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"032820","company_name":"우리기술","profile_path":"atlas/symbol_profiles/032/032820.json","first_date":"2000-06-22","last_date":"2026-02-20","trading_day_count":6295,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["2003-10-28","2005-06-07","2007-07-03","2007-07-31","2009-07-29"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"094820","company_name":"일진파워","profile_path":"atlas/symbol_profiles/094/094820.json","first_date":"2007-11-06","last_date":"2026-02-20","trading_day_count":4483,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2011-09-08","2011-09-30"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"051600","trigger_type":"Stage2-Actionable-NuclearOMProjectServiceBacklogBridge-Positive","entry_date":"2024-07-12","duplicate_status":"new C04 symbol/trigger/date combination outside top-covered and previous R11 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"032820","trigger_type":"Stage2-FalsePositive-NuclearControlSystemThemeBlowoff-NoProjectLegalBridge","entry_date":"2024-07-18","duplicate_status":"new C04 symbol/trigger/date combination outside top-covered and previous R11 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"094820","trigger_type":"Stage2-FalsePositive-NuclearMaintenanceTheme-NoConfirmedProjectMarginBridge","entry_date":"2024-03-18","duplicate_status":"new C04 symbol/trigger/date combination outside top-covered and previous R11 loop symbols"}
```

## 4. Research question

C04 is not “nuclear theme went up.”  
The useful nuclear signal must cross the bridge from policy to project: project visibility, legal-delay containment, contract scope, O&M or EPC role clarity, regulated customer quality, schedule certainty, margin/cash conversion, and financing or licensing risk control. A nuclear headline without that bridge is like a reactor dome before fuel loading: visually powerful, but not yet producing power.

Residual question:

```text
Can C04 distinguish:
1. nuclear O&M / project-service / backlog bridge with good MFE and low MAE,
2. nuclear control-system policy-theme blowoff without project/legal/margin bridge,
3. nuclear maintenance theme where an initial price spike lacks confirmed project scope and margin conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C04_R11L87_051600_KEPCO_KPS_NUCLEAR_OM_PROJECT_BRIDGE","symbol":"051600","company_name":"한전KPS","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_O_AND_M_PROJECT_SERVICE_BACKLOG_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-NuclearOMProjectServiceBacklogBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct_if_project_service_backlog_bridge_required","price_source":"Songdaiki/stock-web","notes":"Nuclear O&M/project-service proxy produced strong MFE with low MAE. Green still requires exact project, scope, legal-delay and margin evidence."}
{"row_type":"case","case_id":"C04_R11L87_032820_WOORITECH_NUCLEAR_CONTROL_THEME_BLOWOFF","symbol":"032820","company_name":"우리기술","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_CONTROL_SYSTEM_THEME_BLOWOFF_WITHOUT_PROJECT_LEGAL_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-NuclearControlSystemThemeBlowoff-NoProjectLegalBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_only_blowoff_high_MFE_but_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_price_only_nuclear_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Control-system/nuclear theme blowoff had same-day MFE, but the path then suffered deep MAE without project/legal/margin bridge. This is classic 4B price-only extension."}
{"row_type":"case","case_id":"C04_R11L87_094820_ILJIN_NUCLEAR_MAINTENANCE_THEME","symbol":"094820","company_name":"일진파워","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_MAINTENANCE_THEME_WITHOUT_CONFIRMED_PROJECT_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-NuclearMaintenanceTheme-NoConfirmedProjectMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub_Yellow_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_maintenance_theme_promoted_without_confirmed_project_scope","price_source":"Songdaiki/stock-web","notes":"Nuclear maintenance theme had MFE below robust Yellow threshold and later deep MAE when project scope, legal-delay resolution and margin bridge did not confirm."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 051600 한전KPS — nuclear O&M/project-service backlog bridge positive

Entry row: `2024-07-12 c=37650`.  
Observed path: early low `2024-08-05 l=35850`, 90D high `2024-11-27 h=48250`, and full-window high `2024-12-03 h=49100`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L87_C04_051600_20240712_STAGE2_NUCLEAR_OM_PROJECT","case_id":"C04_R11L87_051600_KEPCO_KPS_NUCLEAR_OM_PROJECT_BRIDGE","symbol":"051600","company_name":"한전KPS","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_O_AND_M_PROJECT_SERVICE_BACKLOG_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-NuclearOMProjectServiceBacklogBridge-Positive","trigger_date":"2024-07-12","entry_date":"2024-07-12","entry_price":37650.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_nuclear_OandM_project_service_backlog_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; nuclear O&M/service backlog and policy-to-project bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["nuclear_policy_project_proxy","OandM_backlog_proxy","regulated_customer_quality_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_project_scope_pending","legal_delay_resolution_pending","margin_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_only_extension_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv","profile_path":"atlas/symbol_profiles/051/051600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.03,"MFE_90D_pct":28.15,"MFE_180D_pct":30.41,"MAE_30D_pct":-4.78,"MAE_90D_pct":-4.78,"MAE_180D_pct":-4.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":49100.0,"max_drawdown_low_date":"2024-08-05","max_drawdown_low":35850.0,"drawdown_after_peak_pct":-17.92,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_project_scope_legal_and_margin_evidence","four_b_evidence_type":["price_only_extension_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct_if_project_service_backlog_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"051600_2024-07-12_37650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C04 can allow Stage2/Yellow when nuclear policy is tied to service backlog, project scope, legal-delay control and margin bridge. Green still requires exact source-grade evidence."}
```

### 6.2 032820 우리기술 — nuclear control-system theme blowoff without project/legal bridge

Entry row: `2024-07-18 c=2700`.  
Observed path: same-day high `3300`, then lows `2024-10-14 l=2150`, `2024-12-09 l=1650`, and `2024-12-30 l=1621`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L87_C04_032820_20240718_STAGE2_FALSE_POSITIVE_NUCLEAR_CONTROL_BLOWOFF","case_id":"C04_R11L87_032820_WOORITECH_NUCLEAR_CONTROL_THEME_BLOWOFF","symbol":"032820","company_name":"우리기술","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_CONTROL_SYSTEM_THEME_BLOWOFF_WITHOUT_PROJECT_LEGAL_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-NuclearControlSystemThemeBlowoff-NoProjectLegalBridge","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":2700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_nuclear_control_system_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; nuclear control-system theme treated as insufficient without confirmed project scope, legal delay containment, customer order and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["nuclear_control_system_theme","relative_strength_blowoff"],"stage3_evidence_fields":["project_scope_bridge_missing","legal_delay_resolution_missing","customer_order_bridge_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","project_legal_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv","profile_path":"atlas/symbol_profiles/032/032820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.22,"MFE_90D_pct":22.22,"MFE_180D_pct":22.22,"MAE_30D_pct":-11.48,"MAE_90D_pct":-20.56,"MAE_180D_pct":-39.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":3300.0,"max_drawdown_low_date":"2024-12-30","max_drawdown_low":1621.0,"drawdown_after_peak_pct":-50.88,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_nuclear_control_blowoff_without_project_legal_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","project_legal_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_only_blowoff_high_MFE_but_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_price_only_nuclear_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"032820_2024-07-18_2700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C04 should not promote same-day nuclear theme blowoff to Yellow/Green unless project, legal-delay, customer order and margin bridge are verified. MFE alone is not enough when MAE opens deeply."}
```

### 6.3 094820 일진파워 — nuclear maintenance theme without confirmed project/margin bridge

Entry row: `2024-03-18 c=13000`.  
Observed path: high `2024-05-29 h=15200`, then lows `2024-10-11 l=8940`, `2024-12-09 l=6900`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L87_C04_094820_20240318_STAGE2_FALSE_POSITIVE_NUCLEAR_MAINTENANCE_THEME","case_id":"C04_R11L87_094820_ILJIN_NUCLEAR_MAINTENANCE_THEME","symbol":"094820","company_name":"일진파워","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_MAINTENANCE_THEME_WITHOUT_CONFIRMED_PROJECT_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-NuclearMaintenanceTheme-NoConfirmedProjectMarginBridge","trigger_date":"2024-03-18","entry_date":"2024-03-18","entry_price":13000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_nuclear_maintenance_policy_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; nuclear maintenance theme treated as insufficient without confirmed project scope, legal-delay resolution, backlog quality and margin/cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["nuclear_maintenance_theme","policy_project_keyword","relative_strength_rebound"],"stage3_evidence_fields":["confirmed_project_scope_missing","legal_delay_resolution_missing","margin_cash_bridge_missing","customer_quality_missing"],"stage4b_evidence_fields":["price_only_local_extension","project_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/094/094820/2024.csv","profile_path":"atlas/symbol_profiles/094/094820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.92,"MFE_90D_pct":16.92,"MFE_180D_pct":16.92,"MAE_30D_pct":-14.92,"MAE_90D_pct":-14.92,"MAE_180D_pct":-46.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-29","peak_price":15200.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":6900.0,"drawdown_after_peak_pct":-54.61,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"nuclear_maintenance_theme_without_confirmed_project_margin_bridge_should_remain_watch_4B_not_Yellow","four_b_evidence_type":["price_only","project_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_maintenance_theme_promoted_without_confirmed_project_scope","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"094820_2024-03-18_13000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C04 should keep nuclear maintenance themes in Watch unless confirmed project scope, legal-delay resolution, customer quality and margin/cash bridge are exact-evidence repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C04_R11L87_051600_KEPCO_KPS_NUCLEAR_OM_PROJECT_BRIDGE","trigger_id":"R11L87_C04_051600_20240712_STAGE2_NUCLEAR_OM_PROJECT","symbol":"051600","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C04 requires policy-to-project, legal-delay and margin bridge rather than nuclear theme alone","raw_component_scores_before":{"policy_project_score":12,"project_scope_score":11,"legal_delay_control_score":10,"customer_quality_score":11,"service_backlog_score":12,"margin_cash_bridge_score":8,"relative_strength_score":11,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":70,"stage_label_before":"Stage2-Watch/Yellow-candidate","raw_component_scores_after":{"policy_project_score":15,"project_scope_score":14,"legal_delay_control_score":13,"customer_quality_score":13,"service_backlog_score":15,"margin_cash_bridge_score":10,"relative_strength_score":12,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"O&M/project-service bridge and low MAE support Yellow-watch; exact project/legal/margin evidence still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C04_R11L87_032820_WOORITECH_NUCLEAR_CONTROL_THEME_BLOWOFF","trigger_id":"R11L87_C04_032820_20240718_STAGE2_FALSE_POSITIVE_NUCLEAR_CONTROL_BLOWOFF","symbol":"032820","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_scope":"current_default_proxy","profile_hypothesis":"nuclear control-system blowoff without project/legal bridge should be 4B-watch","raw_component_scores_before":{"policy_project_score":7,"project_scope_score":1,"legal_delay_control_score":0,"customer_quality_score":2,"service_backlog_score":1,"margin_cash_bridge_score":0,"relative_strength_score":15,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"policy_project_score":1,"project_scope_score":0,"legal_delay_control_score":0,"customer_quality_score":0,"service_backlog_score":0,"margin_cash_bridge_score":0,"relative_strength_score":4,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Price-only MFE is outweighed by missing project/legal bridge and deep MAE."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C04_R11L87_094820_ILJIN_NUCLEAR_MAINTENANCE_THEME","trigger_id":"R11L87_C04_094820_20240318_STAGE2_FALSE_POSITIVE_NUCLEAR_MAINTENANCE_THEME","symbol":"094820","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_scope":"current_default_proxy","profile_hypothesis":"nuclear maintenance theme without confirmed project/margin bridge should remain Watch/blocked","raw_component_scores_before":{"policy_project_score":6,"project_scope_score":2,"legal_delay_control_score":1,"customer_quality_score":2,"service_backlog_score":2,"margin_cash_bridge_score":1,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":8,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"policy_project_score":1,"project_scope_score":0,"legal_delay_control_score":0,"customer_quality_score":0,"service_backlog_score":0,"margin_cash_bridge_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-20,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Watch-Blocked","component_delta_explanation":"MFE below strong Yellow threshold and deep 180D MAE require confirmed project/margin bridge before promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R11L87_C04_P0_CURRENT","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C04 needs explicit project scope, legal-delay control, customer quality, service backlog, margin and cash bridge gates","eligible_trigger_count":3,"avg_MFE90_pct":22.43,"avg_MAE90_pct":-13.42,"avg_MFE180_pct":23.18,"avg_MAE180_pct":-30.55,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C04_project_legal_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R11L87_C04_P1_SECTOR_SPECIFIC","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P1_L1_nuclear_project_legal_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 nuclear signals need project scope, legal-delay resolution, regulated customer quality, backlog or margin/cash bridge before Stage2-Actionable","changed_axes":["project_scope_required","legal_delay_control_required","nuclear_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_project_scope_legal_delay_customer_backlog_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":22.43,"avg_MAE90_pct":-13.42,"avg_MFE180_pct":23.18,"avg_MAE180_pct":-30.55,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R11L87_C04_P2_CANONICAL","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P2_C04_project_legal_margin_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C04 should reward policy-to-project conversion, not nuclear theme or control-system blowoff labels","changed_axes":["C04_project_legal_margin_bridge_required","C04_price_only_nuclear_theme_local_4B_guard","C04_confirmed_scope_required_for_Yellow"],"changed_thresholds":{"stage2_yellow_gate":"project_scope_or_backlog_plus_legal_delay_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":22.43,"avg_MAE90_pct":-13.42,"avg_MFE180_pct":23.18,"avg_MAE180_pct":-30.55,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R11L87_C04_P3_COUNTEREXAMPLE_GUARD","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P3_C04_price_only_blowoff_and_180D_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If project/legal bridge is missing and MAE180<=-35, route to 4B-watch even when same-day MFE exists","changed_axes":["C04_price_only_blowoff_guardrail","C04_deep_180D_MAE_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_MAE180_le_minus_35"},"eligible_trigger_count":3,"avg_MFE90_pct":22.43,"avg_MAE90_pct":-13.42,"avg_MFE180_pct":23.18,"avg_MAE180_pct":-30.55,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_NUCLEAR_PROJECT_BRIDGE_VS_THEME_BLOWOFF","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":22.43,"avg_MAE90_pct":-13.42,"avg_MFE180_pct":23.18,"avg_MAE180_pct":-30.55,"stage2_hit_rate_MFE90_ge_20":0.67,"stage2_bad_entry_rate_bridge_missing_MAE180_le_minus_35":0.67,"interpretation":"C04 needs bridge discipline. 한전KPS shows nuclear O&M/project-service bridge can support Yellow-watch, while 우리기술 and 일진파워 show nuclear policy/theme strength should not become Yellow/Green without project scope, legal-delay, customer and margin/cash evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"051600","trigger_type":"Stage2-Actionable-NuclearOMProjectServiceBacklogBridge-Positive","entry_date":"2024-07-12","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_nuclear_OM_project_bridge","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when nuclear policy is tied to project/service backlog and legal/margin bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"032820","trigger_type":"Stage2-FalsePositive-NuclearControlSystemThemeBlowoff-NoProjectLegalBridge","entry_date":"2024-07-18","stage2_to_90D_outcome":"price_only_blowoff_high_MFE_but_MAE90_hit","stage2_to_180D_outcome":"failed_nuclear_theme_deep_180D_MAE","MFE90_ge_20":true,"MAE180_le_minus_35":true,"transition_note":"Same-day nuclear theme MFE should not validate the row when project/legal/margin bridge is missing and 180D MAE opens deeply."}
{"row_type":"stage_transition_summary","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"094820","trigger_type":"Stage2-FalsePositive-NuclearMaintenanceTheme-NoConfirmedProjectMarginBridge","entry_date":"2024-03-18","stage2_to_90D_outcome":"weak_stage2_sub_Yellow_MFE","stage2_to_180D_outcome":"failed_maintenance_theme_deep_MAE","MFE90_ge_20":false,"MAE180_le_minus_35":true,"transition_note":"Nuclear maintenance theme without confirmed project/margin bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","residual_type":"nuclear_policy_theme_overcredit_without_project_legal_margin_bridge","contribution":"Adds two C04 4B/deep-MAE counterexamples against one nuclear O&M/project-service positive, avoiding C04 top-covered symbols and previous R11 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_O_AND_M_PROJECT_BRIDGE_VS_POLICY_THEME_AND_LEGAL_DELAY_BLOWOFF","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C04 now has a non-top-symbol O&M project-service control and two nuclear theme/price-only blowoff counterexamples; next R11 loops should exact-URL repair project scope, legal-delay resolution, regulated customer, margin and cash evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"C04_project_legal_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"051600 worked with project/O&M bridge proxy; 032820 and 094820 failed when nuclear theme lacked confirmed project scope, legal-delay control and margin bridge."}
{"row_type":"shadow_weight","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"C04_price_only_nuclear_theme_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Nuclear theme rows had price-only or sub-Yellow MFE and deep 180D MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R11","loop":"87","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"C04_deep_180D_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If project/legal bridge is missing and MAE180<=-35, route to Watch/4B-risk even if same-day MFE exists."}
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
  - nuclear_policy_theme_overcredit
  - project_scope_bridge_missing
  - legal_delay_resolution_missing
  - price_only_nuclear_theme_blowoff
new_axis_proposed:
  - C04_project_legal_margin_bridge_required_shadow_only
  - C04_price_only_nuclear_theme_local_4B_guard_shadow_only
  - C04_deep_180D_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C04
  - full_4b_requires_non_price_evidence within C04
  - hard_4c_thesis_break_routes_to_4c within C04
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
3. Confirm R11 / L1 / C04 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C04 top-covered symbols
   - previous R11 loop85 C02 symbols
   - previous R11 loop86 C03 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C04-scoped safe patch candidates:
   - C04_project_legal_margin_bridge_required
   - C04_price_only_nuclear_theme_local_4B_guard
   - C04_deep_180D_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R11
completed_loop = 87
next_round = R12
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R11/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.
```
