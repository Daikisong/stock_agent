# E2R Stock-Web v12 Residual Research — R1 Loop 84 / L1 / C05

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R1
loop: 84
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: EPC_MEGA_CONTRACT_MARGIN_BRIDGE_VS_LOW_MARGIN_WORKING_CAPITAL_GAP
sector: industrials / infra / EPC / mega-contract margin gap
output_file: e2r_stock_web_v12_residual_round_R1_loop_84_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after `R13 loop 83`.

```text
scheduled_round = R1
scheduled_loop = 84
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

R1 allows L1 industrials / infra / defense / grid.  
C05 is selected because the No-Repeat ledger shows it as one of the thinner R1 canonical buckets, with fewer rows and symbols than C01~C03. The target is not to re-prove the global rules, but to test a C05-local distinction:

```text
EPC mega-contract headline != structural rerating
unless the contract converts into margin, working-capital, backlog quality, and cash-flow bridge.
```

This is not a live stock recommendation, not a repository patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"000720","company_name":"현대건설","profile_path":"atlas/symbol_profiles/000/000720.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7740,"corporate_action_candidate_count":7,"corporate_action_candidate_dates":["1998-05-23","1998-11-19","1999-03-05","2001-07-06","2001-07-12","2004-01-13","2004-04-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2025 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2025_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"028050","company_name":"삼성E&A","profile_path":"atlas/symbol_profiles/028/028050.json","first_date":"1997-01-03","last_date":"2026-02-20","trading_day_count":7265,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1997-08-22","1999-01-13","1999-05-26","1999-09-29","2016-02-26"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"006360","company_name":"GS건설","profile_path":"atlas/symbol_profiles/006/006360.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7761,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1999-05-07","1999-12-01","2014-06-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
For C05, the top covered symbols include `053690`, `002150`, `011560`, `023350`, `023960`, and `054930`. This run avoids that repeated set and uses three C05-new symbols.

Hard duplicate rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"000720","trigger_type":"Stage2-Actionable-EPCBacklogMarginBridge-Positive","entry_date":"2025-01-22","duplicate_status":"new C05 symbol/trigger/date combination"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"028050","trigger_type":"Stage2-FalsePositive-MegaContractMarginGap-WorkingCapitalBreak","entry_date":"2024-03-11","duplicate_status":"new C05 symbol/trigger/date combination"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"006360","trigger_type":"Stage2-RepairControl-ConstructionMarginRecoveryBridge","entry_date":"2024-04-03","duplicate_status":"new C05 symbol/trigger/date combination"}
```

## 4. Research question

C05 is the EPC pressure test. A headline contract can look like a bridge, but the bridge may be made of paper if gross margin, working capital, cost escalation, and cash conversion are not improving.

Residual question:

