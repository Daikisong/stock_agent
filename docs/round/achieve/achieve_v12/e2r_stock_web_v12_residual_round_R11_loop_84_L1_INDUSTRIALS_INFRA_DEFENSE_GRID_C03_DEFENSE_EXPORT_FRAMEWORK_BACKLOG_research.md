# E2R Stock-Web v12 Residual Research — R11 Loop 84 / L1 / C03

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R11
loop: 84
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_SPACE_AEROSPACE_THEME_SPIKE
sector: industrials / defense / aerospace / policy-defense linkage
output_file: e2r_stock_web_v12_residual_round_R11_loop_84_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R10 loop 84`.

```text
scheduled_round = R11
scheduled_loop = 84
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```

R11 may use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or `L1_INDUSTRIALS_INFRA_DEFENSE_GRID` when the lane is policy-defense linkage.  
This run deliberately selects the L1 defense-export lane because C03 has thin 4B/4C coverage and still needs a sharper split between true export-framework backlog and aerospace/space/defense theme spikes.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"012450","company_name":"한화에어로스페이스","profile_path":"atlas/symbol_profiles/012/012450.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7730,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1996-01-03","1997-01-03","1999-04-08","1999-07-06","2009-02-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"274090","company_name":"켄코아에어로스페이스","profile_path":"atlas/symbol_profiles/274/274090.json","first_date":"2020-03-03","last_date":"2026-02-20","trading_day_count":1465,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2021-03-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"099320","company_name":"쎄트렉아이","profile_path":"atlas/symbol_profiles/099/099320.json","first_date":"2008-06-13","last_date":"2026-02-20","trading_day_count":4364,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["2008-06-27","2019-02-13","2019-03-07","2021-05-11","2024-01-08"],"has_major_raw_discontinuity":true,"calibration_caveat":"Entry is deliberately placed after the 2024-01-08 corporate-action candidate; forward window is treated as clean for selected entry.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"post_2024-01-08_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

The No-Repeat Index is used only as a duplicate-avoidance ledger.  
For C03, the top-covered symbols are:

```text
079550, 047810, 065450, 005870, 103140, 003570
```

This loop avoids that repeated set and introduces three different C03 symbols.  
Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"012450","trigger_type":"Stage2-Actionable-DefensePrimeExportFrameworkBacklogBridge-Positive","entry_date":"2024-02-26","duplicate_status":"new C03 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"274090","trigger_type":"Stage2-FalsePositive-AerospaceThemeSpike-NoFrameworkBacklogBridge","entry_date":"2024-01-18","duplicate_status":"new C03 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"099320","trigger_type":"Stage2-FalsePositive-SpaceDefenseThemeExtension-NoExportFrameworkBridge","entry_date":"2024-07-01","duplicate_status":"new C03 symbol/trigger/date combination outside top-covered list and after 2024-01-08 corporate-action candidate"}
```

## 4. Research question

C03 is not “defense theme went up.”  
It is the bridge test between a defense/policy headline and a real industrial backlog engine: export framework, sovereign customer quality, option exercise, production capacity, margin, and cash conversion.

Residual question:

```text
Can C03 distinguish:
1. defense-prime export framework backlog that reprices structurally,
2. aerospace supply-chain theme spike without sovereign/framework backlog bridge,
3. space-defense theme extension without export framework and production/margin bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C03_R11L84_012450_HANWHA_AERO_EXPORT_FRAMEWORK_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_PRIME_EXPORT_FRAMEWORK_BACKLOG_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-DefensePrimeExportFrameworkBacklogBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_export_framework_backlog_bridge_required","price_source":"Songdaiki/stock-web","notes":"Defense-prime export framework/backlog bridge produced a very large MFE with tolerable initial MAE. Supports Stage2/Yellow and later rerating, but Green still requires source-quality framework/order/margin evidence."}
{"row_type":"case","case_id":"C03_R11L84_274090_KENCOA_AEROSPACE_THEME_SPIKE","symbol":"274090","company_name":"켄코아에어로스페이스","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"AEROSPACE_SUPPLY_CHAIN_THEME_SPIKE_WITHOUT_FRAMEWORK_BACKLOG","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AerospaceThemeSpike-NoFrameworkBacklogBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_aerospace_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Aerospace/defense supply-chain theme spike had shallow MFE and deep drawdown without framework backlog, sovereign customer and margin bridge."}
{"row_type":"case","case_id":"C03_R11L84_099320_SATREC_SPACE_DEFENSE_THEME_EXTENSION","symbol":"099320","company_name":"쎄트렉아이","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"SPACE_DEFENSE_THEME_EXTENSION_WITHOUT_EXPORT_FRAMEWORK_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SpaceDefenseThemeExtension-NoExportFrameworkBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_space_defense_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Space-defense theme extension peaked locally, then produced high MAE when export framework, production capacity and margin bridge were missing."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 012450 한화에어로스페이스 — defense-prime export framework backlog bridge

Entry row: `2024-02-26 c=166200`.  
Forward path: `2024-04-02 h=245000`, `2024-06-19 h=256000`, and `2024-11-12 h=425000`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L84_C03_012450_20240226_STAGE2_DEFENSE_PRIME_EXPORT_BACKLOG","case_id":"C03_R11L84_012450_HANWHA_AERO_EXPORT_FRAMEWORK_BACKLOG","symbol":"012450","company_name":"한화에어로스페이스","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_PRIME_EXPORT_FRAMEWORK_BACKLOG_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-DefensePrimeExportFrameworkBacklogBridge-Positive","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":166200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_defense_export_framework_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; export framework/backlog and sovereign customer bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_disclosure_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["export_framework_proxy","sovereign_customer_quality_proxy","backlog_visibility_proxy","relative_strength_turn"],"stage3_evidence_fields":["production_capacity_bridge_pending","margin_bridge_pending","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv","profile_path":"atlas/symbol_profiles/012/012450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":47.41,"MFE_90D_pct":54.03,"MFE_180D_pct":155.72,"MAE_30D_pct":-6.26,"MAE_90D_pct":-6.26,"MAE_180D_pct":-6.26,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":425000.0,"max_drawdown_low_date":"2024-02-26","max_drawdown_low":155800.0,"drawdown_after_peak_pct":-36.47,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_export_framework_backlog_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"012450_2024-02-26_166200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C03 works when defense theme is tied to export framework, sovereign customer and backlog bridge. Green should still require exact source, production capacity, margin and cash-conversion evidence."}
```

### 6.2 274090 켄코아에어로스페이스 — aerospace supply-chain theme spike without framework backlog

