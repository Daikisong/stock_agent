# E2R Stock-Web v12 Residual Research — R1 Loop 90 / L1 / C04

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R1
loop: 90
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_OM_SERVICE_PROJECT_POLICY_BRIDGE_VS_INSTRUMENTATION_ACTUATOR_THEME_DELAY_DECAY
sector: industrials / nuclear policy / project legal delay / O&M service / instrumentation / actuator
output_file: e2r_stock_web_v12_residual_round_R1_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R13 loop 89`.

```text
scheduled_round = R1
scheduled_loop = 90
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```

R1 is restricted to L1 industrials / infra / defense / grid.  
C04 is selected because the immediate loop89 R13 redteam closed the cycle and the L1 bucket should restart without simply repeating C02/C03. C04 remains thin and has a 4B/legal-delay profile that benefits from more non-top-symbol evidence.

No-Repeat Index snapshot:

```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
rows = 12
symbols = 7
good/bad Stage2 = 5/3
4B/4C = 1/0
top-covered = 011700, 083650, 006910, 034020, 042370, 046120
```

This loop avoids the C04 top-covered symbols and recent L1 loop symbols:

```text
R11 loop87 C04: 051600, 032820, 094820
R11 loop88 C05: 052690, 026150, 028100
R11 loop89 C02: 229640, 199820, 006910
R1 loop89 C03: 064350, 099320, 214430
```

Selected symbols:

```text
130660, 105840, 019990
```

This loop tests:

```text
nuclear O&M / utility-service policy bridge
vs
nuclear instrumentation theme with price-only MFE but deep later MAE
vs
nuclear actuator / policy-equipment rebound without project certainty, legal milestone or margin bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"130660","company_name":"한전산업","profile_path":"atlas/symbol_profiles/130/130660.json","first_date":"2010-12-16","last_date":"2026-02-20","trading_day_count":3718,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"105840","company_name":"우진","profile_path":"atlas/symbol_profiles/105/105840.json","first_date":"2010-07-26","last_date":"2026-02-20","trading_day_count":3832,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2012-11-19","2012-12-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"019990","company_name":"에너토크","profile_path":"atlas/symbol_profiles/019/019990.json","first_date":"2006-02-01","last_date":"2026-02-20","trading_day_count":4945,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2016-07-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"130660","trigger_type":"Stage2-Actionable-NuclearOMServicePolicyProjectBridge-Positive","entry_date":"2024-04-22","duplicate_status":"new C04 symbol/trigger/date combination outside C04 top-covered and previous L1 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"105840","trigger_type":"Stage2-FalsePositive-NuclearInstrumentationThemePriceMFE-NoProjectLegalMarginBridge","entry_date":"2024-05-22","duplicate_status":"new C04 symbol/trigger/date combination outside C04 top-covered and previous L1 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"019990","trigger_type":"Stage2-FalsePositive-NuclearActuatorPolicyEquipmentRebound-NoLegalProjectBridge","entry_date":"2024-02-22","duplicate_status":"new C04 symbol/trigger/date combination outside C04 top-covered and previous L1 loop symbols"}
```

## 4. Research question

C04 is not “원전주가 올랐다.”  
The useful nuclear-policy signal must prove a chain from policy to project economics:

```text
project approval or legal milestone
customer/project scope
O&M or service backlog
regulatory certainty
delivery or maintenance schedule
margin and working-capital bridge
delay-risk control
cash conversion
```

A nuclear theme without this bridge is a control-room light flashing before the reactor is synchronized to the grid. It draws attention, but it does not yet sell power or services.

Residual question:

```text
Can C04 distinguish:
1. nuclear O&M/service policy bridge with high MFE and controlled early MAE,
2. instrumentation price-only MFE that later collapses because project/legal/margin evidence is missing,
3. actuator/policy-equipment rebound where no legal milestone, order scope or cash bridge confirms the theme?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C04_R1L90_130660_KEPCO_INDUSTRIAL_NUCLEAR_OM_SERVICE","symbol":"130660","company_name":"한전산업","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_OM_SERVICE_POLICY_PROJECT_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-NuclearOMServicePolicyProjectBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_low_MAE_Green_strict","current_profile_verdict":"current_profile_correct_if_project_policy_service_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Nuclear O&M/service policy bridge proxy produced very high 90D/180D MFE with low MAE. Green still requires exact project scope, legal/regulatory milestone, service backlog and margin/cash evidence."}
{"row_type":"case","case_id":"C04_R1L90_105840_WOOJIN_INSTRUMENTATION_THEME","symbol":"105840","company_name":"우진","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_INSTRUMENTATION_THEME_WITHOUT_PROJECT_LEGAL_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-NuclearInstrumentationThemePriceMFE-NoProjectLegalMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_only_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_instrumentation_theme_MFE_overcredited","price_source":"Songdaiki/stock-web","notes":"Instrumentation theme produced local MFE above 20%, but later deep MAE shows it should not be counted as C04 project/legal success without exact non-price bridge."}
{"row_type":"case","case_id":"C04_R1L90_019990_ENERTORK_ACTUATOR_POLICY_REBOUND","symbol":"019990","company_name":"에너토크","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_ACTUATOR_POLICY_EQUIPMENT_REBOUND_WITHOUT_LEGAL_PROJECT_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-NuclearActuatorPolicyEquipmentRebound-NoLegalProjectBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_actuator_policy_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Actuator/policy-equipment rebound had near-zero MFE and deep later MAE without legal milestone, project scope, order backlog or margin/cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 130660 한전산업 — nuclear O&M/service project-policy bridge positive

Entry row: `2024-04-22 c=7060`.  
Observed path: early low `2024-04-22 l=6920`, 30D peak around `2024-05-28 h=12480`, and full-window high `2024-07-18 h=19500`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L90_C04_130660_20240422_STAGE2_NUCLEAR_OM_SERVICE_POLICY","case_id":"C04_R1L90_130660_KEPCO_INDUSTRIAL_NUCLEAR_OM_SERVICE","symbol":"130660","company_name":"한전산업","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_OM_SERVICE_POLICY_PROJECT_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-NuclearOMServicePolicyProjectBridge-Positive","trigger_date":"2024-04-22","entry_date":"2024-04-22","entry_price":7060.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_nuclear_OM_service_policy_project_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; nuclear O&M/service policy, project scope and regulatory bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_policy_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["nuclear_policy_project_proxy","OM_service_scope_proxy","regulatory_certainty_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_project_scope_pending","legal_or_regulatory_milestone_pending","service_backlog_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv","profile_path":"atlas/symbol_profiles/130/130660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":76.77,"MFE_90D_pct":176.20,"MFE_180D_pct":176.20,"MAE_30D_pct":-1.98,"MAE_90D_pct":-1.98,"MAE_180D_pct":-1.98,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":19500.0,"max_drawdown_low_date":"2024-04-22","max_drawdown_low":6920.0,"drawdown_after_peak_pct":-54.41,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_project_legal_service_margin_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_low_MAE_Green_strict","current_profile_verdict":"current_profile_correct_if_project_policy_service_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"130660_2024-04-22_7060","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C04 can allow Stage2/Yellow when nuclear policy strength is tied to project/legal milestones, O&M/service scope, regulatory certainty, margin and cash bridge. Green still requires exact source-grade evidence."}
```

### 6.2 105840 우진 — nuclear instrumentation theme with price-only MFE but no project/legal/margin bridge

Entry row: `2024-05-22 c=9100`.  
Observed path: peak `2024-05-27 h=11200`, then late-year low `2024-12-09 l=5630`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L90_C04_105840_20240522_STAGE2_FALSE_POSITIVE_INSTRUMENTATION_THEME","case_id":"C04_R1L90_105840_WOOJIN_INSTRUMENTATION_THEME","symbol":"105840","company_name":"우진","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_INSTRUMENTATION_THEME_WITHOUT_PROJECT_LEGAL_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;price_only_blowoff_stress_test","trigger_type":"Stage2-FalsePositive-NuclearInstrumentationThemePriceMFE-NoProjectLegalMarginBridge","trigger_date":"2024-05-22","entry_date":"2024-05-22","entry_price":9100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_nuclear_instrumentation_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; nuclear instrumentation theme treated as insufficient without project approval, legal milestone, order scope, margin and cash bridge","evidence_source_type":"historical_public_policy_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["nuclear_instrumentation_theme","relative_strength_spike"],"stage3_evidence_fields":["project_approval_missing","legal_milestone_missing","order_scope_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_high_MFE","project_legal_bridge_missing_watch","deep_180D_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv","profile_path":"atlas/symbol_profiles/105/105840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.08,"MFE_90D_pct":23.08,"MFE_180D_pct":23.08,"MAE_30D_pct":-5.05,"MAE_90D_pct":-12.20,"MAE_180D_pct":-38.13,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-27","peak_price":11200.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":5630.0,"drawdown_after_peak_pct":-49.73,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"nuclear_instrumentation_price_MFE_without_project_legal_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only_high_MFE","project_legal_bridge_missing_watch","deep_180D_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_only_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_instrumentation_theme_MFE_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"105840_2024-05-22_9100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C04 should not count nuclear instrumentation price-only MFE as project/legal success. Project approval, legal milestone, order scope, margin and cash bridge must be exact-repaired before Yellow/Green."}
```

