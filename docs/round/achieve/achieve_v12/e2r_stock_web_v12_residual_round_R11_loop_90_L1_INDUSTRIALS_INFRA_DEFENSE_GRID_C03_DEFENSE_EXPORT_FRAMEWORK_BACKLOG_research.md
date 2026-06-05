# E2R Stock-Web v12 Residual Research — R11 Loop 90 / L1 / C03

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R11
loop: 90
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id: DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_DUALUSE_MACHINING_RF_THEME_PRICE_ONLY_DECAY
sector: industrials / defense / export framework / backlog / defense electronics / machining / RF components
output_file: e2r_stock_web_v12_residual_round_R11_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R10 loop 90`.

```text
scheduled_round = R11
scheduled_loop = 90
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```

R11 is the L1 policy / infrastructure / defense lane.  
C03 is selected because R11 loop89 used C02 grid/datacenter capex, while the prior L1 rotation shows the next defense-backlog bucket as C03.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
rows = 21
symbols = 12
good/bad Stage2 = 11/3
4B/4C = 0/0
top-covered = 079550, 047810, 065450, 005870, 103140, 003570
```

This loop avoids the C03 top-covered list and recent L1 loop symbols:

```text
R11 loop86 C03: 012450, 010820, 013810
R11 loop87 C04: 051600, 032820, 094820
R11 loop88 C05: 052690, 026150, 028100
R11 loop89 C02: 229640, 199820, 006910
R1 loop89 C03: 064350, 099320, 214430
R1 loop90 C04: 130660, 105840, 019990
```

Candidate hygiene note:

```text
During this execution path, R10/C30 construction-material rows and some R9/R8 surrounding candidates were touched while reading price files.
Those candidates are not used in this R11/C03 output.
```

Selected symbols:

```text
272210, 095190, 218410
```

This loop tests:

```text
defense electronics / radar / export-framework backlog bridge
vs
dual-use machining / naval-equipment theme with high price-only MFE but missing export framework and backlog bridge
vs
RF / GaN / defense-communications theme rebound without signed defense export backlog and margin/cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"272210","company_name":"한화시스템","profile_path":"atlas/symbol_profiles/272/272210.json","first_date":"2019-11-13","last_date":"2026-02-20","trading_day_count":1539,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2021-06-23"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"095190","company_name":"이엠코리아","profile_path":"atlas/symbol_profiles/095/095190.json","first_date":"2007-10-29","last_date":"2026-02-20","trading_day_count":4516,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2007-11-16","2011-01-14","2014-02-11","2018-01-03"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"218410","company_name":"RFHIC","profile_path":"atlas/symbol_profiles/218/218410.json","first_date":"2015-06-30","last_date":"2026-02-20","trading_day_count":2410,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2017-09-01","2017-12-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"SPAC/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"272210","trigger_type":"Stage2-Actionable-DefenseElectronicsExportFrameworkBacklogBridge-Positive","entry_date":"2024-04-22","duplicate_status":"new C03 symbol/trigger/date combination outside top-covered and previous L1 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"095190","trigger_type":"Stage2-FalsePositive-DualUseMachiningNavalThemePriceMFE-NoExportFrameworkBacklogBridge","entry_date":"2024-02-15","duplicate_status":"new C03 symbol/trigger/date combination outside top-covered and previous L1 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"218410","trigger_type":"Stage2-FalsePositive-RFDefenseCommunicationsThemeNoSignedExportBacklogBridge","entry_date":"2024-01-22","duplicate_status":"new C03 symbol/trigger/date combination outside top-covered and previous L1 loop symbols"}
```

## 4. Research question

C03 is not “방산 테마가 움직였다.”  
The useful defense-export signal must prove the bridge from policy or geopolitics to signed backlog economics:

```text
signed export contract or framework order
end-customer / country visibility
delivery schedule
backlog conversion
defense electronics or platform integration
export-license / government approval path
margin mix
working-capital and cash conversion
```

A defense headline without this bridge is a radar sweep with no target lock. The screen glows, but the fire-control chain has not closed.

Residual question:

