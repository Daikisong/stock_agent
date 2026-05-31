# V12 Rolling Calibration State

이 파일은 연구 자료가 어떤 작은 패치로 바뀌었는지 추적하는 장부입니다.
`run-v12-calibration`은 이 장부의 apply_next_patch를 E2R 2.2 rolling profile에 반영합니다.

- archetype_count: `36`
- decision_counts: `{'apply_next_patch': 111, 'blocked_by_data_quality': 5, 'hold_for_more_evidence': 3}`
- patch_spec_count: `111`
- production_default_scoring_changed: `run-v12-calibration에서 true`

| archetype | large_sector | positive_symbols | counterexample_symbols | 4B_cases | 4C_cases | next_delta_recommendation |
|---|---|---:|---:|---:|---:|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 5 | 3 | 0 | 0 | apply_limited_next_patch |
| C02_POWER_GRID_DATACENTER_CAPEX | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 4 | 7 | 9 | 0 | apply_limited_next_patch |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 7 | 9 | 15 | 0 | apply_limited_next_patch |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 9 | 9 | 18 | 0 | apply_limited_next_patch |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 2 | 3 | 0 | 4 | apply_limited_next_patch |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | L2_AI_SEMICONDUCTOR_ELECTRONICS | 1 | 2 | 4 | 1 | apply_limited_next_patch |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | L2_AI_SEMICONDUCTOR_ELECTRONICS | 10 | 15 | 12 | 0 | apply_limited_next_patch |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | L2_AI_SEMICONDUCTOR_ELECTRONICS | 7 | 8 | 12 | 0 | apply_limited_next_patch |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | L2_AI_SEMICONDUCTOR_ELECTRONICS | 11 | 13 | 11 | 1 | apply_limited_next_patch |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | L2_AI_SEMICONDUCTOR_ELECTRONICS | 6 | 3 | 0 | 0 | apply_limited_next_patch |
| C11_BATTERY_ORDERBOOK_RERATING | L3_BATTERY_EV_GREEN_MOBILITY | 8 | 14 | 8 | 0 | apply_limited_next_patch |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | L3_BATTERY_EV_GREEN_MOBILITY | 9 | 9 | 7 | 1 | apply_limited_next_patch |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | L3_BATTERY_EV_GREEN_MOBILITY | 2 | 6 | 2 | 0 | apply_limited_next_patch |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | L3_BATTERY_EV_GREEN_MOBILITY | 10 | 9 | 17 | 9 | apply_limited_next_patch |
| C15_MATERIAL_SPREAD_SUPERCYCLE | L4_MATERIALS_SPREAD_RESOURCE | 11 | 11 | 11 | 0 | apply_limited_next_patch |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | L4_MATERIALS_SPREAD_RESOURCE | 8 | 13 | 14 | 0 | apply_limited_next_patch |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | L4_MATERIALS_SPREAD_RESOURCE | 14 | 13 | 14 | 2 | apply_limited_next_patch |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | L5_CONSUMER_BRAND_DISTRIBUTION | 8 | 8 | 7 | 3 | apply_limited_next_patch |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | L5_CONSUMER_BRAND_DISTRIBUTION | 4 | 7 | 9 | 5 | apply_limited_next_patch |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | L5_CONSUMER_BRAND_DISTRIBUTION | 9 | 8 | 14 | 7 | apply_limited_next_patch |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 11 | 6 | 9 | 0 | apply_limited_next_patch |
| C22_INSURANCE_RATE_CYCLE_RESERVE | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 5 | 6 | 10 | 3 | apply_limited_next_patch |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | L7_BIO_HEALTHCARE_MEDICAL | 3 | 3 | 7 | 4 | apply_limited_next_patch |
| C24_BIO_TRIAL_DATA_EVENT_RISK | L7_BIO_HEALTHCARE_MEDICAL | 7 | 9 | 1 | 4 | apply_limited_next_patch |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | L7_BIO_HEALTHCARE_MEDICAL | 8 | 10 | 9 | 2 | apply_limited_next_patch |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | L8_PLATFORM_CONTENT_SW_SECURITY | 7 | 10 | 6 | 1 | apply_limited_next_patch |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | L8_PLATFORM_CONTENT_SW_SECURITY | 12 | 15 | 15 | 4 | apply_limited_next_patch |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | L8_PLATFORM_CONTENT_SW_SECURITY | 7 | 10 | 12 | 2 | apply_limited_next_patch |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | L3_BATTERY_EV_GREEN_MOBILITY | 12 | 13 | 15 | 4 | apply_limited_next_patch |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | L9_CONSTRUCTION_REALESTATE_HOUSING | 12 | 19 | 4 | 8 | apply_limited_next_patch |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 25 | 30 | 20 | 0 | apply_limited_next_patch |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 7 | 10 | 14 | 1 | apply_limited_next_patch |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 37 | 35 | 12 | 13 | apply_limited_next_patch |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 4 | 8 | 0 | 0 | apply_limited_next_patch |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 2 | 12 | 1 | 1 | apply_limited_next_patch |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 3 | 1 | 1 | 1 | apply_limited_next_patch |