### 6.3 019990 에너토크 — actuator/policy-equipment rebound without legal/project bridge

Entry row: `2024-02-22 c=6940`.  
Observed path: local high `2024-02-22 h=7100`, later high `2024-10-22 h=7130`, and late-year low `2024-12-09 l=4030`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L90_C04_019990_20240222_STAGE2_FALSE_POSITIVE_ACTUATOR_POLICY_REBOUND","case_id":"C04_R1L90_019990_ENERTORK_ACTUATOR_POLICY_REBOUND","symbol":"019990","company_name":"에너토크","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_ACTUATOR_POLICY_EQUIPMENT_REBOUND_WITHOUT_LEGAL_PROJECT_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-NuclearActuatorPolicyEquipmentRebound-NoLegalProjectBridge","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":6940.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_nuclear_actuator_policy_equipment_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; actuator/policy equipment rebound treated as insufficient without legal milestone, project approval, customer order, delay-risk control and margin/cash bridge","evidence_source_type":"historical_public_policy_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["nuclear_actuator_theme","policy_equipment_rebound"],"stage3_evidence_fields":["legal_milestone_missing","project_approval_missing","customer_order_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["near_zero_MFE","legal_project_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/019/019990/2024.csv","profile_path":"atlas/symbol_profiles/019/019990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.31,"MFE_90D_pct":2.31,"MFE_180D_pct":2.74,"MAE_30D_pct":-13.98,"MAE_90D_pct":-18.44,"MAE_180D_pct":-41.93,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-22","peak_price":7130.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":4030.0,"drawdown_after_peak_pct":-43.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"actuator_policy_equipment_rebound_without_legal_project_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","legal_project_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_actuator_policy_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"019990_2024-02-22_6940","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C04 should not promote actuator/policy equipment rebound without legal milestone, project approval, order scope, delay-risk control and margin/cash bridge. Near-zero MFE and deep MAE require 4B-watch."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_R1L90_130660_KEPCO_INDUSTRIAL_NUCLEAR_OM_SERVICE","trigger_id":"R1L90_C04_130660_20240422_STAGE2_NUCLEAR_OM_SERVICE_POLICY","symbol":"130660","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C04 requires project/legal milestone, O&M/service scope, delay-risk control, margin and cash bridge rather than nuclear policy label alone","raw_component_scores_before":{"policy_specificity_score":13,"project_scope_score":12,"legal_milestone_score":10,"service_backlog_score":11,"delay_risk_control_score":9,"margin_bridge_score":10,"cash_conversion_score":7,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"policy_specificity_score":16,"project_scope_score":15,"legal_milestone_score":13,"service_backlog_score":14,"delay_risk_control_score":11,"margin_bridge_score":12,"cash_conversion_score":9,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Project/legal/O&M service bridge plus very high MFE supports Yellow/Green-candidate watch; exact source-grade evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_R1L90_105840_WOOJIN_INSTRUMENTATION_THEME","trigger_id":"R1L90_C04_105840_20240522_STAGE2_FALSE_POSITIVE_INSTRUMENTATION_THEME","symbol":"105840","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_scope":"current_default_proxy","profile_hypothesis":"instrumentation theme with MFE but no project/legal bridge should be Watch/4B","raw_component_scores_before":{"policy_specificity_score":4,"project_scope_score":1,"legal_milestone_score":0,"service_backlog_score":1,"delay_risk_control_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":13,"valuation_repricing_score":5,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"policy_specificity_score":1,"project_scope_score":0,"legal_milestone_score":0,"service_backlog_score":0,"delay_risk_control_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"MFE is price-only; deep 180D MAE and missing legal/project/margin bridge block Yellow/Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_R1L90_019990_ENERTORK_ACTUATOR_POLICY_REBOUND","trigger_id":"R1L90_C04_019990_20240222_STAGE2_FALSE_POSITIVE_ACTUATOR_POLICY_REBOUND","symbol":"019990","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_scope":"current_default_proxy","profile_hypothesis":"actuator/policy equipment rebound without legal project bridge should be blocked","raw_component_scores_before":{"policy_specificity_score":3,"project_scope_score":1,"legal_milestone_score":0,"service_backlog_score":0,"delay_risk_control_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":5,"valuation_repricing_score":2,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"policy_specificity_score":1,"project_scope_score":0,"legal_milestone_score":0,"service_backlog_score":0,"delay_risk_control_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE convert actuator/policy rebound into missing legal-project bridge failure."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R1L90_C04_P0_CURRENT","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C04 needs explicit project/legal/O&M service/margin/cash bridge and instrumentation/actuator theme 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":67.20,"avg_MAE90_pct":-10.87,"avg_MFE180_pct":67.34,"avg_MAE180_pct":-27.35,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":0.67,"score_return_alignment_verdict":"mixed_without_C04_project_legal_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R1L90_C04_P1_SECTOR_SPECIFIC","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P1_L1_nuclear_project_legal_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 nuclear policy signals need project scope, legal/regulatory milestone, service backlog, delay-risk control, margin or cash conversion before Stage2-Actionable","changed_axes":["project_scope_required","legal_milestone_required","instrumentation_actuator_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_project_scope_legal_milestone_service_backlog_delay_control_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":67.20,"avg_MAE90_pct":-10.87,"avg_MFE180_pct":67.34,"avg_MAE180_pct":-27.35,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R1L90_C04_P2_CANONICAL","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P2_C04_project_legal_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C04 should reward policy-to-project mechanics, not nuclear equipment theme labels","changed_axes":["C04_project_legal_margin_bridge_required","C04_instrumentation_actuator_theme_local_4B_guard","C04_price_only_MFE_not_project_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"project_scope_or_legal_milestone_plus_service_backlog_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":67.20,"avg_MAE90_pct":-10.87,"avg_MFE180_pct":67.34,"avg_MAE180_pct":-27.35,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R1L90_C04_P3_COUNTEREXAMPLE_GUARD","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P3_C04_price_only_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If project/legal bridge is missing, MFE cannot validate Stage2/Yellow when MAE180<=-25; if MFE90<5 and bridge is missing, hard-block Yellow/Green","changed_axes":["C04_price_only_MFE_guardrail","C04_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_MAE180_le_minus25; hard_block_if_MFE90_lt_5_and_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":67.20,"avg_MAE90_pct":-10.87,"avg_MFE180_pct":67.34,"avg_MAE180_pct":-27.35,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_NUCLEAR_OM_SERVICE_POSITIVE_VS_INSTRUMENTATION_ACTUATOR_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":67.20,"avg_MAE90_pct":-10.87,"avg_MFE180_pct":67.34,"avg_MAE180_pct":-27.35,"stage2_hit_rate_MFE90_ge20":0.67,"stage2_bad_entry_rate_bridge_missing":0.67,"price_only_MFE_counterexample_count":1,"interpretation":"C04 needs bridge discipline. 한전산업 shows nuclear O&M/service policy bridge can create very high MFE, while 우진 and 에너토크 show instrumentation/actuator nuclear themes should not be promoted without project approval, legal milestone, order scope, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"130660","trigger_type":"Stage2-Actionable-NuclearOMServicePolicyProjectBridge-Positive","entry_date":"2024-04-22","stage2_to_90D_outcome":"good_stage2_very_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_project_policy_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when nuclear policy is tied to project/legal milestone, O&M/service scope and margin/cash bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"105840","trigger_type":"Stage2-FalsePositive-NuclearInstrumentationThemePriceMFE-NoProjectLegalMarginBridge","entry_date":"2024-05-22","stage2_to_90D_outcome":"price_only_MFE_without_project_bridge","stage2_to_180D_outcome":"failed_instrumentation_theme_deep_MAE","MFE90_ge20":true,"MAE180_le_minus25":true,"transition_note":"Instrumentation MFE without project/legal/margin bridge should be treated as 4B-watch, not positive evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"019990","trigger_type":"Stage2-FalsePositive-NuclearActuatorPolicyEquipmentRebound-NoLegalProjectBridge","entry_date":"2024-02-22","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_bridge_missing","stage2_to_180D_outcome":"failed_actuator_policy_rebound_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Actuator/policy-equipment rebound without legal project bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","residual_type":"nuclear_instrumentation_actuator_theme_overcredit_without_project_legal_margin_bridge","contribution":"Adds two C04 4B counterexamples against one nuclear O&M/service policy positive, avoiding C04 top-covered and recent L1 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_OM_SERVICE_PROJECT_POLICY_BRIDGE_VS_INSTRUMENTATION_ACTUATOR_THEME_DELAY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C04 now has non-top-symbol O&M/service policy positive and two instrumentation/actuator weak-bridge counterexamples; next L1 C04 loops should exact-URL repair project approval, legal/regulatory milestone, customer/order scope, service backlog, delay-risk control, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"C04_project_legal_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"130660 worked when project-policy/O&M service proxy existed; 105840 and 019990 failed or became price-only when project/legal/margin bridge was missing."}
{"row_type":"shadow_weight","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"C04_instrumentation_actuator_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Instrumentation and actuator rows showed either price-only MFE with deep MAE or near-zero MFE with deep MAE when non-price project/legal bridge was missing."}
{"row_type":"shadow_weight","round":"R1","loop":"90","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"C04_price_only_MFE_not_project_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"105840 shows MFE90>=20 should not count as C04 positive evidence when project/legal/margin bridge is missing and MAE180<=-25."}
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
  - nuclear_equipment_theme_overcredit
  - instrumentation_theme_MFE_overcredit
  - legal_project_bridge_missing
  - margin_cash_bridge_missing
new_axis_proposed:
  - C04_project_legal_margin_bridge_required_shadow_only
  - C04_instrumentation_actuator_theme_local_4B_watch_guard_shadow_only
  - C04_price_only_MFE_not_project_validation_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.  
`105840` and `019990` have historical corporate-action candidates long before 2024, but their selected 2024 windows are usable for price-path residual analysis.  
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
3. Confirm R1 / L1 / C04 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C04 top-covered symbols
   - previous R11 loop87 C04 symbols
   - previous R11 loop88 C05 symbols
   - previous R11 loop89 C02 symbols
   - previous R1 loop89 C03 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C04-scoped safe patch candidates:
   - C04_project_legal_margin_bridge_required
   - C04_instrumentation_actuator_theme_local_4B_watch_guard
   - C04_price_only_MFE_not_project_validation_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R1
completed_loop = 90
next_round = R2
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.
```
