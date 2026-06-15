# E2R Stock-Web v12 Residual Research — R13 Loop 91 / Cross-Archetype 4B·4C Redteam

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R13
loop: 91
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: LOOP91_BRIDGE_PRESENT_POSITIVE_VS_WEAK_BRIDGE_THEME_PRICE_ONLY_DATA_QUALITY_GUARD
sector: cross-sector / 4B / 4C / bridge-missing / price-only / data-quality / Green strictness
output_file: e2r_stock_web_v12_residual_round_R13_loop_91_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
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

This run follows the v12 sequential scheduler after completed `R12 loop 91`.

```text
scheduled_round = R13
scheduled_loop = 91
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

R13 is not a fresh symbol-mining round.
It is a cross-archetype redteam checkpoint that reviews the 36 trigger rows produced by R1~R12 loop91.

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
{"row_type":"price_source_validation","round":"R13","loop":"91","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","validation_scope":"R13 reviews R1~R12 loop91 trigger rows; it does not create new price triggers."}
```

Reviewed files:

```text
- e2r_stock_web_v12_residual_round_R1_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
- e2r_stock_web_v12_residual_round_R2_loop_91_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
- e2r_stock_web_v12_residual_round_R3_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
- e2r_stock_web_v12_residual_round_R4_loop_91_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
- e2r_stock_web_v12_residual_round_R5_loop_91_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
- e2r_stock_web_v12_residual_round_R6_loop_91_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
- e2r_stock_web_v12_residual_round_R7_loop_91_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
- e2r_stock_web_v12_residual_round_R8_loop_91_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
- e2r_stock_web_v12_residual_round_R9_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
- e2r_stock_web_v12_residual_round_R10_loop_91_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
- e2r_stock_web_v12_residual_round_R11_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
- e2r_stock_web_v12_residual_round_R12_loop_91_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

## 3. Aggregate redteam statistics

```jsonl
{"row_type":"aggregate_metric","round":"R13","loop":"91","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":36,"reviewed_source_file_count":12,"reviewed_original_round_count":12,"reviewed_original_canonical_count":12,"positive_control_count":12,"counterexample_count":24,"positive_avg_MFE90_pct":90.29,"positive_avg_MAE90_pct":-4.28,"positive_avg_MFE180_pct":105.35,"positive_avg_MAE180_pct":-8.98,"counter_avg_MFE90_pct":9.04,"counter_avg_MAE90_pct":-24.99,"counter_avg_MFE180_pct":9.76,"counter_avg_MAE180_pct":-42.43,"counter_MFE90_lt_20_count":20,"counter_MFE90_ge_20_count":4,"counter_MAE90_le_minus20_count":12,"counter_MAE90_le_minus30_count":6,"counter_MAE180_le_minus25_count":21,"counter_MAE180_le_minus35_count":15,"counter_MAE180_le_minus50_count":7,"price_only_like_count":3,"late_rebound_or_spike_not_validation_count":2,"data_quality_watch_count":6,"source_proxy_only_count":36,"evidence_url_pending_count":36,"four_c_watch_count":1}
```

Interpretation:

```text
Bridge-present positive/positive-watch controls: avg MFE90 90.29% / avg MAE90 -4.28%.
Bridge-present positive/positive-watch controls avg MFE180 105.35% / avg MAE180 -8.98%.

Weak-bridge counterexamples: avg MFE90 9.04% / avg MAE90 -24.99%.
Weak-bridge counterexamples avg MFE180 9.76% / avg MAE180 -42.43%.

