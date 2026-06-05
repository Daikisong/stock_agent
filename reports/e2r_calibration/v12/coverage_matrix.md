# V12 Coverage Matrix

v12 coverage는 rolling calibration의 근거 장부입니다. active 반영은 검증된 apply_next_patch만 scope 제한으로 적용합니다.

| group | value | rows | symbols | positives | counterexamples | evidence URL pending | source proxy | good Stage2 | bad Stage2 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| global_v12 | all | 1621 | 539 | 141 | 640 | 1390 | 1066 | 401 | 517 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 669 | 373 | 15 | 207 | 488 | 439 | 137 | 309 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 134 | 68 | 18 | 55 | 124 | 99 | 43 | 25 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS | 89 | 49 | 12 | 38 | 83 | 57 | 27 | 20 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY | 184 | 97 | 26 | 88 | 174 | 122 | 45 | 41 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE | 92 | 53 | 10 | 40 | 89 | 57 | 23 | 17 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION | 90 | 40 | 14 | 40 | 87 | 57 | 26 | 18 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 90 | 30 | 9 | 45 | 87 | 57 | 25 | 23 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL | 89 | 50 | 13 | 43 | 83 | 57 | 33 | 17 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY | 87 | 48 | 13 | 41 | 84 | 57 | 23 | 20 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING | 97 | 45 | 11 | 43 | 91 | 64 | 19 | 27 |
| canonical_archetype_id | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 16 | 12 | 1 | 9 | 16 | 9 | 7 | 3 |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX | 24 | 13 | 4 | 8 | 21 | 18 | 8 | 3 |
| canonical_archetype_id | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 30 | 16 | 4 | 11 | 30 | 27 | 10 | 6 |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 31 | 13 | 4 | 14 | 27 | 21 | 9 | 7 |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 33 | 17 | 5 | 13 | 30 | 24 | 9 | 6 |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 21 | 16 | 3 | 9 | 18 | 12 | 6 | 4 |
| canonical_archetype_id | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 18 | 16 | 4 | 8 | 18 | 15 | 5 | 3 |
| canonical_archetype_id | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 14 | 11 | 1 | 7 | 14 | 9 | 4 | 4 |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 15 | 11 | 2 | 7 | 15 | 9 | 6 | 3 |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 21 | 18 | 2 | 7 | 18 | 12 | 6 | 6 |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING | 23 | 16 | 2 | 12 | 23 | 15 | 7 | 5 |
| canonical_archetype_id | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 27 | 21 | 4 | 11 | 24 | 18 | 9 | 4 |
| canonical_archetype_id | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 27 | 17 | 5 | 13 | 24 | 18 | 6 | 6 |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C | 21 | 17 | 0 | 8 | 21 | 15 | 3 | 3 |
| canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE | 33 | 24 | 3 | 15 | 33 | 18 | 6 | 7 |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 30 | 20 | 4 | 14 | 30 | 18 | 9 | 4 |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 29 | 15 | 3 | 11 | 26 | 21 | 8 | 6 |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 33 | 22 | 5 | 16 | 33 | 21 | 11 | 8 |
| canonical_archetype_id | C19_BRAND_RETAIL_INVENTORY_MARGIN | 24 | 12 | 4 | 8 | 21 | 15 | 5 | 4 |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 33 | 17 | 5 | 16 | 33 | 21 | 10 | 6 |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 48 | 23 | 5 | 25 | 45 | 30 | 15 | 10 |
| canonical_archetype_id | C22_INSURANCE_RATE_CYCLE_RESERVE | 42 | 9 | 4 | 20 | 42 | 27 | 10 | 13 |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 29 | 20 | 5 | 15 | 26 | 18 | 11 | 7 |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK | 27 | 17 | 4 | 14 | 27 | 18 | 11 | 4 |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 33 | 17 | 4 | 14 | 30 | 21 | 11 | 6 |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 36 | 16 | 5 | 19 | 33 | 21 | 11 | 6 |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION | 24 | 17 | 4 | 11 | 24 | 15 | 6 | 7 |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 27 | 15 | 4 | 11 | 27 | 21 | 6 | 7 |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 86 | 53 | 15 | 44 | 82 | 56 | 20 | 23 |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 97 | 45 | 11 | 43 | 91 | 64 | 19 | 27 |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 77 | 57 | 7 | 35 | 69 | 36 | 22 | 17 |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 55 | 32 | 6 | 22 | 52 | 36 | 12 | 14 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 351 | 286 | 0 | 35 | 190 | 190 | 80 | 188 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 129 | 117 | 2 | 67 | 129 | 129 | 23 | 66 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 57 | 57 | 0 | 48 | 48 | 48 | 0 | 24 |