```text
Can the calibrated E2R profile distinguish:
1. EPC/backlog rerating with later price confirmation and tolerable MAE,
2. mega-contract or overseas EPC headline that fails because margin/working-capital bridge is absent,
3. low-base construction/EPC repair path that works as a Watch/Yellow bridge but not a Green unlock?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C05_R1L84_000720_HDC_EPC_BACKLOG_MARGIN_BRIDGE","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_BACKLOG_MARGIN_REPAIR_WITH_LATE_PRICE_CONFIRMATION","symbol":"000720","company_name":"현대건설","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-EPCBacklogMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_may_undercredit_if_C05_too_guarded","price_source":"Songdaiki/stock-web","notes":"EPC/infra backlog bridge worked after 2025 entry; use as positive control, not Green relaxation."}
{"row_type":"case","case_id":"C05_R1L84_028050_SAMSUNG_EA_MARGIN_GAP_COUNTEREXAMPLE","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"MEGA_CONTRACT_HEADLINE_WITH_MARGIN_WORKING_CAPITAL_GAP","symbol":"028050","company_name":"삼성E&A","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-MegaContractMarginGap-WorkingCapitalBreak","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_contract_headline_overcredited","price_source":"Songdaiki/stock-web","notes":"Contract/headline and relative-strength rebound failed without margin and cash-conversion evidence."}
{"row_type":"case","case_id":"C05_R1L84_006360_GS_EC_MARGIN_REPAIR_CONTROL","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CONSTRUCTION_EPC_MARGIN_REPAIR_WATCH_CONTROL","symbol":"006360","company_name":"GS건설","case_type":"watch_positive_control","positive_or_counterexample":"positive","best_trigger":"Stage2-RepairControl-ConstructionMarginRecoveryBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"moderate_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_watch_yellow_not_green","price_source":"Songdaiki/stock-web","notes":"Repair path had usable MFE with tolerable MAE, but should remain Watch/Yellow until margin bridge is verified."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 000720 현대건설 — positive backlog/margin bridge control

Entry row: `2025-01-22 c=28450`.  
Observed price path: tolerable same-day MAE and large 90D/180D MFE as EPC/infra backlog rerating unfolded.

```jsonl
{"row_type":"trigger","trigger_id":"R1L84_C05_000720_20250122_STAGE2_EPC_BACKLOG_MARGIN_BRIDGE_POSITIVE","case_id":"C05_R1L84_000720_HDC_EPC_BACKLOG_MARGIN_BRIDGE","symbol":"000720","company_name":"현대건설","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_BACKLOG_MARGIN_REPAIR_WITH_LATE_PRICE_CONFIRMATION","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-EPCBacklogMarginBridge-Positive","trigger_date":"2025-01-22","entry_date":"2025-01-22","entry_price":28450.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_report_consensus_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; EPC/infra backlog and margin-repair thesis treated as non-price bridge proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["backlog_visibility","margin_bridge_proxy","relative_strength_turn"],"stage3_evidence_fields":["multi_quarter_margin_bridge_pending","cash_conversion_pending","source_url_pending"],"stage4b_evidence_fields":["positioning_overheat_watch_after_large_MFE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000720/2025.csv","profile_path":"atlas/symbol_profiles/000/000720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":31.99,"MFE_90D_pct":135.15,"MFE_180D_pct":199.12,"MAE_30D_pct":-9.14,"MAE_90D_pct":-9.14,"MAE_180D_pct":-9.14,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-25","peak_price":85100.0,"max_drawdown_low_date":"2025-01-22","max_drawdown_low":25850.0,"drawdown_after_peak_pct":-36.13,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_may_undercredit_if_C05_too_guarded","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2025_window","same_entry_group_id":"000720_2025-01-22_28450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 should not be pure anti-EPC. When backlog/margin bridge and later price confirmation align, Stage2/Yellow should be allowed. Green still requires confirmed margin and cash conversion."}
```

### 6.2 028050 삼성E&A — mega-contract headline / margin gap counterexample

Entry row: `2024-03-11 c=26750`.  
Observed path: upside was shallow, while the later 180D low reached `2024-12-09 l=16300`.

```jsonl
{"row_type":"trigger","trigger_id":"R1L84_C05_028050_20240311_STAGE2_FALSE_POSITIVE_MARGIN_GAP","case_id":"C05_R1L84_028050_SAMSUNG_EA_MARGIN_GAP_COUNTEREXAMPLE","symbol":"028050","company_name":"삼성E&A","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"MEGA_CONTRACT_HEADLINE_WITH_MARGIN_WORKING_CAPITAL_GAP","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-MegaContractMarginGap-WorkingCapitalBreak","trigger_date":"2024-03-11","entry_date":"2024-03-11","entry_price":26750.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_contract_report_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; mega-contract/overseas EPC narrative treated as insufficient without margin and working-capital bridge","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["contract_headline","relative_strength_rebound"],"stage3_evidence_fields":["margin_bridge_missing","working_capital_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.23,"MFE_90D_pct":5.23,"MFE_180D_pct":5.23,"MAE_30D_pct":-10.47,"MAE_90D_pct":-19.25,"MAE_180D_pct":-39.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-15","peak_price":28150.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":16300.0,"drawdown_after_peak_pct":-42.10,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"early_local_peak_should_remain_watch_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_headline_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"028050_2024-03-11_26750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 needs a local bridge requirement. Contract/relative-strength headline without margin, working-capital, and cash-conversion bridge produced low MFE and deep 180D MAE."}
```

### 6.3 006360 GS건설 — repair path Watch/Yellow control

Entry row: `2024-04-03 c=15630`.  
Observed path: moderate 180D MFE, tolerable MAE, and later repair rally, but not enough for Green without margin evidence.

```jsonl
{"row_type":"trigger","trigger_id":"R1L84_C05_006360_20240403_STAGE2_REPAIR_CONTROL_MARGIN_BRIDGE","case_id":"C05_R1L84_006360_GS_EC_MARGIN_REPAIR_CONTROL","symbol":"006360","company_name":"GS건설","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CONSTRUCTION_EPC_MARGIN_REPAIR_WATCH_CONTROL","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-RepairControl-ConstructionMarginRecoveryBridge","trigger_date":"2024-04-03","entry_date":"2024-04-03","entry_price":15630.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_repair_report_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; construction/EPC margin-repair path used as Watch/Yellow control only","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["repair_base","relative_strength_turn","margin_bridge_proxy"],"stage3_evidence_fields":["confirmed_margin_bridge_pending","working_capital_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["valuation_or_positioning_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv","profile_path":"atlas/symbol_profiles/006/006360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.97,"MFE_90D_pct":19.13,"MFE_180D_pct":27.19,"MAE_30D_pct":-10.17,"MAE_90D_pct":-10.17,"MAE_180D_pct":-10.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-28","peak_price":19880.0,"max_drawdown_low_date":"2024-04-19","max_drawdown_low":14040.0,"drawdown_after_peak_pct":-14.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_control_not_full_4B","four_b_evidence_type":["price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_moderate_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_watch_yellow_not_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"006360_2024-04-03_15630","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 local guard should not block all repair paths. Moderate MFE with tolerable MAE can support Watch/Yellow, but Green needs confirmed margin and working-capital evidence."}
```

## 7. Score simulation rows

These rows are research proxy simulations only.

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L84_000720_HDC_EPC_BACKLOG_MARGIN_BRIDGE","trigger_id":"R1L84_C05_000720_20250122_STAGE2_EPC_BACKLOG_MARGIN_BRIDGE_POSITIVE","symbol":"000720","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"current calibrated profile may be too guarded for C05 positives unless margin/backlog bridge is explicitly recognized","raw_component_scores_before":{"contract_score":13,"backlog_visibility_score":15,"margin_bridge_score":12,"revision_score":9,"relative_strength_score":14,"customer_quality_score":11,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":-5,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":18,"margin_bridge_score":16,"revision_score":11,"relative_strength_score":15,"customer_quality_score":12,"policy_or_regulatory_score":3,"valuation_repricing_score":9,"execution_risk_score":-4,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable/Stage3-Yellow-Watch","component_delta_explanation":"Explicit backlog-to-margin bridge upgrades Stage2/Yellow, but source URL and cash-conversion confirmation still block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L84_028050_SAMSUNG_EA_MARGIN_GAP_COUNTEREXAMPLE","trigger_id":"R1L84_C05_028050_20240311_STAGE2_FALSE_POSITIVE_MARGIN_GAP","symbol":"028050","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"headline contract credit can create false Stage2 if margin/working-capital bridge is not required","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":11,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":13,"customer_quality_score":8,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":-10,"legal_or_contract_risk_score":-5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":8,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":-14,"legal_or_contract_risk_score":-7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/Stage2-Watch-Blocked","component_delta_explanation":"C05 guard penalizes missing margin, working-capital, and cash-conversion bridge; high 180D MAE confirms false positive."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L84_006360_GS_EC_MARGIN_REPAIR_CONTROL","trigger_id":"R1L84_C05_006360_20240403_STAGE2_REPAIR_CONTROL_MARGIN_BRIDGE","symbol":"006360","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"repair path should be Watch/Yellow, not Green, until margin bridge is visible","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":10,"revision_score":6,"relative_strength_score":11,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":-7,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":57,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":9,"backlog_visibility_score":11,"margin_bridge_score":12,"revision_score":7,"relative_strength_score":12,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":9,"execution_risk_score":-6,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":63,"stage_label_after":"Stage2-Watch/Yellow-Repair-Control","component_delta_explanation":"Moderate MFE and tolerable MAE support Watch/Yellow repair control, but missing exact bridge evidence blocks Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R1L84_C05_P0_CURRENT","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help, but C05 still needs explicit margin/working-capital bridge distinction","eligible_trigger_count":3,"avg_MFE_90D_pct":53.17,"avg_MAE_90D_pct":-12.85,"avg_MFE_180D_pct":77.18,"avg_MAE_180D_pct":-19.46,"false_positive_rate":0.33,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C05_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R1L84_C05_P1_SECTOR_SPECIFIC","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P1_L1_EPC_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 EPC positives require backlog-to-margin and working-capital bridge; otherwise stay Watch","changed_axes":["margin_bridge_required","working_capital_bridge_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_margin_or_cash_conversion_proxy"},"eligible_trigger_count":3,"avg_MFE_90D_pct":53.17,"avg_MAE_90D_pct":-12.85,"avg_MFE_180D_pct":77.18,"avg_MAE_180D_pct":-19.46,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better_than_current_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R1L84_C05_P2_CANONICAL","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P2_C05_bridge_guard_candidate","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C05 should distinguish EPC backlog quality from margin gap; contract headline alone is insufficient","changed_axes":["C05_margin_working_capital_bridge_required","C05_headline_contract_penalty"],"changed_thresholds":{"stage2_yellow_gate":"non_price_bridge_required"},"eligible_trigger_count":3,"avg_MFE_90D_pct":53.17,"avg_MAE_90D_pct":-12.85,"avg_MFE_180D_pct":77.18,"avg_MAE_180D_pct":-19.46,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R1L84_C05_P3_COUNTEREXAMPLE_GUARD","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P3_C05_high_MAE_counterexample_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE180<=-30 while margin bridge is missing, block Stage2-Actionable/Yellow","changed_axes":["C05_high_MAE_guardrail","C05_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE180_le_minus_30"},"eligible_trigger_count":3,"avg_MFE_90D_pct":53.17,"avg_MAE_90D_pct":-12.85,"avg_MFE_180D_pct":77.18,"avg_MAE_180D_pct":-19.46,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_EPC_MARGIN_BRIDGE_VS_HEADLINE_GAP","row_count":3,"unique_symbol_count":3,"positive_case_count":2,"counterexample_count":1,"good_stage2_count":2,"bad_stage2_count":1,"4B_case_count":1,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":53.17,"avg_MAE90_pct":-12.85,"avg_MFE180_pct":77.18,"avg_MAE180_pct":-19.46,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.0,"interpretation":"C05 is not simply bearish EPC. Positive paths exist when backlog/margin bridge is visible, but headline-only mega-contract paths need a margin/working-capital guard."}
{"row_type":"stage_transition_summary","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"000720","trigger_type":"Stage2-Actionable-EPCBacklogMarginBridge-Positive","entry_date":"2025-01-22","stage2_to_90D_outcome":"good_stage2_high_MFE","stage2_to_180D_outcome":"positive_re_rating_path","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Bridge-positive EPC can be Stage2/Yellow; Green requires confirmed margin and cash conversion."}
{"row_type":"stage_transition_summary","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"028050","trigger_type":"Stage2-FalsePositive-MegaContractMarginGap-WorkingCapitalBreak","entry_date":"2024-03-11","stage2_to_90D_outcome":"weak_stage2_low_MFE","stage2_to_180D_outcome":"counterexample_high_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Headline-only EPC path had low MFE and deep 180D MAE; require bridge evidence before Yellow."}
{"row_type":"stage_transition_summary","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"006360","trigger_type":"Stage2-RepairControl-ConstructionMarginRecoveryBridge","entry_date":"2024-04-03","stage2_to_90D_outcome":"watch_control_moderate_MFE","stage2_to_180D_outcome":"positive_control_tolerable_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Repair path supports Watch/Yellow but not Green without confirmed margin bridge."}
{"row_type":"residual_contribution","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","residual_type":"EPC_headline_vs_margin_working_capital_bridge","contribution":"Adds three new C05 symbols and separates EPC structural bridge from headline-only margin gap false positive.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MEGA_CONTRACT_MARGIN_BRIDGE_VS_LOW_MARGIN_WORKING_CAPITAL_GAP","positive_case_count":2,"counterexample_count":1,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"Need exact URL repair and more 4C cases for EPC cost-overrun/legal delay; current loop improves positive balance and headline-gap counterexample coverage."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_margin_working_capital_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"028050 shows headline-only EPC contract path can fail; 000720 and 006360 show bridge-positive paths should remain eligible for Watch/Yellow."}
{"row_type":"shadow_weight","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_headline_contract_false_positive_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"If contract headline has MFE90<10 and MAE180<=-30 without margin/cash-conversion bridge, block Stage2-Actionable/Yellow."}
{"row_type":"shadow_weight","round":"R1","loop":"84","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_repair_path_watch_allowance","scope":"canonical_archetype","candidate_delta":0.5,"direction":"selective_allow","apply_now":false,"shadow_only":true,"evidence_basis":"Do not over-block all C05 repair paths. Moderate MFE and tolerable MAE with bridge proxy can remain Watch/Yellow but not Green."}
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
  - missed_structural_if_C05_too_guarded
  - false_positive_if_EPC_headline_overcredited
  - low_margin_working_capital_gap
new_axis_proposed:
  - C05_margin_working_capital_bridge_required_shadow_only
  - C05_headline_contract_false_positive_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C05
  - full_4b_requires_non_price_evidence within C05
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
The non-price evidence layer is still source-name/proxy level.

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
3. Confirm R1 / L1 / C05 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. If aggregate support remains stable after exact evidence URL repair, consider C05-scoped safe patch candidates:
   - C05_margin_working_capital_bridge_required
   - C05_headline_contract_false_positive_guard
   - C05_repair_path_watch_allowance
6. Do not loosen Stage3-Green.
7. Do not use future MFE/MAE in runtime scoring.
8. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R1
completed_loop = 84
next_round = R2
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 counterexamples, and 2 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C05_EPC_MEGA_CONTRACT_MARGIN_GAP.
```
