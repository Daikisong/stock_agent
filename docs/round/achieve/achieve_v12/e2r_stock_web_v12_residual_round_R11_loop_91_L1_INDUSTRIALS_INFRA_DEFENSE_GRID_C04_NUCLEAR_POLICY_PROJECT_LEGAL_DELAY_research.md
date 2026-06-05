# E2R Stock-Web v12 Residual Research — R11 Loop 91 / L1 / C04

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R11
loop: 91
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_O_AND_M_PROJECT_EXECUTION_BRIDGE_VS_IPO_SMR_POLICY_MAINTENANCE_VOCABULARY_DECAY
sector: industrials / infrastructure / nuclear / O&M / SMR / project approval / legal delay / maintenance service
output_file: e2r_stock_web_v12_residual_round_R11_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R10 loop 91`.

```text
scheduled_round = R11
scheduled_loop = 91
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```

R11 is the L1 policy / infrastructure / defense / grid lane.  
C04 is selected because R11 loop90 used C03 defense export backlog, and the L1 rotation now returns to nuclear policy / project / legal-delay residuals.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
rows = 12
symbols = 7
good/bad Stage2 = 5/3
4B/4C = 1/0
top-covered = 011700, 083650, 006910, 034020, 042370, 046120
```

This loop avoids the C04 top-covered list and recent L1 loop symbols:

```text
R11 loop86 C03: 012450, 010820, 013810
R11 loop87 C04: 051600, 032820, 094820
R11 loop88 C05: 052690, 026150, 028100
R11 loop89 C02: 229640, 199820, 006910
R11 loop90 C03: 272210, 095190, 218410
R1 loop89 C03: 064350, 099320, 214430
R1 loop90 C04: 130660, 105840, 019990
R1 loop91 C05: 100840, 028050, 037350
```

Candidate hygiene note:

```text
During this execution path, a stale R10/C30 file was accidentally generated and several construction/autoparts candidates were touched.
Those rows are not used in this R11/C04 output.
```

Selected symbols:

```text
126720, 457550, 036190
```

The selected pocket is:

```text
nuclear/power-plant O&M project execution and utilization bridge
vs
recent-listing SMR/nuclear-service price spike without project/legal/revenue bridge
vs
legacy maintenance-service vocabulary without fresh nuclear project approval and backlog conversion bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"126720","company_name":"수산인더스트리","profile_path":"atlas/symbol_profiles/126/126720.json","first_date":"2022-08-01","last_date":"2026-02-20","trading_day_count":868,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"457550","company_name":"우진엔텍","profile_path":"atlas/symbol_profiles/457/457550.json","first_date":"2024-01-24","last_date":"2026-02-20","trading_day_count":503,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Recent listing; selected 2024 entry has sufficient forward path but IPO/listing volatility requires data-quality watch before any production patch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"recent_listing_watch"}
{"row_type":"price_source_validation","symbol":"036190","company_name":"금화피에스시","profile_path":"atlas/symbol_profiles/036/036190.json","first_date":"2000-12-26","last_date":"2026-02-20","trading_day_count":6196,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"126720","trigger_type":"Stage2-Actionable-NuclearPowerPlantOMProjectExecutionBridge-Positive","entry_date":"2024-01-22","duplicate_status":"new C04 symbol/trigger/date combination outside top-covered and recent L1 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","trigger_type":"Stage2-FalsePositive-RecentListingSMRNuclearServiceSpikeNoProjectLegalRevenueBridge","entry_date":"2024-01-26","duplicate_status":"new C04 symbol/trigger/date combination outside top-covered and recent L1 loop symbols; recent-listing price-quality watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"036190","trigger_type":"Stage2-FalsePositive-LegacyPlantMaintenanceVocabularyNoFreshNuclearProjectBridge","entry_date":"2024-01-02","duplicate_status":"new C04 symbol/trigger/date combination outside top-covered and recent L1 loop symbols"}
```

## 4. Research question

C04 is not “원전 테마가 있다.”  
The useful nuclear-policy/project signal must prove the bridge from policy vocabulary to executable economics:

```text
project approval or legal milestone
O&M / maintenance contract visibility
plant utilization and outage schedule
regulated demand or mandated service scope
customer / operator visibility
project margin or service margin
working-capital discipline
cash collection
legal-delay or regulatory-risk containment
```

A nuclear policy headline without this bridge is a reactor schematic pinned to the wall. It has power on paper, but E2R needs the permit, operator, outage schedule, service order, margin ledger, and cash trail.

Residual question:

```text
Can C04 distinguish:
1. nuclear/power-plant O&M project execution bridge with strong MFE and controlled entry MAE,
2. recent-listing SMR/nuclear-service price spikes where project/legal/revenue bridge is not proven,
3. legacy plant-maintenance vocabulary where fresh nuclear project approval and backlog conversion are missing?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C04_R11L91_126720_SUSAN_NUCLEAR_OM_PROJECT","symbol":"126720","company_name":"수산인더스트리","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_POWER_PLANT_OM_PROJECT_EXECUTION_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-NuclearPowerPlantOMProjectExecutionBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE90_low_MAE_project_execution_bridge","current_profile_verdict":"current_profile_correct_if_project_approval_OM_contract_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Power-plant O&M / nuclear-service execution proxy produced high MFE90 with controlled MAE. Green still requires exact operator, contract, outage/service schedule, margin and cash evidence."}
{"row_type":"case","case_id":"C04_R11L91_457550_WOOJIN_ENTEC_RECENT_LISTING_SPIKE","symbol":"457550","company_name":"우진엔텍","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"RECENT_LISTING_SMR_NUCLEAR_SERVICE_SPIKE_WITHOUT_PROJECT_LEGAL_REVENUE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-RecentListingSMRNuclearServiceSpikeNoProjectLegalRevenueBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"counterexample_price_spike_high_MAE_recent_listing_no_project_bridge","current_profile_verdict":"current_profile_false_positive_if_recent_listing_nuclear_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Recent-listing nuclear/SMR-service spike had large early volatility and deep MAE. Without project approval, legal milestone, service revenue run-rate and cash bridge, it should remain Watch/4B and data-quality repair."}
{"row_type":"case","case_id":"C04_R11L91_036190_KEUMHWA_MAINTENANCE_NO_FRESH_PROJECT","symbol":"036190","company_name":"금화피에스시","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"LEGACY_PLANT_MAINTENANCE_VOCABULARY_WITHOUT_FRESH_NUCLEAR_PROJECT_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LegacyPlantMaintenanceVocabularyNoFreshNuclearProjectBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_low_MAE_no_fresh_project_bridge","current_profile_verdict":"current_profile_false_positive_if_maintenance_vocabulary_overcredited_as_nuclear_project","price_source":"Songdaiki/stock-web","notes":"Legacy plant-maintenance vocabulary had low MFE and modest MAE; stable cash service alone is not C04 nuclear project/legal-delay evidence without fresh project approval, operator scope or backlog conversion."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 126720 수산인더스트리 — nuclear / power-plant O&M project execution bridge

Entry row: `2024-01-22 c=19040`.  
Observed path: entry low `2024-01-22 l=17900`, staged rise to `2024-05-27 h=31600`, then post-peak drawdown but still above entry through the full window.

```jsonl
{"row_type":"trigger","trigger_id":"R11L91_C04_126720_20240122_STAGE2_NUCLEAR_OM_PROJECT","case_id":"C04_R11L91_126720_SUSAN_NUCLEAR_OM_PROJECT","symbol":"126720","company_name":"수산인더스트리","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_POWER_PLANT_OM_PROJECT_EXECUTION_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-NuclearPowerPlantOMProjectExecutionBridge-Positive","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":19040.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_power_plant_OM_nuclear_service_project_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; power-plant O&M service, nuclear-service scope, outage schedule, project execution and margin/cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["power_plant_OM_scope_proxy","nuclear_service_customer_proxy","outage_or_project_schedule_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_operator_contract_source_pending","project_or_maintenance_scope_pending","service_margin_source_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","post_peak_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/126/126720/2024.csv","profile_path":"atlas/symbol_profiles/126/126720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.86,"MFE_90D_pct":65.97,"MFE_180D_pct":65.97,"MAE_30D_pct":-5.99,"MAE_90D_pct":-5.99,"MAE_180D_pct":-5.99,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-27","peak_price":31600.0,"max_drawdown_low_date":"2024-01-22","max_drawdown_low":17900.0,"drawdown_after_peak_pct":-30.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.27,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_operator_contract_project_schedule_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","post_peak_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_low_MAE_project_execution_bridge","current_profile_verdict":"current_profile_correct_if_project_approval_OM_contract_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"126720_2024-01-22_19040","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C04 can allow Stage2/Yellow when nuclear/power-plant strength is tied to operator contract, project or outage schedule, O&M scope, service margin and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 457550 우진엔텍 — recent-listing SMR/nuclear-service spike without project/legal/revenue bridge

Entry row: `2024-01-26 c=31000`, shortly after listing.  
Observed path: high `2024-02-08 h=38250`, but also extreme low `2024-02-01 l=14760`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L91_C04_457550_20240126_STAGE2_FALSE_POSITIVE_RECENT_LISTING_NUCLEAR_SPIKE","case_id":"C04_R11L91_457550_WOOJIN_ENTEC_RECENT_LISTING_SPIKE","symbol":"457550","company_name":"우진엔텍","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"RECENT_LISTING_SMR_NUCLEAR_SERVICE_SPIKE_WITHOUT_PROJECT_LEGAL_REVENUE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;recent_listing_price_quality_stress_test","trigger_type":"Stage2-FalsePositive-RecentListingSMRNuclearServiceSpikeNoProjectLegalRevenueBridge","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":31000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_recent_listing_nuclear_service_SMR_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; recent-listing SMR/nuclear-service vocabulary treated as insufficient without project approval, legal milestone, operator contract, revenue run-rate and margin/cash bridge","evidence_source_type":"historical_public_listing_and_theme_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["recent_listing_nuclear_service_keyword","SMR_policy_vocabulary","relative_strength_spike"],"stage3_evidence_fields":["project_approval_missing","legal_milestone_missing","operator_contract_missing","revenue_margin_cash_bridge_missing"],"stage4b_evidence_fields":["recent_listing_watch","price_only_spike","extreme_MAE"],"stage4c_evidence_fields":["listing_volatility_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/457/457550/2024.csv","profile_path":"atlas/symbol_profiles/457/457550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.39,"MFE_90D_pct":23.39,"MFE_180D_pct":23.39,"MAE_30D_pct":-52.39,"MAE_90D_pct":-52.39,"MAE_180D_pct":-52.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-08","peak_price":38250.0,"max_drawdown_low_date":"2024-02-01","max_drawdown_low":14760.0,"drawdown_after_peak_pct":-61.41,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"recent_listing_nuclear_SMR_spike_without_project_legal_revenue_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["recent_listing_watch","price_only_spike","extreme_MAE"],"four_c_protection_label":"listing_volatility_watch_only","trigger_outcome_label":"counterexample_price_spike_high_MAE_recent_listing_no_project_bridge","current_profile_verdict":"current_profile_false_positive_if_recent_listing_nuclear_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["recent_listing_price_quality_watch"],"corporate_action_window_status":"recent_listing_2024-01-24; selected_entry_two_trading_days_after_listing","same_entry_group_id":"457550_2024-01-26_31000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C04 should not promote recent-listing nuclear/SMR vocabulary unless project approval, legal milestone, operator contract, revenue run-rate, margin and cash evidence are exact-repaired. Price-only IPO volatility routes to 4B/data-quality watch."}
```

### 6.3 036190 금화피에스시 — legacy plant-maintenance vocabulary without fresh nuclear project bridge

Entry row: `2024-01-02 c=26050`.  
Observed path: mild high `2024-03-18 h=28700`, later low `2024-12-09 l=23700`.

```jsonl
{"row_type":"trigger","trigger_id":"R11L91_C04_036190_20240102_STAGE2_FALSE_POSITIVE_LEGACY_PLANT_MAINTENANCE","case_id":"C04_R11L91_036190_KEUMHWA_MAINTENANCE_NO_FRESH_PROJECT","symbol":"036190","company_name":"금화피에스시","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"LEGACY_PLANT_MAINTENANCE_VOCABULARY_WITHOUT_FRESH_NUCLEAR_PROJECT_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;low_MFE_bridge_missing_stress_test","trigger_type":"Stage2-FalsePositive-LegacyPlantMaintenanceVocabularyNoFreshNuclearProjectBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":26050.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_plant_maintenance_power_service_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; legacy plant-maintenance vocabulary treated as insufficient C04 evidence without fresh nuclear project approval, operator/customer contract, legal milestone, backlog conversion and margin/cash bridge","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["plant_maintenance_vocabulary","power_service_keyword","stable_service_business_proxy"],"stage3_evidence_fields":["fresh_nuclear_project_approval_missing","operator_contract_missing","legal_milestone_missing","backlog_conversion_missing"],"stage4b_evidence_fields":["low_MFE_watch","project_bridge_missing_watch","no_policy_leverage_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036190/2024.csv","profile_path":"atlas/symbol_profiles/036/036190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.50,"MFE_90D_pct":10.17,"MFE_180D_pct":10.17,"MAE_30D_pct":-4.80,"MAE_90D_pct":-4.80,"MAE_180D_pct":-9.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-18","peak_price":28700.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":23700.0,"drawdown_after_peak_pct":-17.42,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.25,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"legacy_maintenance_vocabulary_without_fresh_nuclear_project_approval_or_legal_milestone_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE_watch","project_bridge_missing_watch","no_policy_leverage_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_low_MAE_no_fresh_project_bridge","current_profile_verdict":"current_profile_false_positive_if_maintenance_vocabulary_overcredited_as_nuclear_project","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"036190_2024-01-02_26050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C04 should not equate stable plant-maintenance vocabulary with nuclear project/legal-delay evidence. Fresh project approval, operator contract, legal milestone, backlog conversion and margin/cash bridge must be repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_R11L91_126720_SUSAN_NUCLEAR_OM_PROJECT","trigger_id":"R11L91_C04_126720_20240122_STAGE2_NUCLEAR_OM_PROJECT","symbol":"126720","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C04 requires project approval, legal milestone, O&M/operator contract, service schedule, margin and cash bridge rather than nuclear vocabulary alone","raw_component_scores_before":{"project_approval_score":10,"legal_milestone_score":8,"operator_contract_score":12,"OM_scope_score":13,"outage_schedule_score":11,"regulated_demand_score":8,"service_margin_score":10,"cash_conversion_score":7,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"project_approval_score":12,"legal_milestone_score":10,"operator_contract_score":15,"OM_scope_score":16,"outage_schedule_score":13,"regulated_demand_score":10,"service_margin_score":12,"cash_conversion_score":9,"relative_strength_score":15,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":87,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"O&M/project execution bridge plus high MFE90 supports Yellow/Green-candidate watch; exact operator/project/margin evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_R11L91_457550_WOOJIN_ENTEC_RECENT_LISTING_SPIKE","trigger_id":"R11L91_C04_457550_20240126_STAGE2_FALSE_POSITIVE_RECENT_LISTING_NUCLEAR_SPIKE","symbol":"457550","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_scope":"current_default_proxy","profile_hypothesis":"recent-listing nuclear/SMR price spike without project/legal bridge should be blocked","raw_component_scores_before":{"project_approval_score":1,"legal_milestone_score":0,"operator_contract_score":1,"OM_scope_score":2,"outage_schedule_score":0,"regulated_demand_score":1,"service_margin_score":0,"cash_conversion_score":0,"relative_strength_score":15,"valuation_repricing_score":5,"execution_risk_score":-20,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/RecentListingWatch","raw_component_scores_after":{"project_approval_score":0,"legal_milestone_score":0,"operator_contract_score":0,"OM_scope_score":1,"outage_schedule_score":0,"regulated_demand_score":0,"service_margin_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-32,"theme_spike_risk":-26,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Price spike is IPO/listing volatility; extreme MAE and missing project/legal bridge block Yellow/Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_R11L91_036190_KEUMHWA_MAINTENANCE_NO_FRESH_PROJECT","trigger_id":"R11L91_C04_036190_20240102_STAGE2_FALSE_POSITIVE_LEGACY_PLANT_MAINTENANCE","symbol":"036190","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_scope":"current_default_proxy","profile_hypothesis":"legacy plant-maintenance vocabulary without fresh nuclear project/legal bridge should remain Watch/4B even if downside is modest","raw_component_scores_before":{"project_approval_score":0,"legal_milestone_score":0,"operator_contract_score":2,"OM_scope_score":4,"outage_schedule_score":1,"regulated_demand_score":1,"service_margin_score":2,"cash_conversion_score":1,"relative_strength_score":3,"valuation_repricing_score":2,"execution_risk_score":-8,"theme_spike_risk":-10,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"project_approval_score":0,"legal_milestone_score":0,"operator_contract_score":1,"OM_scope_score":2,"outage_schedule_score":0,"regulated_demand_score":0,"service_margin_score":1,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-14,"theme_spike_risk":-12,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and missing project/legal bridge keep stable maintenance vocabulary out of Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R11L91_C04_P0_CURRENT","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C04 needs explicit project approval, legal milestone, operator contract, O&M scope, service schedule, margin/cash and recent-listing data-quality taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":33.18,"avg_MAE90_pct":-21.06,"avg_MFE180_pct":33.18,"avg_MAE180_pct":-22.47,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.51,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C04_project_legal_OM_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R11L91_C04_P1_SECTOR_SPECIFIC","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P1_L1_nuclear_project_OM_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 nuclear signals need project approval, legal milestone, operator/O&M contract, outage/service schedule, margin or cash conversion before Stage2-Actionable","changed_axes":["project_legal_required","operator_OM_contract_required","recent_listing_nuclear_spike_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_project_approval_legal_milestone_operator_contract_OM_scope_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":33.18,"avg_MAE90_pct":-21.06,"avg_MFE180_pct":33.18,"avg_MAE180_pct":-22.47,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R11L91_C04_P2_CANONICAL","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P2_C04_project_legal_OM_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C04 should reward project/legal/O&M execution mechanics, not nuclear/SMR or plant-maintenance vocabulary","changed_axes":["C04_project_legal_operator_OM_margin_cash_bridge_required","C04_recent_listing_SMR_spike_local_4B_guard","C04_maintenance_vocabulary_low_MFE_guard"],"changed_thresholds":{"stage2_yellow_gate":"project_or_operator_contract_plus_legal_or_OM_margin_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":33.18,"avg_MAE90_pct":-21.06,"avg_MFE180_pct":33.18,"avg_MAE180_pct":-22.47,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R11L91_C04_P3_COUNTEREXAMPLE_GUARD","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P3_C04_extreme_MAE_or_low_MFE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If project/legal/O&M bridge is missing, recent-listing price spikes or MFE90<15 should block Yellow/Green; MAE90<=-30 hard-routes to 4B/data-quality watch","changed_axes":["C04_recent_listing_price_quality_guard","C04_low_MFE_bridge_missing_guard","C04_extreme_MAE_4B_guard"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(recent_listing_watch_or_MFE90_lt_15_or_MAE90_le_minus_30)"},"eligible_trigger_count":3,"avg_MFE90_pct":33.18,"avg_MAE90_pct":-21.06,"avg_MFE180_pct":33.18,"avg_MAE180_pct":-22.47,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_NUCLEAR_OM_POSITIVE_VS_RECENT_LISTING_MAINTENANCE_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":33.18,"avg_MAE90_pct":-21.06,"avg_MFE180_pct":33.18,"avg_MAE180_pct":-22.47,"stage2_hit_rate_MFE90_ge20":0.67,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE90_le_minus30":0.33,"interpretation":"C04 needs bridge discipline. 수산인더스트리 shows nuclear/power-plant O&M project execution can support Yellow/Green-candidate-watch, while 우진엔텍 and 금화피에스시 show recent-listing nuclear spikes or legacy maintenance vocabulary should not be promoted without project approval, legal milestone, operator contract, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"126720","trigger_type":"Stage2-Actionable-NuclearPowerPlantOMProjectExecutionBridge-Positive","entry_date":"2024-01-22","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_OM_project_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when nuclear strength is tied to operator contract, O&M/project schedule, service margin and cash bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","trigger_type":"Stage2-FalsePositive-RecentListingSMRNuclearServiceSpikeNoProjectLegalRevenueBridge","entry_date":"2024-01-26","stage2_to_90D_outcome":"bad_stage2_price_spike_extreme_MAE_recent_listing_watch","stage2_to_180D_outcome":"failed_recent_listing_nuclear_spike_no_project_bridge","MFE90_ge20":true,"MAE90_le_minus30":true,"transition_note":"Recent-listing nuclear/SMR spike without project/legal/revenue bridge should be Watch/4B and data-quality repair, not Stage2/Yellow."}
{"row_type":"stage_transition_summary","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"036190","trigger_type":"Stage2-FalsePositive-LegacyPlantMaintenanceVocabularyNoFreshNuclearProjectBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"weak_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"stable_but_not_nuclear_project_validation","MFE90_ge20":false,"MAE180_le_minus20":false,"transition_note":"Stable plant-maintenance vocabulary without fresh nuclear project approval or legal milestone should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","residual_type":"recent_listing_SMR_and_legacy_maintenance_vocabulary_overcredit_without_project_legal_OM_margin_cash_bridge","contribution":"Adds two C04 4B counterexamples against one nuclear/power-plant O&M project-execution positive, avoiding C04 top-covered and recent L1 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_O_AND_M_PROJECT_EXECUTION_BRIDGE_VS_IPO_SMR_POLICY_MAINTENANCE_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C04 now has non-top-symbol nuclear O&M project-execution positive and two recent-listing/legacy-maintenance weak-bridge counterexamples; next R11 C04 loops should exact-URL repair project approval, legal milestone, operator contract, O&M scope, outage schedule, service margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"C04_project_legal_operator_OM_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"126720 worked when O&M/project execution proxy existed; 457550 and 036190 failed as C04 positives when project/legal/operator/margin evidence was missing."}
{"row_type":"shadow_weight","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"C04_recent_listing_SMR_spike_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"457550 shows recent-listing nuclear/SMR price spikes can produce high MFE and extreme MAE without project bridge; block Yellow/Green until exact evidence and data quality are repaired."}
{"row_type":"shadow_weight","round":"R11","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"C04_maintenance_vocabulary_low_MFE_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"036190 shows stable plant-maintenance vocabulary is not enough for C04 unless fresh nuclear project approval, operator scope and legal milestone are repaired."}
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
  - nuclear_policy_vocabulary_overcredit
  - recent_listing_SMR_price_spike_overcredit
  - legacy_plant_maintenance_vocabulary_overcredit
  - project_approval_legal_milestone_missing
  - operator_contract_margin_cash_bridge_missing
new_axis_proposed:
  - C04_project_legal_operator_OM_margin_cash_bridge_required_shadow_only
  - C04_recent_listing_SMR_spike_local_4B_guard_shadow_only
  - C04_maintenance_vocabulary_low_MFE_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows.  
`126720` and `036190` have clean selected 2024 windows.  
`457550` is a 2024 recent listing, so it is usable for research but should remain data-quality watch before any production patching.  
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
recent_listing_watch = true for 457550
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
   - previous R11 loop86 C03 symbols
   - previous R11 loop87 C04 symbols
   - previous R11 loop88 C05 symbols
   - previous R11 loop89 C02 symbols
   - previous R11 loop90 C03 symbols
   - previous R1 loop89 C03 symbols
   - previous R1 loop90 C04 symbols
   - previous R1 loop91 C05 symbols
6. Confirm accidentally generated R10/C30 and touched construction/autoparts candidates are not ingested from this MD.
7. Keep 457550 in recent-listing data-quality watch before patch consideration.
8. If aggregate support remains stable after exact evidence URL repair, consider C04-scoped safe patch candidates:
   - C04_project_legal_operator_OM_margin_cash_bridge_required
   - C04_recent_listing_SMR_spike_local_4B_guard
   - C04_maintenance_vocabulary_low_MFE_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R11
completed_loop = 91
next_round = R12
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R11/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.
```