Entry row: `2024-01-18 c=14840`.  
Forward path: same-day high `15900`, then lows reached `2024-03-20 l=10650`, `2024-10-29 l=7860`, and `2024-12-09 l=8780`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L84_C03_274090_20240118_STAGE2_FALSE_POSITIVE_AEROSPACE_THEME","case_id":"C03_R11L84_274090_KENCOA_AEROSPACE_THEME_SPIKE","symbol":"274090","company_name":"켄코아에어로스페이스","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"AEROSPACE_SUPPLY_CHAIN_THEME_SPIKE_WITHOUT_FRAMEWORK_BACKLOG","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-AerospaceThemeSpike-NoFrameworkBacklogBridge","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":14840.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_aerospace_defense_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; aerospace/defense supply-chain theme treated as insufficient without export framework, sovereign customer and backlog/margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["aerospace_defense_theme","relative_strength_spike"],"stage3_evidence_fields":["export_framework_missing","sovereign_customer_quality_missing","backlog_bridge_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/274/274090/2024.csv","profile_path":"atlas/symbol_profiles/274/274090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.14,"MFE_90D_pct":7.14,"MFE_180D_pct":7.14,"MAE_30D_pct":-24.19,"MAE_90D_pct":-28.23,"MAE_180D_pct":-47.04,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-18","peak_price":15900.0,"max_drawdown_low_date":"2024-10-29","max_drawdown_low":7860.0,"drawdown_after_peak_pct":-50.57,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"aerospace_theme_peak_without_export_backlog_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_aerospace_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"274090_2024-01-18_14840","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Aerospace supply-chain theme without framework backlog produced shallow MFE and deep MAE. C03 needs a local export-framework/backlog bridge guard."}
```

### 6.3 099320 쎄트렉아이 — space-defense theme extension without export-framework bridge

Entry row: `2024-07-01 c=54800`.  
Forward path: same-day high `58500`, then lows reached `2024-09-24 l=35250`, `2024-10-02 l=34650`, and `2024-12-10 l=35500`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L84_C03_099320_20240701_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_THEME","case_id":"C03_R11L84_099320_SATREC_SPACE_DEFENSE_THEME_EXTENSION","symbol":"099320","company_name":"쎄트렉아이","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"SPACE_DEFENSE_THEME_EXTENSION_WITHOUT_EXPORT_FRAMEWORK_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SpaceDefenseThemeExtension-NoExportFrameworkBridge","trigger_date":"2024-07-01","entry_date":"2024-07-01","entry_price":54800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_space_defense_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; satellite/space-defense theme extension treated as insufficient unless export framework, production capacity and margin bridge are verified","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["space_defense_theme","relative_strength_extension"],"stage3_evidence_fields":["export_framework_missing","production_capacity_bridge_missing","sovereign_customer_quality_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/099/099320/2024.csv","profile_path":"atlas/symbol_profiles/099/099320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.75,"MFE_90D_pct":6.75,"MFE_180D_pct":6.75,"MAE_30D_pct":-17.15,"MAE_90D_pct":-36.77,"MAE_180D_pct":-36.77,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-01","peak_price":58500.0,"max_drawdown_low_date":"2024-10-02","max_drawdown_low":34650.0,"drawdown_after_peak_pct":-40.77,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"space_defense_theme_extension_without_export_framework_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_space_defense_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"entry_after_2024-01-08_candidate_clean_forward_window","same_entry_group_id":"099320_2024-07-01_54800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Space-defense theme extension without export framework and production/margin bridge produced local peak then high MAE. C03 should block Yellow/Green without non-price backlog bridge."}
```

## 7. Score simulation rows

These rows are research proxy simulations only and do not change production scoring.

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C03_R11L84_012450_HANWHA_AERO_EXPORT_FRAMEWORK_BACKLOG","trigger_id":"R11L84_C03_012450_20240226_STAGE2_DEFENSE_PRIME_EXPORT_BACKLOG","symbol":"012450","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C03 gives credit only to export-framework/backlog bridge rather than price-only defense theme","raw_component_scores_before":{"export_framework_score":17,"sovereign_customer_quality":16,"backlog_visibility":15,"production_capacity_bridge":10,"margin_bridge_score":10,"relative_strength_score":15,"valuation_repricing_score":10,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":81,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"export_framework_score":20,"sovereign_customer_quality":18,"backlog_visibility":18,"production_capacity_bridge":12,"margin_bridge_score":12,"relative_strength_score":16,"valuation_repricing_score":11,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Export-framework/backlog bridge and very high MFE support upgrade, but exact source and margin/cash conversion proof still block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C03_R11L84_274090_KENCOA_AEROSPACE_THEME_SPIKE","trigger_id":"R11L84_C03_274090_20240118_STAGE2_FALSE_POSITIVE_AEROSPACE_THEME","symbol":"274090","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_scope":"current_default_proxy","profile_hypothesis":"aerospace theme without framework/backlog bridge should be blocked","raw_component_scores_before":{"export_framework_score":2,"sovereign_customer_quality":2,"backlog_visibility":2,"production_capacity_bridge":3,"margin_bridge_score":1,"relative_strength_score":13,"valuation_repricing_score":7,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":24,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_framework_score":0,"sovereign_customer_quality":0,"backlog_visibility":0,"production_capacity_bridge":1,"margin_bridge_score":0,"relative_strength_score":5,"valuation_repricing_score":3,"execution_risk_score":-18,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and deep MAE convert aerospace theme spike into evidence-quality failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C03_R11L84_099320_SATREC_SPACE_DEFENSE_THEME_EXTENSION","trigger_id":"R11L84_C03_099320_20240701_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_THEME","symbol":"099320","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_scope":"current_default_proxy","profile_hypothesis":"space-defense relative-strength extension without export framework should remain Watch/4B-risk","raw_component_scores_before":{"export_framework_score":2,"sovereign_customer_quality":3,"backlog_visibility":2,"production_capacity_bridge":4,"margin_bridge_score":1,"relative_strength_score":14,"valuation_repricing_score":7,"execution_risk_score":-10,"theme_spike_risk":-13,"information_confidence":3},"weighted_score_before":33,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_framework_score":0,"sovereign_customer_quality":1,"backlog_visibility":0,"production_capacity_bridge":2,"margin_bridge_score":0,"relative_strength_score":5,"valuation_repricing_score":3,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Local peak and high MAE argue for C03 local 4B guard unless framework/backlog bridge is verified."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R11L84_C03_P0_CURRENT","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C03 needs explicit export-framework/backlog and sovereign customer bridge distinction","eligible_trigger_count":3,"avg_MFE_90D_pct":22.64,"avg_MAE_90D_pct":-23.75,"avg_MFE_180D_pct":56.54,"avg_MAE_180D_pct":-30.02,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C03_framework_backlog_guard"}
{"row_type":"profile_comparison","comparison_id":"R11L84_C03_P1_SECTOR_SPECIFIC","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P1_L1_policy_defense_framework_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 policy-defense signals need export framework, sovereign customer, backlog, production capacity or margin bridge before Stage2-Actionable","changed_axes":["export_framework_required","sovereign_customer_quality_required","backlog_bridge_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_export_framework_sovereign_backlog_or_capacity_proxy"},"eligible_trigger_count":3,"avg_MFE_90D_pct":22.64,"avg_MAE_90D_pct":-23.75,"avg_MFE_180D_pct":56.54,"avg_MAE_180D_pct":-30.02,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R11L84_C03_P2_CANONICAL","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P2_C03_export_framework_backlog_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C03 should reward export-framework backlog, not aerospace/space defense theme spikes","changed_axes":["C03_export_framework_backlog_required","C03_theme_spike_penalty","C03_sovereign_customer_quality_gate"],"changed_thresholds":{"stage2_yellow_gate":"export_framework_or_backlog_bridge_required"},"eligible_trigger_count":3,"avg_MFE_90D_pct":22.64,"avg_MAE_90D_pct":-23.75,"avg_MFE_180D_pct":56.54,"avg_MAE_180D_pct":-30.02,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R11L84_C03_P3_COUNTEREXAMPLE_GUARD","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P3_C03_high_MAE_4B_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-25 while framework/backlog bridge is missing, block Yellow/Green","changed_axes":["C03_high_MAE_guardrail","C03_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_25"},"eligible_trigger_count":3,"avg_MFE_90D_pct":22.64,"avg_MAE_90D_pct":-23.75,"avg_MFE_180D_pct":56.54,"avg_MAE_180D_pct":-30.02,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_DEFENSE_EXPORT_BACKLOG_VS_SPACE_AEROSPACE_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":22.64,"avg_MAE90_pct":-23.75,"avg_MFE180_pct":56.54,"avg_MAE180_pct":-30.02,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"stage2_bad_entry_rate_MAE180_le_minus_30":0.67,"interpretation":"C03 needs bridge discipline. 012450 shows a true export-framework/backlog path, while 274090 and 099320 show aerospace/space defense theme spikes that fail without sovereign customer, framework backlog and margin bridge."}
{"row_type":"stage_transition_summary","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"012450","trigger_type":"Stage2-Actionable-DefensePrimeExportFrameworkBacklogBridge-Positive","entry_date":"2024-02-26","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_structural_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when export framework/backlog bridge exists; Green requires exact framework, production and margin evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"274090","trigger_type":"Stage2-FalsePositive-AerospaceThemeSpike-NoFrameworkBacklogBridge","entry_date":"2024-01-18","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_entry_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Aerospace theme spike without export-framework/backlog bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"099320","trigger_type":"Stage2-FalsePositive-SpaceDefenseThemeExtension-NoExportFrameworkBridge","entry_date":"2024-07-01","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_entry_space_theme_extension","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Space-defense theme extension without export framework, sovereign customer and production/margin bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","residual_type":"defense_theme_overcredit_without_export_framework_backlog_bridge","contribution":"Adds two C03 local 4B/high-MAE counterexamples against one defense-prime export-framework positive, avoiding top-covered C03 symbols and strengthening R11 policy-defense linkage evidence.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_SPACE_AEROSPACE_THEME_SPIKE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C03 now has two non-top-symbol theme-spike 4B/high-MAE counterexamples; next R11 loops should exact-URL repair export framework/backlog and sovereign customer evidence and add true 4C contract-delay rows."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"C03_export_framework_backlog_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"012450 worked with export framework/backlog bridge proxy; 274090 and 099320 failed when framework/backlog evidence was missing."}
{"row_type":"shadow_weight","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"C03_space_aerospace_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Aerospace and space-defense theme spikes showed low MFE and high MAE without sovereign customer and backlog evidence."}
{"row_type":"shadow_weight","round":"R11","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"C03_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-25 while export-framework/backlog bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - defense_theme_overcredit
  - aerospace_supply_chain_spike_no_framework_backlog
  - space_defense_theme_extension_no_export_bridge
new_axis_proposed:
  - C03_export_framework_backlog_bridge_required_shadow_only
  - C03_space_aerospace_theme_local_4B_watch_guard_shadow_only
  - C03_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C03
  - full_4b_requires_non_price_evidence within C03
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
3. Confirm R11 / L1 / C03 round-sector consistency. R11 permits L1 when the research lane is policy-defense linkage.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C03 top-covered symbols.
6. Confirm 099320 entry is after the 2024-01-08 corporate-action candidate.
7. If aggregate support remains stable after exact evidence URL repair, consider C03-scoped safe patch candidates:
   - C03_export_framework_backlog_bridge_required
   - C03_space_aerospace_theme_local_4B_watch_guard
   - C03_high_MAE_guardrail
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R11
completed_loop = 84
next_round = R12
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R11/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.
```
