# E2R Stock-Web v12 Residual Research — R13 Loop 89 / Cross-Archetype 4B·4C Redteam

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R13
loop: 89
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: LOOP89_BRIDGE_PRESENT_POSITIVE_VS_WEAK_BRIDGE_THEME_PRICE_ONLY_GUARD
sector: cross-sector / 4B / 4C / data-quality / late-rebound guard
output_file: e2r_stock_web_v12_residual_round_R13_loop_89_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
new_independent_case_count: 0
do_not_count_as_new_case: true
do_not_propose_new_weight_delta: true
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R12 loop 89`.

```text
scheduled_round = R13
scheduled_loop = 89
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

R13 is a cross-redteam review round.  
It does **not** add fresh stock cases. It re-inspects the 36 trigger rows produced by R1~R12 loop89 and asks whether the same failure pattern keeps appearing across sectors:

```text
theme vocabulary without bridge
price-only MFE without non-price evidence
late rebound/spike pretending to validate an earlier weak entry
data-quality watch rows requiring repair before patching
Green-candidate rows that still need exact evidence
```

Therefore all R13 review rows are locked as:

```text
new_independent_case_count = 0
r13_do_not_count_as_new_case = true
independent_evidence_weight = 0.0
do_not_propose_new_weight_delta = true
```

## 2. Price source and validation scope

The reviewed source rows were generated from Songdaiki/stock-web 1D tradable raw OHLC shards.

```jsonl
{"row_type":"price_source_validation","round":"R13","loop":"89","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","validation_scope":"R13 reviews R1~R12 loop89 trigger rows; it does not create new price triggers."}
```

## 3. Reviewed loop89 material

Reviewed files:

```text
- e2r_stock_web_v12_residual_round_R10_loop_89_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
- e2r_stock_web_v12_residual_round_R11_loop_89_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
- e2r_stock_web_v12_residual_round_R12_loop_89_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
- e2r_stock_web_v12_residual_round_R1_loop_89_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
- e2r_stock_web_v12_residual_round_R2_loop_89_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
- e2r_stock_web_v12_residual_round_R3_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
- e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
- e2r_stock_web_v12_residual_round_R5_loop_89_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
- e2r_stock_web_v12_residual_round_R6_loop_89_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
- e2r_stock_web_v12_residual_round_R7_loop_89_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
- e2r_stock_web_v12_residual_round_R8_loop_89_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
- e2r_stock_web_v12_residual_round_R9_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

Summary:

```jsonl
{"row_type":"aggregate_metric","round":"R13","loop":"89","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":36,"reviewed_original_round_count":12,"reviewed_original_canonical_count":12,"positive_control_count":12,"counterexample_count":24,"positive_avg_MFE90_pct":54.69,"positive_avg_MAE90_pct":-7.38,"positive_avg_MFE180_pct":64.36,"positive_avg_MAE180_pct":-16.33,"counter_avg_MFE90_pct":12.19,"counter_avg_MAE90_pct":-22.94,"counter_avg_MFE180_pct":12.27,"counter_avg_MAE180_pct":-35.79,"counter_MFE90_lt_20_count":21,"counter_MFE90_ge_20_count":3,"counter_MAE90_le_minus20_count":12,"counter_MAE180_le_minus25_count":16,"price_only_like_count":21,"late_rebound_or_spike_not_validation_count":5,"data_quality_watch_count":4}
```

Interpretation:

```text
Bridge-present positive controls: avg MFE90 54.69% / avg MAE90 -7.38%.
Weak-bridge counterexamples: avg MFE90 12.19% / avg MAE90 -22.94%, avg MAE180 -35.79%.
Counterexamples with MFE90 < 20: 21 / 24.
Counterexamples with MFE90 >= 20 but still not positive evidence: 3 / 24.
Counterexamples with MAE180 <= -25: 16 / 24.
```

## 4. R13 research question

Across loop89, can the calibrated profile keep the door closed when price action is loud but the business bridge is missing?

The repeated answer is yes, but the guard needs to be made explicit for later batch planning:

```text
A high local MFE is not positive evidence if the row is price-only.
A late rebound is not original-entry validation.
A theme label is not an operating bridge.
Green-candidate rows still require exact source-grade non-price evidence.
Data-quality-watch rows must be repaired before production consideration.
```

The cross-sector mechanism is the same in every room of the factory.  
Price is the motor noise; the bridge is the belt that actually turns the machine. Without the belt, the RPM can spike and the output stays zero.

## 5. Cross-round case summary

```jsonl
{"row_type":"r13_cross_case","round":"R13","loop":"89","reviewed_round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","reviewed_trigger_count":3,"positive_control_symbols":["064350"],"counterexample_symbols":["099320","214430"],"avg_positive_MFE90_pct":24.64,"avg_counter_MFE90_pct":14.09,"avg_counter_MAE180_pct":-30.88,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"89","reviewed_round":"R2","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","reviewed_trigger_count":3,"positive_control_symbols":["403870"],"counterexample_symbols":["074600","166090"],"avg_positive_MFE90_pct":45.06,"avg_counter_MFE90_pct":4.28,"avg_counter_MAE180_pct":-62.54,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"89","reviewed_round":"R3","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","reviewed_trigger_count":3,"positive_control_symbols":["222080"],"counterexample_symbols":["089980","290670"],"avg_positive_MFE90_pct":37.36,"avg_counter_MFE90_pct":10.3,"avg_counter_MAE180_pct":-49.44,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"89","reviewed_round":"R4","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","reviewed_trigger_count":3,"positive_control_symbols":["001340"],"counterexample_symbols":["161000","298000"],"avg_positive_MFE90_pct":131.37,"avg_counter_MFE90_pct":1.22,"avg_counter_MAE180_pct":-57.67,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"89","reviewed_round":"R5","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reviewed_trigger_count":3,"positive_control_symbols":["005180"],"counterexample_symbols":["101530","248170"],"avg_positive_MFE90_pct":91.28,"avg_counter_MFE90_pct":6.3,"avg_counter_MAE180_pct":-43.72,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"89","reviewed_round":"R6","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reviewed_trigger_count":3,"positive_control_symbols":["024110"],"counterexample_symbols":["001200","001510"],"avg_positive_MFE90_pct":34.88,"avg_counter_MFE90_pct":25.7,"avg_counter_MAE180_pct":-31.16,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"89","reviewed_round":"R7","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reviewed_trigger_count":3,"positive_control_symbols":["200670"],"counterexample_symbols":["119610","290650"],"avg_positive_MFE90_pct":25.25,"avg_counter_MFE90_pct":9.36,"avg_counter_MAE180_pct":-34.23,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"89","reviewed_round":"R8","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","reviewed_trigger_count":3,"positive_control_symbols":["060850"],"counterexample_symbols":["067920","304100"],"avg_positive_MFE90_pct":25.22,"avg_counter_MFE90_pct":16.45,"avg_counter_MAE180_pct":-43.77,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"89","reviewed_round":"R9","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_count":3,"positive_control_symbols":["064960"],"counterexample_symbols":["012860","067570"],"avg_positive_MFE90_pct":15.1,"avg_counter_MFE90_pct":12.69,"avg_counter_MAE180_pct":-28.08,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"89","reviewed_round":"R10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_count":3,"positive_control_symbols":["004980"],"counterexample_symbols":["006920","007110"],"avg_positive_MFE90_pct":18.1,"avg_counter_MFE90_pct":22.94,"avg_counter_MAE180_pct":-9.78,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"89","reviewed_round":"R11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reviewed_trigger_count":3,"positive_control_symbols":["229640"],"counterexample_symbols":["006910","199820"],"avg_positive_MFE90_pct":131.12,"avg_counter_MFE90_pct":12.85,"avg_counter_MAE180_pct":-16.82,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"89","reviewed_round":"R12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reviewed_trigger_count":3,"positive_control_symbols":["071320"],"counterexample_symbols":["035250","039130"],"avg_positive_MFE90_pct":76.9,"avg_counter_MFE90_pct":10.12,"avg_counter_MAE180_pct":-21.45,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
```

## 6. R13 review trigger rows

```jsonl
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R1","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","reviewed_trigger_id":"R1L89_C03_064350_20240222_STAGE2_DEFENSE_EXPORT_BACKLOG","symbol":"064350","company_name":"현대로템","entry_date":"2024-02-22","entry_price":34500.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":24.64,"MAE_90D_pct":-13.33,"MFE_180D_pct":101.45,"MAE_180D_pct":-13.33,"trigger_outcome_label":"positive_high_MFE90_and_very_high_MFE180_moderate_MAE","current_profile_verdict":"current_profile_correct_if_export_framework_backlog_margin_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R1_loop_89_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R1","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","reviewed_trigger_id":"R1L89_C03_099320_20240424_STAGE2_FALSE_POSITIVE_SPACE_DEFENSE_THEME","symbol":"099320","company_name":"쎄트렉아이","entry_date":"2024-04-24","entry_price":49300.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":18.66,"MAE_90D_pct":-9.94,"MFE_180D_pct":18.66,"MAE_180D_pct":-28.5,"trigger_outcome_label":"counterexample_sub_Yellow_MFE90_deep_180D_MAE_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_space_defense_theme_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R1_loop_89_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R1","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","reviewed_trigger_id":"R1L89_C03_214430_20240325_STAGE2_FALSE_POSITIVE_DEFENSE_SENSOR_THEME","symbol":"214430","company_name":"아이쓰리시스템","entry_date":"2024-03-25","entry_price":46750.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":9.52,"MAE_90D_pct":-18.5,"MFE_180D_pct":9.52,"MAE_180D_pct":-33.26,"trigger_outcome_label":"counterexample_low_MFE90_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_sensor_theme_spike_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R1_loop_89_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R2","reviewed_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","reviewed_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","reviewed_trigger_id":"R2L89_C10_074600_20240607_STAGE2_FALSE_POSITIVE_QUARTZ_MATERIALS_SPIKE","symbol":"074600","company_name":"원익QnC","entry_date":"2024-06-07","entry_price":40950.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":0.12,"MAE_90D_pct":-41.76,"MFE_180D_pct":0.12,"MAE_180D_pct":-59.27,"trigger_outcome_label":"counterexample_near_zero_MFE_extreme_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_quartz_materials_spike_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R2_loop_89_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R2","reviewed_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","reviewed_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","reviewed_trigger_id":"R2L89_C10_166090_20240626_STAGE2_FALSE_POSITIVE_PARTS_LATE_CYCLE","symbol":"166090","company_name":"하나머티리얼즈","entry_date":"2024-06-26","entry_price":63900.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":8.45,"MAE_90D_pct":-53.83,"MFE_180D_pct":8.45,"MAE_180D_pct":-65.81,"trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_parts_late_cycle_extension_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R2_loop_89_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R2","reviewed_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","reviewed_canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","reviewed_trigger_id":"R2L89_C10_403870_20240118_STAGE2_HBM_EQUIPMENT_RAMP","symbol":"403870","company_name":"HPSP","entry_date":"2024-01-18","entry_price":44050.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":45.06,"MAE_90D_pct":-19.07,"MFE_180D_pct":45.06,"MAE_180D_pct":-36.44,"trigger_outcome_label":"positive_high_MFE90_moderate_late_MAE","current_profile_verdict":"current_profile_correct_if_customer_ramp_shipment_margin_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R2_loop_89_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R3","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","reviewed_trigger_id":"R3L89_C11_089980_20240522_STAGE2_FALSE_POSITIVE_SEPARATOR_MATERIALS","symbol":"089980","company_name":"상아프론테크","entry_date":"2024-05-22","entry_price":26350.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":11.39,"MAE_90D_pct":-18.03,"MFE_180D_pct":11.39,"MAE_180D_pct":-32.79,"trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_separator_materials_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R3_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R3","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","reviewed_trigger_id":"R3L89_C11_222080_20240215_STAGE2_BATTERY_EQUIPMENT_ORDERBOOK","symbol":"222080","company_name":"씨아이에스","entry_date":"2024-02-15","entry_price":11000.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":37.36,"MAE_90D_pct":-9.09,"MFE_180D_pct":37.36,"MAE_180D_pct":-28.0,"trigger_outcome_label":"positive_MFE90_ge30_tolerable_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_orderbook_customer_ramp_margin_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R3_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R3","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","reviewed_trigger_id":"R3L89_C11_290670_20240221_STAGE2_FALSE_POSITIVE_MAGNETIC_EQUIPMENT","symbol":"290670","company_name":"대보마그네틱","entry_date":"2024-02-21","entry_price":30400.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":9.21,"MAE_90D_pct":-33.06,"MFE_180D_pct":9.21,"MAE_180D_pct":-66.09,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_without_order_bridge","current_profile_verdict":"current_profile_false_positive_if_equipment_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R3_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R4","reviewed_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","reviewed_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","reviewed_trigger_id":"R4L89_C17_001340_20240522_STAGE2_CHLOR_ALKALI_SPREAD","symbol":"001340","company_name":"백광산업","entry_date":"2024-05-22","entry_price":7970.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":131.37,"MAE_90D_pct":-10.04,"MFE_180D_pct":131.37,"MAE_180D_pct":-17.82,"trigger_outcome_label":"positive_very_high_MFE_tolerable_MAE_resume_watch","current_profile_verdict":"current_profile_correct_if_spread_ASP_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R4","reviewed_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","reviewed_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","reviewed_trigger_id":"R4L89_C17_161000_20240102_STAGE2_FALSE_POSITIVE_BATTERY_CHEM_REBOUND","symbol":"161000","company_name":"애경케미칼","entry_date":"2024-01-02","entry_price":16740.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":2.21,"MAE_90D_pct":-28.26,"MFE_180D_pct":2.21,"MAE_180D_pct":-61.11,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_battery_chemical_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R4","reviewed_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","reviewed_canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","reviewed_trigger_id":"R4L89_C17_298000_20240102_STAGE2_FALSE_POSITIVE_PETROCHEM_REBOUND","symbol":"298000","company_name":"효성화학","entry_date":"2024-01-02","entry_price":86300.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":0.23,"MAE_90D_pct":-31.4,"MFE_180D_pct":0.23,"MAE_180D_pct":-54.23,"trigger_outcome_label":"counterexample_near_zero_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_petrochemical_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R5","reviewed_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","reviewed_canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reviewed_trigger_id":"R5L89_C18_005180_20240415_STAGE2_KFOOD_EXPORT_REORDER","symbol":"005180","company_name":"빙그레","entry_date":"2024-04-15","entry_price":61900.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":91.28,"MAE_90D_pct":-6.62,"MFE_180D_pct":91.28,"MAE_180D_pct":-6.62,"trigger_outcome_label":"positive_very_high_MFE_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_export_reorder_sellthrough_margin_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R5_loop_89_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R5","reviewed_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","reviewed_canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reviewed_trigger_id":"R5L89_C18_101530_20240614_STAGE2_FALSE_POSITIVE_SNACK_LATE_THEME","symbol":"101530","company_name":"해태제과식품","entry_date":"2024-06-14","entry_price":9310.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":1.5,"MAE_90D_pct":-41.46,"MFE_180D_pct":1.5,"MAE_180D_pct":-41.89,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_after_late_spike","current_profile_verdict":"current_profile_false_positive_if_snack_theme_spike_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R5_loop_89_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R5","reviewed_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","reviewed_canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reviewed_trigger_id":"R5L89_C18_248170_20240620_STAGE2_FALSE_POSITIVE_SAUCE_EXPORT_THEME","symbol":"248170","company_name":"샘표식품","entry_date":"2024-06-20","entry_price":40950.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":11.11,"MAE_90D_pct":-32.11,"MFE_180D_pct":11.11,"MAE_180D_pct":-45.54,"trigger_outcome_label":"counterexample_local_MFE_but_deep_MAE_no_reorder_bridge","current_profile_verdict":"current_profile_false_positive_if_sauce_export_theme_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R5_loop_89_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R6","reviewed_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","reviewed_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reviewed_trigger_id":"R6L89_C21_001200_20240222_STAGE2_FALSE_POSITIVE_BROKERAGE_PRICE_BLOWOFF","symbol":"001200","company_name":"유진투자증권","entry_date":"2024-02-22","entry_price":4365.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":47.99,"MAE_90D_pct":-12.49,"MFE_180D_pct":47.99,"MAE_180D_pct":-39.75,"trigger_outcome_label":"counterexample_price_only_high_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_brokerage_price_blowoff_counted_as_capital_return","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R6_loop_89_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R6","reviewed_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","reviewed_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reviewed_trigger_id":"R6L89_C21_001510_20240201_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_REBOUND","symbol":"001510","company_name":"SK증권","entry_date":"2024-02-01","entry_price":647.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":3.4,"MAE_90D_pct":-13.91,"MFE_180D_pct":3.4,"MAE_180D_pct":-22.57,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_small_brokerage_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R6_loop_89_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R6","reviewed_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","reviewed_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reviewed_trigger_id":"R6L89_C21_024110_20240124_STAGE2_BANK_VALUEUP_CAPITAL_RETURN","symbol":"024110","company_name":"기업은행","entry_date":"2024-01-24","entry_price":11870.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":34.88,"MAE_90D_pct":-1.68,"MFE_180D_pct":34.88,"MAE_180D_pct":-1.68,"trigger_outcome_label":"positive_MFE90_ge30_shallow_MAE","current_profile_verdict":"current_profile_correct_if_ROE_PBR_capital_return_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R6_loop_89_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R7","reviewed_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","reviewed_canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reviewed_trigger_id":"R7L89_C25_119610_20240131_STAGE2_FALSE_POSITIVE_CONTACT_LENS_WEAK_BRIDGE","symbol":"119610","company_name":"인터로조","entry_date":"2024-01-31","entry_price":29400.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":17.52,"MAE_90D_pct":-20.75,"MFE_180D_pct":17.52,"MAE_180D_pct":-20.75,"trigger_outcome_label":"counterexample_sub_Yellow_MFE_partial_window_deep_MAE_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_contact_lens_export_theme_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R7_loop_89_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R7","reviewed_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","reviewed_canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reviewed_trigger_id":"R7L89_C25_200670_20240325_STAGE2_AESTHETIC_EXPORT_MARGIN","symbol":"200670","company_name":"휴메딕스","entry_date":"2024-03-25","entry_price":29700.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":25.25,"MAE_90D_pct":-7.41,"MFE_180D_pct":55.56,"MAE_180D_pct":-14.14,"trigger_outcome_label":"positive_MFE90_ge25_MFE180_ge55_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_export_reimbursement_margin_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R7_loop_89_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R7","reviewed_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","reviewed_canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reviewed_trigger_id":"R7L89_C25_290650_20240102_STAGE2_FALSE_POSITIVE_BIOMATERIAL_REBOUND","symbol":"290650","company_name":"엘앤씨바이오","entry_date":"2024-01-02","entry_price":29150.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":1.2,"MAE_90D_pct":-30.7,"MFE_180D_pct":1.2,"MAE_180D_pct":-47.72,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_biomaterial_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R7_loop_89_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R8","reviewed_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","reviewed_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","reviewed_trigger_id":"R8L89_C28_060850_20240102_STAGE2_ERP_SAAS_RETENTION","symbol":"060850","company_name":"영림원소프트랩","entry_date":"2024-01-02","entry_price":9000.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":25.22,"MAE_90D_pct":-8.33,"MFE_180D_pct":25.22,"MAE_180D_pct":-43.33,"trigger_outcome_label":"positive_MFE90_ge20_controlled_90D_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_contract_retention_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R8_loop_89_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R8","reviewed_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","reviewed_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","reviewed_trigger_id":"R8L89_C28_067920_20240119_STAGE2_FALSE_POSITIVE_SECURITY_THEME","symbol":"067920","company_name":"이글루","entry_date":"2024-01-19","entry_price":7310.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":18.74,"MAE_90D_pct":-23.67,"MFE_180D_pct":18.74,"MAE_180D_pct":-35.29,"trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_security_theme_spike_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R8_loop_89_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R8","reviewed_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","reviewed_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","reviewed_trigger_id":"R8L89_C28_304100_20240105_STAGE2_FALSE_POSITIVE_AI_SOFTWARE_BLOWOFF","symbol":"304100","company_name":"솔트룩스","entry_date":"2024-01-05","entry_price":31450.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":14.15,"MAE_90D_pct":-25.44,"MFE_180D_pct":14.15,"MAE_180D_pct":-52.24,"trigger_outcome_label":"counterexample_price_only_local_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_AI_software_blowoff_counted_as_contract_retention","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R8_loop_89_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R9","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_id":"R9L89_C29_012860_20240205_STAGE2_FALSE_POSITIVE_AUTO_ELECTRONICS_SPIKE","symbol":"012860","company_name":"모베이스전자","entry_date":"2024-02-05","entry_price":2100.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":13.81,"MAE_90D_pct":-15.24,"MFE_180D_pct":13.81,"MAE_180D_pct":-38.81,"trigger_outcome_label":"counterexample_local_MFE_but_deep_MAE_no_order_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_auto_electronics_price_spike_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R9_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R9","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_id":"R9L89_C29_064960_20240129_STAGE2_AUTOMOTOR_VOLUME_MIX_CASH","symbol":"064960","company_name":"SNT모티브","entry_date":"2024-01-29","entry_price":43700.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":15.1,"MAE_90D_pct":-1.26,"MFE_180D_pct":15.1,"MAE_180D_pct":-9.15,"trigger_outcome_label":"positive_moderate_MFE_low_MAE_stability_case","current_profile_verdict":"current_profile_correct_if_volume_mix_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R9_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R9","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_id":"R9L89_C29_067570_20240206_STAGE2_FALSE_POSITIVE_NVH_REBOUND","symbol":"067570","company_name":"엔브이에이치코리아","entry_date":"2024-02-06","entry_price":2595.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":11.56,"MAE_90D_pct":-17.34,"MFE_180D_pct":11.56,"MAE_180D_pct":-17.34,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_NVH_interior_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R9_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R10","reviewed_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","reviewed_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_id":"R10L89_C30_004980_20240201_STAGE2_CEMENT_MARGIN_CASH","symbol":"004980","company_name":"성신양회","entry_date":"2024-02-01","entry_price":8120.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":18.1,"MAE_90D_pct":-1.85,"MFE_180D_pct":18.1,"MAE_180D_pct":-15.64,"trigger_outcome_label":"watch_positive_MFE90_ge15_low_early_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_materials_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R10_loop_89_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R10","reviewed_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","reviewed_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_id":"R10L89_C30_006920_20240223_STAGE2_FALSE_POSITIVE_READY_MIX_BLOWOFF","symbol":"006920","company_name":"모헨즈","entry_date":"2024-02-23","entry_price":3775.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":40.13,"MAE_90D_pct":-5.17,"MFE_180D_pct":40.13,"MAE_180D_pct":-5.17,"trigger_outcome_label":"counterexample_price_only_MFE_deep_MAE_no_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_ready_mix_policy_blowoff_counted_as_C30_bridge","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R10_loop_89_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R10","reviewed_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","reviewed_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_id":"R10L89_C30_007110_20240112_STAGE2_FALSE_POSITIVE_STONE_POLICY","symbol":"007110","company_name":"일신석재","entry_date":"2024-01-12","entry_price":1238.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":5.74,"MAE_90D_pct":-14.38,"MFE_180D_pct":5.74,"MAE_180D_pct":-14.38,"trigger_outcome_label":"counterexample_low_original_MFE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_policy_theme_spike_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R10_loop_89_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R11","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reviewed_trigger_id":"R11L89_C02_006910_20240222_STAGE2_FALSE_POSITIVE_POWER_POLICY","symbol":"006910","company_name":"보성파워텍","entry_date":"2024-02-22","entry_price":3275.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":4.73,"MAE_90D_pct":-12.82,"MFE_180D_pct":6.72,"MAE_180D_pct":-13.28,"trigger_outcome_label":"counterexample_price_only_MFE_deep_MAE_no_grid_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_power_policy_rebound_counted_as_C02_bridge","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R11_loop_89_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R11","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reviewed_trigger_id":"R11L89_C02_199820_20240920_STAGE2_FALSE_POSITIVE_SWITCHGEAR_THEME","symbol":"199820","company_name":"제일일렉트릭","entry_date":"2024-09-20","entry_price":9870.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":20.97,"MAE_90D_pct":-20.36,"MFE_180D_pct":20.97,"MAE_180D_pct":-20.36,"trigger_outcome_label":"counterexample_local_MFE_post_candidate_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_switchgear_theme_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R11_loop_89_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R11","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reviewed_trigger_id":"R11L89_C02_229640_20240422_STAGE2_POWER_CABLE_EXPORT_GRID","symbol":"229640","company_name":"LS에코에너지","entry_date":"2024-04-22","entry_price":19600.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":131.12,"MAE_90D_pct":-4.69,"MFE_180D_pct":131.12,"MAE_180D_pct":-4.69,"trigger_outcome_label":"positive_very_high_MFE_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_orderbook_export_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R11_loop_89_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R12","reviewed_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","reviewed_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reviewed_trigger_id":"R12L89_C31_035250_20240206_STAGE2_FALSE_POSITIVE_CASINO_POLICY","symbol":"035250","company_name":"강원랜드","entry_date":"2024-02-06","entry_price":16560.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":9.42,"MAE_90D_pct":-11.78,"MFE_180D_pct":9.42,"MAE_180D_pct":-17.15,"trigger_outcome_label":"counterexample_low_MFE_moderate_MAE_no_policy_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_casino_policy_theme_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R12_loop_89_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R12","reviewed_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","reviewed_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reviewed_trigger_id":"R12L89_C31_039130_20240131_STAGE2_FALSE_POSITIVE_TRAVEL_POLICY","symbol":"039130","company_name":"하나투어","entry_date":"2024-01-31","entry_price":63700.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":10.83,"MAE_90D_pct":-18.05,"MFE_180D_pct":10.83,"MAE_180D_pct":-25.75,"trigger_outcome_label":"counterexample_low_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_travel_policy_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R12_loop_89_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"89","reviewed_round":"R12","reviewed_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","reviewed_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reviewed_trigger_id":"R12L89_C31_071320_20240126_STAGE2_UTILITY_TARIFF_VALUEUP","symbol":"071320","company_name":"지역난방공사","entry_date":"2024-01-26","entry_price":29000.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":76.9,"MAE_90D_pct":-5.17,"MFE_180D_pct":85.86,"MAE_180D_pct":-5.17,"trigger_outcome_label":"positive_very_high_MFE_low_MAE_policy_bridge","current_profile_verdict":"current_profile_correct_if_tariff_cost_recovery_capital_return_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R12_loop_89_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
```

## 7. Guardrail stress-test results

```jsonl
{"row_type":"r13_guardrail_summary","round":"R13","loop":"89","guardrail_id":"bridge_missing_price_only_4B_guard","reviewed_trigger_count":36,"positive_control_count":12,"counterexample_count":24,"counter_MFE90_lt_20_count":21,"counter_MFE90_ge_20_price_only_count":3,"counter_MAE90_le_minus20_count":12,"counter_MAE180_le_minus25_count":16,"price_only_like_count":21,"late_rebound_or_spike_not_validation_count":5,"data_quality_watch_count":4,"verdict":"existing calibrated axes are directionally correct; do not loosen Green; future batch can add canonical bridge-required guards as shadow-only candidates."}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"89","rule_candidate":"cross_archetype_bridge_missing_hard_4B_watch","condition":"bridge_missing_or_unverified AND (MFE90 < 20 OR MAE180 <= -25 OR evidence_type includes price_only)","action":"block Stage2-Actionable/Yellow/Green; route to Watch/4B/evidence repair","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"89","rule_candidate":"late_rebound_not_entry_validation","condition":"original_entry_bridge_missing AND later_full_window_or_Q4_spike_occurs","action":"do not retroactively validate original entry; require fresh trigger date and fresh non-price bridge evidence","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"89","rule_candidate":"data_quality_watch_pre_patch_guard","condition":"corporate_action_candidate_or_partial_window_or_resume_watch_present","action":"allow research annotation but block production patch until price path and exact evidence are repaired","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"89","rule_candidate":"Green_requires_exact_non_price_bridge","condition":"positive_control_has_high_MFE_but_source_proxy_only_or_late_drawdown_watch","action":"allow Yellow/Green-candidate-watch only; exact source-grade bridge required before Green","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
```

## 8. Sector-by-sector redteam notes

```text
R1 / C03 defense:
  064350 confirms export-framework/backlog bridge. 099320 and 214430 show space/sensor defense labels without export/backlog/margin bridge should stay Watch/4B.

R2 / C10 memory equipment:
  403870 confirms HBM equipment customer-ramp bridge. 166090 and 074600 show parts/materials late-cycle labels collapse without fresh order, utilization and margin bridge.

R3 / C11 battery orderbook:
  222080 confirms equipment orderbook/customer-ramp bridge. 290670 and 089980 show material/equipment rebound without orderbook and call-off bridge should not be promoted.

R4 / C17 chemical spread:
  001340 confirms spread/ASP/margin bridge but has resume/data-quality watch. 298000 and 161000 show commodity rebound labels failing without spread/cash bridge.

R5 / C18 consumer export reorder:
  005180 confirms export-channel/reorder bridge. 101530 and 248170 show food theme spikes fail without sell-through, reorder, SKU velocity and margin.

R6 / C21 financial capital return:
  024110 confirms bank value-up/capital-return bridge. 001510 and 001200 show brokerage rebound or price-only MFE is not ROE/capital-return evidence.

R7 / C25 medical device:
  200670 confirms export/reimbursement/margin bridge. 119610 and 290650 show contact-lens/biomaterial labels need accounting, reimbursement, channel, margin and cash repair.

R8 / C28 software/security:
  060850 confirms ERP/SaaS renewal bridge. 067920 and 304100 show security/AI software MFE is not ARR/renewal/enterprise-retention evidence.

R9 / C29 mobility:
  064960 is only a Yellow-watch positive-control. 067570 and 012860 show local MFE or late spike does not prove OEM volume/order/margin bridge.

R10 / C30 construction/PF:
  004980 is only a Yellow-watch materials-margin/cash bridge. 007110 and 006920 show policy/materials MFE without PF/liquidity/backlog/cash bridge is 4B.

R11 / C02 grid/datacenter:
  229640 confirms export cable/grid CAPEX bridge. 199820 and 006910 show switchgear/power-policy themes need orderbook/delivery/margin repair.

R12 / C31 policy:
  071320 confirms policy-to-cash tariff/value-up bridge. 035250 and 039130 show tourism/casino policy vocabulary without demand/payout/margin/cash bridge stays 4B.
```

## 9. Shadow-only recommendations

```jsonl
{"row_type":"shadow_weight","round":"R13","loop":"89","axis":"cross_archetype_bridge_required_before_Yellow","scope":"cross_archetype","candidate_delta":0.0,"direction":"diagnostic_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Across 24 counterexamples, missing bridge rows averaged MFE90 12.19% and MAE180 -35.79%; bridge-present positives averaged MFE90 54.69%."}
{"row_type":"shadow_weight","round":"R13","loop":"89","axis":"cross_archetype_price_only_MFE_not_positive_evidence","scope":"cross_archetype","candidate_delta":0.0,"direction":"diagnostic_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Counterexamples such as 006920, 001200, 199820 and 012860 show MFE can be price-only when non-price bridge evidence is missing."}
{"row_type":"shadow_weight","round":"R13","loop":"89","axis":"cross_archetype_late_rebound_not_original_entry_validation","scope":"cross_archetype","candidate_delta":0.0,"direction":"diagnostic_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Late spike/rebound flags appeared in multiple rows; the original weak entry should not be upgraded unless a fresh trigger date and bridge evidence exist."}
{"row_type":"shadow_weight","round":"R13","loop":"89","axis":"cross_archetype_data_quality_repair_before_patch","scope":"cross_archetype","candidate_delta":0.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"001340, 099320, 119610 and 199820 carry data-quality or partial-window watch flags."}
```

## 10. Residual Contribution Summary

```text
new_independent_case_count: 0
reused_case_count: 36
reviewed_trigger_count: 36
reviewed_original_round_count: 12
reviewed_original_canonical_count: 12
positive_control_count: 12
counterexample_count: 24
do_not_count_as_new_case: true
independent_evidence_weight: 0.0
do_not_propose_new_weight_delta: true

tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - stage3_green_total_min
  - stage3_green_revision_min

residual_error_types_confirmed:
  - theme_label_overcredit
  - bridge_missing_or_unverified
  - price_only_MFE_overcredit
  - late_rebound_not_entry_validation
  - data_quality_watch_before_patch
  - source_proxy_only_before_Green

diagnostic_axis_proposed:
  - cross_archetype_bridge_missing_hard_4B_watch
  - cross_archetype_price_only_MFE_not_positive_evidence
  - cross_archetype_late_rebound_not_entry_validation
  - cross_archetype_data_quality_repair_before_patch
  - Green_requires_exact_non_price_bridge

existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
R13_cross_redteam_rule_candidate: true
loop_contribution_label: axis_stress_test_passed
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this R13 MD only as a cross-redteam review artifact.
2. Do not count any r13_review_trigger as a new independent case.
3. Confirm reviewed rows came from R1~R12 loop89 MDs.
4. Confirm all reviewed source rows use:
   - price_data_source=Songdaiki/stock-web
   - price_basis=tradable_raw
   - price_adjustment_status=raw_unadjusted_marcap
5. Confirm R13 / L10 / R13_CROSS_ARCHETYPE_4B_4C_REDTEAM round-sector consistency.
6. Treat all recommendations here as shadow-only diagnostics.
7. Do not apply weight deltas from this MD alone.
8. Use this MD to prioritize exact evidence repair and canonical guard design:
   - bridge_missing_hard_4B_watch
   - price_only_MFE_not_positive_evidence
   - late_rebound_not_entry_validation
   - data_quality_repair_before_patch
   - Green_requires_exact_non_price_bridge
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
```

## 12. Round state

```text
completed_round = R13
completed_loop = 89
next_round = R1
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 13. Final one-line contribution

```text
This R13 loop reviews 36 loop89 triggers across R1~R12, adds 0 new independent cases, and confirms that bridge-missing / price-only / late-rebound / data-quality guards should remain hard Watch/4B barriers before any Yellow/Green promotion.
```
