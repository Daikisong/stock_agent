# V12 Coverage Matrix

v12 coverage는 rolling calibration의 근거 장부입니다. active 반영은 검증된 apply_next_patch만 scope 제한으로 적용합니다.

| group | value | rows | symbols | positives | counterexamples | evidence URL pending | source proxy | good Stage2 | bad Stage2 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| global_v12 | all | 2222 | 559 | 200 | 451 | 34 | 36 | 454 | 438 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 1090 | 376 | 35 | 233 | 13 | 23 | 167 | 169 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 238 | 115 | 35 | 38 | 21 | 3 | 80 | 45 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS | 256 | 92 | 43 | 52 | 0 | 1 | 69 | 68 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY | 235 | 87 | 45 | 63 | 0 | 5 | 42 | 62 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE | 69 | 35 | 3 | 3 | 0 | 4 | 8 | 11 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION | 72 | 41 | 13 | 11 | 0 | 0 | 22 | 19 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 48 | 21 | 0 | 0 | 0 | 0 | 19 | 0 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL | 70 | 39 | 7 | 7 | 0 | 0 | 22 | 21 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY | 105 | 58 | 13 | 38 | 0 | 0 | 15 | 37 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING | 39 | 18 | 6 | 6 | 0 | 0 | 10 | 6 |
| canonical_archetype_id | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 53 | 24 | 12 | 6 | 0 | 0 | 20 | 8 |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX | 59 | 25 | 11 | 9 | 0 | 3 | 21 | 11 |
| canonical_archetype_id | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 46 | 21 | 0 | 8 | 21 | 0 | 20 | 6 |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 25 | 15 | 0 | 0 | 0 | 0 | 4 | 4 |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 55 | 36 | 12 | 15 | 0 | 0 | 15 | 16 |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 46 | 21 | 6 | 11 | 0 | 0 | 16 | 11 |
| canonical_archetype_id | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 32 | 24 | 5 | 5 | 0 | 1 | 4 | 4 |
| canonical_archetype_id | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 28 | 16 | 9 | 7 | 0 | 0 | 9 | 2 |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 96 | 41 | 16 | 19 | 0 | 0 | 24 | 26 |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 54 | 35 | 7 | 10 | 0 | 0 | 16 | 25 |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING | 56 | 46 | 3 | 4 | 0 | 3 | 15 | 8 |
| canonical_archetype_id | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 68 | 58 | 15 | 25 | 0 | 2 | 15 | 28 |
| canonical_archetype_id | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 23 | 12 | 2 | 6 | 0 | 0 | 2 | 12 |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C | 62 | 34 | 17 | 24 | 0 | 0 | 1 | 11 |
| canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE | 24 | 16 | 3 | 3 | 0 | 2 | 3 | 1 |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 21 | 14 | 0 | 0 | 0 | 2 | 3 | 5 |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 24 | 10 | 0 | 0 | 0 | 0 | 2 | 5 |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 27 | 16 | 5 | 5 | 0 | 0 | 9 | 10 |
| canonical_archetype_id | C19_BRAND_RETAIL_INVENTORY_MARGIN | 22 | 15 | 3 | 3 | 0 | 0 | 1 | 7 |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 23 | 13 | 5 | 3 | 0 | 0 | 12 | 2 |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 25 | 10 | 0 | 0 | 0 | 0 | 11 | 0 |
| canonical_archetype_id | C22_INSURANCE_RATE_CYCLE_RESERVE | 23 | 12 | 0 | 0 | 0 | 0 | 8 | 0 |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 27 | 14 | 0 | 0 | 0 | 0 | 8 | 9 |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK | 22 | 13 | 4 | 4 | 0 | 0 | 5 | 2 |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 21 | 15 | 3 | 3 | 0 | 0 | 9 | 10 |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 36 | 14 | 5 | 18 | 0 | 0 | 8 | 13 |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION | 28 | 15 | 4 | 9 | 0 | 0 | 4 | 11 |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 41 | 29 | 4 | 11 | 0 | 0 | 3 | 13 |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 26 | 14 | 8 | 4 | 0 | 0 | 9 | 3 |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 39 | 18 | 6 | 6 | 0 | 0 | 10 | 6 |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 24 | 24 | 5 | 4 | 0 | 0 | 4 | 2 |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 46 | 13 | 0 | 0 | 0 | 0 | 15 | 0 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 216 | 159 | 15 | 33 | 0 | 0 | 32 | 27 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 339 | 238 | 12 | 55 | 0 | 9 | 52 | 37 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 291 | 209 | 3 | 93 | 0 | 0 | 47 | 36 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 174 | 143 | 0 | 48 | 13 | 14 | 17 | 67 |
