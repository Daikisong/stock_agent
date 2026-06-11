# V12 Coverage Matrix

v12 coverage는 rolling calibration의 근거 장부입니다. active 반영은 검증된 apply_next_patch만 scope 제한으로 적용합니다.

| group | value | rows | symbols | positives | counterexamples | evidence URL pending | source proxy | good Stage2 | bad Stage2 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| global_v12 | all | 2416 | 443 | 45 | 395 | 1506 | 1340 | 562 | 526 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 859 | 213 | 12 | 104 | 449 | 430 | 182 | 191 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 209 | 63 | 0 | 44 | 142 | 136 | 55 | 32 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS | 108 | 48 | 0 | 40 | 108 | 58 | 54 | 6 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY | 209 | 43 | 12 | 76 | 153 | 146 | 43 | 47 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE | 226 | 70 | 1 | 23 | 130 | 130 | 59 | 62 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION | 225 | 47 | 7 | 16 | 145 | 121 | 58 | 39 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 139 | 29 | 7 | 23 | 96 | 72 | 22 | 18 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL | 174 | 53 | 1 | 22 | 142 | 117 | 45 | 54 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY | 182 | 69 | 2 | 33 | 103 | 99 | 34 | 55 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING | 85 | 20 | 3 | 14 | 38 | 31 | 10 | 22 |
| canonical_archetype_id | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 19 | 16 | 0 | 0 | 19 | 19 | 5 | 5 |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX | 10 | 10 | 0 | 0 | 0 | 10 | 3 | 0 |
| canonical_archetype_id | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 62 | 16 | 0 | 12 | 46 | 38 | 23 | 2 |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 71 | 16 | 0 | 32 | 40 | 36 | 17 | 13 |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 47 | 21 | 0 | 0 | 37 | 33 | 7 | 12 |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 17 | 17 | 0 | 17 | 17 | 17 | 11 | 0 |
| canonical_archetype_id | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 18 | 18 | 0 | 0 | 18 | 18 | 12 | 2 |
| canonical_archetype_id | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 50 | 43 | 0 | 0 | 50 | 0 | 18 | 2 |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 10 | 10 | 0 | 10 | 10 | 10 | 3 | 1 |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 13 | 13 | 0 | 13 | 13 | 13 | 10 | 1 |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING | 18 | 18 | 0 | 18 | 18 | 18 | 4 | 5 |
| canonical_archetype_id | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 32 | 20 | 1 | 16 | 24 | 24 | 7 | 13 |
| canonical_archetype_id | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 58 | 24 | 3 | 9 | 50 | 46 | 14 | 10 |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C | 11 | 11 | 0 | 11 | 11 | 11 | 0 | 0 |
| canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE | 73 | 35 | 1 | 16 | 36 | 36 | 20 | 23 |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 82 | 37 | 0 | 3 | 52 | 52 | 17 | 23 |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 71 | 39 | 0 | 4 | 42 | 42 | 22 | 16 |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 97 | 39 | 4 | 2 | 57 | 51 | 22 | 23 |
| canonical_archetype_id | C19_BRAND_RETAIL_INVENTORY_MARGIN | 50 | 34 | 0 | 0 | 38 | 34 | 11 | 5 |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 78 | 34 | 3 | 14 | 50 | 36 | 25 | 11 |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 79 | 23 | 0 | 8 | 56 | 36 | 13 | 10 |
| canonical_archetype_id | C22_INSURANCE_RATE_CYCLE_RESERVE | 60 | 17 | 7 | 15 | 40 | 36 | 9 | 8 |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 48 | 21 | 0 | 0 | 45 | 41 | 14 | 16 |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK | 69 | 34 | 0 | 0 | 59 | 42 | 16 | 17 |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 57 | 25 | 1 | 22 | 38 | 34 | 15 | 21 |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 106 | 30 | 2 | 4 | 59 | 37 | 22 | 30 |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION | 48 | 30 | 0 | 9 | 24 | 34 | 6 | 15 |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 28 | 23 | 0 | 20 | 20 | 28 | 6 | 10 |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 90 | 17 | 8 | 22 | 50 | 47 | 18 | 19 |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 85 | 20 | 3 | 14 | 38 | 31 | 10 | 22 |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 118 | 58 | 9 | 9 | 71 | 51 | 22 | 20 |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 94 | 45 | 0 | 0 | 37 | 38 | 18 | 27 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 153 | 95 | 2 | 38 | 88 | 88 | 23 | 18 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 191 | 113 | 0 | 27 | 99 | 99 | 52 | 26 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 143 | 93 | 0 | 16 | 70 | 70 | 26 | 32 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 160 | 109 | 1 | 14 | 84 | 84 | 41 | 68 |
