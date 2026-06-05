# E2R Stock-Web v12 Residual Research — R1 Loop 91 / L1 / C05

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R1
loop: 91
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: ENERGY_PLANT_EQUIPMENT_BACKLOG_MARGIN_BRIDGE_VS_EPC_CLEANROOM_CONTRACT_THEME_DECAY
sector: industrials / EPC / engineering / plant equipment / cleanroom construction / mega contract / margin gap
output_file: e2r_stock_web_v12_residual_round_R1_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R13 loop 90`.

```text
scheduled_round = R1
scheduled_loop = 91
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

R1 is restricted to L1 industrials / infrastructure / defense / grid.  
C05 is selected because the recent L1 path already used C02, C03, and C04, and C05 remains thin with only 10 rows and 9 symbols.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
rows = 10
symbols = 9
good/bad Stage2 = 3/4
4B/4C = 0/0
top-covered = 053690, 002150, 011560, 023350, 023960, 054930
```

This loop avoids the C05 top-covered symbols and recent L1 loop symbols:

```text
R11 loop86 C03: 012450, 010820, 013810
R11 loop87 C04: 051600, 032820, 094820
R11 loop88 C05: 052690, 026150, 028100
R11 loop89 C02: 229640, 199820, 006910
R11 loop90 C03: 272210, 095190, 218410
R1 loop89 C03: 064350, 099320, 214430
R1 loop90 C04: 130660, 105840, 019990
```

Selected symbols:

```text
100840, 028050, 037350
```

The selected pocket is:

```text
energy plant equipment / heat-exchanger backlog and margin bridge
vs
large EPC rebrand / mega-contract vocabulary without fresh margin conversion
vs
cleanroom / engineering theme late-cycle spike without backlog-to-margin/cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"100840","company_name":"SNT에너지","profile_path":"atlas/symbol_profiles/100/100840.json","first_date":"2008-02-22","last_date":"2026-02-20","trading_day_count":4439,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2008-11-26","2008-12-23","2024-04-16","2024-05-17"],"has_major_raw_discontinuity":true,"calibration_caveat":"2024 corporate-action candidates exist before the selected 2024-06-03 entry. This row is kept as post-candidate data-quality-watch positive-control.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_entry_after_2024-05-17_candidate; data_quality_watch"}
{"row_type":"price_source_validation","symbol":"028050","company_name":"삼성E&A","profile_path":"atlas/symbol_profiles/028/028050.json","first_date":"1997-01-03","last_date":"2026-02-20","trading_day_count":7265,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["1997-08-22","1999-01-13","1999-05-26","1999-09-29","2016-02-26"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window. Name changed from 삼성엔지니어링 to 삼성E&A in April 2024 before the selected entry.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; name_change_watch"}
{"row_type":"price_source_validation","symbol":"037350","company_name":"성도이엔지","profile_path":"atlas/symbol_profiles/037/037350.json","first_date":"2000-01-11","last_date":"2026-02-20","trading_day_count":6431,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2000-09-04","2002-01-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 entry window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"100840","trigger_type":"Stage2-Actionable-EnergyPlantEquipmentBacklogMarginBridge-Positive","entry_date":"2024-06-03","duplicate_status":"new C05 symbol/trigger/date combination outside top-covered and recent L1 loop symbols; post-candidate data-quality watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"028050","trigger_type":"Stage2-FalsePositive-LargeEPCRebrandContractVocabularyNoFreshMarginBridge","entry_date":"2024-04-22","duplicate_status":"new C05 symbol/trigger/date combination outside top-covered and recent L1 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"037350","trigger_type":"Stage2-FalsePositive-CleanroomEngineeringLateCycleSpikeNoBacklogMarginCashBridge","entry_date":"2024-10-10","duplicate_status":"new C05 symbol/trigger/date combination outside top-covered and recent L1 loop symbols"}
```

## 4. Research question

C05 is not “EPC나 엔지니어링 뉴스가 있다.”  
The useful signal must prove the bridge from contract vocabulary to realized economics:

```text
signed contract or executable order
customer / project owner quality
scope and delivery schedule
backlog conversion
cost escalation control
gross-margin visibility
working-capital discipline
cash collection
margin gap containment
```

A mega-contract headline without this bridge is a crane standing over an empty foundation. It is impressive, but E2R needs to see the steel, concrete, progress billing, and margin ledger.

Residual question:

```text
Can C05 distinguish:
1. energy plant equipment / heat-exchanger backlog-margin bridge with very high MFE after a post-candidate entry,
2. large EPC rebrand / mega-contract vocabulary where no fresh order-to-margin conversion exists,
3. cleanroom/engineering late-cycle spike where no backlog, margin, working-capital or cash bridge confirms the move?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C05_R1L91_100840_SNT_ENERGY_BACKLOG_MARGIN","symbol":"100840","company_name":"SNT에너지","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"ENERGY_PLANT_EQUIPMENT_BACKLOG_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-EnergyPlantEquipmentBacklogMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"positive_very_high_MFE90_and_MFE180_low_MAE_post_candidate_watch","current_profile_verdict":"current_profile_correct_if_order_backlog_delivery_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Post-candidate selected entry produced high MFE90 and very high MFE180 with shallow MAE. Positive-control is usable for residual analysis but must remain data-quality watch because of 2024 corporate-action candidates before entry."}
{"row_type":"case","case_id":"C05_R1L91_028050_SAMSUNG_EA_EPC_REBRAND_DECAY","symbol":"028050","company_name":"삼성E&A","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"LARGE_EPC_REBRAND_CONTRACT_VOCABULARY_WITHOUT_FRESH_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LargeEPCRebrandContractVocabularyNoFreshMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_large_EPC_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Large EPC/rebrand vocabulary had low MFE and deep 180D MAE when no fresh order, margin, working-capital or cash bridge was repaired."}
{"row_type":"case","case_id":"C05_R1L91_037350_SUNGDO_CLEANROOM_SPIKE_DECAY","symbol":"037350","company_name":"성도이엔지","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CLEANROOM_ENGINEERING_LATE_CYCLE_SPIKE_WITHOUT_BACKLOG_MARGIN_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CleanroomEngineeringLateCycleSpikeNoBacklogMarginCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_MAE_expansion_no_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_cleanroom_engineering_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Late-cycle cleanroom/engineering spike had near-zero MFE and a later drawdown without backlog, margin, working-capital or cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 100840 SNT에너지 — energy plant equipment backlog / margin bridge positive-control

Selected entry is after the 2024-04-16 and 2024-05-17 corporate-action candidate dates.

```jsonl
{"row_type":"trigger","trigger_id":"R1L91_C05_100840_20240603_STAGE2_ENERGY_EQUIPMENT_BACKLOG_MARGIN","case_id":"C05_R1L91_100840_SNT_ENERGY_BACKLOG_MARGIN","symbol":"100840","company_name":"SNT에너지","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"ENERGY_PLANT_EQUIPMENT_BACKLOG_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test;data_quality_watch","trigger_type":"Stage2-Actionable-EnergyPlantEquipmentBacklogMarginBridge-Positive","trigger_date":"2024-06-03","entry_date":"2024-06-03","entry_price":10050.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_energy_plant_equipment_backlog_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; heat-exchanger/plant-equipment order backlog, delivery and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["order_backlog_proxy","plant_equipment_delivery_proxy","margin_bridge_proxy","relative_strength_turn_after_candidate"],"stage3_evidence_fields":["exact_customer_project_source_pending","signed_order_or_backlog_source_pending","delivery_schedule_pending","working_capital_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","post_candidate_data_quality_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/100/100840/2024.csv","profile_path":"atlas/symbol_profiles/100/100840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":60.20,"MFE_90D_pct":60.20,"MFE_180D_pct":153.73,"MAE_30D_pct":-4.28,"MAE_90D_pct":-4.28,"MAE_180D_pct":-4.28,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-26","peak_price":25500.0,"max_drawdown_low_date":"2024-06-03","max_drawdown_low":9620.0,"drawdown_after_peak_pct":-11.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.63,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_customer_project_backlog_delivery_margin_cash_evidence_and_data_quality_repair","four_b_evidence_type":["price_extension_watch","post_candidate_data_quality_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE90_and_MFE180_low_MAE_post_candidate_watch","current_profile_verdict":"current_profile_correct_if_order_backlog_delivery_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["post_2024_corporate_action_candidate_data_quality_watch"],"corporate_action_window_status":"selected_entry_after_2024-05-17_candidate; data_quality_watch","same_entry_group_id":"100840_2024-06-03_10050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C05 can allow Stage2/Yellow when EPC/equipment strength is tied to executable order backlog, delivery schedule, margin and cash bridge. Green requires exact evidence and price-path data-quality repair."}
```

### 6.2 028050 삼성E&A — large EPC/rebrand vocabulary without fresh margin bridge

```jsonl
{"row_type":"trigger","trigger_id":"R1L91_C05_028050_20240422_STAGE2_FALSE_POSITIVE_EPC_REBRAND","case_id":"C05_R1L91_028050_SAMSUNG_EA_EPC_REBRAND_DECAY","symbol":"028050","company_name":"삼성E&A","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"LARGE_EPC_REBRAND_CONTRACT_VOCABULARY_WITHOUT_FRESH_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-LargeEPCRebrandContractVocabularyNoFreshMarginBridge","trigger_date":"2024-04-22","entry_date":"2024-04-22","entry_price":26300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_large_EPC_contract_rebrand_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; large EPC/rebrand/contract vocabulary treated as insufficient without fresh signed order, delivery, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["large_EPC_vocabulary","rebrand_or_contract_keyword","relative_strength_rebound"],"stage3_evidence_fields":["fresh_signed_order_missing","delivery_schedule_missing","margin_gap_control_missing","cash_conversion_missing"],"stage4b_evidence_fields":["low_MFE_watch","margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv","profile_path":"atlas/symbol_profiles/028/028050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.66,"MFE_90D_pct":2.66,"MFE_180D_pct":2.66,"MAE_30D_pct":-11.79,"MAE_90D_pct":-17.87,"MAE_180D_pct":-38.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-30","peak_price":27000.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":16300.0,"drawdown_after_peak_pct":-39.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"large_EPC_rebrand_or_contract_vocabulary_without_fresh_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_large_EPC_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean; 2024_name_change_watch","same_entry_group_id":"028050_2024-04-22_26300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 should not promote large EPC vocabulary without signed order, scope, delivery, margin-gap control and cash bridge. Low MFE and deep MAE require Watch/4B routing."}
```

### 6.3 037350 성도이엔지 — cleanroom / engineering late-cycle spike without backlog-margin-cash bridge

```jsonl
{"row_type":"trigger","trigger_id":"R1L91_C05_037350_20241010_STAGE2_FALSE_POSITIVE_CLEANROOM_ENGINEERING_SPIKE","case_id":"C05_R1L91_037350_SUNGDO_CLEANROOM_SPIKE_DECAY","symbol":"037350","company_name":"성도이엔지","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CLEANROOM_ENGINEERING_LATE_CYCLE_SPIKE_WITHOUT_BACKLOG_MARGIN_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;late_cycle_price_spike_stress_test","trigger_type":"Stage2-FalsePositive-CleanroomEngineeringLateCycleSpikeNoBacklogMarginCashBridge","trigger_date":"2024-10-10","entry_date":"2024-10-10","entry_price":5380.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cleanroom_engineering_late_cycle_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cleanroom/engineering late-cycle spike treated as insufficient without executable backlog, project scope, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["cleanroom_engineering_theme","late_cycle_price_spike"],"stage3_evidence_fields":["signed_backlog_missing","project_scope_missing","margin_cash_bridge_missing","working_capital_bridge_missing"],"stage4b_evidence_fields":["near_zero_MFE","late_cycle_spike_watch","backlog_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/037/037350/2024.csv","profile_path":"atlas/symbol_profiles/037/037350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.49,"MFE_90D_pct":1.49,"MFE_180D_pct":1.49,"MAE_30D_pct":-22.21,"MAE_90D_pct":-25.00,"MAE_180D_pct":-29.18,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-10","peak_price":5460.0,"max_drawdown_low_date":"2025-04-07","max_drawdown_low":3810.0,"drawdown_after_peak_pct":-30.22,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"cleanroom_engineering_late_cycle_spike_without_backlog_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","late_cycle_spike_watch","backlog_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_MAE_expansion_no_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_cleanroom_engineering_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"037350_2024-10-10_5380","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C05 should not count cleanroom/engineering late-cycle price spikes as EPC backlog evidence. Signed backlog, project scope, margin and cash bridge must be exact-repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L91_100840_SNT_ENERGY_BACKLOG_MARGIN","trigger_id":"R1L91_C05_100840_20240603_STAGE2_ENERGY_EQUIPMENT_BACKLOG_MARGIN","symbol":"100840","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C05 requires signed order/backlog, customer/project quality, delivery schedule, margin-gap control and cash bridge rather than EPC/equipment vocabulary alone","raw_component_scores_before":{"signed_order_score":12,"customer_project_quality_score":11,"delivery_schedule_score":11,"backlog_conversion_score":13,"margin_gap_control_score":11,"working_capital_score":8,"cash_collection_score":7,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch/DataQualityWatch","raw_component_scores_after":{"signed_order_score":15,"customer_project_quality_score":14,"delivery_schedule_score":14,"backlog_conversion_score":16,"margin_gap_control_score":14,"working_capital_score":10,"cash_collection_score":9,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":87,"stage_label_after":"Stage3-Yellow/Green-candidate-watch/DataQualityWatch","component_delta_explanation":"Backlog/delivery/margin bridge plus very high MFE supports Yellow/Green-candidate watch; exact evidence and post-candidate data-quality repair block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L91_028050_SAMSUNG_EA_EPC_REBRAND_DECAY","trigger_id":"R1L91_C05_028050_20240422_STAGE2_FALSE_POSITIVE_EPC_REBRAND","symbol":"028050","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"large EPC/rebrand vocabulary without fresh order/margin bridge should be blocked","raw_component_scores_before":{"signed_order_score":1,"customer_project_quality_score":2,"delivery_schedule_score":1,"backlog_conversion_score":1,"margin_gap_control_score":0,"working_capital_score":0,"cash_collection_score":0,"relative_strength_score":4,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"signed_order_score":0,"customer_project_quality_score":0,"delivery_schedule_score":0,"backlog_conversion_score":0,"margin_gap_control_score":0,"working_capital_score":0,"cash_collection_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert the EPC vocabulary row into missing margin/cash bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C05_R1L91_037350_SUNGDO_CLEANROOM_SPIKE_DECAY","trigger_id":"R1L91_C05_037350_20241010_STAGE2_FALSE_POSITIVE_CLEANROOM_ENGINEERING_SPIKE","symbol":"037350","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_scope":"current_default_proxy","profile_hypothesis":"cleanroom/engineering late-cycle spike without backlog and margin bridge should remain Watch/4B","raw_component_scores_before":{"signed_order_score":1,"customer_project_quality_score":1,"delivery_schedule_score":0,"backlog_conversion_score":0,"margin_gap_control_score":0,"working_capital_score":0,"cash_collection_score":0,"relative_strength_score":6,"valuation_repricing_score":2,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"signed_order_score":0,"customer_project_quality_score":0,"delivery_schedule_score":0,"backlog_conversion_score":0,"margin_gap_control_score":0,"working_capital_score":0,"cash_collection_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and MAE expansion require signed backlog, project scope, margin and cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R1L91_C05_P0_CURRENT","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C05 needs explicit signed order, backlog conversion, delivery, margin-gap control, working-capital/cash and data-quality taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":21.45,"avg_MAE90_pct":-15.72,"avg_MFE180_pct":52.63,"avg_MAE180_pct":-23.83,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.88,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C05_order_backlog_delivery_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R1L91_C05_P1_SECTOR_SPECIFIC","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P1_L1_EPC_order_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L1 EPC/engineering signals need signed order, customer/project quality, delivery schedule, backlog conversion, margin control or cash conversion before Stage2-Actionable","changed_axes":["signed_order_required","delivery_backlog_required","margin_cash_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_signed_order_customer_project_delivery_backlog_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":21.45,"avg_MAE90_pct":-15.72,"avg_MFE180_pct":52.63,"avg_MAE180_pct":-23.83,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R1L91_C05_P2_CANONICAL","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P2_C05_order_backlog_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C05 should reward order-to-margin mechanics, not EPC/rebrand/cleanroom labels","changed_axes":["C05_order_backlog_delivery_margin_cash_bridge_required","C05_EPC_cleanroom_vocabulary_local_4B_guard","C05_post_candidate_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"signed_order_or_backlog_plus_delivery_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":21.45,"avg_MAE90_pct":-15.72,"avg_MFE180_pct":52.63,"avg_MAE180_pct":-23.83,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R1L91_C05_P3_COUNTEREXAMPLE_GUARD","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_id":"P3_C05_low_MFE_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If order/backlog/margin bridge is missing, MFE90<5 or MAE180<=-25 should block Yellow/Green and route to Watch/4B","changed_axes":["C05_low_MFE_guardrail","C05_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_5_or_MAE180_le_minus_25)"},"eligible_trigger_count":3,"avg_MFE90_pct":21.45,"avg_MAE90_pct":-15.72,"avg_MFE180_pct":52.63,"avg_MAE180_pct":-23.83,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"C05_ENERGY_EQUIPMENT_POSITIVE_VS_EPC_CLEANROOM_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":21.45,"avg_MAE90_pct":-15.72,"avg_MFE180_pct":52.63,"avg_MAE180_pct":-23.83,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"data_quality_watch_count":1,"interpretation":"C05 needs bridge discipline. SNT에너지는 post-candidate data-quality watch에도 order/backlog-margin bridge가 있으면 Yellow/Green-candidate-watch가 가능하지만, 삼성E&A and 성도이엔지는 EPC/rebrand/cleanroom vocabulary만으로는 signed order, delivery, margin-gap control and cash bridge를 증명하지 못한다."}
{"row_type":"stage_transition_summary","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"100840","trigger_type":"Stage2-Actionable-EnergyPlantEquipmentBacklogMarginBridge-Positive","entry_date":"2024-06-03","stage2_to_90D_outcome":"good_stage2_very_high_MFE90_low_MAE_post_candidate_watch","stage2_to_180D_outcome":"positive_order_backlog_bridge_but_data_quality_and_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when executable backlog, delivery, margin and cash bridge exists; Green requires exact evidence and post-candidate data-quality repair."}
{"row_type":"stage_transition_summary","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"028050","trigger_type":"Stage2-FalsePositive-LargeEPCRebrandContractVocabularyNoFreshMarginBridge","entry_date":"2024-04-22","stage2_to_90D_outcome":"bad_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_large_EPC_vocabulary_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Large EPC/rebrand vocabulary without fresh order and margin/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"037350","trigger_type":"Stage2-FalsePositive-CleanroomEngineeringLateCycleSpikeNoBacklogMarginCashBridge","entry_date":"2024-10-10","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_MAE_expansion","stage2_to_180D_outcome":"failed_cleanroom_engineering_spike_no_backlog_bridge","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Cleanroom/engineering late-cycle spike without signed backlog and margin bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","residual_type":"EPC_cleanroom_contract_vocabulary_overcredit_without_order_backlog_margin_cash_bridge","contribution":"Adds two C05 4B counterexamples against one post-candidate energy-equipment backlog positive, avoiding C05 top-covered and recent L1 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"ENERGY_PLANT_EQUIPMENT_BACKLOG_MARGIN_BRIDGE_VS_EPC_CLEANROOM_CONTRACT_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C05 now has non-top-symbol energy-equipment backlog positive and two EPC/cleanroom vocabulary weak-bridge counterexamples; next C05 loops should exact-URL repair signed order, customer/project quality, delivery schedule, backlog conversion, margin-gap control, working-capital and cash evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_order_backlog_delivery_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"100840 worked only when order/backlog/delivery/margin proxy existed; 028050 and 037350 failed when EPC/cleanroom vocabulary lacked margin/cash bridge."}
{"row_type":"shadow_weight","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_EPC_cleanroom_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Large EPC/rebrand and cleanroom-engineering rows showed low MFE and MAE expansion when non-price signed-order and margin evidence was missing."}
{"row_type":"shadow_weight","round":"R1","loop":"91","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","axis":"C05_post_candidate_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"100840 has 2024 corporate-action candidate dates before the selected entry, so patch consideration needs price-path repair even though the post-candidate price path is usable for research."}
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
  - EPC_vocabulary_overcredit
  - cleanroom_engineering_theme_overcredit
  - signed_order_backlog_bridge_missing
  - margin_gap_cash_bridge_missing
  - post_candidate_data_quality_watch
new_axis_proposed:
  - C05_order_backlog_delivery_margin_cash_bridge_required_shadow_only
  - C05_EPC_cleanroom_vocabulary_local_4B_guard_shadow_only
  - C05_post_candidate_data_quality_guard_shadow_only
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
`100840` is selected only after its 2024 corporate-action candidate dates and is therefore usable for price-path residual analysis, but it must remain data-quality-watch before any production patch.  
`028050` has a 2024 name change from 삼성엔지니어링 to 삼성E&A before the selected entry, and older corporate-action candidates before 2024.  
`037350` has older corporate-action candidates long before the selected 2024 window.  
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 100840 post-candidate row
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
5. Confirm this loop avoided:
   - C05 top-covered symbols
   - previous R11 loop88 C05 symbols
   - previous R11 loop89 C02 symbols
   - previous R11 loop90 C03 symbols
   - previous R1 loop89 C03 symbols
   - previous R1 loop90 C04 symbols
6. Keep 100840 in post-candidate data-quality watch before patch consideration.
7. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C05-scoped safe patch candidates:
   - C05_order_backlog_delivery_margin_cash_bridge_required
   - C05_EPC_cleanroom_vocabulary_local_4B_guard
   - C05_post_candidate_data_quality_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R1
completed_loop = 91
next_round = R2
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C05_EPC_MEGA_CONTRACT_MARGIN_GAP.
```
