# V12 Rolling Calibration State

이 파일은 연구 자료가 어떤 작은 패치로 바뀌었는지 추적하는 장부입니다.
`run-v12-calibration`은 이 장부의 apply_next_patch를 E2R 2.2 rolling profile에 반영합니다.

- archetype_count: `27`
- decision_counts: `{'apply_next_patch': 64, 'hold_for_more_evidence': 14, 'blocked_by_data_quality': 3}`
- patch_spec_count: `64`
- production_default_scoring_changed: `run-v12-calibration에서 true`

| archetype | large_sector | positive_symbols | counterexample_symbols | 4B_cases | 4C_cases | next_delta_recommendation |
|---|---|---:|---:|---:|---:|---|
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 0 | 0 | 0 | 0 | hold_for_more_non_overlapping_evidence |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 2 | 1 | 1 | 0 | apply_limited_next_patch |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | L2_AI_SEMICONDUCTOR_ELECTRONICS | 1 | 1 | 0 | 1 | apply_limited_next_patch |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | L2_AI_SEMICONDUCTOR_ELECTRONICS | 3 | 2 | 1 | 0 | apply_limited_next_patch |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | L2_AI_SEMICONDUCTOR_ELECTRONICS | 3 | 2 | 2 | 1 | apply_limited_next_patch |
| C11_BATTERY_ORDERBOOK_RERATING | L3_BATTERY_EV_GREEN_MOBILITY | 2 | 0 | 0 | 0 | hold_for_more_non_overlapping_evidence |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | L3_BATTERY_EV_GREEN_MOBILITY | 4 | 3 | 0 | 0 | apply_limited_next_patch |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | L3_BATTERY_EV_GREEN_MOBILITY | 0 | 1 | 0 | 0 | apply_limited_next_patch |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | L3_BATTERY_EV_GREEN_MOBILITY | 3 | 1 | 3 | 3 | apply_limited_next_patch |
| C15_MATERIAL_SPREAD_SUPERCYCLE | L4_MATERIALS_SPREAD_RESOURCE | 0 | 0 | 0 | 0 | hold_for_more_non_overlapping_evidence |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | L4_MATERIALS_SPREAD_RESOURCE | 0 | 0 | 0 | 0 | hold_for_more_non_overlapping_evidence |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | L4_MATERIALS_SPREAD_RESOURCE | 2 | 2 | 0 | 0 | hold_for_more_non_overlapping_evidence |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | L5_CONSUMER_BRAND_DISTRIBUTION | 4 | 4 | 2 | 1 | apply_limited_next_patch |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | L5_CONSUMER_BRAND_DISTRIBUTION | 0 | 0 | 3 | 2 | apply_limited_next_patch |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | L5_CONSUMER_BRAND_DISTRIBUTION | 5 | 5 | 8 | 1 | apply_limited_next_patch |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 10 | 4 | 4 | 0 | apply_limited_next_patch |
| C22_INSURANCE_RATE_CYCLE_RESERVE | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 2 | 3 | 1 | 0 | apply_limited_next_patch |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | L7_BIO_HEALTHCARE_MEDICAL | 2 | 2 | 1 | 0 | apply_limited_next_patch |
| C24_BIO_TRIAL_DATA_EVENT_RISK | L7_BIO_HEALTHCARE_MEDICAL | 5 | 6 | 0 | 0 | apply_limited_next_patch |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | L7_BIO_HEALTHCARE_MEDICAL | 3 | 4 | 2 | 0 | apply_limited_next_patch |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | L8_PLATFORM_CONTENT_SW_SECURITY | 3 | 7 | 0 | 0 | apply_limited_next_patch |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | L8_PLATFORM_CONTENT_SW_SECURITY | 9 | 5 | 6 | 3 | apply_limited_next_patch |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | L8_PLATFORM_CONTENT_SW_SECURITY | 5 | 6 | 6 | 2 | apply_limited_next_patch |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | L3_BATTERY_EV_GREEN_MOBILITY | 2 | 1 | 0 | 0 | hold_for_more_non_overlapping_evidence |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | L9_CONSTRUCTION_REALESTATE_HOUSING | 2 | 2 | 0 | 0 | apply_limited_next_patch |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 3 | 5 | 1 | 0 | apply_limited_next_patch |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 3 | 4 | 2 | 0 | apply_limited_next_patch |
