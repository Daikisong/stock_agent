# E2R Stock-Web v12 Residual Research — R1 Loop 85 / L1 / C04

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R1
loop: 85
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: NUCLEAR_ENGINEERING_PROJECT_BRIDGE_VS_SMALLCAP_POLICY_THEME_AND_LEGAL_DELAY_RISK
sector: industrials / infra / nuclear policy / project / legal-delay
output_file: e2r_stock_web_v12_residual_round_R1_loop_85_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after the completed `R13 loop 84` cross-review.

```text
scheduled_round = R1
scheduled_loop = 85
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```

R1 is restricted to L1 industrials / infra / defense / grid.  
C04 is selected because it remains thinner than the larger R1 buckets and because the previous R1 loop85 should not simply repeat EPC or defense-export evidence. The selected symbols avoid the C04 top-covered list in the No-Repeat Index:

```text
011700, 083650, 006910, 034020, 042370, 046120
```

This is not a live stock recommendation, not a `stock_agent` patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"052690","company_name":"한전기술","profile_path":"atlas/symbol_profiles/052/052690.json","first_date":"2009-12-14","last_date":"2026-02-20","trading_day_count":3984,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_2025_forward_window"}
{"row_type":"price_source_validation","symbol":"105840","company_name":"우진","profile_path":"atlas/symbol_profiles/105/105840.json","first_date":"2010-07-26","last_date":"2026-02-20","trading_day_count":3832,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2012-11-19","2012-12-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"094820","company_name":"일진파워","profile_path":"atlas/symbol_profiles/094/094820.json","first_date":"2007-11-06","last_date":"2026-02-20","trading_day_count":4483,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2011-09-08","2011-09-30"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced here:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"052690","trigger_type":"Stage2-Actionable-NuclearEngineeringProjectBridge-Positive","entry_date":"2024-04-29","duplicate_status":"new C04 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"105840","trigger_type":"Stage2-FalsePositive-NuclearInstrumentTheme-NoProjectBridge","entry_date":"2024-01-15","duplicate_status":"new C04 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"094820","trigger_type":"Stage2-FalsePositive-NuclearMaintenanceTheme-NoLegalProjectBridge","entry_date":"2024-04-05","duplicate_status":"new C04 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C04 is not “nuclear theme up.” It is the bridge between policy tailwind and actual project conversion. A nuclear-policy move only becomes E2R-relevant when the project path, engineering scope, order visibility, regulatory/legal timing, and margin bridge line up. If the policy headline runs ahead of that bridge, the forward path often becomes a local-peak / high-MAE trap.

Residual question:

```text
Can C04 distinguish:
1. nuclear engineering/project bridge with sustained MFE,
2. nuclear instrument/smallcap theme spike without verified project bridge,
3. nuclear maintenance/service theme spike where policy interest does not convert into legal/project/margin bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C04_R1L85_052690_KEPCO_ENGINEERING_PROJECT_BRIDGE","symbol":"052690","company_name":"한전기술","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_ENGINEERING_PROJECT_BRIDGE_WITH_POLICY_TAILWIND","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-NuclearEngineeringProjectBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_project_bridge_required","price_source":"Songdaiki/stock-web","notes":"Nuclear engineering/project bridge produced strong MFE after April entry; Green still requires exact project/legal/margin evidence."}
{"row_type":"case","case_id":"C04_R1L85_105840_WOOJIN_NUCLEAR_INSTRUMENT_THEME_NO_BRIDGE","symbol":"105840","company_name":"우진","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_INSTRUMENT_THEME_SPIKE_WITHOUT_PROJECT_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-NuclearInstrumentTheme-NoProjectBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Nuclear-instrument theme spike had small MFE and high MAE without confirmed project or margin bridge."}
{"row_type":"case","case_id":"C04_R1L85_094820_ILJIN_POWER_NUCLEAR_MAINTENANCE_THEME","symbol":"094820","company_name":"일진파워","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_MAINTENANCE_THEME_WITHOUT_LEGAL_PROJECT_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-NuclearMaintenanceTheme-NoLegalProjectBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_modest_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_service_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Nuclear maintenance/service theme showed a modest bounce but later deep drawdown without legal/project/margin confirmation."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 052690 한전기술 — nuclear engineering/project bridge positive

Entry row: `2024-04-29 c=65400`.  
Forward path: `2024-05-27 h=74200`, `2024-07-18 h=98100`, later low `2024-12-09 l=49900`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L85_C04_052690_20240429_STAGE2_NUCLEAR_ENGINEERING_PROJECT_BRIDGE","case_id":"C04_R1L85_052690_KEPCO_ENGINEERING_PROJECT_BRIDGE","symbol":"052690","company_name":"한전기술","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_ENGINEERING_PROJECT_BRIDGE_WITH_POLICY_TAILWIND","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-NuclearEngineeringProjectBridge-Positive","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":65400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_nuclear_engineering_project_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; nuclear engineering/project and policy tailwind treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["nuclear_policy_tailwind","engineering_project_bridge_proxy","relative_strength_turn"],"stage3_evidence_fields":["legal_or_regulatory_timing_pending","margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.46,"MFE_90D_pct":50.0,"MFE_180D_pct":50.0,"MAE_30D_pct":-5.5,"MAE_90D_pct":-5.81,"MAE_180D_pct":-23.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":98100.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":49900.0,"drawdown_after_peak_pct":-49.13,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_project_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"052690_2024-04-29_65400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C04 should allow Stage2/Yellow when nuclear policy is tied to engineering/project bridge. Green still requires exact project, legal/regulatory and margin evidence."}
```

### 6.2 105840 우진 — nuclear instrument theme without project bridge

Entry row: `2024-01-15 c=10050`.  
Forward path: local high `2024-01-24 h=10500`, then lows `2024-02-01 l=8050`, `2024-04-11 l=7720`, and `2024-08-05 l=7120`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L85_C04_105840_20240115_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENT_THEME","case_id":"C04_R1L85_105840_WOOJIN_NUCLEAR_INSTRUMENT_THEME_NO_BRIDGE","symbol":"105840","company_name":"우진","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_INSTRUMENT_THEME_SPIKE_WITHOUT_PROJECT_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-NuclearInstrumentTheme-NoProjectBridge","trigger_date":"2024-01-15","entry_date":"2024-01-15","entry_price":10050.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_nuclear_instrument_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; nuclear instrument theme treated as insufficient without project/order/margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["nuclear_theme_relative_strength","instrument_supplier_keyword_proxy"],"stage3_evidence_fields":["project_bridge_missing","order_visibility_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv","profile_path":"atlas/symbol_profiles/105/105840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.48,"MFE_90D_pct":4.48,"MFE_180D_pct":8.96,"MAE_30D_pct":-19.9,"MAE_90D_pct":-23.18,"MAE_180D_pct":-29.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":10950.0,"max_drawdown_low_date":"2024-08-05","max_drawdown_low":7120.0,"drawdown_after_peak_pct":-34.98,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"theme_local_peak_without_project_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"105840_2024-01-15_10050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C04 small-cap nuclear-instrument theme without project/order bridge generated low MFE and high MAE. Require project/legal/order evidence before Stage2-Actionable/Yellow."}
```

### 6.3 094820 일진파워 — nuclear maintenance/service theme without legal/project bridge

Entry row: `2024-04-05 c=13520`.  
Forward path: rebound high `2024-05-28 h=15140`, then lows `2024-10-02 l=9030` and `2024-12-09 l=6900`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L85_C04_094820_20240405_STAGE2_FALSE_POSITIVE_NUCLEAR_MAINTENANCE_THEME","case_id":"C04_R1L85_094820_ILJIN_POWER_NUCLEAR_MAINTENANCE_THEME","symbol":"094820","company_name":"일진파워","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_MAINTENANCE_THEME_WITHOUT_LEGAL_PROJECT_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-NuclearMaintenanceTheme-NoLegalProjectBridge","trigger_date":"2024-04-05","entry_date":"2024-04-05","entry_price":13520.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_nuclear_service_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; nuclear maintenance/service theme treated as insufficient without legal/project/order and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["nuclear_policy_tailwind","maintenance_service_theme"],"stage3_evidence_fields":["legal_project_bridge_missing","order_visibility_missing","margin_bridge_missing"],"stage4b_evidence_fields":["theme_fade_watch","price_only_local_peak"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/094/094820/2024.csv","profile_path":"atlas/symbol_profiles/094/094820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.98,"MFE_90D_pct":11.98,"MFE_180D_pct":11.98,"MAE_30D_pct":-18.2,"MAE_90D_pct":-18.2,"MAE_180D_pct":-48.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":15140.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":6900.0,"drawdown_after_peak_pct":-54.43,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"service_theme_rebound_without_legal_project_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_modest_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_service_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"094820_2024-04-05_13520","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C04 should distinguish a project bridge from a service/theme rebound. Without legal/project/margin bridge, modest MFE decayed into deep 180D MAE."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_R1L85_052690_KEPCO_ENGINEERING_PROJECT_BRIDGE","trigger_id":"R1L85_C04_052690_20240429_STAGE2_NUCLEAR_ENGINEERING_PROJECT_BRIDGE","symbol":"052690","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C04 requires project/legal/margin bridge rather than policy keyword alone","raw_component_scores_before":{"policy_tailwind_score":15,"project_bridge_score":14,"legal_regulatory_timing_score":9,"order_visibility_score":9,"margin_bridge_score":8,"relative_strength_score":12,"valuation_repricing_score":8,"execution_or_delay_risk":-6,"theme_spike_risk":-3,"information_confidence":5},"weighted_score_before":71,"stage_label_before":"Stage2-Watch/Yellow-candidate","raw_component_scores_after":{"policy_tailwind_score":17,"project_bridge_score":17,"legal_regulatory_timing_score":11,"order_visibility_score":11,"margin_bridge_score":10,"relative_strength_score":13,"valuation_repricing_score":9,"execution_or_delay_risk":-5,"theme_spike_risk":-2,"information_confidence":6},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Engineering/project bridge and high MFE support Yellow-watch; exact legal/regulatory and margin evidence still block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_R1L85_105840_WOOJIN_NUCLEAR_INSTRUMENT_THEME_NO_BRIDGE","trigger_id":"R1L85_C04_105840_20240115_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENT_THEME","symbol":"105840","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_scope":"current_default_proxy","profile_hypothesis":"nuclear instrument theme without project/order bridge should be blocked","raw_component_scores_before":{"policy_tailwind_score":11,"project_bridge_score":2,"legal_regulatory_timing_score":2,"order_visibility_score":1,"margin_bridge_score":1,"relative_strength_score":12,"valuation_repricing_score":6,"execution_or_delay_risk":-12,"theme_spike_risk":-13,"information_confidence":3},"weighted_score_before":29,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"policy_tailwind_score":7,"project_bridge_score":0,"legal_regulatory_timing_score":0,"order_visibility_score":0,"margin_bridge_score":0,"relative_strength_score":5,"valuation_repricing_score":2,"execution_or_delay_risk":-18,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and high MAE convert the theme signal into evidence-quality failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C04_R1L85_094820_ILJIN_POWER_NUCLEAR_MAINTENANCE_THEME","trigger_id":"R1L85_C04_094820_20240405_STAGE2_FALSE_POSITIVE_NUCLEAR_MAINTENANCE_THEME","symbol":"094820","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_scope":"current_default_proxy","profile_hypothesis":"nuclear maintenance/service rebound without legal/project bridge should stay Watch/4B-risk","raw_component_scores_before":{"policy_tailwind_score":12,"project_bridge_score":3,"legal_regulatory_timing_score":2,"order_visibility_score":2,"margin_bridge_score":2,"relative_strength_score":11,"valuation_repricing_score":7,"execution_or_delay_risk":-10,"theme_spike_risk":-11,"information_confidence":3},"weighted_score_before":39,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"policy_tailwind_score":8,"project_bridge_score":1,"legal_regulatory_timing_score":0,"order_visibility_score":0,"margin_bridge_score":0,"relative_strength_score":6,"valuation_repricing_score":3,"execution_or_delay_risk":-16,"theme_spike_risk":-17,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Modest initial MFE cannot offset deep 180D MAE and missing legal/project/margin bridge."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R1L85_C04_P0_CURRENT","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C04 needs explicit project/legal/margin bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":22.15,"avg_MAE90_pct":-15.73,"avg_MFE180_pct":23.65,"avg_MAE180_pct":-33.94,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C04_project_legal_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R1L85_C04_P1_SECTOR_SPECIFIC","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P1_L1_nuclear_project_legal_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 nuclear policy signals need project, legal/regulatory, order or margin bridge before Stage2-Actionable","changed_axes":["project_bridge_required","legal_regulatory_timing_required","theme_spike_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_project_legal_order_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":22.15,"avg_MAE90_pct":-15.73,"avg_MFE180_pct":23.65,"avg_MAE180_pct":-33.94,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R1L85_C04_P2_CANONICAL","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P2_C04_project_legal_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C04 should reward real project/legal bridge, not nuclear small-cap theme spikes","changed_axes":["C04_project_legal_bridge_required","C04_smallcap_theme_spike_penalty","C04_legal_delay_watch_guard"],"changed_thresholds":{"stage2_yellow_gate":"project_legal_or_order_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":22.15,"avg_MAE90_pct":-15.73,"avg_MFE180_pct":23.65,"avg_MAE180_pct":-33.94,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R1L85_C04_P3_COUNTEREXAMPLE_GUARD","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","profile_id":"P3_C04_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<15 and MAE180<=-25 while project/legal bridge is missing, block Yellow/Green","changed_axes":["C04_high_MAE_guardrail","C04_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_15_and_MAE180_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":22.15,"avg_MAE90_pct":-15.73,"avg_MFE180_pct":23.65,"avg_MAE180_pct":-33.94,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_NUCLEAR_PROJECT_BRIDGE_VS_POLICY_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":22.15,"avg_MAE90_pct":-15.73,"avg_MFE180_pct":23.65,"avg_MAE180_pct":-33.94,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_15":0.67,"stage2_bad_entry_rate_MAE180_le_minus_25":0.67,"interpretation":"C04 needs bridge discipline. 052690 shows a true nuclear engineering/project bridge, while 105840 and 094820 show small-cap nuclear theme or service rebounds that fail without project/legal/order/margin conversion."}
{"row_type":"stage_transition_summary","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"052690","trigger_type":"Stage2-Actionable-NuclearEngineeringProjectBridge-Positive","entry_date":"2024-04-29","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_project_rerating_with_later_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when engineering/project bridge exists; Green requires exact legal/regulatory and margin evidence."}
{"row_type":"stage_transition_summary","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"105840","trigger_type":"Stage2-FalsePositive-NuclearInstrumentTheme-NoProjectBridge","entry_date":"2024-01-15","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_entry_high_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Nuclear instrument theme without project/order bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"094820","trigger_type":"Stage2-FalsePositive-NuclearMaintenanceTheme-NoLegalProjectBridge","entry_date":"2024-04-05","stage2_to_90D_outcome":"weak_stage2_modest_MFE","stage2_to_180D_outcome":"failed_entry_deep_180D_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Nuclear service/theme rebound without legal/project/margin bridge should stay Watch; deep 180D MAE supports local guard."}
{"row_type":"residual_contribution","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","residual_type":"nuclear_policy_theme_overcredit_without_project_legal_margin_bridge","contribution":"Adds two C04 local 4B/high-MAE counterexamples against one engineering/project bridge positive, avoiding C04 top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_ENGINEERING_PROJECT_BRIDGE_VS_SMALLCAP_POLICY_THEME_AND_LEGAL_DELAY_RISK","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C04 now has non-top-symbol nuclear theme counterexamples; next R1 loops should exact-URL repair nuclear project, legal-delay, and order/margin evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"C04_project_legal_order_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"052690 worked with project/engineering bridge proxy; 105840 and 094820 failed when project/legal/order bridge was missing."}
{"row_type":"shadow_weight","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"C04_smallcap_nuclear_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Small-cap nuclear instrument/service theme spikes showed low or modest MFE and high/deep MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R1","loop":"85","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","axis":"C04_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<15 and MAE180<=-25 while project/legal bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - smallcap_nuclear_theme_no_project_bridge
  - service_maintenance_theme_no_legal_project_margin_bridge
new_axis_proposed:
  - C04_project_legal_order_bridge_required_shadow_only
  - C04_smallcap_nuclear_theme_local_4B_watch_guard_shadow_only
  - C04_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C04
  - full_4b_requires_non_price_evidence within C04
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
3. Confirm R1 / L1 / C04 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C04 top-covered symbols.
6. If aggregate support remains stable after exact evidence URL repair, consider C04-scoped safe patch candidates:
   - C04_project_legal_order_bridge_required
   - C04_smallcap_nuclear_theme_local_4B_watch_guard
   - C04_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R1
completed_loop = 85
next_round = R2
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.
```
