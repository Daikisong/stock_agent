# V12 Coverage Matrix

v12 coverage는 rolling calibration의 근거 장부입니다. active 반영은 검증된 apply_next_patch만 scope 제한으로 적용합니다.

| group | value | rows | symbols | positives | counterexamples | evidence URL pending | source proxy | good Stage2 | bad Stage2 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| global_v12 | all | 527 | 265 | 46 | 97 | 390 | 258 | 182 | 153 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 6 | 6 | 2 | 4 | 6 | 6 | 2 | 0 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 83 | 44 | 8 | 19 | 53 | 37 | 47 | 21 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS | 185 | 78 | 17 | 29 | 139 | 63 | 70 | 68 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY | 105 | 36 | 7 | 19 | 65 | 43 | 20 | 23 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE | 30 | 24 | 2 | 6 | 27 | 24 | 11 | 8 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION | 30 | 20 | 2 | 4 | 24 | 18 | 9 | 13 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 12 | 11 | 1 | 2 | 12 | 12 | 3 | 3 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL | 31 | 21 | 3 | 6 | 28 | 22 | 11 | 5 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY | 42 | 28 | 3 | 6 | 33 | 30 | 9 | 12 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING | 3 | 3 | 1 | 2 | 3 | 3 | 0 | 0 |
| canonical_archetype_id | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 31 | 21 | 4 | 5 | 16 | 6 | 20 | 6 |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX | 24 | 15 | 1 | 7 | 12 | 6 | 17 | 4 |
| canonical_archetype_id | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 9 | 8 | 1 | 1 | 9 | 9 | 4 | 3 |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 6 | 5 | 0 | 2 | 6 | 6 | 2 | 3 |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 13 | 10 | 2 | 4 | 10 | 10 | 4 | 5 |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 33 | 19 | 2 | 4 | 21 | 12 | 13 | 11 |
| canonical_archetype_id | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 32 | 22 | 1 | 2 | 20 | 11 | 13 | 14 |
| canonical_archetype_id | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 43 | 26 | 7 | 9 | 40 | 16 | 16 | 15 |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 40 | 30 | 4 | 11 | 34 | 18 | 13 | 16 |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 37 | 18 | 3 | 3 | 24 | 6 | 15 | 12 |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING | 32 | 18 | 1 | 5 | 18 | 12 | 9 | 13 |
| canonical_archetype_id | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 16 | 11 | 1 | 2 | 13 | 10 | 2 | 2 |
| canonical_archetype_id | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 15 | 12 | 1 | 2 | 12 | 9 | 4 | 3 |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C | 39 | 18 | 3 | 8 | 19 | 9 | 4 | 5 |
| canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE | 6 | 6 | 0 | 2 | 6 | 6 | 4 | 1 |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 12 | 10 | 1 | 2 | 12 | 12 | 3 | 4 |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 12 | 9 | 1 | 2 | 9 | 6 | 4 | 3 |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 3 | 3 | 0 | 0 | 3 | 3 | 1 | 1 |
| canonical_archetype_id | C19_BRAND_RETAIL_INVENTORY_MARGIN | 21 | 12 | 2 | 4 | 15 | 9 | 6 | 10 |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 6 | 6 | 0 | 0 | 6 | 6 | 2 | 2 |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 6 | 5 | 0 | 0 | 6 | 6 | 2 | 2 |
| canonical_archetype_id | C22_INSURANCE_RATE_CYCLE_RESERVE | 6 | 6 | 1 | 2 | 6 | 6 | 1 | 1 |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 12 | 9 | 1 | 2 | 9 | 6 | 6 | 3 |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK | 13 | 8 | 1 | 2 | 13 | 10 | 3 | 1 |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 6 | 4 | 1 | 2 | 6 | 6 | 2 | 1 |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 3 | 3 | 0 | 0 | 3 | 3 | 1 | 1 |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION | 21 | 12 | 1 | 2 | 18 | 12 | 4 | 8 |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 18 | 13 | 2 | 4 | 12 | 15 | 4 | 3 |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 3 | 3 | 1 | 2 | 3 | 3 | 1 | 0 |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 3 | 3 | 1 | 2 | 3 | 3 | 0 | 0 |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 3 | 3 | 1 | 2 | 3 | 3 | 1 | 0 |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 3 | 3 | 1 | 2 | 3 | 3 | 1 | 0 |
