# E2R Stock-Web v12 Residual Research — R13 Loop 90 / Cross-Archetype 4B·4C Redteam

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R13
loop: 90
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: LOOP90_BRIDGE_PRESENT_POSITIVE_VS_WEAK_BRIDGE_THEME_PRICE_ONLY_GUARD
sector: cross-sector / 4B / 4C / bridge-missing / price-only / data-quality / Green strictness
output_file: e2r_stock_web_v12_residual_round_R13_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
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

This run follows the v12 sequential scheduler after completed `R12 loop 90`.

```text
scheduled_round = R13
scheduled_loop = 90
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

R13 is not a fresh symbol-mining round.  
It is a cross-archetype redteam checkpoint that reviews the 36 trigger rows produced by R1~R12 loop90.

All R13 review rows are locked as:

```text
new_independent_case_count = 0
r13_do_not_count_as_new_case = true
independent_evidence_weight = 0.0
do_not_propose_new_weight_delta = true
production_scoring_changed = false
shadow_weight_only = true
```

No-Repeat Index reminder:

```text
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM already exists as a review archetype.
This run does not add independent cases to the registry; it adds a cross-check artifact only.
```

## 2. Price source and validation scope

The reviewed rows were already built from Songdaiki/stock-web 1D tradable raw OHLC shards.

```jsonl
{"row_type":"price_source_validation","round":"R13","loop":"90","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","validation_scope":"R13 reviews R1~R12 loop90 trigger rows; it does not create new price triggers."}
```

Reviewed files:

```text
- e2r_stock_web_v12_residual_round_R1_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
- e2r_stock_web_v12_residual_round_R2_loop_90_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
- e2r_stock_web_v12_residual_round_R3_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
- e2r_stock_web_v12_residual_round_R4_loop_90_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
- e2r_stock_web_v12_residual_round_R5_loop_90_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
- e2r_stock_web_v12_residual_round_R6_loop_90_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
- e2r_stock_web_v12_residual_round_R7_loop_90_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
- e2r_stock_web_v12_residual_round_R8_loop_90_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
- e2r_stock_web_v12_residual_round_R9_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
- e2r_stock_web_v12_residual_round_R10_loop_90_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
- e2r_stock_web_v12_residual_round_R11_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
- e2r_stock_web_v12_residual_round_R12_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

## 3. Aggregate redteam statistics

```jsonl
{"row_type":"aggregate_metric","round":"R13","loop":"90","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":36,"reviewed_source_file_count":12,"reviewed_original_round_count":12,"reviewed_original_canonical_count":12,"positive_control_count":12,"counterexample_count":24,"positive_avg_MFE90_pct":60.55,"positive_avg_MAE90_pct":-5.14,"positive_avg_MFE180_pct":66.19,"positive_avg_MAE180_pct":-16.39,"counter_avg_MFE90_pct":9.25,"counter_avg_MAE90_pct":-23.51,"counter_avg_MFE180_pct":9.27,"counter_avg_MAE180_pct":-45.09,"counter_MFE90_lt_20_count":22,"counter_MFE90_ge_20_count":2,"counter_MAE90_le_minus20_count":13,"counter_MAE180_le_minus25_count":21,"counter_MAE180_le_minus35_count":18,"price_only_like_count":12,"late_rebound_or_spike_not_validation_count":1,"data_quality_watch_count":4,"source_proxy_only_count":36,"evidence_url_pending_count":36}
```

Interpretation:

```text
Bridge-present positive controls: avg MFE90 60.55% / avg MAE90 -5.14%.
Bridge-present positives avg MFE180 66.19% / avg MAE180 -16.39%.

Weak-bridge counterexamples: avg MFE90 9.25% / avg MAE90 -23.51%.
Weak-bridge counterexamples avg MFE180 9.27% / avg MAE180 -45.09%.

Counterexamples with MFE90 < 20: 22 / 24.
Counterexamples with MFE90 >= 20 but still not positive evidence: 2 / 24.
Counterexamples with MAE180 <= -25: 21 / 24.
Counterexamples with MAE180 <= -35: 18 / 24.
Price-only-like evidence flags: 12.
Data-quality / recent-listing / segment-change watch flags: 4.
```

## 4. R13 research question

Across loop90, can the calibrated profile keep Stage2/Yellow/Green closed when a case has loud price action but no business bridge?

The answer is directionally yes. The repeated error shape is stable across sectors:

```text
theme label without bridge
local MFE without non-price evidence
late rebound/spike pretending to validate the original weak entry
data-quality / recent-listing / share-count drift before patching
Green-candidate rows that still require exact source-grade non-price evidence
```

The mechanism is the same whether the room is defense, HBM, battery, materials, consumer, insurance, bio, content, mobility, construction, or governance.  
Price is the engine noise. The bridge is the driveshaft. Without the driveshaft, RPM rises and the wheel does not move.

## 5. Cross-round case summary

```jsonl
{"row_type":"r13_cross_case","round":"R13","loop":"90","reviewed_round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","reviewed_trigger_count":3,"positive_control_symbols":["130660"],"counterexample_symbols":["019990","105840"],"avg_positive_MFE90_pct":176.2,"avg_counter_MFE90_pct":12.69,"avg_counter_MAE180_pct":-40.03,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"90","reviewed_round":"R2","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","reviewed_trigger_count":3,"positive_control_symbols":["036540"],"counterexample_symbols":["033170","394280"],"avg_positive_MFE90_pct":37.67,"avg_counter_MFE90_pct":12.8,"avg_counter_MAE180_pct":-70.21,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"90","reviewed_round":"R3","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","reviewed_trigger_count":3,"positive_control_symbols":["114190"],"counterexample_symbols":["417200","450080"],"avg_positive_MFE90_pct":64.41,"avg_counter_MFE90_pct":5.39,"avg_counter_MAE180_pct":-74.03,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"90","reviewed_round":"R4","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reviewed_trigger_count":3,"positive_control_symbols":["128660"],"counterexample_symbols":["009520","018470"],"avg_positive_MFE90_pct":62.59,"avg_counter_MFE90_pct":7.75,"avg_counter_MAE180_pct":-43.89,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"90","reviewed_round":"R5","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","reviewed_trigger_count":3,"positive_control_symbols":["090430"],"counterexample_symbols":["020000","383220"],"avg_positive_MFE90_pct":48.52,"avg_counter_MFE90_pct":0.82,"avg_counter_MAE180_pct":-32.7,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"90","reviewed_round":"R6","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reviewed_trigger_count":3,"positive_control_symbols":["032830"],"counterexample_symbols":["000400","088350"],"avg_positive_MFE90_pct":73.32,"avg_counter_MFE90_pct":8.18,"avg_counter_MAE180_pct":-38.44,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"90","reviewed_round":"R7","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","reviewed_trigger_count":3,"positive_control_symbols":["237690"],"counterexample_symbols":["256840","365270"],"avg_positive_MFE90_pct":49.32,"avg_counter_MFE90_pct":16.41,"avg_counter_MAE180_pct":-63.77,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"90","reviewed_round":"R8","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","reviewed_trigger_count":3,"positive_control_symbols":["035760"],"counterexample_symbols":["206560","241840"],"avg_positive_MFE90_pct":34.29,"avg_counter_MFE90_pct":3.68,"avg_counter_MAE180_pct":-47.36,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"90","reviewed_round":"R9","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_count":3,"positive_control_symbols":["092780"],"counterexample_symbols":["013870","126640"],"avg_positive_MFE90_pct":55.29,"avg_counter_MFE90_pct":3.5,"avg_counter_MAE180_pct":-20.7,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"90","reviewed_round":"R10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_count":3,"positive_control_symbols":["300720"],"counterexample_symbols":["014280","023410"],"avg_positive_MFE90_pct":46.15,"avg_counter_MFE90_pct":8.71,"avg_counter_MAE180_pct":-28.95,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"90","reviewed_round":"R11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","reviewed_trigger_count":3,"positive_control_symbols":["272210"],"counterexample_symbols":["095190","218410"],"avg_positive_MFE90_pct":32.53,"avg_counter_MFE90_pct":27.29,"avg_counter_MAE180_pct":-42.34,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"90","reviewed_round":"R12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reviewed_trigger_count":3,"positive_control_symbols":["008930"],"counterexample_symbols":["003030","006840"],"avg_positive_MFE90_pct":46.35,"avg_counter_MFE90_pct":3.81,"avg_counter_MAE180_pct":-38.67,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
```

## 6. R13 review trigger rows

