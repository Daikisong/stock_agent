# V12 Coverage Matrix

v12 coverage는 rolling calibration의 근거 장부입니다. active 반영은 검증된 apply_next_patch만 scope 제한으로 적용합니다.

| group | value | rows | symbols | positives | counterexamples | evidence URL pending | source proxy | good Stage2 | bad Stage2 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| global_v12 | all | 12453 | 1003 | 1494 | 2624 | 4188 | 5118 | 3327 | 2432 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 3692 | 704 | 220 | 760 | 1051 | 1145 | 776 | 829 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 1347 | 172 | 251 | 304 | 463 | 570 | 456 | 207 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS | 1377 | 138 | 246 | 349 | 468 | 635 | 469 | 284 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY | 1521 | 157 | 238 | 414 | 565 | 683 | 360 | 307 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE | 850 | 149 | 102 | 176 | 282 | 350 | 226 | 170 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION | 889 | 79 | 110 | 133 | 331 | 431 | 266 | 146 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 740 | 45 | 91 | 93 | 269 | 358 | 227 | 98 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL | 781 | 112 | 94 | 133 | 322 | 355 | 246 | 139 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY | 882 | 112 | 107 | 198 | 281 | 399 | 243 | 182 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING | 374 | 51 | 35 | 64 | 156 | 192 | 58 | 70 |
| canonical_archetype_id | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 288 | 89 | 70 | 50 | 105 | 106 | 115 | 43 |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX | 277 | 44 | 50 | 58 | 78 | 139 | 116 | 45 |
| canonical_archetype_id | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 267 | 30 | 47 | 65 | 125 | 151 | 110 | 30 |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 220 | 21 | 33 | 75 | 84 | 85 | 52 | 33 |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 295 | 88 | 51 | 56 | 71 | 89 | 63 | 56 |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 229 | 58 | 32 | 56 | 94 | 93 | 82 | 42 |
| canonical_archetype_id | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 237 | 54 | 56 | 60 | 88 | 138 | 89 | 44 |
| canonical_archetype_id | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 247 | 63 | 39 | 53 | 128 | 155 | 88 | 40 |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 305 | 77 | 59 | 101 | 86 | 123 | 86 | 57 |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 359 | 102 | 60 | 79 | 72 | 126 | 124 | 101 |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING | 286 | 75 | 33 | 73 | 105 | 126 | 94 | 65 |
| canonical_archetype_id | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 256 | 66 | 44 | 88 | 90 | 107 | 62 | 59 |
| canonical_archetype_id | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 307 | 58 | 46 | 81 | 113 | 133 | 63 | 77 |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C | 264 | 56 | 51 | 80 | 88 | 107 | 16 | 19 |
| canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE | 319 | 96 | 47 | 72 | 81 | 100 | 79 | 69 |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 234 | 64 | 24 | 51 | 104 | 109 | 55 | 50 |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 297 | 47 | 31 | 53 | 97 | 141 | 92 | 51 |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 308 | 58 | 42 | 47 | 125 | 159 | 98 | 56 |
| canonical_archetype_id | C19_BRAND_RETAIL_INVENTORY_MARGIN | 223 | 44 | 26 | 41 | 105 | 139 | 46 | 47 |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 358 | 50 | 42 | 45 | 101 | 133 | 122 | 43 |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 413 | 38 | 44 | 43 | 123 | 192 | 136 | 46 |
| canonical_archetype_id | C22_INSURANCE_RATE_CYCLE_RESERVE | 327 | 20 | 47 | 50 | 146 | 166 | 91 | 52 |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 269 | 38 | 27 | 24 | 90 | 90 | 78 | 45 |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK | 253 | 63 | 36 | 41 | 130 | 143 | 78 | 32 |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 259 | 52 | 31 | 68 | 102 | 122 | 90 | 62 |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 334 | 37 | 35 | 65 | 114 | 153 | 98 | 71 |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION | 263 | 40 | 33 | 46 | 81 | 112 | 70 | 56 |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 285 | 52 | 39 | 87 | 86 | 134 | 75 | 55 |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 411 | 59 | 66 | 93 | 169 | 210 | 125 | 87 |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 377 | 51 | 36 | 66 | 156 | 192 | 58 | 70 |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 478 | 180 | 64 | 102 | 174 | 197 | 110 | 105 |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 378 | 67 | 25 | 50 | 114 | 137 | 108 | 67 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 1023 | 430 | 72 | 172 | 315 | 336 | 210 | 234 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 619 | 326 | 29 | 104 | 106 | 129 | 129 | 73 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 715 | 394 | 15 | 202 | 189 | 189 | 127 | 170 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 473 | 299 | 12 | 127 | 153 | 157 | 92 | 180 |