Counterexamples with MFE90 < 20: 20 / 24.
Counterexamples with MFE90 >= 20 but still not positive evidence: 4 / 24.
Counterexamples with MAE90 <= -20: 12 / 24.
Counterexamples with MAE90 <= -30: 6 / 24.
Counterexamples with MAE180 <= -25: 21 / 24.
Counterexamples with MAE180 <= -35: 15 / 24.
Counterexamples with MAE180 <= -50: 7 / 24.
Price-only-like evidence flags: 3.
Late rebound/spike not-validation flags: 2.
Data-quality / listing / segment-change / inactive-like watch flags: 6.
4C-watch flags: 1.
```

## 4. R13 research question

Across loop91, can the calibrated profile keep Stage2/Yellow/Green closed when a case has loud price action but no business bridge?

The answer is directionally yes. The repeated error shape is stable across sectors:

```text
theme label without bridge
local MFE without non-price evidence
late rebound/spike pretending to validate the original weak entry
recent-listing / market-segment-change / inactive-like data quality before patching
regulatory failure or CRL-risk rows requiring 4C-watch
Green-candidate rows that still require exact source-grade non-price evidence
```

The same mechanism appears whether the surface story is EPC, HBM equipment, battery JV/AMPC, copper spread, K-beauty exports, financial value-up, bio commercialization, platform ARPU, mobility volume, construction PF, nuclear O&M, or policy subsidy.
Price is the engine noise. The bridge is the driveshaft. Without the driveshaft, RPM rises and the wheel does not move.

## 5. Cross-round case summary

```jsonl
{"row_type":"r13_cross_case","round":"R13","loop":"91","reviewed_round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reviewed_trigger_count":3,"positive_control_symbols":["100840"],"counterexample_symbols":["028050","037350"],"avg_positive_MFE90_pct":60.2,"avg_counter_MFE90_pct":2.08,"avg_counter_MAE180_pct":-33.6,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"91","reviewed_round":"R2","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","reviewed_trigger_count":3,"positive_control_symbols":["084370"],"counterexample_symbols":["086390","217190"],"avg_positive_MFE90_pct":60.0,"avg_counter_MFE90_pct":21.62,"avg_counter_MAE180_pct":-57.02,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"91","reviewed_round":"R3","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","reviewed_trigger_count":3,"positive_control_symbols":["036830"],"counterexample_symbols":["014820","095500"],"avg_positive_MFE90_pct":122.0,"avg_counter_MFE90_pct":7.97,"avg_counter_MAE180_pct":-47.75,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"91","reviewed_round":"R4","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","reviewed_trigger_count":3,"positive_control_symbols":["006340"],"counterexample_symbols":["005810","008350"],"avg_positive_MFE90_pct":301.33,"avg_counter_MFE90_pct":4.38,"avg_counter_MAE180_pct":-34.27,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"91","reviewed_round":"R5","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reviewed_trigger_count":3,"positive_control_symbols":["003350"],"counterexample_symbols":["004370","051900"],"avg_positive_MFE90_pct":185.49,"avg_counter_MFE90_pct":10.88,"avg_counter_MAE180_pct":-34.88,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"91","reviewed_round":"R6","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reviewed_trigger_count":3,"positive_control_symbols":["005940"],"counterexample_symbols":["001290","030610"],"avg_positive_MFE90_pct":25.6,"avg_counter_MFE90_pct":3.83,"avg_counter_MAE180_pct":-32.61,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"91","reviewed_round":"R7","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reviewed_trigger_count":3,"positive_control_symbols":["326030"],"counterexample_symbols":["067630","229000"],"avg_positive_MFE90_pct":64.56,"avg_counter_MFE90_pct":2.16,"avg_counter_MAE180_pct":-68.74,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"91","reviewed_round":"R8","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","reviewed_trigger_count":3,"positive_control_symbols":["181710"],"counterexample_symbols":["104200","236810"],"avg_positive_MFE90_pct":30.29,"avg_counter_MFE90_pct":19.59,"avg_counter_MAE180_pct":-57.27,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"91","reviewed_round":"R9","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_count":3,"positive_control_symbols":["123410"],"counterexample_symbols":["012280","033250"],"avg_positive_MFE90_pct":112.45,"avg_counter_MFE90_pct":3.43,"avg_counter_MAE180_pct":-34.34,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"91","reviewed_round":"R10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_count":3,"positive_control_symbols":["006390"],"counterexample_symbols":["002290","025750"],"avg_positive_MFE90_pct":14.82,"avg_counter_MFE90_pct":2.04,"avg_counter_MAE180_pct":-34.23,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"91","reviewed_round":"R11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","reviewed_trigger_count":3,"positive_control_symbols":["126720"],"counterexample_symbols":["036190","457550"],"avg_positive_MFE90_pct":65.97,"avg_counter_MFE90_pct":16.78,"avg_counter_MAE180_pct":-30.7,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_cross_case","round":"R13","loop":"91","reviewed_round":"R12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reviewed_trigger_count":3,"positive_control_symbols":["086790"],"counterexample_symbols":["034230","068290"],"avg_positive_MFE90_pct":40.73,"avg_counter_MFE90_pct":13.7,"avg_counter_MAE180_pct":-43.7,"cross_redteam_verdict":"bridge_required_guard_passed; counterexamples remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
```

## 6. R13 review trigger rows

```jsonl
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R1","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reviewed_trigger_id":"R1L91_C05_028050_20240422_STAGE2_FALSE_POSITIVE_EPC_REBRAND","symbol":"028050","company_name":"삼성E&A","entry_date":"2024-04-22","entry_price":26300.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":2.66,"MAE_90D_pct":-17.87,"MFE_180D_pct":2.66,"MAE_180D_pct":-38.02,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_large_EPC_vocabulary_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R1_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R1","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reviewed_trigger_id":"R1L91_C05_037350_20241010_STAGE2_FALSE_POSITIVE_CLEANROOM_ENGINEERING_SPIKE","symbol":"037350","company_name":"성도이엔지","entry_date":"2024-10-10","entry_price":5380.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":1.49,"MAE_90D_pct":-25.0,"MFE_180D_pct":1.49,"MAE_180D_pct":-29.18,"trigger_outcome_label":"counterexample_near_zero_MFE_MAE_expansion_no_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_cleanroom_engineering_spike_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R1_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R1","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reviewed_trigger_id":"R1L91_C05_100840_20240603_STAGE2_ENERGY_EQUIPMENT_BACKLOG_MARGIN","symbol":"100840","company_name":"SNT에너지","entry_date":"2024-06-03","entry_price":10050.0,"positive_or_counterexample":"positive_control_or_positive_watch","MFE_90D_pct":60.2,"MAE_90D_pct":-4.28,"MFE_180D_pct":153.73,"MAE_180D_pct":-4.28,"trigger_outcome_label":"positive_very_high_MFE90_and_MFE180_low_MAE_post_candidate_watch","current_profile_verdict":"current_profile_correct_if_order_backlog_delivery_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R1_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R2","reviewed_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","reviewed_canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","reviewed_trigger_id":"R2L91_C07_084370_20240222_STAGE2_HBM_DEPOSITION_EQUIPMENT_ORDER_RAMP","symbol":"084370","company_name":"유진테크","entry_date":"2024-02-22","entry_price":37500.0,"positive_or_counterexample":"positive_control_or_positive_watch","MFE_90D_pct":60.0,"MAE_90D_pct":-3.73,"MFE_180D_pct":60.0,"MAE_180D_pct":-19.2,"trigger_outcome_label":"positive_high_MFE90_controlled_MAE_market_segment_watch","current_profile_verdict":"current_profile_correct_if_HBM_customer_order_delivery_margin_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R2_loop_91_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R2","reviewed_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","reviewed_canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","reviewed_trigger_id":"R2L91_C07_086390_20240308_STAGE2_FALSE_POSITIVE_MEMORY_TESTER_THEME","symbol":"086390","company_name":"유니테스트","entry_date":"2024-03-08","entry_price":15420.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":26.46,"MAE_90D_pct":-13.36,"MFE_180D_pct":26.46,"MAE_180D_pct":-51.56,"trigger_outcome_label":"counterexample_price_only_MFE_deep_MAE_no_order_bridge","current_profile_verdict":"current_profile_false_positive_if_memory_tester_MFE_overcredited","r13_guard_verdict":"hard_4B_watch_price_MFE_without_bridge","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R2_loop_91_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R2","reviewed_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","reviewed_canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","reviewed_trigger_id":"R2L91_C07_217190_20240124_STAGE2_FALSE_POSITIVE_BACKEND_HBM_POSTPROCESS","symbol":"217190","company_name":"제너셈","entry_date":"2024-01-24","entry_price":15800.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":16.77,"MAE_90D_pct":-23.92,"MFE_180D_pct":16.77,"MAE_180D_pct":-62.47,"trigger_outcome_label":"counterexample_low_MFE_extreme_MAE_no_backlog_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_backend_equipment_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R2_loop_91_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R3","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","reviewed_trigger_id":"R3L91_C13_014820_20240321_STAGE2_FALSE_POSITIVE_PACKAGING_CAN_MATERIALS","symbol":"014820","company_name":"동원시스템즈","entry_date":"2024-03-21","entry_price":50700.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":2.96,"MAE_90D_pct":-26.82,"MFE_180D_pct":6.9,"MAE_180D_pct":-26.82,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_utilization_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_packaging_can_materials_vocabulary_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R3_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R3","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","reviewed_trigger_id":"R3L91_C13_036830_20240129_STAGE2_ELECTROLYTE_JV_UTILIZATION_AMPC","symbol":"036830","company_name":"솔브레인홀딩스","entry_date":"2024-01-29","entry_price":39550.0,"positive_or_counterexample":"positive_control_or_positive_watch","MFE_90D_pct":122.0,"MAE_90D_pct":-3.16,"MFE_180D_pct":122.0,"MAE_180D_pct":-14.03,"trigger_outcome_label":"positive_very_high_MFE90_low_MAE90_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_JV_utilization_AMPC_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R3_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R3","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","reviewed_trigger_id":"R3L91_C13_095500_20240229_STAGE2_FALSE_POSITIVE_LITHIUM_IRA_VOCABULARY","symbol":"095500","company_name":"미래나노텍","entry_date":"2024-02-29","entry_price":22350.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":12.98,"MAE_90D_pct":-29.71,"MFE_180D_pct":12.98,"MAE_180D_pct":-68.68,"trigger_outcome_label":"counterexample_sub_Yellow_MFE_extreme_MAE_no_AMPC_bridge","current_profile_verdict":"current_profile_false_positive_if_lithium_IRA_vocabulary_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R3_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R4","reviewed_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","reviewed_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","reviewed_trigger_id":"R4L91_C15_005810_20240411_STAGE2_FALSE_POSITIVE_COPPER_HOLDCO","symbol":"005810","company_name":"풍산홀딩스","entry_date":"2024-04-11","entry_price":31600.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":7.59,"MAE_90D_pct":-15.35,"MFE_180D_pct":7.59,"MAE_180D_pct":-24.21,"trigger_outcome_label":"counterexample_low_MFE_moderate_MAE_post_candidate_watch","current_profile_verdict":"current_profile_false_positive_if_copper_holdco_vocabulary_overcredited","r13_guard_verdict":"hard_4B_watch_with_data_quality_repair_required","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R4_loop_91_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R4","reviewed_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","reviewed_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","reviewed_trigger_id":"R4L91_C15_006340_20240314_STAGE2_COPPER_WIRE_SPREAD","symbol":"006340","company_name":"대원전선","entry_date":"2024-03-14","entry_price":1358.0,"positive_or_counterexample":"positive_control_or_positive_watch","MFE_90D_pct":301.33,"MAE_90D_pct":-4.12,"MFE_180D_pct":301.33,"MAE_180D_pct":-4.12,"trigger_outcome_label":"positive_extreme_MFE90_low_MAE_inventory_spread_bridge","current_profile_verdict":"current_profile_correct_if_inventory_spread_ASP_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R4_loop_91_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R4","reviewed_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","reviewed_canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","reviewed_trigger_id":"R4L91_C15_008350_20240213_STAGE2_FALSE_POSITIVE_ALUMINUM_EXTRUSION","symbol":"008350","company_name":"남선알미늄","entry_date":"2024-02-13","entry_price":2155.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":1.16,"MAE_90D_pct":-18.84,"MFE_180D_pct":1.16,"MAE_180D_pct":-44.32,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_spread_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_aluminum_theme_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R4_loop_91_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R5","reviewed_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","reviewed_canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reviewed_trigger_id":"R5L91_C20_003350_20240415_STAGE2_KBEAUTY_EXPORT_MANUFACTURING","symbol":"003350","company_name":"한국화장품제조","entry_date":"2024-04-15","entry_price":25500.0,"positive_or_counterexample":"positive_control_or_positive_watch","MFE_90D_pct":185.49,"MAE_90D_pct":-3.53,"MFE_180D_pct":250.59,"MAE_180D_pct":-3.53,"trigger_outcome_label":"positive_extreme_MFE90_and_MFE180_low_MAE_export_channel_bridge","current_profile_verdict":"current_profile_correct_if_export_channel_reorder_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R5_loop_91_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R5","reviewed_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","reviewed_canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reviewed_trigger_id":"R5L91_C20_004370_20240614_STAGE2_FALSE_POSITIVE_FOOD_GLOBAL_POSTMOVE","symbol":"004370","company_name":"농심","entry_date":"2024-06-14","entry_price":548000.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":7.48,"MAE_90D_pct":-30.57,"MFE_180D_pct":7.48,"MAE_180D_pct":-42.15,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_reorder_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_food_global_distribution_postmove_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R5_loop_91_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R5","reviewed_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","reviewed_canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","reviewed_trigger_id":"R5L91_C20_051900_20240430_STAGE2_FALSE_POSITIVE_LEGACY_BEAUTY_CHANNEL","symbol":"051900","company_name":"LG생활건강","entry_date":"2024-04-30","entry_price":420000.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":14.29,"MAE_90D_pct":-19.05,"MFE_180D_pct":14.29,"MAE_180D_pct":-27.62,"trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_MAE_no_fresh_channel_bridge","current_profile_verdict":"current_profile_false_positive_if_legacy_beauty_channel_vocabulary_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R5_loop_91_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R6","reviewed_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","reviewed_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reviewed_trigger_id":"R6L91_C21_001290_20240215_STAGE2_FALSE_POSITIVE_TURNAROUND_BROKERAGE","symbol":"001290","company_name":"상상인증권","entry_date":"2024-02-15","entry_price":800.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":6.25,"MAE_90D_pct":-20.88,"MFE_180D_pct":6.25,"MAE_180D_pct":-49.88,"trigger_outcome_label":"counterexample_low_MFE_extreme_MAE_no_capital_return_bridge","current_profile_verdict":"current_profile_false_positive_if_turnaround_brokerage_vocabulary_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R6_loop_91_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R6","reviewed_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","reviewed_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reviewed_trigger_id":"R6L91_C21_005940_20240129_STAGE2_BROKERAGE_CAPITAL_RETURN","symbol":"005940","company_name":"NH투자증권","entry_date":"2024-01-29","entry_price":10430.0,"positive_or_counterexample":"positive_control_or_positive_watch","MFE_90D_pct":25.6,"MAE_90D_pct":-2.11,"MFE_180D_pct":39.31,"MAE_180D_pct":-2.11,"trigger_outcome_label":"positive_high_MFE90_low_entry_MAE_late_repricing_watch","current_profile_verdict":"current_profile_correct_if_ROE_payout_buyback_capital_buffer_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R6_loop_91_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R6","reviewed_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","reviewed_canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reviewed_trigger_id":"R6L91_C21_030610_20240219_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_VALUEUP","symbol":"030610","company_name":"교보증권","entry_date":"2024-02-19","entry_price":5640.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":1.42,"MAE_90D_pct":-15.34,"MFE_180D_pct":1.6,"MAE_180D_pct":-15.34,"trigger_outcome_label":"counterexample_near_zero_MFE_moderate_MAE_no_explicit_payout_bridge","current_profile_verdict":"current_profile_false_positive_if_small_brokerage_PBR_vocabulary_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R6_loop_91_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R7","reviewed_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","reviewed_canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reviewed_trigger_id":"R7L91_C23_067630_20240422_STAGE2_FALSE_POSITIVE_APPROVAL_EXPECTATION_CRL","symbol":"067630","company_name":"HLB생명과학","entry_date":"2024-04-22","entry_price":17310.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":3.99,"MAE_90D_pct":-55.52,"MFE_180D_pct":3.99,"MAE_180D_pct":-55.52,"trigger_outcome_label":"counterexample_near_zero_MFE_extreme_MAE_4C_watch","current_profile_verdict":"current_profile_false_positive_if_approval_expectation_overcredited_without_CRL_protection","r13_guard_verdict":"hard_4C_watch_regulatory_or_thesis_failure_risk","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R7_loop_91_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R7","reviewed_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","reviewed_canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reviewed_trigger_id":"R7L91_C23_229000_20240102_STAGE2_FALSE_POSITIVE_DIAGNOSTIC_COMMERCIALIZATION","symbol":"229000","company_name":"젠큐릭스","entry_date":"2024-01-02","entry_price":6270.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":0.32,"MAE_90D_pct":-49.52,"MFE_180D_pct":0.32,"MAE_180D_pct":-81.96,"trigger_outcome_label":"counterexample_near_zero_MFE_extreme_MAE_diagnostic_vocabulary_decay","current_profile_verdict":"current_profile_false_positive_if_diagnostic_commercialization_vocabulary_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R7_loop_91_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R7","reviewed_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","reviewed_canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","reviewed_trigger_id":"R7L91_C23_326030_20240705_STAGE2_CNS_COMMERCIALIZATION_REVENUE","symbol":"326030","company_name":"SK바이오팜","entry_date":"2024-07-05","entry_price":79000.0,"positive_or_counterexample":"positive_control_or_positive_watch","MFE_90D_pct":64.56,"MAE_90D_pct":-2.91,"MFE_180D_pct":64.56,"MAE_180D_pct":-2.91,"trigger_outcome_label":"positive_high_MFE90_low_MAE_commercialization_revenue_bridge","current_profile_verdict":"current_profile_correct_if_launch_revenue_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R7_loop_91_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R8","reviewed_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","reviewed_canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","reviewed_trigger_id":"R8L91_C26_104200_20240119_STAGE2_FALSE_POSITIVE_MUSIC_PLATFORM","symbol":"104200","company_name":"NHN벅스","entry_date":"2024-01-19","entry_price":4805.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":21.54,"MAE_90D_pct":-11.86,"MFE_180D_pct":21.54,"MAE_180D_pct":-45.89,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_ARPU_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_music_platform_content_theme_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R8_loop_91_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R8","reviewed_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","reviewed_canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","reviewed_trigger_id":"R8L91_C26_181710_20240129_STAGE2_PLATFORM_OPERATING_LEVERAGE","symbol":"181710","company_name":"NHN","entry_date":"2024-01-29","entry_price":22450.0,"positive_or_counterexample":"positive_control_or_positive_watch","MFE_90D_pct":30.29,"MAE_90D_pct":-3.56,"MFE_180D_pct":30.29,"MAE_180D_pct":-30.33,"trigger_outcome_label":"positive_MFE90_ge30_low_entry_MAE_but_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_ARPU_mix_cost_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R8_loop_91_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R8","reviewed_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","reviewed_canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","reviewed_trigger_id":"R8L91_C26_236810_20240103_STAGE2_FALSE_POSITIVE_REWARD_ADTECH","symbol":"236810","company_name":"엔비티","entry_date":"2024-01-03","entry_price":9010.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":17.65,"MAE_90D_pct":-38.62,"MFE_180D_pct":17.65,"MAE_180D_pct":-68.65,"trigger_outcome_label":"counterexample_sub_Yellow_MFE_extreme_MAE_no_ad_revenue_bridge","current_profile_verdict":"current_profile_false_positive_if_reward_adtech_spike_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R8_loop_91_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R9","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_id":"R9L91_C29_012280_20240111_STAGE2_FALSE_POSITIVE_CASTING_AUTOPARTS","symbol":"012280","company_name":"영화금속","entry_date":"2024-01-11","entry_price":989.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":1.11,"MAE_90D_pct":-14.05,"MFE_180D_pct":1.11,"MAE_180D_pct":-25.58,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_utilization_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_casting_autoparts_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R9_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R9","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_id":"R9L91_C29_033250_20240102_STAGE2_FALSE_POSITIVE_CHASSIS_PARTS","symbol":"033250","company_name":"체시스","entry_date":"2024-01-02","entry_price":1863.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":5.74,"MAE_90D_pct":-39.88,"MFE_180D_pct":5.74,"MAE_180D_pct":-43.1,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_OEM_volume_bridge","current_profile_verdict":"current_profile_false_positive_if_chassis_parts_vocabulary_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R9_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R9","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_id":"R9L91_C29_123410_20240122_STAGE2_HYBRID_VOLUME_MIX","symbol":"123410","company_name":"코리아에프티","entry_date":"2024-01-22","entry_price":3855.0,"positive_or_counterexample":"positive_control_or_positive_watch","MFE_90D_pct":112.45,"MAE_90D_pct":-5.32,"MFE_180D_pct":112.45,"MAE_180D_pct":-5.32,"trigger_outcome_label":"positive_high_MFE90_low_MAE_customer_volume_mix_bridge","current_profile_verdict":"current_profile_correct_if_OEM_volume_program_mix_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R9_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R10","reviewed_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","reviewed_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_id":"R10L91_C30_002290_20240102_STAGE2_FALSE_POSITIVE_SMALL_CONSTRUCTION_POLICY","symbol":"002290","company_name":"삼일기업공사","entry_date":"2024-01-02","entry_price":4220.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":2.49,"MAE_90D_pct":-19.67,"MFE_180D_pct":15.64,"MAE_180D_pct":-33.65,"trigger_outcome_label":"counterexample_low_local_MFE_deep_MAE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_small_construction_policy_vocabulary_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R10_loop_91_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R10","reviewed_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","reviewed_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_id":"R10L91_C30_006390_20240531_STAGE2_CEMENT_ASP_MARGIN","symbol":"006390","company_name":"한일현대시멘트","entry_date":"2024-05-31","entry_price":14980.0,"positive_or_counterexample":"positive_control_or_positive_watch","MFE_90D_pct":14.82,"MAE_90D_pct":-9.21,"MFE_180D_pct":14.82,"MAE_180D_pct":-12.55,"trigger_outcome_label":"positive_watch_moderate_MFE_low_entry_MAE_but_inactive_like_data_quality_watch","current_profile_verdict":"current_profile_correct_if_ASP_input_cost_margin_cash_bridge_required_and_data_quality_repaired","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R10_loop_91_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R10","reviewed_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","reviewed_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_id":"R10L91_C30_025750_20240110_STAGE2_FALSE_POSITIVE_HOME_MATERIALS","symbol":"025750","company_name":"한솔홈데코","entry_date":"2024-01-10","entry_price":873.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":1.6,"MAE_90D_pct":-13.86,"MFE_180D_pct":1.6,"MAE_180D_pct":-34.82,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_housing_margin_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_home_materials_rebound_overcredited","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R10_loop_91_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R11","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","reviewed_trigger_id":"R11L91_C04_036190_20240102_STAGE2_FALSE_POSITIVE_LEGACY_PLANT_MAINTENANCE","symbol":"036190","company_name":"금화피에스시","entry_date":"2024-01-02","entry_price":26050.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":10.17,"MAE_90D_pct":-4.8,"MFE_180D_pct":10.17,"MAE_180D_pct":-9.02,"trigger_outcome_label":"counterexample_low_MFE_low_MAE_no_fresh_project_bridge","current_profile_verdict":"current_profile_false_positive_if_maintenance_vocabulary_overcredited_as_nuclear_project","r13_guard_verdict":"hard_4B_watch_bridge_missing_or_unverified","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R11_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R11","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","reviewed_trigger_id":"R11L91_C04_126720_20240122_STAGE2_NUCLEAR_OM_PROJECT","symbol":"126720","company_name":"수산인더스트리","entry_date":"2024-01-22","entry_price":19040.0,"positive_or_counterexample":"positive_control_or_positive_watch","MFE_90D_pct":65.97,"MAE_90D_pct":-5.99,"MFE_180D_pct":65.97,"MAE_180D_pct":-5.99,"trigger_outcome_label":"positive_high_MFE90_low_MAE_project_execution_bridge","current_profile_verdict":"current_profile_correct_if_project_approval_OM_contract_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R11_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R11","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","reviewed_trigger_id":"R11L91_C04_457550_20240126_STAGE2_FALSE_POSITIVE_RECENT_LISTING_NUCLEAR_SPIKE","symbol":"457550","company_name":"우진엔텍","entry_date":"2024-01-26","entry_price":31000.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":23.39,"MAE_90D_pct":-52.39,"MFE_180D_pct":23.39,"MAE_180D_pct":-52.39,"trigger_outcome_label":"counterexample_price_spike_high_MAE_recent_listing_no_project_bridge","current_profile_verdict":"current_profile_false_positive_if_recent_listing_nuclear_spike_overcredited","r13_guard_verdict":"hard_4B_watch_with_data_quality_repair_required","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R11_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R12","reviewed_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","reviewed_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reviewed_trigger_id":"R12L91_C31_034230_20240401_STAGE2_FALSE_POSITIVE_CASINO_TOURISM_POLICY","symbol":"034230","company_name":"파라다이스","entry_date":"2024-04-01","entry_price":15310.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":2.61,"MAE_90D_pct":-19.92,"MFE_180D_pct":2.61,"MAE_180D_pct":-41.08,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_market_segment_watch","current_profile_verdict":"current_profile_false_positive_if_tourism_casino_policy_vocabulary_overcredited","r13_guard_verdict":"hard_4B_watch_with_data_quality_repair_required","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R12_loop_91_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R12","reviewed_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","reviewed_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reviewed_trigger_id":"R12L91_C31_068290_20240110_STAGE2_FALSE_POSITIVE_LOWBIRTH_CHILDCARE_POLICY","symbol":"068290","company_name":"삼성출판사","entry_date":"2024-01-10","entry_price":24000.0,"positive_or_counterexample":"counterexample","MFE_90D_pct":24.79,"MAE_90D_pct":-22.88,"MFE_180D_pct":24.79,"MAE_180D_pct":-46.33,"trigger_outcome_label":"counterexample_price_MFE_but_deep_MAE_no_policy_to_revenue_bridge","current_profile_verdict":"current_profile_false_positive_if_low_birth_policy_price_MFE_overcredited","r13_guard_verdict":"hard_4B_watch_price_MFE_without_bridge","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R12_loop_91_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
{"row_type":"r13_review_trigger","round":"R13","loop":"91","reviewed_round":"R12","reviewed_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","reviewed_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reviewed_trigger_id":"R12L91_C31_086790_20240129_STAGE2_VALUEUP_POLICY_CAPITAL_RETURN","symbol":"086790","company_name":"하나금융지주","entry_date":"2024-01-29","entry_price":46400.0,"positive_or_counterexample":"positive_control_or_positive_watch","MFE_90D_pct":40.73,"MAE_90D_pct":-3.45,"MFE_180D_pct":49.14,"MAE_180D_pct":-3.45,"trigger_outcome_label":"positive_high_MFE90_low_MAE_policy_to_cash_bridge","current_profile_verdict":"current_profile_correct_if_policy_timetable_payout_capital_return_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R12_loop_91_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md"}
```

## 7. Guardrail stress-test results

```jsonl
{"row_type":"r13_guardrail_summary","round":"R13","loop":"91","guardrail_id":"bridge_missing_price_only_data_quality_4B_4C_guard","reviewed_trigger_count":36,"positive_control_count":12,"counterexample_count":24,"counter_MFE90_lt_20_count":20,"counter_MFE90_ge_20_price_only_count":4,"counter_MAE90_le_minus20_count":12,"counter_MAE180_le_minus25_count":21,"counter_MAE180_le_minus35_count":15,"price_only_like_count":3,"late_rebound_or_spike_not_validation_count":2,"data_quality_watch_count":6,"four_c_watch_count":1,"verdict":"existing calibrated axes are directionally correct; do not loosen Green; future batch can add canonical bridge-required guards as shadow-only candidates."}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"91","rule_candidate":"cross_archetype_bridge_missing_hard_4B_watch","condition":"bridge_missing_or_unverified AND (MFE90 < 20 OR MAE180 <= -25 OR evidence_type includes price_only)","action":"block Stage2-Actionable/Yellow/Green; route to Watch/4B/evidence repair","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"91","rule_candidate":"late_rebound_or_spike_not_entry_validation","condition":"original_entry_bridge_missing AND later_full_window_or_Q4_spike_occurs","action":"do not retroactively validate original entry; require fresh trigger date and fresh non-price bridge evidence","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"91","rule_candidate":"data_quality_repair_before_patch","condition":"recent_listing_or_market_segment_change_or_inactive_like_or_post_candidate_watch_present","action":"allow research annotation but block production patch until price path and exact evidence are repaired","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"91","rule_candidate":"4C_regulatory_failure_hard_watch","condition":"CRL_or_review_failure_or_thesis_break_risk_materialized","action":"route to hard 4C-watch; do not classify as mere weak 4B","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"91","rule_candidate":"Green_requires_exact_non_price_bridge","condition":"positive_control_has_high_MFE_but_source_proxy_only_or_late_drawdown_or_data_quality_watch","action":"allow Yellow/Green-candidate-watch only; exact source-grade bridge required before Green","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
```

## 8. Sector-by-sector redteam notes

```text
R1 / C05 EPC:
  100840 confirms order/backlog/delivery/margin bridge but remains post-candidate data-quality watch. 028050 and 037350 show EPC/cleanroom vocabulary fails without signed order, delivery and cash evidence.

R2 / C07 HBM equipment:
  084370 confirms HBM/deposition order-ramp bridge. 086390 and 217190 show tester/backend HBM equipment vocabulary fails without customer order, qualification, delivery and margin bridge.

R3 / C13 battery JV/AMPC:
  036830 confirms electrolyte/JV utilization/AMPC bridge. 014820 and 095500 show packaging/lithium/IRA vocabulary fails without utilization, offtake, subsidy and cash bridge.

R4 / C15 materials spread:
  006340 confirms copper-wire inventory/spread bridge but has C02 overlap watch. 005810 and 008350 show holdco/aluminum vocabulary fails without direct spread, ASP, margin and cash evidence.

R5 / C20 beauty/food distribution:
  003350 confirms K-beauty manufacturing/export/reorder bridge. 051900 and 004370 show legacy beauty or food global vocabulary fails after the first move without fresh sell-through, reorder, margin and cash bridge.

R6 / C21 financial value-up:
  005940 confirms large-brokerage dividend/value-up/capital-return bridge. 030610 and 001290 show small brokerage/PBR/turnaround vocabulary fails without explicit payout, buyback, ROE and capital-quality bridge.

R7 / C23 bio commercialization:
  326030 confirms CNS commercialization/revenue bridge. 067630 is approval-expectation CRL/review-failure 4C-watch. 229000 is diagnostic commercialization 4B-watch without reimbursement, adoption, revenue and cash bridge.

R8 / C26 platform operating leverage:
  181710 confirms platform revenue-mix/cost-discipline bridge but Green stays strict after drawdown. 236810 and 104200 show adtech/music platform vocabulary fails without advertiser retention, ARPU, margin and cash bridge.

R9 / C29 mobility:
  123410 confirms hybrid auto-parts OEM-volume/program-mix bridge. 033250 and 012280 show chassis/casting vocabulary fails without fresh customer volume, utilization, price/cost and margin bridge.

R10 / C30 construction:
  006390 is cement ASP/margin positive-watch but inactive-like data-quality repair is required. 002290 and 025750 show small construction/home-materials vocabulary fails without PF/backlog/housing-demand/margin/cash bridge.

R11 / C04 nuclear:
  126720 confirms nuclear O&M/project execution bridge. 457550 is recent-listing SMR/nuclear-service 4B/data-quality watch. 036190 shows stable maintenance vocabulary is not nuclear project/legal milestone evidence.

R12 / C31 policy:
  086790 confirms value-up policy-to-capital-return bridge. 034230 and 068290 show casino/low-birth policy vocabulary fails without implementation, revenue channel, margin and cash bridge.
```

## 9. Shadow-only recommendations

```jsonl
{"row_type":"shadow_weight","round":"R13","loop":"91","axis":"cross_archetype_bridge_required_before_Yellow","scope":"cross_archetype","candidate_delta":0.0,"direction":"diagnostic_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Across loop91, positive controls averaged MFE90 90.29% while weak-bridge counterexamples averaged MFE90 9.04% and MAE180 -42.43%."}
{"row_type":"shadow_weight","round":"R13","loop":"91","axis":"cross_archetype_price_MFE_not_positive_evidence","scope":"cross_archetype","candidate_delta":0.0,"direction":"diagnostic_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Counterexamples with MFE90 >= 20 still appeared where high MFE was price-only, recent-listing, or bridge-missing."}
{"row_type":"shadow_weight","round":"R13","loop":"91","axis":"cross_archetype_late_rebound_or_spike_not_original_entry_validation","scope":"cross_archetype","candidate_delta":0.0,"direction":"diagnostic_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Late-spike/rebound flags appeared in construction and battery-policy rows, but the original weak entry was not validated without fresh evidence."}
{"row_type":"shadow_weight","round":"R13","loop":"91","axis":"cross_archetype_data_quality_repair_before_patch","scope":"cross_archetype","candidate_delta":0.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Recent-listing, market-segment-change, inactive-like, post-candidate and future-candidate watch rows require repair before production patch consideration."}
{"row_type":"shadow_weight","round":"R13","loop":"91","axis":"cross_archetype_4C_failure_risk_not_4B","scope":"cross_archetype","candidate_delta":0.0,"direction":"hard_failure_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"C23/067630 shows approval expectation with regulatory failure risk should route to hard 4C-watch."}
{"row_type":"shadow_weight","round":"R13","loop":"91","axis":"cross_archetype_Green_requires_exact_non_price_bridge","scope":"cross_archetype","candidate_delta":0.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"All 12 positive/positive-watch controls remain source-proxy-only and require exact evidence before Green."}
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
  - price_only_or_price_MFE_overcredit
  - late_rebound_or_spike_not_entry_validation
  - data_quality_watch_before_patch
  - regulatory_failure_4C_watch
  - source_proxy_only_before_Green

diagnostic_axis_proposed:
  - cross_archetype_bridge_missing_hard_4B_watch
  - cross_archetype_price_MFE_not_positive_evidence
  - cross_archetype_late_rebound_or_spike_not_entry_validation
  - cross_archetype_data_quality_repair_before_patch
  - cross_archetype_4C_failure_risk_not_4B
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
3. Confirm reviewed rows came from R1~R12 loop91 MDs.
4. Confirm all reviewed source rows use:
   - price_data_source=Songdaiki/stock-web
   - price_basis=tradable_raw
   - price_adjustment_status=raw_unadjusted_marcap
5. Confirm R13 / L10 / R13_CROSS_ARCHETYPE_4B_4C_REDTEAM round-sector consistency.
6. Treat all recommendations here as shadow-only diagnostics.
7. Do not apply weight deltas from this MD alone.
8. Use this MD to prioritize exact evidence repair and canonical guard design:
   - bridge_missing_hard_4B_watch
   - price_MFE_not_positive_evidence
   - late_rebound_or_spike_not_entry_validation
   - data_quality_repair_before_patch
   - 4C_failure_risk_not_4B
   - Green_requires_exact_non_price_bridge
9. Confirm accidentally touched R11/C04, R10/C30, R9/C29 and earlier-sector candidate rows are not double-counted here beyond their already-reviewed scheduled MDs.
10. Do not loosen Stage3-Green.
11. Do not use future MFE/MAE in runtime scoring.
```

## 12. Round state

```text
completed_round = R13
completed_loop = 91
next_round = R1
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 13. Final one-line contribution

```text
This R13 loop reviews 36 loop91 triggers across R1~R12, adds 0 new independent cases, and confirms that bridge-missing / price-MFE / late-rebound / data-quality / 4C-failure / Green-exact-evidence guards should remain hard Watch/4B/4C barriers before any Yellow/Green promotion.
```
