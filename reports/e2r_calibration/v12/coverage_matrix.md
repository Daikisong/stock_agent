# V12 Coverage Matrix

v12 coverage는 rolling calibration의 근거 장부입니다. active 반영은 검증된 apply_next_patch만 scope 제한으로 적용합니다.

| group | value | rows | symbols | positives | counterexamples | evidence URL pending | source proxy | good Stage2 | bad Stage2 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| global_v12 | all | 1121 | 448 | 221 | 269 | 327 | 303 | 428 | 250 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 277 | 153 | 41 | 70 | 92 | 92 | 103 | 71 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 90 | 52 | 21 | 20 | 21 | 21 | 46 | 18 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS | 85 | 39 | 15 | 19 | 29 | 20 | 42 | 14 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY | 153 | 59 | 28 | 32 | 39 | 35 | 55 | 28 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE | 85 | 45 | 18 | 28 | 26 | 26 | 35 | 12 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION | 95 | 38 | 20 | 15 | 40 | 27 | 33 | 20 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 88 | 30 | 21 | 13 | 21 | 24 | 32 | 22 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL | 89 | 47 | 20 | 20 | 23 | 17 | 34 | 20 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY | 78 | 44 | 15 | 26 | 16 | 16 | 32 | 16 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING | 81 | 31 | 22 | 27 | 20 | 25 | 16 | 29 |
| canonical_archetype_id | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 25 | 14 | 6 | 3 | 8 | 8 | 16 | 4 |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX | 22 | 12 | 4 | 2 | 6 | 6 | 11 | 4 |
| canonical_archetype_id | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 21 | 12 | 5 | 5 | 7 | 7 | 11 | 3 |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 12 | 7 | 2 | 4 | 0 | 0 | 5 | 3 |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 10 | 9 | 4 | 6 | 0 | 0 | 3 | 4 |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 7 | 6 | 2 | 1 | 3 | 0 | 4 | 1 |
| canonical_archetype_id | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 11 | 9 | 6 | 4 | 0 | 0 | 7 | 0 |
| canonical_archetype_id | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 21 | 11 | 2 | 4 | 3 | 3 | 9 | 5 |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 17 | 11 | 2 | 4 | 7 | 7 | 7 | 3 |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 29 | 18 | 3 | 6 | 16 | 10 | 15 | 5 |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING | 21 | 14 | 3 | 3 | 10 | 10 | 8 | 4 |
| canonical_archetype_id | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 28 | 11 | 5 | 8 | 13 | 9 | 9 | 6 |
| canonical_archetype_id | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 23 | 16 | 2 | 4 | 10 | 10 | 9 | 2 |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C | 21 | 14 | 0 | 6 | 3 | 3 | 3 | 3 |
| canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE | 28 | 11 | 4 | 7 | 9 | 9 | 13 | 0 |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 36 | 23 | 7 | 11 | 17 | 17 | 14 | 9 |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 21 | 15 | 7 | 10 | 0 | 0 | 8 | 3 |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 38 | 19 | 10 | 6 | 10 | 10 | 17 | 9 |
| canonical_archetype_id | C19_BRAND_RETAIL_INVENTORY_MARGIN | 38 | 13 | 4 | 5 | 23 | 17 | 8 | 9 |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 19 | 11 | 6 | 4 | 7 | 0 | 8 | 2 |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 51 | 19 | 12 | 7 | 11 | 14 | 22 | 11 |
| canonical_archetype_id | C22_INSURANCE_RATE_CYCLE_RESERVE | 37 | 12 | 9 | 6 | 10 | 10 | 10 | 11 |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 26 | 14 | 5 | 4 | 0 | 0 | 8 | 5 |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK | 30 | 20 | 8 | 8 | 10 | 10 | 13 | 9 |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 33 | 16 | 7 | 8 | 13 | 7 | 13 | 6 |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 13 | 10 | 5 | 8 | 0 | 0 | 2 | 6 |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION | 39 | 15 | 6 | 10 | 6 | 6 | 20 | 6 |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 26 | 19 | 4 | 8 | 10 | 10 | 10 | 4 |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 60 | 27 | 18 | 11 | 3 | 3 | 26 | 13 |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 81 | 31 | 22 | 27 | 20 | 25 | 16 | 29 |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 97 | 70 | 22 | 29 | 25 | 25 | 35 | 25 |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 41 | 22 | 10 | 10 | 8 | 8 | 16 | 12 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 35 | 29 | 5 | 16 | 0 | 0 | 10 | 18 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 19 | 16 | 1 | 2 | 0 | 0 | 8 | 5 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 30 | 29 | 4 | 11 | 8 | 8 | 9 | 9 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 55 | 47 | 0 | 3 | 51 | 51 | 25 | 2 |
