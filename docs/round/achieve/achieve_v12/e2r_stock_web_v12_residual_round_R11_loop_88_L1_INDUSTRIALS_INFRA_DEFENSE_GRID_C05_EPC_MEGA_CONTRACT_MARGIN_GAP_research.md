# E2R Stock-Web v12 Residual Research — R11 Loop 88 / L1 / C05

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R11
loop: 88
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: EPC_NUCLEAR_ENGINEERING_PROJECT_SCOPE_MARGIN_BRIDGE_VS_CIVIL_WORKS_POLICY_THEME_BLOWOFF
sector: industrials / infra / EPC / nuclear engineering / civil works / mega-contract margin gap
output_file: e2r_stock_web_v12_residual_round_R11_loop_88_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R10 loop 88`.

```text
scheduled_round = R11
scheduled_loop = 88
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

R11 is the L1 policy / defense / infra linkage lane.  
C05 is selected because the recent R11 loop sequence already covered:

```text
R11 loop85: C02_POWER_GRID_DATACENTER_CAPEX
R11 loop86: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
R11 loop87: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```

C05 is under-covered and still thin:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
rows = 10
symbols = 9
good/bad Stage2 = 3/4
4B/4C = 0/0
top-covered = 053690, 002150, 011560, 023350, 023960, 054930
```

This loop avoids the C05 top-covered symbols and also avoids the previous R11 loop symbols:

```text
R11 loop85 C02: 267260, 010120, 103590
R11 loop86 C03: 012450, 010820, 013810
R11 loop87 C04: 051600, 032820, 094820
```

Additional candidate rejection notes:

```text
028050 / 삼성E&A was checked but not used here because it was just used in R10 loop88 for C30 construction/backlog/cash bridge.
001880 / DL건설 was rejected because the 2024 forward window ends too early around delisting/merger behavior.
009410 / 태영건설 was rejected because the 2024 path contains suspension/reopening/corporate-action contamination.
```

Selected symbols:

```text
052690, 026150, 028100
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"052690","company_name":"한전기술","profile_path":"atlas/symbol_profiles/052/052690.json","first_date":"2009-12-14","last_date":"2026-02-20","trading_day_count":3984,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"026150","company_name":"특수건설","profile_path":"atlas/symbol_profiles/026/026150.json","first_date":"1997-08-06","last_date":"2026-02-20","trading_day_count":6709,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1998-01-15","2000-05-02","2009-07-15","2018-11-02"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"028100","company_name":"동아지질","profile_path":"atlas/symbol_profiles/028/028100.json","first_date":"2009-06-12","last_date":"2026-02-20","trading_day_count":4114,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2022-02-21"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before selected 2024 forward window. Late-2024 share-count change watch is noted before any patch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; late_2024_share_count_drift_watch"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"052690","trigger_type":"Stage2-Actionable-NuclearEPCEngineeringProjectScopeMarginBridge-Positive","entry_date":"2024-04-22","duplicate_status":"new C05 symbol/trigger/date combination outside top-covered and previous R11 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"026150","trigger_type":"Stage2-FalsePositive-CivilWorksInfrastructureThemeNoEPCMarginBridge","entry_date":"2024-01-30","duplicate_status":"new C05 symbol/trigger/date combination outside top-covered and previous R11 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"028100","trigger_type":"Stage2-FalsePositive-GeotechnicalCivilWorksThemeNoFreshContractMarginBridge","entry_date":"2024-01-30","duplicate_status":"new C05 symbol/trigger/date combination outside top-covered and previous R11 loop symbols"}
```

## 4. Research question

C05 is not “EPC or construction engineering theme moved.”  
The useful EPC signal must prove contract economics: project scope, client quality, contract certainty, margin clause, milestone billing, working-capital schedule, cost inflation protection, execution risk and cash conversion. A mega-contract headline without that bridge is a large blueprint with no quantity survey; the building may be drawn, but the margin is not yet poured into concrete.

Residual question:

```text
Can C05 distinguish:
1. nuclear/EPC engineering project-scope bridge with large MFE and controlled early MAE,
2. civil-works/infrastructure price spike where no EPC project-scope, margin or cash bridge exists,
3. geotechnical/civil-works rebound where later price bursts do not validate the original weak entry without fresh contract economics?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C05_R11L88_052690_KEPCO_ENGINEERING_NUCLEAR_EPC_SCOPE","symbol":"052690","company_name":"한전기술","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"NUCLEAR_EPC_ENGINEERING_PROJECT_SCOPE_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-NuclearEPCEngineeringProjectScopeMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_controlled_90D_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_project_scope_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Nuclear/EPC engineering project-scope proxy produced strong MFE with controlled early MAE. Later drawdown keeps Green strict and requires exact project scope, client, margin and working-capital evidence."}
{"row_type":"case","case_id":"C05_R11L88_026150_TUKSU_CIVIL_WORKS_THEME","symbol":"026150","company_name":"특수건설","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CIVIL_WORKS_INFRASTRUCTURE_THEME_WITHOUT_EPC_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CivilWorksInfrastructureThemeNoEPCMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_late_rebound_not_validation","current_profile_verdict":"current_profile_false_positive_if_civil_works_theme_promoted_without_contract_margin_bridge","price_source":"Songdaiki/stock-web","notes":"Civil-works/infrastructure theme spike had almost no forward MFE from the selected entry and then deep MAE. Late rebounds do not validate the original weak-bridge entry."}
{"row_type":"case","case_id":"C05_R11L88_028100_DONGA_GEOTECH_CIVIL_WORKS_THEME","symbol":"028100","company_name":"동아지질","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"GEOTECHNICAL_CIVIL_WORKS_THEME_WITHOUT_FRESH_CONTRACT_MARGIN_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-GeotechnicalCivilWorksThemeNoFreshContractMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_low_MFE_moderate_MAE_late_rebound_not_validation","current_profile_verdict":"current_profile_false_positive_if_geotechnical_theme_overcredited_without_contract_economics","price_source":"Songdaiki/stock-web","notes":"Geotechnical/civil works theme had low early MFE and moderate MAE; late spikes in Q4 should not validate the original entry without fresh contract, margin and cash bridge. Late share-count drift watch is retained before patching."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 052690 한전기술 — nuclear/EPC engineering project-scope bridge positive

Entry row: `2024-04-22 c=59200`.  
Observed path: entry-day low `55700`, 30D high `2024-05-23 h=73200`, 90D high `2024-07-18 h=98100`, and late-year low `2024-12-10 l=49250`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L88_C05_052690_20240422_STAGE2_NUCLEAR_EPC_SCOPE","case_id":"C05_R11L88_052690_KEPCO_ENGINEERING_NUCLEAR_EPC_SCOPE","symbol":"052690","company_name":"한전기술","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"NUCLEAR_EPC_ENGINEERING_PROJECT_SCOPE_MARGIN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-NuclearEPCEngineeringProjectScopeMarginBridge-Positive","trigger_date":"2024-04-22","entry_date":"2024-04-22","entry_price":59200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_nuclear_EPC_engineering_project_scope_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; nuclear engineering project-scope, client quality and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["project_scope_proxy","client_quality_proxy","EPC_engineering_backlog_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_contract_scope_pending","margin_clause_pending","milestone_billing_pending","working_capital_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.65,"MFE_90D_pct":65.71,"MFE_180D_pct":65.71,"MAE_30D_pct":-5.91,"MAE_90D_pct":-5.91,"MAE_180D_pct":-16.81,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":98100.0,"max_drawdown_low_date":"2024-12-10","max_drawdown_low":49250.0,"drawdown_after_peak_pct":-49.80,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_price_extension_and_late_drawdown_watch; Green requires exact project-scope/margin/cash evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_controlled_90D_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_project_scope_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"052690_2024-04-22_59200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 can allow Stage2/Yellow when EPC strength is tied to project scope, client quality, margin clauses, milestone billing and cash conversion. Green still requires exact source-grade evidence because late drawdown can be large."}
```

### 6.2 026150 특수건설 — civil-works infrastructure theme without EPC margin bridge

Entry row: `2024-01-30 c=9400`.  
Observed path: same-day high `9420`, drawdown through spring, low `2024-10-22 l=5250`, and late Q4 rebound that should not validate the original weak entry.

```jsonl
{"row_type":"trigger","trigger_id":"R11L88_C05_026150_20240130_STAGE2_FALSE_POSITIVE_CIVIL_WORKS_THEME","case_id":"C05_R11L88_026150_TUKSU_CIVIL_WORKS_THEME","symbol":"026150","company_name":"특수건설","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CIVIL_WORKS_INFRASTRUCTURE_THEME_WITHOUT_EPC_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-CivilWorksInfrastructureThemeNoEPCMarginBridge","trigger_date":"2024-01-30","entry_date":"2024-01-30","entry_price":9400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_civil_works_infrastructure_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; civil works/infrastructure theme treated as insufficient without EPC project scope, contract margin, milestone billing and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["civil_works_infra_theme","relative_strength_spike"],"stage3_evidence_fields":["EPC_project_scope_missing","contract_margin_bridge_missing","milestone_billing_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","late_rebound_not_entry_validation","contract_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/026/026150/2024.csv","profile_path":"atlas/symbol_profiles/026/026150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.21,"MFE_90D_pct":0.21,"MFE_180D_pct":0.21,"MAE_30D_pct":-16.81,"MAE_90D_pct":-21.17,"MAE_180D_pct":-44.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-30","peak_price":9420.0,"max_drawdown_low_date":"2024-10-22","max_drawdown_low":5250.0,"drawdown_after_peak_pct":-44.27,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"civil_works_theme_without_EPC_margin_cash_bridge_should_be_4B_watch_not_positive; late_rebound_not_entry_validation","four_b_evidence_type":["price_only","late_rebound_not_entry_validation","contract_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_late_rebound_not_validation","current_profile_verdict":"current_profile_false_positive_if_civil_works_theme_promoted_without_contract_margin_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"026150_2024-01-30_9400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 should not promote civil-works/infrastructure theme spikes without EPC scope, contract margin, milestone billing and cash bridge. Near-zero MFE and deep MAE require 4B-watch."}
```

### 6.3 028100 동아지질 — geotechnical/civil works theme without fresh contract margin bridge

Entry row: `2024-01-30 c=14980`.  
Observed path: same-day high `15620`, spring/summer drawdown, and Q4 theme spikes that should not validate the original weak-bridge entry.

```jsonl
{"row_type":"trigger","trigger_id":"R11L88_C05_028100_20240130_STAGE2_FALSE_POSITIVE_GEOTECH_CIVIL_WORKS","case_id":"C05_R11L88_028100_DONGA_GEOTECH_CIVIL_WORKS_THEME","symbol":"028100","company_name":"동아지질","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"GEOTECHNICAL_CIVIL_WORKS_THEME_WITHOUT_FRESH_CONTRACT_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-GeotechnicalCivilWorksThemeNoFreshContractMarginBridge","trigger_date":"2024-01-30","entry_date":"2024-01-30","entry_price":14980.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_geotechnical_civil_works_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; geotechnical/civil-works theme treated as insufficient without fresh contract scope, margin clause, execution and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["geotechnical_civil_works_theme","relative_strength_spike"],"stage3_evidence_fields":["fresh_contract_scope_missing","margin_clause_missing","execution_risk_control_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","late_rebound_not_entry_validation","data_quality_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028100/2024.csv","profile_path":"atlas/symbol_profiles/028/028100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.27,"MFE_90D_pct":4.27,"MFE_180D_pct":4.27,"MAE_30D_pct":-14.22,"MAE_90D_pct":-17.29,"MAE_180D_pct":-19.49,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-30","peak_price":15620.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":12060.0,"drawdown_after_peak_pct":-22.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"geotechnical_civil_works_theme_without_fresh_contract_margin_bridge_should_remain_watch; late_Q4_spikes_not_entry_validation","four_b_evidence_type":["price_only","late_rebound_not_entry_validation","fresh_contract_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_moderate_MAE_late_rebound_not_validation","current_profile_verdict":"current_profile_false_positive_if_geotechnical_theme_overcredited_without_contract_economics","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["late_2024_share_count_drift_watch_before_patch"],"corporate_action_window_status":"clean_for_2024_entry; late_2024_share_count_drift_watch","same_entry_group_id":"028100_2024-01-30_14980","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C05 should not equate civil-works theme strength with fresh EPC contract economics. Low MFE plus missing margin/cash bridge should stay Watch/4B-risk, and late spikes should not validate the original entry."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R11L88_052690_KEPCO_ENGINEERING_NUCLEAR_EPC_SCOPE","trigger_id":"R11L88_C05_052690_20240422_STAGE2_NUCLEAR_EPC_SCOPE","symbol":"052690","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C05 requires project scope, client quality, margin clause, milestone billing and cash bridge rather than EPC theme alone","raw_component_scores_before":{"project_scope_score":13,"client_quality_score":12,"contract_certainty_score":11,"margin_clause_score":10,"milestone_billing_score":9,"working_capital_score":7,"execution_risk_control":8,"relative_strength_score":12,"valuation_repricing_score":7,"theme_spike_risk":-3,"information_confidence":5},"weighted_score_before":71,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"project_scope_score":16,"client_quality_score":15,"contract_certainty_score":14,"margin_clause_score":13,"milestone_billing_score":11,"working_capital_score":9,"execution_risk_control":10,"relative_strength_score":13,"valuation_repricing_score":8,"theme_spike_risk":-2,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Project-scope/margin bridge plus strong MFE supports Yellow-watch; late drawdown and proxy-only evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R11L88_026150_TUKSU_CIVIL_WORKS_THEME","trigger_id":"R11L88_C05_026150_20240130_STAGE2_FALSE_POSITIVE_CIVIL_WORKS_THEME","symbol":"026150","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"civil-works theme without EPC margin and cash bridge should be blocked","raw_component_scores_before":{"project_scope_score":2,"client_quality_score":1,"contract_certainty_score":1,"margin_clause_score":0,"milestone_billing_score":0,"working_capital_score":0,"execution_risk_control":1,"relative_strength_score":10,"valuation_repricing_score":4,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"project_scope_score":0,"client_quality_score":0,"contract_certainty_score":0,"margin_clause_score":0,"milestone_billing_score":0,"working_capital_score":0,"execution_risk_control":0,"relative_strength_score":2,"valuation_repricing_score":1,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE convert civil-works theme into missing contract-margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C05_R11L88_028100_DONGA_GEOTECH_CIVIL_WORKS_THEME","trigger_id":"R11L88_C05_028100_20240130_STAGE2_FALSE_POSITIVE_GEOTECH_CIVIL_WORKS","symbol":"028100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"geotechnical/civil works theme without fresh contract economics should remain Watch","raw_component_scores_before":{"project_scope_score":2,"client_quality_score":1,"contract_certainty_score":1,"margin_clause_score":0,"milestone_billing_score":0,"working_capital_score":0,"execution_risk_control":1,"relative_strength_score":8,"valuation_repricing_score":3,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"project_scope_score":0,"client_quality_score":0,"contract_certainty_score":0,"margin_clause_score":0,"milestone_billing_score":0,"working_capital_score":0,"execution_risk_control":0,"relative_strength_score":2,"valuation_repricing_score":1,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Watch-Blocked","component_delta_explanation":"Low MFE and missing contract economics keep the original entry Watch/4B; later spikes do not validate the original row."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R11L88_C05_P0_CURRENT","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C05 needs explicit project-scope/margin/cash bridge and civil-works theme 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":23.4,"avg_MAE90_pct":-14.79,"avg_MFE180_pct":23.4,"avg_MAE180_pct":-26.82,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C05_project_scope_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R11L88_C05_P1_SECTOR_SPECIFIC","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P1_L1_EPC_project_scope_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 EPC/infra signals need project scope, client quality, contract certainty, margin clause, milestone billing or working-capital/cash bridge before Stage2-Actionable","changed_axes":["project_scope_required","margin_cash_bridge_required","civil_works_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_project_scope_client_contract_margin_milestone_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":23.4,"avg_MAE90_pct":-14.79,"avg_MFE180_pct":23.4,"avg_MAE180_pct":-26.82,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R11L88_C05_P2_CANONICAL","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P2_C05_project_scope_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C05 should reward project economics, not civil works price themes","changed_axes":["C05_project_scope_margin_cash_bridge_required","C05_civil_works_theme_local_4B_guard","C05_late_rebound_not_contract_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"project_scope_or_contract_certainty_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":23.4,"avg_MAE90_pct":-14.79,"avg_MFE180_pct":23.4,"avg_MAE180_pct":-26.82,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R11L88_C05_P3_COUNTEREXAMPLE_GUARD","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P3_C05_near_zero_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and MAE90<=-15 while project/margin/cash bridge is missing, block Yellow/Green and route to Watch/4B","changed_axes":["C05_near_zero_MFE_guardrail","C05_deep_MAE_4B_guardrail","C05_late_rebound_not_validation"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_MAE90_le_minus_15_with_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":23.4,"avg_MAE90_pct":-14.79,"avg_MFE180_pct":23.4,"avg_MAE180_pct":-26.82,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_SCOPE_BRIDGE_VS_CIVIL_WORKS_THEME","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":23.4,"avg_MAE90_pct":-14.79,"avg_MFE180_pct":23.4,"avg_MAE180_pct":-26.82,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE90_le_minus_15":0.67,"interpretation":"C05 needs bridge discipline. 한전기술 shows project-scope/margin bridge can produce large MFE, while 특수건설 and 동아지질 show civil-works/geotechnical price themes should not be promoted without fresh contract scope, margin, milestone billing and cash conversion."}
{"row_type":"stage_transition_summary","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"052690","trigger_type":"Stage2-Actionable-NuclearEPCEngineeringProjectScopeMarginBridge-Positive","entry_date":"2024-04-22","stage2_to_90D_outcome":"good_stage2_very_high_MFE_controlled_MAE","stage2_to_180D_outcome":"positive_EPC_project_scope_bridge_with_late_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when project scope, client quality, margin and milestone/cash bridge exists; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"026150","trigger_type":"Stage2-FalsePositive-CivilWorksInfrastructureThemeNoEPCMarginBridge","entry_date":"2024-01-30","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_high_MAE","stage2_to_180D_outcome":"failed_civil_works_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Civil works theme without EPC margin/cash bridge should stay Watch/4B-risk; late rebound is not entry validation."}
{"row_type":"stage_transition_summary","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"028100","trigger_type":"Stage2-FalsePositive-GeotechnicalCivilWorksThemeNoFreshContractMarginBridge","entry_date":"2024-01-30","stage2_to_90D_outcome":"weak_stage2_low_MFE","stage2_to_180D_outcome":"weak_original_entry_late_rebound_not_validation","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Geotechnical/civil works theme without fresh contract/margin bridge should remain Watch; late Q4 spikes should not validate the original entry."}
{"row_type":"residual_contribution","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","residual_type":"civil_works_infra_theme_overcredit_without_EPC_scope_margin_cash_bridge","contribution":"Adds two C05 local 4B/Watch civil-works counterexamples against one nuclear/EPC engineering project-scope positive, avoiding C05 top-covered and previous R11 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_NUCLEAR_ENGINEERING_PROJECT_SCOPE_MARGIN_BRIDGE_VS_CIVIL_WORKS_POLICY_THEME_BLOWOFF","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C05 now has non-top-symbol EPC engineering positive and two civil-works/geotechnical weak-bridge counterexamples; next R11 loops should exact-URL repair project scope, client quality, contract certainty, margin clause, milestone billing and working-capital evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_project_scope_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"052690 worked when project-scope/margin proxy was present; 026150 and 028100 failed or remained weak when only civil-works/geotechnical theme existed."}
{"row_type":"shadow_weight","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_civil_works_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Civil works rows showed near-zero/low MFE and meaningful MAE without non-price contract economics."}
{"row_type":"shadow_weight","round":"R11","loop":"88","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_late_rebound_not_contract_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"026150 and 028100 show Q4 price spikes should not retroactively validate original weak entries unless fresh contract-scope, margin and cash evidence is repaired."}
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
  - civil_works_infra_theme_overcredit
  - project_scope_bridge_missing
  - margin_clause_bridge_missing
  - milestone_billing_cash_bridge_missing
new_axis_proposed:
  - C05_project_scope_margin_cash_bridge_required_shadow_only
  - C05_civil_works_theme_local_4B_watch_guard_shadow_only
  - C05_late_rebound_not_contract_validation_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C05
  - full_4b_requires_non_price_evidence within C05
  - hard_4c_thesis_break_routes_to_4c within C05
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
`028100` has a late-2024 share-count drift watch in the selected price path, so the original 90D/180D weak-entry finding is usable, but any future production patch should exact-repair the price path and evidence URLs.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 028100 late-2024 share-count drift before patch
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
3. Confirm R11 / L1 / C05 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C05 top-covered symbols
   - previous R11 loop85 C02 symbols
   - previous R11 loop86 C03 symbols
   - previous R11 loop87 C04 symbols
6. Confirm rejected candidates:
   - 028050 was excluded because it was just used in R10 loop88 C30.
   - 001880 was excluded because the 2024 forward window ends too early.
   - 009410 was excluded because the 2024 path has suspension/reopening/corporate-action contamination.
7. Keep 028100 in data-quality watch before patch consideration.
8. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C05-scoped safe patch candidates:
   - C05_project_scope_margin_cash_bridge_required
   - C05_civil_works_theme_local_4B_watch_guard
   - C05_late_rebound_not_contract_validation_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R11
completed_loop = 88
next_round = R12
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R11/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C05_EPC_MEGA_CONTRACT_MARGIN_GAP.
```