```text
Can C03 distinguish:
1. defense electronics / radar / export-framework bridge with strong MFE and shallow entry MAE,
2. dual-use machining / naval-equipment theme with high MFE but no export framework, delivery and margin bridge,
3. RF/GaN communications rebound where no signed defense export backlog or cash bridge exists?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C03_R11L90_272210_HANWHA_SYSTEMS_DEFENSE_ELECTRONICS","symbol":"272210","company_name":"한화시스템","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-DefenseElectronicsExportFrameworkBacklogBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE90_very_high_MFE180_low_MAE_backlog_bridge","current_profile_verdict":"current_profile_correct_if_export_framework_backlog_delivery_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Defense electronics / radar / systems export-framework proxy produced high 90D MFE and very high 180D MFE with shallow MAE. Green still requires exact export customer, framework order, delivery and margin/cash evidence."}
{"row_type":"case","case_id":"C03_R11L90_095190_EMKOREA_DUALUSE_MACHINING_NAVAL_THEME","symbol":"095190","company_name":"이엠코리아","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DUALUSE_MACHINING_NAVAL_THEME_WITHOUT_EXPORT_FRAMEWORK_BACKLOG_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DualUseMachiningNavalThemePriceMFE-NoExportFrameworkBacklogBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_only_high_MFE_deep_MAE_no_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_dualuse_machining_MFE_overcredited","price_source":"Songdaiki/stock-web","notes":"Dual-use machining/naval-equipment theme produced high local MFE but later deep MAE. Without signed export framework, delivery and margin bridge, high MFE should remain 4B-watch."}
{"row_type":"case","case_id":"C03_R11L90_218410_RFHIC_RF_GAN_DEFENSE_THEME","symbol":"218410","company_name":"RFHIC","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"RF_GAN_DEFENSE_COMMUNICATIONS_THEME_WITHOUT_SIGNED_EXPORT_BACKLOG_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-RFDefenseCommunicationsThemeNoSignedExportBacklogBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_no_export_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_RF_defense_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"RF/GaN defense-communications rebound had near-zero original-entry MFE and deep forward MAE without signed defense customer backlog, export framework, delivery schedule or margin/cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 272210 한화시스템 — defense electronics export-framework backlog bridge

Entry row: `2024-04-22 c=16940`.  
Observed path: entry low `2024-04-22 l=16710`, 90D peak `2024-06-18 h=22450`, and full-window peak `2024-11-14 h=30200`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L90_C03_272210_20240422_STAGE2_DEFENSE_ELECTRONICS_EXPORT_BACKLOG","case_id":"C03_R11L90_272210_HANWHA_SYSTEMS_DEFENSE_ELECTRONICS","symbol":"272210","company_name":"한화시스템","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-DefenseElectronicsExportFrameworkBacklogBridge-Positive","trigger_date":"2024-04-22","entry_date":"2024-04-22","entry_price":16940.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_defense_electronics_export_framework_backlog_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; defense electronics, radar/systems export framework, delivery and backlog bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["defense_electronics_proxy","export_framework_proxy","backlog_conversion_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_country_pending","signed_framework_or_contract_pending","delivery_schedule_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv","profile_path":"atlas/symbol_profiles/272/272210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.61,"MFE_90D_pct":32.53,"MFE_180D_pct":78.28,"MAE_30D_pct":-1.36,"MAE_90D_pct":-1.36,"MAE_180D_pct":-1.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-14","peak_price":30200.0,"max_drawdown_low_date":"2024-04-22","max_drawdown_low":16710.0,"drawdown_after_peak_pct":-34.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.72,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_export_customer_framework_delivery_margin_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_very_high_MFE180_low_MAE_backlog_bridge","current_profile_verdict":"current_profile_correct_if_export_framework_backlog_delivery_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"272210_2024-04-22_16940","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C03 can allow Stage2/Yellow when defense strength is tied to signed export framework, backlog conversion, delivery schedule, customer/country visibility, margin and cash bridge. Green still requires exact source-grade evidence."}
```

### 6.2 095190 이엠코리아 — dual-use machining / naval-equipment theme with price-only MFE

