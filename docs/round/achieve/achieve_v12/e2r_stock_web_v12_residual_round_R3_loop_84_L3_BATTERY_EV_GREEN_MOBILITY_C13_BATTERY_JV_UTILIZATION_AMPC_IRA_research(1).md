# E2R Stock-Web v12 Residual Research — R3 Loop 84 / L3 / C13

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 84
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: AMPC_JV_UTILIZATION_BRIDGE_VS_POLICY_CREDIT_AND_HOLDCO_DISCOUNT_FALSE_POSITIVE
sector: battery / EV / green mobility / JV-utilization-AMPC-IRA
output_file: e2r_stock_web_v12_residual_round_R3_loop_84_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R2 loop 84`.

```text
scheduled_round = R3
scheduled_loop = 84
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

R3 is restricted to L3 battery / EV / green mobility.  
C13 is selected because the No-Repeat ledger shows C13 already has many positive Stage2 rows but relatively thin bad-stage coverage. The objective is therefore not to prove the broad battery-cycle rule again, but to test a C13-local bridge:

```text
AMPC / IRA / JV optionality is only Stage2-Actionable when utilization, shipment, customer call-off quality, and margin/FCF bridge are visible.
```

This is not a live recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"373220","company_name":"LG에너지솔루션","profile_path":"atlas/symbol_profiles/373/373220.json","first_date":"2022-01-27","last_date":"2026-02-20","trading_day_count":992,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_2025_forward_window"}
{"row_type":"price_source_validation","symbol":"361610","company_name":"SK아이이테크놀로지","profile_path":"atlas/symbol_profiles/361/361610.json","first_date":"2021-05-11","last_date":"2026-02-20","trading_day_count":1171,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"051910","company_name":"LG화학","profile_path":"atlas/symbol_profiles/051/051910.json","first_date":"2001-04-25","last_date":"2026-02-20","trading_day_count":6110,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
For C13, the top-covered symbols are `005070`, `020150`, `003670`, `025900`, `348370`, and `002710`. This loop avoids that repeated set.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"373220","trigger_type":"Stage2-Actionable-AMPC-JV-UtilizationBridge-Positive","entry_date":"2024-08-21","duplicate_status":"new C13 symbol/trigger/date combination"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"361610","trigger_type":"Stage2-FalsePositive-SeparatorUtilizationShortfall-NoAMPCBridge","entry_date":"2024-03-19","duplicate_status":"new C13 symbol/trigger/date combination"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"051910","trigger_type":"Stage2-FalsePositive-HoldcoBatteryJVAMPC-DiscountNoFCFBridge","entry_date":"2024-02-16","duplicate_status":"new C13 symbol/trigger/date combination"}
```

## 4. Research question

C13 is not “battery policy is good.” It is the bridge test between a subsidy/policy/JV label and the actual economic furnace: utilization, shipment, AMPC recognition quality, margin bridge, and FCF conversion.

Residual question:

```text
Can C13 distinguish:
1. battery cell leader where AMPC/JV/utilization optionality becomes a tradable rerating path,
2. separator utilization shortfall where EV/JV optionality never becomes order/margin bridge,
3. battery holding-company / JV / AMPC exposure where valuation discount and FCF drag overwhelm the policy narrative?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C13_R3L84_373220_LGES_AMPC_JV_UTILIZATION_BRIDGE","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CELL_LEADER_AMPC_JV_UTILIZATION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-AMPC-JV-UtilizationBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_moderate_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_utilization_bridge_required","price_source":"Songdaiki/stock-web","notes":"AMPC/JV optionality worked only after price and utilization/recovery proxy aligned. Green remains blocked without exact evidence URL and FCF bridge."}
{"row_type":"case","case_id":"C13_R3L84_361610_SKIET_SEPARATOR_UTILIZATION_SHORTFALL","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SEPARATOR_UTILIZATION_SHORTFALL_NO_CUSTOMER_CALL_OFF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SeparatorUtilizationShortfall-NoAMPCBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive_if_EV_JV_optionality_overcredited","price_source":"Songdaiki/stock-web","notes":"Separator/JV optionality did not overcome utilization and customer call-off risk; forward path had deep MAE."}
{"row_type":"case","case_id":"C13_R3L84_051910_LGCHEM_HOLDCO_BATTERY_JV_DISCOUNT","symbol":"051910","company_name":"LG화학","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"HOLDCO_BATTERY_JV_AMPC_OPTIONALITY_WITH_FCF_DISCOUNT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-HoldcoBatteryJVAMPC-DiscountNoFCFBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_optionalities_overcredited","price_source":"Songdaiki/stock-web","notes":"Battery exposure and AMPC/JV optionality were not enough when holding-company discount, chemicals drag, and FCF bridge were weak."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 373220 LG에너지솔루션 — AMPC/JV/utilization bridge positive

Entry row: `2024-08-21 c=350000`.  
Forward path: `2024-09-30 h=430000` within 30D, `2024-10-08 h=444000` as full-window peak, and clean corporate-action profile.

```jsonl
{"row_type":"trigger","trigger_id":"R3L84_C13_373220_20240821_STAGE2_AMPC_JV_UTILIZATION_BRIDGE","case_id":"C13_R3L84_373220_LGES_AMPC_JV_UTILIZATION_BRIDGE","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CELL_LEADER_AMPC_JV_UTILIZATION_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-AMPC-JV-UtilizationBridge-Positive","trigger_date":"2024-08-21","entry_date":"2024-08-21","entry_price":350000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_AMPC_JV_utilization_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; AMPC/JV/utilization recovery used as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["AMPC_or_IRA_optionalities","JV_utilization_proxy","relative_strength_turn"],"stage3_evidence_fields":["shipment_bridge_proxy","margin_bridge_pending","FCF_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.86,"MFE_90D_pct":26.86,"MFE_180D_pct":26.86,"MAE_30D_pct":-5.14,"MAE_90D_pct":-5.14,"MAE_180D_pct":-11.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000.0,"max_drawdown_low_date":"2025-04-03","max_drawdown_low":310500.0,"drawdown_after_peak_pct":-30.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_moderate_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_utilization_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"373220_2024-08-21_350000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C13 can allow Stage2/Yellow when policy optionality is tied to actual utilization and shipment bridge. Still, Green should require exact URL, margin bridge, and FCF conversion."}
```

### 6.2 361610 SK아이이테크놀로지 — separator utilization shortfall counterexample

Entry row: `2024-03-19 c=76800`.  
Upside stalled almost immediately at `2024-03-26 h=77700`, while later lows reached `2024-07-17 l=40200` and `2024-12-09 l=22650`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L84_C13_361610_20240319_STAGE2_FALSE_POSITIVE_SEPARATOR_UTILIZATION","case_id":"C13_R3L84_361610_SKIET_SEPARATOR_UTILIZATION_SHORTFALL","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SEPARATOR_UTILIZATION_SHORTFALL_NO_CUSTOMER_CALL_OFF_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SeparatorUtilizationShortfall-NoAMPCBridge","trigger_date":"2024-03-19","entry_date":"2024-03-19","entry_price":76800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_EV_separator_policy_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; separator/JV optionality treated as insufficient without utilization/customer call-off bridge","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["EV_policy_optionalities","relative_strength_rebound"],"stage3_evidence_fields":["utilization_bridge_missing","customer_call_off_quality_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","thesis_break_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv","profile_path":"atlas/symbol_profiles/361/361610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.17,"MFE_90D_pct":1.17,"MFE_180D_pct":1.17,"MAE_30D_pct":-23.18,"MAE_90D_pct":-47.66,"MAE_180D_pct":-70.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":77700.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":22650.0,"drawdown_after_peak_pct":-70.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_peak_without_utilization_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive_if_EV_JV_optionality_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"361610_2024-03-19_76800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C13 policy/JV optionality can be a trap when utilization and customer call-off bridge are missing. High MAE argues for a local utilization guard."}
```

### 6.3 051910 LG화학 — battery holding/JV optionality without FCF bridge

Entry row: `2024-02-16 c=504000`.  
A brief rebound peaked at `2024-02-19 h=520000`, then the path deteriorated to `2024-11-15 l=267500` and later `2024-12-09 l=246000`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L84_C13_051910_20240216_STAGE2_FALSE_POSITIVE_HOLDCO_AMPC_JV_DISCOUNT","case_id":"C13_R3L84_051910_LGCHEM_HOLDCO_BATTERY_JV_DISCOUNT","symbol":"051910","company_name":"LG화학","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"HOLDCO_BATTERY_JV_AMPC_OPTIONALITY_WITH_FCF_DISCOUNT","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-HoldcoBatteryJVAMPC-DiscountNoFCFBridge","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":504000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_JV_holding_discount_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; battery/JV/AMPC exposure treated as insufficient when holdco discount, chemicals drag, and FCF bridge are unresolved","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["battery_JV_exposure","AMPC_or_IRA_optionalities","relative_strength_rebound"],"stage3_evidence_fields":["FCF_bridge_missing","holding_company_discount_unresolved","chemicals_drag_unresolved","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv","profile_path":"atlas/symbol_profiles/051/051910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.17,"MFE_90D_pct":3.17,"MFE_180D_pct":3.17,"MAE_30D_pct":-14.68,"MAE_90D_pct":-30.56,"MAE_180D_pct":-46.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":520000.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":267500.0,"drawdown_after_peak_pct":-48.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_peak_without_FCF_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_policy_optionalities_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"051910_2024-02-16_504000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C13 should penalize battery holding/JV optionality when FCF conversion and core margin bridge are missing. AMPC label alone should not unlock Stage2-Actionable or Yellow."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L84_373220_LGES_AMPC_JV_UTILIZATION_BRIDGE","trigger_id":"R3L84_C13_373220_20240821_STAGE2_AMPC_JV_UTILIZATION_BRIDGE","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_scope":"current_default_proxy","profile_hypothesis":"current calibrated profile works when AMPC/JV optionality has utilization and shipment bridge","raw_component_scores_before":{"contract_score":9,"backlog_visibility_score":10,"margin_bridge_score":8,"revision_score":9,"relative_strength_score":13,"customer_quality_score":12,"policy_or_regulatory_score":16,"valuation_repricing_score":9,"execution_risk_score":-5,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":12,"margin_bridge_score":11,"revision_score":11,"relative_strength_score":15,"customer_quality_score":14,"policy_or_regulatory_score":18,"valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable/Stage3-Yellow-Watch","component_delta_explanation":"Utilization and shipment bridge upgrade C13 from Watch to Yellow-watch, while FCF/source confirmation still blocks Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L84_361610_SKIET_SEPARATOR_UTILIZATION_SHORTFALL","trigger_id":"R3L84_C13_361610_20240319_STAGE2_FALSE_POSITIVE_SEPARATOR_UTILIZATION","symbol":"361610","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_scope":"current_default_proxy","profile_hypothesis":"policy/JV optionality without utilization bridge should be blocked","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":4,"relative_strength_score":11,"customer_quality_score":5,"policy_or_regulatory_score":12,"valuation_repricing_score":7,"execution_risk_score":-12,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":51,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":6,"customer_quality_score":2,"policy_or_regulatory_score":8,"valuation_repricing_score":4,"execution_risk_score":-18,"legal_or_contract_risk_score":-3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":28,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Utilization and customer call-off bridge missing; high MAE converts optionality into guardrail evidence."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L84_051910_LGCHEM_HOLDCO_BATTERY_JV_DISCOUNT","trigger_id":"R3L84_C13_051910_20240216_STAGE2_FALSE_POSITIVE_HOLDCO_AMPC_JV_DISCOUNT","symbol":"051910","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_scope":"current_default_proxy","profile_hypothesis":"AMPC/JV exposure embedded in holdco discount should not count without FCF bridge","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":5,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":13,"valuation_repricing_score":8,"execution_risk_score":-10,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":52,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":3,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":9,"valuation_repricing_score":4,"execution_risk_score":-16,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":30,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Holdco discount, chemicals drag, and missing FCF bridge overwhelm policy/JV optionality."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L84_C13_P0_CURRENT","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C13 needs explicit utilization/FCF bridge distinction","eligible_trigger_count":3,"avg_MFE_90D_pct":10.40,"avg_MAE_90D_pct":-27.79,"avg_MFE_180D_pct":10.40,"avg_MAE_180D_pct":-42.91,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C13_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R3L84_C13_P1_SECTOR_SPECIFIC","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P1_L3_AMPC_utilization_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"Battery policy optionality needs utilization/customer/shipment bridge before Stage2-Actionable","changed_axes":["utilization_bridge_required","customer_calloff_quality_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_utilization_or_shipment_bridge"},"eligible_trigger_count":3,"avg_MFE_90D_pct":10.40,"avg_MAE_90D_pct":-27.79,"avg_MFE_180D_pct":10.40,"avg_MAE_180D_pct":-42.91,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R3L84_C13_P2_CANONICAL","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P2_C13_utilization_FCF_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C13 should separate real utilization bridge from subsidy-label false positives","changed_axes":["C13_utilization_bridge_required","C13_FCF_bridge_penalty","C13_holdco_discount_penalty"],"changed_thresholds":{"stage2_yellow_gate":"utilization_or_FCF_bridge_required"},"eligible_trigger_count":3,"avg_MFE_90D_pct":10.40,"avg_MAE_90D_pct":-27.79,"avg_MFE_180D_pct":10.40,"avg_MAE_180D_pct":-42.91,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R3L84_C13_P3_COUNTEREXAMPLE_GUARD","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P3_C13_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-30 while utilization/FCF bridge is missing, block Yellow/Green","changed_axes":["C13_high_MAE_guardrail","C13_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_30"},"eligible_trigger_count":3,"avg_MFE_90D_pct":10.40,"avg_MAE_90D_pct":-27.79,"avg_MFE_180D_pct":10.40,"avg_MAE_180D_pct":-42.91,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_AMPC_JV_UTILIZATION_BRIDGE_VS_POLICY_FALSE_POSITIVE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":10.40,"avg_MAE90_pct":-27.79,"avg_MFE180_pct":10.40,"avg_MAE180_pct":-42.91,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C13 needs bridge discipline. AMPC/JV optionality worked for 373220 only with utilization/shipment bridge proxy, while 361610 and 051910 show high-MAE false positives without utilization/FCF bridge."}
{"row_type":"stage_transition_summary","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"373220","trigger_type":"Stage2-Actionable-AMPC-JV-UtilizationBridge-Positive","entry_date":"2024-08-21","stage2_to_90D_outcome":"good_stage2_moderate_MFE","stage2_to_180D_outcome":"positive_bridge_with_tolerable_MAE","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when utilization/shipment bridge is present; Green requires margin/FCF and exact source repair."}
{"row_type":"stage_transition_summary","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"361610","trigger_type":"Stage2-FalsePositive-SeparatorUtilizationShortfall-NoAMPCBridge","entry_date":"2024-03-19","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_rerating_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Separator/JV optionality without utilization and customer call-off bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"051910","trigger_type":"Stage2-FalsePositive-HoldcoBatteryJVAMPC-DiscountNoFCFBridge","entry_date":"2024-02-16","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_rerating_holdco_discount","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Battery/JV optionality embedded in holdco discount needs FCF bridge; otherwise it becomes false positive."}
{"row_type":"residual_contribution","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","residual_type":"AMPC_JV_optionalities_overcredit_without_utilization_FCF_bridge","contribution":"Adds two C13 counterexamples against one utilization-bridge positive, improving the prior good-heavy C13 coverage balance.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_JV_UTILIZATION_BRIDGE_VS_POLICY_CREDIT_AND_HOLDCO_DISCOUNT_FALSE_POSITIVE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C13 counterexample balance improved; next R3 loops should add exact URL repair and 4C thesis-break examples for utilization/call-off failures."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_utilization_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"373220 worked with utilization/shipment bridge proxy; 361610 failed when utilization and call-off quality were missing."}
{"row_type":"shadow_weight","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_FCF_bridge_and_holdco_discount_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"051910 shows battery/JV/AMPC optionality can be neutralized by holding-company discount, chemical-cycle drag, and missing FCF bridge."}
{"row_type":"shadow_weight","round":"R3","loop":"84","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-30 while utilization/FCF bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
residual_error_types_found:
  - AMPC_JV_optionalities_overcredit_without_utilization_bridge
  - separator_utilization_shortfall_high_MAE
  - battery_holdco_discount_no_FCF_bridge
new_axis_proposed:
  - C13_utilization_bridge_required_shadow_only
  - C13_FCF_bridge_and_holdco_discount_guard_shadow_only
  - C13_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C13
  - full_4b_requires_non_price_evidence within C13
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
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
3. Confirm R3 / L3 / C13 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. If aggregate support remains stable after exact evidence URL repair, consider C13-scoped safe patch candidates:
   - C13_utilization_bridge_required
   - C13_FCF_bridge_and_holdco_discount_guard
   - C13_high_MAE_guardrail
6. Do not loosen Stage3-Green.
7. Do not use future MFE/MAE in runtime scoring.
8. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R3
completed_loop = 84
next_round = R4
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA.
```
