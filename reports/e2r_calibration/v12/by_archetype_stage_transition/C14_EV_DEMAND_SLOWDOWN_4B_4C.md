# C14_EV_DEMAND_SLOWDOWN_4B_4C Stage Transition Report

v12 stage transition은 rolling calibration의 근거 장부입니다. Stage2->4B 단순수익률과 4B peak capture를 구분합니다.
case_fixture나 historical research 성공은 live discovery 증명이 아니며, safe patch만 scope 제한으로 반영합니다.

- stage_transition_summary_rows: `62`

| case_id | symbol | archetype | Stage2 entry | Green entry | 4B entry | peak return from Stage2 | 4B peak capture | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| C14_L149_001_LGES_Q4_OPERATING_LOSS_BUT_RELIEF_MFE | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 348500.0 | None | None | no_valid_stage_transition |
| C14_L149_002_SAMSUNG_SDI_Q2_EV_CHASM_STAGED_4B_TO_4C | 006400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 319500.0 | None | None | no_valid_stage_transition |
| C14_L149_003_SKIET_Q2_SEPARATOR_UTILIZATION_HARD_4C_SUCCESS | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_L149_004_ECOPRO_MATERIALS_Q1_LOSS_HIGH_VOLATILITY_FALSE_SHORT | 450080 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 108300.0 | None | None | no_valid_stage_transition |
| C14_L149_005_ECOPROBM_2024_LOSS_BUT_180D_RELIEF_RALLY | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 121200.0 | None | None | no_valid_stage_transition |
| C14_L216_001570_KUMYANG_BATTERY_THEME_PEAK | 001570 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 152200.0 | None | None | no_valid_stage_transition |
| C14_L216_005420_COSMO_RECYCLING_INDEX_SPIKE | 005420 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 64800.0 | None | None | no_valid_stage_transition |
| C14_L216_008730_YULCHON_POUCH_FILM_VISIBILITY_GAP | 008730 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_L216_089980_SANG_A_BATTERY_CAP_DELAYED | 089980 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_L216_093370_FOOSUNG_LIPF6_HALT | 093370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_L216_131400_EV_ADVANCED_MATERIAL_THEME_HALT | 131400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 11660.0 | None | None | no_valid_stage_transition |
| C14_L216_234920_ZAICELL_US_LFP_JV | 234920 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 16250.0 | None | None | 4b_too_early |
| C14_L216_234920_ZAIGLE_LFP_FINANCING_GAP | 234920 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_L216_290670_DAEBO_MAGNETIC_TAKEOVER_PEAK | 290670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 77500.0 | None | None | no_valid_stage_transition |
| C14_L96_093370_1 | 093370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_L96_121600_4 | 121600 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 139800.0 | None | None | no_valid_stage_transition |
| C14_L96_278280_2 | 278280 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_L96_336370_5 | 336370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 19440.0 | None | None | no_valid_stage_transition |
| C14_L96_348370_3 | 348370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 236500.0 | None | None | 66.81 | None | stage2_actionable_best_entry |
| C14_R3L127_003670_20240124 | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 261000.0 | None | None | no_valid_stage_transition |
| C14_R3L127_003670_20240124 | None | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 261000.0 | None | None | 4b_too_early |
| C14_R3L127_278280_20230823 | 278280 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L127_278280_20230823 | None | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L127_336370_20240208 | 336370 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L127_336370_20240208 | None | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L127_393890_20240807 | 393890 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 21000.0 | None | None | no_valid_stage_transition |
| C14_R3L127_393890_20240807 | None | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 21000.0 | None | None | no_valid_stage_transition |
| C14_R3L127_393890_20241122 | 393890 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L127_393890_20241122 | None | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3L136_005070_20240430 | 005070 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 151800.0 | None | None | 19.24 | None | stage2_captured_most_upside |
| C14_R3L136_005070_20240430 | None | C14_EV_DEMAND_SLOWDOWN_4B_4C | 151800.0 | None | None | 19.24 | None | stage2_captured_most_upside |
| C14_R3L136_011790_20240805 | 011790 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 114100.0 | None | None | no_valid_stage_transition |
| C14_R3L136_011790_20240805 | None | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 114100.0 | None | None | no_valid_stage_transition |
| C14_R3L136_020150_20240607 | 020150 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 49200.0 | None | None | no_valid_stage_transition |
| C14_R3L136_020150_20240607 | None | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 49200.0 | None | None | no_valid_stage_transition |
| C14_R3L136_020150_20250124 | 020150 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 23050.0 | None | None | no_valid_stage_transition |
| C14_R3L136_020150_20250124 | None | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 23050.0 | None | None | no_valid_stage_transition |
| C14_R3L136_066970_20240202 | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 145600.0 | None | None | 4b_too_early |
| C14_R3L136_066970_20240202 | None | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 145600.0 | None | None | 4b_too_early |
| C14_R3L136_066970_20240326 | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 183100.0 | None | None | 2.95 | None | stage2_captured_most_upside |
| C14_R3L136_066970_20240326 | None | C14_EV_DEMAND_SLOWDOWN_4B_4C | 183100.0 | None | None | 2.95 | None | stage2_captured_most_upside |
| C14_R3L98_137400_PNT_BACKLOG_LATE_CHASE_20240607 | 137400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 78000.0 | None | None | 14.7436 | None | stage2_actionable_best_entry |
| C14_R3L98_222080_CIS_DOWNSTREAM_INVESTMENT_DELAY_20231228 | 222080 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 11000.0 | None | None | no_valid_stage_transition |
| C14_R3L98_277880_TSI_UNDISCLOSED_CONTRACT_EV_CAPEX_RISK_20240208 | 277880 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 8390.0 | None | None | 10.7271 | None | stage2_actionable_best_entry |
| C14_R3L98_299030_HANATECH_PILOT_PO_OFFSET_20250120 | 299030 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 23200.0 | None | None | 42.4569 | None | stage2_actionable_best_entry |
| C14_R3L98_382840_WONJUN_SINGLE_CUSTOMER_CAPEX_DEPENDENCY_20220825 | 382840 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 33350.0 | None | None | 5.8471 | None | stage2_actionable_best_entry |
| C14_R3_L95_003670_20240425 | 003670 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 280500.0 | None | None | 5.7 | None | stage2_actionable_best_entry |
| C14_R3_L95_006400_20241031 | 006400 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3_L95_247540_20240208 | 247540 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 243500.0 | None | None | 4b_too_early |
| C14_R3_L95_361610_20231106 | 361610 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3_L95_373220_20240426 | 373220 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 372000.0 | None | None | 4b_too_early |
| C14_R3_L97_005070_20240725_COSMO_PROFITABLE_CHASM_HIGH_MAE | 005070 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 130800.0 | None | None | 5.66 | None | stage2_actionable_best_entry |
| C14_R3_L97_011790_20240808_SKC_COPPERFOIL_DELAY_OPTIONALITY_REBOUND | 011790 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 113700.0 | None | None | no_valid_stage_transition |
| C14_R3_L97_020150_20241104_LOTTE_EM_COPPERFOIL_INVENTORY_UTILIZATION_4C | 020150 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3_L97_066970_20240202_LNF_MATERIAL_PRICE_LAG_HIGH_MAE | 066970 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 145600.0 | None | None | no_valid_stage_transition |
| C14_R3_L97_393890_20241115_WCP_SEPARATOR_CHASM_4C | 393890 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | None | None | None | no_valid_stage_transition |
| C14_R3_L99_090470_제이스텍_2024-01-24_C12_BOUNDARY_TO_C14 | 090470 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 10200.0 | None | None | no_valid_stage_transition |
| C14_R3_L99_101360_에코앤드림_2025-04-14_C12_BOUNDARY_TO_C14 | 101360 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 28600.0 | None | None | 1.3986 | None | stage2_actionable_best_entry |
| C14_R3_L99_137080_나래나노텍_2023-03-30_C12_BOUNDARY_TO_C14 | 137080 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 12250.0 | None | None | no_valid_stage_transition |
| C14_R3_L99_340930_유일에너테크_2024-06-07_C12_BOUNDARY_TO_C14 | 340930 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 3750.0 | None | None | no_valid_stage_transition |
| C14_R3_L99_416180_신성에스티_2024-06-20_C12_BOUNDARY_TO_C14 | 416180 | C14_EV_DEMAND_SLOWDOWN_4B_4C | None | None | 39650.0 | None | None | no_valid_stage_transition |
| C14_R3_L99_419050_삼기에너지솔루션즈_2024-12-05_C12_BOUNDARY_TO_C14 | 419050 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 1850.0 | None | None | 41.3514 | None | stage2_actionable_best_entry |