Entry row: `2024-02-15 c=2560`, on a dual-use machining / naval-equipment theme spike.  
Observed path: high `2024-06-26 h=3920`, but then a collapse to `2024-12-09 l=1551`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L90_C03_095190_20240215_STAGE2_FALSE_POSITIVE_DUALUSE_MACHINING","case_id":"C03_R11L90_095190_EMKOREA_DUALUSE_MACHINING_NAVAL_THEME","symbol":"095190","company_name":"이엠코리아","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DUALUSE_MACHINING_NAVAL_THEME_WITHOUT_EXPORT_FRAMEWORK_BACKLOG_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_only_MFE_stress_test","trigger_type":"Stage2-FalsePositive-DualUseMachiningNavalThemePriceMFE-NoExportFrameworkBacklogBridge","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":2560.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_dualuse_machining_naval_equipment_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; dual-use machining/naval equipment theme treated as insufficient without signed export framework, customer, backlog, delivery and margin/cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["dualuse_machining_theme","naval_equipment_keyword","relative_strength_spike"],"stage3_evidence_fields":["signed_export_framework_missing","customer_country_missing","delivery_schedule_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_high_MFE","export_backlog_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095190/2024.csv","profile_path":"atlas/symbol_profiles/095/095190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.88,"MFE_90D_pct":53.13,"MFE_180D_pct":53.13,"MAE_30D_pct":-7.42,"MAE_90D_pct":-7.42,"MAE_180D_pct":-39.41,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-26","peak_price":3920.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1551.0,"drawdown_after_peak_pct":-60.43,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"dualuse_machining_theme_high_MFE_without_export_framework_backlog_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only_high_MFE","export_backlog_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_only_high_MFE_deep_MAE_no_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_dualuse_machining_MFE_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"095190_2024-02-15_2560","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C03 should not count high MFE as defense-export evidence if the move is price-only. Signed framework order, customer/country, delivery schedule, backlog conversion, margin and cash bridge must be exact-repaired before Yellow/Green."}
```

### 6.3 218410 RFHIC — RF/GaN defense-communications theme without signed backlog bridge

Entry row: `2024-01-22 c=19460`.  
Observed path: local high `2024-01-23 h=19740`, then a long drawdown to `2024-12-09 l=10650`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L90_C03_218410_20240122_STAGE2_FALSE_POSITIVE_RF_DEFENSE_THEME","case_id":"C03_R11L90_218410_RFHIC_RF_GAN_DEFENSE_THEME","symbol":"218410","company_name":"RFHIC","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"RF_GAN_DEFENSE_COMMUNICATIONS_THEME_WITHOUT_SIGNED_EXPORT_BACKLOG_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-RFDefenseCommunicationsThemeNoSignedExportBacklogBridge","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":19460.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_RF_GaN_defense_communications_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; RF/GaN defense communications theme treated as insufficient without signed defense customer backlog, export framework, delivery, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["RF_GaN_defense_theme","communications_keyword","relative_strength_rebound"],"stage3_evidence_fields":["signed_defense_backlog_missing","export_framework_missing","delivery_schedule_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["near_zero_MFE","backlog_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/218/218410/2024.csv","profile_path":"atlas/symbol_profiles/218/218410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.44,"MFE_90D_pct":1.44,"MFE_180D_pct":1.44,"MAE_30D_pct":-15.16,"MAE_90D_pct":-23.95,"MAE_180D_pct":-45.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-23","peak_price":19740.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":10650.0,"drawdown_after_peak_pct":-46.05,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"RF_GaN_defense_theme_without_signed_export_backlog_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","export_backlog_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_export_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_RF_defense_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_SPAC_transition_pre_2024; selected_window_clean","same_entry_group_id":"218410_2024-01-22_19460","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C03 should not promote RF/GaN communications theme strength without signed defense backlog, export framework, delivery schedule, margin and cash bridge. Near-zero MFE and deep MAE force Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C03_R11L90_272210_HANWHA_SYSTEMS_DEFENSE_ELECTRONICS","trigger_id":"R11L90_C03_272210_20240422_STAGE2_DEFENSE_ELECTRONICS_EXPORT_BACKLOG","symbol":"272210","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C03 requires signed export framework, customer/country, delivery schedule, backlog conversion, margin and cash bridge rather than defense label alone","raw_component_scores_before":{"export_framework_score":13,"customer_country_score":11,"signed_backlog_score":12,"delivery_schedule_score":10,"platform_integration_score":10,"margin_bridge_score":9,"cash_conversion_score":7,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"export_framework_score":16,"customer_country_score":14,"signed_backlog_score":15,"delivery_schedule_score":13,"platform_integration_score":12,"margin_bridge_score":11,"cash_conversion_score":9,"relative_strength_score":15,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Defense electronics/export-framework bridge plus high MFE supports Yellow/Green-candidate watch; exact contract/customer/delivery evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C03_R11L90_095190_EMKOREA_DUALUSE_MACHINING_NAVAL_THEME","trigger_id":"R11L90_C03_095190_20240215_STAGE2_FALSE_POSITIVE_DUALUSE_MACHINING","symbol":"095190","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_scope":"current_default_proxy","profile_hypothesis":"dual-use machining theme with high MFE but no signed export framework should be blocked as price-only","raw_component_scores_before":{"export_framework_score":1,"customer_country_score":0,"signed_backlog_score":0,"delivery_schedule_score":0,"platform_integration_score":2,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":15,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-22,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_framework_score":0,"customer_country_score":0,"signed_backlog_score":0,"delivery_schedule_score":0,"platform_integration_score":1,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"High MFE is price-only; deep later MAE and missing export/backlog bridge block Yellow/Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C03_R11L90_218410_RFHIC_RF_GAN_DEFENSE_THEME","trigger_id":"R11L90_C03_218410_20240122_STAGE2_FALSE_POSITIVE_RF_DEFENSE_THEME","symbol":"218410","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_scope":"current_default_proxy","profile_hypothesis":"RF/GaN defense theme without signed backlog and delivery bridge should remain Watch/4B","raw_component_scores_before":{"export_framework_score":1,"customer_country_score":0,"signed_backlog_score":0,"delivery_schedule_score":0,"platform_integration_score":2,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_framework_score":0,"customer_country_score":0,"signed_backlog_score":0,"delivery_schedule_score":0,"platform_integration_score":1,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE convert RF/defense communications rebound into missing export-backlog bridge failure."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R11L90_C03_P0_CURRENT","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C03 needs explicit export framework, customer/country, signed backlog, delivery, margin/cash and price-only dual-use theme taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":29.03,"avg_MAE90_pct":-10.91,"avg_MFE180_pct":44.28,"avg_MAE180_pct":-28.68,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.57,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C03_export_framework_backlog_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R11L90_C03_P1_SECTOR_SPECIFIC","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P1_L1_defense_export_framework_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 defense signals need signed export framework, customer/country visibility, delivery schedule, backlog conversion, margin or cash conversion before Stage2-Actionable","changed_axes":["export_framework_required","signed_backlog_delivery_required","dualuse_RF_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_export_framework_customer_country_backlog_delivery_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":29.03,"avg_MAE90_pct":-10.91,"avg_MFE180_pct":44.28,"avg_MAE180_pct":-28.68,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R11L90_C03_P2_CANONICAL","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P2_C03_export_framework_backlog_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C03 should reward signed export/backlog mechanics, not dual-use machining or RF theme labels","changed_axes":["C03_export_framework_backlog_delivery_margin_bridge_required","C03_dualuse_RF_theme_local_4B_guard","C03_price_only_MFE_not_backlog_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"signed_export_or_framework_plus_delivery_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":29.03,"avg_MAE90_pct":-10.91,"avg_MFE180_pct":44.28,"avg_MAE180_pct":-28.68,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R11L90_C03_P3_COUNTEREXAMPLE_GUARD","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","profile_id":"P3_C03_price_only_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If export/backlog bridge is missing, MFE can only be credited after exact non-price evidence; MAE180<=-35 routes to 4B-watch even when local MFE is high","changed_axes":["C03_price_only_MFE_guardrail","C03_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_5_or_MAE180_le_minus35); high_MFE_without_bridge_not_positive"},"eligible_trigger_count":3,"avg_MFE90_pct":29.03,"avg_MAE90_pct":-10.91,"avg_MFE180_pct":44.28,"avg_MAE180_pct":-28.68,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_DEFENSE_ELECTRONICS_POSITIVE_VS_DUALUSE_RF_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":29.03,"avg_MAE90_pct":-10.91,"avg_MFE180_pct":44.28,"avg_MAE180_pct":-28.68,"stage2_hit_rate_MFE90_ge20":0.67,"price_only_high_MFE_counterexample_count":1,"stage2_bad_entry_rate_bridge_missing":0.67,"interpretation":"C03 needs bridge discipline. 한화시스템 shows defense electronics/export-framework backlog bridge can support Yellow/Green-candidate-watch, while 이엠코리아 and RFHIC show dual-use/RF defense theme moves should not be promoted without signed export framework, customer/country visibility, delivery schedule, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"272210","trigger_type":"Stage2-Actionable-DefenseElectronicsExportFrameworkBacklogBridge-Positive","entry_date":"2024-04-22","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_export_backlog_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when defense strength is tied to export framework, backlog conversion, delivery and margin/cash bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"095190","trigger_type":"Stage2-FalsePositive-DualUseMachiningNavalThemePriceMFE-NoExportFrameworkBacklogBridge","entry_date":"2024-02-15","stage2_to_90D_outcome":"price_only_high_MFE_without_backlog_bridge","stage2_to_180D_outcome":"failed_dualuse_theme_deep_MAE","MFE90_ge20":true,"MAE180_le_minus35":true,"transition_note":"Dual-use machining/naval equipment high MFE without signed export/backlog bridge should be treated as 4B-watch, not positive C03 evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"218410","trigger_type":"Stage2-FalsePositive-RFDefenseCommunicationsThemeNoSignedExportBacklogBridge","entry_date":"2024-01-22","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_RF_defense_theme_deep_MAE","MFE90_ge20":false,"MAE180_le_minus35":true,"transition_note":"RF/GaN defense communications rebound without signed export backlog and delivery bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","residual_type":"dualuse_RF_defense_theme_overcredit_without_signed_export_framework_backlog_bridge","contribution":"Adds two C03 4B counterexamples against one defense-electronics export/backlog positive, avoiding C03 top-covered and recent L1 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_BRIDGE_VS_DUALUSE_MACHINING_RF_THEME_PRICE_ONLY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C03 now has non-top-symbol defense-electronics export/backlog positive and two dual-use/RF weak-bridge counterexamples; next L1 C03 loops should exact-URL repair signed framework, customer/country visibility, delivery schedule, export-license path, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"C03_export_framework_backlog_delivery_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"272210 worked when defense electronics/export-framework proxy existed; 095190 and 218410 failed when defense-adjacent price action lacked signed export/backlog/delivery evidence."}
{"row_type":"shadow_weight","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"C03_dualuse_RF_theme_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Dual-use machining and RF/GaN rows were not sufficient C03 positives without signed export framework, customer/country, delivery and margin bridge."}
{"row_type":"shadow_weight","round":"R11","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"C03_price_only_MFE_not_backlog_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"095190 shows even MFE90 above 50 should not count as positive C03 evidence when the export/backlog bridge is missing and MAE180 is deep."}
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
  - dualuse_machining_theme_overcredit
  - RF_GaN_defense_theme_overcredit
  - signed_export_framework_backlog_bridge_missing
new_axis_proposed:
  - C03_export_framework_backlog_delivery_margin_bridge_required_shadow_only
  - C03_dualuse_RF_theme_local_4B_guard_shadow_only
  - C03_price_only_MFE_not_backlog_validation_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.  
`272210`, `095190`, and `218410` have historical corporate-action or SPAC/name-transition candidates before the selected 2024 windows; those candidates are outside the chosen forward windows and do not contaminate this residual price-path analysis.  
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
3. Confirm R11 / L1 / C03 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C03 top-covered symbols
   - previous R11 loop86 C03 symbols
   - previous R11 loop87 C04 symbols
   - previous R11 loop88 C05 symbols
   - previous R11 loop89 C02 symbols
   - previous R1 loop89 C03 symbols
   - previous R1 loop90 C04 symbols
6. Confirm accidentally touched R10/C30, R9/C29 and R8/C27 candidate rows are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C03-scoped safe patch candidates:
   - C03_export_framework_backlog_delivery_margin_bridge_required
   - C03_dualuse_RF_theme_local_4B_guard
   - C03_price_only_MFE_not_backlog_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R11
completed_loop = 90
next_round = R12
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R11/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG.
```