```jsonl
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R1","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","reviewed_trigger_id":"R1L90_C04_019990_20240222_STAGE2_FALSE_POSITIVE_ACTUATOR_POLICY_REBOUND","symbol":"019990","company_name":"에너토크","entry_date":"2024-02-22","entry_price":6940.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":2.31,"MAE_90D_pct":-18.44,"MFE_180D_pct":2.74,"MAE_180D_pct":-41.93,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_actuator_policy_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R1_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R1","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","reviewed_trigger_id":"R1L90_C04_105840_20240522_STAGE2_FALSE_POSITIVE_INSTRUMENTATION_THEME","symbol":"105840","company_name":"우진","entry_date":"2024-05-22","entry_price":9100.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":23.08,"MAE_90D_pct":-12.2,"MFE_180D_pct":23.08,"MAE_180D_pct":-38.13,"trigger_outcome_label":"counterexample_price_only_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_instrumentation_theme_MFE_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R1_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R1","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","reviewed_trigger_id":"R1L90_C04_130660_20240422_STAGE2_NUCLEAR_OM_SERVICE_POLICY","symbol":"130660","company_name":"한전산업","entry_date":"2024-04-22","entry_price":7060.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":176.2,"MAE_90D_pct":-1.98,"MFE_180D_pct":176.2,"MAE_180D_pct":-1.98,"trigger_outcome_label":"positive_very_high_MFE_low_MAE_Green_strict","current_profile_verdict":"current_profile_correct_if_project_policy_service_margin_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R1_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R2","reviewed_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","reviewed_canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","reviewed_trigger_id":"R2L90_C06_033170_20240222_STAGE2_FALSE_POSITIVE_OSAT_PACKAGING_THEME","symbol":"033170","company_name":"시그네틱스","entry_date":"2024-02-22","entry_price":2035.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":14.74,"MAE_90D_pct":-29.24,"MFE_180D_pct":14.74,"MAE_180D_pct":-67.71,"trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_MAE_no_capacity_bridge","current_profile_verdict":"current_profile_false_positive_if_OSAT_packaging_theme_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R2_loop_90_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R2","reviewed_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","reviewed_canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","reviewed_trigger_id":"R2L90_C06_036540_20240118_STAGE2_MEMORY_BACKEND_CAPACITY","symbol":"036540","company_name":"SFA반도체","entry_date":"2024-01-18","entry_price":5920.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":37.67,"MAE_90D_pct":-7.09,"MFE_180D_pct":37.67,"MAE_180D_pct":-52.36,"trigger_outcome_label":"positive_high_MFE_low_early_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_customer_capacity_ramp_margin_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R2_loop_90_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R2","reviewed_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","reviewed_canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","reviewed_trigger_id":"R2L90_C06_394280_20240222_STAGE2_FALSE_POSITIVE_AI_IP_BLOWOFF","symbol":"394280","company_name":"오픈엣지테크놀로지","entry_date":"2024-02-22","entry_price":35000.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":10.86,"MAE_90D_pct":-42.71,"MFE_180D_pct":10.86,"MAE_180D_pct":-72.71,"trigger_outcome_label":"counterexample_local_MFE_deep_MAE_no_customer_capacity_bridge","current_profile_verdict":"current_profile_false_positive_if_AI_IP_blowoff_counted_as_HBM_capacity","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R2_loop_90_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R3","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","reviewed_trigger_id":"R3L90_C12_114190_20240126_STAGE2_BATTERY_EQUIPMENT_CALLOFF","symbol":"114190","company_name":"강원에너지","entry_date":"2024-01-26","entry_price":13290.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":64.41,"MAE_90D_pct":-6.7,"MFE_180D_pct":64.41,"MAE_180D_pct":-32.2,"trigger_outcome_label":"positive_high_MFE_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_customer_calloff_shipment_margin_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R3_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R3","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","reviewed_trigger_id":"R3L90_C12_417200_20240102_STAGE2_FALSE_POSITIVE_SUPERCAP_IPO_THEME","symbol":"417200","company_name":"LS머트리얼즈","entry_date":"2024-01-02","entry_price":45800.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":9.83,"MAE_90D_pct":-38.65,"MFE_180D_pct":9.83,"MAE_180D_pct":-79.04,"trigger_outcome_label":"counterexample_low_MFE_extreme_MAE_IPO_decay","current_profile_verdict":"current_profile_false_positive_if_supercapacitor_EV_theme_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R3_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R3","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","reviewed_trigger_id":"R3L90_C12_450080_20240213_STAGE2_FALSE_POSITIVE_PRECURSOR_REBOUND","symbol":"450080","company_name":"에코프로머티","entry_date":"2024-02-13","entry_price":209500.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":0.95,"MAE_90D_pct":-46.49,"MFE_180D_pct":0.95,"MAE_180D_pct":-69.02,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_recent_listing_watch","current_profile_verdict":"current_profile_false_positive_if_precursor_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R3_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R4","reviewed_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","reviewed_canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reviewed_trigger_id":"R4L90_C16_009520_20240611_STAGE2_FALSE_POSITIVE_LITHIUM_THEME","symbol":"009520","company_name":"포스코엠텍","entry_date":"2024-06-11","entry_price":22550.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":9.53,"MAE_90D_pct":-22.84,"MFE_180D_pct":9.53,"MAE_180D_pct":-48.12,"trigger_outcome_label":"counterexample_low_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_lithium_materials_theme_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R4_loop_90_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R4","reviewed_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","reviewed_canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reviewed_trigger_id":"R4L90_C16_018470_20240220_STAGE2_FALSE_POSITIVE_ALUMINUM_SHEET","symbol":"018470","company_name":"조일알미늄","entry_date":"2024-02-20","entry_price":2095.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":5.97,"MAE_90D_pct":-6.78,"MFE_180D_pct":5.97,"MAE_180D_pct":-39.67,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_aluminum_sheet_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R4_loop_90_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R4","reviewed_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","reviewed_canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reviewed_trigger_id":"R4L90_C16_128660_20240412_STAGE2_ALUMINUM_SUPPLY","symbol":"128660","company_name":"피제이메탈","entry_date":"2024-04-12","entry_price":3315.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":62.59,"MAE_90D_pct":-1.81,"MFE_180D_pct":62.59,"MAE_180D_pct":-22.32,"trigger_outcome_label":"positive_high_MFE_low_early_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_supply_policy_spread_margin_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R4_loop_90_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R5","reviewed_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","reviewed_canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","reviewed_trigger_id":"R5L90_C19_020000_20240207_STAGE2_FALSE_POSITIVE_PREMIUM_APPAREL","symbol":"020000","company_name":"한섬","entry_date":"2024-02-07","entry_price":21550.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":0.46,"MAE_90D_pct":-12.39,"MFE_180D_pct":0.46,"MAE_180D_pct":-27.15,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_share_count_watch","current_profile_verdict":"current_profile_false_positive_if_premium_apparel_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R5_loop_90_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R5","reviewed_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","reviewed_canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","reviewed_trigger_id":"R5L90_C19_090430_20240412_STAGE2_BEAUTY_CHANNEL_MARGIN","symbol":"090430","company_name":"아모레퍼시픽","entry_date":"2024-04-12","entry_price":135000.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":48.52,"MAE_90D_pct":-6.81,"MFE_180D_pct":48.52,"MAE_180D_pct":-26.3,"trigger_outcome_label":"positive_high_MFE90_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_channel_inventory_sellthrough_margin_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R5_loop_90_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R5","reviewed_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","reviewed_canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","reviewed_trigger_id":"R5L90_C19_383220_20240401_STAGE2_FALSE_POSITIVE_APPAREL_INVENTORY","symbol":"383220","company_name":"F&F","entry_date":"2024-04-01","entry_price":76500.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":1.18,"MAE_90D_pct":-24.58,"MFE_180D_pct":1.18,"MAE_180D_pct":-38.24,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_inventory_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_apparel_brand_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R5_loop_90_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R6","reviewed_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","reviewed_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reviewed_trigger_id":"R6L90_C22_000400_20240213_STAGE2_FALSE_POSITIVE_NONLIFE_MNA_THEME","symbol":"000400","company_name":"롯데손해보험","entry_date":"2024-02-13","entry_price":3370.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":8.9,"MAE_90D_pct":-23.59,"MFE_180D_pct":8.9,"MAE_180D_pct":-46.17,"trigger_outcome_label":"counterexample_price_only_local_MFE_deep_MAE_no_reserve_cycle_bridge","current_profile_verdict":"current_profile_false_positive_if_MNA_theme_counted_as_C22_rate_cycle","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R6_loop_90_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R6","reviewed_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","reviewed_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reviewed_trigger_id":"R6L90_C22_032830_20240124_STAGE2_LIFE_RATE_RESERVE_CAPITAL","symbol":"032830","company_name":"삼성생명","entry_date":"2024-01-24","entry_price":62600.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":73.32,"MAE_90D_pct":-1.44,"MFE_180D_pct":73.32,"MAE_180D_pct":-1.44,"trigger_outcome_label":"positive_very_high_MFE_low_MAE_capital_return_bridge","current_profile_verdict":"current_profile_correct_if_reserve_capital_buffer_payout_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R6_loop_90_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R6","reviewed_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","reviewed_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reviewed_trigger_id":"R6L90_C22_088350_20240213_STAGE2_FALSE_POSITIVE_LIFE_PRICE_SPIKE","symbol":"088350","company_name":"한화생명","entry_date":"2024-02-13","entry_price":3550.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":7.46,"MAE_90D_pct":-21.27,"MFE_180D_pct":7.46,"MAE_180D_pct":-30.7,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_reserve_payout_bridge","current_profile_verdict":"current_profile_false_positive_if_life_insurance_spike_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R6_loop_90_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R7","reviewed_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","reviewed_canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","reviewed_trigger_id":"R7L90_C24_237690_20240223_STAGE2_RNA_PLATFORM_BRIDGE","symbol":"237690","company_name":"에스티팜","entry_date":"2024-02-23","entry_price":66300.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":49.32,"MAE_90D_pct":-3.92,"MFE_180D_pct":71.19,"MAE_180D_pct":-3.92,"trigger_outcome_label":"positive_high_MFE_low_MAE_platform_bridge","current_profile_verdict":"current_profile_correct_if_endpoint_partner_manufacturing_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R7_loop_90_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R7","reviewed_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","reviewed_canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","reviewed_trigger_id":"R7L90_C24_256840_20240320_STAGE2_FALSE_POSITIVE_THERAPEUTIC_EVENT","symbol":"256840","company_name":"한국비엔씨","entry_date":"2024-03-20","entry_price":7960.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":18.22,"MAE_90D_pct":-26.38,"MFE_180D_pct":18.22,"MAE_180D_pct":-55.09,"trigger_outcome_label":"counterexample_local_MFE_deep_MAE_no_commercial_bridge","current_profile_verdict":"current_profile_false_positive_if_therapeutic_event_momentum_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R7_loop_90_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R7","reviewed_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","reviewed_canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","reviewed_trigger_id":"R7L90_C24_365270_20240320_STAGE2_FALSE_POSITIVE_VASCULAR_EVENT","symbol":"365270","company_name":"큐라클","entry_date":"2024-03-20","entry_price":18630.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":14.6,"MAE_90D_pct":-55.88,"MFE_180D_pct":14.6,"MAE_180D_pct":-72.46,"trigger_outcome_label":"counterexample_sub_Yellow_MFE_extreme_MAE_no_regulatory_bridge","current_profile_verdict":"current_profile_false_positive_if_trial_event_spike_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R7_loop_90_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R8","reviewed_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","reviewed_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","reviewed_trigger_id":"R8L90_C27_035760_20240122_STAGE2_MEDIA_COMMERCE_IP","symbol":"035760","company_name":"CJ ENM","entry_date":"2024-01-22","entry_price":66500.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":34.29,"MAE_90D_pct":-6.02,"MFE_180D_pct":34.29,"MAE_180D_pct":-19.7,"trigger_outcome_label":"positive_MFE90_ge30_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_distribution_IP_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R8_loop_90_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R8","reviewed_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","reviewed_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","reviewed_trigger_id":"R8L90_C27_206560_20240109_STAGE2_FALSE_POSITIVE_VFX_THEME","symbol":"206560","company_name":"덱스터","entry_date":"2024-01-09","entry_price":10280.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":3.31,"MAE_90D_pct":-27.24,"MFE_180D_pct":3.31,"MAE_180D_pct":-42.61,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_VFX_content_theme_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R8_loop_90_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R8","reviewed_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","reviewed_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","reviewed_trigger_id":"R8L90_C27_241840_20240102_STAGE2_FALSE_POSITIVE_DRAMA_IP","symbol":"241840","company_name":"에이스토리","entry_date":"2024-01-02","entry_price":13800.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":4.06,"MAE_90D_pct":-29.57,"MFE_180D_pct":4.06,"MAE_180D_pct":-52.1,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_distribution_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_drama_IP_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R8_loop_90_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R9","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_id":"R9L90_C29_013870_20240102_STAGE2_FALSE_POSITIVE_THERMAL_PUMP","symbol":"013870","company_name":"지엠비코리아","entry_date":"2024-01-02","entry_price":4830.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":5.59,"MAE_90D_pct":-14.6,"MFE_180D_pct":5.59,"MAE_180D_pct":-18.84,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_operating_leverage_bridge","current_profile_verdict":"current_profile_false_positive_if_pump_autoparts_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R9_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R9","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_id":"R9L90_C29_092780_20240422_STAGE2_POWERTRAIN_PISTON_VOLUME","symbol":"092780","company_name":"동양피스톤","entry_date":"2024-04-22","entry_price":4585.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":55.29,"MAE_90D_pct":-4.69,"MFE_180D_pct":55.29,"MAE_180D_pct":-7.31,"trigger_outcome_label":"positive_high_MFE_low_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_OEM_volume_mix_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R9_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R9","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_id":"R9L90_C29_126640_20240102_STAGE2_FALSE_POSITIVE_SMALL_CHASSIS","symbol":"126640","company_name":"화신정공","entry_date":"2024-01-02","entry_price":1711.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":1.4,"MAE_90D_pct":-15.43,"MFE_180D_pct":1.4,"MAE_180D_pct":-22.56,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_volume_bridge","current_profile_verdict":"current_profile_false_positive_if_small_chassis_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R9_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R10","reviewed_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","reviewed_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_id":"R10L90_C30_014280_20240213_STAGE2_FALSE_POSITIVE_FORMWORK_REBOUND","symbol":"014280","company_name":"금강공업","entry_date":"2024-02-13","entry_price":6390.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":2.35,"MAE_90D_pct":-17.21,"MFE_180D_pct":2.35,"MAE_180D_pct":-37.79,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_backlog_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_formwork_material_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R10_loop_90_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R10","reviewed_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","reviewed_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_id":"R10L90_C30_023410_20240223_STAGE2_FALSE_POSITIVE_READY_MIX_POLICY","symbol":"023410","company_name":"유진기업","entry_date":"2024-02-23","entry_price":3980.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":15.08,"MAE_90D_pct":-13.57,"MFE_180D_pct":15.08,"MAE_180D_pct":-20.1,"trigger_outcome_label":"counterexample_local_MFE_but_MAE_expansion_no_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_ready_mix_policy_MFE_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R10_loop_90_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R10","reviewed_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","reviewed_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_id":"R10L90_C30_300720_20240129_STAGE2_CEMENT_MARGIN_CASH","symbol":"300720","company_name":"한일시멘트","entry_date":"2024-01-29","entry_price":11550.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":46.15,"MAE_90D_pct":-1.21,"MFE_180D_pct":46.15,"MAE_180D_pct":-1.21,"trigger_outcome_label":"positive_high_MFE90_low_MAE_materials_margin_bridge","current_profile_verdict":"current_profile_correct_if_materials_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R10_loop_90_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R11","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","reviewed_trigger_id":"R11L90_C03_095190_20240215_STAGE2_FALSE_POSITIVE_DUALUSE_MACHINING","symbol":"095190","company_name":"이엠코리아","entry_date":"2024-02-15","entry_price":2560.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":53.13,"MAE_90D_pct":-7.42,"MFE_180D_pct":53.13,"MAE_180D_pct":-39.41,"trigger_outcome_label":"counterexample_price_only_high_MFE_deep_MAE_no_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_dualuse_machining_MFE_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R11_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R11","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","reviewed_trigger_id":"R11L90_C03_218410_20240122_STAGE2_FALSE_POSITIVE_RF_DEFENSE_THEME","symbol":"218410","company_name":"RFHIC","entry_date":"2024-01-22","entry_price":19460.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":1.44,"MAE_90D_pct":-23.95,"MFE_180D_pct":1.44,"MAE_180D_pct":-45.27,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_export_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_RF_defense_theme_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R11_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R11","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","reviewed_trigger_id":"R11L90_C03_272210_20240422_STAGE2_DEFENSE_ELECTRONICS_EXPORT_BACKLOG","symbol":"272210","company_name":"한화시스템","entry_date":"2024-04-22","entry_price":16940.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":32.53,"MAE_90D_pct":-1.36,"MFE_180D_pct":78.28,"MAE_180D_pct":-1.36,"trigger_outcome_label":"positive_high_MFE90_very_high_MFE180_low_MAE_backlog_bridge","current_profile_verdict":"current_profile_correct_if_export_framework_backlog_delivery_margin_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R11_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R12","reviewed_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","reviewed_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reviewed_trigger_id":"R12L90_C32_003030_20240102_STAGE2_FALSE_POSITIVE_STEEL_HOLDCO_NAV","symbol":"003030","company_name":"세아제강지주","entry_date":"2024-01-02","entry_price":236000.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":2.12,"MAE_90D_pct":-17.37,"MFE_180D_pct":2.12,"MAE_180D_pct":-33.69,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_return_bridge","current_profile_verdict":"current_profile_false_positive_if_NAV_discount_vocabulary_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R12_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R12","reviewed_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","reviewed_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reviewed_trigger_id":"R12L90_C32_006840_20240102_STAGE2_FALSE_POSITIVE_HOLDCO_DISCOUNT","symbol":"006840","company_name":"AK홀딩스","entry_date":"2024-01-02","entry_price":17090.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":5.5,"MAE_90D_pct":-16.33,"MFE_180D_pct":5.5,"MAE_180D_pct":-43.65,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_control_premium_bridge","current_profile_verdict":"current_profile_false_positive_if_holdco_discount_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_price_only","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R12_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"90","reviewed_round":"R12","reviewed_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","reviewed_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reviewed_trigger_id":"R12L90_C32_008930_20240112_STAGE2_CONTROL_PREMIUM_EVENT","symbol":"008930","company_name":"한미사이언스","entry_date":"2024-01-12","entry_price":38400.0,"positive_or_counterexample":"positive_control","MFE_90D_pct":46.35,"MAE_90D_pct":-18.62,"MFE_180D_pct":46.35,"MAE_180D_pct":-26.56,"trigger_outcome_label":"positive_high_MFE_low_entry_MAE_but_event_volatility_watch","current_profile_verdict":"current_profile_correct_if_control_premium_ownership_event_bridge_required","r13_guard_verdict":"bridge_present_positive_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R12_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md"}
```

