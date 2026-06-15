# V12 Coverage Matrix

v12 coverage는 rolling calibration의 근거 장부입니다. active 반영은 검증된 apply_next_patch만 scope 제한으로 적용합니다.

| group | value | rows | symbols | positives | counterexamples | evidence URL pending | source proxy | good Stage2 | bad Stage2 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| global_v12 | all | 11200 | 962 | 1326 | 2385 | 3888 | 3611 | 3017 | 2183 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 3302 | 671 | 187 | 701 | 995 | 981 | 667 | 752 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 1104 | 160 | 205 | 268 | 405 | 370 | 398 | 179 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS | 1175 | 128 | 209 | 298 | 408 | 298 | 410 | 233 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY | 1370 | 153 | 209 | 370 | 520 | 506 | 340 | 268 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE | 715 | 117 | 87 | 159 | 279 | 270 | 197 | 136 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION | 858 | 79 | 110 | 121 | 295 | 259 | 257 | 142 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 719 | 45 | 86 | 91 | 257 | 227 | 220 | 97 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL | 746 | 112 | 91 | 122 | 305 | 281 | 238 | 130 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY | 845 | 112 | 107 | 191 | 268 | 270 | 236 | 176 |
| large_sector_id | L9_CONSTRUCTION_REALESTATE_HOUSING | 366 | 51 | 35 | 64 | 156 | 149 | 54 | 70 |
| canonical_archetype_id | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 188 | 60 | 46 | 31 | 79 | 65 | 85 | 28 |
| canonical_archetype_id | C02_POWER_GRID_DATACENTER_CAPEX | 263 | 44 | 50 | 58 | 50 | 65 | 111 | 44 |
| canonical_archetype_id | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 260 | 30 | 47 | 65 | 121 | 93 | 109 | 29 |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 213 | 21 | 33 | 75 | 84 | 80 | 50 | 33 |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 180 | 54 | 29 | 39 | 71 | 67 | 43 | 45 |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 215 | 58 | 28 | 54 | 72 | 63 | 78 | 39 |
| canonical_archetype_id | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 224 | 54 | 56 | 60 | 76 | 80 | 84 | 42 |
| canonical_archetype_id | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 235 | 63 | 39 | 51 | 118 | 44 | 83 | 38 |
| canonical_archetype_id | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 291 | 77 | 59 | 101 | 73 | 60 | 82 | 57 |
| canonical_archetype_id | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 210 | 68 | 27 | 32 | 69 | 51 | 83 | 57 |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING | 280 | 75 | 30 | 70 | 89 | 90 | 93 | 62 |
| canonical_archetype_id | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 249 | 69 | 43 | 88 | 81 | 83 | 62 | 61 |
| canonical_archetype_id | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 189 | 38 | 24 | 43 | 110 | 103 | 45 | 39 |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C | 251 | 56 | 48 | 77 | 76 | 69 | 16 | 19 |
| canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE | 208 | 60 | 32 | 55 | 81 | 77 | 55 | 39 |
| canonical_archetype_id | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 217 | 63 | 24 | 51 | 104 | 106 | 52 | 46 |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 290 | 47 | 31 | 53 | 94 | 87 | 90 | 51 |
| canonical_archetype_id | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 296 | 58 | 42 | 41 | 105 | 99 | 92 | 56 |
| canonical_archetype_id | C19_BRAND_RETAIL_INVENTORY_MARGIN | 217 | 44 | 26 | 35 | 99 | 86 | 46 | 46 |
| canonical_archetype_id | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 345 | 50 | 42 | 45 | 91 | 74 | 119 | 40 |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 399 | 38 | 44 | 43 | 123 | 100 | 132 | 45 |
| canonical_archetype_id | C22_INSURANCE_RATE_CYCLE_RESERVE | 320 | 20 | 42 | 48 | 134 | 127 | 88 | 52 |
| canonical_archetype_id | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 263 | 38 | 24 | 21 | 81 | 74 | 76 | 43 |
| canonical_archetype_id | C24_BIO_TRIAL_DATA_EVENT_RISK | 239 | 63 | 36 | 41 | 130 | 117 | 74 | 30 |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 244 | 52 | 31 | 60 | 94 | 90 | 88 | 57 |
| canonical_archetype_id | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 327 | 37 | 35 | 58 | 106 | 87 | 97 | 70 |
| canonical_archetype_id | C27_CONTENT_IP_GLOBAL_MONETIZATION | 248 | 40 | 33 | 46 | 78 | 82 | 69 | 52 |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 270 | 52 | 39 | 87 | 84 | 101 | 70 | 54 |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 404 | 59 | 66 | 93 | 164 | 161 | 124 | 87 |
| canonical_archetype_id | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 369 | 51 | 36 | 66 | 156 | 149 | 54 | 70 |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 422 | 155 | 55 | 86 | 174 | 155 | 95 | 89 |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 360 | 66 | 25 | 50 | 114 | 109 | 102 | 66 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 967 | 419 | 67 | 162 | 286 | 286 | 203 | 227 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 556 | 310 | 20 | 93 | 99 | 108 | 114 | 67 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 580 | 354 | 12 | 193 | 177 | 177 | 88 | 137 |
| canonical_archetype_id | R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 411 | 274 | 5 | 114 | 145 | 146 | 65 | 166 |
