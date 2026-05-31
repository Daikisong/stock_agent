# V12 Coverage Matrix

v12 coverage는 rolling calibration의 근거 장부입니다. active 반영은 검증된 apply_next_patch만 scope 제한으로 적용합니다.

| group | value | rows | symbols | positives | counterexamples | evidence URL pending | source proxy | good Stage2 | bad Stage2 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| global_v12 | all | 3148 | 416 | 514 | 598 | 27 | 40 | 945 | 400 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 698 | 190 | 92 | 108 | 0 | 7 | 198 | 129 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 203 | 46 | 71 | 80 | 7 | 10 | 67 | 25 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS | 228 | 34 | 60 | 76 | 0 | 0 | 65 | 17 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY | 381 | 51 | 64 | 85 | 4 | 0 | 96 | 56 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE | 233 | 52 | 47 | 70 | 8 | 4 | 80 | 23 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION | 368 | 36 | 46 | 42 | 0 | 4 | 109 | 45 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 347 | 29 | 32 | 25 | 8 | 8 | 118 | 40 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL | 275 | 39 | 39 | 33 | 0 | 7 | 93 | 16 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY | 305 | 51 | 48 | 55 | 0 | 0 | 104 | 31 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING | 110 | 29 | 15 | 24 | 0 | 0 | 15 | 18 |
| canonical_archetype_id | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 8 | 6 | 5 | 3 | 0 | 3 | 5 | 1 |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX | 49 | 7 | 21 | 19 | 4 | 4 | 24 | 1 |
| canonical_archetype_id | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 74 | 13 | 23 | 27 | 0 | 0 | 30 | 7 |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 53 | 12 | 19 | 26 | 0 | 0 | 5 | 9 |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 19 | 12 | 3 | 5 | 3 | 3 | 3 | 7 |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 34 | 2 | 6 | 7 | 0 | 0 | 9 | 2 |
| canonical_archetype_id | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 56 | 20 | 19 | 20 | 0 | 0 | 20 | 4 |
| canonical_archetype_id | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 66 | 10 | 12 | 21 | 0 | 0 | 21 | 7 |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 50 | 16 | 17 | 22 | 0 | 0 | 6 | 0 |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 22 | 9 | 6 | 6 | 0 | 0 | 9 | 4 |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING | 67 | 20 | 8 | 16 | 0 | 0 | 24 | 5 |
| canonical_archetype_id | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 53 | 16 | 15 | 20 | 0 | 0 | 13 | 2 |
| canonical_archetype_id | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 37 | 7 | 4 | 10 | 0 | 0 | 8 | 9 |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C | 70 | 15 | 17 | 18 | 0 | 0 | 0 | 0 |
| canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE | 56 | 23 | 18 | 18 | 0 | 0 | 20 | 3 |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 52 | 20 | 12 | 26 | 4 | 4 | 14 | 5 |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 125 | 21 | 17 | 26 | 4 | 0 | 46 | 15 |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 108 | 17 | 13 | 14 | 0 | 0 | 31 | 11 |
| canonical_archetype_id | C19_BRAND_RETAIL_INVENTORY_MARGIN | 68 | 12 | 7 | 12 | 0 | 4 | 15 | 14 |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 192 | 18 | 26 | 16 | 0 | 0 | 63 | 20 |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 209 | 22 | 18 | 13 | 0 | 0 | 73 | 20 |
| canonical_archetype_id | C22_INSURANCE_RATE_CYCLE_RESERVE | 138 | 11 | 14 | 12 | 8 | 8 | 45 | 20 |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 130 | 11 | 12 | 7 | 0 | 0 | 36 | 5 |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK | 62 | 16 | 12 | 11 | 0 | 7 | 22 | 3 |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 83 | 17 | 15 | 15 | 0 | 0 | 35 | 8 |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 125 | 13 | 18 | 22 | 0 | 0 | 47 | 17 |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION | 93 | 23 | 17 | 16 | 0 | 0 | 31 | 8 |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 87 | 15 | 13 | 17 | 0 | 0 | 26 | 6 |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 157 | 27 | 22 | 22 | 4 | 0 | 51 | 40 |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 113 | 29 | 16 | 26 | 0 | 0 | 15 | 18 |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 155 | 62 | 29 | 37 | 0 | 7 | 38 | 32 |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 122 | 14 | 13 | 14 | 0 | 0 | 45 | 23 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 368 | 137 | 42 | 41 | 0 | 0 | 104 | 63 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 12 | 12 | 4 | 8 | 0 | 0 | 5 | 3 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 23 | 21 | 1 | 5 | 0 | 0 | 3 | 5 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 12 | 12 | 0 | 0 | 0 | 0 | 3 | 3 |