## 7. Guardrail stress-test results

```jsonl
{"row_type":"r13_guardrail_summary","round":"R13","loop":"90","guardrail_id":"bridge_missing_price_only_4B_guard","reviewed_trigger_count":36,"positive_control_count":12,"counterexample_count":24,"counter_MFE90_lt_20_count":22,"counter_MFE90_ge_20_price_only_count":2,"counter_MAE90_le_minus20_count":13,"counter_MAE180_le_minus25_count":21,"counter_MAE180_le_minus35_count":18,"price_only_like_count":12,"late_rebound_or_spike_not_validation_count":1,"data_quality_watch_count":4,"verdict":"existing calibrated axes are directionally correct; do not loosen Green; future batch can add canonical bridge-required guards as shadow-only candidates."}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"90","rule_candidate":"cross_archetype_bridge_missing_hard_4B_watch","condition":"bridge_missing_or_unverified AND (MFE90 < 20 OR MAE180 <= -25 OR evidence_type includes price_only)","action":"block Stage2-Actionable/Yellow/Green; route to Watch/4B/evidence repair","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"90","rule_candidate":"late_rebound_not_entry_validation","condition":"original_entry_bridge_missing AND later_full_window_or_Q4_spike_occurs","action":"do not retroactively validate original entry; require fresh trigger date and fresh non-price bridge evidence","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"90","rule_candidate":"data_quality_repair_before_patch","condition":"corporate_action_candidate_or_recent_listing_or_share_count_drift_or_market_segment_change_watch_present","action":"allow research annotation but block production patch until price path and exact evidence are repaired","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"90","rule_candidate":"Green_requires_exact_non_price_bridge","condition":"positive_control_has_high_MFE_but_source_proxy_only_or_late_drawdown_or_event_reversal_watch","action":"allow Yellow/Green-candidate-watch only; exact source-grade bridge required before Green","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
```

