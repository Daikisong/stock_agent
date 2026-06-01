# V12 Coverage Matrix

v12 coverage는 rolling calibration의 근거 장부입니다. active 반영은 검증된 apply_next_patch만 scope 제한으로 적용합니다.

| group | value | rows | symbols | positives | counterexamples | evidence URL pending | source proxy | good Stage2 | bad Stage2 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| global_v12 | all | 3699 | 492 | 670 | 754 | 525 | 523 | 1112 | 463 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 784 | 210 | 98 | 140 | 73 | 68 | 207 | 142 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 257 | 56 | 98 | 95 | 59 | 62 | 99 | 25 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS | 270 | 39 | 74 | 91 | 42 | 42 | 84 | 19 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY | 466 | 62 | 92 | 110 | 81 | 77 | 124 | 66 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE | 278 | 59 | 56 | 87 | 44 | 40 | 89 | 33 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION | 415 | 41 | 63 | 52 | 42 | 46 | 125 | 48 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 397 | 31 | 54 | 35 | 58 | 55 | 139 | 53 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL | 323 | 50 | 55 | 48 | 42 | 49 | 110 | 22 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY | 353 | 63 | 63 | 70 | 42 | 42 | 120 | 34 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING | 156 | 29 | 17 | 26 | 42 | 42 | 15 | 21 |
| canonical_archetype_id | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 23 | 12 | 13 | 7 | 15 | 18 | 14 | 1 |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX | 64 | 11 | 26 | 23 | 17 | 17 | 33 | 1 |
| canonical_archetype_id | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 89 | 13 | 31 | 31 | 15 | 15 | 40 | 7 |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 62 | 14 | 25 | 29 | 9 | 9 | 9 | 9 |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 19 | 12 | 3 | 5 | 3 | 3 | 3 | 7 |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 37 | 5 | 7 | 9 | 3 | 3 | 10 | 2 |
| canonical_archetype_id | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 68 | 22 | 25 | 23 | 12 | 12 | 28 | 4 |
| canonical_archetype_id | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 78 | 13 | 15 | 27 | 12 | 12 | 24 | 9 |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 56 | 17 | 19 | 25 | 6 | 6 | 7 | 0 |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 31 | 10 | 8 | 7 | 9 | 9 | 15 | 4 |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING | 79 | 21 | 13 | 20 | 12 | 12 | 31 | 9 |
| canonical_archetype_id | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 68 | 18 | 18 | 25 | 11 | 11 | 15 | 2 |
| canonical_archetype_id | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 43 | 11 | 8 | 12 | 6 | 6 | 10 | 9 |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C | 76 | 15 | 17 | 19 | 6 | 6 | 0 | 0 |
| canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE | 71 | 25 | 21 | 24 | 12 | 12 | 21 | 8 |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 67 | 23 | 14 | 32 | 13 | 13 | 17 | 7 |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 140 | 23 | 21 | 31 | 19 | 15 | 51 | 18 |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 126 | 20 | 23 | 19 | 18 | 18 | 41 | 14 |
| canonical_archetype_id | C19_BRAND_RETAIL_INVENTORY_MARGIN | 89 | 17 | 12 | 17 | 21 | 25 | 17 | 14 |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 200 | 18 | 28 | 16 | 3 | 3 | 67 | 20 |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 235 | 24 | 30 | 18 | 26 | 23 | 86 | 24 |
| canonical_archetype_id | C22_INSURANCE_RATE_CYCLE_RESERVE | 162 | 11 | 24 | 17 | 32 | 32 | 53 | 29 |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 139 | 15 | 16 | 9 | 9 | 9 | 39 | 7 |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK | 83 | 19 | 19 | 17 | 15 | 22 | 30 | 7 |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 101 | 21 | 20 | 22 | 18 | 18 | 41 | 8 |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 137 | 16 | 21 | 26 | 12 | 12 | 50 | 17 |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION | 114 | 25 | 26 | 22 | 15 | 15 | 42 | 11 |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 102 | 22 | 16 | 22 | 15 | 15 | 28 | 6 |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 203 | 36 | 38 | 35 | 46 | 42 | 68 | 46 |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 159 | 29 | 18 | 28 | 42 | 42 | 15 | 21 |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 206 | 77 | 30 | 59 | 39 | 40 | 41 | 38 |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 157 | 23 | 18 | 24 | 34 | 28 | 51 | 23 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 368 | 137 | 42 | 41 | 0 | 0 | 104 | 68 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 12 | 12 | 4 | 8 | 0 | 0 | 5 | 3 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 23 | 21 | 1 | 5 | 0 | 0 | 3 | 7 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 12 | 12 | 0 | 0 | 0 | 0 | 3 | 3 |