## 8. Sector-by-sector redteam notes

```text
R1 / C04 nuclear:
  130660 confirms project/legal/O&M service bridge. 105840 and 019990 show nuclear instrumentation/actuator themes need project approval, legal milestone, margin and cash evidence.

R2 / C06 HBM/memory:
  036540 confirms backend/customer-capacity bridge. 033170 and 394280 show OSAT/AI-IP theme MFE is not HBM customer-capacity evidence.

R3 / C12 battery call-off:
  114190 confirms customer call-off/shipment bridge. 450080 and 417200 show battery mega-theme or recent-listing price memory is not call-off evidence.

R4 / C16 resource supply:
  128660 confirms aluminum/nonferrous supply-spread bridge. 009520 and 018470 show lithium/aluminum theme rebound fails without supply, spread, margin and cash bridge.

R5 / C19 brand/retail:
  090430 confirms beauty channel-inventory/margin bridge. 383220 and 020000 show apparel rebound fails without inventory turn, sell-through and margin bridge.

R6 / C22 insurance:
  032830 confirms reserve/capital/payout bridge. 088350 and 000400 show insurance price or M&A theme fails without reserve quality, capital buffer and payout bridge.

R7 / C24 bio trial-event:
  237690 confirms RNA platform / CMC / data bridge. 365270 and 256840 show trial-event momentum fails without partner, regulatory, commercial and cash-runway bridge.

R8 / C27 content/IP:
  035760 confirms media-commerce/IP monetization bridge. 241840 and 206560 show drama/VFX theme fails without distribution, licensing, margin and cash evidence.

R9 / C29 mobility:
  092780 confirms OEM volume/program-mix bridge. 126640 and 013870 show small auto-parts rebound fails without fresh customer volume, utilization and margin bridge.

R10 / C30 construction/PF:
  300720 confirms cement ASP/margin/cash bridge. 023410 and 014280 show ready-mix/formwork price action fails without PF, backlog, margin and cash evidence.

R11 / C03 defense:
  272210 confirms defense electronics/export-framework bridge. 095190 and 218410 show dual-use/RF defense themes fail without signed export backlog, delivery and margin bridge.

R12 / C32 governance:
  008930 confirms control-premium/ownership-event bridge. 006840 and 003030 show holdco/NAV vocabulary fails without tender, buyback/cancellation, asset-sale, legal/voting or cash-return bridge.
```

## 9. Shadow-only recommendations

```jsonl
{"row_type":"shadow_weight","round":"R13","loop":"90","axis":"cross_archetype_bridge_required_before_Yellow","scope":"cross_archetype","candidate_delta":0.0,"direction":"diagnostic_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Across loop90, positive controls averaged MFE90 60.55% while weak-bridge counterexamples averaged MFE90 9.25% and MAE180 -45.09%."}
{"row_type":"shadow_weight","round":"R13","loop":"90","axis":"cross_archetype_price_only_MFE_not_positive_evidence","scope":"cross_archetype","candidate_delta":0.0,"direction":"diagnostic_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Counterexamples with MFE90 >= 20 still appeared where high MFE was price-only and bridge-missing."}
{"row_type":"shadow_weight","round":"R13","loop":"90","axis":"cross_archetype_late_rebound_not_original_entry_validation","scope":"cross_archetype","candidate_delta":0.0,"direction":"diagnostic_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Late-spike or late-rebound flags appeared in several counterexamples, but the original weak entry was not validated without fresh evidence."}
{"row_type":"shadow_weight","round":"R13","loop":"90","axis":"cross_archetype_data_quality_repair_before_patch","scope":"cross_archetype","candidate_delta":0.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Recent-listing, share-count drift, market-segment-change and older corporate-action watch flags should be repaired before production patch consideration."}
{"row_type":"shadow_weight","round":"R13","loop":"90","axis":"cross_archetype_Green_requires_exact_non_price_bridge","scope":"cross_archetype","candidate_delta":0.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"All 12 positive controls remain source-proxy-only and require exact evidence before Green."}
```

## 10. Residual Contribution Summary

```text
new_independent_case_count: 0
reused_case_count: 36
reviewed_trigger_count: 36
reviewed_source_file_count: 12
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
3. Confirm reviewed rows came from R1~R12 loop90 MDs.
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
9. Confirm accidentally touched R11/C03, R10/C30, R9/C29 and R8/C27 candidate rows are not double-counted here beyond their already-reviewed scheduled MDs.
10. Do not loosen Stage3-Green.
11. Do not use future MFE/MAE in runtime scoring.
```

## 12. Round state

```text
completed_round = R13
completed_loop = 90
next_round = R1
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 13. Final one-line contribution

```text
This R13 loop reviews 36 loop90 triggers across R1~R12, adds 0 new independent cases, and confirms that bridge-missing / price-only / late-rebound / data-quality / Green-exact-evidence guards should remain hard Watch/4B barriers before any Yellow/Green promotion.
```
